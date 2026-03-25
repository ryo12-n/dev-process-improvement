# File-Level Task Division: sprint-template-design

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 5
- Dependency graph: なし（全タスク独立）

## Task Assignments

### T-001: plan.md テンプレート作成
- **Assigned files (CREATE)**: `templates/sprint_template/plan.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint_template 設計計画書.txt`（確定フォーマット参照）, `sessions/initiatives/sprint-template-design/01_proposal.md`（責任マトリクス参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - メタ情報（Sprint ID, 開始日, 目標完了日, ステータス）セクションがある
  - 目標・スコープ（In Scope / Out of Scope）・成功条件セクションがある
  - タスク詳細セクションに対応方針ログが隣接配置されている
  - 責任マトリクスコメント（planner: 作成・更新、generator: READ ONLY、evaluator: READ ONLY）が記載されている
  - テンプレート変数（`{{sprint_name}}`, `{{sprint_id}}` 等）が使用されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: todo.md テンプレート作成
- **Assigned files (CREATE)**: `templates/sprint_template/todo.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint_template 設計計画書.txt`（確定フォーマット参照）, `sessions/initiatives/sprint-template-design/01_proposal.md`（責任マトリクス参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - メタ情報（Sprint ID, 最終更新）セクションがある
  - テーブル形式のタスクリスト（ID, タスク名, ステータス, 担当, 備考）がある
  - ステータス種別（todo / in-progress / done / blocked）がコメントに記載されている
  - 親タスク（T-XXX）は planner 管理、子タスク（T-XXX-Y）は generator 管理の2層構造が示されている
  - blocked が DEVIATION トリガーである旨がコメントに記載されている
  - 責任マトリクスコメント（planner: 作成・タスク追加・ステータス更新、generator: ステータス更新のみ、evaluator: READ ONLY）が記載されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: work_log.md テンプレート作成
- **Assigned files (CREATE)**: `templates/sprint_template/work_log.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint_template 設計計画書.txt`（確定フォーマット参照）, `sessions/initiatives/sprint-template-design/01_proposal.md`（責任マトリクス参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - タスク単位（T-XXX-Y）のセクション構造がある
  - 小見出し4つ（詰まったポイント / 判断 / 参考 / 結果）がある
  - DEVIATION マーカー（`🚧 DEVIATION`）セクションがある
  - DEVIATION セクションに「乖離内容」「planner への依頼」小見出しがある
  - 責任マトリクスコメント（planner: READ ONLY（DEVIATION受信）、generator: 追記のみ、evaluator: READ ONLY）が記載されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: review.md テンプレート作成
- **Assigned files (CREATE)**: `templates/sprint_template/review.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint_template 設計計画書.txt`（確定フォーマット参照）, `sessions/initiatives/sprint-template-design/01_proposal.md`（責任マトリクス参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - Round 別セクション構造がある
  - 成功条件チェックテーブル（成功条件, 結果, 所見）がある
  - IMP 連番指摘（IMP-001, IMP-002...）構造がある（ラウンドをまたいで連番）
  - 総評セクションが各ラウンドに含まれている
  - 責任マトリクスコメント（planner: READ ONLY（次アクション入力）、generator: 触れない、evaluator: round別セクションで追記）が記載されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: knowledge.md テンプレート作成
- **Assigned files (CREATE)**: `templates/sprint_template/knowledge.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint_template 設計計画書.txt`（確定フォーマット参照）, `sessions/initiatives/sprint-template-design/01_proposal.md`（責任マトリクス参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - メタ情報（Sprint ID, エスカレーション先, エスカレーション済みフラグ）がある
  - 蒸留ボリューム単位セクション（Vol.1, Vol.2...）がある
  - 各蒸留セクションにソース（work_log / review 参照）が記載される構造がある
  - 知見エントリに「状況 / 学び / エスカレーション候補」がある
  - エスカレーションログテーブルがある
  - 責任マトリクスコメント（planner: 定期蒸留・更新・エスカレーション、generator: 触れない、evaluator: 触れない）が記載されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|
| `templates/sprint_template/plan.md` | CREATE | - | - | - | - |
| `templates/sprint_template/todo.md` | - | CREATE | - | - | - |
| `templates/sprint_template/work_log.md` | - | - | CREATE | - | - |
| `templates/sprint_template/review.md` | - | - | - | CREATE | - |
| `templates/sprint_template/knowledge.md` | - | - | - | - | CREATE |
| `inbox/sprint_template 設計計画書.txt` | READ | READ | READ | READ | READ |
| `sessions/initiatives/sprint-template-design/01_proposal.md` | READ | READ | READ | READ | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。
**競合検出結果**: 競合なし。各タスクの CREATE 対象ファイルはすべて異なる。READ のみ共有。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001（plan.md）, T-002（todo.md）, T-003（work_log.md）, T-004（review.md）, T-005（knowledge.md）

**Wave 2 以降**: なし（全タスク Wave 1 で完結）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業のため汎用ワーカーで十分 | Worker |
| なし | - | テンプレート準拠の確認は汎用評価者で十分 | Evaluator |

## Summary

- Total tasks: 5
- Total waves: 1
- Estimated max parallelism: 5 workers
- Conflict count: 0（全タスクが異なるファイルへの CREATE）

### 備考
- `templates/` ディレクトリ自体が現時点で存在しないため、最初のタスク実行時に `templates/sprint_template/` ディレクトリの作成が必要。ディレクトリ作成は各ワーカーが `mkdir -p` で冪等に実行可能
- 全タスクの Read-only 依存が共通（設計計画書 + 01_proposal.md）であり、並列実行に影響しない

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-25
