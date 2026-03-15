# GHA トリガー共存時のジョブ分離ルール追加提案

## 気づき
GHA ワークフローで `schedule` と `workflow_dispatch` を共存させる場合、各ジョブに `if: github.event_name == '...'` を明示的に付与しないと、意図しないトリガーでジョブが実行されてしまう。

## 提案
`.claude/rules/gha-workflow-security.md` のチェック項目に以下を追加する:
- `[ ] 複数トリガー共存時は各ジョブに `if: github.event_name == '...'` を設定する`

## 発見元
施策 `backlog-to-issue-scheduled` の worker・evaluator 両方がルール化候補として挙げた知見。

---
**起票日**: 2026-03-15
**発見元施策**: backlog-to-issue-scheduled
