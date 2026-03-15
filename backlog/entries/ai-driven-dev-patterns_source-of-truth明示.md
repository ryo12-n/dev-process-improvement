# ai-driven-dev-patterns Source of Truth 明示

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-018 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | ai-driven-dev-patterns |
| **起票日** | 2026-03-08 |

## 課題・背景

ai-driven-dev-patterns において、CLAUDE.md と roles/dev_manager.md に知見ルーティングテーブルが重複しており、将来的な乖離リスクがある。dev-process-improvement では「.claude/skills/ 配下が正の情報源（Source of Truth）」と CLAUDE.md に明記しており、同様のパターンを ai-driven-dev-patterns にも適用すべき。

具体的には CLAUDE.md に「roles/ 配下のロール定義が正の情報源。CLAUDE.md は概要のみ記載」と明記するルールを .claude/rules/ に追加する。

## 期待効果

- 知見ルーティングテーブルの乖離リスク防止
- 情報源の一元化による保守コスト削減

## 補足・参考情報

- 起票元: design-process-setup 施策（08_gate_review.md）
- 評価者（L2-evaluator）も同一課題を指摘しており、2層管理の設計自体は妥当だが正の情報源の明示が不足している点で一致
- inbox からの移行（2026-03-08 トリアージ）
- **前提変化（2026-03-12 BM-003 検出）**: roles/ → agents/ 移行完了。agents/ 移行後を見据えた Source of Truth 定義に拡張する必要あり（「roles/ が正の情報源」→ 移行後は「agents/ が正の情報源」に更新）
