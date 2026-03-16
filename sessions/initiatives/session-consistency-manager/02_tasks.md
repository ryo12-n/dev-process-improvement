# タスクリスト: session-consistency-manager

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 |
|-------------|------|---------|
| なし | - | プロセス改善の定型作業（セッション定義作成）のため省略 |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-008 | スキル定義・テンプレート・連動更新の作成 |
| L2-evaluator | T-E01〜T-E03 | 自己整合性チェック・対称性検証 |

## フェーズ1 タスク（スキル・エージェント定義作成）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `.claude/skills/session-consistency-manager/SKILL.md` を作成する。config-optimizer-manager の SKILL.md を参照パターンとし、SC-001〜SC-008 のターゲット定義を含める。session-flow-policy §2 の必須セクション（あなたの役割・作業フロー・やること・やらないこと・オーケストレーション・担当ファイル）を全て含めること。TG-008 との関係を「完全独立」と明記すること | SKILL.md が session-flow-policy §2 の全必須セクションを含み、SC ターゲット定義・3フェーズオーケストレーション・担当ファイルテーブルが記載されている | 🔴 | ⬜ |
| T-002 | `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md` を作成する。config-collection-worker.md を参照パターンとし、SC ターゲット別の収集手順を記載する。session-flow-policy §3 の必須セクションを全て含めること | エージェント定義が session-flow-policy §3 の全必須セクション（役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）を含み、壁打ちフェーズが定義されている | 🔴 | ⬜ |
| T-003 | `.claude/skills/session-consistency-manager/agents/sc-analysis-worker.md` を作成する。config-analysis-worker.md を参照パターンとし、SC ターゲット別の分析手順を記載する | 同上 | 🔴 | ⬜ |
| T-004 | `.claude/skills/session-consistency-manager/agents/sc-proposal-worker.md` を作成する。config-proposal-worker.md を参照パターンとし、OPT-XXX 形式の提案作成手順を記載する | 同上 | 🔴 | ⬜ |
| T-005 | `.claude/skills/session-consistency-manager/agents/sc-evaluator.md` を作成する。config-optimizer-evaluator.md を参照パターンとし、Phase 1〜3 のフェーズ別評価基準を含める。対称性確認テーブルを含めること | エージェント定義が全必須セクションを含み、フェーズ別評価基準と対称性確認テーブルが定義されている | 🔴 | ⬜ |
| T-005a | `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` の初期テンプレートを作成する。SC-001〜SC-008 のセクション構造を含む空テンプレート | SC-001〜SC-008 の全セクションが構造化されたテンプレートが存在する | 🟡 | ⬜ |

## フェーズ2 タスク（セッションテンプレート作成）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-006 | `sessions/session-consistency/_template/` 配下に15ファイルのテンプレートを作成する。`sessions/config-optimization/_template/` をコピー元とし、SC ターゲット固有の内容に置き換える。マネージャーレベル: 00_pre_investigation.md, 01_plan.md, 02_dispatch_log.md, 03_report.md, 04_gate_review.md。フェーズゲート: phase-1-collection/01_gate.md, phase-2-analysis/01_gate.md, phase-3-proposal/01_gate.md。ワーカーレベル: workers/_template/ 配下の7ファイル | 15ファイルが全て存在し、config-optimizer テンプレートと対称的な構造を持つ | 🔴 | ⬜ |

## フェーズ3 タスク（連動ファイル更新）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-007 | 連動ファイル5件を更新する: (1) `.claude/rules/commit-message.md` に `sc-mgr` / `sc-worker` / `sc-eval` エントリ追加 (2) `.claude/skills/manager-common-policy/SKILL.md` §1 適用対象テーブルに session-consistency-manager 行追加 (3) `.claude/skills/session-flow-policy/SKILL.md` §5 セッションタイプテーブルに行追加 (4) `.claude/skills/triage-standard-policy/SKILL.md` §1.2 適用マトリクスに sc-manager/sc-worker/sc-evaluator 列追加、§1.3 記録先対応に行追加、§2.1 ペアリング構造に行追加、§3.1 走査対象にファイルパス追加 (5) `docs/workflow.md` にセッション一貫性チェックフローの記述追加。適用対象環境: CLI / SDK いずれでも可 | 5ファイル全てが更新され、新セッションタイプが各ファイルに正しく登録されている | 🔴 | ⬜ |

## 固定タスク（実施ワーカー向け）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-008 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-009 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |
| T-010 | メタルール横断検証を実施する: (1) 変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているか確認・修正 (2) `docs/workflow.md` の該当セクションが変更内容と整合しているか確認・更新 (3) `triage-standard-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新。結果を `04_work_report.md` に記録する | 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている | 🔴 | ⬜ |

## 固定タスク（評価ワーカー向け）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | session-flow-policy §5.1 の新セッションタイプ追加チェックリストを全項目実施する。結果を `06_eval_report.md` に記録する | チェックリスト全項目の結果が記載されている | 🔴 | ⬜ |
| T-E02 | triage-standard-policy §3.2 のチェック項目（A〜E）を新セッション定義に適用し、自己整合性を検証する。結果を `06_eval_report.md` に記録する | チェック項目 A〜E の全結果が記載されている | 🔴 | ⬜ |
| T-E03 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E04 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-16
