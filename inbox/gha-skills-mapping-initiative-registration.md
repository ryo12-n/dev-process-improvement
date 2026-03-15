# gha-skills-mapping.yml に initiative ワークフロー4件のマッピング追加

## 背景

gha-initiative-skills-separation 施策で GHA 専用スキル4つ（gha-wallbash, gha-execute, gha-close, gha-question）を作成したが、`.github/gha-skills-mapping.yml` にこれら4件のマッピングが未登録。TG-010（GHA↔Skills 整合性チェック）でドリフト検出ができない状態。

## 提案

`gha-skills-mapping.yml` に以下4件を追加:
- `initiative-wallbash.yml` → `.claude/skills/gha-wallbash/SKILL.md`
- `initiative-execute.yml` → `.claude/skills/gha-execute/SKILL.md`
- `initiative-close.yml` → `.claude/skills/gha-close/SKILL.md`
- `initiative-question.yml` → `.claude/skills/gha-question/SKILL.md`

## 起票元

`sessions/initiatives/gha-initiative-skills-separation/07_issues.md`
