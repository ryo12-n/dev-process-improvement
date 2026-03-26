# File-Level Task Division: sprint-skill-implementation

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 3
- Dependency graph: T-001 → {T-002, T-003, T-004}（並列可）, T-005 は独立

T-001（ディレクトリ整備）が完了してから T-002〜T-004（SKILL.md 作成）を並列実行する。
SKILL.md 内でテンプレートパス `sessions/sprints/_template/` を参照するため、ディレクトリ構成が先に確定している必要がある。
T-005（inbox 整理・起票）は他タスクと独立しており、どの Wave でも実行可能。

## Task Assignments

### T-001: ディレクトリ構成の整備（git mv + アーカイブ作成 + 変数名統一）
- **Assigned files (CREATE)**: `sessions/sprints/_archive/.gitkeep`
- **Assigned files (MODIFY)**: `sessions/sprints/_template/knowledge.md`（`{{repo}}` → `{{repository_name}}` 変数名統一、行41付近 `refs/{{repo}}/knowledge.md` → `refs/{{repository_name}}/knowledge.md`）
- **Assigned files (git mv)**: `templates/sprint_template/{plan.md, todo.md, work_log.md, review.md, knowledge.md}` → `sessions/sprints/_template/`
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `sessions/sprints/_template/` に plan.md / todo.md / work_log.md / review.md / knowledge.md の5ファイルが存在する
  - `sessions/sprints/_archive/` ディレクトリが存在する（`.gitkeep` あり）
  - `templates/sprint_template/` が削除されている（`git mv` による移動済み）
  - `sessions/sprints/_template/knowledge.md` 内の `{{repo}}` が `{{repository_name}}` に統一されている
  - 移動前に `grep -r "sprint_template"` で既存参照箇所を確認し、必要なら更新済み
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: sprint-planner SKILL.md の作成（指摘B・C 対応含む）
- **Assigned files (CREATE)**: `.claude/skills/sprint-planner/SKILL.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint-skill-implementation 実施計画書.md`（「sprint-planner SKILL.md 仕様」セクション）, `01_proposal.md`（指摘B・C の対応方針）
- **Prerequisite tasks**: T-001（SKILL.md 内でテンプレートパス `sessions/sprints/_template/` を参照するため）
- **Acceptance criteria**:
  - `.claude/skills/sprint-planner/SKILL.md` が存在する
  - フロントマター（name / description / user-invocable）が記載されている
  - 起動パターン2つ（new / 再開）が記載され、他ロールとの区別が明確である（指摘B 対応: `sprint: new <name>` は planner 固有、`sprint: <name>` は再開時で planner/generator/evaluator が文脈で区別可能であることが明記されている）
  - 「フォルダ状態に応じた分岐」セクションに「全タスク done → 親タスク（T-XXX）のステータスを done に更新」が planner の責務として明記されている（指摘C 対応）
  - TodoWrite 登録例、壁打ちルール、担当ファイルテーブル、やらないことが記載されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: sprint-generator SKILL.md の作成（指摘B 対応含む）
- **Assigned files (CREATE)**: `.claude/skills/sprint-generator/SKILL.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint-skill-implementation 実施計画書.md`（「sprint-generator SKILL.md 仕様」セクション）, `01_proposal.md`（指摘B の対応方針）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**:
  - `.claude/skills/sprint-generator/SKILL.md` が存在する
  - フロントマター（name / description / user-invocable）が記載されている
  - 起動パターンが記載され、generator 固有の起動文脈が明確化されている（指摘B 対応: generator として起動する場合のユーザー発話パターンを例示）
  - タスク選択ルール（自律判断・一括提示・承認後自走）が記載されている
  - work_log.md 記録ルール・DEVIATION フォーマットが記載されている
  - todo.md 更新ルールテーブル、担当ファイルテーブル、やらないことが記載されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: sprint-evaluator SKILL.md の作成（指摘B 対応含む）
- **Assigned files (CREATE)**: `.claude/skills/sprint-evaluator/SKILL.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `inbox/sprint-skill-implementation 実施計画書.md`（「sprint-evaluator SKILL.md 仕様」セクション）, `01_proposal.md`（指摘B の対応方針）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**:
  - `.claude/skills/sprint-evaluator/SKILL.md` が存在する
  - フロントマター（name / description / user-invocable）が記載されている
  - 起動パターンが記載され、evaluator 固有の起動文脈が明確化されている（指摘B 対応: evaluator として起動する場合のユーザー発話パターンを例示）
  - レビュー基準（3値判定）が記載されている
  - review.md 記録ルール（Round 追記・IMP 連番）、次アクションガイド出力が記載されている
  - 担当ファイルテーブル、やらないことが記載されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: inbox 整理・コミットメッセージ規約起票
- **Assigned files (CREATE)**: `inbox/sprint-commit-message-session-type.md`
- **Assigned files (DELETE)**: `inbox/sprint-folder-definition.md`, `inbox/sprint-template-variable-unification.md`
- **Read-only dependencies**: `.claude/rules/commit-message.md`（既存の session-type 一覧を参照し、sprint 系の追加提案を起票）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `inbox/sprint-folder-definition.md` が削除されている
  - `inbox/sprint-template-variable-unification.md` が削除されている
  - `inbox/sprint-commit-message-session-type.md` が作成されており、sprint-planner / sprint-generator / sprint-evaluator の3ロールに対応する session-type の追加提案が記載されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|
| `templates/sprint_template/*` (5 files) | git mv | - | - | - | - |
| `sessions/sprints/_template/knowledge.md` | MODIFY | - | - | - | - |
| `sessions/sprints/_archive/.gitkeep` | CREATE | - | - | - | - |
| `.claude/skills/sprint-planner/SKILL.md` | - | CREATE | - | - | - |
| `.claude/skills/sprint-generator/SKILL.md` | - | - | CREATE | - | - |
| `.claude/skills/sprint-evaluator/SKILL.md` | - | - | - | CREATE | - |
| `inbox/sprint-folder-definition.md` | - | - | - | - | DELETE |
| `inbox/sprint-template-variable-unification.md` | - | - | - | - | DELETE |
| `inbox/sprint-commit-message-session-type.md` | - | - | - | - | CREATE |
| `inbox/sprint-skill-implementation 実施計画書.md` | - | READ | READ | READ | - |
| `.claude/rules/commit-message.md` | - | - | - | - | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, DELETE = 削除, git mv = 移動, `-` = 無関係

**競合検出**: 競合なし。各タスクの CREATE/MODIFY 対象ファイルは重複していない。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001（ディレクトリ構成の整備）
- T-005（inbox 整理・起票）

T-001 と T-005 は操作対象ファイルが完全に独立しており、並列実行可能。

### Wave 2 (Wave 1 完了後)
- T-002（sprint-planner SKILL.md）
- T-003（sprint-generator SKILL.md）
- T-004（sprint-evaluator SKILL.md）

T-002/T-003/T-004 は T-001 の完了が前提（テンプレートパスの確定）。
3タスクは互いに独立しており並列実行可能。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 全タスクが文書作成・ファイル操作のため、汎用 l2-worker で対応可能 | Worker |
| なし | - | 汎用 l2-evaluator で対応可能 | Evaluator |

## Summary

- Total tasks: 5
- Total waves: 2
- Estimated max parallelism: 3 workers（Wave 2）
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-26
