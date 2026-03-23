# 評価計画: 情報ソース管理・評価サイクル基盤の構築 — Set-1

## 壁打ちフェーズ [2026-03-20 16:00]

### 理解のサマリー
- 評価の目的: L2-worker が ai-research-notebook リポジトリに作成した情報ソース管理・評価サイクル基盤（ディレクトリ構造、評価基準、ソースリスト、テンプレート3種、README）の品質を SC-1〜SC-5 に基づき検証する
- 評価スコープ: `spaces/ai-news-lab/source-management/` 配下の全成果物 + `spaces/ai-news-lab/README.md` への追記
- 完了条件: T-E01〜T-E03 の全完了。評価レポートに全成功基準の合否が記載されていること

### 前提条件チェック
- [x] 評価対象（03_worker_report.md）の完成度: 十分（T-001〜T-010 全て完了済み）
- [x] 評価基準（02_plan.md の成功基準）の明確さ: 評価可能（SC-1〜SC-5 が明確に定義済み）
- [x] 評価に必要なツール・アクセス権限: 確認済み（ai-research-notebook は `--add-dir` で参照可能）
- [x] 参照ドメインエージェント: 指定なし → 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 参照ドメインエージェント

| エージェント名 | 参照パス | 評価への活用方針 |
|-------------|---------|---------------|
| なし | - | - |

## 評価対象

ai-research-notebook リポジトリの `spaces/ai-news-lab/source-management/` 配下に作成された以下の成果物:
1. ディレクトリ構造（discovery-log/, evaluation-log/, review-log/, templates/）
2. evaluation-criteria.md
3. source-list.md
4. templates/source-discovery-template.md
5. templates/source-evaluation-template.md
6. templates/quarterly-review-template.md
7. source-management/README.md
8. ai-news-lab/README.md への追記

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | SC-1: ディレクトリ構造 | ディレクトリ存在確認（ls コマンド） | discovery-log/, evaluation-log/, review-log/, templates/ が全て存在し .gitkeep が配置されている |
| 2 | SC-2: source-list.md のテーブル構造 | ファイル内容確認 | ID/ソース名/URL/カテゴリ/粒度/ステータス/追加日/最終評価日/総合スコア/備考 の列が全て存在。ステータス定義・カテゴリ一覧セクションあり |
| 3 | SC-3: evaluation-criteria.md | ファイル内容確認 | 5軸の判定基準・スコアリングガイド（1-5段階の具体的説明）・総合スコア算出方法・判定基準テーブル・版管理セクションが存在 |
| 4 | SC-4: テンプレート3種 | ファイル存在・frontmatter 確認 | 3種テンプレートが存在し、frontmatter が既存テンプレート（date, tags, task_type）と一貫した形式 |
| 5 | SC-5: README.md 運用ガイド | ファイル内容確認 | ワークフロー（3層サイクル）・ステータス遷移・ディレクトリ構成が記載されている |
| 6 | 追加検証: Perplexity 解釈可能性 | evaluation-criteria.md のスコアリングガイドが AI にとって解釈可能か検証 | 各軸のスコア基準が具体的かつ曖昧性が低い。判定ヒントがフリーテキストからの抽出に有用 |
| 7 | 追加検証: README 整合性 | README のワークフロー記述とディレクトリ構造の一致確認 | README に記載されたパス・ファイル名が実際の構造と一致 |
| 8 | 追加検証: ai-news-lab/README.md 追記 | 既存記述が壊されていないか確認 | source-management/ の行が追加され、他の行が変更されていない |

## 評価スケジュール
- 壁打ち → 評価計画作成 → SC-1〜SC-5 順次検証 → 追加検証 → レポート作成

## 前提・制約
- ai-research-notebook リポジトリへの読み取りアクセスのみ使用

---
**作成者**: L2（評価）
**作成日**: 2026-03-20
