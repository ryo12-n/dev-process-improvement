# タスク指示: Phase 3（最適化提案）

## Phase 情報

| 項目 | 内容 |
|------|------|
| Phase | 3（最適化提案） |
| ワーカー | config-proposal-worker |
| CO ターゲット | CO-001〜CO-007 |

## タスク一覧

| # | タスク | 完了条件 |
|---|--------|---------|
| 1 | CO-001: PreToolUse hook による deny ルール代替ガード + sandbox 有効化提案 | 具体的な実装例付き |
| 2 | CO-002: path-scoped rules の導入提案 + commit-message.md 分離提案 | 対象ファイル・paths 設定の具体例 |
| 3 | CO-003: GHA スキル5件への disable-model-invocation 設定提案 | 対象スキル・変更内容の具体例 |
| 4 | CO-004: PostToolUse/Stop 等の活用提案 | ユースケースと実装例 |
| 5 | CO-005: CLAUDE.md の import(@) 活用 + rules/ 委譲による 112行以下への縮小提案 | 分離対象・分離先・期待行数の具体計画 |
| 6 | CO-006: 高優先度プラグイン4件の導入計画 | 導入順序・期待効果 |
| 7 | CO-007: sandbox 有効化 + settings.local.json 導入提案 | 設定内容の具体例 |
| 8 | 全提案の優先順位付け（Impact × Effort マトリクス） | Quick Wins の特定 |

## 参照ファイル

- `workers/set-2/04_scan_report.md`（Phase 2 分析結果）
- `workers/set-2/07_issues.md`（Phase 2 課題）
- `workers/set-1/04_scan_report.md`（Phase 1 収集結果）
- `.claude/skills/config-optimizer-manager/reference/claude-code-config-reference.md`（リファレンス）
- `25_analysis_gate.md`（Phase 2 ゲート判定・引き継ぎ事項）

## Phase 2 からの引き継ぎ（主要ギャップ）

**高重要度:**
1. deny ルール14件非機能 + PreToolUse hook/sandbox 未実装 → セキュリティガード不在
2. CLAUDE.md 192行（推奨50-100行）、import(@) 未使用
3. sandbox 未有効化

**中重要度:**
4. GHA スキル5件に disable-model-invocation 未設定
5. path-scoped rules 未使用（292行が全て起動時読み込み）
6. commit-message.md 肥大化（139行）
7. 評価済み高優先度プラグイン4件未導入
8. PostToolUse hook 未使用

**評価者補足:**
- permissions.ask 未使用
- permissions.defaultMode 未言及

## 完了の定義

- 全ギャップに対して具体的な提案（実装例付き）が作成されている
- 各提案が Impact × Effort で優先順位付けされている
- Quick Wins（高Impact/低Effort）が明確に特定されている
- 各提案がバックログエントリとして転記可能な具体性を持っている
