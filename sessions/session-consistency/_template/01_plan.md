# セッション一貫性チェック実施計画: YYYY-MM-DD

<!-- 00_pre_investigation.md の結果を受けて作成する -->

## 今回の実施スコープ

### 実施する SC ターゲット

- [ ] SC-001: SKILL.md 構造準拠
- [ ] SC-002: エージェント定義構造準拠
- [ ] SC-003: Worker ↔ Evaluator 対称性
- [ ] SC-004: テンプレート ↔ エージェント担当ファイル整合
- [ ] SC-005: manager-common-policy 準拠
- [ ] SC-006: triage-standard-policy 適用マトリクス整合
- [ ] SC-007: commit-message 規約カバレッジ
- [ ] SC-008: 関連ファイル一覧の相互参照整合

### 実施しない対象と理由

<!-- 今回はスコープ外にするものがあれば記載 -->
-

## 今回の重点

<!-- 00_pre_investigation.md のサマリから転記 -->
1.
2.
3.

## フェーズ計画

### Phase 1: 情報収集

| 項目 | 内容 |
|------|------|
| タスクファイル | `workers/set-1/01_tasks.md` |
| ワーカー | sc-collection-worker |
| 重点収集対象 | <!-- 事前調査で特に収集が必要と判断した領域 --> |

### Phase 2: 現状分析

| 項目 | 内容 |
|------|------|
| タスクファイル | `workers/set-2/01_tasks.md` |
| ワーカー | sc-analysis-worker |
| 重点分析対象 | <!-- 事前調査で特に不整合が疑われる領域 --> |

### Phase 3: 改善提案

| 項目 | 内容 |
|------|------|
| タスクファイル | `workers/set-3/01_tasks.md` |
| ワーカー | sc-proposal-worker |
| 提案の方向性 | <!-- 事前調査を踏まえた提案の方向性 --> |

## 完了基準

- [ ] Phase 1〜3 の全ゲートが通過している
- [ ] 各フェーズのワーカーレポートが評価者に承認されている
- [ ] 集約レポート（03_report.md）が作成されている
- [ ] 高優先度の提案が backlog/entries/ に転記されている
- [ ] PR を作成してユーザーにレビューを依頼している

---
**作成者**: session-consistency-manager
**作成日**: YYYY-MM-DD
