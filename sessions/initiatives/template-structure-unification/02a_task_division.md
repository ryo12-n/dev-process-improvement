# File-Level Task Division: テンプレート構造統一改修

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 2
- Dependency graph: T-001 は基盤定義（session-lifecycle-policy）であり、他タスクが参照する可能性がある。T-002（l1-manager）は T-001 の §1.4.3 を前提とする。T-003〜T-006（エージェント定義4件）は互いに独立。T-007（parallel-dev.md）は独立。T-008（docs/workflow.md）は T-001〜T-007 の結果を反映する必要があるため最後。

## Task Assignments

### T-001: session-lifecycle-policy §1.4.3 を 2-phase 構造に改訂

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/session-lifecycle-policy/SKILL.md`
  - §1.4.1 マネージャールートファイルテーブル: 旧ファイル名を新ファイル名に更新（`00a_wallbash_log.md` → `00_wallbash_log.md`（番号 00）、`00_proposal.md` → `01_proposal.md`、`01_plan.md` → `02_plan.md`、`02_tasks.md` → `03_tasks.md`、`02a_task_division.md` → 削除（phase-1 内に移動）、`02b_dispatch_log.md` → `04_dispatch_log.md`、`08_gate_review.md` → `05_gate_review.md`、`09_cost_record.md` → `06_cost_record.md`）
  - §1.4.2 ワーカーセットテンプレートを initiative 向け 7 ファイル（worker_plan/worker_log/worker_report/eval_plan/eval_log/eval_report/issues）に更新。既存の 3-phase 向けテーブル（01_tasks〜07_issues）は別パターンとして残す
  - §1.4.3 Initiative テンプレートを 2-phase 構造（phase-1-planning / phase-2-execution）に全面改訂。15 ファイルフラット構造 → マネージャールート + 2-phase のネスト構造に変更。W_template 行を削除
  - §1.3 記録先ファイル対応テーブル（パターン A）: 旧ファイル名を新パスに更新（`00_proposal.md` → `01_proposal.md` 等）。壁打ちログの記録先を `00_wallbash_log.md` に更新
- **Read-only dependencies**: `00_proposal.md`（新テンプレート構造の合意内容）、`01_plan.md`（新旧ファイル名対応表）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - §1.4.3 が 2-phase 構造を正確に定義している
  - §1.4.1 の initiative 用マネージャールートファイルが新番号体系を反映
  - §1.4.2 に initiative 向けワーカーセット 7 ファイルのテーブルが追加されている（または既存テーブルと併記）
  - §1.3 パターン A の全ファイル参照が新パスに更新されている
  - W_template 関連の記述が除去されている
  - 「移行中」ステータスの注記が付与されている（ポリシーと実ファイルの乖離期間のため）
- **Estimated complexity**: L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: l1-manager SKILL.md のファイルパス・Phase 番号・並列ディスパッチ手順更新

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`
  - 「セッションライフサイクル todo 登録」セクション: パターン1 の旧ファイル名参照を新名に更新（`00_proposal.md` → `01_proposal.md`、`01_plan.md` → `02_plan.md`、`08_gate_review.md` → `05_gate_review.md`、`02a_task_division.md` → `phase-1-planning/*/08_task_division.md`、`02_tasks.md` → `03_tasks.md`、`09_cost_record.md` → `06_cost_record.md`）
  - 「新施策の開始手順」セクション: `02b_dispatch_log.md` → `04_dispatch_log.md`、`09_cost_record.md` → `06_cost_record.md`
  - 「担当フェーズと成果物」セクション: Phase 番号と各ファイル名を新体系に更新
  - 「Phase 4 並列ディスパッチ手順」セクション: per-worker ファイル作成手順を set コピー方式に全面改訂（`_template/03_work_log_W_template.md` からのコピー → `phase-2-execution/_template/` を `set-N/` にコピー）。W_template 参照を除去
  - 「やらないこと」セクション: 旧ファイル名参照を新名に更新（`03_work_log.md` → `phase-2-execution/set-N/02_worker_log.md` 等）
  - 「L2 壁打ちフェーズへの応答フロー」セクション: 壁打ち記録先を新パスに更新（`03_work_log.md` → `phase-*/set-N/01_worker_plan.md`、`05_eval_plan.md` → `phase-*/set-N/04_eval_plan.md`）
  - 「initiative クローズ手順」セクション: `08_gate_review.md` → `05_gate_review.md`、`09_cost_record.md` → `06_cost_record.md`
  - 「関連ファイル一覧」セクション: テンプレートパス参照の更新
- **Read-only dependencies**: `00_proposal.md`、`01_plan.md`、`.claude/skills/session-lifecycle-policy/SKILL.md`（T-001 の変更後）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**:
  - 全旧ファイル名参照が新名に更新されている
  - Phase 番号が新体系と一貫している
  - 並列ディスパッチ手順が set コピー方式を反映している
  - W_template への参照が除去されている
  - per-worker ファイル（`03_work_log_W<N>.md`、`07_issues_W<N>.md`）への参照が除去されている
- **Estimated complexity**: L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: l2-plan-worker エージェント定義の担当ファイルテーブル更新

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-plan-worker.md`
  - 「担当ファイル」テーブル: 旧ファイル名を phase-1-planning 配下の新パスに更新
    - `00_proposal.md` → `01_proposal.md`（読み取り）
    - `01_plan.md` → `02_plan.md`（読み取り）
    - `02a_task_division.md` → `phase-1-planning/set-N/08_task_division.md`（作成）
    - `03_work_log.md` → `phase-1-planning/set-N/01_worker_plan.md`（壁打ち）+ `phase-1-planning/set-N/02_worker_log.md`（作業履歴）
    - `04_work_report.md` → `phase-1-planning/set-N/03_worker_report.md`（レポート）
    - `07_issues.md` → `phase-1-planning/set-N/07_issues.md`（課題起票）
  - 「作業フロー」セクション: ファイル名参照の更新（壁打ち記録先、成果物名）
  - 「壁打ちフェーズ」セクション: `03_work_log.md` → `01_worker_plan.md` に記録先変更
  - 「作業履歴の書き方」セクション: 記録先を `02_worker_log.md` に変更
  - 「02a_task_division.md のフォーマット」セクション: ファイル名を `08_task_division.md` に変更
  - 「やること」セクション: ファイル名参照の更新
  - 「やらないこと」セクション: `00_proposal.md` → `01_proposal.md`、`01_plan.md` → `02_plan.md`、`02_tasks.md` → `03_tasks.md`、`08_gate_review.md` → `05_gate_review.md` に更新
  - 「関連ファイル一覧」セクション: テンプレートパス参照の更新（`_template/02a_task_division.md` → `_template/phase-1-planning/_template/08_task_division.md`）
- **Read-only dependencies**: `01_plan.md`（新旧対応表）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 担当ファイルテーブルが plan/log/report の3ファイル体系を反映している
  - 全旧ファイル名参照が phase-1-planning 配下の新パスに更新されている
  - 壁打ち記録先が `01_worker_plan.md` に変更されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: l2-plan-evaluator エージェント定義の担当ファイルテーブル更新

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-plan-evaluator.md`
  - 「担当ファイル」テーブル: 旧ファイル名を phase-1-planning 配下の新パスに更新
    - `01_plan.md` → `02_plan.md`（読み取り）
    - `02a_task_division.md` → `phase-1-planning/set-N/08_task_division.md`（読み取り）
    - `04_work_report.md` → `phase-1-planning/set-N/03_worker_report.md`（読み取り）
    - `05_eval_plan.md` → `phase-1-planning/set-N/04_eval_plan.md`（作成・編集）
    - `06_eval_report.md` → `phase-1-planning/set-N/06_eval_report.md`（作成・編集）
    - `07_issues.md` → `phase-1-planning/set-N/07_issues.md`（追記）
  - 「作業フロー」セクション: ファイル名参照の更新（`01_plan.md` → `02_plan.md`、`04_work_report.md` → `03_worker_report.md`、`05_eval_plan.md` → `04_eval_plan.md`、`06_eval_report.md` → `06_eval_report.md` + `05_eval_log.md` 追加）
  - 「壁打ちフェーズ」セクション: `05_eval_plan.md` → `04_eval_plan.md` に記録先変更
  - 「対称性確認テーブル」セクション: ファイル名を新名に更新
  - 「やること」「やらないこと」セクション: ファイル名参照の更新
  - 「関連ファイル一覧」セクション: テンプレートパス参照の更新
- **Read-only dependencies**: `01_plan.md`（新旧対応表）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 担当ファイルテーブルが eval_plan/eval_log/eval_report の3ファイル体系を反映している
  - 全旧ファイル名参照が phase-1-planning 配下の新パスに更新されている
  - 壁打ち記録先が `04_eval_plan.md` に変更されている
  - `05_eval_log.md` への参照が追加されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: l2-worker エージェント定義の担当ファイルテーブル更新

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-worker.md`
  - 「担当ファイル」テーブル: 旧ファイル名を phase-2-execution 配下の新パスに更新
    - `02_tasks.md` → `03_tasks.md`（読み取り）
    - `03_work_log.md` → `phase-2-execution/set-N/01_worker_plan.md`（壁打ち）+ `phase-2-execution/set-N/02_worker_log.md`（作業履歴）
    - `03_work_log_W<N>.md` → 削除（set コピー方式で不要）
    - `04_work_report.md` → `phase-2-execution/set-N/03_worker_report.md`（レポート）
    - `07_issues.md` → `phase-2-execution/set-N/07_issues.md`（課題起票）
    - `07_issues_W<N>.md` → 削除（set コピー方式で不要）
  - 「作業フロー」セクション: 順次/並列の判別ロジックを set コピー方式に全面改訂。Worker ID → set 番号（set-N）に変更。per-worker ファイルへの言及を削除
  - 「壁打ちフェーズ」セクション: `03_work_log.md` / `03_work_log_W<N>.md` → `01_worker_plan.md` に統一
  - 「作業履歴の書き方」セクション: 記録先を `02_worker_log.md` に変更
  - 「やること」セクション: 旧ファイル名・per-worker 参照を新名に更新
  - 「やらないこと」セクション: `00_proposal.md` → `01_proposal.md`、`01_plan.md` → `02_plan.md`、`08_gate_review.md` → `05_gate_review.md` に更新
  - 「関連ファイル一覧」セクション: W_template 参照行を削除、テンプレートパスを更新
- **Read-only dependencies**: `01_plan.md`（新旧対応表）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 担当ファイルテーブルが plan/log/report の3ファイル体系を反映している
  - per-worker ファイル（`03_work_log_W<N>.md`、`07_issues_W<N>.md`）への参照がすべて除去されている
  - Worker ID 判別ロジックが set コピー方式に更新されている
  - 全旧ファイル名参照が phase-2-execution 配下の新パスに更新されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-006: l2-evaluator エージェント定義の担当ファイルテーブル更新

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-evaluator.md`
  - 「担当ファイル」テーブル: 旧ファイル名を phase-2-execution 配下の新パスに更新
    - `01_plan.md` → `02_plan.md`（読み取り）
    - `02_tasks.md` → `03_tasks.md`（読み取り）
    - `04_work_report.md` → `phase-2-execution/set-N/03_worker_report.md`（読み取り）
    - `05_eval_plan.md` → `phase-2-execution/set-N/04_eval_plan.md`（作成・編集）
    - `06_eval_report.md` → `phase-2-execution/set-N/06_eval_report.md`（作成・編集）
    - `07_issues.md` → `phase-2-execution/set-N/07_issues.md`（追記）
  - 「作業フロー」セクション: ファイル名参照の更新。`05_eval_log.md` への参照を追加
  - 「壁打ちフェーズ」セクション: `05_eval_plan.md` → `04_eval_plan.md` に記録先変更
  - 「やること」「やらないこと」セクション: ファイル名参照の更新（`00_proposal.md` → `01_proposal.md`、`01_plan.md` → `02_plan.md`、`08_gate_review.md` → `05_gate_review.md` 等）
  - 「関連ファイル一覧」セクション: テンプレートパス参照の更新
- **Read-only dependencies**: `01_plan.md`（新旧対応表）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 担当ファイルテーブルが eval_plan/eval_log/eval_report の3ファイル体系を反映している
  - 全旧ファイル名参照が phase-2-execution 配下の新パスに更新されている
  - 壁打ち記録先が `04_eval_plan.md` に変更されている
  - `05_eval_log.md` への参照が追加されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-007: parallel-dev.md を set コピー方式に改訂

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/rules/parallel-dev.md`
  - §1 前提条件: 条件3「per-worker ファイル作成済み」→「set ディレクトリ作成済み」（`phase-N-xxx/_template/` を `set-N/` にコピー）に変更
  - §2 per-worker ファイル分離パターン: set コピー方式に全面改訂
    - §2.1: `03_work_log_W<N>.md`、`07_issues_W<N>.md` → `phase-N-xxx/set-N/` のワーカーセット7ファイルに変更
    - §2.2: 分離不要ファイルの記述を更新（set 内で完結するため分離不要の概念自体が変わる）
    - §2.3: 順次ディスパッチ時の扱いを `set-1/` 固定に更新。Worker ID 判別 → set 番号判別に変更
    - W_template 参照をすべて除去
  - §3 Wave 方式の運用ルール:
    - §3.2: Wave ディスパッチ手順を set コピー方式に更新
    - §3.3: 事前検証チェックリストを set ディレクトリ確認に更新
  - §4 成果物統合手順:
    - §4.1: per-worker ファイルの統合 → set 間の課題統合に変更
    - §4.2: 統合後チェックリストを set 方式に更新
- **Read-only dependencies**: `01_plan.md`（新旧対応表）、`00_proposal.md`（set コピー方式の設計）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - per-worker ファイル（`03_work_log_W<N>.md`、`07_issues_W<N>.md`）への参照がすべて除去されている
  - W_template への参照がすべて除去されている
  - set コピー方式（`_template/` → `set-N/`）が明確に定義されている
  - 順次ディスパッチ時は `set-1/` 固定の扱いが記述されている
  - 統合手順が set 間統合に更新されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-008: docs/workflow.md の連動更新

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `docs/workflow.md`
  - 「イニシアティブセッション フロー」セクション（行 8〜100 付近）:
    - 旧ファイル名参照を新名に全面更新（`00_proposal.md` → `01_proposal.md`、`01_plan.md` → `02_plan.md`、`02_tasks.md` → `03_tasks.md`、`02b_dispatch_log.md` → `04_dispatch_log.md`、`09_cost_record.md` → `06_cost_record.md`、`08_gate_review.md` → `05_gate_review.md`、`02a_task_division.md` → `phase-1-planning/set-N/08_task_division.md`）
    - 並列ディスパッチ部分を set コピー方式に更新（`03_work_log_W<N>.md` → set 方式、`07_issues_W<N>.md` → set 方式）
    - per-worker ファイル参照を除去
  - 「フェーズゲートチェック」セクション（行 112〜124 付近）: `08_gate_review.md` → `05_gate_review.md`
  - 「壁打ちフェーズ」セクション（行 130〜132 付近）: `03_work_log.md` → `01_worker_plan.md` / `02_worker_log.md`、`05_eval_plan.md` → `04_eval_plan.md`
  - 「固定タスク」セクション（行 145〜154 付近）: 旧ファイル名を新名に更新
  - 「Initiative ファイル権限マトリクス」セクション（行 1008〜1022 付近）: 旧ファイル名を新名に更新、phase 構造を反映
- **Read-only dependencies**: T-001〜T-007 の変更後の全対象ファイル
- **Prerequisite tasks**: T-001, T-002, T-003, T-004, T-005, T-006, T-007
- **Acceptance criteria**:
  - イニシアティブフロー図の全ファイル名参照が新名に更新されている
  - 並列ディスパッチ部分が set コピー方式を反映している
  - ファイル権限マトリクスが新ファイル構造を反映している
  - per-worker / W_template 参照がすべて除去されている
  - 可視化文書としての正の情報源（T-001〜T-007 の変更結果）との整合性が確認されている
- **Estimated complexity**: L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 | T-006 | T-007 | T-008 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `.claude/skills/session-lifecycle-policy/SKILL.md` | MODIFY | READ | - | - | - | - | - | READ |
| `.claude/skills/l1-manager/SKILL.md` | - | MODIFY | - | - | - | - | - | READ |
| `.claude/skills/l1-manager/agents/l2-plan-worker.md` | - | - | MODIFY | - | - | - | - | READ |
| `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` | - | - | - | MODIFY | - | - | - | READ |
| `.claude/skills/l1-manager/agents/l2-worker.md` | - | - | - | - | MODIFY | - | - | READ |
| `.claude/skills/l1-manager/agents/l2-evaluator.md` | - | - | - | - | - | MODIFY | - | READ |
| `.claude/rules/parallel-dev.md` | - | - | - | - | - | - | MODIFY | READ |
| `docs/workflow.md` | - | - | - | - | - | - | - | MODIFY |
| `00_proposal.md` | READ | READ | - | - | - | - | READ | - |
| `01_plan.md` | READ | READ | READ | READ | READ | READ | READ | - |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。

**競合検出結果**: 各ファイルへの MODIFY は1タスクのみであり、T-001〜T-007 間にファイル書き込み競合はない。T-008（docs/workflow.md）は T-001〜T-007 の変更結果を READ する必要があるため、Wave 2 に分離する。

## Wave Assignment

### Wave 1 (並列実行可)

- T-001, T-003, T-004, T-005, T-006, T-007

T-002 は T-001 に依存するが、依存の性質は「T-001 の変更結果を参照する」であり、T-001 の §1.4.3 定義を前提として l1-manager のファイルパスを更新する。ただし T-002 の参照元情報は `01_plan.md` の新旧対応表で十分把握可能であるため、T-001 と並列実行しても問題ない。T-002 が T-001 の出力ファイルを READ するが MODIFY しないため、ファイル競合は発生しない。

**Wave 1 の並列化判断**: T-001〜T-007 の7タスクはファイル書き込み先が完全に分離されており、全タスクを Wave 1 で並列実行可能。ただし、7 並列は実運用上のワーカー数上限を超える可能性があるため、L1 の判断で Wave 分割を調整してよい。

### Wave 2 (Wave 1 完了後)

- T-008 (depends on T-001, T-002, T-003, T-004, T-005, T-006, T-007)

T-008 は可視化文書であり、正の情報源（T-001〜T-007 の変更結果）との整合性を確保するため、全ポリシー修正完了後に実施する。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業（ポリシー文書のファイル名・パス更新）であり、専門知識は不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 8
- Total waves: 2
- Estimated max parallelism: 7 workers（Wave 1。実運用上は L1 判断で調整）
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-19
