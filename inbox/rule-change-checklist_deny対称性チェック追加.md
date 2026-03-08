# rule-change-checklist に deny パターンの Read/Write/Edit 対称性チェック項目を追加

## 背景

`cli-permission-verification` 施策で、deny リスト修正時に以下の漏れが発生した:
- 実施ワーカー: Edit deny を追加したが Write `*.pem`/`*.key` を追加し忘れた
- ISS-048 で網羅性チェック不足を指摘しつつ、同一作業内で同種の問題が再発

人的チェックだけでは再発するため、rule-change-checklist にチェック項目を追加して防止したい。

## 提案内容

`rule-change-checklist` スキルに以下のチェック項目を追加:
- 「deny パターン追加時: 同一対象に対して Read/Write/Edit の3ツール全てに deny が設定されているか確認」

## 関連情報
- ISS-048, ISS-050
- `06_eval_report.md` EVL-001
- 発見元施策: `cli-permission-verification`
