# 実施計画: knowledge-table-origin-column-backport

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | テンプレート変更・整合性確認 | `08_gate_review.md` の「必須把握事項」テーブルに「発見元」列追加済み、docs/ 影響確認完了 |
| 2 | 評価 | 変更内容が前回施策との一貫性を持ち、テーブル構造が triage と対称的であることを確認 |

## スケジュール

- Phase 1: Worker ディスパッチ後、単一セッションで完了可能な小規模変更
- Phase 2: Worker 完了後、Evaluator が評価

## 成功基準（全体）
1. `sessions/initiatives/_template/08_gate_review.md` の「必須把握事項」テーブルに「発見元」列が追加されている
2. docs/ 可視化文書への影響確認が完了し、変更不要または更新済みである
3. `04_work_report.md` / `06_eval_report.md` の「発見元」列と命名・位置が一致している

## リソース・前提条件
- 前回施策（`_archive/knowledge-table-origin-column-backport/`）の完了確認済み
- `_template/04_work_report.md` および `06_eval_report.md` の「発見元」列が存在することを確認済み
- `_template/08_gate_review.md` の「必須把握事項」テーブルに「発見元」列がないことを確認済み

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| テーブル構造の不一致 | 低 | 低 | work_report/eval_report の列構造を参照して同一フォーマットにする |
| docs/ 整合性漏れ | 低 | 低 | workflow.md を確認し、知見テーブル構造の記載がある場合は更新する |

---
**作成者**: L1
**作成日**: 2026-03-18
**最終更新**: 2026-03-18
