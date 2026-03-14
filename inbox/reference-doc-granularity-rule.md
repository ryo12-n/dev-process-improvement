# リファレンス文書の評価粒度基準のルール化

## 背景
claude-code-plugin-skills-survey 施策の評価で、リファレンス文書（builtin-skills-reference, plugin-reference）の記述粒度基準が暗黙的であることが判明。

## 提案
適用可能性「高」「中」は4要素（機能概要・適用可能性・具体的利用シーン・制約事項）を必須とし、「低」「対象外」は1行の理由で十分とする基準を、L2-worker 向けタスク完了条件のテンプレートに組み込む。

## 関連
- 元施策: `sessions/initiatives/claude-code-plugin-skills-survey/`
- 評価レポート: `06_eval_report.md` のルール化候補#1
