# evaluator 対称性確認テーブル統一

## 起票情報

| 項目 | 内容 |
|------|------|
| 起票元 | session-consistency チェック 2026-03-17（IMP-003, SC-003） |
| 起票日 | 2026-03-17 |

## 内容

l2-evaluator、triage-evaluator、metacognition-evaluator の3件に session-flow-policy §3.3 推奨の対称性確認テーブルが欠落している。後発の evaluator（sync, backlog-maintenance, automation, config-optimizer, sc, l2-plan, impl）にはテーブルが存在する。

対称性要件6項目自体は全ペアで充足しており、実質的なリスクはないが、テーブルの追加により早期不整合検出が可能になる。sync-evaluator の実装を参考テンプレートとして3件に追加する案。

## 判断ポイント

- 推奨プラクティスを必須に格上げするか
- 3件の追加は機械的作業（低 Effort）だが、施策管理のオーバーヘッドとの比較
