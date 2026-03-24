# session-flow-policy に「担当ファイルセクション必須」を追加

## 背景

`l1-no-direct-work-enforcement` 施策で、L1 SKILL.md に「担当ファイル」セクションが欠落していたことが判明した。L2-worker / L2-evaluator には既に存在していたが、L1 には同等のセクションがなかった。

## 提案

`session-flow-policy` に、新規セッション種別作成時のチェック項目として「担当ファイルセクションの必須化」を追加する。

## 期待効果

新規セッション種別で担当ファイルテーブルの漏れを防止し、セッション間の責務境界を構造的に明確化できる。

---
**起票元**: `sessions/initiatives/l1-no-direct-work-enforcement/05_gate_review.md`
**起票日**: 2026-03-24
