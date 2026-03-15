# GHA スキル6件に disable-model-invocation 設定

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-069 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-15 |
| **起票元** | config-optimization/20260315 OPT-003 |

## 概要

GHA 専用スキル6件（gha-close, gha-execute, gha-guideline, gha-question, gha-test, gha-wallbash）に `disable-model-invocation: true` を追加し、CLI セッションでのコンテキスト消費と誤起動を防止する。

## 期待効果

- ~600トークンのコンテキスト予算節約
- Claude が GHA 専用スキルを誤って自動起動するリスクの排除
- GHA ワークフローからの明示的起動には影響なし
