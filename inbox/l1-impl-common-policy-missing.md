# l1-impl-manager が manager-common-policy §1 に未掲載

## 気づき
`manager-common-policy` §1 の適用対象テーブルに `l1-impl-manager` が含まれていない。description も「7つのマネージャー」のままになっている。

実際には l1-impl-manager は §2〜§8 を参照しており、8つ目のマネージャーとして §1 テーブルに追加し description を更新すべき。

## 発見元
- 施策: manager-overview-doc
- 発見者: L2-worker（T-004 grep 結果の突合）、L2-evaluator（T-E03 検証で確認）

## 提案アクション
`manager-common-policy` §1 テーブルに l1-impl-manager の行を追加し、description の「7つ」を「8つ」に修正する。

---
**起票日**: 2026-03-16
