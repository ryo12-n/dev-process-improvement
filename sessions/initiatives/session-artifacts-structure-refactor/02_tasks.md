# タスクリスト: session-artifacts-structure-refactor

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 |
|-------------|------|---------|
| なし | - | プロセス改善の定型作業（テンプレート更新・スキル定義の参照更新）であり、外部専門知識は不要 |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-007 | config-optimizer → impl の順で実施。テンプレートファイル移動 + SKILL.md/エージェント参照更新 |
| L2-evaluator | T-E01〜T-E02 | 旧ファイル名残存チェック、参照整合性検証 |

## 実施タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | config-optimizer テンプレートに phase ディレクトリ追加: `sessions/config-optimization/_template/` に `phase-1-collection/01_gate.md`, `phase-2-analysis/01_gate.md`, `phase-3-proposal/01_gate.md` を作成。gate テンプレートの内容は SKILL.md 内のゲート判定フォーマットを参考に作成する | 3 phase ディレクトリと各 `01_gate.md` が存在すること | 🔴 | ⬜ |
| T-002 | config-optimizer SKILL.md + エージェント定義の参照更新: `15_collection_gate.md` → `phase-1-collection/01_gate.md`, `25_analysis_gate.md` → `phase-2-analysis/01_gate.md`, `35_proposal_gate.md` → `phase-3-proposal/01_gate.md` に全参照を更新 | `.claude/skills/config-optimizer-manager/` 配下で旧ファイル名（`15_collection_gate`, `25_analysis_gate`, `35_proposal_gate`）の grep 結果が 0 件 | 🔴 | ⬜ |
| T-003 | impl テンプレートのディレクトリ再構成: `sessions/impl/_template/` に `phase-1-investigation/`, `phase-2-design/`, `phase-3-impl-plan/`, `phase-4-impl/` を作成し、対応する 26 ファイルを移動・連番リネーム。旧ファイルを削除 | `ls -R sessions/impl/_template/` の出力が新構造（ルート 7 ファイル + 4 phase ディレクトリ）と一致。旧ファイル（`10_`〜`45_` プレフィックス）がルート直下に存在しない | 🔴 | ⬜ |
| T-004 | impl SKILL.md + エージェント定義の参照更新: `.claude/skills/l1-impl-manager/SKILL.md` および `agents/` 配下の全エージェント定義ファイルで旧パスを新パスに更新（例: `10_investigation_tasks.md` → `phase-1-investigation/01_tasks.md`） | `.claude/skills/l1-impl-manager/` 配下で旧ファイル名（`10_`〜`45_` プレフィックス）の grep 結果が 0 件 | 🔴 | ⬜ |
| T-005 | docs/workflow.md の連動更新: SKILL.md の変更に合わせて、config-optimizer および impl セクションのファイル名参照を新構造に更新する | `docs/workflow.md` 内に旧ファイル名参照が残っていないこと | 🟡 | ⬜ |
| T-006 | メタルール横断検証: (1) 変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているか確認・修正 (2) `docs/workflow.md` の該当セクション整合確認 (3) `triage-standard-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新 | 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている | 🔴 | ⬜ |
| T-007 | 知見記録・CSV 転記: 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録（ルール化候補 + 参考情報）。`07_issues.md` の未転記課題を `プロセス改善_課題管理.csv` へ転記 | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載。全課題に `[転記済 ISS-XXX]` または「転記不要」の判断 | 🔴 | ⬜ |

## 評価タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | 旧ファイル名残存チェック: リポジトリ全体で `15_collection_gate`, `25_analysis_gate`, `35_proposal_gate`, `10_investigation`, `11_investigation`, `20_design`, `21_design`, `30_impl_plan`, `31_impl_plan`, `40_impl`, `41_impl`, `42_impl`, `43_impl`, `44_impl`, `45_impl` を grep し更新漏れがないことを確認 | grep 結果が 0 件（既存セッションインスタンスは対象外） | 🔴 | ⬜ |
| T-E02 | 参照整合性検証: SKILL.md + エージェント定義内で参照される全ファイルパスが、対応するテンプレートディレクトリ内に実在することを確認。triage/metacognition/BM/automation/sync のテンプレートが未変更であることを `git diff` で確認 | 全参照パスが実在。非対象セッションに差分なし | 🔴 | ⬜ |

## ファイル対応表（impl テンプレート — L2-worker の参照用）

| 旧パス | 新パス |
|-------|--------|
| `10_investigation_tasks.md` | `phase-1-investigation/01_tasks.md` |
| `11_investigation_work_log.md` | `phase-1-investigation/02_work_log.md` |
| `12_investigation_work_report.md` | `phase-1-investigation/03_work_report.md` |
| `13_investigation_eval_plan.md` | `phase-1-investigation/04_eval_plan.md` |
| `14_investigation_eval_report.md` | `phase-1-investigation/05_eval_report.md` |
| `15_investigation_gate.md` | `phase-1-investigation/06_gate.md` |
| `20_design_tasks.md` | `phase-2-design/01_tasks.md` |
| `21_design_work_log.md` | `phase-2-design/02_work_log.md` |
| `22_design_work_report.md` | `phase-2-design/03_work_report.md` |
| `23_design_eval_plan.md` | `phase-2-design/04_eval_plan.md` |
| `24_design_eval_report.md` | `phase-2-design/05_eval_report.md` |
| `25_design_gate.md` | `phase-2-design/06_gate.md` |
| `30_impl_plan_tasks.md` | `phase-3-impl-plan/01_tasks.md` |
| `31_impl_plan_work_log.md` | `phase-3-impl-plan/02_work_log.md` |
| `32_impl_plan_work_report.md` | `phase-3-impl-plan/03_work_report.md` |
| `33_impl_plan_eval_plan.md` | `phase-3-impl-plan/04_eval_plan.md` |
| `34_impl_plan_eval_report.md` | `phase-3-impl-plan/05_eval_report.md` |
| `35_impl_plan_gate.md` | `phase-3-impl-plan/06_gate.md` |
| `36_file_task_division.md` | `phase-3-impl-plan/07_file_task_division.md` |
| `40_impl_tasks.md` | `phase-4-impl/01_tasks.md` |
| `41_impl_work_log_W_template.md` | `phase-4-impl/02_work_log_W_template.md` |
| `42_impl_work_report.md` | `phase-4-impl/03_work_report.md` |
| `43_impl_eval_plan.md` | `phase-4-impl/04_eval_plan.md` |
| `44_impl_eval_report.md` | `phase-4-impl/05_eval_report.md` |
| `45_impl_gate.md` | `phase-4-impl/06_gate.md` |

---
**作成者**: L1
**最終更新**: 2026-03-16
