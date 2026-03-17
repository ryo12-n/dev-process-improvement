# session-flow-policy §5.1 に §1.2/§1.3 列数一致確認を追加

## 背景

session-consistency-manager 施策の評価時に、triage-standard-policy §1.2（適用マトリクス）と §1.3（記録先対応テーブル）のセッションタイプ列数が不一致であることが発見された（§1.2 に co-* 列があるが §1.3 には欠落）。

新セッションタイプ追加時に §1.2 への列追加は実施されるが §1.3 への追加が漏れるリスクがある。

## 提案

session-flow-policy §5.1 の新セッションタイプ追加チェックリストに「triage-standard-policy §1.2 と §1.3 の列数一致を確認する」項目を追加する。

## 起票元

- 施策: session-consistency-manager
- 評価レポート T-E03 ルール化候補 #1
- 08_gate_review.md 横展開セクション

---
**作成日**: 2026-03-16
