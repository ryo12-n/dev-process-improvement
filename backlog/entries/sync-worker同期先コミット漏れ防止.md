# sync-worker 同期先コミット漏れ防止

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-020 |
| **優先度** | 🔴 高 |
| **ステータス** | initiative 開始済 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | sync-worker-target-commit |
| **起票日** | 2026-03-08 |

## 課題・背景

sync/20260308 セッションで、sync-worker が ai-driven-dev-patterns にファイルを書き込んだが、同期先でのコミット・プッシュ・PR作成が行われなかった。sync-worker.md の作業フローに「同期先リポジトリでのコミット・プッシュ」ステップが定義されていないことが原因。

## 期待効果

- sync-worker.md の作業フローに同期先でのコミット・プッシュステップを追加
- sync-manager/SKILL.md のワーカー成果物確認観点に同期先のコミット確認を追加
- docs/workflow.md の同期フロー記述を更新

## 補足・参考情報

- 修正スコープ: 小（2-3ファイル、各数行）
- 発見元: sync/20260308 セッション（ユーザーがPRレビュー時に発見）
- 関連 inbox エントリ: `inbox/sync-worker同期先コミット漏れ防止.md`（backlog化に伴い削除対象）
