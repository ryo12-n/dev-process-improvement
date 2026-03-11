# rule-change-checklist の grep 走査対象に docs/ を明示追加

## 発見元
メタ認知セッション 2026-03-11 / MC-001 パターン4

## 概要
rule-change-checklist の grep 走査対象に `docs/` が明示的に含まれていないため、ルール変更時に docs/ 配下のガイド文書に旧パス参照が残存する問題が12施策以上で繰り返し発生している。

## 提案
- rule-change-checklist SKILL.md の grep 走査対象リストに `docs/` を明示追加する
- 併せて `backlog/` も走査対象に含めるか検討する

## 関連
- ISS-054（CSV転記済み）
- MC-001 パターン4: grep/パス参照検証の必要性（12施策+）
