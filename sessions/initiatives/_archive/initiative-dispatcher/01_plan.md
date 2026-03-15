# 実施計画: initiative-dispatcher

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | ディスパッチャー新規作成 + question ワークフロー新規作成 | `initiative-dispatcher.yml` と `initiative-question.yml` が作成されている |
| 2 | 既存ワークフローのトリガー変更 | wallbash / execute / close が `workflow_dispatch` のみで発火する |
| 3 | backlog-to-issue 連携変更 + initiative-start ラベル廃止 | `backlog-to-issue.yml` が直接 wallbash を dispatch する |

## 成功基準（全体）

1. `issue_comment` トリガーを持つ initiative 関連ワークフローが `initiative-dispatcher.yml` のみであること
2. `@ai-task /command` 形式のコメントで全フェーズ（start/approve/reject/question）のルーティングが正しく動作すること
3. フェーズ不一致時にディスパッチャーがエラーコメントを返すこと
4. `backlog-to-issue.yml` が Issue 作成後に wallbash を直接 dispatch すること
5. `initiative-start` ラベルがトリガーとして使用されていないこと

## リソース・前提条件

- `actions: write` パーミッションが GITHUB_TOKEN で `gh workflow run` に使用可能であること
- `workflow_dispatch` の inputs で文字列パラメータの受け渡しが正常に動作すること

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| inputs の文字列長制限 | 低 | 中 | feedback は最大65535文字（GitHub制限）、通常のコメントでは問題なし |
| `gh workflow run` の非同期性 | 低 | 低 | sub-workflow 側で Issue コメントによる状況報告を維持 |
| 移行中の二重発火 | 低 | 低 | 全変更を1コミットでアトミックに適用 |

---
**作成者**: L1
**作成日**: 2026-03-15
**最終更新**: 2026-03-15
