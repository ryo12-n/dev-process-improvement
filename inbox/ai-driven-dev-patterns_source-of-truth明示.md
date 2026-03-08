# ai-driven-dev-patterns の Source of Truth 明示パターン

- **起票日**: 2026-03-08
- **起票元**: design-process-setup 施策（08_gate_review.md）
- **種別**: 改善提案
- **内容**: ai-driven-dev-patterns において、CLAUDE.md と roles/dev_manager.md に知見ルーティングテーブルが重複しており、将来的な乖離リスクがある。dev-process-improvement では「.claude/skills/ 配下が正の情報源（Source of Truth）」と CLAUDE.md に明記しており、同様のパターンを ai-driven-dev-patterns にも適用すべき。具体的には CLAUDE.md に「roles/ 配下のロール定義が正の情報源。CLAUDE.md は概要のみ記載」と明記するルールを .claude/rules/ に追加する。
- **補足**: 評価者（L2-evaluator）も同一課題を指摘しており、2層管理の設計自体は妥当だが正の情報源の明示が不足している点で一致。
