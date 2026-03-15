# 評価計画: initiative-dispatcher

## 壁打ちフェーズ [2026-03-15]

### 理解のサマリー
- 評価の目的: L2-worker の作業成果（ワークフロー変更6件 + 新規2件）が `01_plan.md` の成功基準5項目を満たしているかを検証する
- 評価スコープ: `.github/workflows/` 配下の initiative 関連ワークフロー全体、`04_work_report.md`、`07_issues.md`
- 完了条件: 全評価項目の判定が完了し、`06_eval_report.md` に記載されていること

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク完了報告済み、知見セクション記載あり）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（5項目が具体的に定義されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read/Grep/Glob でワークフローファイルの検証が可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.github/workflows/initiative-dispatcher.yml`（新規）
- `.github/workflows/initiative-question.yml`（新規）
- `.github/workflows/initiative-wallbash.yml`（変更）
- `.github/workflows/initiative-execute.yml`（変更）
- `.github/workflows/initiative-close.yml`（変更）
- `.github/workflows/backlog-to-issue.yml`（変更）
- `04_work_report.md`（作業レポート）
- `07_issues.md`（課題メモ）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-001 | `issue_comment` トリガーの排他性 | 全 initiative 関連 `.yml` ファイルを Grep で `issue_comment` 検索 | `initiative-dispatcher.yml` のみが `issue_comment` トリガーを持つこと |
| E-002 | ルーティングテーブルの完全性 | `initiative-dispatcher.yml` の case 文を `00_proposal.md` のルーティングテーブル（5パターン）と照合 | 5パターン全てが正しいラベル条件・起動先で実装されていること |
| E-003 | フェーズ不一致エラーハンドリング | ディスパッチャーの各コマンド分岐で不一致時の処理を確認 | 全コマンドでフェーズ不一致時にエラーコメントが返ること |
| E-004 | `backlog-to-issue.yml` の直接 dispatch | ワークフローの内容を確認 | Issue 作成後に `gh workflow run initiative-wallbash.yml` が実行されること。`initiative-start` ラベル付与が除去されていること |
| E-005 | `initiative-start` ラベルの完全廃止 | 全ワークフローファイルを Grep で `initiative-start` 検索 | ワークフロー `.yml` ファイル内に `initiative-start` への参照がないこと（README は対象外） |
| E-006 | `@ai-task` 形式の統一 | wallbash / execute の次ステップ案内テキストを確認 | 全ての次ステップ案内が `@ai-task /command` 形式であること |
| E-007 | 既存 Claude プロンプトの非変更 | wallbash / execute / close の Claude プロンプト部分を確認 | トリガー・入力部分のみ変更され、プロンプトの趣旨・指示内容が維持されていること |
| E-008 | シェルインジェクションリスク | ディスパッチャーの `dispatch_inputs` JSON 構築部分を精査 | ユーザー入力（ARGS 等）が JSON 構築に直接展開される箇所でインジェクションリスクがないこと |
| E-009 | 作業レポートの完全性 | `04_work_report.md` の内容を確認 | 全タスクの実績・成果物一覧・知見（ルール化候補・参考情報各1行以上）が記載されていること |
| E-010 | 課題メモの適切性 | `07_issues.md` の内容を確認 | 全課題に転記判断が付いていること |

## 評価スケジュール
- E-001 〜 E-010 を順に評価する

## 前提・制約
- 動作確認（実際の Issue コメントからのディスパッチ）はデプロイ後に必要であり、本評価はコードレビューベースで実施する

---
**作成者**: L2（評価）
**作成日**: 2026-03-15
