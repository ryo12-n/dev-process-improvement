# スキャン計画: Phase 3（最適化提案）

## 壁打ちフェーズ [2026-03-15 13:30]

### 理解のサマリー
- タスクの目的: Phase 2 で特定された22件のギャップに対し、Impact x Effort で優先順位付けした具体的な最適化提案（OPT-001〜OPT-007 + マトリクス）を作成する
- スコープ: CO-001〜CO-007 の全ギャップ。高重要度3件 + 中重要度5件 + 評価者補足2件
- 完了条件: 全ギャップに実装例付き提案、Quick Wins の特定、バックログエントリとして転記可能な具体性

### 前提条件チェック
- [x] 割り当てタスクの内容を理解: 理解済み（01_tasks.md 確認）
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み（Phase 2 レポート・課題・リファレンス・設定ファイル全て存在）
- [x] 前フェーズの成果物（該当する場合）の確認: 確認済み（set-2/04_scan_report.md, set-2/07_issues.md, 25_analysis_gate.md）

### 不明点・確認事項
なし。Phase 2 の分析結果とリファレンスで十分な情報が揃っている。

---

## スキャン計画

### 走査対象

| # | 対象 | 走査方法 | 期待する出力 |
|---|------|---------|------------|
| 1 | CO-001: settings.json deny 代替 | Phase 2 ギャップ + リファレンス §1/§4 を基に PreToolUse hook 実装例を設計 | OPT-001: 実装例付き提案 |
| 2 | CO-002: rules/ 最適化 | Phase 2 ギャップ + リファレンス §2 を基に path-scoped 導入 + commit-message.md 分離を設計 | OPT-002: paths フロントマター・分離案 |
| 3 | CO-003: skills/ 最適化 | Phase 2 ギャップ + リファレンス §3 を基に disable-model-invocation 設定を設計 | OPT-003: 対象スキル・変更例 |
| 4 | CO-004: hooks/ 拡充 | Phase 2 ギャップ + リファレンス §4 を基に PostToolUse/Stop 活用を設計 | OPT-004: ユースケース・実装例 |
| 5 | CO-005: CLAUDE.md 縮小 | Phase 2 分離候補 + リファレンス §5 を基に import(@) + rules/ 委譲計画を設計 | OPT-005: 分離対象・期待行数 |
| 6 | CO-006: プラグイン導入 | Phase 2 ギャップ + リファレンス §6 を基に導入計画を設計 | OPT-006: 導入順序・コマンド例 |
| 7 | CO-007: sandbox + その他 | Phase 2 ギャップ + リファレンス §7 を基に sandbox 有効化 + settings.local.json を設計 | OPT-007: 設定例 |
| 8 | 全提案マトリクス | OPT-001〜007 を Impact x Effort で分類 | Quick Wins / Strategic / Easy Adds / Nice-to-Have |

### 走査順序・依存関係

- OPT-001（PreToolUse hook）→ OPT-007（sandbox）: セキュリティの二重防御として関連。OPT-001 を先に設計し、OPT-007 で補完する
- OPT-002（path-scoped rules）→ OPT-005（CLAUDE.md 縮小）: OPT-005 の rules/ 委譲は OPT-002 の path-scoped 導入と連動する
- OPT-003, OPT-004, OPT-006 は独立して設計可能
- マトリクスは全提案完了後に作成

---
**作成者**: config-proposal-worker
**作成日**: 2026-03-15
