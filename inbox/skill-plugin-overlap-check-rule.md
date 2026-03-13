# スキル/プラグイン機能重複の定期チェックルール化

## 背景
builtin-skills-reference と plugin-reference の両方で類似機能の評価が存在する（例: /simplify と code-simplifier）。リファレンス文書が2つに分かれたことで、機能重複の把握が煩雑になるリスクがある。

## 提案
スキルとプラグインの機能重複を定期的にチェックし、統合・整理するタイミングをルール化する。

## 関連
- builtin-skills-reference: `.claude/skills/builtin-skills-reference/SKILL.md`
- plugin-reference: `.claude/skills/plugin-reference/SKILL.md`
- 元施策: `sessions/initiatives/claude-code-plugin-skills-survey/`
