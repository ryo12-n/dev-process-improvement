# File-Level Task Division: initiative-template-2phase-migration

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 1
- Dependency graph: T-001 → T-002 → T-003 → T-004（逐次依存）

T-001（ルートファイル配置）が完了しないと T-002/T-003 の移動元・移動先が混在する。T-004 は全構造変更完了後にのみ実施可能。
小規模施策（S）のため、全タスクを 1 ワーカーで逐次実行するのが最も効率的。

## Task Assignments

### T-001: マネージャールートファイルのリネーム（7件）

旧番号体系のルートファイルを新番号体系にリネームする。

- **Assigned files (CREATE)**:
  - `sessions/initiatives/_template/00_wallbash_log.md`（旧 `00a_wallbash_log.md` のリネーム）
  - `sessions/initiatives/_template/01_proposal.md`（旧 `00_proposal.md` のリネーム）
  - `sessions/initiatives/_template/02_plan.md`（旧 `01_plan.md` のリネーム）
  - `sessions/initiatives/_template/03_tasks.md`（旧 `02_tasks.md` のリネーム）
  - `sessions/initiatives/_template/04_dispatch_log.md`（旧 `02b_dispatch_log.md` のリネーム）
  - `sessions/initiatives/_template/05_gate_review.md`（旧 `08_gate_review.md` のリネーム）
  - `sessions/initiatives/_template/06_cost_record.md`（旧 `09_cost_record.md` のリネーム）
- **Assigned files (MODIFY)**: なし
- **Assigned files (DELETE)**:
  - `sessions/initiatives/_template/00_proposal.md`
  - `sessions/initiatives/_template/00a_wallbash_log.md`
  - `sessions/initiatives/_template/01_plan.md`
  - `sessions/initiatives/_template/02_tasks.md`
  - `sessions/initiatives/_template/02b_dispatch_log.md`
  - `sessions/initiatives/_template/08_gate_review.md`
  - `sessions/initiatives/_template/09_cost_record.md`
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 旧ファイル 7 件が削除されている
  - 新ファイル 7 件が正しい番号で配置されている
  - 各ファイルの内容が旧ファイルと同一である（リネームのみ）
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: phase-1-planning ディレクトリの作成（ゲートファイル + ワーカーセット 8 ファイル）

`phase-1-planning/01_gate.md` と `phase-1-planning/_template/` 配下の計画ワーカーセット 7 ファイル + `08_task_division.md` を作成する。

- **Assigned files (CREATE)**:
  - `sessions/initiatives/_template/phase-1-planning/01_gate.md`（新規作成）
  - `sessions/initiatives/_template/phase-1-planning/_template/01_worker_plan.md`（新規作成: plan-worker 壁打ち）
  - `sessions/initiatives/_template/phase-1-planning/_template/02_worker_log.md`（新規作成: plan-worker 作業ログ）
  - `sessions/initiatives/_template/phase-1-planning/_template/03_worker_report.md`（新規作成: plan-worker レポート）
  - `sessions/initiatives/_template/phase-1-planning/_template/04_eval_plan.md`（新規作成: plan-evaluator 評価計画）
  - `sessions/initiatives/_template/phase-1-planning/_template/05_eval_log.md`（新規作成: plan-evaluator 評価ログ）
  - `sessions/initiatives/_template/phase-1-planning/_template/06_eval_report.md`（新規作成: plan-evaluator 評価レポート）
  - `sessions/initiatives/_template/phase-1-planning/_template/07_issues.md`（新規作成: 課題バッファ）
  - `sessions/initiatives/_template/phase-1-planning/_template/08_task_division.md`（旧 `02a_task_division.md` の移動）
- **Assigned files (DELETE)**:
  - `sessions/initiatives/_template/02a_task_division.md`
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/agents/l2-plan-worker.md`（plan-worker の壁打ちフォーマット参照）
  - `.claude/skills/l1-manager/agents/l2-plan-evaluator.md`（plan-evaluator の壁打ちフォーマット参照）
  - `.claude/skills/session-lifecycle-policy/SKILL.md` §1.4.2（initiative 向けワーカーセット定義）
- **Prerequisite tasks**: T-001（ルートファイルのリネームが完了していること）
- **Acceptance criteria**:
  - `phase-1-planning/01_gate.md` が存在する
  - `phase-1-planning/_template/` に 8 ファイルが配置されている
  - `08_task_division.md` の内容が旧 `02a_task_division.md` と同一
  - `01_worker_plan.md` の壁打ちセクションが `l2-plan-worker.md` の定義と整合している
  - `04_eval_plan.md` の壁打ちセクションが `l2-plan-evaluator.md` の定義と整合している
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

**注意: phase-1 の壁打ちテンプレート内容**

`01_worker_plan.md` は plan-worker 向けの壁打ちテンプレートであり、`l2-plan-worker.md` エージェント定義の壁打ちフォーマットに準拠する。phase-2 の `01_worker_plan.md`（実施ワーカー向け）とは前提条件チェック項目が異なる:

| 項目 | phase-1 (plan-worker) | phase-2 (worker) |
|------|----------------------|-----------------|
| チェック1 | 施策計画（02_plan.md）の内容を理解 | 依存タスクの完了状態 |
| チェック2 | 提案書（01_proposal.md）の確認 | 必要ツール・コマンドの利用可否 |
| チェック3 | 変更対象ファイル群の特定 | 環境の準備状況 |
| チェック4 | - | 外部リポジトリ成果物の記法スタイル確認 |

同様に `04_eval_plan.md` も plan-evaluator 向け（評価対象: `08_task_division.md`）と evaluator 向け（評価対象: `03_worker_report.md`）で前提条件が異なる。ただし、テンプレートレベルではプレースホルダ（`[施策名]`、`YYYY-MM-DD`）のみであり、内容の差異はロール名の表記のみに留まる。

### T-003: phase-2-execution ディレクトリの作成（ゲートファイル + ワーカーセット 7 ファイル）+ 旧ファイル削除

`phase-2-execution/01_gate.md` と `phase-2-execution/_template/` 配下の実施ワーカーセット 7 ファイルを作成し、旧フラット構造の残存ファイルを削除する。

- **Assigned files (CREATE)**:
  - `sessions/initiatives/_template/phase-2-execution/01_gate.md`（新規作成）
  - `sessions/initiatives/_template/phase-2-execution/_template/01_worker_plan.md`（新規作成: worker 壁打ち。旧 `03_work_log.md` の壁打ちセクションを移行）
  - `sessions/initiatives/_template/phase-2-execution/_template/02_worker_log.md`（旧 `03_work_log.md` の作業ログセクションを移行）
  - `sessions/initiatives/_template/phase-2-execution/_template/03_worker_report.md`（旧 `04_work_report.md` の内容を移行）
  - `sessions/initiatives/_template/phase-2-execution/_template/04_eval_plan.md`（旧 `05_eval_plan.md` の内容を移行）
  - `sessions/initiatives/_template/phase-2-execution/_template/05_eval_log.md`（新規作成: evaluator 評価ログ）
  - `sessions/initiatives/_template/phase-2-execution/_template/06_eval_report.md`（旧 `06_eval_report.md` の内容を移行）
  - `sessions/initiatives/_template/phase-2-execution/_template/07_issues.md`（旧 `07_issues.md` の内容を移行）
- **Assigned files (DELETE)**:
  - `sessions/initiatives/_template/03_work_log.md`
  - `sessions/initiatives/_template/03_work_log_W_template.md`
  - `sessions/initiatives/_template/04_work_report.md`
  - `sessions/initiatives/_template/05_eval_plan.md`
  - `sessions/initiatives/_template/06_eval_report.md`
  - `sessions/initiatives/_template/07_issues.md`
  - `sessions/initiatives/_template/07_issues_W_template.md`
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/agents/l2-worker.md`（worker の壁打ちフォーマット参照）
  - `.claude/skills/l1-manager/agents/l2-evaluator.md`（evaluator の壁打ちフォーマット参照）
  - `.claude/skills/session-lifecycle-policy/SKILL.md` §1.4.2（initiative 向けワーカーセット定義）
- **Prerequisite tasks**: T-002（phase-1-planning 作成完了後。ファイル競合はないが、構造の一貫性を保つため逐次実行）
- **Acceptance criteria**:
  - `phase-2-execution/01_gate.md` が存在する
  - `phase-2-execution/_template/` に 7 ファイルが配置されている
  - 旧ファイル 7 件（`03_work_log.md`, `03_work_log_W_template.md`, `04_work_report.md`, `05_eval_plan.md`, `06_eval_report.md`, `07_issues.md`, `07_issues_W_template.md`）が削除されている
  - 移行した各ファイルの内容が旧ファイルから適切に引き継がれている
  - `01_worker_plan.md` の壁打ちセクションが旧 `03_work_log.md` の壁打ちセクションと整合している
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: ポリシー「移行中」注記解除 + l1-manager/SKILL.md 整合確認

`session-lifecycle-policy` §1.4.3 の「移行中」注記を削除し、`l1-manager/SKILL.md` のテンプレートパス参照が新構造と整合していることを確認する。

- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**:
  - `.claude/skills/session-lifecycle-policy/SKILL.md`（§1.4.3 の「移行中」注記バナーを削除。行180付近の `> **移行中（2026-03-20）**: ...` ブロック）
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/SKILL.md`（関連ファイル一覧のテンプレートパス参照を確認）
  - `.claude/skills/l1-manager/agents/l2-worker.md`（`phase-2-execution/_template/` パス参照を確認）
  - `.claude/skills/l1-manager/agents/l2-plan-worker.md`（`phase-1-planning/_template/` パス参照を確認）
  - `sessions/initiatives/_template/`（新構造の実ファイルと §1.4.3 tree 図の一致を最終確認）
- **Prerequisite tasks**: T-003（テンプレート構造変更が全て完了していること）
- **Acceptance criteria**:
  - §1.4.3 の「移行中」注記バナーが削除されている
  - `l1-manager/SKILL.md` の関連ファイル一覧のパスが新テンプレート構造と整合している
  - `l1-manager/SKILL.md` の新施策の開始手順（行81-84）が新構造と整合している
  - 旧ファイル名（`00_proposal.md`, `00a_wallbash_log.md`, `02a_task_division.md` 等）へのスキル・エージェント定義からの参照が残存していないことを grep で確認
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 |
|------|:-----:|:-----:|:-----:|:-----:|
| `_template/00_wallbash_log.md` (new) | CREATE | - | - | - |
| `_template/00a_wallbash_log.md` (old) | DELETE | - | - | - |
| `_template/01_proposal.md` (new) | CREATE | - | - | - |
| `_template/00_proposal.md` (old) | DELETE | - | - | - |
| `_template/02_plan.md` (new) | CREATE | - | - | - |
| `_template/01_plan.md` (old) | DELETE | - | - | - |
| `_template/03_tasks.md` (new) | CREATE | - | - | - |
| `_template/02_tasks.md` (old) | DELETE | - | - | - |
| `_template/04_dispatch_log.md` (new) | CREATE | - | - | - |
| `_template/02b_dispatch_log.md` (old) | DELETE | - | - | - |
| `_template/05_gate_review.md` (new) | CREATE | - | - | - |
| `_template/08_gate_review.md` (old) | DELETE | - | - | - |
| `_template/06_cost_record.md` (new) | CREATE | - | - | - |
| `_template/09_cost_record.md` (old) | DELETE | - | - | - |
| `_template/02a_task_division.md` (old) | - | DELETE | - | - |
| `_template/phase-1-planning/01_gate.md` | - | CREATE | - | - |
| `_template/phase-1-planning/_template/*.md` (8 files) | - | CREATE | - | - |
| `_template/03_work_log.md` (old) | - | - | DELETE | - |
| `_template/03_work_log_W_template.md` (old) | - | - | DELETE | - |
| `_template/04_work_report.md` (old) | - | - | DELETE | - |
| `_template/05_eval_plan.md` (old) | - | - | DELETE | - |
| `_template/06_eval_report.md` (old) | - | - | DELETE | - |
| `_template/07_issues.md` (old) | - | - | DELETE | - |
| `_template/07_issues_W_template.md` (old) | - | - | DELETE | - |
| `_template/phase-2-execution/01_gate.md` | - | - | CREATE | - |
| `_template/phase-2-execution/_template/*.md` (7 files) | - | - | CREATE | - |
| `session-lifecycle-policy/SKILL.md` | - | - | - | MODIFY |
| `l1-manager/SKILL.md` | - | - | - | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, DELETE = 削除, READ = 読取のみ, `-` = 無関係

**競合検出**: なし。各タスクの操作対象ファイルは完全に分離されている。

## Wave Assignment

### Wave 1
- T-001（単独実行）

### Wave 2 (Wave 1 完了後)
- T-002 (depends on T-001)

### Wave 3 (Wave 2 完了後)
- T-003 (depends on T-002)

### Wave 4 (Wave 3 完了後)
- T-004 (depends on T-003)

**注**: 小規模施策のため全タスク逐次実行（1 ワーカー、4 Wave）。ファイル競合は存在しないが、構造変更の一貫性を保つため逐次実行を推奨する。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | テンプレートファイルのリネーム・再配置が主作業のため特殊ドメイン知識不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 4
- Total waves: 4（逐次実行）
- Estimated max parallelism: 1 worker
- Conflict count: 0（全タスク間でファイル操作が分離済み）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-20
