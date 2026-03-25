# File-Level Task Division: batch-rule-policy-minor-additions

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 1（逐次ディスパッチ）
- Dependency graph: T-001〜T-007 は独立。T-008（docs/workflow.md 連動更新）は T-001〜T-007 全完了後。T-009〜T-012 は固定タスク（T-007 完了後）

## Task Assignments

### T-001: BL-022 deny リスト変更提案への副作用分析チェック項目追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/rule-change-checklist/SKILL.md` — §5「deny リスト変更時の対称性チェック」の後に新セクション「§6 deny リスト変更提案時の副作用分析」を追加（現§6→§7、§7→§8 に繰り下げ）
- **Read-only dependencies**: `backlog/entries/denyリスト変更提案への副作用分析必須化.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - deny 変更提案時にブロックされる正当なパターンの洗い出し義務化チェック項目が追加されている
  - 代替手段の提示が必須化されている
  - 既存の§5（deny リスト対称性チェック）と重複なく補完関係にある
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: BL-028 ゲート判定基準に課題重大度の判定フレームワーク追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/manager-common-policy/SKILL.md` — §4「ゲート判定基準」の後（§4 末尾〜§5 前）にサブセクション「§4.1 課題重大度の判定基準」を追加
- **Read-only dependencies**: `backlog/entries/ゲート判定基準での課題重大度の明文化.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - ブロック課題/非ブロック課題の判定基準テーブルが定義されている
  - 「この課題は次フェーズをブロックするか？」の判断フレームワークが明文化されている
  - 既存の§4 ゲート判定基準（通過/条件付き通過/差し戻し）と整合している
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: BL-063 リファレンス文書の粒度基準追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/manager-common-policy/SKILL.md` — §5.3「refs ルーティング実行手順」の後に「§5.4 リファレンス文書の粒度基準」を追加
- **Read-only dependencies**: `backlog/entries/reference-doc-granularity-rule.md`, `refs/_knowledge_template.md`, `refs/_work_log_template.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - knowledge.md に追記する知見の粒度基準が定義されている（1エントリの範囲・分割基準）
  - work-logs/ に記録する調査ログの粒度基準が定義されている（作成要否の判断基準）
  - 具体例または判断フローチャートが含まれている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: BL-044 user-invocable: false スキルの description 設計パターン追記
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/session-flow-policy/SKILL.md` — §2.1「YAML フロントマター」の後に「§2.1.1 description 設計パターン」を追加
- **Read-only dependencies**: `backlog/entries/user-invocable-false-description-pattern.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `user-invocable: true` と `user-invocable: false` で description の設計方針が異なることが明記されている
  - `user-invocable: false` の場合は「何の情報を持つか」+「どの文脈で参照するか」の2要素パターンが定義されている
  - 良い例・悪い例が含まれている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: BL-046 固定タスクセクションのサブヘッダ構造化
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md` — 「タスクリストに含める固定タスク」セクション（L211付近）にサブヘッダ「全施策共通」「条件付き（ルール変更施策）」「条件付き（プロジェクト紐づけ施策）」を追加
- **Read-only dependencies**: `backlog/entries/条件付き固定タスク配置ルール整備.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 無条件タスク（全施策適用）と条件付きタスク（特定施策のみ適用）がサブヘッダで視覚的に区分されている
  - 各条件付きタスクの適用条件が明記されている
  - 既存の固定タスク内容は変更せず、構造のみ変更している
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-006: BL-041 全スキルに「関連ファイル一覧」セクション義務化ルール追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/session-flow-policy/SKILL.md` — §2.2「必須セクション」に「関連ファイル一覧」を追加、および §3.1「必須セクション」にもエージェント向けの「関連ファイル一覧」を追加
- **Read-only dependencies**: `backlog/entries/rules-skills移動時の波及更新パターン.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - SKILL.md の必須セクションリスト（§2.2）に「関連ファイル一覧」が追加されている
  - エージェント定義の必須セクション（§3.1）にも「関連ファイル一覧」が追加されている
  - セクションのフォーマット（テーブル形式: ファイル | 連動更新の内容）が定義されている
  - 本施策スコープはルール定義のみ（全スキルへの実展開は別施策）であることが注記されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-007: BL-025 エージェント管理ガイドラインセクション新設
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/session-flow-policy/SKILL.md` — §3 の末尾（§3.5「順序制約」の後）に「§3.6 エージェント管理ガイドライン」を追加
- **Read-only dependencies**: `backlog/entries/agentsの管理方法のガイドライン追記.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `.claude/agents`（グローバルエージェント）と `.claude/skills/<skill>/agents`（スキル内エージェント）の使い分けガイドが記載されている
  - エージェントのスコープ・タイミング・プロンプト構成のベストプラクティスが定義されている
  - 新セッションタイプ追加時の設計指針として参照可能な構成になっている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-008: docs/workflow.md 連動更新
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `docs/workflow.md` — T-001〜T-007 の変更内容に対応するセクションを更新
- **Read-only dependencies**: `.claude/skills/rule-change-checklist/SKILL.md`, `.claude/skills/manager-common-policy/SKILL.md`, `.claude/skills/session-flow-policy/SKILL.md`, `.claude/skills/l1-manager/SKILL.md`
- **Prerequisite tasks**: T-001, T-002, T-003, T-004, T-005, T-006, T-007
- **Acceptance criteria**:
  - T-001〜T-007 で追加・変更した内容が docs/workflow.md の該当セクションに反映されている
  - 可視化文書としての整合性が維持されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-009: 知見記録（固定タスク — 実施ワーカー向け）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `phase-2-execution/set-N/03_worker_report.md` — 「作業中の知見」セクション
- **Read-only dependencies**: なし
- **Prerequisite tasks**: T-007（全実施タスク完了後）
- **Acceptance criteria**: 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-010: メタルール横断検証（固定タスク — ルール変更施策）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `phase-2-execution/set-N/03_worker_report.md` — メタルール横断検証結果セクション
- **Read-only dependencies**: `.claude/skills/session-lifecycle-policy/SKILL.md`, `docs/workflow.md`（T-008 更新後）
- **Prerequisite tasks**: T-008
- **Acceptance criteria**: 3領域（メタルールフロー記述・workflow.md 同期・TG-008 基準連動）の検証結果が記載されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-011: rule-change-checklist 実施（固定タスク — ルール変更施策）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `phase-2-execution/set-N/02_worker_log.md` — チェックリスト確認結果
- **Read-only dependencies**: `.claude/skills/rule-change-checklist/SKILL.md`
- **Prerequisite tasks**: T-010
- **Acceptance criteria**: チェックリスト全7項目の確認結果が記録されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-012: 課題転記確認（固定タスク — 実施ワーカー向け）
- **Assigned files (CREATE)**: `issues/entries/ISS-XXX.md`（必要に応じて）
- **Assigned files (MODIFY)**: `phase-2-execution/set-N/07_issues.md`
- **Read-only dependencies**: `issues/_template.md`
- **Prerequisite tasks**: T-011
- **Acceptance criteria**: 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 | T-006 | T-007 | T-008 | T-009 | T-010 | T-011 | T-012 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `.claude/skills/rule-change-checklist/SKILL.md` | MODIFY | - | - | - | - | - | - | READ | - | - | READ | - |
| `.claude/skills/manager-common-policy/SKILL.md` | - | MODIFY | MODIFY | - | - | - | - | READ | - | - | - | - |
| `.claude/skills/session-flow-policy/SKILL.md` | - | - | - | MODIFY | - | MODIFY | MODIFY | READ | - | - | - | - |
| `.claude/skills/l1-manager/SKILL.md` | - | - | - | - | MODIFY | - | - | READ | - | - | - | - |
| `docs/workflow.md` | - | - | - | - | - | - | - | MODIFY | - | READ | - | - |
| `phase-2-execution/set-N/03_worker_report.md` | - | - | - | - | - | - | - | - | MODIFY | MODIFY | - | - |
| `phase-2-execution/set-N/02_worker_log.md` | - | - | - | - | - | - | - | - | - | - | MODIFY | - |
| `phase-2-execution/set-N/07_issues.md` | - | - | - | - | - | - | - | - | - | - | - | MODIFY |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | - | - | - | - | - | - | - | - | - | READ | - | - |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**:

| 競合ファイル | 関連タスク | 競合種別 | 解決方針 |
|------------|-----------|---------|---------|
| `manager-common-policy/SKILL.md` | T-002(MODIFY), T-003(MODIFY) | 同一ファイル別セクション | T-002 は §4 末尾、T-003 は §5.3 後に追記。セクションが離れており逐次処理で安全。Wave 1 内で順次実行 |
| `session-flow-policy/SKILL.md` | T-004(MODIFY), T-006(MODIFY), T-007(MODIFY) | 同一ファイル別セクション | T-004 は §2.1 後、T-006 は §2.2/§3.1、T-007 は §3.5 後。セクションが分散しており逐次処理で安全。Wave 1 内で順次実行 |
| `phase-2-execution/set-N/03_worker_report.md` | T-009(MODIFY), T-010(MODIFY) | 同一ファイル別セクション | T-009 は「知見」セクション、T-010 は「横断検証結果」セクション。逐次処理で安全 |

**結論**: 逐次ディスパッチ（1ワーカー）のため、全競合は実行順序により構造的に解消される。

## Wave Assignment

### Wave 1（逐次実行 — 1ワーカーが順次処理）
- T-001: BL-022 rule-change-checklist 副作用分析追加
- T-002: BL-028 manager-common-policy ゲート判定基準追加
- T-003: BL-063 manager-common-policy リファレンス粒度基準追加
- T-004: BL-044 session-flow-policy description パターン追記
- T-005: BL-046 l1-manager 固定タスクサブヘッダ構造化
- T-006: BL-041 session-flow-policy 関連ファイル一覧義務化
- T-007: BL-025 session-flow-policy エージェント管理ガイドライン

### Wave 2（Wave 1 完了後）
- T-008: docs/workflow.md 連動更新（depends on T-001〜T-007）

### Wave 3（Wave 2 完了後）
- T-009: 知見記録（depends on T-008）
- T-010: メタルール横断検証（depends on T-008）
- T-011: rule-change-checklist 実施（depends on T-010）
- T-012: 課題転記確認（depends on T-011）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業（ルール追記）のためドメインエージェント不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 12（実施7 + 連動更新1 + 固定タスク4）
- Total waves: 3
- Estimated max parallelism: 1 worker（逐次ディスパッチ）
- Conflict count: 3（同一ファイルへの複数 MODIFY — いずれも別セクションのため逐次処理で解消）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-25
