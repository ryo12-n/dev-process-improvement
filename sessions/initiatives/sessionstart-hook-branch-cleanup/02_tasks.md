# タスクリスト: SessionStart hook ブランチ整理自動化

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `.claude/hooks/session-start-branch-cleanup.sh` を新規作成する。ロジック: (1) `git branch --show-current` で現在ブランチ取得 (2) main なら `git pull` のみ (3) main 以外なら未プッシュコミット確認→push→PR確認/作成→main切替 (4) 結果を JSON で stdout に出力。エラーハンドリング: 全パスで exit 0 を保証、gh 不在時は PR ステップをスキップし warnings に記録。chmod +x を忘れないこと。適用対象環境: CLI / SDK 共通 | スクリプトが `bash -n` で構文エラーなし。main 時・別ブランチ時・gh 不在時の3パターンのロジックが実装されている | 🔴 | ✅ |
| T-002 | `.claude/settings.json` に `hooks.SessionStart` セクションを追加する。matcher は `startup\|resume`、command は `.claude/hooks/session-start-branch-cleanup.sh`。既存の `permissions` セクションはそのまま保持する。適用対象環境: CLI / SDK 共通 | settings.json が有効な JSON であること。hooks セクションが追加されていること | 🔴 | ✅ |
| T-003 | 以下6つのマネージャースキルの「セッション開始時のブランチ整理」セクションを更新する: (1) `.claude/skills/l1-manager/SKILL.md` (2) `.claude/skills/triage-manager/SKILL.md` (3) `.claude/skills/metacognition-manager/SKILL.md` (4) `.claude/skills/sync-manager/SKILL.md` (5) `.claude/skills/l1-impl-manager/SKILL.md` (6) `.claude/skills/backlog-maintenance-manager/SKILL.md`。変更内容: 手動実行の記述を「SessionStart hook（`.claude/hooks/session-start-branch-cleanup.sh`）により自動実行される。hook の出力を確認し、エラーや警告があればユーザーに報告すること。」に置き換える。6ファイルすべて同一の記述にすること | 6ファイルすべてが同一の hook 自動実行記述に更新されていること | 🔴 | ✅ |
| T-004 | `.claude/rules/session-start-branch-cleanup.md` の冒頭に以下のバナーを追加する: `> **実行ロジック移行済み**: ブランチ整理の実行ロジックは `.claude/hooks/session-start-branch-cleanup.sh` に移行済み。本文書は設計仕様リファレンスとして維持する。` 既存の6ステップの手順はそのまま残す（設計仕様として機能するため） | バナーが追加されていること。既存の手順が維持されていること | 🟡 | ✅ |
| T-005 | `docs/workflow.md` の session-start-branch-cleanup に関する記述を更新し、hook による自動化を反映する。「SessionStart hook により自動実行される」旨を記載する | docs/workflow.md が更新されていること | 🟡 | ✅ |
| T-006 | `backlog/entries/SessionStart-hookブランチ整理自動化.md` を `git rm` で削除する。`backlog/backlog.csv` の該当行（30行目）を削除する | backlog エントリと CSV 行が削除されていること | 🟡 | ✅ |
| T-007 | ルール変更連動更新チェックリスト（`rule-change-checklist` スキル）を実施する | チェックリストの全項目が確認済み。確認結果を `03_work_log.md` に記録 | 🔴 | ✅ |

---
**作成者**: L1
**最終更新**: 2026-03-13
