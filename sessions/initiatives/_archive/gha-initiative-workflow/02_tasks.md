# タスクリスト: GHA Initiative ワークフロー

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `.github/workflows/initiative-wallbash.yml` を作成する。トリガー: `issues:labeled` (initiative-start) + `workflow_dispatch`。Claude Code Action で壁打ちサマリーを生成し Issue コメントに投稿。施策ブランチ作成・コミット・プッシュ後に PR を作成する。ラベル操作 (`initiative-start` → `initiative` + `initiative:wallbashing`) を Shell step で実行。既存の `backlog-auto-execute.yml` のパターン（Action設定、パーミッション）を参考にすること | ワークフローファイルが存在し、トリガー・ジョブ条件・ステップ・パーミッションが計画通りに定義されている | 🔴 | ✅ |
| T-002 | `.github/workflows/initiative-execute.yml` を作成する。トリガー: `issue_comment:created`。ジョブ条件: `initiative:wallbashing` ラベル + `/approve` コメント、または `initiative:gate-review` ラベル + `/reject` コメント。Issue 番号から PR ブランチを取得してチェックアウトし、Claude Code Action で計画・実行・評価・ゲート判定を行い、ゲート判定サマリーを Issue コメントに投稿する。`claude_args` は `--max-turns 80` を設定。ラベル操作を Shell step で実行 | ワークフローファイルが存在し、`/approve` と `/reject` の両方のトリガー条件が正しく定義されている | 🔴 | ✅ |
| T-003 | `.github/workflows/initiative-close.yml` を作成する。トリガー: `issue_comment:created`。ジョブ条件: `initiative:gate-review` ラベル + `/approve` コメント。PR ブランチをチェックアウトし、Claude Code Action でアーカイブ移動・知見ルーティングを行い、Issue をクローズしラベルを `initiative:completed` に変更する | ワークフローファイルが存在し、アーカイブ・クローズのステップが定義されている | 🔴 | ✅ |
| T-004 | `.claude/skills/gha-guideline/SKILL.md` の §5 ワークフロー権限マトリクスに、新規3ワークフロー（initiative-wallbash, initiative-execute, initiative-close）の権限設計と設計根拠を追記する | §5 に3ワークフローのエントリが追加されている | 🟡 | ✅ |
| T-005 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-006 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

---
**作成者**: L1
**最終更新**: 2026-03-14
