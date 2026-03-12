# session-flow-policy §5.1 チェックリストに manager-common-policy §1 追加を提案

## 背景

施策 `l1-impl-manager-session` の評価で、新マネージャースキル作成時に `manager-common-policy` §1 適用対象テーブルへの追加が漏れた（ISS-056）。

現在の `session-flow-policy` §5.1 チェックリストには以下が含まれているが:
- docs/workflow.md への追記
- commit-message.md への追加
- triage-standard-policy への追加

**manager-common-policy §1 テーブルへの追加** が明示されていない。

## 提案

`session-flow-policy` §5.1 のチェックリストに以下を追加:
```
- [ ] `manager-common-policy` §1 適用対象テーブルに新セッションタイプを追加した
```

## 関連
- 施策: `sessions/initiatives/l1-impl-manager-session/`
- 課題: ISS-056
- 評価レポート: `06_eval_report.md` E-07, 知見 #1

---
**起票日**: 2026-03-12
**起票元施策**: l1-impl-manager-session
