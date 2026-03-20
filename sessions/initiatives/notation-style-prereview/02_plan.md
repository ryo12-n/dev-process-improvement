# 実施計画: notation-style-prereview

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | l2-worker.md にチェック項目追加・docs/workflow.md 確認・連動更新 | 1セッション | チェック項目が追加され、docs/workflow.md が整合している |

## スケジュール

- Phase 1: L2-worker が 1 セッションで完結

## 成功基準（全体）

1. `.claude/skills/l1-manager/agents/l2-worker.md` の「前提条件チェック」または「外部リポジトリでの作業手順」に記法スタイル確認項目が 1 項目以上追加されている
2. `docs/workflow.md` の L2-worker 壁打ちフェーズ記述が l2-worker.md の変更と整合している（または更新不要と判断・記録されている）
3. 変更が施策ブランチにコミット・プッシュ済み

## リソース・前提条件

- 対象ファイル: `.claude/skills/l1-manager/agents/l2-worker.md`, `docs/workflow.md`
- dev-process-improvement リポジトリのみで完結（外部リポジトリ不要）
- ローカル CLI / SDK どちらでも実施可能

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| docs/workflow.md の記述が抽象的で更新不要と判断される | 中 | 低 | 「更新不要」と判断した根拠を work_report に記録する |
| l2-worker.md の変更が連動ファイル（l2-evaluator.md 等）に影響する | 低 | 低 | l2-worker.md の「関連ファイル一覧」を参照し、今回の変更が対称性要件に影響しないことを確認する |

---
**作成者**: L1
**作成日**: 2026-03-20
**最終更新**: 2026-03-20
