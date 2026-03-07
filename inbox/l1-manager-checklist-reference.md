# l1-manager にチェックリスト参照の固定タスクを組み込む

## 背景

施策「ルール変更連動更新標準化」で `.claude/skills/rule-change-checklist/SKILL.md` を作成したが、L1-manager がルール変更施策の 02_tasks.md 作成時にこのチェックリストを参照する仕組みが明示的でない。

## 提案

l1-manager/SKILL.md の「タスクリストに含める固定タスク」セクション（または相当箇所）に、ルール変更施策の場合は `.claude/skills/rule-change-checklist/SKILL.md` の項目を固定タスクとして組み込む旨を追記する。

## 出典

施策「ルール変更連動更新標準化」の 06_eval_report.md（評価者の観察事項）
