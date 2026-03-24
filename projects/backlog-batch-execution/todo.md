# TODO管理: backlog-batch-execution

## ステータス定義

| ステータス | 意味 |
|-----------|------|
| `未着手` | 未開始 |
| `進行中` | 施策として着手済み |
| `完了` | ゲート判定通過・アーカイブ済み |
| `ブロック` | 外部要因で停止中 |

## TODO一覧

| # | タスク | 施策名 | 優先度 | ステータス | 備考 |
|---|--------|--------|--------|-----------|------|
| 1 | 壊れた参照修正・リネーム追従 | batch-reference-fix-and-rename | 高 | 完了 | アーカイブ済み |
| 2 | GHAスキル設定・マッピング | batch-gha-minor-fixes | 高 | 未着手 | 4件、dev-process-improvement内で完結 |
| 3 | docs/workflow.md・テンプレート修正 | batch-template-doc-fixes | 中 | 未着手 | 6件 |
| 4 | ルール・ポリシー軽微追記 | batch-rule-policy-minor-additions | 中 | 未着手 | 7件 |
| 5 | aidd関連軽微修正 | batch-aidd-minor-fixes | 中 | 未着手 | 6件、CLI --add-dir 環境必要 |
| 6 | スキル・セッション微調整 | batch-skill-session-tweaks | 低 | 未着手 | 8件 |
| 7 | 非施策セッションGHA自動化 | (M統合) BL-055+BL-057 | 中 | 未着手 | M分類統合候補 |
| 8 | workflow.md網羅性改善 | (M統合) BL-054+BL-065 | 中 | 未着手 | M分類統合候補 |
| 9 | PostToolUse hook品質チェック統合 | (M統合) BL-030+BL-082 | 中 | 未着手 | M分類統合候補 |

---
**最終更新**: 2026-03-24
