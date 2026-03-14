# 改善施策提案: GHA-Claude-Code運用ガイドライン策定

## 背景・課題

GitHub Actions で `claude-code-action` および Claude Code CLI を使用する際、以下の暗黙知が存在し、ワークフロー作成・レビュー時に見落としが発生している。

### 1. 権限の3層構造が未整理

GHA ワークフローには権限に関わる設定が3層あり、それぞれの対応関係が文書化されていない:

| 層 | 設定箇所 | 例 |
|----|---------|-----|
| GHA ジョブ権限 | `permissions:` ブロック | `issues: write`, `pull-requests: write` |
| Claude Code ツール許可 | `settings.permissions.allow` (Action) / `--allowedTools` (CLI) | `Bash(gh *)`, `Bash(git *)` |
| プロンプト内の指示 | `prompt:` | 「Issue を作成してください」 |

### 2. `Bash(gh *)` の要否判断基準がない

- `backlog-auto-execute.yml`: `Bash(gh *)` なし。Issue クローズは shell ステップで実行
- `test-permissions.yml`: `Bash(gh *)` あり。PR/Issue 作成を Claude に委任

どちらの設計パターンが適切かの判断基準がない。

### 3. `gh` コマンドの前提条件が未文書化

- `gh issue create --label` はラベルが事前に存在しないとエラー
- `gh pr create` はリモートブランチが存在しないとエラー
- これらの前提条件がワークフロー設計時に考慮されていない

### 4. daily-triage.yml が `--dangerously-skip-permissions` を使用

最もリスクが高い状態。Claude Code に全ツールへの無制限アクセスを許可している。

## 目標

- GHA × Claude Code ワークフローの権限設計を標準化するリファレンススキルを作成する
- `daily-triage.yml` の `--dangerously-skip-permissions` を適切な権限設定に置換する

## スコープ
### やること
- `.claude/skills/gha-guideline/SKILL.md` にリファレンス型スキルを作成
- 権限3層モデルの対応関係を文書化
- Claude委任 vs shellステップの設計判断基準を明文化
- gh コマンドの前提条件チェックリストを作成
- 既存4ワークフローの権限マトリクスを整理
- `daily-triage.yml` の権限適用（`--dangerously-skip-permissions` → 適切な allowedTools）

### やらないこと
- `backlog-auto-execute.yml`、`backlog-candidate-propose.yml`、`test-permissions.yml` の権限変更
- 新規ワークフローの作成
- GHA 以外の CI/CD ツールのガイドライン

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- ワークフロー作成時の権限設計レビュー基準が明確化される
- `daily-triage.yml` の `--dangerously-skip-permissions` が解消され、最小権限の原則が適用される
- 新規ワークフロー追加時に権限3層の整合性チェックが標準化される

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| allow リスト不足で triage が動かなくなる | 高 | triage.md の全操作を洗い出し済み。評価時に突合検証する |
| CLI の権限設定書式の正確性 | 中 | Claude Code CLI ドキュメントで書式を確認 |

## 壁打ちの背景

- 配置先は当初 `docs/` を検討したが、GHA 作成時に自動で参照されるよう `.claude/skills/` にリファレンス型スキル（`user-invocable: false`）として配置することに決定。`rule-change-checklist` と同じパターン
- `daily-triage.yml` への権限適用はガイドラインの実証を兼ねてこの施策のスコープに含めることに決定（別施策にしない）
- 権限設定は Action の `settings.permissions.allow` パターン（backlog-auto-execute.yml で実証済み）と CLI の `--allowedTools` の両方をカバーする

## 備考・設計パターン

既存ワークフローの権限設定パターン:

| ワークフロー | 方式 | Claude Code ツール許可 |
|---|---|---|
| backlog-auto-execute.yml | Action + settings JSON | `Bash(git/cp/mkdir/rm/ls *)`, Read/Write/Edit/Glob/Grep |
| daily-triage.yml | CLI + `--dangerously-skip-permissions` | 全ツール無制限（要改善） |
| test-permissions.yml | Action + settings JSON | 上記 + `Bash(gh/echo *)` |
| backlog-candidate-propose.yml | Shell のみ（Claude Code なし） | N/A |

---
**起票者**: L1
**起票日**: 2026-03-14
**ステータス**: 実施中
**backlog元ファイル**: GHA-Claude-Code運用ガイドライン策定.md
