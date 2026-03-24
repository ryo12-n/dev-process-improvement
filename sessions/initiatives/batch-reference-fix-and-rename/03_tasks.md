# タスクリスト: batch-reference-fix-and-rename

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 全タスクが S 複雑度の機械的作業 | Worker |
| なし | - | 同上 | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-007 | 1ワーカー逐次実行 |
| L2-evaluator | 全タスクの成果物評価 | worker 完了後に起動 |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-007 | Wave 1→2 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | Wave 1（T-001〜T-003）→ Wave 2（T-004〜T-007） |

> **方式**: 逐次（1ワーカーずつ） / 並列（Wave 方式、`.claude/rules/parallel-dev.md` 参照）

## Wave 1 タスク（並列実行可だが逐次実行）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `.claude/skills/l1-manager/agents/l2-plan-worker.md` の L199 にある `triage-standard-policy` を `session-lifecycle-policy` に置換する | 1. L199 が `session-lifecycle-policy` に更新済み 2. `Grep` で `.claude/skills/` および `.claude/rules/` 配下に `triage-standard-policy` のアクション可能な残存参照がゼロ（`session-consistency-reference.md` の SC リファレンスデータはスコープ外） | 🔴 | ✅ |
| T-002 | `.claude/rules/rename-reference-check.md` を新規作成する。内容: (1) リネーム前に旧名称で Grep 全文検索を実行する義務 (2) 検出された全箇所を新名称に更新する義務 (3) 更新後に旧名称で再度 Grep を実行し残存参照ゼロを確認する義務 (4) 対象範囲: `.claude/skills/`、`docs/`、`sessions/*/_template/`、`.claude/rules/`、`backlog/` (5) ファイル廃止（DELETE）時も同様に旧名称の残存参照チェックを義務化する | 1. `.claude/rules/rename-reference-check.md` が存在する 2. 上記5項目がすべて含まれている 3. `rule-change-checklist` §4 と重複せず補完的である | 🔴 | ✅ |
| T-003 | 以下4件のバックログエントリを `git rm` で削除する: `backlog/entries/SC-008壊れた参照修正.md`、`backlog/entries/SCチェックQuickWins一括是正.md`、`backlog/entries/リネーム時全文検索チェック義務化ルール追加.md`、`backlog/entries/sync-worker同期先コミット漏れ防止.md` | 1. 4件のファイルが `git rm` で削除されている 2. `backlog/backlog.csv` の自動生成状況を確認し、CSV との整合性を報告 | 🟡 | ✅ |

## Wave 2 タスク（Wave 1 完了後）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-004 | `rule-change-checklist` スキル（`.claude/skills/rule-change-checklist/SKILL.md`）のチェックリスト全7項目を確認する。確認ポイント: (1) `l2-plan-worker.md` の「関連ファイル一覧」連動更新要否 (2) `docs/workflow.md` への影響 (3) `session-lifecycle-policy/SKILL.md` への影響 (4) パス変更走査対象の網羅性 (5) deny リスト対称性 (6) テンプレート連動更新 (7) コミットメッセージ規約確認 | チェックリスト全7項目の結果（確認済み / 修正済み / 該当なし）が `phase-2-execution/set-1/02_worker_log.md` に記録されている | 🔴 | ✅ |
| T-005 | メタルール横断検証: (1) 変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているか確認・修正 (2) `docs/workflow.md` の該当セクションが変更内容と整合しているか確認・更新 (3) `session-lifecycle-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新 | 3領域の検証結果（合格/修正済/該当なし）が `phase-2-execution/set-1/03_worker_report.md` に記載されている | 🔴 | ✅ |
| T-006 | 作業中に発見した知見を `phase-2-execution/set-1/03_worker_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-007 | `phase-2-execution/set-1/07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` に作成する。転記時は `issues/_template.md` をコピーして作成。該当なしの場合は「転記対象なし」と記載 | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

---
**作成者**: L1
**最終更新**: 2026-03-24
