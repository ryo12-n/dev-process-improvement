# File-Level Task Division: l2-knowledge-action-gap

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 4（ファイル競合なし）
- Dependency graph: なし（全タスク独立）

> ただし全タスクで「即時適用可能」の判断基準を一貫させる必要がある。以下の共通定義を全タスクの実装時に参照すること。

### 共通定義: 「即時適用可能」の判断基準

以下の3条件をすべて満たす場合に「即時適用可能」と判断する:
1. 修正対象ファイルが現施策のスコープ内にある
2. 修正内容が明確で、追加調査を必要としない
3. 修正が他の施策と競合しない

上記を満たさない場合は従来通り L1 のルーティング（inbox/backlog/refs）に回す。

## Task Assignments

### T-001: l2-worker.md に「知見に基づく修正適用」ステップを追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-worker.md`
  - 作業フロー（## 作業フロー）: ステップ5（レポート作成）の後に「知見に基づく修正適用」ステップを追加（ステップ5.5 相当、またはステップ5の直後に新ステップとして挿入）
  - やること（## やること）: 「即時適用可能なルール化候補は同一セッション内で修正を適用する」を追加
  - やらないこと（## やらないこと）: 「即時適用可能」の3条件を満たさない知見の修正は行わない旨を追加
- **Read-only dependencies**: `01_proposal.md`（即時適用可能の判断基準を参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 作業フローに「知見に基づく修正適用」ステップが追加されている
  - やることセクションに修正適用の記載がある
  - 「即時適用可能」の判断基準（3条件）が明記されている
  - 条件を満たさない場合は従来通りルーティングに回す旨が記載されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: l2-evaluator.md に「知見に基づく修正提案」ステップを追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-evaluator.md`
  - 作業フロー（## 作業フロー）: ステップ4（評価実施）の後に「知見に基づく修正提案」ステップを追加
  - やること（## やること）: 「即時適用可能なルール化候補の修正提案を評価レポートに記載する」を追加
  - やらないこと（## やらないこと）: evaluator は直接修正を適用しない（提案のみ）旨を明記
- **Read-only dependencies**: `01_proposal.md`（即時適用可能の判断基準を参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 作業フローに「知見に基づく修正提案」ステップが追加されている
  - やることセクションに修正提案の記載がある
  - 「即時適用可能」の判断基準（3条件）が T-001 と一貫している
  - evaluator は直接修正せず提案のみ行う旨が明記されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: l1-manager SKILL.md の成果物確認観点に「知見修正適用チェック」を追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`
  - L2成果物の確認観点（### L2成果物の確認観点（evaluator起動前））セクション（267行目付近）: 「ルール化候補に即時適用可能なものがある場合、修正が適用済みか」のチェック項目を追加
- **Read-only dependencies**: `01_proposal.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - L2成果物の確認観点に「知見修正適用チェック」が追加されている
  - チェック内容が T-001/T-002 で追加されるステップと整合している
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: ゲートレビューテンプレートのプロセス品質チェックに項目追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `sessions/initiatives/_template/05_gate_review.md`
  - プロセス品質チェック（## プロセス品質チェック）テーブル: 「ルール化候補に即時適用可能なものがある場合、修正適用済み（worker）/ 修正提案済み（evaluator）」のチェック行を追加
- **Read-only dependencies**: `01_proposal.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - プロセス品質チェックテーブルに修正適用ステータス確認の行が追加されている
  - 条件付き項目（即時適用可能な知見がある場合のみ）として記載されている
  - チェック内容が T-001/T-002/T-003 と一貫している
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 |
|------|:-----:|:-----:|:-----:|:-----:|
| `.claude/skills/l1-manager/agents/l2-worker.md` | MODIFY | - | - | - |
| `.claude/skills/l1-manager/agents/l2-evaluator.md` | - | MODIFY | - | - |
| `.claude/skills/l1-manager/SKILL.md` | - | - | MODIFY | - |
| `sessions/initiatives/_template/05_gate_review.md` | - | - | - | MODIFY |
| `01_proposal.md` | READ | READ | READ | READ |

**競合検出結果**: 競合なし。各タスクが変更するファイルは完全に分離されている。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001, T-002, T-003, T-004

> 全タスクがファイル競合なしで独立しているため、Wave 1 のみで完了可能。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業（ルール追記）のため不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 4
- Total waves: 1
- Estimated max parallelism: 4 workers
- Conflict count: 0

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-24
