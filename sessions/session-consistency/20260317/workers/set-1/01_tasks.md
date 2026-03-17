# タスク指示: Phase 1（情報収集）

## Phase 情報

| 項目 | 内容 |
|------|------|
| Phase | 1（情報収集） |
| ワーカー | sc-collection-worker |
| SC ターゲット | SC-001〜SC-008（全ターゲット） |

## タスク一覧

| # | タスク | 完了条件 |
|---|--------|---------|
| 1 | SC-001: 9マネージャー SKILL.md の必須セクション有無を収集 | 全9件の必須セクション（あなたの役割・作業フロー・やること・やらないこと）＋オーケストレーション記載の有無がリファレンスに記録 |
| 2 | SC-002: 27エージェント定義の必須セクション有無を収集 | 全27件の必須セクション（あなたの役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）の有無がリファレンスに記録 |
| 3 | SC-003: Worker/Evaluator ペアの対称性要件の有無を収集 | 全ペアの対称性要件（壁打ち・計画・レポート・知見記録・課題起票・停止ルール）がリファレンスに記録 |
| 4 | SC-004: テンプレートファイル一覧 vs エージェント担当ファイルを収集 | テンプレートとエージェント担当ファイルの突合結果がリファレンスに記録 |
| 5 | SC-005: 各マネージャーの manager-common-policy 参照パターンを収集 | §2〜§8 の参照箇所がリファレンスに記録 |
| 6 | SC-006: session-lifecycle-policy 適用マトリクスのセッションタイプを収集 | マトリクス記載と実際のセッション定義の突合結果がリファレンスに記録 |
| 7 | SC-007: commit-message.md のセッション種別一覧を収集 | 全セッションタイプの登録状況がリファレンスに記録 |
| 8 | SC-008: 各定義の「関連ファイル一覧」の参照先を収集 | 参照先ファイルの実在・逆方向参照がリファレンスに記録 |

## 参照ファイル

- `.claude/skills/*/SKILL.md`（9マネージャー + ポリシー）
- `.claude/skills/*/agents/*.md`（27エージェント定義）
- `sessions/*/_template/`（9テンプレートディレクトリ）
- `.claude/skills/session-flow-policy/SKILL.md`
- `.claude/skills/session-lifecycle-policy/SKILL.md`
- `.claude/skills/manager-common-policy/SKILL.md`
- `.claude/rules/commit-message.md`
- `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md`

## 完了の定義

- 全8ターゲットの情報がリファレンスに記録されている
- リファレンスの Snapshot Date が 2026-03-17 に更新されている
- `04_scan_report.md` に構造化された収集結果が記載されている
- 発見した課題が `07_issues.md` に起票されている
