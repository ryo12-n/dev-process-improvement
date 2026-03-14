# GHA-Claude-Code運用ガイドライン策定

## メタ情報

| 項目 | 内容 |
|-----|-----|
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | |
| **起票日** | 2026-03-14 |

## 課題・背景

GitHub Actions で `claude-code-action` を使用する際、以下の暗黙知が存在し、ワークフロー作成・レビュー時に見落としが発生している。

### 1. 権限の3層構造が未整理

GHA ワークフローには権限に関わる設定が3層あり、それぞれの対応関係が文書化されていない:

| 層 | 設定箇所 | 例 |
|----|---------|-----|
| GHA ジョブ権限 | `permissions:` ブロック | `issues: write`, `pull-requests: write` |
| Claude Code ツール許可 | `settings.permissions.allow` | `Bash(gh *)`, `Bash(git *)` |
| プロンプト内の指示 | `prompt:` | 「Issue を作成してください」 |

**実例**: `test-permissions.yml` で `permissions: issues: write` を宣言していたが、Claude Code のプロンプトに Issue 操作の指示がなく、権限テストが不完全だった。

### 2. `Bash(gh *)` の要否判断基準がない

- `backlog-auto-execute.yml`: Claude Code に `Bash(gh *)` を与えず、Issue クローズは別の shell ステップで実行
- `test-permissions.yml`: Claude Code に `Bash(gh *)` を与え、PR/Issue 作成を Claude に委任

どちらの設計パターンが適切かの判断基準がない。

### 3. `gh` コマンドの前提条件が未文書化

- `gh issue create --label` はラベルが事前に存在しないとエラー
- `gh pr create` はリモートブランチが存在しないとエラー
- これらの前提条件がワークフロー設計時に考慮されていない

## 期待効果

- GHA × Claude Code ワークフロー作成時のチェックリスト化（権限3層の整合性確認）
- 「Claude に委任する操作」vs「shell ステップで実行する操作」の設計判断基準の明文化
- `gh` コマンドの前提条件リストにより、実行時エラーを事前に防止
- 新規ワークフロー追加時のレビュー基準として機能

## 補足・参考情報

- 関連ワークフロー: `.github/workflows/test-permissions.yml`, `backlog-auto-execute.yml`, `backlog-candidate-propose.yml`
- `test-permissions.yml` の Issue 作成テスト追加時に得られた知見が起点
