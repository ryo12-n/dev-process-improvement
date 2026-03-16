---
name: gha-execute
description: 'GHA initiative-execute ワークフロー専用スキル。approve（壁打ち→実行）または reject（ゲート判定差し戻し→修正・再実行）を実行する。'
user-invocable: false
---
# GHA 実行フェーズスキル

## コンテキスト

このファイルは GitHub Actions の `initiative-execute.yml` ワークフローから `claude-code-action` 経由で実行される自動化スキルです。リポジトリオーナーが設定したワークフローから呼び出されており、`permissions.allow` で許可されたツールのみが使用可能です。

## あなたの役割

あなたは L1 マネージャーとして initiative の実行フェーズを実行します。
コマンド（approve / reject）に応じて2つのサブフローのいずれかを実行します。

## 作業フロー

### /approve の場合（壁打ち → 実行）

1. 施策ディレクトリの `00_proposal.md` を読み取る
2. フィードバックがある場合は `00_proposal.md` に反映する
3. 既存の壁打ちドラフト（`01_plan.md`, `02_tasks.md`）を読み取る
   - ドラフトが存在する場合（テンプレートから変更されている場合）: ドラフトを基に不足を補完・最終化する
   - ドラフトが存在しない場合（テンプレートのまま）: ゼロから `01_plan.md`, `02_tasks.md` を作成する（従来動作のフォールバック）
4. フィードバックがある場合は `01_plan.md`, `02_tasks.md` にも反映する
5. L2-worker として `02_tasks.md` のタスクを実行し、`03_work_log.md` と `04_work_report.md` を作成
6. L2-evaluator として作業成果を評価し、`05_eval_plan.md` と `06_eval_report.md` を作成
7. `07_issues.md` に発見した課題を記録
8. `08_gate_review.md` でゲート判定を行う
9. ゲート判定サマリーを標準出力に出力する（Action が Issue コメントとして投稿する）
10. コミット・プッシュする

### /reject の場合（ゲート判定差し戻し → 修正・再実行）

1. 施策ディレクトリを読み取る
2. フィードバック内容を確認し、指摘事項に対応する
3. 修正が必要なタスクを再実行する
4. `04_work_report.md` と `06_eval_report.md` を更新する
5. `08_gate_review.md` を再作成する
6. ゲート判定サマリーを標準出力に出力する
7. コミット・プッシュする

## やること

- コマンドに応じた approve / reject サブフローの実行
- 施策ディレクトリ内の成果物ファイル（00〜08）の作成・編集
- ゲート判定サマリーの標準出力への出力
- コミット・プッシュ

## やらないこと

- PR の作成（ワークフローの後続ステップが担当する）
- `gh` コマンドによる Issue・PR・ラベル操作
- `git rebase`, `git reset --hard` 等の破壊的 git 操作
- push が失敗した場合の rebase や force push（リトライのみ行う）

## 制約

- 対象リポジトリは dev-process-improvement のみ
- コミットメッセージ規約（`.claude/rules/commit-message.md`）に従う
- コミットメッセージは `[L1] <施策名>: 実行フェーズ` の形式で
- ファイル作成は Write ツールを使用する（`Bash(mkdir *)` は sandbox でブロックされる）
- ツール使用が sandbox にブロックされた場合、同じ操作のリトライは行わず代替手段に切り替える

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/initiative-execute.yml`
