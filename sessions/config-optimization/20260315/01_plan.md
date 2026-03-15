# config最適化セッション実施計画: 2026-03-15

<!-- 00_pre_investigation.md の結果を受けて作成する -->

## 今回の実施スコープ

### 実施する CO ターゲット

- [x] CO-001: settings.json（permissions, hooks, sandbox, model config）
- [x] CO-002: .claude/rules/（構成、path-scoping、内容品質）
- [x] CO-003: .claude/skills/（構成、description最適化、コンテキスト予算）
- [x] CO-004: .claude/hooks/（フックタイプカバレッジ）
- [x] CO-005: CLAUDE.md（構造、サイズ、import(@)活用）
- [x] CO-006: プラグイン導入（plugin-reference との整合）
- [x] CO-007: その他（permission パターン、settings.local.json、memory、sandbox）

### 実施しない対象と理由

- 全 CO ターゲットを実施（初回セッションのため全領域をベースライン調査）

## 今回の重点

1. CO-005（CLAUDE.md）— 192行で150行目標を42行超過。import(@) 未使用で rules/ への委譲余地あり
2. CO-003（skills/）— 24スキルでコンテキスト予算約48%消費。description 最適化によるトリガー精度向上の余地
3. CO-004（hooks/）— SessionStart のみ使用中。PreToolUse/PostToolUse/Stop の活用余地を調査

## フェーズ計画

### Phase 1: 情報収集

| 項目 | 内容 |
|------|------|
| タスクファイル | `workers/set-1/01_tasks.md` |
| ワーカー | config-collection-worker |
| 重点収集対象 | リファレンススナップショット初回収集（公式ドキュメントからのベストプラクティス）、全7ターゲットの現状データ収集 |

### Phase 2: 現状分析

| 項目 | 内容 |
|------|------|
| タスクファイル | `workers/set-2/01_tasks.md` |
| ワーカー | config-analysis-worker |
| 重点分析対象 | CLAUDE.md のサイズ・構造分析、skills description のトリガー精度、hooks カバレッジのギャップ分析 |

### Phase 3: 最適化提案

| 項目 | 内容 |
|------|------|
| タスクファイル | `workers/set-3/01_tasks.md` |
| ワーカー | config-proposal-worker |
| 提案の方向性 | CLAUDE.md の import(@) 活用によるサイズ削減、skills description 最適化、hooks 拡張（PreToolUse/PostToolUse 活用）、path-scoped rules 活用 |

## 完了基準

- [ ] Phase 1〜3 の全ゲートが通過している
- [ ] 各フェーズのワーカーレポートが評価者に承認されている
- [ ] 集約レポート（03_report.md）が作成されている
- [ ] 高優先度の提案が backlog/entries/ に転記されている
- [ ] PR を作成してユーザーにレビューを依頼している

---
**作成者**: config最適化マネージャー
**作成日**: 2026-03-15
