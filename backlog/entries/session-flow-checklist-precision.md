# session-flow-policy §5.1 チェックリストの精度向上

> **バックログ ID**: BL-042


## 気づき

新セッションタイプ追加時（backlog-maintenance-session 施策）の実施・評価で、session-flow-policy §5.1 チェックリストに明記されていない連動更新箇所が発見された。

### チェックリストに含まれていない更新箇所

- `triage-standard-policy` の §1.3 記録先対応テーブル
- `triage-standard-policy` の §2.1 ペアリング構造テーブル
- `triage-standard-policy` の §3.1 走査対象リスト
- 各変更ファイルの「関連ファイル一覧」セクション

### 提案

§5.1 チェックリストに triage-standard-policy の更新箇所を明示する項目を追加し、次のセッションタイプ追加時の漏れを防ぐ。

## 発見元

- 施策: `sessions/initiatives/backlog-maintenance-session/`
- 08_gate_review.md 必須把握事項 #1
- worker/evaluator 双方から同じ知見が報告された
