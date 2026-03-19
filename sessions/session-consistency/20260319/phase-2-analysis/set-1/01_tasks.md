# タスク指示: Phase 2（現状分析）

## Phase 情報

| 項目 | 内容 |
|------|------|
| Phase | 2（現状分析） |
| ワーカー | sc-analysis-worker |
| SC ターゲット | SC-001〜SC-008（全8ターゲット。重点: SC-008, SC-006, SC-003） |

## タスク一覧

| # | タスク | 完了条件 |
|---|--------|---------|
| 1 | SC-001〜SC-007: Phase 1 収集データの分析 | 各ターゲットの準拠状況を分析し、不整合があればエビデンス付きで記録 |
| 2 | SC-008 重点分析: 壊れた参照3箇所の影響分析 | l2-plan-worker.md/l2-plan-evaluator.md の triage-standard-policy 参照について、影響範囲・修正の具体的内容を分析 |
| 3 | SC-003 重点分析: l2-evaluator の対称性テーブル欠如の分析 | l2-worker ↔ l2-evaluator ペアで E:なし、triage/metacognition ペアでも E:なし。これが意図的か否か分析 |
| 4 | 前回 SC セッション（20260317）の知見フォローアップ | 前回指摘された課題が対応されているか確認 |

## 参照ファイル

- `sessions/session-consistency/20260319/phase-1-collection/set-1/04_scan_report.md` — Phase 1 収集結果
- `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` — 最新リファレンス
- `.claude/skills/l1-manager/agents/l2-plan-worker.md` — 壊れた参照の実ファイル
- `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` — 壊れた参照の実ファイル
- `.claude/skills/l1-manager/agents/l2-evaluator.md` — 対称性テーブル欠如の確認
- `.claude/skills/session-flow-policy/SKILL.md` — §3.2 対称性要件の確認
- `sessions/session-consistency/20260317/` — 前回 SC セッションの成果物

## 完了の定義

- 全8ターゲットについて現状分析が完了し、04_scan_report.md にエビデンス付きの分析結果が記載されている
- 不整合が具体的なデータ（ファイル名、セクション名、行番号）に基づいている
- 前回指摘の課題のフォローアップ状況が記録されている
