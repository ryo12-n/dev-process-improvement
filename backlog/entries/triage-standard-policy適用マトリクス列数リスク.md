# triage-standard-policy テーブル幅肥大化への対応検討

> **バックログ ID**: BL-043
> **対象リポジトリ**: dev-process-improvement


## 気づき

backlog-maintenance セッションタイプの追加により、triage-standard-policy の適用マトリクスが5セッションタイプ×15列に拡大し、マークダウンテーブルの可読性が低下している。

今後さらにセッションタイプが追加される場合、テーブル形式の再設計（縦横の転置、セッションタイプ別の分割テーブル等）を検討する余地がある。

## 発見元

- 施策: `sessions/initiatives/backlog-maintenance-session/`
- 08_gate_review.md 必須把握事項 #2
