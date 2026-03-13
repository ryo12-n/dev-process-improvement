# claude-code-action バージョン追従ルール

## 背景
施策 `backlog-auto-initiative-gha` で `anthropics/claude-code-action@v1` を導入したが、OIDC 認証に `id-token: write` が必須であり、GitHub Issue #1010 でセキュリティ懸念が指摘されている。将来のバージョンアップで改善される可能性がある。

## 提案
claude-code-action のバージョンアップ時に以下を再確認する手順を制度化する:
- `id-token: write` 権限の必要性が解消されているか
- 新しい inputs/outputs の追加があるか
- 破壊的変更の有無

## 起票元
- 施策: `sessions/initiatives/backlog-auto-initiative-gha/`
- 評価レポート: `06_eval_report.md` 参考情報 #1
