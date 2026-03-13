# タスクリスト: impl-worktree-parallel

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `07_issues_W_template.md` テンプレートを `sessions/impl/_template/` に新規作成する | ファイルが存在し、Worker 情報・課題メモセクションがある。`07_issues.md` と同じ起票フォーマットのコメントが含まれる | 🔴 | ✅ |
| T-002 | `impl-worker.md` を worktree 対応に更新する。具体的には: (1) 作業フロー step 5 の作業ディレクトリを worktree パスに変更、(2) step 10 の課題起票先を `07_issues_W<N>.md` に変更、(3) 外部リポジトリでの作業手順を worktree パスベースに書き換え、(4) 担当ファイルテーブルの `07_issues.md` → `07_issues_W<N>.md` 変更、(5) チェックポイント記録の Branch を `impl/<施策名>-W<N>` に変更、(6) 「ワーカー完了チェックリスト」セクションを新規追加 | 全6項目が反映済み。`initiative/` → `impl/` のブランチ名変更が全箇所に適用済み。関連ファイル一覧が更新済み | 🔴 | ✅ |
| T-003 | `SKILL.md` の並列ディスパッチ機構を更新する。具体的には: (1) 「事前準備（Wave ディスパッチ前）」サブセクション追加（worktree 作成・per-worker ファイル作成・事前検証チェックリスト）、(2) 「Wave 完了後処理」サブセクション追加（事後検証チェックリスト・マージ手順・課題統合・クリーンアップ）、(3) ディスパッチパラメータに Worker ID / worktree パス / per-worker ブランチ名 / 課題ファイルパスを追加、(4) B+C 集約手順に per-worker ブランチの git log 読み取りと課題統合ステップを追加、(5) マージコンフリクト解消手順を追加 | 全5項目が反映済み。`initiative/` → `impl/` のブランチ名変更が全箇所に適用済み | 🔴 | ✅ |
| T-004 | `36_file_task_division.md` テンプレートに「Worktree Configuration」セクションを追加する。Per-Worker Mapping テーブル（Worker / Work Log / Issues / External Branch / Worktree Path）を含める | セクションとテーブルが追加されている | 🟡 | ✅ |
| T-005 | `42_impl_work_report.md` テンプレートに「Merge Results」テーブルと「Consolidated Issues」セクションを追加する | 両セクションが追加されている | 🟡 | ✅ |
| T-006 | `impl-evaluator.md` の Phase 4 評価基準に worktree 関連チェック項目を追加する: (1) per-worker ブランチのマージ正常完了、(2) マージ後テスト PASS、(3) Assigned files 範囲外変更なし、(4) 07_issues.md への課題統合完了 | Phase 4 の評価基準に4項目が追加されている。`initiative/` → `impl/` のブランチ名変更が適用済み | 🟡 | ✅ |
| T-007 | impl-manager 配下の残りのエージェント定義（`investigation-worker.md`, `design-worker.md`, `impl-plan-worker.md`）のブランチ参照を `initiative/` → `impl/` に変更する | 全ファイルで `initiative/<施策名>` が `impl/<施策名>` に置換されている | 🟡 | ✅ |
| T-008 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |

## フェーズ2 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-009 | `docs/git-worktree-guideline.md` のステータスバナーを「一部統合済み」に更新し、「impl-manager ハイブリッド方式」セクションを追加する。ハイブリッド方式の設計判断（外部リポ worktree + セッションファイル分離）と3層検証チェックリストの概要を記載する | ステータス更新済み。impl-manager 実装セクションが追加されている | 🟡 | ✅ |
| T-010 | `docs/workflow.md` の実装セッションフローに worktree 記述を追加する。Phase 4 の並列ディスパッチフローに worktree 作成・マージ・クリーンアップのステップが反映されている | workflow.md の記述が SKILL.md の実態と一致している | 🟡 | ✅ |
| T-011 | メタルール横断検証を実施する: (1) フロー記述: 変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているか確認・修正、(2) workflow.md 同期: T-010 の結果を確認、(3) TG-008 基準連動: `triage-standard-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新。適用対象環境: CLI | 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている | 🔴 | ✅ |
| T-012 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

---
**作成者**: L1
**最終更新**: 2026-03-12
