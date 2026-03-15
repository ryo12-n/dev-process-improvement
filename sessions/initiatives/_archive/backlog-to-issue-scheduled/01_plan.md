# 実施計画: backlog-to-issue-scheduled

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | スクリプト改修・ワークフロー改修・不要ファイル削除 | 1セッション | 全変更がコミット済み、既存 workflow_dispatch 動作に影響なし |

## スケジュール
- フェーズ1: 全タスクを1セッションで完了

## 成功基準（全体）
1. `backlog-to-issue.yml` に `schedule` トリガー（6時間ごと）が設定されている
2. `select-backlog-candidate.sh` が全優先度（低→中→高順）で候補を選定し、BL-ID を出力する
3. 重複チェック（既存 Issue の BL-ID 検索）が実装されている
4. `backlog-candidate-propose.yml` と `backlog-auto-execute.yml` が削除されている
5. GHA セキュリティルール（`${{ }}` の `env:` 経由渡し）に準拠している

## リソース・前提条件
- 既存ワークフロー: `backlog-to-issue.yml`、`select-backlog-candidate.sh`
- GHA セキュリティガイドライン: `.claude/rules/gha-workflow-security.md`

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| schedule と workflow_dispatch の共存による条件分岐の複雑化 | 中 | 低 | ジョブを分離して独立性を確保 |
| 既存 workflow_dispatch の回帰 | 低 | 中 | 手動トリガー部分は既存ロジックを維持 |

---
**作成者**: L1
**作成日**: 2026-03-15
**最終更新**: 2026-03-15
