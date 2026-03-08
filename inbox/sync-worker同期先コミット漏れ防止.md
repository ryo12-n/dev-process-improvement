# sync-worker が同期先リポジトリでのコミット・PR作成を行わない問題

## 気づき

sync/20260308 セッションで、sync-worker が ai-driven-dev-patterns にファイルを書き込んだが、同期先でのコミット・プッシュ・PR作成が行われなかった。ユーザーの指摘で発覚し、マネージャーが手動で対応した。

## 原因

sync-worker.md の作業フローに「同期先リポジトリでのコミット・プッシュ」ステップが定義されていない。worker は dev-process-improvement 側の成果物（03_work_log.md, 04_sync_report.md）のコミットのみ行い、同期先の変更は未コミットのまま残った。

## 対応案

1. `sync-worker.md` の作業フローに同期先でのコミット・プッシュステップを追加
2. `sync-manager/SKILL.md` のワーカー成果物確認観点に同期先のコミット確認を追加
3. 必要に応じて `docs/workflow.md` の同期フロー記述を更新

修正スコープは小さい（2〜3ファイル、各数行）。maintenance コミットで対応可能な規模。

## 発見元

- セッション: sync/20260308
- 発見者: ユーザー（PRレビュー時）
