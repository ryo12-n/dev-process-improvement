# ワーカータスク指示: Set-4

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-010 | GHA/Skills | `.github/gha-skills-mapping.yml` に基づくドリフト検出 | 全マッピングのチェック完了、ドリフト重大度判定済み |

## 走査時の注意事項

- `.github/gha-skills-mapping.yml` が存在することは確認済み
- 前回トリアージ（20260315-2）以降に `.claude/skills/` と `.github/prompts/` に多数の変更がマージされている
- マッピングマニフェストの各 mapping について、checkpoints（task_ids, workflow_steps, report_sections, file_templates, file_numbers）を突合すること
- inherent_differences が実際にまだ有効かを検証すること
- ドリフト重大度: CRITICAL（Skill にあるが GHA にないタスクID等）/ WARNING（ステップ・構造の不一致）/ INFO（軽微な差異）

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-17
