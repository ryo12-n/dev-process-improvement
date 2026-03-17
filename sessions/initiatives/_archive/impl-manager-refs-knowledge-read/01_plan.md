# 実施計画: impl-manager-refs-knowledge-read

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | l1-impl-manager/SKILL.md と 3つの worker エージェント定義に refs 知見参照ステップを追加。ドメインエージェント参照の選定フローを移植 | 全変更対象ファイルに参照ステップが追加されている。メタルール横断検証が合格 |

## 成功基準（全体）

1. l1-impl-manager/SKILL.md の Phase 1-3 タスク作成時に refs 参照ステップがある
2. investigation-worker, design-worker, impl-plan-worker の各エージェント定義に知見読み込み手順がある
3. l1-impl-manager/SKILL.md の Wave ディスパッチ時に impl-worker へ知見要約を渡すステップがある
4. ドメインエージェント参照の選定フローが l1-impl-manager に存在する
5. docs/workflow.md の該当セクションが変更内容と整合している

## リソース・前提条件

- 変更対象ファイル:
  - `.claude/skills/l1-impl-manager/SKILL.md`
  - `.claude/skills/l1-impl-manager/agents/investigation-worker.md`
  - `.claude/skills/l1-impl-manager/agents/design-worker.md`
  - `.claude/skills/l1-impl-manager/agents/impl-plan-worker.md`
- 参照ファイル（変更なし）:
  - `.claude/skills/l1-manager/SKILL.md`（ドメインエージェント参照の実装パターン）
  - `.claude/skills/manager-common-policy/SKILL.md`（§5.3, §10）
  - `refs/agency-agents/knowledge.md`（ドメインエージェントカタログ）

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| knowledge.md が存在しない施策での空振り | 高 | 低 | 「存在する場合に参照」の条件付きステップ |
| 陳腐化した知見による誤誘導 | 中 | 中 | 「参考情報として扱い、最新調査を省略しない」旨を明記 |
| 担当ファイルテーブルの不整合 | 低 | 中 | 変更時に担当ファイルテーブルも更新 |

---
**作成者**: L1
**作成日**: 2026-03-17
**最終更新**: 2026-03-17
