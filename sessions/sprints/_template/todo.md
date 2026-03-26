<!-- 責任マトリクス
  planner:   ✅ 作成・タスク追加・ステータス更新
  generator: ✅ ステータス更新のみ
  evaluator: 📖 READ ONLY
-->

# Sprint Todo: {{sprint_name}}

## メタ情報
- Sprint ID: {{sprint_id}}
- 最終更新: {{updated_at}}

## タスクリスト

| ID | タスク名 | ステータス | 担当 | 備考 |
|---|---|---|---|---|
| T-001 | {{task_title}} | todo | planner | |
| T-001-1 | {{subtask_title}} | todo | generator | |
| T-001-2 | {{subtask_title}} | todo | generator | |
| T-002 | {{task_title}} | todo | planner | |
| T-002-1 | {{subtask_title}} | todo | generator | |

<!-- ステータス: todo / in-progress / done / blocked -->
<!-- blocked になった場合は work_log.md に DEVIATION を記載してplannerに通知 -->
<!-- 担当: planner / generator / evaluator -->
<!-- 親タスク(T-XXX)はplanner管理、子タスク(T-XXX-Y)はgenerator管理 -->
