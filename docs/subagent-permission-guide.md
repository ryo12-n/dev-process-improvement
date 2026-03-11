# サブエージェントの権限許可モデル運用ガイド

## 1. サブエージェントの権限継承モデルの概要

### Permission 評価順序

Claude Code のサブエージェント（Task ツール）で実行されるツール呼び出しは、以下の順序で権限が評価される:

```
Hooks → Deny rules → Permission mode → Allow rules → canUseTool callback
```

1. **Hooks**: カスタムフック（設定されている場合）が最初に評価される
2. **Deny rules**: `.claude/settings.json` の `permissions.deny` に一致する場合、即座に拒否
3. **Permission mode**: セッションの権限モード（`default` / `bypassPermissions`）に基づく判定
4. **Allow rules**: `.claude/settings.json` の `permissions.allow` に一致する場合、許可プロンプトなしで許可
5. **canUseTool callback**: SDK レベルのコールバック（設定されている場合）

### 権限の継承

- サブエージェントは**親セッションの allow/deny リストを継承する**
- 親が `bypassPermissions` モードの場合、子も継承する（ただし `bypassPermissions` では `allowedTools` は無効化され全ツール承認）

## 2. `.claude/settings.json` の allow/deny リストとサブエージェントの関係

### 現在の設定（本プロジェクト）

```json
{
  "permissions": {
    "allow": [
      "Read(*)", "Edit(*)", "Write(*)", "Glob(*)", "Grep(*)",
      "Bash(git *)", "Bash(gh pr *)", "Bash(gh api *)", "Bash(gh run *)",
      "Bash(ls *)", "Bash(ls)", "Bash(wc *)", "Bash(cp *)",
      "Bash(mkdir *)", "Bash(mv *)", "Bash(cat *)", "Bash(head *)",
      "Bash(tail *)", "Bash(find *)", "Bash(echo *)"
    ],
    "deny": [
      "Bash(rm -rf *)", "Bash(cat .env*)", "Bash(cat secrets/*)",
      "Read(./.env*)", "Read(./secrets/**)", "Read(**/*.pem)", "Read(**/*.key)",
      "Edit(./.env*)", "Edit(./secrets/**)", "Edit(**/*.pem)", "Edit(**/*.key)",
      "Write(./.env*)", "Write(./secrets/**)", "Write(**/*.pem)", "Write(**/*.key)"
    ]
  }
}
```

### 適用範囲

| 環境 | allow リスト | deny リスト | 備考 |
|------|------------|-----------|------|
| Claude Code CLI（対話型） | **有効** — 許可プロンプト省略 | **有効** — 即座に拒否 | ユーザーに許可プロンプトが表示される基本環境 |
| Claude Code CLI + Task ツール（サブエージェント） | 継承されるが効果の切り分け困難 *1 | **継承・有効** — 実機検証で確認済み *2 | deny は機能する。allow 外コマンドも自動承認されるため allow の効果は観測不可 |
| Claude Agent SDK 経由 | **機能しない** — 実機検証済み | **機能しない** — 実機検証済み | ISS-045 参照。SDK 環境では別の制御メカニズムが必要 |

*1: Task ツール経由のサブエージェントでは許可プロンプトを表示できないため、deny 以外の全コマンドが自動承認される。allow リストの「プロンプト省略」効果は対話型環境でのみ意味を持つ。

*2: 2026-03-08 の CLI 環境実機検証（施策 `cli-permission-verification` T-001）で全9パターンのうち8パターンを検証し、全て拒否を確認。

### 注意事項: 環境差異

#### SDK 環境での検証結果（2026-03-08、施策 `subagent-permission-model`）
- Claude Agent SDK 経由のサブエージェント環境では、deny リストに含まれるコマンド（`rm -rf` 等）が拒否されず実行された
- 非 allow リストのコマンド（`date`, `pwd`, `whoami`）も許可プロンプトなしで実行された
- **allow/deny リストによる制御は Claude Code CLI の対話型環境を前提とした仕組みであり、SDK/API 経由の実行では別の制御メカニズムが必要になる可能性がある**

#### CLI Task ツール環境での検証結果（2026-03-08、施策 `cli-permission-verification`）
- Task ツール経由のサブエージェント環境では、**deny リストは有効に機能**した（全テストパターンで拒否を確認）
- allow リスト外のコマンド（`date`, `pwd`, `whoami`, `uname`）は許可プロンプトなしで自動承認された
- サブエージェントでは対話的な許可プロンプトを表示できないため、deny 以外は自動承認される動作モデル
- **deny リストが唯一の強制的な制限メカニズム**であり、allow リストはサブエージェント環境では実質的に効果なし

## 3. エージェント定義の `tools` / `disallowedTools` フィールドの役割

### `tools` フィールド（allowlist）

エージェント定義ファイル（例: `.claude/skills/l1-manager/agents/l2-worker.md`）のフロントマターに設定する。

```yaml
---
tools: ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]
---
```

- Task ツールでサブエージェントを起動する際、このリストに含まれるツールが初期ロードされる
- ただし、**deferred tools（遅延ロードツール）は tools フィールドの制限を受けない**（下記検証結果参照）

### `disallowedTools` フィールド（denylist）

```yaml
---
disallowedTools: ["WebSearch", "WebFetch"]
---
```

- 明示的に利用を禁止するツールを指定する
- `tools` と `disallowedTools` を同時に指定した場合、`disallowedTools` が優先される

### 実機検証結果

#### SDK 環境（施策 `subagent-permission-model` T-002）
- Claude Agent SDK 環境では `tools` フィールドによるツール制限は機能していなかった
- `tools` に含まれていない WebSearch, WebFetch, TodoWrite 等も全て利用可能だった

#### CLI Task ツール環境（施策 `cli-permission-verification` T-004）
- `tools: ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]` の定義に対し、以下を検証:
  - tools リスト内のツール（Read, Write 等）: 全て利用可能 — 期待通り
  - tools リスト外の deferred tools（WebSearch, WebFetch, NotebookEdit, TaskCreate 等）: **全て ToolSearch 経由で発見・ロード・利用可能**
- **`tools` フィールドは初期ロードされるツールセットの定義であり、deferred tools を制限するメカニズムではない**
- `tools` フィールドによる完全なツール制限は、現時点では CLI 環境でも SDK 環境でも実現できない

### tools フィールドの適用範囲（まとめ）

| 環境 | 初期ロードツールの制限 | deferred tools の制限 | 備考 |
|------|-------------------|---------------------|------|
| Claude Code CLI + Task ツール | 適用される | **適用されない** | ToolSearch で迂回可能 |
| Claude Agent SDK | 適用されない | 適用されない | ISS-046 参照 |

## 4. フォアグラウンド vs バックグラウンド実行時の挙動差

### フォアグラウンド実行（Task ツール）

- **本PJの標準方式**: L1 が Task ツールで L2-worker / L2-evaluator を起動
- 親セッションの deny リストを継承（実機検証済み）
- 親セッションが完了を待つ（同期実行）
- deny 以外のコマンドは自動承認（許可プロンプト表示不可のため）
- エージェント定義の `tools` フィールドは初期ツールセットのみに適用（deferred tools は制限外）

### バックグラウンド実行（`run_in_background`）

- Bash ツールの `run_in_background` パラメータで起動する非同期実行
- **起動前にプリアプルーブ（pre-approve）が必要**
- プリアプルーブで許可されていない操作は**自動拒否**される（ユーザーに確認を求められないため）
- 本PJでは使用していない

### 比較表

| 項目 | フォアグラウンド（Task） | バックグラウンド（run_in_background） |
|------|----------------------|-----------------------------------|
| 同期/非同期 | 同期（親が待つ） | 非同期（親は待たない） |
| deny リスト | 継承・有効（実機検証済み） | プリアプルーブで個別許可 |
| 非 deny コマンド | 自動承認 | プリアプルーブ依存 |
| 本PJでの利用 | あり（L2 起動） | なし |

### 再帰的サブエージェント起動

- Task ツール経由のサブエージェント内から、さらにサブエージェントを起動する手段はない
- Task ツール（サブエージェント起動ツール）はサブエージェント内では提供されない
- したがって、再帰的な権限継承の検証は不可（1階層のみ検証済み）

## 5. 本プロジェクトにおける推奨設定と注意点

### 現在の構成の評価

本PJの L2 サブエージェントは以下の構成で運用されている:
- **起動方式**: Task ツール（フォアグラウンド）
- **エージェント定義の tools**: `["Read", "Write", "Edit", "Glob", "Grep", "Bash"]`
- **settings.json**: allow/deny リストが設定済み

### 推奨事項

1. **settings.json の deny リストは維持する**: CLI 対話型環境でのセーフガードとして有効。Task ツール経由のサブエージェントでも有効に機能する（実機検証済み）。SDK 環境で機能しないことは認識した上で、CLI 環境での安全策として維持する

2. **エージェント定義の `tools` フィールドは維持する**: deferred tools の制限はできないが、最小権限の原則を文書として明示する意味がある。L2-worker に WebSearch 等が不要なことを明示することで、意図の文書化となる

3. **`disallowedTools` の追加は現時点では不要**: `tools` フィールドで allowlist を指定済みのため、重複して denylist を設定する必要性は低い。ただし deferred tools を明示的に禁止したい場合は `disallowedTools` の追加を検討する

4. **バックグラウンド実行を導入する場合**: プリアプルーブの設定を慎重に行うこと。未許可操作が自動拒否されるため、必要な操作を事前に網羅する必要がある

### 注意点

- **deny リストが唯一の強制的制限**: Task ツール経由のサブエージェントでは、deny リストのみが強制的な制限として機能する。allow リストはサブエージェント環境では効果なし（全自動承認のため）
- **deny リストは絶対的な安全策ではない**: SDK/API 環境では機能しない可能性があるため、deny リストのみに依存したセキュリティ設計は避けること
- **環境差異を意識する**: Claude Code CLI と Claude Agent SDK では権限モデルの挙動が異なる。本ガイドの検証結果は特定の環境条件下でのものであり、環境が変わると挙動が変わる可能性がある
- **`bypassPermissions` の利用は慎重に**: 親セッションを `bypassPermissions` にすると、全サブエージェントも全ツール承認となり、deny リストも含めて無効化される可能性がある
- **deferred tools は tools フィールドで制限できない**: ToolSearch 経由で遅延ロードされるツール（WebSearch, WebFetch, NotebookEdit 等）は、エージェント定義の tools リストに関係なく利用可能

---
**作成日**: 2026-03-08
**最終更新**: 2026-03-08（CLI 環境実機検証結果を反映）
**関連施策**: `sessions/initiatives/subagent-permission-model/`, `sessions/initiatives/cli-permission-verification/`
**情報源**: 公式ドキュメント調査 + 実機検証（SDK: T-001〜T-003, CLI: T-001〜T-004）
