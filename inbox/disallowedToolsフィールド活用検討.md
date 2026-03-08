# disallowedTools フィールドの活用検討

## 背景

`cli-permission-verification` 施策で、エージェント定義の `tools` フィールドでは deferred tools（ToolSearch 経由でロードされるツール）を制限できないことが判明した（ISS-047）。

`tools: ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]` と指定しても、WebSearch, WebFetch, NotebookEdit 等が ToolSearch 経由で利用可能。

## 提案内容

`disallowedTools` フィールドで明示的にツールを禁止する方法を検討する:
- L2-worker / L2-evaluator のエージェント定義に `disallowedTools` を追加
- 不要なツール（WebSearch, CronCreate 等）を明示的に禁止
- `disallowedTools` が deferred tools にも適用されるかの検証

## 関連情報
- ISS-047
- `docs/subagent-permission-guide.md` セクション3
- 発見元施策: `cli-permission-verification`
