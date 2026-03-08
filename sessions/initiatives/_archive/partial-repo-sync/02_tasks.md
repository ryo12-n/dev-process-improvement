# タスクリスト: 2つのリポジトリの部分的同期

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク（実施ワーカー向け）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `sessions/` ディレクトリを作成し、`git mv` で `triage/` → `sessions/triage/`、`initiatives/` → `sessions/initiatives/` を移動する | 旧パス `triage/`, `initiatives/` が存在せず、`sessions/` 配下に移動されている | 🔴 | ✅ |
| T-002 | `sessions/triage/_archive/` ディレクトリを作成する（`.gitkeep` を配置） | `sessions/triage/_archive/` が存在する | 🔴 | ✅ |
| T-003 | triage-manager スキル定義（`.claude/skills/triage-manager/SKILL.md`）のテンプレートコピー手順を改善する。セッション作成時は `_template/` 直下ファイル（00〜04）のみコピーし `workers/` は空ディレクトリで作成する。ワーカーセット作成時は `sessions/triage/_template/workers/_template/` から直接 `workers/set-N/` にコピーする方式に変更する | スキル定義内のコピー手順が更新され、`workers/_template/` がセッションフォルダにコピーされない手順になっている | 🔴 | ✅ |
| T-004 | 以下のファイル内の `triage/` → `sessions/triage/`、`initiatives/` → `sessions/initiatives/` のパス参照を更新する: `.claude/skills/l1-manager/SKILL.md`, `agents/l2-worker.md`, `agents/l2-evaluator.md`, `.claude/skills/triage-manager/SKILL.md`, `agents/triage-worker.md`, `agents/triage-evaluator.md`, `.claude/skills/rule-change-checklist/SKILL.md`, `.claude/rules/commit-message.md`, `.claude/rules/session-start-branch-cleanup.md` | 上記9ファイル内の旧パス参照がすべて新パスに更新されている | 🔴 | ✅ |
| T-005 | 以下のドキュメントのパス参照を更新する: `CLAUDE.md`（ディレクトリ構成テーブル含む）, `docs/workflow.md`, `docs/management-system-guide.md`, `docs/implementation.md`, `docs/coordination-protocol-guideline.md`, `docs/git-worktree-guideline.md` | 上記6ファイル内の旧パス参照がすべて新パスに更新されている | 🔴 | ✅ |
| T-006 | 旧パス（`triage/`, `initiatives/`）がリポジトリ内のどのファイルにも残っていないことを `grep -r` で検証する。テンプレートファイル内やgit履歴への言及など、更新不要なものは除外リストに記載する | grep 結果が空、または除外理由が明記された一覧がある | 🔴 | ✅ |
| T-007 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-008 | ルール変更連動更新チェックリスト（rule-change-checklist スキル）を実施する | チェックリストの全項目が確認済み | 🔴 | ✅ |
| T-009 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

## フェーズ2 タスク（実施ワーカー向け）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-010 | ai-driven-dev-patterns への同期チェックリストを作成する。dev-process-improvement の `sessions/` 構成を基に、導入すべき要素・差異が許容されるポイント・統一すべきポイントを一覧化する | チェックリスト文書が作成され、同期対象・許容差異・統一要件が明記されている | 🟡 | ✅ |

## 評価ワーカー向けタスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | フェーズ1の成果物を評価する。パス参照の更新漏れがないか、テンプレートコピー手順が正しく改善されているかを検証する | 評価レポートに検証結果と判定が記載されている | 🔴 | ⬜ |
| T-E02 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E03 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-08
