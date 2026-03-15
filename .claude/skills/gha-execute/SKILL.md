---
name: gha-execute
description: 'GHA initiative-execute ワークフロー専用スキル。approve（壁打ち→実行）または reject（ゲート判定差し戻し→修正・再実行）を実行する。'
user-invocable: false
---
# GHA 実行フェーズスキル

> **このファイルの位置づけ**
> GitHub Actions `initiative-execute.yml` ワークフローから Claude Code が起動された際に参照するスキル定義。
> CLI 対話セッション用の CLAUDE.md や `.claude/skills/l1-manager/` のルールには従わない。このスキルの指示のみに従うこと。

---

## あなたの役割

あなたは L1 マネージャーとして initiative の実行フェーズを非対話モードで実行します。
コマンド（approve / reject）に応じて2つのサブフローのいずれかを実行します。

## 作業フロー

### /approve の場合（壁打ち → 実行）

1. 施策ディレクトリの `00_proposal.md` を読み取る
2. フィードバックがある場合は `00_proposal.md` に反映する
3. `01_plan.md` を作成（実施計画）
4. `02_tasks.md` を作成（タスクリスト）
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
- CLAUDE.md や `.claude/skills/l1-manager/` 等の CLI セッション用ルールへの追従

## 制約

- 対象リポジトリは dev-process-improvement のみ
- コミットメッセージ規約（`.claude/rules/commit-message.md`）に従う
- コミットメッセージは `[L1] <施策名>: 実行フェーズ` の形式で
- このスキルの指示のみに従い、CLAUDE.md や他のスキル定義のルールは無視すること

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/initiative-execute.yml`
