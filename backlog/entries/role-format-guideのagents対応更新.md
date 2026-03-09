# role-format-guide の agents 対応更新

## メタ情報

| 項目 | 内容 |
|------|------|
| **優先度** | 低 |
| **ステータス** | 候補 |
| **起票日** | 2026-03-08 |

## 課題・背景

ai-driven-dev-patterns リポジトリの `role-format-guide` スキル（`.claude/skills/role-format-guide/SKILL.md`）が `roles/*.md` を前提としたフォーマットガイドになっている。roles/ → .claude/agents/ 移行が完了したため、agents 形式（YAML フロントマター）に合わせた更新が必要。

## 期待効果

- 新規エージェント作成時のフォーマットガイドが実態と一致する
- ケバブケース命名規則、YAML フロントマターの必須フィールド等が明文化される

## 補足・参考情報

- 前提施策: `sessions/initiatives/roles-agents-migration/`
- 対象ファイル: `.claude/skills/role-format-guide/SKILL.md`（ai-driven-dev-patterns 側）
