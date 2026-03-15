# タスクリスト: initiative-dispatcher

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 実施タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `initiative-dispatcher.yml` を新規作成する。`issue_comment` トリガーで `@ai-task` を含むコメントを検知し、`/start`, `/approve`, `/reject`, `/question` のコマンドを解析する。ラベルを確認してルーティングテーブルに従い `gh workflow run` で適切なワークフローを起動する。フェーズ不一致時はエラーコメントを Issue に投稿する。コマンド検出時は eyes リアクションを付与する。パーミッションは `contents: read`, `issues: write`, `actions: write`。 | ディスパッチャーワークフローが作成され、ルーティングテーブル（`00_proposal.md` 記載の5パターン）が実装されている。エラーハンドリング（不明コマンド・フェーズ不一致・既存initiative）が実装されている | 🔴 | ✅ |
| T-002 | `initiative-question.yml` を新規作成する。`workflow_dispatch` トリガーで `issue_number` と `question` を inputs として受け取る。PR ブランチをチェックアウトし、Claude に施策ファイルを読み取り専用で渡して質問に回答させる。回答を Issue コメントとして投稿する。model: `claude-sonnet-4-6`, max-turns: 10。パーミッションは `contents: read`, `issues: write`, `id-token: write`。 | question ワークフローが作成され、inputs の定義・Claude プロンプト・Issue コメント投稿が実装されている | 🔴 | ✅ |
| T-003 | `initiative-wallbash.yml` のトリガーを変更する。`issues: [labeled]` トリガーを削除し、`workflow_dispatch` のみにする。`if:` の `initiative-start` ラベル条件を削除する。issue番号の分岐ロジック（event vs input）を削除し、常に `inputs.issue_number` を使用する。ラベル操作から `initiative-start` の削除処理を除去する（`initiative` + `initiative:wallbashing` の追加は維持）。 | wallbash が `workflow_dispatch` のみで発火する。`issues: [labeled]` トリガーと `initiative-start` 関連ロジックが除去されている | 🔴 | ✅ |
| T-004 | `initiative-execute.yml` のトリガーを変更する。`issue_comment` トリガーを `workflow_dispatch` に変更する。inputs: `issue_number` (number, required), `command` (string, required: approve/reject), `feedback` (string, optional), `phase` (string, required: wallbashing/gate-review)。`github.event.issue.number` を `inputs.issue_number` に、コメントパース処理を `inputs.command`, `inputs.feedback`, `inputs.phase` の直接参照に置換する。ラベル管理はそのまま維持する。 | execute が `workflow_dispatch` のみで発火する。`issue_comment` トリガーと `github.event.comment.body` パース処理が除去されている。inputs からコンテキストを取得している | 🔴 | ✅ |
| T-005 | `initiative-close.yml` のトリガーを変更する。`issue_comment` トリガーを `workflow_dispatch` に変更する。inputs: `issue_number` (number, required)。`github.event.issue.number` を `inputs.issue_number` に置換する。ラベル管理はそのまま維持する。 | close が `workflow_dispatch` のみで発火する。`issue_comment` トリガーと `github.event.issue.*` 参照が除去されている | 🔴 | ✅ |
| T-006 | `backlog-to-issue.yml` を変更する。Issue 作成時の `initiative-start` ラベル付与を削除する。Issue 作成後に issue 番号をキャプチャし、`gh workflow run initiative-wallbash.yml -f issue_number=<N>` で wallbash を直接 dispatch する。`actions: write` パーミッションを追加する。 | `initiative-start` ラベル付与が除去されている。Issue 作成後に wallbash が dispatch される。`actions: write` パーミッションが追加されている | 🔴 | ✅ |
| T-007 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-008 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

## 注意事項

- T-001〜T-006 は全変更を1コミットでアトミックに適用すること（移行中の二重発火を防ぐため）
- 既存ワークフローの Claude プロンプト内容は変更しない（トリガー・入力部分のみ変更）
- 適用対象環境: SDK（GitHub Actions 上で実行）

---
**作成者**: L1
**最終更新**: 2026-03-15
