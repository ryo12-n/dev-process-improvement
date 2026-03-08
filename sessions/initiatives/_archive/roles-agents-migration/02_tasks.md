# タスクリスト: roles/ → .claude/agents/ 移行

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 注意事項

- **作業対象リポジトリ**: `/home/nr202/projects/ai-driven-dev-patterns`（本リポジトリではない）
- T-001〜T-005 は順序依存あり（T-001 → T-002 → T-003 → T-004 → T-005 の順で実施）

## フェーズ1 タスク

### 実施ワーカー（l2-worker）向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `roles/_base/common.md` の共通ルールを `.claude/rules/` に分離する。以下のテーマ別にルールファイルを作成する: (1) `agent-common-workflow.md`（基本的な作業ループ、壁打ちフェーズ、完了報告形式、知見記載義務）、(2) `agent-restrictions.md`（共通禁止事項）、(3) `worktree-rules.md`（worktree 環境での共通ルール）。既存の `.claude/rules/commit-message.md` は `common.md` セクション5のコミット規約と重複するため、内容を統合する。セクション1（アーキテクチャ説明）とセクション2（リポジトリ構造）は CLAUDE.md に既にあるため移行不要 | (1) 3つのルールファイルが `.claude/rules/` に作成されている (2) `common.md` のセクション3〜8の内容が漏れなく移行されている (3) コミット規約が既存の `commit-message.md` と統合されている | 🔴 | ✅ |
| T-002 | 8つの専門ロール（feature_builder, test_writer, reviewer, bug_fixer, refactorer, optimizer, documentarian, openspec_specialist）を `.claude/agents/*.md` に変換する。各ファイルに YAML フロントマター（name, description, tools, model）を付与する。`common.md` への参照（「作業開始前に common.md を読んでください」）は削除する（T-001 で `.claude/rules/` に移行済みのため自動適用される）。ロール定義の内容・ロジックは変更しない（フォーマット変換のみ） | (1) 8ファイルが `.claude/agents/` に配置されている (2) 各ファイルに有効な YAML フロントマターがある (3) `tools:` フィールドで適切なツール制限が設定されている（例: reviewer は Read, Grep, Glob, Bash のみ） (4) ロール定義の内容が元ファイルと同等である | 🔴 | ✅ |
| T-003 | `dev_manager.md` のオーケストレーションロジックを `.claude/skills/dispatcher/SKILL.md` に統合する。現在の dispatcher はシナリオ判定のみだが、dev_manager のセッション管理・ロール起動・フェーズゲート判定の機能を統合する。統合後の SKILL.md は `roles/dev_manager.md` の全機能を包含すること。ロール起動時の参照先を `roles/<role>.md` から `.claude/agents/<role>.md` に変更する | (1) dispatcher SKILL.md に dev_manager の全機能（セッション管理、ロール起動、フェーズゲート判定、知見収集、課題管理）が統合されている (2) ロール起動の参照先が `.claude/agents/` になっている (3) 既存の dispatcher 機能（シナリオ判定）が維持されている | 🔴 | ✅ |
| T-004 | `roles/` を参照している全ファイルのパスを更新する。対象は grep で `roles/` にヒットするファイルのうち、`docs/design/` 配下（歴史的設計書）と `roles/` 自身を除く全ファイル。主な置換パターン: (1) `roles/<role>.md` → `.claude/agents/<role>.md` (2) `roles/_base/common.md` → `.claude/rules/`（適切なルールファイル名に） (3) `roles/` → `.claude/agents/`（ディレクトリ参照）(4) `roles/dev_manager.md` → `.claude/skills/dispatcher/SKILL.md` | (1) `grep -r 'roles/' --include='*.md'` で `docs/design/` 以外にヒットしない (2) 更新後のパスが実在するファイルを指している (3) README, CLAUDE.md, .claude/skills/, .claude/rules/, sessions/, triage/, backlog/, inbox/ の全ファイルが更新されている | 🔴 | ✅ |
| T-005 | `roles/` ディレクトリを `git rm -r` で削除する。削除前に T-001〜T-004 が全て完了していることを確認する | (1) `roles/` ディレクトリが存在しない (2) `git status` で `roles/` 配下の全ファイルが deleted として表示される | 🔴 | ✅ |
| T-006 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-007 | ルール変更連動更新チェックリスト（rule-change-checklist スキル）を実施する。特に注意: (1) ai-driven-dev-patterns 側の `docs/workflow.md` 等の人間向けドキュメント更新 (2) session-flow-policy の関連ファイル一覧更新 (3) triage テンプレートの参照パス更新 | チェックリストの全項目が確認済みで、`03_work_log.md` に確認結果が記録されている | 🔴 | ✅ |
| T-008 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

### 評価ワーカー（l2-evaluator）向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-101 | 移行の網羅性を検証する: (1) `grep -r 'roles/' --include='*.md'` で残存参照を検出し、歴史的記録以外にヒットがないことを確認 (2) `.claude/agents/` の8ファイルが元の `roles/` の内容と同等であることを確認 (3) `.claude/rules/` の共通ルールが `common.md` の内容を漏れなくカバーしていることを確認 | 検証結果が `06_eval_report.md` に記録されている | 🔴 | ✅ |
| T-102 | dispatcher SKILL.md の統合品質を検証する: (1) dev_manager の全機能（8セクション）が統合されているか (2) 既存の dispatcher 機能が維持されているか (3) ロール起動の参照先が正しいか | 検証結果が `06_eval_report.md` に記録されている | 🔴 | ✅ |
| T-103 | agents 形式の妥当性を検証する: (1) 各 agent の YAML フロントマターが有効か (2) `tools:` フィールドのツール制限がロールの責務と整合しているか (3) `description:` がロールの用途を適切に表現しているか | 検証結果が `06_eval_report.md` に記録されている | 🔴 | ✅ |
| T-104 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-105 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

---
**作成者**: L1
**最終更新**: 2026-03-08
