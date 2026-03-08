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
      "Write(./.env*)", "Write(./secrets/**)"
    ]
  }
}
```

### 適用範囲

| 環境 | allow リスト | deny リスト | 備考 |
|------|------------|-----------|------|
| Claude Code CLI（対話型） | 有効 | 有効 | ユーザーに許可プロンプトが表示される |
| Claude Code CLI + Task ツール（フォアグラウンド） | 継承・有効（公式ドキュメントに基づく） | 継承・有効 | 親セッションの設定を引き継ぐ |
| Claude Agent SDK 経由 | 動作未確認 | 動作未確認 | 実機検証では機能していなかった（注意事項参照） |

### 注意事項: 環境差異

2026-03-08 の実機検証（T-001）で以下が判明:
- Claude Agent SDK 経由のサブエージェント環境では、deny リストに含まれるコマンド（`rm -rf` 等）が拒否されず実行された
- 非 allow リストのコマンド（`date`, `pwd`, `whoami`）も許可プロンプトなしで実行された
- **allow/deny リストによる制御は Claude Code CLI の対話型環境を前提とした仕組みであり、SDK/API 経由の実行では別の制御メカニズムが必要になる可能性がある**

## 3. エージェント定義の `tools` / `disallowedTools` フィールドの役割

### `tools` フィールド（allowlist）

エージェント定義ファイル（例: `.claude/skills/l1-manager/agents/l2-worker.md`）のフロントマターに設定する。

```yaml
---
tools: ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]
---
```

- Task ツールでサブエージェントを起動する際、このリストに含まれるツールのみが利用可能になる
- 未指定のツールはサブエージェント内で利用不可となる（CLI 環境での期待動作）

### `disallowedTools` フィールド（denylist）

```yaml
---
disallowedTools: ["WebSearch", "WebFetch"]
---
```

- 明示的に利用を禁止するツールを指定する
- `tools` と `disallowedTools` を同時に指定した場合、`disallowedTools` が優先される

### 実機検証結果（T-002）

- Claude Agent SDK 環境では `tools` フィールドによるツール制限は機能していなかった
- `tools` に含まれていない WebSearch, WebFetch, TodoWrite 等も全て利用可能だった
- **`tools` フィールドは Claude Code CLI の Task ツール起動時にのみ適用される制限と推測される**

## 4. フォアグラウンド vs バックグラウンド実行時の挙動差

### フォアグラウンド実行（Task ツール）

- **本PJの標準方式**: L1 が Task ツールで L2-worker / L2-evaluator を起動
- 親セッションの allow/deny リストを継承
- 親セッションが完了を待つ（同期実行）
- エージェント定義の `tools` / `disallowedTools` による追加制限が可能

### バックグラウンド実行（`run_in_background`）

- Bash ツールの `run_in_background` パラメータで起動する非同期実行
- **起動前にプリアプルーブ（pre-approve）が必要**
- プリアプルーブで許可されていない操作は**自動拒否**される（ユーザーに確認を求められないため）
- 本PJでは使用していない

### 比較表

| 項目 | フォアグラウンド（Task） | バックグラウンド（run_in_background） |
|------|----------------------|-----------------------------------|
| 同期/非同期 | 同期（親が待つ） | 非同期（親は待たない） |
| 権限継承 | 親の allow/deny を継承 | プリアプルーブで個別許可 |
| 未許可操作 | 許可プロンプト表示（CLI環境） | 自動拒否 |
| 本PJでの利用 | あり（L2 起動） | なし |

## 5. 本プロジェクトにおける推奨設定と注意点

### 現在の構成の評価

本PJの L2 サブエージェントは以下の構成で運用されている:
- **起動方式**: Task ツール（フォアグラウンド）
- **エージェント定義の tools**: `["Read", "Write", "Edit", "Glob", "Grep", "Bash"]`
- **settings.json**: allow/deny リストが設定済み

### 推奨事項

1. **settings.json の deny リストは維持する**: CLI 対話型環境でのセーフガードとして有効。SDK 環境で機能しないことは認識した上で、CLI 環境での安全策として維持する

2. **エージェント定義の `tools` フィールドは維持する**: 最小権限の原則を文書として明示する意味がある。L2-worker に WebSearch 等が不要なことを明示することで、意図の文書化となる

3. **`disallowedTools` の追加は現時点では不要**: `tools` フィールドで allowlist を指定済みのため、重複して denylist を設定する必要性は低い

4. **バックグラウンド実行を導入する場合**: プリアプルーブの設定を慎重に行うこと。未許可操作が自動拒否されるため、必要な操作を事前に網羅する必要がある

### 注意点

- **deny リストは絶対的な安全策ではない**: SDK/API 環境では機能しない可能性があるため、deny リストのみに依存したセキュリティ設計は避けること
- **環境差異を意識する**: Claude Code CLI と Claude Agent SDK では権限モデルの挙動が異なる。本ガイドの検証結果は特定の環境条件下でのものであり、環境が変わると挙動が変わる可能性がある
- **`bypassPermissions` の利用は慎重に**: 親セッションを `bypassPermissions` にすると、全サブエージェントも全ツール承認となり、`tools` フィールドの制限が無効化される

---
**作成日**: 2026-03-08
**関連施策**: `sessions/initiatives/subagent-permission-model/`
**情報源**: 公式ドキュメント調査（00_proposal.md）+ 実機検証（T-001〜T-003）
