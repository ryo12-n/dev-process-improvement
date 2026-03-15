# 評価計画: backlog-to-issue-scheduled

## 壁打ちフェーズ [2026-03-15 13:00]

### 理解のサマリー
- 評価の目的: L2-worker が構築した schedule トリガー付き backlog-to-issue ワークフローが、01_plan.md の成功基準5項目を満たしているか評価する
- 評価スコープ: `.github/workflows/backlog-to-issue.yml`（scheduled-create ジョブ）、`.github/scripts/select-backlog-candidate.sh`、不要ワークフロー削除、GHA セキュリティ準拠、既存 workflow_dispatch ジョブへの回帰有無
- 完了条件: 06_eval_report.md に全項目の評価結果とエビデンスが記載、知見セクション記載済み、課題起票・転記判断済み

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク完了報告、成果物一覧、知見記録あり）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（5項目すべて客観的に検証可能）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read/Bash/Grep でファイル内容を直接検証可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.github/workflows/backlog-to-issue.yml`（schedule トリガー + scheduled-create ジョブ）
- `.github/scripts/select-backlog-candidate.sh`（全優先度対応・BL-ID 出力）
- 削除確認: `backlog-candidate-propose.yml`、`backlog-auto-execute.yml`
- 04_work_report.md、07_issues.md の品質

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-1 | schedule トリガー設定 | `backlog-to-issue.yml` の `on.schedule` セクションを確認 | `cron: '0 */6 * * *'` が設定されている |
| E-2 | 候補選定スクリプト | `select-backlog-candidate.sh` のフィルタ条件・ソート順・出力項目を確認 | 全優先度（低→中→高順）で候補を選定し、`id`（BL-XXX）を `$GITHUB_OUTPUT` に出力する |
| E-3 | 重複チェック実装 | `scheduled-create` ジョブの重複チェックステップを確認 | `gh issue list --search "[BL-XXX] in:title" --state all` で既存 Issue を検索し、存在時はスキップする |
| E-4 | 不要ワークフロー削除 | `backlog-candidate-propose.yml` と `backlog-auto-execute.yml` のファイル存在確認 | 両ファイルが削除されている |
| E-5 | GHA セキュリティルール準拠 | `scheduled-create` ジョブの全 `${{ }}` 使用箇所を確認 | `run:` ブロック内で `${{ }}` を直接展開せず、`env:` 経由で渡している |
| E-6 | 既存 workflow_dispatch の回帰有無 | `create-issue` ジョブの `if` 条件と構造を確認 | `if: github.event_name == 'workflow_dispatch'` が設定され、schedule 時に実行されない |
| E-7 | 作業レポートの品質 | `04_work_report.md` の構成・内容を確認 | タスク実績・成果物一覧・知見記録（ルール化候補・参考情報 各1行以上）が記載されている |
| E-8 | 課題メモの品質 | `07_issues.md` の記載内容・転記判断を確認 | 課題に転記判断が付いている |

## 評価スケジュール
- 全項目を1回の評価セッションで実施

## 前提・制約
- GHA 環境での実行時テストは不可（構文・ロジックレビューのみ）
- cron スケジュールの実際の動作検証は本評価のスコープ外

---
**作成者**: L2（評価）
**作成日**: 2026-03-15
