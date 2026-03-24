# 計画レポート: batch-reference-fix-and-rename — Plan-Worker Set-1

## サマリ

施策の7ファイル操作を4タスク・2 Wave に分割した。`02_plan.md` から重要な差分として、`l2-plan-evaluator.md` が PR #167 で廃止済みであり、MODIFY 対象が3箇所から1箇所に縮小されることを発見した。全タスクが S 複雑度のため、1ワーカー逐次実行を推奨する。ファイル競合はゼロ。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| - | 壁打ちフェーズ・調査 | 10分 | 完了 | l2-plan-evaluator.md 廃止を発見 |
| - | 08_task_division.md 作成 | 10分 | 完了 | 4タスク・2 Wave に分割 |
| - | 03_worker_report.md 作成 | 5分 | 完了 | - |

## 成果物一覧
- `phase-1-planning/set-1/08_task_division.md` — タスク分割（プライマリ成果物）
- `phase-1-planning/set-1/01_worker_plan.md` — 壁打ちフェーズ記録（L1 が事前記入済み、追記なし）
- `phase-1-planning/set-1/02_worker_log.md` — 作業履歴
- `phase-1-planning/set-1/03_worker_report.md` — 本レポート

## 発生した課題
なし（07_issues.md への起票なし）

## 計画中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | ファイル廃止時にバックログエントリ・SC リファレンスの記載が残存しやすい | Grep 調査 | `session-consistency-reference.md`、`backlog/` | `l2-plan-evaluator.md` は PR #167 で廃止されたが、SC リファレンスや `02_plan.md` 作成時のバックログエントリにはまだ旧ファイル名が記載されていた。T-002 で作成する `rename-reference-check.md` のスコープに「ファイル廃止（DELETE）時」も含めると、この種の残存を防止できる |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | `session-consistency-reference.md` の壊れた参照記録は SC スキャンの自動更新で解消される想定 | Grep 調査 | SC マネージャーのリファレンスデータのため、本施策では手動修正せず次回スキャンに委ねる判断とした。SC スキャンが長期間実行されない場合は陳腐化する可能性あり |

## 所感・次フェーズへの申し送り
- 全タスクが機械的・軽量（S 複雑度）のため、1ワーカーで Wave 1 → Wave 2 を逐次実行すれば30分以内に完了する見込み
- T-004（rule-change-checklist）では `docs/workflow.md` への影響がないことの確認が重要。`01_proposal.md` の「やらないこと」に記載済みだが、`.claude/rules/` への新規ファイル追加が workflow フローに影響しないことを実際に検証すること
- `backlog/backlog.csv` が自動生成かどうかの確認を T-003 実行時に行うこと

---
**作成者**: L2（計画ワーカー）
**作成日**: 2026-03-24
