# coverage_summary バリデーション強化

## 概要
gen-tests SKILL.md の coverage_summary フィールドについて、by_type / by_priority の合計値が total_test_cases と一致することを機械的に検証するバリデーションステップを追加する提案。

## 背景
ai-dev-chain-gen-tests 施策の評価者が発見した知見。現状は SKILL.md のステップ5（出力整形）で coverage_summary を生成しているが、数値整合性の自動検証は行っていない。

## 期待効果
- テストケース数の集計ミスを自動検出
- gen-ci / gen-tasks 等の後続チェーンでも同様のパターンを適用可能

## 発見元
- `sessions/initiatives/ai-dev-chain-gen-tests/phase-2-execution/set-1/06_eval_report.md` 評価項目7

---
**起票日**: 2026-03-25
**起票元**: ai-dev-chain-gen-tests ゲートレビュー横展開
