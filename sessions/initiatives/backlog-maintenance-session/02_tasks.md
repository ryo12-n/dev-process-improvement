# タスクリスト: backlogメンテナンスセッション作成

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 実施ワーカー（l2-worker）向けタスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `.claude/skills/backlog-maintenance-manager/SKILL.md` を作成する。triage-manager の構造をベースに、BM タスク定義（BM-001〜BM-005）、ワーカーディスパッチ手順、成果物確認観点を記載する。manager-common-policy を参照し、固有ロジックのみ記載すること | session-flow-policy §2 の必須要素（あなたの役割・作業フロー・やること・やらないこと・担当ファイル）が含まれている。BM タスク定義テーブルが記載されている | 🔴 | ⬜ |
| T-002 | `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md` を作成する。triage-worker をベースに、BM タスクの走査手順・スキャンレポート形式を定義する | session-flow-policy §3.1 の必須要素（あなたの役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）が含まれている。壁打ちフェーズが定義されている | 🔴 | ⬜ |
| T-003 | `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md` を作成する。triage-evaluator をベースに、BM 走査結果の評価基準を定義する。対称性確認テーブルを含めること | session-flow-policy §3.2 のペアリング対称性要件を満たしている。対称性確認テーブルが含まれている | 🔴 | ⬜ |
| T-004 | `sessions/backlog-maintenance/_template/` を作成する。triage の _template 構造に倣い、マネージャー直下ファイル（00_pre_investigation.md〜04_gate_review.md）と workers/_template/（01_tasks.md〜07_issues.md）を用意する | テンプレートファイル一式が存在し、triage テンプレートと同等の構造を持つ | 🔴 | ⬜ |
| T-005 | `docs/workflow.md` に backlog-maintenance セッションタイプのフローを追記する | workflow.md に backlog-maintenance の作業フロー図・説明が追記されている | 🔴 | ⬜ |
| T-006 | `.claude/rules/commit-message.md` に新セッション種別（`bm-mgr`, `bm-worker`, `bm-eval`）を追加する | 非施策作業テーブルに bm-mgr, bm-worker, bm-eval の3行が追加されている | 🔴 | ⬜ |
| T-007 | `.claude/skills/session-flow-policy/SKILL.md` §5 の既存セッションタイプ一覧テーブルに backlog-maintenance を追加する | テーブルに backlog-maintenance の行が追加されている | 🟡 | ⬜ |
| T-008 | `.claude/skills/manager-common-policy/SKILL.md` §1 の適用対象テーブルに backlog-maintenance-manager を追加する | テーブルに backlog-maintenance-manager の行が追加されている | 🟡 | ⬜ |
| T-009 | `.claude/skills/triage-standard-policy/SKILL.md` の適用マトリクスに backlog-maintenance セッションの行を追加する（必要な場合）。追加不要と判断した場合はその理由を work_log に記録する | 適用マトリクスに追加されている、または追加不要の判断理由が記録されている | 🟡 | ⬜ |
| T-010 | ルール変更連動更新チェックリスト（rule-change-checklist スキル）を実施する。変更した各ファイルの「関連ファイル一覧」セクションを確認し、連動更新漏れがないことを検証する | チェックリストの全項目が確認済み。確認結果を 03_work_log.md に記録 | 🔴 | ⬜ |
| T-011 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-012 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

## 評価ワーカー（l2-evaluator）向けタスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| E-001 | 実施ワーカーの成果物を session-flow-policy §5.1 チェックリストに照らして評価する | 評価レポートに全チェック項目の判定結果が記載されている | 🔴 | ⬜ |
| E-002 | ペアリング対称性要件（§3.2）の充足を検証する | worker.md と evaluator.md の対称性が確認されている | 🔴 | ⬜ |
| E-003 | 既存セッションタイプ（triage, metacognition）との構造一貫性を評価する | 命名規則・ファイル構成・セクション構成の一貫性が確認されている | 🔴 | ⬜ |
| E-004 | 連動更新の網羅性を検証する（docs/workflow.md, commit-message.md, session-flow-policy, manager-common-policy, triage-standard-policy） | 各連動更新ファイルの変更内容が適切であることが確認されている | 🔴 | ⬜ |
| E-005 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| E-006 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-10
