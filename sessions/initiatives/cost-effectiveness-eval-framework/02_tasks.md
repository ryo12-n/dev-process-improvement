# タスクリスト: 費用対効果評価フレームワークの標準化

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業 | Worker |
| なし | - | プロセス改善の定型作業 | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-006 | 逐次実行（T-001→T-002→T-003→T-004→T-005→T-006） |
| L2-evaluator | T-E01〜T-E03 | Worker 完了後にディスパッチ |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-006 | Wave 1（逐次） |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | 小規模施策のため並列不要 |

## 施策フェーズ1 タスク

### 実施ワーカー（l2-worker）向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `.claude/templates/cost-effectiveness-evaluation.md` を新規作成する。ソース: `sessions/initiatives/_archive/ai-automation-tool-review/04_work_report.md` T-003（L97-121）。以下のセクションを含む: (1) 概要、(2) 評価軸定義テーブル（頻度・手動コスト・実装難易度、各3段階のレベル説明付き）、(3) 算出式（優先度スコア = 頻度 x 手動コスト / 実装難易度）、(4) 評価テーブルテンプレート（コピー用）、(5) カスタマイズ指針。自動化候補固有カラム（「自動化手段」等）は含めず汎用化する。「4軸」の定義を明確化すること（独立変数3つ + 算出結果1つ） | `.claude/templates/cost-effectiveness-evaluation.md` が存在し、上記5セクションすべてが記載されている。SC-1 を充足 | 🔴 | ⬜ |
| T-002 | `automation-candidates/_template.md` の `## 費用対効果分析` セクション（L31）の直上に追跡コメント `<!-- 費用対効果分析: 基底テンプレート .claude/templates/cost-effectiveness-evaluation.md を参照 -->` を追加する。既存テーブル（L32-38）は変更しない | `grep -r "基底テンプレート .claude/templates/cost-effectiveness-evaluation.md" automation-candidates/` が `_template.md` を返す。SC-2 を充足 | 🔴 | ⬜ |
| T-003 | `CLAUDE.md` のディレクトリ構成テーブルに `.claude/templates/` の行を追加し、文書分類ポリシーテーブルにも `.claude/templates/` の行を追加する。挿入位置は行番号ではなくテーブルの文脈で判断すること。既存の `templates/` 行との区別を明確にする用途説明を記載する。適用対象環境: CLI / SDK 共通 | CLAUDE.md のディレクトリ構成テーブルに `.claude/templates/` の行が存在し、文書分類ポリシーテーブルにも `.claude/templates/` の行が存在する。SC-3 を充足 | 🔴 | ⬜ |
| T-004 | メタルール横断検証を実施する。(1) CLAUDE.md に追加した `.claude/templates/` 記載が既存構成と矛盾しないか確認、(2) `docs/workflow.md` の更新要否を判断（必要なら更新）、(3) `.claude/rules/` や `.claude/skills/` で `.claude/templates/` に言及すべき箇所がないか確認。結果を `04_work_report.md` に記録する | 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている | 🔴 | ⬜ |
| T-005 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-006 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題があれば `issues/entries/ISS-XXX.md` を作成する（`issues/_template.md` をコピー）。転記時は課題詳細を記載する。全課題に `[転記済 ISS-XXX]` または「転記不要」の判断を付ける | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-17
