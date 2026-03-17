# タスク指示: Phase 2（現状分析）

## Phase 情報

| 項目 | 内容 |
|------|------|
| Phase | 2（現状分析） |
| ワーカー | sc-analysis-worker |
| SC ターゲット | SC-001〜SC-008（全ターゲット） |

## タスク一覧

| # | タスク | 完了条件 |
|---|--------|---------|
| 1 | SC-001: マネージャー SKILL.md の必須セクション準拠を分析 | Gaps & Inconsistencies テーブルに不整合（もしくは「なし」）が記載 |
| 2 | SC-002: エージェント定義の必須セクション準拠を分析 | 同上 |
| 3 | SC-003: Worker ↔ Evaluator 対称性の不足要素を分析 | 対称性テーブル欠落3件（l2-evaluator, triage-evaluator, metacognition-evaluator）の影響分析を含む |
| 4 | SC-004: テンプレートとエージェント担当ファイルの整合を分析 | テンプレート↔担当ファイルの不整合を特定 |
| 5 | SC-005: manager-common-policy §2〜§8 参照パターンの網羅性を分析 | 参照漏れパターンの特定 |
| 6 | SC-006: session-lifecycle-policy マトリクスとロール定義の整合を分析 | マトリクスのセル値とロール定義の実態の乖離を特定 |
| 7 | SC-007: commit-message 規約の未登録セッションタイプを分析 | l2-plan-worker/evaluator の扱いの明確化 |
| 8 | SC-008: 関連ファイル一覧の壊れた参照と逆方向参照欠落を分析 | 壊れた参照2件の影響分析、逆方向参照パターンの分析 |

## 参照ファイル

- `workers/set-1/04_scan_report.md`（Phase 1 収集結果）
- `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md`（リファレンス）
- `.claude/skills/*/SKILL.md`（分析対象）
- `.claude/skills/*/agents/*.md`（分析対象）
- `.claude/skills/session-flow-policy/SKILL.md`（準拠基準）
- `.claude/skills/session-lifecycle-policy/SKILL.md`（準拠基準）
- `.claude/skills/manager-common-policy/SKILL.md`（準拠基準）
- `.claude/rules/commit-message.md`（準拠基準）
- `sessions/*/_template/`（分析対象）

## 完了の定義

- 全8ターゲットの分析が完了し、各ターゲットに Current State / Requirements / Gaps / Recommendations が記載されている
- 不整合にはエビデンス（ファイル名、セクション名等）が付与されている
- `04_scan_report.md` に構造化された分析結果が記載されている
- 発見した課題が `07_issues.md` に起票されている
