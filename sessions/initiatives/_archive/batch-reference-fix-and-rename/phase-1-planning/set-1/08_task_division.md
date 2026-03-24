# File-Level Task Division: batch-reference-fix-and-rename

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 1
- Dependency graph: T-001 → T-004（参照修正完了後にメタルール検証）。T-002, T-003 は独立だが、全体が軽量のため1ワーカー逐次実行を推奨。

## Task Assignments

### T-001: 壊れた参照修正（SC-008）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-plan-worker.md`（L199: `triage-standard-policy` → `session-lifecycle-policy`）
- **Read-only dependencies**: `.claude/skills/session-lifecycle-policy/SKILL.md`（正しいパス確認用）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - L199 の `triage-standard-policy` が `session-lifecycle-policy` に置換されていること
  - `Grep` で `.claude/skills/` および `.claude/rules/` 配下に `triage-standard-policy` のアクション可能な残存参照がないこと（`session-consistency-reference.md` のリファレンスデータは SC スキャンの記録のためスコープ外）
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

**計画時の注意**: `02_plan.md` では `l2-plan-evaluator.md` の2箇所も修正対象だったが、同ファイルは PR #167（refactor-phase-gates）で廃止済み。実際の MODIFY 対象は `l2-plan-worker.md` の1箇所のみ。

### T-002: リネーム時全文検索チェックルール作成
- **Assigned files (CREATE)**: `.claude/rules/rename-reference-check.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**:
  - `backlog/entries/リネーム時全文検索チェック義務化ルール追加.md`（実施案の参照）
  - `.claude/skills/rule-change-checklist/SKILL.md`（チェックリスト §4 との整合性確認）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `.claude/rules/rename-reference-check.md` が作成されていること
  - 以下の内容が含まれていること:
    1. リネーム前に旧名称で Grep 全文検索を実行する義務
    2. 検出された全箇所を新名称に更新する義務
    3. 更新後に旧名称で再度 Grep を実行し残存参照ゼロを確認する義務
    4. 対象範囲: `.claude/skills/`、`docs/`、`sessions/*/_template/`、`.claude/rules/`、`backlog/`
  - `rule-change-checklist` §4 と重複せず補完的であること
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: バックログエントリクリーンアップ
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: なし
- **Assigned files (DELETE)**:
  - `backlog/entries/SC-008壊れた参照修正.md`
  - `backlog/entries/SCチェックQuickWins一括是正.md`
  - `backlog/entries/リネーム時全文検索チェック義務化ルール追加.md`
  - `backlog/entries/sync-worker同期先コミット漏れ防止.md`
- **Read-only dependencies**: `backlog/backlog.csv`（削除後の CSV 自動生成への影響確認）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 4件のファイルが `git rm` で削除されていること
  - `backlog/backlog.csv` の該当行も整合していること（CSV が自動生成の場合、生成トリガーの確認のみ）
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: ルール変更連動更新チェックリスト（rule-change-checklist）実施
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: なし（チェックの結果、連動更新が必要になった場合は該当ファイルを MODIFY）
- **Read-only dependencies**:
  - `.claude/skills/rule-change-checklist/SKILL.md`（チェックリスト本体）
  - `.claude/skills/l1-manager/agents/l2-plan-worker.md`（変更ファイルの「関連ファイル一覧」確認）
  - `docs/workflow.md`（連動更新要否の確認）
- **Prerequisite tasks**: T-001, T-002, T-003
- **Acceptance criteria**:
  - rule-change-checklist の全7項目について確認結果が `02_worker_log.md` に記録されていること
  - 具体的な確認ポイント:
    1. `l2-plan-worker.md` の「関連ファイル一覧」に記載されたファイルの連動更新要否 → 要否判断済み
    2. `docs/workflow.md` への影響 → `01_proposal.md` で「やらないこと」に記載済みだが、実際の変更内容と照合して確認
    3. `session-lifecycle-policy/SKILL.md` への影響 → 影響なし（参照を修正しただけで、ポリシー内容の変更なし）
    4. パス変更・リネームの走査対象網羅性 → T-001 の Grep 結果で確認済みであること
    5. deny リスト → 該当なし
    6. テンプレート連動 → 該当なし
    7. コミットメッセージ規約 → 該当なし
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 |
|------|:-----:|:-----:|:-----:|:-----:|
| `.claude/skills/l1-manager/agents/l2-plan-worker.md` | MODIFY | - | - | READ |
| `.claude/rules/rename-reference-check.md` | - | CREATE | - | READ |
| `backlog/entries/SC-008壊れた参照修正.md` | - | - | DELETE | - |
| `backlog/entries/SCチェックQuickWins一括是正.md` | - | - | DELETE | - |
| `backlog/entries/リネーム時全文検索チェック義務化ルール追加.md` | - | READ | DELETE | - |
| `backlog/entries/sync-worker同期先コミット漏れ防止.md` | - | - | DELETE | - |
| `.claude/skills/rule-change-checklist/SKILL.md` | - | READ | - | READ |
| `docs/workflow.md` | - | - | - | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, DELETE = 削除, `-` = 無関係

**競合検出**: 同一ファイルに対して複数タスクが CREATE/MODIFY/DELETE を持つケースなし。T-002 が READ する `リネーム時全文検索チェック義務化ルール追加.md` を T-003 が DELETE するが、T-002 は実施案の参照のみで書き込みを行わないため、実行順序制約は不要（T-002 が先に READ すれば問題なし）。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001: 壊れた参照修正
- T-002: リネームチェックルール作成
- T-003: バックログエントリクリーンアップ

**注記**: T-002 は `リネーム時全文検索チェック義務化ルール追加.md` を READ するため、T-003 の DELETE より先に実行するか、内容を事前に確認してから並列実行すること。1ワーカー逐次実行の場合は T-002 → T-003 の順序で自然に解決される。

### Wave 2 (Wave 1 完了後)
- T-004: ルール変更連動更新チェックリスト（T-001, T-002, T-003 の全完了が前提）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 全タスクが S 複雑度の機械的作業のため汎用ワーカーで十分 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 4
- Total waves: 2
- Estimated max parallelism: 1 worker（全タスク S 複雑度、1ワーカー逐次実行を推奨）
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）

### 計画時の差分（02_plan.md からの変更点）

| 項目 | 02_plan.md の記載 | 計画時の発見 |
|------|------------------|------------|
| `l2-plan-evaluator.md` の MODIFY（2箇所） | 修正対象に含まれている | PR #167 で廃止済み。MODIFY 対象から除外 |
| `triage-standard-policy` の残存参照 | 3箇所（evaluator 2箇所 + worker 1箇所） | 実質1箇所（worker L199 のみ）。`session-consistency-reference.md` にも記録があるが SC リファレンスデータのためスコープ外 |
| rule-change-checklist タスク | 成功基準に記載あり | T-004 として独立タスク化 |

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-24
