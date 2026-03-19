# File-Level Task Division: dispatch-log-and-cost-tracking

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 4（Wave 1）
- Dependency graph: T-001, T-002, T-003, T-005 は独立 → T-004 は T-001/T-002/T-003 に依存 → T-006 は T-003/T-004 に依存

```
Wave 1: T-001 ─┐
        T-002 ─┤
        T-003 ─┼→ Wave 2: T-004 ─→ Wave 3: T-006
        T-005 ─┘
```

## Task Assignments

### T-001: 02b_dispatch_log.md テンプレート新設
- **Assigned files (CREATE)**: `sessions/initiatives/_template/02b_dispatch_log.md`
- **Assigned files (MODIFY)**: -
- **Read-only dependencies**: `sessions/triage/_template/02_dispatch_log.md`（パターン参考）, `00_proposal.md`, `01_plan.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - initiative の Phase 構造（Phase 2〜5）に対応するディスパッチ記録構造を持つ
  - Worker Set 一覧テーブルに Phase・Set・ステータス列がある
  - ディスパッチ履歴セクションに Worker 起動/完了・Evaluator 起動/完了の記録テンプレートがある
  - トリアージの dispatch_log パターンとの構造的整合性がある（セクション名・記録形式の一貫性）
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: 09_cost_record.md テンプレート新設
- **Assigned files (CREATE)**: `sessions/initiatives/_template/09_cost_record.md`
- **Assigned files (MODIFY)**: -
- **Read-only dependencies**: `.claude/templates/session-cost-measurement.md`（Section B・C 参考、Section D 料金リファレンス参照）, `00_proposal.md`, `01_plan.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - フェーズ別（提案・計画 / 実施 / 評価 / ゲート判定）のセッションコスト記録テーブルがある
  - セッション種別（L1 / L2-worker / L2-evaluator）集計テーブルがある
  - 施策サマリテーブル（総コスト・総トークン・リワーク率等）がある
  - 料金リファレンスは `.claude/templates/session-cost-measurement.md` Section D への参照で重複を避けている
  - ディスパッチログ（02b）からの生データ取り込みを前提とした設計であること（テンプレート内に注記）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: 08_gate_review.md フェーズコスト評価セクション追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `sessions/initiatives/_template/08_gate_review.md`（末尾の判定セクション周辺にフェーズコスト評価セクションを追加）
- **Read-only dependencies**: `01_plan.md`, `00_proposal.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 既存チェック項目（Phase 1→2〜Phase 5→6）は変更されていない
  - 各 Phase チェックセクションにフェーズコスト小計行が追加されている（例: `| X-N | フェーズコスト小計が 09_cost_record.md に記録されている | ✅/❌ | |`）
  - 最終ゲート判定セクションに施策全体コスト集計が含まれている
  - フェーズコスト評価は「追加」であり、既存構造を破壊していない
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: l1-manager/SKILL.md ディスパッチログ・コスト記録手順の組み込み
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`（既存フローへの行追加が中心。新セクション追加は最小限）
- **Read-only dependencies**: `sessions/initiatives/_template/02b_dispatch_log.md`（T-001 成果物）, `sessions/initiatives/_template/09_cost_record.md`（T-002 成果物）, `sessions/initiatives/_template/08_gate_review.md`（T-003 成果物）, `00_proposal.md`, `01_plan.md`
- **Prerequisite tasks**: T-001, T-002, T-003
- **Acceptance criteria**:
  - 新施策開始手順に `02b_dispatch_log.md` と `09_cost_record.md` の初期化手順が追加されている
  - L2 サブエージェント起動時に `02b_dispatch_log.md` への記録手順が記載されている（起動・完了のタイムスタンプ記録）
  - 各 Phase チェック時に `09_cost_record.md` へのフェーズコスト小計記録手順が記載されている
  - 最終ゲート判定時に施策全体コスト集計の手順が記載されている
  - 既存フローの可読性を損なわない（行追加中心、新セクション最小限）
  - `関連ファイル一覧` に新テンプレート（02b, 09）が追加されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: session-cost-measurement.md サンプリング方式→全施策方式の整合性更新
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/templates/session-cost-measurement.md`（Section A の概要・適用場面・計測方式を更新）
- **Read-only dependencies**: `00_proposal.md`, `01_plan.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - Section A の「目的」がサンプリングキャンペーン限定ではなく全施策標準として記述されている
  - Section A の「適用場面」が「全施策の `_template/09_cost_record.md` で使用する」に更新されている
  - Section A の「計測方式」の収集者が L2 ではなくマネージャー（L1）に修正されている（計測主体の変更を反映）
  - Section B・C の雛形は `_template/09_cost_record.md` と整合している
  - Section D（料金リファレンス）は変更不要（`09_cost_record.md` から参照される）
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-006: メタルール横断検証（workflow.md・session-lifecycle-policy 等）
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `docs/workflow.md`（イニシアティブセッションフローのセクションにディスパッチログ・コスト記録の記述を追加）
- **Read-only dependencies**: `.claude/skills/l1-manager/SKILL.md`（T-004 成果物）, `sessions/initiatives/_template/08_gate_review.md`（T-003 成果物）, `.claude/skills/session-lifecycle-policy/SKILL.md`（TG-008 基準連動確認）
- **Prerequisite tasks**: T-003, T-004
- **Acceptance criteria**:
  - `docs/workflow.md` のイニシアティブセッションフローに `02b_dispatch_log.md`・`09_cost_record.md` への言及がある
  - `docs/workflow.md` のフェーズゲートチェック項目数がテンプレートの実態と一致している
  - `session-lifecycle-policy/SKILL.md` の TG-008 基準が変更内容に対応しているか確認済み（確認結果を `04_work_report.md` に記載）
  - 3領域の検証結果（メタルールフロー記述・workflow.md 同期・TG-008 基準連動）が記録されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 | T-006 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `sessions/initiatives/_template/02b_dispatch_log.md` | CREATE | - | - | READ | - | - |
| `sessions/initiatives/_template/09_cost_record.md` | - | CREATE | - | READ | - | - |
| `sessions/initiatives/_template/08_gate_review.md` | - | - | MODIFY | READ | - | READ |
| `.claude/skills/l1-manager/SKILL.md` | - | - | - | MODIFY | - | READ |
| `.claude/templates/session-cost-measurement.md` | - | READ | - | - | MODIFY | - |
| `docs/workflow.md` | - | - | - | - | - | MODIFY |
| `sessions/triage/_template/02_dispatch_log.md` | READ | - | - | - | - | - |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | - | - | - | - | - | READ |
| `00_proposal.md` | READ | READ | READ | READ | READ | - |
| `01_plan.md` | READ | READ | READ | READ | READ | - |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。
競合がある場合は Prerequisite tasks で依存関係を設定し、別 Wave に分離する。

**競合検出結果**: 競合なし。全ての CREATE/MODIFY 対象ファイルは各タスクで一意。Wave 間の依存関係は READ 依存のみ（T-004 が T-001/T-002/T-003 の成果物を READ、T-006 が T-003/T-004 の成果物を READ）。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001（02b_dispatch_log.md 新設）
- T-002（09_cost_record.md 新設）
- T-003（08_gate_review.md フェーズコスト追加）
- T-005（session-cost-measurement.md 整合性更新）

### Wave 2 (Wave 1 完了後)
- T-004（l1-manager/SKILL.md 更新）— depends on T-001, T-002, T-003

### Wave 3 (Wave 2 完了後)
- T-006（メタルール横断検証）— depends on T-003, T-004

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業（テンプレート更新・ルール追記）のため不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 6
- Total waves: 3
- Estimated max parallelism: 4 workers（Wave 1）
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）

### 備考

- Wave 1 は 4 タスクが並列可能だが、施策規模（S〜M の定型作業）を考慮すると、逐次ディスパッチでも十分実用的。L1 の判断で並列/逐次を選択してよい
- T-004（SKILL.md 更新）が最も複雑（既存フローへの組み込み）。可読性維持のため、新セクション追加ではなく既存手順への行追加を推奨
- T-006 のメタルール横断検証は l2-worker の固定タスク（ルール・テンプレート変更施策の場合）に該当。`rule-change-checklist` スキルのチェックリスト確認も含む

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-19
