# gha-test/SKILL.md に「やらないこと」セクション追加

## 気づき
gha-guideline セクション7.7 で検証用テンプレートを定義したが、gha-test/SKILL.md 本体に「やらないこと」セクションが欠如している。

## 発見元
sessions/initiatives/batch-gha-minor-fixes — L2-evaluator 修正提案

## 提案
gha-test/SKILL.md に以下を追加:
- `git rebase`, `git reset --hard` 等の破壊的 git 操作禁止
- 本番データ（`sessions/initiatives/` 内の実施策）の変更禁止

---
**起票日**: 2026-03-24
