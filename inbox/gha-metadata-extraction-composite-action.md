# メタデータ取得ロジックの composite action 共通化

## 提案
initiative-dispatcher.yml と initiative-batch-approve.yml で重複しているメタデータ取得ロジック（`gh api` + `jq select` + `grep/sed`）を composite action に共通化する。

## 背景
gha-pipeline-autorun 施策の L2-evaluator が参考情報として指摘。現時点では2箇所のみであり、共通化のコスト対効果は要検討。

---
**起票日**: 2026-03-19
