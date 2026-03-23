# タスクリスト: 情報ソース管理・評価サイクル基盤の構築

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-008 | ai-research-notebook への書き込みあり |
| L2-evaluator | T-E01〜T-E03 | - |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-008 / T-E01〜T-E03 | Wave 1 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | - |

> **方式**: 逐次（1ワーカーずつ） / 並列（Wave 方式、`.claude/rules/parallel-dev.md` 参照）

## 施策フェーズ1 タスク

### 実施ワーカー（l2-worker）向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `spaces/ai-news-lab/source-management/` ディレクトリ構造を作成する。サブディレクトリ: `discovery-log/`, `evaluation-log/`, `review-log/`, `templates/` | 全ディレクトリが存在する（.gitkeep 配置） | 🔴 | ✅ |
| T-002 | `source-management/evaluation-criteria.md` を作成する。5軸（速報性20%・独自性20%・信頼性20%・関連性25%・効率性15%）の判定基準とスコアリングガイドを定義。バージョン管理セクションを含む。Perplexity が参照して人間のフィードバックからスコアリングできる記述にする | 5軸の判定基準・スコアリングガイド（1-5段階の具体的説明）・総合スコア算出方法・判定基準テーブル・版管理セクションが記載されている | 🔴 | ✅ |
| T-003 | `source-management/source-list.md` を作成する。表形式テーブルで、列: ID(S-XXX)/ソース名/URL/カテゴリ/粒度/ステータス/追加日/最終評価日/総合スコア/備考。ステータス定義（candidate/trial/active/inactive/removed）を含む。カテゴリ初期値（ニュースサイト/個人ブログ・ニュースレター/SNSアカウント/YouTube・Podcast/論文リポジトリ/企業公式ブログ/コミュニティ・フォーラム）を記載 | テーブル列が全て存在、ステータス定義セクションあり、カテゴリ一覧セクションあり | 🔴 | ✅ |
| T-004 | `source-management/templates/source-discovery-template.md` を作成する。YAML frontmatter（date, tags, task_type: source-discovery）。セクション: 発見経路、発見ソース一覧（各ソースの URL/カテゴリ/粒度/初期印象/推奨アクション）、source-list.md 反映チェックリスト | frontmatter が既存テンプレートと一貫した形式。必要セクションが全て存在 | 🟡 | ✅ |
| T-005 | `source-management/templates/source-evaluation-template.md` を作成する。2層構造: 人間フィードバック（自由記述、観点ガイドのみ提示）+ AI スコアリング結果（evaluation-criteria.md 参照でPerplexityが記入するテーブル）。ステータス変更提案セクションを含む | 人間向け自由記述セクションとAIスコアリングテーブルが分離されている。evaluation-criteria.md への参照がある | 🟡 | ✅ |
| T-006 | `source-management/templates/quarterly-review-template.md` を作成する。セクション: レビュー対象期間サマリー、ソース別評価サマリー（スコア推移付き）、カテゴリ別カバレッジ評価、探索テーマ提案、ステータス変更決定 | 全セクションが存在。period フィールドが既存の monthly-analysis-template と一貫した形式 | 🟡 | ✅ |
| T-007 | `source-management/README.md` を作成する。運用ガイドとして: ディレクトリ構成、サイクル全体のワークフロー（日次/随時→隔週→四半期の3層）、ステータス遷移ルール（candidate→trial→active/inactive/removed）、既存タスクとの接続点を記載 | ワークフロー図・ステータス遷移・ディレクトリ構成が記載されている | 🔴 | ✅ |
| T-008 | `spaces/ai-news-lab/README.md` のディレクトリ構成テーブルに `source-management/` の1行を追記する。既存の記述は変更しない | source-management の説明行がテーブルに追加されている。既存行が変更されていない | 🟡 | ✅ |
| T-009 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-010 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

### 評価ワーカー（l2-evaluator）向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | SC-1〜SC-5 の成功基準に基づき成果物を評価する。全テンプレートの frontmatter が既存テンプレートと一貫した形式か、evaluation-criteria.md のスコアリングガイドが Perplexity にとって解釈可能か、README のワークフロー記述が実際のディレクトリ構造と一致するかを検証する | 評価レポートに全成功基準の合否が記載されている | 🔴 | ⬜ |
| T-E02 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E03 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-20
