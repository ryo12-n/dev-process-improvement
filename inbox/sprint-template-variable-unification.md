# スプリントテンプレートの変数名統一

## 背景
sprint-template-design 施策の評価で、knowledge.md 内で `{{repository_name}}` と `{{repo}}` の変数名が混在していることが発見された。設計計画書自体の問題であり、将来パーサーや置換処理を導入する際に統一が必要。

## 提案
- knowledge.md 内の `{{repo}}` を `{{repository_name}}` に統一する（または逆方向で統一）
- 全テンプレートファイルの変数名一覧を整理する

## 発見元
sprint-template-design 施策 06_eval_report.md

---
**起票日**: 2026-03-25
