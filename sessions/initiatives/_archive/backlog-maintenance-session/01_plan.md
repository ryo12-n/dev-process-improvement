# 実施計画: backlogメンテナンスセッション作成

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | セッションタイプ実装（SKILL.md, agents/, テンプレート） | session-flow-policy §5.1 チェックリスト全項目クリア |
| 2 | 関連ファイル連動更新（workflow.md, commit-message.md 等） | 既存ファイルとの整合性確認完了 |

## 成功基準（全体）

1. `.claude/skills/backlog-maintenance-manager/SKILL.md` が session-flow-policy §2 の必須要素を含んでいる
2. `agents/` にワーカー・評価者のペアが定義され、ペアリング対称性要件（§3.2）を満たしている
3. `sessions/backlog-maintenance/_template/` にワーカーセット用テンプレートが用意されている
4. `docs/workflow.md` に新セッションタイプのフローが追記されている
5. `.claude/rules/commit-message.md` に新セッション種別（`bm-mgr`, `bm-worker`, `bm-eval`）が追加されている
6. `.claude/skills/session-flow-policy/SKILL.md` §5 の既存セッションタイプ一覧に追加されている
7. `.claude/skills/manager-common-policy/SKILL.md` §1 の適用対象テーブルに追加されている

## リソース・前提条件

- 参照する既存セッションタイプ: triage-manager, metacognition-manager
- session-flow-policy, manager-common-policy の既存ポリシーに準拠
- 新セッションの作業フォルダは triage と同じ構造（マネージャー直下ファイル + workers/set-N/）

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 既存ファイルの連動更新漏れ | 中 | 中 | session-flow-policy §5.1 チェックリストで網羅確認 |
| BMタスクの観点がトリアージ TG-002 と重複 | 低 | 低 | スコープ分離を SKILL.md に明記 |

---
**作成者**: L1
**作成日**: 2026-03-10
**最終更新**: 2026-03-10
