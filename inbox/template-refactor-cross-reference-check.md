# テンプレートリファクタ時のテンプレート内相互参照チェック

## 起票元
- 施策: `sessions/initiatives/session-artifacts-structure-refactor/`
- 発見者: L2-evaluator（06_eval_report.md）

## 気づき

テンプレートファイルのリネーム・移動を行う施策で、SKILL.md とエージェント定義のみを参照更新チェック対象にすると、テンプレートファイル内の相互参照（gate_summary → gate ファイルパス、file_task_division → work_log パス、work_report → work_log パス等）の更新漏れが発生する。

## 提案

メタルール横断検証（T-006 相当のタスク）のチェック対象に「テンプレートファイル内の旧ファイル名パターン grep」を追加する。具体的には `sessions/*/_template/` 配下の全 `.md` ファイルを grep 対象に含める。

## 対象
- `.claude/skills/l1-manager/SKILL.md` のメタルール横断検証タスクの記述
- または `rule-change-checklist` スキル
