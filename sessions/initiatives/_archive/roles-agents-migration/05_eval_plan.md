# 評価計画: roles/ → .claude/agents/ 移行

## 壁打ちフェーズ [2026-03-08 19:00]

### 理解のサマリー
- 評価の目的: L2-worker が実施した roles/ → .claude/agents/ 移行の品質・網羅性を検証する
- 評価スコープ: T-101〜T-105（移行の網羅性、dispatcher統合品質、agents形式妥当性、知見記録、課題起票）
- 完了条件: 全評価項目の結果が 06_eval_report.md に記録されていること

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク完了、成果物一覧・知見記録あり）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（6つの成功基準が明確に定義されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（ai-driven-dev-patterns リポジトリのブランチ initiative/roles-agents-migration にアクセス可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- ai-driven-dev-patterns リポジトリ（ブランチ: initiative/roles-agents-migration）の移行成果物
- dev-process-improvement 側の作業記録（03_work_log.md, 04_work_report.md）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | 残存参照チェック（T-101-1） | `grep -r 'roles/' --include='*.md'` で docs/design/ 以外にヒットがないことを確認 | ヒット0件 |
| 2 | agents の内容同等性（T-101-2） | 元の roles/*.md と .claude/agents/*.md の diff を比較し、内容・ロジックの変更がないことを確認 | フォーマット変換のみで、ロール定義の内容・ロジックが同等 |
| 3 | rules の網羅性（T-101-3） | common.md のセクション3〜8が .claude/rules/ の3ファイル + commit-message.md にカバーされていることを確認 | セクション3〜8の全内容がいずれかのルールファイルに含まれている |
| 4 | dispatcher 統合品質（T-102） | dev_manager.md の全8セクションが dispatcher SKILL.md に統合されているか確認 | 8セクション全てが存在し、既存の dispatcher 機能（シナリオ判定）も維持 |
| 5 | agents 形式妥当性（T-103） | YAML フロントマターの有効性、tools 制限の適切性、description の適切性を確認 | 全8ファイルに有効なフロントマターがあり、reviewer の tools が制限されていること |
| 6 | 知見記録（T-104） | 06_eval_report.md の「評価中の知見」セクションに記録 | ルール化候補・参考情報の両テーブルに最低1行の記載 |
| 7 | 課題起票・転記（T-105） | 評価中に発見した課題を 07_issues.md に起票、施策横断課題は CSV 転記 | 全課題に転記済み/転記不要の判断が付いている |

## 評価スケジュール
- 評価項目 1〜5: ファイル読み取り・diff 比較による検証
- 評価項目 6: 評価中に随時記録
- 評価項目 7: 評価完了後に起票・転記

## 前提・制約
- ai-driven-dev-patterns の roles/ は git rm 済みのため、main ブランチの git show で元ファイルを参照する
- docs/design/ 配下は歴史的設計書として roles/ 参照が残っていてよい

---
**作成者**: L2（評価）
**作成日**: 2026-03-08
