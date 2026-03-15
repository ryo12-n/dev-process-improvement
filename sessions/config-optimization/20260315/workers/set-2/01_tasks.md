# タスク指示: Phase 2（現状分析）

## Phase 情報

| 項目 | 内容 |
|------|------|
| Phase | 2（現状分析） |
| ワーカー | config-analysis-worker |
| CO ターゲット | CO-001〜CO-007 |

## タスク一覧

| # | タスク | 完了条件 |
|---|--------|---------|
| 1 | CO-001: settings.json の現状をリファレンスと比較。未設定フィールド・deny非機能性の実効性検証 | ギャップがエビデンス付きで記載 |
| 2 | CO-002: rules/ の構成・path-scoped活用状況・重複/肥大化を分析 | 現状とベストプラクティスのギャップが特定 |
| 3 | CO-003: skills/ のdescription品質（単一行推奨）・コンテキスト予算・トリガー精度を分析 | 24スキル全てのdescription確認、予算推定 |
| 4 | CO-004: hooks の使用状況。24イベント中の活用余地を分析 | 使用中/未使用のイベントが特定 |
| 5 | CO-005: CLAUDE.md のサイズ(192行)・構造・import(@)活用余地・rules/委譲候補を分析 | 公式推奨(50-100行)との具体的差分 |
| 6 | CO-006: プラグイン導入状況。plugin-reference評価との整合を確認 | 現状の導入状況が把握されている |
| 7 | CO-007: settings.local.json, memory, sandbox, 環境変数の現状確認 | 未活用機能がリストアップ |

## 参照ファイル

- `.claude/skills/config-optimizer-manager/reference/claude-code-config-reference.md`（リファレンス）
- `workers/set-1/04_scan_report.md`（Phase 1 収集レポート）
- `workers/set-1/07_issues.md`（Phase 1 課題）
- `.claude/settings.json`（分析対象）
- `.claude/rules/*.md`（分析対象）
- `.claude/skills/*/SKILL.md`（分析対象）
- `.claude/hooks/*`（分析対象）
- `CLAUDE.md`（分析対象）

## Phase 1 からの引き継ぎ事項

1. deny ルール非機能性（ISS-TEMP-001）: 14件の deny ルールの実効性を検証すること
2. hooks 24イベント拡張（ISS-TEMP-002）: 活用余地を具体的に分析すること
3. CLAUDE.md: 192行、import(@) 未使用。公式推奨は50-100行
4. skills description: 単一行推奨。YAML マルチライン非対応
5. settings.json: 30+ フィールド中3フィールドのみ使用

## 完了の定義

- 7ターゲット全ての分析が完了し、ギャップがエビデンス付きで記載されている
- 未活用機能がリストアップされている
- Phase 1 の知見が分析に反映されている
