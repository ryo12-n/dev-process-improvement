# 実施計画: initiative-template-2phase-migration

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | テンプレート構造変更 | 新構造が §1.4.3 と一致 |
| 2 | ポリシー注記解除・整合確認 | 「移行中」注記が削除され、関連ファイルが整合 |

## 変更対象ファイル

### 削除対象（旧テンプレートのルートから除去）

| 旧ファイル | 理由 |
|-----------|------|
| `02a_task_division.md` | `phase-1-planning/_template/08_task_division.md` に移動 |
| `02b_dispatch_log.md` | `04_dispatch_log.md` にリネーム |
| `03_work_log.md` | `phase-2-execution/_template/02_worker_log.md` に移動 |
| `03_work_log_W_template.md` | set コピー方式で不要（削除） |
| `04_work_report.md` | `phase-2-execution/_template/03_worker_report.md` に移動 |
| `05_eval_plan.md` | `phase-2-execution/_template/04_eval_plan.md` に移動 |
| `06_eval_report.md` | `phase-2-execution/_template/06_eval_report.md` に移動 |
| `07_issues.md` | `phase-2-execution/_template/07_issues.md` に移動 |
| `07_issues_W_template.md` | set コピー方式で不要（削除） |
| `08_gate_review.md` | `05_gate_review.md` にリネーム |
| `09_cost_record.md` | `06_cost_record.md` にリネーム |

### マネージャールートファイル（新番号体系）

| 新ファイル | 旧ファイル | 変更内容 |
|-----------|-----------|---------|
| `00_wallbash_log.md` | `00a_wallbash_log.md` | リネームのみ |
| `01_proposal.md` | `00_proposal.md` | リネームのみ |
| `02_plan.md` | `01_plan.md` | リネームのみ |
| `03_tasks.md` | `02_tasks.md` | リネームのみ |
| `04_dispatch_log.md` | `02b_dispatch_log.md` | リネームのみ |
| `05_gate_review.md` | `08_gate_review.md` | リネームのみ |
| `06_cost_record.md` | `09_cost_record.md` | リネームのみ |

### 新規作成

| ファイル | 内容 |
|---------|------|
| `phase-1-planning/01_gate.md` | Phase 1 ゲート記録テンプレート |
| `phase-1-planning/_template/01_worker_plan.md` | plan-worker 壁打ち |
| `phase-1-planning/_template/02_worker_log.md` | plan-worker 作業ログ |
| `phase-1-planning/_template/03_worker_report.md` | plan-worker レポート |
| `phase-1-planning/_template/04_eval_plan.md` | plan-evaluator 評価計画 |
| `phase-1-planning/_template/05_eval_log.md` | plan-evaluator 評価ログ |
| `phase-1-planning/_template/06_eval_report.md` | plan-evaluator 評価レポート |
| `phase-1-planning/_template/07_issues.md` | 課題バッファ |
| `phase-1-planning/_template/08_task_division.md` | タスク分割（成果物） |
| `phase-2-execution/01_gate.md` | Phase 2 ゲート記録テンプレート |
| `phase-2-execution/_template/01_worker_plan.md` | worker 壁打ち |
| `phase-2-execution/_template/02_worker_log.md` | worker 作業ログ |
| `phase-2-execution/_template/03_worker_report.md` | worker レポート |
| `phase-2-execution/_template/04_eval_plan.md` | evaluator 評価計画 |
| `phase-2-execution/_template/05_eval_log.md` | evaluator 評価ログ |
| `phase-2-execution/_template/06_eval_report.md` | evaluator 評価レポート |
| `phase-2-execution/_template/07_issues.md` | 課題バッファ |

### ポリシー更新

| ファイル | 変更内容 |
|---------|---------|
| `session-lifecycle-policy/SKILL.md` §1.4.3 | 「移行中」注記を削除 |

## 成功基準（全体）

1. `sessions/initiatives/_template/` のディレクトリ構造が `session-lifecycle-policy` §1.4.3 の tree 図と完全一致する
2. マネージャールートファイル 7 件が新番号体系（`00_wallbash_log.md` 〜 `06_cost_record.md`）で配置されている
3. `phase-1-planning/_template/` に計画ワーカーセット 7 ファイル + `08_task_division.md` が配置されている
4. `phase-2-execution/_template/` に実施ワーカーセット 7 ファイルが配置されている
5. 旧ファイル（`02a_task_division.md`, `03_work_log_W_template.md`, `07_issues_W_template.md` 等）が削除されている
6. `session-lifecycle-policy` §1.4.3 の「移行中」注記が解除されている
7. `l1-manager/SKILL.md` の関連ファイル一覧・テンプレートコピー手順が新構造と整合している

## リソース・前提条件
- 前施策（template-structure-unification）でポリシー・スキル定義の更新が完了していること
- `session-lifecycle-policy` §1.4.2 に initiative 向けワーカーセット 7 ファイルの定義があること

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 旧テンプレートファイル名への残存参照 | 低 | 中 | grep で旧ファイル名の残存参照を検索・確認 |
| ワーカーセットファイルの内容不整合 | 低 | 中 | §1.4.2 の定義と照合 |

### スコープ外

- GHA ワークフロー — BL-119 で対応
- テンプレート内容の改善 — 構造変更のみ

---
**作成者**: L1
**作成日**: 2026-03-20
**最終更新**: 2026-03-20
