# PreToolUse hookコミットメッセージバリデーション

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-029 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-10 |

## 課題・背景

コミットメッセージ規約（`[session-type] category: summary` 形式）の遵守は毎コミット時に手動確認されており、優先度スコア6.0。PreToolUse hook で Bash コマンド中の `git commit` を検知し、正規表現バリデーションで形式チェックを強制化できる。

## 期待効果

- コミットメッセージの規約違反を自動検知・ブロックし、規約遵守を guaranteed execution にする
- 手動確認の負荷を削減

## 補足・参考情報

- 実装方針・設定例JSON: `sessions/initiatives/ai-automation-tool-review/04_work_report.md` の「順位2」セクション参照
- HEREDOC 形式のコミットメッセージへの対応が必要
- 元施策: `sessions/initiatives/ai-automation-tool-review/`
