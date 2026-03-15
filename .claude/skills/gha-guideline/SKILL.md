---
name: gha-guideline
description: 'GHA × Claude Code ワークフローの権限設計リファレンス。新規ワークフロー作成・既存ワークフローのレビュー時に参照する。'
user-invocable: false
---
# GHA × Claude Code 運用ガイドライン

> **このファイルの位置づけ**
> GitHub Actions で Claude Code（Action / CLI）を使用するワークフローの権限設計リファレンス。
> 新規ワークフロー作成時・既存ワークフローのレビュー時に参照する。

---

## 1. 権限3層モデル

GHA × Claude Code ワークフローには、権限に関わる設定が3層あり、すべてが整合している必要がある。

### 1.1 3層の対応関係テーブル

| 層 | 設定箇所 | 制御対象 | 例 |
|----|---------|---------|-----|
| L1: GHA ジョブ権限 | `permissions:` ブロック | GitHub API へのアクセス（GITHUB_TOKEN のスコープ） | `contents: write`, `pull-requests: write`, `issues: write` |
| L2: Claude Code ツール許可 | Action: `settings.permissions.allow` / CLI: `--allowedTools` | Claude Code が使用できるツール | `Bash(git *)`, `Read`, `Write`, `Edit` |
| L3: プロンプト内の指示 | `prompt:` / `--system-prompt-file` | Claude に実行させる操作の指示 | 「Issue を作成してください」「ファイルを編集してください」 |

### 1.2 整合性チェックポイント

以下の3つの整合性が保たれていることを確認する。

| チェック | 内容 | 不整合時のリスク |
|---------|------|----------------|
| L1 ⊇ L3 | プロンプトで指示する GitHub API 操作に対応する GHA 権限があるか | 実行時に権限エラー（403） |
| L2 ⊇ L3 | プロンプトで指示する操作に対応する Claude Code ツールが許可されているか | Claude がツール使用を拒否される |
| L2 ⊆ 最小権限 | Claude Code のツール許可が必要最小限か（不要なツールが含まれていないか） | セキュリティリスク（意図しない操作の実行） |

**整合性確認の手順**:

1. L3（プロンプト）から必要な操作を洗い出す
2. 各操作に必要な L2（Claude Code ツール）を導出する
3. 各操作に必要な L1（GHA 権限）を導出する
4. L2 が最小権限の原則を満たしているか確認する

---

## 2. 設計判断基準: Claude 委任 vs Shell ステップ

GitHub API 操作（git, gh コマンド等）を Claude に委任するか、ワークフローの shell ステップで実行するかの判断基準。

### 2.1 判断フロー

```
操作は動的な判断を伴うか？
├─ Yes → Claude に委任（L2 で Bash(git/gh *) を許可）
│        例: コミットメッセージの生成、PR 本文の動的構成
└─ No → 操作は固定パターンか？
    ├─ Yes → Shell ステップで実行（Claude の L2 許可不要）
    │        例: git add -A && git commit、git push、gh pr create（テンプレ本文）
    └─ No → 条件分岐が必要か？
        ├─ Yes（GHA の if 条件で表現可能）→ Shell ステップ + GHA 条件分岐
        └─ Yes（Claude の判断が必要）→ Claude に委任
```

### 2.2 パターン別の推奨

| 操作 | 推奨 | 理由 |
|------|------|------|
| git add / commit / push | Shell ステップ | 固定パターン。Claude の判断不要 |
| gh pr create（固定テンプレ） | Shell ステップ | 本文が固定。Shell 変数で十分 |
| gh pr create（動的本文） | Claude 委任 | 作業結果に基づく本文生成が必要 |
| gh issue create / close | Shell ステップ | 固定パターンの場合。Claude 委任は `Bash(gh *)` が必要でリスク増 |
| ファイル編集（内容の判断を伴う） | Claude 委任 | Claude の判断力が必要 |
| ブランチ作成 | Shell ステップ | 固定パターン |

### 2.3 Shell ステップ推奨の利点

- Claude Code のツール許可から `Bash(git *)` / `Bash(gh *)` を除外できる
- 最小権限の原則に沿う
- ワークフローの可読性が向上（操作が明示的）

---

## 3. Claude Code 権限設定パターン

### 3.1 Action の settings JSON 形式

`anthropics/claude-code-action@v1` を使用する場合、`settings` パラメータで権限を設定する。

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    settings: |
      {
        "permissions": {
          "allow": [
            "Bash(git *)",
            "Bash(cp *)",
            "Bash(mkdir *)",
            "Bash(rm *)",
            "Bash(ls *)",
            "Read",
            "Write",
            "Edit",
            "Glob",
            "Grep"
          ]
        }
      }
```

### 3.2 CLI の --allowedTools 形式

`claude` CLI を使用する場合、`--allowedTools` フラグで許可ツールを指定する。

```bash
claude --print \
  --allowedTools "Read" "Write" "Edit" "Glob" "Grep" \
    "Bash(cp *)" "Bash(mkdir *)" "Bash(rm *)" "Bash(ls *)" \
  --max-turns 50 \
  "プロンプトテキスト"
```

**書式の注意点**:
- スペース区切りまたはカンマ区切りで指定可能
- `Bash(command *)` のようにワイルドカードを使用する場合、シェルの glob 展開を避けるためクォートで囲む
- `--dangerously-skip-permissions` との併用は不可（`--allowedTools` を指定すると、指定したツールのみが許可される）

### 3.3 最小権限の原則

ツール許可は必要最小限に設定する。以下のリスクレベルに基づき判断する。

| ツール | リスクレベル | 説明 | 許可の判断基準 |
|--------|-----------|------|--------------|
| `Read` | 低 | ファイル読み取り | ほぼ全ワークフローで必要 |
| `Glob` | 低 | ファイル検索 | ほぼ全ワークフローで必要 |
| `Grep` | 低 | コンテンツ検索 | ほぼ全ワークフローで必要 |
| `Write` | 中 | ファイル作成・上書き | ファイル作成が必要な場合のみ |
| `Edit` | 中 | ファイル編集 | ファイル編集が必要な場合のみ |
| `Bash(cp *)` | 中 | ファイルコピー | テンプレートコピー等で必要 |
| `Bash(mkdir *)` | 中 | ディレクトリ作成 | ディレクトリ構造の作成で必要 |
| `Bash(rm *)` | 中 | ファイル削除 | 処理済みファイルの削除等で必要 |
| `Bash(ls *)` | 低 | ディレクトリ一覧 | ファイル探索で必要 |
| `Bash(echo *)` | 低 | テキスト出力 | デバッグ・一時ファイル作成等 |
| `Bash(git *)` | 高 | Git 操作 | 動的なコミットメッセージ生成等の場合のみ。固定パターンは Shell ステップ推奨 |
| `Bash(gh *)` | 高 | GitHub CLI 操作 | PR/Issue の動的作成等の場合のみ。固定パターンは Shell ステップ推奨 |
| `--dangerously-skip-permissions` | 最高 | 全ツール無制限 | 使用禁止（サンドボックス環境を除く） |

### 3.4 deny リストとの関係

`--disallowedTools`（CLI）や `settings.permissions.deny`（Action）で特定ツールを拒否できる。
`allow` と `deny` の両方が指定された場合、`deny` が優先される。

---

## 4. gh コマンド前提条件チェックリスト

`Bash(gh *)` を Claude に許可する場合、以下の前提条件を確認する。

### 4.1 コマンド別チェックリスト

| コマンド | 前提条件 | エラーパターン | 回避策 |
|---------|---------|-------------|--------|
| `gh pr create` | リモートブランチが push 済みであること | `fatal: the current branch has no upstream branch` | Shell ステップで事前に `git push -u origin <branch>` |
| `gh pr create` | base ブランチと差分があること | `pull request create failed: No commits between...` | 差分チェックを Shell ステップで事前実行 |
| `gh issue create --label <label>` | 指定ラベルがリポジトリに存在すること | `label not found` | ラベル作成を事前に行うか、ラベルなしで作成 |
| `gh issue close <number>` | Issue が open 状態であること | 既に close 済みの場合はエラーにならない（冪等） | 特になし |
| `gh pr list` / `gh issue list` | 特になし | - | - |
| `gh api` | エンドポイントに対応する GHA 権限があること | `HTTP 403` | L1（GHA permissions）を確認 |

### 4.2 GHA 権限（L1）との対応

| gh サブコマンド | 必要な GHA 権限 |
|---------------|---------------|
| `gh pr create` / `gh pr edit` / `gh pr close` | `pull-requests: write` |
| `gh pr list` / `gh pr view` | `pull-requests: read` |
| `gh issue create` / `gh issue edit` / `gh issue close` | `issues: write` |
| `gh issue list` / `gh issue view` | `issues: read` |
| `gh repo clone` | `contents: read` |

### 4.3 認証

GHA 環境では `GITHUB_TOKEN` が自動的に設定されるが、Claude Code に `Bash(gh *)` を許可する場合は `GH_TOKEN` 環境変数を設定する必要がある場合がある。

```yaml
env:
  GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Shell ステップで gh コマンドを使用する場合も同様に `GH_TOKEN` の設定が必要。

---

## 5. 既存ワークフロー権限マトリクス

### 5.1 ワークフロー一覧

| ワークフロー | Claude Code 方式 | トリガー | 用途 |
|-------------|-----------------|---------|------|
| `backlog-auto-execute.yml` | Action + settings JSON | `issues:labeled` | バックログの自動施策化 |
| `daily-triage.yml` | CLI + `--allowedTools` | `schedule` / `workflow_dispatch` | 日次トリアージ |
| `test-permissions.yml` | Action + settings JSON | `workflow_dispatch` | E2E 権限テスト |
| `backlog-candidate-propose.yml` | なし（Shell のみ） | `schedule` / `workflow_dispatch` | バックログ候補の Issue 作成 |
| `initiative-wallbash.yml` | Action + settings JSON | `issues:labeled` / `workflow_dispatch` | Initiative 壁打ちフェーズ（テンプレートコピー・提案作成・壁打ちサマリー投稿） |
| `initiative-execute.yml` | Action + settings JSON | `issue_comment:created` | Initiative 実行フェーズ（計画・実行・評価・ゲート判定） |
| `initiative-close.yml` | Action + settings JSON | `issue_comment:created` | Initiative クローズフェーズ（アーカイブ移動・知見ルーティング・Issue クローズ） |

### 5.2 権限マトリクス

| ワークフロー | GHA permissions | Claude Code ツール許可 | git/gh 操作の実行者 |
|-------------|----------------|----------------------|-------------------|
| `backlog-auto-execute.yml` | contents:write, pull-requests:write, issues:write, id-token:write | Read, Write, Edit, Glob, Grep, Bash(git/cp/mkdir/rm/ls *) | git: Claude（Bash(git *)）, gh: Shell ステップ |
| `daily-triage.yml` | contents:write, pull-requests:write | Read, Write, Edit, Glob, Grep, Bash(cp/mkdir/rm/ls *) | git: Shell ステップ, gh: Shell ステップ |
| `test-permissions.yml` | contents:write, pull-requests:write, issues:write, id-token:write | Read, Write, Edit, Glob, Grep, Bash(git/gh/cp/mkdir/rm/ls/echo *) | git: Claude, gh: Claude |
| `backlog-candidate-propose.yml` | issues:write, contents:read | N/A（Claude Code 不使用） | gh: Shell ステップ |
| `initiative-wallbash.yml` | contents:write, pull-requests:write, issues:write, id-token:write | Read, Write, Edit, Glob, Grep, Bash(git/cp/mkdir/rm/ls/cat *) | git: Claude（Bash(git *)）, gh: Shell ステップ |
| `initiative-execute.yml` | contents:write, pull-requests:write, issues:write, id-token:write | Read, Write, Edit, Glob, Grep, Bash(git/cp/mkdir/rm/ls/cat *) | git: Claude（Bash(git *)）, gh: Shell ステップ |
| `initiative-close.yml` | contents:write, pull-requests:write, issues:write, id-token:write | Read, Write, Edit, Glob, Grep, Bash(git/cp/mkdir/rm/ls/cat *) | git: Claude（Bash(git *)）, gh: Shell ステップ |

### 5.3 設計判断の記録

| ワークフロー | 設計判断 | 理由 |
|-------------|---------|------|
| `backlog-auto-execute.yml` | git を Claude に委任、gh を Shell | Claude がブランチ作成・コミットを動的に実行する必要がある。Issue クローズは固定パターンなので Shell |
| `daily-triage.yml` | git/gh ともに Shell | Claude の作業はファイル編集のみ。git commit/push、gh pr create は固定パターンで Shell ステップが実行 |
| `test-permissions.yml` | git/gh ともに Claude に委任 | E2E テスト目的で全権限の動作確認が必要。本番用途ではない |
| `backlog-candidate-propose.yml` | Shell のみ | Claude Code を使用しないワークフロー |
| `initiative-wallbash.yml` | git を Claude に委任、gh を Shell | Claude が施策ブランチ作成・テンプレートコピー・コミットを動的に実行。PR 作成・ラベル操作・Issue コメント投稿は固定パターンなので Shell |
| `initiative-execute.yml` | git を Claude に委任、gh を Shell | Claude が計画・実行・評価・ゲート判定を自律実行し、動的にコミット。PR ブランチ取得・ラベル操作・ゲート判定サマリー投稿は固定パターンなので Shell |
| `initiative-close.yml` | git を Claude に委任、gh を Shell | Claude がアーカイブ移動・知見ルーティングを動的に実行し、コミット。Issue クローズ・ラベル操作は固定パターンなので Shell |

---

## 6. 実践知見リファレンス

`claude-code-action` の実装時に判明した制約・ハマりポイント・対策は `refs/claude-code-action/knowledge.md` に蓄積されている。

新規ワークフロー作成時・既存ワークフローのデバッグ時に参照すること。主要なトピック:

- **outputs の仕様**: `result` output は存在しない。execution_file のフォールバックパス
- **permission パターンマッチ**: フラグ付きコマンド（`cp -r` 等）の別途 allow が必要
- **スコープ制御**: Claude が CLAUDE.md/.claude/skills/ を読み込んでプロンプト範囲を超える問題と対策
- **allowed_bots**: `workflow_dispatch` 経由での actor 認証
- **破壊的操作の防止**: `git rebase`/`git reset --hard` のプロンプトベース禁止

### 知見の追記ルール

GHA ワークフローの作成・修正・デバッグで新たな制約・ハマりポイント・対策が判明した場合、`refs/claude-code-action/knowledge.md` の「蓄積された知見」テーブルに追記すること。

- 連番（#）を振り、施策名・日付・カテゴリ・内容を記入する
- 詳細な説明が必要な場合は「知見の詳細」セクションにサブセクションを追加する
- カテゴリ: `API仕様` / `権限` / `認証` / `前提条件` / `スコープ制御` / `安全性` / `ターン消費` / `GHA設定` / `その他`

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.github/workflows/daily-triage.yml` | 権限設定パターン（セクション3）の変更が daily-triage の設定に影響する場合 |
| `.github/workflows/backlog-auto-execute.yml` | 権限マトリクス（セクション5）の更新が必要な場合 |
| `.github/workflows/test-permissions.yml` | 権限マトリクス（セクション5）の更新が必要な場合 |
| `.github/workflows/initiative-wallbash.yml` | 権限マトリクス（セクション5）の更新が必要な場合 |
| `.github/workflows/initiative-execute.yml` | 権限マトリクス（セクション5）の更新が必要な場合 |
| `.github/workflows/initiative-close.yml` | 権限マトリクス（セクション5）の更新が必要な場合 |
| `docs/workflow.md` | 新規スキル追加のため、スキル一覧セクションの更新が必要 |
| `refs/claude-code-action/knowledge.md` | 実践知見の蓄積先。セクション6で参照 |

---

**作成日**: 2026-03-14
**関連施策**: `sessions/initiatives/gha-claude-code-guidelines/`
