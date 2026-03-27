# コミットメッセージ規約への sprint 系 session-type 追加

## 背景
sprint-skill-implementation 施策で sprint-planner / sprint-generator / sprint-evaluator の3つの skill を作成した。
これらのセッションでコミットする際の session-type が `.claude/rules/commit-message.md` に未定義。

## 提案
以下の session-type を `.claude/rules/commit-message.md` の非施策作業テーブルに追加する:

| session-type | category | 用途 | 例 |
|-------------|----------|------|-----|
| `sprint-plan` | `<sprint_name>` | planner: 計画作成・タスク管理・知見蒸留 | `[sprint-plan] auth-refactor: plan.md・todo.md 作成` |
| `sprint-gen` | `<sprint_name>` | generator: タスク実行・work_log 記録 | `[sprint-gen] auth-refactor: T-001 実装完了` |
| `sprint-eval` | `<sprint_name>` | evaluator: レビュー・review.md 記録 | `[sprint-eval] auth-refactor: Round 1 レビュー完了` |

## 発見元
sprint-skill-implementation 施策 壁打ちフェーズ（指摘D）

---
**起票日**: 2026-03-26
