# 実施計画: リポジトリ間テンプレート同期の検証チェックリスト

## フェーズ構成

本施策は単一フェーズで完了する。

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | sync セッションタイプの構築 + 検証チェックリスト追加 + 連動更新 | 下記5項目 |

## 成功基準（全体）

1. `.claude/skills/sync-manager/SKILL.md` が session-flow-policy の SKILL.md 必須要素（§2）を満たしている
2. `agents/sync-worker.md` と `agents/sync-evaluator.md` がエージェント定義の必須要素（§3）を満たし、ペアリング対称性要件を満たしている
3. `sessions/sync/_template/` に9ファイル（00〜08）が存在する
4. `repo-sync-checklist/SKILL.md` にセクション5（7つの検証観点）が追加されている
5. 連動更新が完了している:
   - `commit-message.md` に `sync-mgr` / `sync-worker` / `sync-eval` が追加されている
   - `docs/workflow.md` に同期セッションフローが追記されている
   - `session-flow-policy` の既存セッションタイプ一覧に sync が追加されている
   - `triage-standard-policy` の適用マトリクス・ペアリング構造・走査対象に sync が追加されている

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| セッションタイプ間の構造不整合 | 低 | 中 | session-flow-policy §5.1 チェックリストに従う |
| 連動更新の漏れ | 中 | 中 | rule-change-checklist を参照 |

---
**作成者**: L1
**作成日**: 2026-03-08
**最終更新**: 2026-03-08
