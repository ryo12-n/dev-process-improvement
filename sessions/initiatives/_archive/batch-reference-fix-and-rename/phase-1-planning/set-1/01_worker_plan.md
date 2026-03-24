# ワーカー計画: batch-reference-fix-and-rename — Set-1

## 壁打ちフェーズ [2026-03-24]

### 理解のサマリー
- タスクの目的: 壊れた参照修正（SC-008）、リネームチェックルール新設、バックログエントリ4件のクリーンアップをバッチ処理する
- スコープ: `.claude/skills/` 配下の参照修正、`.claude/rules/` へのルール新規作成、`backlog/entries/` の不要エントリ削除
- 完了条件: `08_task_division.md` にタスク割当・Conflict Check Matrix・Wave Assignment が記載されていること

### 前提条件チェック
- [x] 施策計画（02_plan.md）の内容を理解: 理解済み
- [x] 提案書（01_proposal.md）の確認: 確認済み
- [x] 変更対象ファイル群の特定: 特定済み（※重要な差分あり、下記参照）

### 不明点・確認事項

なし（以下の差分は計画に反映して自走する）

**重要な発見事項**: `02_plan.md` に記載された修正対象のうち、`.claude/skills/l1-manager/agents/l2-plan-evaluator.md` は既に削除済み（PR #167 `refactor-phase-gates: フェーズゲート簡素化・plan-evaluator 廃止` で廃止）。そのため MODIFY 対象は当初3箇所から1箇所（`l2-plan-worker.md` L199）に縮小される。Grep 全文検索で `.claude/` 配下の `triage-standard-policy` 残存を確認し、アクション可能な参照は `l2-plan-worker.md` L199 の1箇所のみ。`session-consistency-reference.md` にも旧参照の記録があるが、これは SC マネージャーのリファレンスデータであり本施策のスコープ外（次回 SC スキャンで自動更新される想定）。

### L1 確認結果
確認事項なし：計画開始

---

## 分析計画サマリ

1. `01_proposal.md` / `02_plan.md` を読み、全7ファイル操作を把握
2. Grep で `triage-standard-policy` を全文検索し、修正対象の現状を確認
3. `l2-plan-evaluator.md` の廃止を発見 → MODIFY 対象が3箇所→1箇所に縮小
4. タスク間の依存関係とファイル競合を分析し、Wave 分割を決定
5. `rule-change-checklist` の適用要件を確認し、メタルール横断検証タスクを設計
