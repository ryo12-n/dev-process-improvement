# 実施計画: テンプレート構造統一改修

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | ポリシー・スキル定義の更新 | 全対象ファイルが新テンプレート構造を反映 |
| 2 | 評価 | 変更の整合性・網羅性が確認済み |

## 変更対象ファイル一覧

### 主要変更対象（ポリシー・スキル定義）

| # | ファイル | 変更内容 |
|---|---------|---------|
| 1 | `.claude/skills/session-lifecycle-policy/SKILL.md` | §1.4.3 Initiative テンプレート定義を 2-phase 構造に改訂。§1.3 記録先ファイル対応テーブルのファイル名・パスを更新 |
| 2 | `.claude/skills/l1-manager/SKILL.md` | ファイル参照パス（00→01, 02→03, 08→05, 09→06 等）、Phase 番号、並列ディスパッチ手順（set コピー方式）、per-worker ファイル参照の除去 |
| 3 | `.claude/skills/l1-manager/agents/l2-plan-worker.md` | 担当ファイルテーブルを phase-1-planning 配下のパスに更新。plan/log/report の3ファイル体系に変更 |
| 4 | `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` | 同上（eval_plan/eval_log/eval_report） |
| 5 | `.claude/skills/l1-manager/agents/l2-worker.md` | 担当ファイルテーブルを phase-2-execution 配下のパスに更新。W_template 参照の除去。plan/log/report の3ファイル体系に変更 |
| 6 | `.claude/skills/l1-manager/agents/l2-evaluator.md` | 同上（eval_plan/eval_log/eval_report） |
| 7 | `.claude/rules/parallel-dev.md` | per-worker ファイル分離パターンを set コピー方式に改訂。W_template 関連セクションの除去 |
| 8 | `docs/workflow.md` | 人間向け可視化の連動更新 |

### スコープ外（本施策では変更しない）

| ファイル | 理由 |
|---------|------|
| `sessions/initiatives/_template/` 実ファイル | 別施策（実ファイル改修）で対応 |
| GHA ワークフロー（`.github/workflows/initiative-*.yml`） | テンプレート実体の変更後に対応 |
| `.claude/skills/gha-wallbash/SKILL.md` | テンプレート実体の変更後に対応 |
| 既存セッションインスタンス | 遡及変更しない方針 |
| `backlog/backlog.csv` | 自動生成されるため直接変更不要 |

## 成功基準（全体）

1. 全8ファイルで旧ファイル名・旧番号への参照が新体系に更新されている
2. 新テンプレート構造（2-phase + ワーカーセット 7ファイル）がポリシーに定義されている
3. parallel-dev.md が set コピー方式を反映し、W_template への参照が除去されている
4. l1-manager SKILL.md の Phase 番号とファイルパスが一貫している
5. 4つのエージェント定義の担当ファイルテーブルが新パスを反映している
6. docs/workflow.md が新構造を反映している

## 新旧ファイル名対応表（ワーカー参照用）

### マネージャールートファイル

| 旧ファイル名 | 新ファイル名 | 備考 |
|-------------|-------------|------|
| `00a_wallbash_log.md` | `00_wallbash_log.md` | 番号昇格 |
| `00_proposal.md` | `01_proposal.md` | 壁打ちの後に移動 |
| `01_plan.md` | `02_plan.md` | 連番 |
| `02_tasks.md` | `03_tasks.md` | 連番 |
| `02b_dispatch_log.md` | `04_dispatch_log.md` | 連番化 |
| `08_gate_review.md` | `05_gate_review.md` | 連番化 |
| `09_cost_record.md` | `06_cost_record.md` | 連番化 |

### ワーカーセットテンプレート（phase-1-planning/_template/）

| 旧ファイル名 | 新ファイル名 | 備考 |
|-------------|-------------|------|
| `03_work_log.md`（壁打ち部分） | `01_worker_plan.md` | タスク理解・不明点解消 |
| `03_work_log.md`（作業メモ部分） | `02_worker_log.md` | 判断背景・つまづき記録 |
| `04_work_report.md` | `03_worker_report.md` | 振り返り・課題発見 |
| `05_eval_plan.md` | `04_eval_plan.md` | 評価観点の整理 |
| （新規） | `05_eval_log.md` | 評価中の判断・メモ |
| `06_eval_report.md` | `06_eval_report.md` | 評価結果・改善点 |
| `07_issues.md` | `07_issues.md` | 課題バッファ |
| `02a_task_division.md` | `08_task_division.md` | phase-1 の成果物（最後） |

### ワーカーセットテンプレート（phase-2-execution/_template/）

| 旧ファイル名 | 新ファイル名 | 備考 |
|-------------|-------------|------|
| `03_work_log.md`（壁打ち部分） | `01_worker_plan.md` | タスク理解・不明点解消 |
| `03_work_log.md`（作業メモ部分） | `02_worker_log.md` | 判断背景・つまづき記録 |
| `04_work_report.md` | `03_worker_report.md` | 振り返り・課題発見 |
| `05_eval_plan.md` | `04_eval_plan.md` | 評価観点の整理 |
| （新規） | `05_eval_log.md` | 評価中の判断・メモ |
| `06_eval_report.md` | `06_eval_report.md` | 評価結果・改善点 |
| `07_issues.md` | `07_issues.md` | 課題バッファ |

### 廃止ファイル

| ファイル | 理由 |
|---------|------|
| `03_work_log_W_template.md` | set コピー方式で不要 |
| `07_issues_W_template.md` | set コピー方式で不要 |
| `02a_task_division.md`（ルート直下） | phase-1-planning/_template/ 内に移動 |

## リソース・前提条件

- session-lifecycle-policy §1.4 の基本モデル定義が確定していること（確認済み）
- 既存セッションインスタンスは変更しない前提

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| ファイル参照の更新漏れ | 中 | 中 | grep でパス参照を網羅的にチェック |
| ポリシーと実ファイルの乖離期間 | 高 | 低 | ポリシーに「移行中」注記を付与。後続施策で速やかに実ファイル改修 |
| 他セッションタイプへの意図しない影響 | 低 | 中 | initiative 固有の変更に限定。共通パターン（§1.4.2 ワーカーセット7ファイル）は新規追加であり既存を壊さない |

---
**作成者**: L1
**作成日**: 2026-03-19
**最終更新**: 2026-03-19
