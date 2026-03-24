# File-Level Task Division: l1-no-direct-work-enforcement

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 2
- Dependency graph: T-003 → T-001（T-003 は T-001 の追加内容を可視化文書に反映するため依存）

## Task Assignments

### T-001: L1 SKILL.md に担当ファイルテーブルを新設し「やらないこと」を拡充

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`（160行目付近「やらないこと」セクション拡充、150行目付近に「担当ファイル」セクション新設）
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/agents/l2-worker.md`（担当ファイルテーブル 59行目〜: 形式の参照・整合性確認）
  - `.claude/skills/l1-manager/agents/l2-evaluator.md`（担当ファイルテーブル 55行目〜: 形式の参照・整合性確認）
  - `sessions/initiatives/l1-no-direct-work-enforcement/02_plan.md`（L1 担当ファイルテーブル設計案）
  - `sessions/initiatives/l1-no-direct-work-enforcement/01_proposal.md`（施策背景・スコープ）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  1. L1 SKILL.md に「担当ファイル」セクションが新設され、02_plan.md の設計案に基づく「L1 が編集可能なファイル」テーブルが記載されている
  2. L1 SKILL.md の「やらないこと」セクションに、禁止対象ファイルパスパターン（`.claude/skills/**`, `.claude/rules/**`, `.claude/templates/**`, `sessions/initiatives/_template/**`, `sessions/triage/_template/**`, `docs/**`）が具体的に列挙されている
  3. L2-worker, L2-evaluator の既存「担当ファイルテーブル」と形式（テーブル構造: ファイル | 操作）が統一されている
  4. 「担当ファイル」セクションの位置は「やらないこと」セクションの直前（150行目の `---` の直後、「やること」セクションの前）に配置されている
  5. 適用対象環境: CLI / SDK 共通
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: CLAUDE.md の禁止事項を強化

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `CLAUDE.md`（38行目付近「禁止事項」セクション）
- **Read-only dependencies**:
  - `sessions/initiatives/l1-no-direct-work-enforcement/02_plan.md`（禁止事項の設計案）
  - `sessions/initiatives/l1-no-direct-work-enforcement/01_proposal.md`（施策背景）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  1. CLAUDE.md の禁止事項セクション（38行目付近）に「L1セッションが施策のタスク対象ファイル（`.claude/skills/`, `.claude/rules/`, `.claude/templates/`, テンプレート等）を直接編集すること（L2ワーカーに委任すべき実作業）」が追記されている
  2. 既存の禁止事項（L1 が work_log を直接編集、L2 が plan/gate_review を変更 等）と整合性がある
  3. 文言が具体的で曖昧さがない（パスパターンが明示されている）
  4. 適用対象環境: CLI / SDK 共通
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: docs/workflow.md の連動更新

- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `docs/workflow.md`（L1 マネージャーセクション付近）
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/SKILL.md`（T-001 で追加された担当ファイルテーブルと「やらないこと」の内容を反映）
  - `sessions/initiatives/l1-no-direct-work-enforcement/02_plan.md`（計画の確認）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**:
  1. docs/workflow.md に L1 マネージャーの担当ファイル制約に関する記述が追加されている
  2. T-001 で追加された L1 SKILL.md の担当ファイルテーブルおよび「やらないこと」の内容が正確に反映されている
  3. 可視化文書としての位置づけ（正の情報源は L1 SKILL.md）が維持されている
  4. 適用対象環境: CLI / SDK 共通
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 |
|------|:-----:|:-----:|:-----:|
| `.claude/skills/l1-manager/SKILL.md` | MODIFY | - | READ |
| `CLAUDE.md` | - | MODIFY | - |
| `docs/workflow.md` | - | - | MODIFY |
| `.claude/skills/l1-manager/agents/l2-worker.md` | READ | - | - |
| `.claude/skills/l1-manager/agents/l2-evaluator.md` | READ | - | - |
| `02_plan.md` | READ | READ | READ |
| `01_proposal.md` | READ | READ | - |

**競合検出**: なし。全タスクの MODIFY 対象ファイルは重複しない。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001: L1 SKILL.md に担当ファイルテーブルを新設し「やらないこと」を拡充
- T-002: CLAUDE.md の禁止事項を強化

### Wave 2 (Wave 1 完了後)
- T-003: docs/workflow.md の連動更新（depends on T-001）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | ルール文書の編集が主であり、特定ドメイン知識は不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 3
- Total waves: 2
- Estimated max parallelism: 2 workers（Wave 1）
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-24
