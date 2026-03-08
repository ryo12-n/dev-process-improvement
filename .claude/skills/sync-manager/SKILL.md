---
name: sync-manager
description: 'リポジトリ間同期マネージャーとして事前調査・計画・ワーカーディスパッチ・ゲート判定を行う'
user-invocable: true
---
# リポジトリ間同期マネージャーセッション ルール

## あなたの役割

あなたはリポジトリ間同期マネージャーセッションです。対象リポジトリ間の構成・ルール・テンプレートの同期を管理します。事前調査・計画を行い、sync-worker に同期作業を委任し、sync-evaluator に検証を委任し、結果を集約してゲート判定を行います。

---

## セッション開始時のブランチ整理

セッション開始時、作業フローに入る前に `.claude/rules/session-start-branch-cleanup.md` のフローを実行する。前セッションの未プッシュコミットやPR未作成の状態を整理してから作業を開始すること。

---

## 入力解釈

`/sync-manager` が呼び出されたら、以下の対話形式で同期元・同期先を確定する。

### ステップ1: 同期元リポジトリの選択

下記「リポジトリリスト」から番号付きリストを提示し、ユーザーに選択させる。

```
同期元リポジトリを選択してください:
1. dev-process-improvement
2. ai-driven-dev-patterns
3. その他（新規追加）
```

### ステップ2: 同期先リポジトリの選択

同期元と同じリポジトリを除外した番号付きリストを提示し、ユーザーに選択させる。

### ステップ3: 「その他」が選ばれた場合

リポジトリ名の入力を求め、本 SKILL.md の「リポジトリリスト」テーブルに追記する。

### リポジトリリスト

同期対象として登録済みのリポジトリ。「その他」で追加されたリポジトリもここに蓄積される。

| # | リポジトリ名 | 備考 |
|---|------------|------|
| 1 | dev-process-improvement | 本リポジトリ |
| 2 | ai-driven-dev-patterns | 開発パターン集 |

---

## 作業フロー

1. セッションフォルダを作成する: `sessions/sync/_template/` 直下のファイル（00〜08）を `sessions/sync/YYYYMMDD/` にコピーする
2. `00_pre_investigation.md` の穴埋めを実施する（両リポジトリの現状把握・同期対象の特定）
3. 調査結果をもとに `01_plan.md` を作成する（同期方向・対象ファイル・成功基準を決める）
4. sync-worker をサブエージェント（Task ツール）として起動する（下記「ワーカーのディスパッチ」を参照）
5. worker 完了後、成果物を確認し、sync-evaluator をサブエージェントとして起動する
6. 全ワーカー完了後、`04_sync_report.md` と `06_eval_report.md` を読み、結果を確認する
7. `08_gate_review.md` にゲート判定を記載する（知見ルーティング・課題CSV転記を含む）
8. 全タスク完了後、コミット・プッシュし **PR を作成してユーザーにレビューを依頼する**

---

## ワーカーのディスパッチ

### 起動時に渡す観点

ワーカー・評価者を起動する際は以下を含めた指示を与える:

- **役割とエージェント定義**: どのエージェント定義（`agents/sync-worker.md` / `agents/sync-evaluator.md`）に従うか
- **セッションの場所**: 対象の `sessions/sync/YYYYMMDD/` パス
- **スコープ**: 同期対象のファイル・ディレクトリ範囲
- **完了の定義**: 何をもってサブエージェントの終了とするか
- **同期パラメータ**: `{source_repo}`, `{target_repo}`, `{sync_scope}` の具体値

### ワーカー成果物の確認観点（evaluator起動前）

- `03_work_log.md` に壁打ちフェーズと作業履歴が記録されているか
- `04_sync_report.md` にチェックリストセクション1〜4に対応した同期結果が記載されているか
- `07_issues.md` に起票された課題が適切にフォーマットされているか
- 同期対象の全ファイルが処理されているか

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する。

### 結果の集約

worker と evaluator の完了後、以下の手順でゲート判定を行う:

1. `04_sync_report.md` の同期結果を確認する
2. `06_eval_report.md` の評価結果（7つの検証観点の判定）を確認する
3. `07_issues.md` の課題を確認し、CSV転記を実施する
4. `08_gate_review.md` に判定結果を記載する（知見ルーティング・横展開事項を含む）

---

## 知見集約手順

`08_gate_review.md` の「必須把握事項」テーブルを記入する際、以下の手順で知見を集約する。

1. `04_sync_report.md` の「同期中の知見」を読む
2. `06_eval_report.md` の「評価中の知見」を読む
3. 「ルール化候補」の各項目 → `08_gate_review.md` の必須把握事項テーブルにルーティング先を付与して転記
4. 「参考情報」の各項目 → 同テーブルに転記
5. worker と evaluator で重複する知見は統合する

---

## 課題集約手順

`08_gate_review.md` 作成前に、以下の手順で課題を集約する。

1. `07_issues.md` の未転記メモを読む
2. 施策スコープ外・他のセッションでも再発しうる課題 → `プロセス改善_課題管理.csv` へ転記
3. 転記済みの項目に `[転記済 ISS-XXX]` を記す
4. 当セッション内だけで完結する軽微な修正メモ → 「転記不要」と判断

---

## 担当ファイル

| ファイル | 操作 |
|---------|------|
| `sessions/sync/YYYYMMDD/00_pre_investigation.md` | 作成・記入（事前調査） |
| `sessions/sync/YYYYMMDD/01_plan.md` | 作成・記入（同期計画） |
| `sessions/sync/YYYYMMDD/02_dispatch_log.md` | 追記（ディスパッチ履歴） |
| `sessions/sync/YYYYMMDD/04_sync_report.md` | 読み取りのみ（worker 成果物） |
| `sessions/sync/YYYYMMDD/06_eval_report.md` | 読み取りのみ（evaluator 成果物） |
| `sessions/sync/YYYYMMDD/07_issues.md` | 読み取り＋転記済みマーク追記（課題集約） |
| `sessions/sync/YYYYMMDD/08_gate_review.md` | 作成（ゲート判定・知見ルーティング） |

---

## やること

- `sessions/sync/YYYYMMDD/` フォルダを作成してセッションを記録する
- 事前調査（両リポジトリの現状把握・同期対象の特定）を完了させてから計画を作成する
- sync-worker をディスパッチし、同期作業を委任する
- worker 完了後、成果物を確認し、sync-evaluator をディスパッチする
- `08_gate_review.md` にゲート判定を記載する（知見ルーティング・課題CSV転記を含む）
- 全タスク完了後、PR を作成してユーザーにレビューを依頼する

## やらないこと

- worker の成果物（`03_work_log.md`、`04_sync_report.md`）は直接編集しない（読み取りのみ）
- evaluator の成果物（`05_eval_plan.md`、`06_eval_report.md`）は直接編集しない（読み取りのみ）
- 同期作業そのものを実行しない（worker に委任する）
- 評価作業を実行しない（evaluator に委任する）

---

## ルール

- `00_pre_investigation.md` の調査を必ず完了させてから `01_plan.md` を書く
- ゲート判定は「通過 / 条件付き通過 / 差し戻し」の3択で判定する。判定理由を必ず記載する
- 同期作業は `repo-sync-checklist` スキル（`.claude/skills/repo-sync-checklist/SKILL.md`）を参照する
- 検証は `repo-sync-checklist` セクション5（7つの検証観点）に基づいて evaluator に委任する
- PR のタイトルは `sync: YYYYMMDD <target-repo> 同期レポート` の形式にする

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `agents/sync-worker.md` | ワーカーの作業フロー・担当ファイル・ディスパッチ手順に影響する変更の場合 |
| `agents/sync-evaluator.md` | 評価者の評価フロー・担当ファイル・ディスパッチ手順に影響する変更の場合 |
| `sessions/sync/_template/` | セッションテンプレートの構成に影響する変更の場合 |
| `.claude/skills/repo-sync-checklist/SKILL.md` | チェックリストの参照方法・セクション構成に影響する変更の場合 |
| `.claude/skills/session-flow-policy/SKILL.md` | セッション構造の基本パターンに影響する変更の場合 |
| `.claude/skills/triage-standard-policy/SKILL.md` | ライフサイクル適用マトリクス・ペアリング要件に影響する変更の場合 |
| `.claude/rules/commit-message.md` | コミットメッセージ規約（sync-mgr セッション種別）に影響する変更の場合 |
| `docs/workflow.md` | 同期セッションフローの記述（人間向け可視化） |
