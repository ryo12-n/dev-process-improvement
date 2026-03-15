# backlog エントリの「対象リポジトリ」列：精査対象ファイル所在リポジトリの明記

## 気づき

backlog の `対象リポジトリ` 列は「施策の主な作業対象ファイルが存在するリポジトリ」を記載すべきだが、dev-workflow-detail-l1-ref-review 施策では `dev-process-improvement` と記載されていた。実際の精査対象は `ai-driven-dev-patterns` の `docs/design/dev-workflow-detail.md` であり、GHA 環境（1リポジトリ制約）での実施可否判断を誤らせる可能性があった。

## 提案

backlog 起票ガイドライン（または `l1-manager` スキルのタスク作成ガイド）に以下を追記する：

- `対象リポジトリ` 列には「精査・変更対象ファイルが実際に存在するリポジトリ」を記載する
- 複数リポジトリにまたがる場合は「横断」とし、制約事項に両リポジトリ名を明記する
- GHA 環境（SDK 環境）は1リポジトリ制約があるため、起票時点で実行環境の選定に影響する

## 背景

- 施策: dev-workflow-detail-l1-ref-review
- 発見者: L2 Worker（実施・評価とも同様の知見）

---
**記録日**: 2026-03-15
**発生施策**: dev-workflow-detail-l1-ref-review
