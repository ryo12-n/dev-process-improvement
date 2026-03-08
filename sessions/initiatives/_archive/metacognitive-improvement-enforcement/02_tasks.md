# タスクリスト: メタ認知による改善の強制

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク

### L2-worker 向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `sessions/metacognition/_template/` ディレクトリを作成する。triage テンプレート（`sessions/triage/_template/`）をモデルに、マネージャー用テンプレート（`00_pre_investigation.md`, `01_plan.md`, `02_dispatch_log.md`, `03_report.md`, `04_gate_review.md`）とワーカー用テンプレート（`workers/_template/` 配下に `01_tasks.md`, `02_scan_plan.md`, `03_work_log.md`, `04_scan_report.md`, `05_eval_plan.md`, `06_eval_report.md`, `07_issues.md`）を作成する | 全テンプレートファイルが作成され、triage テンプレートとの構造的対称性が確認できる | 🔴 | ✅ |
| T-002 | `.claude/skills/metacognition-manager/SKILL.md` を作成する。triage-manager をベースに、MC タスク（MC-001〜MC-005）固有のワークフローを記載する。必須セクション: あなたの役割・ブランチ整理・作業フロー・やること・やらないこと・担当ファイル・関連ファイル一覧。triage との責務の違いを明記すること | session-flow-policy セクション5.1 の全チェック項目を満たす | 🔴 | ✅ |
| T-003 | `.claude/skills/metacognition-manager/agents/metacognition-worker.md` と `metacognition-evaluator.md` を作成する。triage-worker/evaluator をベースに、MC タスク固有のスキャン手順を記載する。ペアリング対称性要件（壁打ち・計画・レポート・知見記録・課題起票・停止ルール）を全て満たすこと | triage-standard-policy セクション2.3 のペアリング対称性チェックを全て満たす | 🔴 | ✅ |
| T-004 | `.claude/rules/commit-message.md` に `meta-mgr`, `meta-worker`, `meta-eval` セッション種別を追加する。category は `YYYYMMDD`（triage と同形式）。例示を含めること | 新セッション種別がテーブルに追加され、例示が含まれている | 🟡 | ✅ |
| T-005 | `docs/workflow.md` にメタ認知セッションフローのセクションを追加する。triage セッションフローと同等の詳細度で記載し、コミットメッセージ規約テーブルにも新 session-type を追加する | 新セッションフローが workflow.md に記載され、triage フローと同等の詳細度がある | 🟡 | ✅ |
| T-006 | 関連ポリシーファイルを更新する。(1) `CLAUDE.md` のディレクトリ構成テーブルに `metacognition/` を追加 (2) `.claude/skills/session-flow-policy/SKILL.md` セクション5のテーブルにメタ認知フローを追加 (3) `.claude/skills/triage-standard-policy/SKILL.md` セクション1.2 適用マトリクスに meta-manager/worker/evaluator を追加、セクション3.1 走査対象に metacognition-manager の定義ファイルを追加 | 全関連ファイルが更新され、新セッションタイプが各ポリシーで認識される状態 | 🟡 | ✅ |
| T-007 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-008 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

### L2-evaluator 向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | 全成果物を session-flow-policy / triage-standard-policy の基準で評価する。ライフサイクル完備・ペアリング対称性・課題起票手段・停止ルールを確認する | `06_eval_report.md` に全チェック項目の評価結果が記載されている | 🔴 | ⬜ |
| T-E02 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E03 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/ISS-XXX.md` を作成し、課題詳細を記載する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-08
