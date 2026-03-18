# セッション一貫性チェック事前調査: 2026-03-17

## 現在のセッション定義サーベイ

### マネージャー SKILL.md

- [x] マネージャースキル数：9 件
- [x] user-invocable スキル数：9 件
- [x] 必須セクション完備率：未検証（Phase 1 で確認）
- [x] スキル一覧（名前 / パス）：
  - l1-manager / `.claude/skills/l1-manager/SKILL.md`
  - triage-manager / `.claude/skills/triage-manager/SKILL.md`
  - metacognition-manager / `.claude/skills/metacognition-manager/SKILL.md`
  - sync-manager / `.claude/skills/sync-manager/SKILL.md`
  - backlog-maintenance-manager / `.claude/skills/backlog-maintenance-manager/SKILL.md`
  - automation-manager / `.claude/skills/automation-manager/SKILL.md`
  - config-optimizer-manager / `.claude/skills/config-optimizer-manager/SKILL.md`
  - session-consistency-manager / `.claude/skills/session-consistency-manager/SKILL.md`
  - l1-impl-manager / `.claude/skills/l1-impl-manager/SKILL.md`

### エージェント定義

- [x] エージェント定義数（全スキル合計）：27 件
- [x] ワーカーエージェント数：17 件
- [x] 評価者エージェント数：10 件
- [x] 必須セクション完備率：未検証（Phase 1 で確認）

内訳:
| マネージャー | ワーカー | 評価者 |
|-------------|---------|--------|
| l1-manager | l2-plan-worker, l2-worker (2) | l2-plan-evaluator, l2-evaluator (2) |
| l1-impl-manager | investigation-worker, design-worker, impl-plan-worker, impl-worker (4) | impl-evaluator (1) |
| triage-manager | triage-worker (1) | triage-evaluator (1) |
| metacognition-manager | metacognition-worker (1) | metacognition-evaluator (1) |
| sync-manager | sync-worker (1) | sync-evaluator (1) |
| backlog-maintenance-manager | backlog-maintenance-worker (1) | backlog-maintenance-evaluator (1) |
| automation-manager | automation-worker (1) | automation-evaluator (1) |
| config-optimizer-manager | config-collection-worker, config-analysis-worker, config-proposal-worker (3) | config-optimizer-evaluator (1) |
| session-consistency-manager | sc-collection-worker, sc-analysis-worker, sc-proposal-worker (3) | sc-evaluator (1) |

### テンプレート

- [x] テンプレートディレクトリ数：9 件
- [x] テンプレートファイル総数：約 56 件（サブディレクトリ含む）
- [x] テンプレート一覧：
  - sessions/initiatives/_template/ (13 files: 00_proposal, 00a_wallbash_log, 01_plan, 02_tasks, 02a_task_division, 03_work_log, 03_work_log_W_template, 04_work_report, 05_eval_plan, 06_eval_report, 07_issues, 07_issues_W_template, 08_gate_review)
  - sessions/triage/_template/ (5 files + workers/_template/)
  - sessions/metacognition/_template/ (5 files + workers/_template/)
  - sessions/sync/_template/ (8 files)
  - sessions/backlog-maintenance/_template/ (5 files + workers/_template/)
  - sessions/automation/_template/ (5 files + workers/_template/)
  - sessions/config-optimization/_template/ (5 files + workers/_template/)
  - sessions/session-consistency/_template/ (5 files + workers/_template/)
  - sessions/impl/_template/ (8 files)

### ポリシー準拠状況

- [x] manager-common-policy 適用対象数：9 件（§1 テーブルの行数）
- [x] session-lifecycle-policy 適用マトリクス列数：31 列（L1-manager ～ sc-evaluator）
- [x] commit-message.md セッション種別数：29 件

## リファレンススナップショット確認

- [x] 前回スナップショット日：なし（初回）
- [x] 前回からのセッション定義変更有無：N/A（初回）

## 過去セッション確認

- [x] 前回 session-consistency セッション実施日：なし（初回）
- [x] 前回からの変更点：N/A（初回）

## 調査サマリ・今回の重点

初回実行のため、全8ターゲット（SC-001〜SC-008）をフルスキャンする。特に以下の3点に注力:

- 重点 SC ターゲット1：SC-003（Worker ↔ Evaluator 対称性）— 27 エージェントの対称性を初めて網羅的に検証
- 重点 SC ターゲット2：SC-006（session-lifecycle-policy 適用マトリクス整合）— 31 列 × 9 ステージの大規模マトリクスと実態の整合
- 重点 SC ターゲット3：SC-008（関連ファイル一覧の相互参照整合）— 各 SKILL.md の「関連ファイル一覧」の双方向参照整合

## フェーズ構成の確認

- [x] Phase 1（情報収集）: 実施
- [x] Phase 2（現状分析）: 実施
- [x] Phase 3（改善提案）: 実施

---
**調査者**: session-consistency-manager
**調査日**: 2026-03-17
