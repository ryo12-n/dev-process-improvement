# 改善施策提案: 同期チェックリストのスキル化と後続施策連携

## 背景・課題

施策「2つのリポジトリの部分的同期」（partial-repo-sync）で ai-driven-dev-patterns への同期チェックリストを作成したが、以下の課題がある。

1. **チェックリストの埋没**: `sessions/initiatives/_archive/partial-repo-sync/sync-checklist.md` にあり、同期作業時に発見・呼び出しにくい
2. **後続施策との連携不足**: backlog「リポジトリ間テンプレート同期の検証チェックリスト」に、本チェックリストの存在が記載されていない

## 目標

1. 同期チェックリストを `.claude/skills/repo-sync-checklist/SKILL.md` としてスキル化し、オンデマンドで呼び出せるようにする
2. 後続施策の backlog に情報を追記し、文脈の引き継ぎを完成させる

## スコープ

### やること
- `sync-checklist.md` の内容を `.claude/skills/repo-sync-checklist/SKILL.md` としてスキル化（スキルとしての指示文追加）
- `backlog/リポジトリ間テンプレート同期の検証チェックリスト.md` に本スキルの情報を追記

### やらないこと
- チェックリストの内容自体の大幅な変更
- ai-driven-dev-patterns への実際の同期実施

## 期待される効果

- `/repo-sync-checklist` で同期チェックリストを呼び出せるようになる
- 後続施策の L1 が文脈を引き継いで作業を開始できる

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| スキルの配置が他スキルと整合しない | 低 | session-flow-policy を参照して配置を決定 |

## 壁打ちの背景

- スキル名は `repo-sync-checklist`、配置先は `.claude/skills/repo-sync-checklist/SKILL.md`
- スキルとしての指示文を追加し、同期作業時にこのチェックリストに従って作業を進められる形にする
- 後続施策でこのスキルを使って実際に連携を行える状態を目指す

---
**起票者**: L1
**起票日**: 2026-03-08
**ステータス**: 承認済
