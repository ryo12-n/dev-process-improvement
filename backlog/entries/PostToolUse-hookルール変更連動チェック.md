# PostToolUse hookルール変更連動チェック

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-030 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-10 |

## 課題・背景

`.claude/skills/` や `.claude/rules/` のファイル変更時に連動更新が必要なファイルのチェックが手動で行われており、漏れが発生するリスクがある。優先度スコア3.0。PostToolUse hook で Edit/Write を検知し、対象パス変更時に関連ファイル一覧と `docs/workflow.md` 更新のリマインダーを自動通知できる。

## 期待効果

- ルール変更時の連動更新漏れを防止
- `docs/workflow.md` の更新忘れを削減

## 補足・参考情報

- 実装方針・設定例JSON: `sessions/initiatives/ai-automation-tool-review/04_work_report.md` の「順位3」セクション参照
- 元施策: `sessions/initiatives/ai-automation-tool-review/`

## 関連エントリ

- BL-082: PostToolUse hook 自動検証
- **統合候補（2026-03-17 BM-005 検出）**: BL-030 + BL-082 を「PostToolUse hook 品質チェック統合」として統合推奨（同一実装基盤: ルール変更連動 + 行数/フロントマター検証を1つの hook で実装）
