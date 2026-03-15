# タスク指示: Phase 1（情報収集）

## Phase 情報

| 項目 | 内容 |
|------|------|
| Phase | 1（情報収集） |
| ワーカー | config-collection-worker |
| CO ターゲット | CO-001〜CO-007 |

## タスク一覧

| # | タスク | 完了条件 |
|---|--------|---------|
| 1 | CO-001: settings.json のスキーマ・サポートフィールドを公式ドキュメントから収集 | リファレンスの §1 が具体的な値で埋まっている |
| 2 | CO-002: rules/ のフォーマット・path-scoped rules・ベストプラクティスを収集 | リファレンスの §2 が埋まっている |
| 3 | CO-003: skills/ の SKILL.md フォーマット・description最適化・コンテキスト予算を収集 | リファレンスの §3 が埋まっている |
| 4 | CO-004: hooks の全タイプ仕様（SessionStart/PreToolUse/PostToolUse/Stop）を収集 | リファレンスの §4 が埋まっている |
| 5 | CO-005: CLAUDE.md の import(@) 構文・サイズガイドライン・読み込み順を収集 | リファレンスの §5 が埋まっている |
| 6 | CO-006: プラグインシステムの仕様・利用可能プラグインを収集 | リファレンスの §6 が埋まっている |
| 7 | CO-007: settings.local.json, memory, sandbox, 環境変数を収集 | リファレンスの §7 が埋まっている |

## 参照ファイル

- `.claude/skills/config-optimizer-manager/reference/claude-code-config-reference.md`（リファレンススナップショット、更新対象）
- `.claude/settings.json`（現在の設定）
- `.claude/rules/*.md`（現在のルールファイル）
- `.claude/skills/*/SKILL.md`（現在のスキル定義）
- `.claude/hooks/*`（現在のフック）
- `CLAUDE.md`（現在のプロジェクト設定）

## 完了の定義

- リファレンスの全7セクション（§1〜§7）が公式ドキュメントからの具体的な情報で更新されている
- Snapshot Date が 2026-03-15 に更新されている
- Changelog に初回収集の記録がある
- `04_scan_report.md` に7ターゲット全てのカバレッジ結果が記載されている
