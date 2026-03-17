# knowledge.md テーブルの肥大化リスク

## 気づき

`refs/agency-agents/knowledge.md` の施策タイプ別推奨マッピングテーブルに Evaluator 向け推奨列を追加したことで8列に増加。今後施策タイプが増えるとさらにテーブルが肥大化し、可読性・保守性が低下する。

## 提案

- Worker/Evaluator 別建てテーブルへの分離
- または施策タイプ別の詳細定義ファイルへの分割

## 発見元

`sessions/initiatives/l1-manager-enhanced-planning/` 施策フェーズ3 ワーカー知見（T3-005）

---
**起票日**: 2026-03-17
