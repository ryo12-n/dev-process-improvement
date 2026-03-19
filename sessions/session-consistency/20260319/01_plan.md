# セッション一貫性チェック実施計画: 2026-03-19

## 今回の実施スコープ

### 実施する SC ターゲット

- [x] SC-001: SKILL.md 構造準拠
- [x] SC-002: エージェント定義構造準拠
- [x] SC-003: Worker ↔ Evaluator 対称性
- [x] SC-004: テンプレート ↔ エージェント担当ファイル整合
- [x] SC-005: manager-common-policy 準拠
- [x] SC-006: session-lifecycle-policy 適用マトリクス整合
- [x] SC-007: commit-message 規約カバレッジ
- [x] SC-008: 関連ファイル一覧の相互参照整合

### 実施しない対象と理由

- なし（全8ターゲットを実施）

## 今回の重点

1. SC-008: 関連ファイル一覧の相互参照整合 — リネーム（#140）・構造変更（#138, #155）後の参照切れリスクが高い
2. SC-006: session-lifecycle-policy 適用マトリクス整合 — triage-standard-policy → session-lifecycle-policy リネーム後の整合性確認
3. SC-003: Worker ↔ Evaluator 対称性 — l1-manager 拡張（l2-plan-worker / l2-plan-evaluator 追加）後の新ペア対称性

## フェーズ計画

### Phase 1: 情報収集

| 項目 | 内容 |
|------|------|
| タスクファイル | `phase-1-collection/set-1/01_tasks.md` |
| ワーカー | sc-collection-worker |
| 重点収集対象 | リファレンスの全面更新（前回 2026-03-17 から多数の変更あり）。特に session-lifecycle-policy リネーム後の参照状態、l1-manager 拡張後のエージェント構成 |

### Phase 2: 現状分析

| 項目 | 内容 |
|------|------|
| タスクファイル | `phase-2-analysis/set-1/01_tasks.md` |
| ワーカー | sc-analysis-worker |
| 重点分析対象 | SC-008（参照切れ）、SC-006（マトリクス整合）、SC-003（ペア対称性）を優先的に分析 |

### Phase 3: 改善提案

| 項目 | 内容 |
|------|------|
| タスクファイル | `phase-3-proposal/set-1/01_tasks.md` |
| ワーカー | sc-proposal-worker |
| 提案の方向性 | 前回指摘の Quick Wins 残件の確認、リネーム後の残存不整合の修正提案、新ペアの対称性確保 |

## 完了基準

- [ ] Phase 1〜3 の全ゲートが通過している
- [ ] 各フェーズのワーカーレポートが評価者に承認されている
- [ ] 集約レポート（03_report.md）が作成されている
- [ ] 高優先度の提案が backlog/entries/ に転記されている
- [ ] PR を作成してユーザーにレビューを依頼している

---
**作成者**: session-consistency-manager
**作成日**: 2026-03-19
