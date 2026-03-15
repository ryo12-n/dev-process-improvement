# user-invocable: false スキルの description 設計パターン

> **バックログ ID**: BL-044


## 種別
ルール改善の種

## 内容
`user-invocable: false` のスキルでは、description に「何の情報を持つか」+「どの文脈で参照するか」の2要素を含めるパターンが有効。

builtin-skills-reference の例:
> Claude Code ビルトイン skills の評価結果・適用可能性の参照。新規 skill の評価・skills 活用の相談・ビルトイン skill の利用判断時に参照する

この形式により、Claude がオンデマンドで適切なタイミングでスキルを自動参照できる。

## 背景
builtin-skills-evaluation 施策の評価中に L2-evaluator が発見した知見。現時点では事例が1件のみであり、パターンの一般化には追加事例の蓄積が必要。

## 出典
- `sessions/initiatives/_archive/builtin-skills-evaluation/06_eval_report.md`（評価中の知見 ルール化候補 #1）
