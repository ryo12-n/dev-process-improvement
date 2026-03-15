# ワーカータスク指示: Set-2

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-003 | CSV | ステータス「起票」24件の棚卸し。ISS-052〜055（メタ認知起票）、ISS-056〜058（直近施策起票）の対応方針検討。ステータス「方針確定」1件（ISS-031）の確認 | 各アイテムの状態が確認されている |
| TG-004 | initiative | 10件の状態確認。アーカイブ候補5件: automation-manager-session, claude-code-plugin-skills-survey, impl-worktree-parallel, phase-gate-standardization, sessionstart-hook-branch-cleanup。進行中2件: sync-worker-target-commit, triage-phase-gate-and-gha-sync。状態不明3件: backlog-id-and-issue-template, impl-worker-worklog-reliability, external-repo-cleanup-on-demand | 全施策の状態がスキャンレポートに記録されている |
| TG-007 | README | README.md の4セクション整合性チェック: (1)ディレクトリ構成図 (2)セッション種別テーブル (3)AI向けスキル定義テーブル (4)ドキュメントマップ。既知: l1-impl-manager, automation-manager, config-optimizer-manager 等9+スキルが未記載、3セッションタイプ未記載 | チェック結果がスキャンレポートに記録されている |

## 走査時の注意事項

- TG-003: CSV は `プロセス改善_課題管理.csv`（リポジトリルート）。長期起票（ISS-006 は 2026-02-23 起票、21日経過）の対応方針を検討すること
- TG-004: アーカイブ候補の5件について、l1-manager のクローズチェックリストに準じた確認を行うこと（ゲート通過判定、backlog.csv エントリ削除確認、知見ルーティング実行確認）
- TG-004: 状態不明3件は 08_gate_review.md の有無・内容を確認し、施策の現状を正確に記録すること
- TG-007: `.claude/skills/` 配下の全スキルディレクトリ（19件）と README の記載を突合すること。起動型スキル（user-invocable: true）とポリシー/チェックリスト型スキルを区別して報告すること

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-15
