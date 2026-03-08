# 実施計画: fork-sync-rebuild

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | 社内リポジトリの削除と再作成 | 当日 | 2リポジトリが作成され、upstream と同期済み |
| 2 | fork-sync スキルの作成 | 当日 | SKILL.md + repos.json が配置され、PR がマージ済み |
| 3 | MEMORY.md の更新 | 当日 | 新構成に合わせた記載に更新済み |

## スケジュール

- 2026-03-08: 全フェーズを1セッションで実施

## 成功基準（全体）
1. 旧リポジトリ `ai-driven-dev-patterns-fork` が削除されている
2. `ai-driven-dev-patterns` と `dev-process-improvement` の2つの社内リポジトリが作成され、upstream と同期済み
3. fork-sync スキル（SKILL.md + repos.json）が dev-process-improvement に配置されている
4. MEMORY.md が新構成に合わせて更新されている
5. origin + upstream の両方に PR が作成・マージされている

## リソース・前提条件
- gh CLI で ryo-nagata_monotaro / ryo12-n の両アカウントが認証済み
- upstream 側で既にリポジトリ分離が完了している

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| `gh repo delete` の権限不足 | 中 | 低 | GitHub Web UI から手動削除 |
| `gh pr create` の Enterprise 制限 | 高 | 低 | フォールバック URL を提示 |

---
**作成者**: L1
**作成日**: 2026-03-08
**最終更新**: 2026-03-08
