# タスクリスト: リポジトリ間テンプレート同期の検証チェックリスト

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 実施ワーカー（l2-worker）向けタスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | sync-manager スキル定義の作成 | session-flow-policy §2 の全項目を満たす SKILL.md が作成されている | 🔴 | ⬜ |
| T-002 | sync-worker エージェント定義の作成 | session-flow-policy §3 の全項目を満たすエージェント定義が作成されている | 🔴 | ⬜ |
| T-003 | sync-evaluator エージェント定義の作成 | sync-worker との対称性を満たすエージェント定義が作成されている | 🔴 | ⬜ |
| T-004 | セッションテンプレートの作成 | `sessions/sync/_template/` に9ファイルが作成されている | 🔴 | ⬜ |
| T-005 | repo-sync-checklist にセクション5を追加 | 7観点がパラメータ化されて追加されている | 🔴 | ⬜ |
| T-006 | 連動更新: commit-message.md | sync-mgr/sync-worker/sync-eval が追加されている | 🔴 | ⬜ |
| T-007 | 連動更新: docs/workflow.md | 同期セッションフロー・ファイルオーナーシップ・コミット規約テーブルが更新されている | 🔴 | ⬜ |
| T-008 | 連動更新: session-flow-policy, triage-standard-policy | 両ファイルに sync セッションタイプが追加されている | 🔴 | ⬜ |
| T-009 | 作業中の知見を記録する（固定タスク） | ルール化候補・参考情報の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-010 | 課題のCSV転記（固定タスク） | 全課題に [転記済 ISS-XXX] or 転記不要が付いている | 🔴 | ⬜ |

### T-001: sync-manager スキル定義の作成
- **やること**: `.claude/skills/sync-manager/SKILL.md` を作成する。triage-manager を構造の参考とし、session-flow-policy §2 の必須要素を満たすこと
  - YAML フロントマター（name: sync-manager, description, user-invocable: true）
  - あなたの役割、セッション開始時のブランチ整理、入力解釈（`sync: <target-repo> [<direction>]`）
  - 作業フロー（テンプレートコピー → 事前調査 → 計画 → worker ディスパッチ → evaluator ディスパッチ → ゲート判定）
  - 担当ファイル、やること、やらないこと、ルール
  - ワーカーのディスパッチ手順、成果物確認観点、結果集約手順
  - 関連ファイル一覧

### T-002: sync-worker エージェント定義の作成
- **やること**: `.claude/skills/sync-manager/agents/sync-worker.md` を作成する。l2-worker を構造の参考とし、session-flow-policy §3 の必須要素を満たすこと
  - YAML フロントマター（name: sync-worker, description, tools）
  - あなたの役割（repo-sync-checklist のセクション1〜4に従い同期作業を実行）
  - 作業フロー（01_plan.md 読み → 壁打ちフェーズ → チェックリスト参照 → 同期実施 → 04_sync_report.md 作成）
  - 壁打ちフェーズ（03_work_log.md に記録）
  - 担当ファイル、やること、やらないこと、停止ルール
  - 知見セクション（ルール化候補 + 参考情報テーブル、04_sync_report.md に記載）
  - 関連ファイル一覧

### T-003: sync-evaluator エージェント定義の作成
- **やること**: `.claude/skills/sync-manager/agents/sync-evaluator.md` を作成する。l2-evaluator を構造の参考とし、session-flow-policy §3 の必須要素を満たすこと
  - YAML フロントマター（name: sync-evaluator, description, tools）
  - あなたの役割（repo-sync-checklist のセクション5の7つの検証観点で同期結果を評価）
  - 作業フロー（01_plan.md 読み → 壁打ちフェーズ → 検証観点のパラメータ具体化 → 評価実施 → 06_eval_report.md 作成）
  - 壁打ちフェーズ（05_eval_plan.md に記録）
  - 担当ファイル、やること、やらないこと、停止ルール
  - 知見セクション（ルール化候補 + 参考情報テーブル、06_eval_report.md に記載）
  - sync-worker との対称性確認
  - 関連ファイル一覧

### T-004: セッションテンプレートの作成
- **やること**: `sessions/sync/_template/` ディレクトリを作成し、9ファイルを作成する
  - `00_pre_investigation.md` — 事前調査テンプレート（両リポジトリの現状把握、同期対象の特定）
  - `01_plan.md` — 同期計画テンプレート（対象リポジトリ、同期方向、ファイルリスト、成功基準）
  - `02_dispatch_log.md` — ディスパッチ記録テンプレート
  - `03_work_log.md` — 作業履歴テンプレート（壁打ちフェーズフォーマット含む）
  - `04_sync_report.md` — 同期レポートテンプレート（チェックリストセクション1〜4に対応した構成、知見セクション含む）
  - `05_eval_plan.md` — 評価計画テンプレート（壁打ちフェーズフォーマット含む）
  - `06_eval_report.md` — 評価レポートテンプレート（7つの検証観点の結果テーブル、知見セクション含む）
  - `07_issues.md` — 課題バッファテンプレート
  - `08_gate_review.md` — ゲート判定テンプレート（横展開・知見ルーティングセクション含む）
  - 参考: initiatives テンプレートと triage テンプレートを確認し、sync に合った形式に調整すること

### T-005: repo-sync-checklist にセクション5を追加
- **やること**: `.claude/skills/repo-sync-checklist/SKILL.md` にセクション5「同期結果の検証チェックリスト（7つの検証観点）」を追加する
  - 7観点をパラメータ化して記載（`{source_repo}`, `{target_repo}`, `{sync_scope}`）
  - 各観点に検証内容・検証方法・パラメータを明記
  - 検証チェック（各観点に対して実施するチェックボックス）を追加
  - 関連ファイル一覧を更新（sync-manager, sync-worker, sync-evaluator を追加、バックログ参照を削除）

### T-006: 連動更新（commit-message.md）
- **やること**: `.claude/rules/commit-message.md` の非施策作業テーブルに `sync-mgr` / `sync-worker` / `sync-eval` を追加。既存 `sync` 行に「git レベルの単純同期」と補足

### T-007: 連動更新（docs/workflow.md）
- **やること**: `docs/workflow.md` に「リポジトリ間同期セッション フロー」セクションを追加。ファイルオーナーシップ・コミットメッセージテーブルも更新

### T-008: 連動更新（session-flow-policy, triage-standard-policy）
- **やること**:
  1. `session-flow-policy/SKILL.md` §5 に sync を追加
  2. `triage-standard-policy/SKILL.md` の適用マトリクス・記録先・ペアリング構造・走査対象を更新

### T-009: 作業中の知見を記録する（固定タスク）
- **やること**: 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載）

### T-010: 課題のCSV転記（固定タスク）
- **やること**: `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/ISS-XXX.md` を作成し、課題詳細を記載する

## 評価ワーカー（l2-evaluator）向けタスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| E-001 | session-flow-policy 準拠チェック | 各チェック項目の PASS/FAIL 判定が記録されている | 🔴 | ⬜ |
| E-002 | 7つの検証観点の汎用性チェック | 汎用性の判定結果が記録されている | 🔴 | ⬜ |
| E-003 | 連動更新の完全性チェック | 連動更新の完全性が判定されている | 🔴 | ⬜ |
| E-004 | 評価中の知見を記録する（固定タスク） | ルール化候補・参考情報の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| E-005 | 課題の起票とCSV転記（固定タスク） | 全課題に [転記済 ISS-XXX] or 転記不要が付いている | 🔴 | ⬜ |

### E-001: session-flow-policy 準拠チェック
- **やること**: T-001〜T-003 で作成されたスキル・エージェント定義が session-flow-policy の必須要素を満たしているかを検証する
  - SKILL.md 必須要素（§2）、エージェント必須要素（§3）、ペアリング対称性（§3.2）、新セッションタイプ追加チェックリスト（§5.1）

### E-002: 7つの検証観点の汎用性チェック
- **やること**: repo-sync-checklist セクション5 の7観点が triage-process-brushup 以外の同期シナリオにも適用可能かを検証する

### E-003: 連動更新の完全性チェック
- **やること**: T-006〜T-008 の連動更新が完全かを検証する

### E-004: 評価中の知見を記録する（固定タスク）
- **やること**: 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する

### E-005: 課題の起票とCSV転記（固定タスク）
- **やること**: 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する

---
**作成者**: L1
**最終更新**: 2026-03-08
