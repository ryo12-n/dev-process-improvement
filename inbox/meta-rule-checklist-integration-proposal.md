# 「メタルール横断検証」と `rule-change-checklist` タスクの統合・整理

## 背景

施策 `l1-manager-checklist-integration` の評価で発見。`l1-manager/SKILL.md` に現在2つの条件付き固定タスクが同一適用条件（`.claude/skills/`, `.claude/rules/` 変更時）で共存している:

1. **メタルール横断検証**（3領域: フロー記述・workflow.md・TG-008基準）
2. **rule-change-checklist 参照**（7項目: 上記3領域 + パス変更走査・deny リスト・テンプレート・コミットメッセージ規約）

`rule-change-checklist`（7項目）は「メタルール横断検証」（3領域）の上位互換として機能するため、将来的な整合性・分かりやすさの観点から統合・置換を検討する価値がある。

## 提案

- 「メタルール横断検証」タスクを廃止し、`rule-change-checklist` 参照タスクに一本化する
- または「メタルール横断検証」の詳細説明を `rule-change-checklist` スキルの項目説明に統合する

**起票元**: l1-manager-checklist-integration 施策 08_gate_review.md
**起票日**: 2026-03-18
