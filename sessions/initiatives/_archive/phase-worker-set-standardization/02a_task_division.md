# File-Level Task Division: phase-worker-set-standardization

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 3（Wave 2 で SKILL.md 2ファイル + エージェント定義群を並列可能）
- Dependency graph:
  - T-001（テンプレートディレクトリ操作）は全タスクの前提条件
  - T-002〜T-005（パス参照更新）は T-001 完了後に並列実行可能
  - T-006〜T-007（ポリシー更新）は T-001 完了後に並列実行可能（パス参照更新とは独立）
  - T-008（docs/workflow.md 更新）は T-001 完了後に実行可能
  - T-009（横断検証）は全タスク完了後

## Task Assignments

### T-001: session-consistency テンプレート: workers/ 中間ディレクトリの廃止
- **Assigned files (CREATE)**:
  - `sessions/session-consistency/_template/phase-1-collection/_template/01_tasks.md`
  - `sessions/session-consistency/_template/phase-1-collection/_template/02_scan_plan.md`
  - `sessions/session-consistency/_template/phase-1-collection/_template/03_work_log.md`
  - `sessions/session-consistency/_template/phase-1-collection/_template/04_scan_report.md`
  - `sessions/session-consistency/_template/phase-1-collection/_template/05_eval_plan.md`
  - `sessions/session-consistency/_template/phase-1-collection/_template/06_eval_report.md`
  - `sessions/session-consistency/_template/phase-1-collection/_template/07_issues.md`
  - `sessions/session-consistency/_template/phase-2-analysis/_template/` (同7ファイル)
  - `sessions/session-consistency/_template/phase-3-proposal/_template/` (同7ファイル)
- **Assigned files (MODIFY)**: -（ディレクトリ操作: 旧 `workers/_template/` を `_template/` に移動後、空の `workers/` ディレクトリを削除）
- **Read-only dependencies**:
  - `sessions/session-consistency/_template/phase-1-collection/workers/_template/*` （移動元）
  - `sessions/session-consistency/_template/phase-2-analysis/workers/_template/*` （移動元）
  - `sessions/session-consistency/_template/phase-3-proposal/workers/_template/*` （移動元）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 各 `phase-N-xxx/_template/` に7ファイル（01_tasks〜07_issues）が存在する
  - 旧 `phase-N-xxx/workers/_template/` が削除されている
  - ファイル内容が移動前と同一である
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: config-optimization テンプレート: Phase 内 _template/ 配置への変更
- **Assigned files (CREATE)**:
  - `sessions/config-optimization/_template/phase-1-collection/_template/01_tasks.md`
  - `sessions/config-optimization/_template/phase-1-collection/_template/02_scan_plan.md`
  - `sessions/config-optimization/_template/phase-1-collection/_template/03_work_log.md`
  - `sessions/config-optimization/_template/phase-1-collection/_template/04_scan_report.md`
  - `sessions/config-optimization/_template/phase-1-collection/_template/05_eval_plan.md`
  - `sessions/config-optimization/_template/phase-1-collection/_template/06_eval_report.md`
  - `sessions/config-optimization/_template/phase-1-collection/_template/07_issues.md`
  - `sessions/config-optimization/_template/phase-2-analysis/_template/` (同7ファイル)
  - `sessions/config-optimization/_template/phase-3-proposal/_template/` (同7ファイル)
- **Assigned files (MODIFY)**: -（ディレクトリ操作: ルート `workers/_template/` を各 Phase にコピー後、`workers/` ディレクトリを削除）
- **Read-only dependencies**:
  - `sessions/config-optimization/_template/workers/_template/*` （コピー元）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 各 `phase-N-xxx/_template/` に7ファイル（01_tasks〜07_issues）が存在する
  - 旧 `workers/_template/` ディレクトリが削除されている
  - ファイル内容がコピー元と同一である
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: session-consistency-manager SKILL.md のパス参照更新
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**:
  - `.claude/skills/session-consistency-manager/SKILL.md` — 以下のパス置換:
    - `phase-N-xxx/workers/_template/` → `phase-N-xxx/_template/`（作業フロー §1、セット作成手順、関連ファイル一覧）
    - `phase-N-xxx/workers/set-1/` → `phase-N-xxx/set-1/`（3フェーズオーケストレーション全Phase、担当ファイルテーブル、やらないことセクション）
- **Read-only dependencies**:
  - `sessions/initiatives/phase-worker-set-standardization/01_plan.md`（変更仕様）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**:
  - `grep -c "workers/" SKILL.md` が 0 を返す（SC ターゲット説明等の一般的な用語使用を除く）
  - 全パス参照が `phase-N-xxx/_template/` または `phase-N-xxx/set-1/` パターンに一致
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: config-optimizer-manager SKILL.md のパス参照更新
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**:
  - `.claude/skills/config-optimizer-manager/SKILL.md` — 以下のパス置換:
    - `_template/workers/_template/` → Phase 別 `_template/phase-N-xxx/_template/`（作業フロー §1）
    - `workers/set-1/` → `phase-1-collection/set-1/`（Phase 1 オーケストレーション）
    - `workers/set-2/` → `phase-2-analysis/set-1/`（Phase 2 オーケストレーション）
    - `workers/set-3/` → `phase-3-proposal/set-1/`（Phase 3 オーケストレーション）
    - `workers/set-N/` → `phase-N-xxx/set-1/`（セット作成手順、結果集約、担当ファイルテーブル、やらないことセクション、関連ファイル一覧）
    - `YYYYMMDD/workers/` → Phase 別パス（作業フロー §1: 空ディレクトリ作成の記述を削除し、Phase 内テンプレートコピーの記述に変更）
- **Read-only dependencies**:
  - `sessions/initiatives/phase-worker-set-standardization/01_plan.md`（変更仕様）
- **Prerequisite tasks**: T-002
- **Acceptance criteria**:
  - `grep -c "workers/set-" SKILL.md` が 0 を返す
  - `grep -c "workers/_template" SKILL.md` が 0 を返す
  - 全パス参照が新標準パターン（`phase-N-xxx/_template/` または `phase-N-xxx/set-1/`）に一致
- **Estimated complexity**: L（パス置換箇所が多い）
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: session-consistency エージェント定義（4ファイル）のパス参照更新
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**:
  - `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md` — `phase-1-collection/workers/set-1/` → `phase-1-collection/set-1/`
  - `.claude/skills/session-consistency-manager/agents/sc-analysis-worker.md` — `phase-2-analysis/workers/set-1/` → `phase-2-analysis/set-1/`、`phase-1-collection/workers/set-1/` → `phase-1-collection/set-1/`
  - `.claude/skills/session-consistency-manager/agents/sc-proposal-worker.md` — `phase-3-proposal/workers/set-1/` → `phase-3-proposal/set-1/`、`phase-2-analysis/workers/set-1/` → `phase-2-analysis/set-1/`
  - `.claude/skills/session-consistency-manager/agents/sc-evaluator.md` — `phase-N-xxx/workers/set-1` → `phase-N-xxx/set-1`（パラメータ説明テーブル＋フェーズ別ファイル対応テーブル）
- **Read-only dependencies**:
  - `sessions/initiatives/phase-worker-set-standardization/01_plan.md`（変更仕様）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**:
  - 4ファイルすべてで `grep -c "workers/set-1" <file>` が 0 を返す
  - 担当ファイルテーブル・フローステップ内のパスが新標準に一致
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-006: config-optimizer エージェント定義（4ファイル）のパス参照更新
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**:
  - `.claude/skills/config-optimizer-manager/agents/config-collection-worker.md` — `workers/set-1/` → `phase-1-collection/set-1/`
  - `.claude/skills/config-optimizer-manager/agents/config-analysis-worker.md` — `workers/set-2/` → `phase-2-analysis/set-1/`、`workers/set-1/` → `phase-1-collection/set-1/`
  - `.claude/skills/config-optimizer-manager/agents/config-proposal-worker.md` — `workers/set-3/` → `phase-3-proposal/set-1/`、`workers/set-2/` → `phase-2-analysis/set-1/`
  - `.claude/skills/config-optimizer-manager/agents/config-optimizer-evaluator.md` — `workers/set-N/` → `phase-N-xxx/set-1/`（パラメータテーブル）、フェーズ別ファイル対応テーブルの Set 列を `phase-N-xxx/set-1` に変更
- **Read-only dependencies**:
  - `sessions/initiatives/phase-worker-set-standardization/01_plan.md`（変更仕様）
- **Prerequisite tasks**: T-002
- **Acceptance criteria**:
  - 4ファイルすべてで `grep -c "workers/set-" <file>` が 0 を返す
  - 担当ファイルテーブル・フローステップ内のパスが新標準に一致
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-007: session-flow-policy §4.3 追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**:
  - `.claude/skills/session-flow-policy/SKILL.md` — §4.2 の後に §4.3「3フェーズセッションの標準ディレクトリ構成」を新設。内容:
    - テンプレートパス: `sessions/<session-type>/_template/phase-N-xxx/_template/`（workers/ 不要）
    - ランタイムパス: `sessions/<session-type>/YYYYMMDD/phase-N-xxx/set-1/`
    - ディレクトリ構成図（01_plan.md の標準パターン定義を引用）
    - 既存 §5 の番号は変更不要（§4.3 は §4 配下のサブセクション追加）
- **Read-only dependencies**:
  - `sessions/initiatives/phase-worker-set-standardization/01_plan.md`（標準パターン定義）
  - `sessions/initiatives/phase-worker-set-standardization/00_proposal.md`（背景）
- **Prerequisite tasks**: T-001（テンプレート構成が確定していること）
- **Acceptance criteria**:
  - §4.3 が存在し、標準パターンのディレクトリ構成が記載されている
  - テンプレートパス・ランタイムパスの説明が 01_plan.md と一致
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-008: session-lifecycle-policy §1.3 に config最適化系列を追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**:
  - `.claude/skills/session-lifecycle-policy/SKILL.md` — §1.3 記録先ファイルの対応テーブルに「config最適化系」列を追加。既存の「セッション一貫性系」列と同じ構成（ワーカーセットファイルが各 Phase のセット内に配置されるパターン）
- **Read-only dependencies**:
  - `.claude/skills/config-optimizer-manager/SKILL.md`（担当ファイルテーブル参照）
  - `sessions/initiatives/phase-worker-set-standardization/01_plan.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - §1.3 テーブルに「config最適化系」列が存在する
  - §1.2 の列（co-manager, co-worker, co-evaluator）と §1.3 の列が整合している
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-009: docs/workflow.md の2フロー図更新
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**:
  - `docs/workflow.md` — 以下の2フロー図のパスを更新:
    - L634-686（config最適化フロー）: `workers/set-1/` → `phase-1-collection/set-1/`、`workers/set-2/` → `phase-2-analysis/set-1/`、`workers/set-3/` → `phase-3-proposal/set-1/`
    - L698-750（セッション一貫性フロー）: `phase-N-xxx/workers/set-1/` → `phase-N-xxx/set-1/`
- **Read-only dependencies**:
  - `sessions/initiatives/phase-worker-set-standardization/01_plan.md`（変更仕様）
- **Prerequisite tasks**: T-001, T-002（テンプレート構成確定後）
- **Acceptance criteria**:
  - `grep -c "workers/set-" docs/workflow.md` で該当2フロー図内の旧パスが 0
  - `grep -c "workers/" docs/workflow.md` で該当2フロー図内の旧パスが 0
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-010: 横断検証（旧パス残存チェック + 連動更新確認）
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: -（検証のみ。問題発見時は該当タスクに差し戻し）
- **Read-only dependencies**:
  - `sessions/session-consistency/_template/` 以下全ファイル
  - `sessions/config-optimization/_template/` 以下全ファイル
  - `.claude/skills/session-consistency-manager/SKILL.md`
  - `.claude/skills/session-consistency-manager/agents/*.md`
  - `.claude/skills/config-optimizer-manager/SKILL.md`
  - `.claude/skills/config-optimizer-manager/agents/*.md`
  - `.claude/skills/session-flow-policy/SKILL.md`
  - `.claude/skills/session-lifecycle-policy/SKILL.md`
  - `docs/workflow.md`
- **Prerequisite tasks**: T-001〜T-009 全タスク
- **Acceptance criteria**:
  - `grep -r "workers/set-\|workers/_template" sessions/session-consistency/_template/ sessions/config-optimization/_template/` が空
  - `grep -r "workers/set-\|workers/_template" .claude/skills/session-consistency-manager/ .claude/skills/config-optimizer-manager/` が空（一般用語の "workers" を除く）
  - 全 `phase-N-xxx/_template/` に7ファイルが存在（session-consistency: 3 Phase、config-optimization: 3 Phase、計 6 ディレクトリ）
  - session-flow-policy §4.3 が存在
  - session-lifecycle-policy §1.3 に config最適化系列が存在
  - docs/workflow.md の2フロー図が新パスを使用
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 | T-006 | T-007 | T-008 | T-009 | T-010 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `sessions/session-consistency/_template/phase-1-collection/_template/*` | CREATE | - | - | - | - | - | - | - | - | READ |
| `sessions/session-consistency/_template/phase-2-analysis/_template/*` | CREATE | - | - | - | - | - | - | - | - | READ |
| `sessions/session-consistency/_template/phase-3-proposal/_template/*` | CREATE | - | - | - | - | - | - | - | - | READ |
| `sessions/session-consistency/_template/phase-N/workers/_template/*` | MODIFY(削除) | - | - | - | - | - | - | - | - | - |
| `sessions/config-optimization/_template/phase-1-collection/_template/*` | - | CREATE | - | - | - | - | - | - | - | READ |
| `sessions/config-optimization/_template/phase-2-analysis/_template/*` | - | CREATE | - | - | - | - | - | - | - | READ |
| `sessions/config-optimization/_template/phase-3-proposal/_template/*` | - | CREATE | - | - | - | - | - | - | - | READ |
| `sessions/config-optimization/_template/workers/_template/*` | - | MODIFY(削除) | - | - | - | - | - | - | - | - |
| `.claude/skills/session-consistency-manager/SKILL.md` | - | - | MODIFY | - | - | - | - | - | - | READ |
| `.claude/skills/config-optimizer-manager/SKILL.md` | - | - | - | MODIFY | - | - | - | - | - | READ |
| `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md` | - | - | - | - | MODIFY | - | - | - | - | READ |
| `.claude/skills/session-consistency-manager/agents/sc-analysis-worker.md` | - | - | - | - | MODIFY | - | - | - | - | READ |
| `.claude/skills/session-consistency-manager/agents/sc-proposal-worker.md` | - | - | - | - | MODIFY | - | - | - | - | READ |
| `.claude/skills/session-consistency-manager/agents/sc-evaluator.md` | - | - | - | - | MODIFY | - | - | - | - | READ |
| `.claude/skills/config-optimizer-manager/agents/config-collection-worker.md` | - | - | - | - | - | MODIFY | - | - | - | READ |
| `.claude/skills/config-optimizer-manager/agents/config-analysis-worker.md` | - | - | - | - | - | MODIFY | - | - | - | READ |
| `.claude/skills/config-optimizer-manager/agents/config-proposal-worker.md` | - | - | - | - | - | MODIFY | - | - | - | READ |
| `.claude/skills/config-optimizer-manager/agents/config-optimizer-evaluator.md` | - | - | - | - | - | MODIFY | - | - | - | READ |
| `.claude/skills/session-flow-policy/SKILL.md` | - | - | - | - | - | - | MODIFY | - | - | READ |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | - | - | - | - | - | - | - | MODIFY | - | READ |
| `docs/workflow.md` | - | - | - | - | - | - | - | - | MODIFY | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ行は **なし**。T-010 は READ のみのため競合なし。全タスクのファイル書き込みは排他的。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001: session-consistency テンプレートディレクトリ移動
- T-002: config-optimization テンプレートディレクトリ変更
- T-008: session-lifecycle-policy §1.3 列追加（テンプレート変更に依存しない）

### Wave 2 (Wave 1 完了後、並列実行可)
- T-003: session-consistency-manager SKILL.md パス更新（depends on T-001）
- T-004: config-optimizer-manager SKILL.md パス更新（depends on T-002）
- T-005: session-consistency エージェント定義パス更新（depends on T-001）
- T-006: config-optimizer エージェント定義パス更新（depends on T-002）
- T-007: session-flow-policy §4.3 追加（depends on T-001）
- T-009: docs/workflow.md 更新（depends on T-001, T-002）

### Wave 3 (Wave 2 完了後)
- T-010: 横断検証（depends on T-001〜T-009）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 汎用的なファイル操作・パス置換のため専門エージェント不要 | Worker |
| なし | - | パス整合性の検証は汎用的なため専門エージェント不要 | Evaluator |

## Summary

- Total tasks: 10
- Total waves: 3
- Estimated max parallelism: 6 workers（Wave 2）
- Conflict count: 0（全タスクのファイル書き込みが排他的）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-19
