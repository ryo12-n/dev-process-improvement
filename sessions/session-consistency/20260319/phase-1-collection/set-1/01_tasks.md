# タスク指示: Phase 1（情報収集）

## Phase 情報

| 項目 | 内容 |
|------|------|
| Phase | 1（情報収集） |
| ワーカー | sc-collection-worker |
| SC ターゲット | SC-001〜SC-008（全8ターゲット） |

## タスク一覧

| # | タスク | 完了条件 |
|---|--------|---------|
| 1 | SC-001: 全マネージャー SKILL.md の必須セクション有無を収集 | 9件のマネージャー SKILL.md について4必須セクション＋オーケストレーション関連記載の有無を記録 |
| 2 | SC-002: 全エージェント定義の必須セクション有無を収集 | 28件のエージェント定義について6必須セクションの有無を記録 |
| 3 | SC-003: Worker ↔ Evaluator ペアの対称性要件を収集 | 全ペアについて壁打ち・計画・レポート・知見記録・課題起票・停止ルールの有無を記録 |
| 4 | SC-004: テンプレートファイル一覧とエージェント担当ファイルの突合 | テンプレートファイルとエージェント担当ファイルテーブルの突合結果を記録 |
| 5 | SC-005: manager-common-policy §2〜§8 の参照パターンを収集 | 9件のマネージャーについて各§の参照有無を記録 |
| 6 | SC-006: session-lifecycle-policy 適用マトリクスの現状を収集 | マトリクスの全セル値と実在セッション定義の突合結果を記録 |
| 7 | SC-007: commit-message.md セッション種別と実在セッションの突合 | 全セッション種別の登録状況を記録 |
| 8 | SC-008: 関連ファイル一覧の参照先実在・逆方向参照を収集 | 関連ファイル一覧を持つ全スキルについて参照先実在・逆参照の状況を記録 |
| 9 | リファレンス更新 | reference/session-consistency-reference.md を最新状態に更新 |

## 参照ファイル

- `.claude/skills/*/SKILL.md` — 全マネージャー・ポリシースキル
- `.claude/skills/*/agents/*.md` — 全エージェント定義
- `sessions/*/_template/` — 全テンプレートディレクトリ
- `.claude/skills/manager-common-policy/SKILL.md` — §1 適用対象テーブル
- `.claude/skills/session-lifecycle-policy/SKILL.md` — §1.2 適用マトリクス
- `.claude/skills/session-flow-policy/SKILL.md` — §2, §3 必須セクション定義
- `.claude/rules/commit-message.md` — セッション種別テーブル
- `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` — 既存リファレンス

## 完了の定義

- 全8ターゲットについて情報収集が完了し、04_scan_report.md に構造化された結果が記載されている
- リファレンスが最新状態に更新されている（Changelog に変更点を追記済み）
- 作業中に発見した課題が 07_issues.md に起票されている
