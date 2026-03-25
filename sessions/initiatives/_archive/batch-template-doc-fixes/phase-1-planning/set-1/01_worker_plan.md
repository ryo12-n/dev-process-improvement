# ワーカー計画: batch-template-doc-fixes — Set-1

## 壁打ちフェーズ [2026-03-25 12:00]

### 理解のサマリー
- タスクの目的: 6件のS分類バックログエントリ（BL-054, BL-065, BL-077, BL-045, BL-060, BL-083）をバッチ消化するためのファイルレベルタスク分割を作成する
- スコープ: 08_task_division.md の作成（タスク割当・コンフリクトマトリクス・Wave割当・ドメインエージェント推奨）
- 完了条件: 08_task_division.md が完成し、03_worker_report.md に計画レポートが記載されている

### 前提条件チェック
- [x] 施策計画（02_plan.md）の内容を理解: 理解済み
- [x] 提案書（01_proposal.md）の確認: 確認済み
- [x] 変更対象ファイル群の特定: 特定済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：計画開始

---

## 分析計画サマリ

### 調査結果

#### グループ A: docs/workflow.md 拡充（BL-054 + BL-065）
- `docs/workflow.md`（1184行）には既に「GHA Initiative スキル」セクション（L482-549）が存在する
- BL-054 の課題「initiative GHA ワークフロー記述がない」は起票後に解消された可能性がある。ワーカーは現状を確認し、不足があれば追加する方針
- BL-065 のリファレンス系スキル一覧は未記載。`user-invocable: false` のスキルは15件存在（builtin-skills-reference, external-repo-cleanup, format-conversion-checklist, gha-close, gha-execute, gha-guideline, gha-question, gha-test, gha-wallbash, manager-common-policy, manager-overview, plugin-reference, rule-change-checklist, session-flow-policy, session-lifecycle-policy）
- GHA スキルとリファレンススキルは性質が異なるため、リファレンスセクションは GHA セクションとは別に追加する

#### グループ B: バックログエントリ旧フォーマット統一（BL-077）
- 対象: BL-036〜BL-047, BL-049 の13件
- 実態: 13件とも既にメタ情報テーブル形式（`## メタ情報` + テーブル）に変換済み
- 不足点: `依存する環境前提` フィールドが空欄、`起票時チェックリスト` セクションが未付与、`関連エントリ` セクションの書式が不統一
- BL-047 は backlog.csv に存在しない（欠番の可能性）。ワーカーは現存確認して存在するもののみ変換
- format-conversion-checklist スキルの適用対象

#### グループ C: チェックリスト型スキルテンプレート（BL-045）
- 対象スキル3件: rule-change-checklist, format-conversion-checklist, repo-sync-checklist
- 共通構成: YAML frontmatter → 位置づけ説明ブロック → チェックリスト本体 → 使い方セクション → 関連ファイル一覧
- repo-sync-checklist は `user-invocable: true` で他2件と異なる点に注意
- `.claude/templates/checklist-skill-template.md` として新規作成

#### グループ D: Claude Code Action バージョン追跡手順（BL-060）
- `docs/claude-code-action-version-tracking.md` を新規作成（運用ガイドカテゴリ）
- CLAUDE.md の docs/ ファイル分類テーブル（L110付近）に行追加が必要

#### グループ E: refs メタ情報テンプレート標準化（BL-083）
- `refs/_knowledge_template.md`（22行）にメタ情報セクション追加
- CLAUDE.md 規定「参照物格納時は用途・有効期限のメタ情報を必ず記載すること」との整合

### タスク分割方針
- グループ A は docs/workflow.md を MODIFY する1タスク
- グループ B は backlog/entries/ の13ファイルを MODIFY する1タスク + バックログエントリの削除（BL-054, BL-065, BL-077, BL-045, BL-060, BL-083 の6件を git rm）+ backlog.csv のステータス更新を1タスク
- グループ C, D, E は各1タスク（それぞれ独立ファイルの CREATE）
- グループ D は CLAUDE.md の MODIFY も含む
- バックログエントリ削除は全グループの作業完了後に実施（Wave 2）
