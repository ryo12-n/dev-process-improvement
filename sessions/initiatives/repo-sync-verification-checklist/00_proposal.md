# 改善施策提案: リポジトリ間テンプレート同期の検証チェックリスト

## 背景・課題

triage-process-brushup 施策の評価で、リポジトリ間テンプレート同期時に有効だった7つの検証観点が発見された。現在、同期作業は `[sync]` コミット種別で行われるが、対応するセッションスキル（マネージャー・ワーカー・評価者）が存在せず、同期作業の品質管理が構造化されていない。

既存の `repo-sync-checklist` スキルは「同期時に何を確認するか」（作業チェックリスト）を提供するが、「同期結果が正しいか」（検証チェックリスト）は含まれていない。

## 目標

1. 専用の sync セッションタイプ（sync-manager + sync-worker + sync-evaluator）を新設する
2. 既存の `repo-sync-checklist` に7つの検証観点をパラメータ化して追加する
3. session-flow-policy に準拠した構造で、他セッションタイプとの整合性を確保する

## スコープ

### やること

- `.claude/skills/sync-manager/SKILL.md` の作成（マネージャースキル）
- `.claude/skills/sync-manager/agents/sync-worker.md` の作成（同期ワーカー）
- `.claude/skills/sync-manager/agents/sync-evaluator.md` の作成（検証評価者）
- `sessions/sync/_template/` の作成（セッションテンプレート9ファイル）
- `.claude/skills/repo-sync-checklist/SKILL.md` へのセクション5追加
- 連動更新（commit-message.md、workflow.md、session-flow-policy、triage-standard-policy）

### やらないこと

- 既存の `[sync]` コミット種別の廃止（git レベル同期用に温存）
- 実際の同期作業の実施（本施策はセッション基盤の構築のみ）

## 期待される効果

- 同期作業の品質が構造化された検証で担保される
- 7つの検証観点が標準化され、同期対象に依存しない汎用的な検証が可能になる
- マネージャー → ワーカー → 評価者のフローにより、同期漏れの早期検出が可能になる

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| セッションタイプ間の構造不整合 | 中 | session-flow-policy のチェックリスト（§5.1）に従って確認 |
| 連動更新の漏れ | 中 | rule-change-checklist を参照して確認 |

## 壁打ちの背景

### 意思決定の記録

1. **追加 vs 新規スキル**: 既存の `repo-sync-checklist` に検証セクションを追加する方針。使用タイミングが同じであれば1つに統合する方が効率的（ユーザー判断）
2. **7観点の汎用化**: パラメータ化（`{source_repo}`, `{target_repo}`, `{sync_scope}`）で任意の同期ターゲットに適用可能にする
3. **セッション構成**: initiative セッションを参考に、マネージャー・実施ワーカー・評価ワーカーの3ロール構成（B案を採用）
4. **コミット種別**: `sync-mgr` / `sync-worker` / `sync-eval` を新設。既存 `sync` は git レベル同期用に温存

---
**起票者**: L1
**起票日**: 2026-03-08
**ステータス**: 実施中
