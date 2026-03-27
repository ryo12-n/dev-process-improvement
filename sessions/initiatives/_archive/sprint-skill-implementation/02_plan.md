# 実施計画: sprint-skill-implementation

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | ディレクトリ構成の整備 | `sessions/sprints/_template/` に5ファイル移動済み、`_archive/` 作成済み、変数名統一済み、`templates/sprint_template/` 削除済み |
| 2 | SKILL.md 3ファイルの作成 | 3つの SKILL.md が仕様通りに存在し、指摘B・C の改善が反映されている |
| 3 | inbox 整理・起票 | 関連 inbox ファイルの削除、コミットメッセージ規約 inbox 起票 |

## スケジュール

1. フェーズ1〜3 は依存関係が低いため、単一ワーカーで逐次実行する
2. 評価者が成果物を検証する
3. ゲート判定

## 成功基準（全体）

1. `sessions/sprints/_template/` に plan.md / todo.md / work_log.md / review.md / knowledge.md の5ファイルが存在する
2. `sessions/sprints/_archive/` ディレクトリが存在する
3. `.claude/skills/sprint-planner/SKILL.md` が存在し、壁打ちルール・担当ファイル・やらないことが記載されている
4. `.claude/skills/sprint-generator/SKILL.md` が存在し、タスク選択ルール・DEVIATION パターン・担当ファイルが記載されている
5. `.claude/skills/sprint-evaluator/SKILL.md` が存在し、レビュー基準・Round 追記方式・担当ファイルが記載されている
6. `templates/sprint_template/` が削除されている（`git mv` で移動済み）
7. `sessions/sprints/_template/knowledge.md` 内の変数名が `{{repository_name}}` に統一されている
8. 3つの SKILL.md の起動キーワードが互いに区別可能である（指摘B 対応）
9. sprint-planner の SKILL.md に親タスクのステータス管理が planner の責務である旨が明記されている（指摘C 対応）
10. 関連 inbox ファイル（sprint-folder-definition.md, sprint-template-variable-unification.md）が削除されている
11. コミットメッセージ規約への sprint 系 session-type 追加が inbox に起票されている

## リソース・前提条件

- `templates/sprint_template/` に5ファイルが存在すること（確認済み）
- `inbox/sprint-skill-implementation 実施計画書.md` に3つの SKILL.md の詳細仕様が記載されていること（確認済み）
- `.claude/skills/` ディレクトリに sprint 系の既存 skill がないこと（確認済み）

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| `templates/sprint_template/` の移動で既存参照が壊れる | 低 | 低 | 移動前に grep で参照箇所を確認し、必要なら更新する |
| skill の起動キーワードが既存 skill と競合する | 低 | 低 | 既存 skill の name 一覧を確認してから命名する |

---
**作成者**: L1
**作成日**: 2026-03-26
**最終更新**: 2026-03-26
