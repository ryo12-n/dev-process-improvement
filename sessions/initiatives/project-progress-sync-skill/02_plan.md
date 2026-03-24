# 実施計画: project-progress-sync-skill

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| Phase B | knowledge テンプレート作成 + スキル作成 | テンプレートとスキルが作成されていること |

## 成功基準（全体）

1. `projects/_initiative_template/knowledge.md` テンプレートが作成されていること
2. `.claude/skills/project-progress-sync/SKILL.md` が作成され、user-invocable であること
3. スキルが todo.md, knowledge.md, plan.md の3ファイルを更新対象としていること

## リソース・前提条件
- 単一ワーカーで実施（M規模）
- 既存の `projects/_initiative_template/` の構成を維持

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 施策→プロジェクト紐づけの判定が困難 | 中 | 中 | スキル実行時にプロジェクト名を引数で指定する |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
