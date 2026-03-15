# backlog-auto-execute.yml への GHA スキル分離パターン適用

## 背景

gha-initiative-skills-separation 施策で initiative ワークフロー4つに GHA 専用スキルを作成し、YAML プロンプトのリファクタを完了した。`backlog-auto-execute.yml` も同様のスコープクリープリスクがあるが、スコープ限定のため本施策では対象外とした。

## 提案

`backlog-auto-execute.yml` に対しても同パターン（`gha-auto-execute/SKILL.md` 作成 + YAML プロンプトリファクタ + execution_file 修正）を適用する。

## 起票元

`sessions/initiatives/gha-initiative-skills-separation/08_gate_review.md` 横展開セクション
