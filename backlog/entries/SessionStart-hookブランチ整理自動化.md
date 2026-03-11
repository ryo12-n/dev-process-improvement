# SessionStart hookブランチ整理自動化

## メタ情報

| 項目 | 内容 |
|------|------|
| **優先度** | 🔴 高 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-10 |

## 課題・背景

セッション開始時のブランチ整理（7ステップ）は全マネージャーセッションで毎回手動実行されており、優先度スコア9.0（費用対効果評価で最高）。SessionStart hook + シェルスクリプトで完全自動化が可能。外部リポジトリ整理（R-014）も統合して実装する。

## 期待効果

- セッション開始時の手動7ステップを自動化し、毎セッション数分の作業を削減
- 手順の実行漏れ・ミスを根絶
- `.claude/rules/session-start-branch-cleanup.md` の手順定義をスクリプトに移行し、二重管理を解消

## 補足・参考情報

- 実装方針・設定例JSON: `sessions/initiatives/ai-automation-tool-review/04_work_report.md` の「順位1」セクション参照
- 元施策: `sessions/initiatives/ai-automation-tool-review/`
