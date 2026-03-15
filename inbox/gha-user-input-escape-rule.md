# GHA ワークフローでのユーザー入力エスケープルール

## 背景
initiative-dispatcher 施策（ISS-059）で、`issue_comment` 経由のユーザー入力が shell 変数に展開される際にシェルインジェクションのリスクが発覚した。

## 提案
`.claude/skills/gha-guideline/SKILL.md` または `.claude/rules/` に以下のルールを追加する:

1. **`eval` の使用禁止**: ワークフロー内でユーザー入力を含む変数に `eval` を使用しない
2. **`jq` エスケープの推奨**: JSON 構築時は `jq -Rn --arg v "$VAR" '$v'` でエスケープする
3. **`-f` フラグ直接指定の推奨**: `gh workflow run` では `-f key="$value"` 形式で直接指定する

## 起票元
- 施策: `sessions/initiatives/initiative-dispatcher/`
- 評価レポート: `06_eval_report.md` E-008
- 課題: ISS-059
