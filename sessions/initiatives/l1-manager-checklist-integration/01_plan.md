# 実施計画: l1-manager-checklist-integration

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | `l1-manager/SKILL.md` の「タスクリストに含める固定タスク」セクションに `rule-change-checklist` 参照タスクを追加する | 1セッション | タスクが追加され、適用条件・完了条件が明確に定義されている |
| 2 | 評価：変更後の `l1-manager/SKILL.md` が `rule-change-checklist/SKILL.md` の意図通りに機能するか確認する | 1セッション | 評価レポートで成功基準を達成している |

## スケジュール

- Phase 1: 提案・計画・タスク作成（壁打ち含む）
- Phase 2: L2-worker による実施（`l1-manager/SKILL.md` 変更・連動更新）
- Phase 3: L2-evaluator による評価
- Phase 4: ゲート判定・クローズ

## 成功基準（全体）

1. `l1-manager/SKILL.md` の「タスクリストに含める固定タスク」セクションに、ルール変更施策向けの `rule-change-checklist` 参照タスクが追加されている
2. 適用条件（`.claude/skills/` や `.claude/rules/` 配下のファイルを変更する施策）が明示されている
3. `rule-change-checklist/SKILL.md` の「関連ファイル一覧」に記載されている連動更新が完了している（`docs/workflow.md` 等）

## リソース・前提条件

- `rule-change-checklist/SKILL.md` の内容が確定済みであること（既に確定済み）
- `l1-manager/SKILL.md` の「タスクリストに含める固定タスク」セクションの構造を把握すること

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 「メタルール横断検証」タスクとの重複・整合性問題 | 中 | 低 | 両タスクの役割を明確化し、重複する項目は統合または補完関係として記述する |
| `docs/workflow.md` の連動更新範囲が想定より広い | 低 | 低 | rule-change-checklist/SKILL.md のチェックリストに従い網羅的に確認する |

---
**作成者**: L1
**作成日**: 2026-03-18
**最終更新**: 2026-03-18
