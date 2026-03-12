# タスクリスト: l1-impl-manager セッションタイプの新設

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク（実施ワーカー向け）

### スキル・エージェント定義の作成

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `.claude/skills/l1-impl-manager/SKILL.md` を作成する。入力パターン（`impl: <施策名>` / `impl-continue: <パス>`）、セッションライフサイクルtodo（4フェーズのオーケストレーション手順）、壁打ちフェーズ、並列ディスパッチ機構（Wave方式）、B+C作業ログ集約手順、クローズ手順を含める。`manager-common-policy` の §2-§8 を参照で記述量を抑える。 | SKILL.md が存在し、4フェーズのオーケストレーションフロー・入力パターン・ライフサイクルtodo・並列ディスパッチ・B+C集約・クローズ手順が記載されている | 🔴 | ⬜ |
| T-002 | `.claude/skills/l1-impl-manager/agents/investigation-worker.md` を作成する。Phase 1 のコードベース調査ワーカー。対象リポジトリの構造調査、依存関係マッピング、変更対象ファイルの特定を担当。作業フロー・担当ファイル・壁打ちフェーズ・停止ルールを含める。 | investigation-worker.md が存在し、作業フロー・担当ファイル（11, 12, 07）・壁打ちフェーズ・停止ルールが記載されている | 🔴 | ⬜ |
| T-003 | `.claude/skills/l1-impl-manager/agents/design-worker.md` を作成する。Phase 2 の設計ドキュメント作成ワーカー。`02_impl_design.md` をプライマリ成果物として、コンポーネント設計・API変更・データフロー・エラーハンドリング・テスト方針を記載。 | design-worker.md が存在し、`02_impl_design.md` の作成を主タスクとする作業フロー・担当ファイル（02, 21, 22, 07）が記載されている | 🔴 | ⬜ |
| T-004 | `.claude/skills/l1-impl-manager/agents/impl-plan-worker.md` を作成する。Phase 3 の実装計画ワーカー。`36_file_task_division.md` をプライマリ成果物として、ファイルレベルのタスク分割・Conflict Check Matrix・並列度分析・テストコマンド指定を含める。 | impl-plan-worker.md が存在し、`36_file_task_division.md` の作成フォーマット（IMPL-XXX形式・Conflict Check Matrix）が定義されている | 🔴 | ⬜ |
| T-005 | `.claude/skills/l1-impl-manager/agents/impl-worker.md` を作成する。Phase 4 のコード実装ワーカー。テスト失敗リトライループ（max 3回）、チェックポイント記録（START/TEST-RUN/COMPLETE/ESCALATE）、エスカレーション条件（設計矛盾・スコープ外ファイル・テスト3回失敗）を含める。 | impl-worker.md が存在し、テストリトライループ・チェックポイント記録フォーマット・エスカレーション条件が明確に定義されている | 🔴 | ⬜ |
| T-006 | `.claude/skills/l1-impl-manager/agents/impl-evaluator.md` を作成する。全フェーズ共通評価者。マネージャーからフェーズ固有のコンテキスト（評価対象ファイル・成功基準）を受け取り、評価計画→評価実施→レポート作成のフローを実行。 | impl-evaluator.md が存在し、フェーズパラメータ化された評価フロー・担当ファイル（フェーズ別の eval_plan/eval_report）・壁打ちフェーズ・停止ルールが記載されている | 🔴 | ⬜ |

### テンプレートファイルの作成

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-007 | `sessions/impl/_template/` ディレクトリを作成し、グローバルテンプレート（`00_proposal.md`, `01_plan.md`, `02_impl_design.md`, `07_issues.md`, `08_gate_summary.md`）を作成する。`00_proposal.md` はコード実装向けにカスタマイズ（対象リポジトリ・ブランチ・受入基準のセクション追加）。 | 5つのグローバルテンプレートが存在し、`00_proposal.md` にコード実装固有セクションが含まれている | 🔴 | ⬜ |
| T-008 | Phase 1 テンプレート（`10_investigation_tasks.md`, `11_investigation_work_log.md`, `12_investigation_work_report.md`, `13_investigation_eval_plan.md`, `14_investigation_eval_report.md`, `15_investigation_gate.md`）を作成する。 | Phase 1 の6テンプレートファイルが存在する | 🟡 | ⬜ |
| T-009 | Phase 2 テンプレート（`20_design_tasks.md`, `21_design_work_log.md`, `22_design_work_report.md`, `23_design_eval_plan.md`, `24_design_eval_report.md`, `25_design_gate.md`）を作成する。 | Phase 2 の6テンプレートファイルが存在する | 🟡 | ⬜ |
| T-010 | Phase 3 テンプレート（`30_impl_plan_tasks.md`, `31_impl_plan_work_log.md`, `32_impl_plan_work_report.md`, `33_impl_plan_eval_plan.md`, `34_impl_plan_eval_report.md`, `35_impl_plan_gate.md`, `36_file_task_division.md`）を作成する。`36_file_task_division.md` は IMPL-XXX 形式のタスク分割テンプレートと Conflict Check Matrix を含める。 | Phase 3 の7テンプレートファイルが存在し、`36_file_task_division.md` にIMPL-XXX形式とConflict Check Matrixが含まれている | 🟡 | ⬜ |
| T-011 | Phase 4 テンプレート（`40_impl_tasks.md`, `42_impl_work_report.md`, `43_impl_eval_plan.md`, `44_impl_eval_report.md`, `45_impl_gate.md`）を作成する。`42_impl_work_report.md` はB+C集約用のフォーマット。Phase 4 の `41_impl_work_log_W*.md` はテンプレート不要（動的生成）。 | Phase 4 の5テンプレートファイルが存在し、`42_impl_work_report.md` にB+C集約フォーマットが含まれている | 🟡 | ⬜ |

### 連動更新

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-012 | `.claude/rules/commit-message.md` に `impl-mgr`, `impl-worker`, `impl-evaluator` のセッション種別を追加する。施策作業テーブルに追記し、例を追加する。 | commit-message.md の施策作業テーブルに3種別が追加され、例が記載されている | 🔴 | ⬜ |
| T-013 | `docs/workflow.md` に l1-impl-manager セッションフローの記述を追加する。4フェーズ構成・並列実装・B+C作業ログの概要を人間向けに可視化する。 | workflow.md に l1-impl-manager セクションが追加されている | 🔴 | ⬜ |
| T-014 | `.claude/skills/triage-standard-policy/SKILL.md` のライフサイクル適用マトリクスに l1-impl-manager を追加する。 | triage-standard-policy に l1-impl-manager の行が追加されている | 🟡 | ⬜ |
| T-015 | `.claude/skills/session-flow-policy/SKILL.md` のセッションタイプ一覧に l1-impl-manager を追加する（該当テーブルがある場合）。 | session-flow-policy に l1-impl-manager の記載がある | 🟡 | ⬜ |

### 知見記録・課題転記（固定タスク）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-016 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-017 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

### メタルール横断検証（固定タスク — ルール・テンプレート変更施策）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-018 | 以下3領域のメタルール横断検証を実施し、結果を `04_work_report.md` に記録する: (1) 変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているか確認・修正 (2) `docs/workflow.md` の該当セクションが変更内容と整合しているか確認・更新 (3) `triage-standard-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新。適用対象環境: CLI（ローカルCLI専用のセッションタイプのため） | 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている | 🔴 | ⬜ |

## フェーズ1 タスク（評価ワーカー向け）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E02 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-12
