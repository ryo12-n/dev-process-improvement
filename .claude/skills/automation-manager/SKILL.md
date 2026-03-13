---
name: automation-manager
description: 'オートメーションマネージャーとして自動化候補の探索・評価・追跡を定期的に行う'
user-invocable: true
---
# オートメーションマネージャーセッション ルール

## あなたの役割

あなたはオートメーションマネージャーセッションです。自動化候補の探索・再評価・実装進捗追跡・backlog 起票提案を定期的に行います。事前調査・計画を行い、1〜N組のワーカー＋評価者セットをディスパッチして走査を委任し、結果を集約してレポートを作成します。

### triage・backlog-maintenance との責務の違い

- **triage**: inbox/backlog/CSV の日常的なハウスキーピング + ルール準拠チェック
- **backlog-maintenance**: backlog エントリの陳腐化を深掘り分析する専用セッション
- **automation**: skills/rules/テンプレートの定型作業を走査し、自動化候補の発見・再評価・進捗追跡を行う専用セッション

---

## セッション開始時のブランチ整理

セッション開始時、作業フローに入る前に `.claude/rules/session-start-branch-cleanup.md` のフローを実行する。前セッションの未プッシュコミットやPR未作成の状態を整理してから作業を開始すること。

---

## セッションライフサイクル todo 登録

> **共通パターン**: `manager-common-policy` §8 に従う（義務・登録パターン・進捗追跡）。

ブランチ整理完了後、作業フロー開始前に以下の 8 ステップを TaskCreate で登録する。

1. セッションフォルダ作成（テンプレートコピー）
2. 事前調査（00_pre_investigation.md の穴埋め）
3. 実施計画作成（01_plan.md）
4. ワーカーセット作成・ディスパッチ
5. 結果集約・レポート作成（03_report.md）
6. ゲート判定（04_gate_review.md）
7. アクション実施（automation-candidates 変更・backlog 起票提案・CSV 更新等）
8. コミット・プッシュ・PR 作成

---

## 作業フロー

1. セッションフォルダを作成する: `sessions/automation/_template/` 直下のファイル（00〜04）のみを `sessions/automation/YYYYMMDD/` にコピーし、`sessions/automation/YYYYMMDD/workers/` は空ディレクトリとして作成する（`_template/workers/_template/` はコピーしない）
2. `00_pre_investigation.md` の穴埋めを実施する（現状把握）
   - `automation-candidates/entries/` 内の全エントリのステータス・優先度スコア・最終評価日を確認する
   - `automation-candidates/automation-candidates.csv` と `entries/` の整合性を確認する
   - `.claude/skills/`、`.claude/rules/`、`sessions/*/` の追加・変更状況を確認する
   - `backlog/entries/` 内の自動化関連エントリを確認する
   - `sessions/initiatives/` および `sessions/initiatives/_archive/` の自動化関連施策の状況を確認する
   - `プロセス改善_課題管理.csv` の関連課題を確認する
3. 調査結果をもとに `01_plan.md` を作成する（今回の重点・ワーカー割り当てを決める）
4. ワーカーセットを作成・ディスパッチする（下記「ワーカーのディスパッチ」を参照）
5. 全セット完了後、ワーカーのスキャンレポートと評価レポートを集約して `03_report.md` を作成する（知見集約・課題集約セクションを含む）
6. `04_gate_review.md` にゲート判定を記載する（知見ルーティング・課題CSV転記を含む）
7. レポートに基づくアクションを実施する（automation-candidates 更新・backlog 起票提案・CSV 更新等）
8. 全タスク完了後、コミット・プッシュし **PR を作成してユーザーにレビューを依頼する**

---

## AT タスク定義

| ID | 名称 | スキャン対象 | 目的 |
|----|------|------------|------|
| AT-001 | 新規自動化候補スキャン | `.claude/skills/`, `.claude/rules/`, `sessions/*/`, `docs/` | skills/rules/テンプレートの追加・変更に伴い新たに生まれた定型作業を検出 |
| AT-002 | 既存候補の再評価 | `automation-candidates/entries/*.md`, CSV | 優先度スコア・実装難易度・自動化手段の妥当性を環境変化に基づき再評価 |
| AT-003 | 実装進捗確認 | `backlog/entries/*.md`, `sessions/initiatives/`, `_archive/` | backlog 起票済み候補の施策化・実装状況を追跡 |
| AT-004 | backlog 起票提案 | AT-001〜AT-003 の結果 | 新規候補や優先度変更候補を backlog エントリとして起票提案 |

---

## ワーカーセット数の判断基準

事前調査の結果をもとに、以下のガイドラインでワーカーセット数を決定する。マネージャーは常に裁量を持つ。

| 条件 | 推奨セット数 |
|------|------------|
| automation-candidates エントリ ≤ 15件 | 1セット（全ATタスク） |
| automation-candidates エントリ 16〜30件 | 2セット（AT-001+AT-002 / AT-003+AT-004） |
| automation-candidates エントリ > 30件 | 3セット（新規スキャン / 再評価 / 進捗確認+起票提案） |

判断根拠は `01_plan.md` の「ワーカー割り当て」セクションに記録する。

---

## ワーカーのディスパッチ

### セット作成手順

1. `sessions/automation/_template/workers/_template/` を `sessions/automation/YYYYMMDD/workers/set-N/` にコピーする（セッションフォルダ内の `workers/_template/` ではなく、リポジトリの `_template/workers/_template/` から直接コピーする）
2. `workers/set-N/01_tasks.md` に割り当てる AT タスクを記入する
3. automation-worker をサブエージェント（Task ツール）として起動する
4. ワーカー完了後、automation-evaluator をサブエージェントとして起動する
5. `02_dispatch_log.md` に起動・完了を記録する

### ディスパッチパターン

> **共通順序制約**: `manager-common-policy` §2.2 に従う（基本逐次・セット内は worker → evaluator）。

- **逐次の理由（automation 固有）**: AT タスク間に依存がある（AT-001 の新規候補が AT-004 の起票提案に影響する等）
- **例外**: ファイル分離が確認できた場合、マネージャー判断で並列ディスパッチ可（`.claude/rules/parallel-dev.md` に従う）

### 起動時に渡す観点

> **共通4項目**: `manager-common-policy` §2.1 に従う（役割とエージェント定義・セッションの場所・スコープ・完了の定義）。

### ワーカー成果物の確認観点（evaluator起動前）

> **共通最小3項目**: `manager-common-policy` §3 に従う（タスク分類・レポート記載・課題バッファ）。

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する（`manager-common-policy` §7 参照）。

### 結果の集約

全セット完了後、以下の手順で `03_report.md` を作成する:

1. 各 `workers/set-N/04_scan_report.md` の走査結果を AT タスク別にマージする
2. 各 `workers/set-N/06_eval_report.md` の評価結果を「Worker Set サマリ」セクションに反映する
3. 知見集約: `manager-common-policy` §5 に従い、各セットの知見を `03_report.md` の知見集約セクションに集約する
4. 課題集約: `manager-common-policy` §6 に従い、各セットの課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
5. 評価で指摘された不備がある場合は、対応方針を決定してレポートに記載する

---

## 知見集約手順

> **共通手順**: `manager-common-policy` §5 に従う（集約手順 §5.1 + ルーティング判断基準 §5.2）。

automation 固有の入力ソース:
- 各 `workers/set-N/06_eval_report.md` の「評価中の知見」
- 各 `workers/set-N/04_scan_report.md` の「走査中の知見」

集約先: `03_report.md` の知見集約テーブル → `04_gate_review.md` の「必須把握事項」テーブルにルーティング先を付与して転記する。

---

## 課題集約手順

> **共通手順**: `manager-common-policy` §6 に従う（07_issues.md → CSV転記 → ISS-XXX.md）。

automation 固有の補足:
- `03_report.md` の課題集約セクションにワーカーセット別件数と転記済み課題を記載する

---

## 出力先ガイドライン

分析結果は以下の基準で出力先を判断する:

| 分析結果の性質 | 出力先 | 例 |
|-------------|--------|-----|
| 新規自動化候補の検出 | `automation-candidates/entries/AC-XXX.md` + CSV | 「新しい定型作業を検出、AC-015 として登録」 |
| 既存候補の優先度変更 | `automation-candidates/entries/AC-XXX.md` + CSV 更新 | 「環境変化により AC-005 の優先度を 1.0 → 3.0 に変更」 |
| backlog 起票提案 | `03_report.md` の「backlog 起票提案」セクション | 「AC-002 は優先度スコアが高く backlog 起票を提案」 |
| 実装完了の確認 | `automation-candidates/entries/AC-XXX.md` + CSV 更新 | 「AC-001 の施策が完了、ステータスを実装完了に更新」 |
| 明確な課題（対応が必要） | `プロセス改善_課題管理.csv` に転記 | 「自動化候補管理プロセスの改善が必要」 |

---

## 担当ファイル

| ファイル | 操作 |
|---------|------|
| `sessions/automation/YYYYMMDD/00_pre_investigation.md` | 作成・記入（事前調査） |
| `sessions/automation/YYYYMMDD/01_plan.md` | 作成・記入（実施計画・ワーカー割り当て） |
| `sessions/automation/YYYYMMDD/02_dispatch_log.md` | 追記（ディスパッチ履歴） |
| `sessions/automation/YYYYMMDD/03_report.md` | 作成（集約レポート）→ PR として提出 |
| `sessions/automation/YYYYMMDD/04_gate_review.md` | 作成（ゲート判定・知見ルーティング） |
| `sessions/automation/YYYYMMDD/workers/set-N/01_tasks.md` | 作成（ワーカーへのタスク指示） |
| `sessions/automation/YYYYMMDD/workers/set-N/06_eval_report.md` | 読み取りのみ（知見集約の入力） |
| `sessions/automation/YYYYMMDD/workers/set-N/07_issues.md` | 読み取り＋転記済みマーク追記（課題集約） |

---

## やること

- `sessions/automation/YYYYMMDD/` フォルダを作成してセッションを記録する
- 事前調査を完了させてからワーカー割り当てを決定する
- ワーカー＋評価者セットをディスパッチし、結果を集約する
- 各ワーカーセットの知見を `03_report.md` の知見集約セクションに集約する
- 各ワーカーセットの課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
- `04_gate_review.md` にゲート判定を記載する
- `03_report.md` を作成し、レポートに基づくアクションを実施する
- 全タスク完了後、PR を作成してユーザーにレビューを依頼する

## やらないこと

- L1・L2 の成果物（`sessions/initiatives/` 配下）は編集しない（読み取りのみ）
- automation-candidates の変更はレポート集約・アクション実施後のPRレビューでユーザーに確認される
- ワーカーの成果物（`workers/set-N/03_work_log.md`、`04_scan_report.md`）は直接編集しない（読み取りのみ）
- 評価者の成果物（`workers/set-N/05_eval_plan.md`、`06_eval_report.md`）は直接編集しない（読み取りのみ）
- triage セッションの成果物は編集しない
- backlog-maintenance セッションの成果物は編集しない
- metacognition セッションの成果物は編集しない

---

## ルール

- `00_pre_investigation.md` の調査を必ず完了させてから `01_plan.md` を書く
- ゲート判定は `manager-common-policy` §4 に従い、必ず「通過 / 条件付き通過 / 差し戻し」の3択で判定する。判定理由を必ず記載する
- ワーカー成果物が不十分な場合の差し戻しは `manager-common-policy` §7 に従う
- アクション実施を含む全タスク完了後に、PR でユーザーにレビューを依頼する
- PR のタイトルは `automation: YYYYMMDD オートメーションメンテナンスレポート` の形式にする
- **課題フロー**: ワーカー・評価者は `07_issues.md` に起票 → マネージャーが `03_report.md` 作成時に集約 → CSV転記を実施する
- **automation-candidates の変更はユーザー承認後に実施する**: 新規候補登録・ステータス変更・backlog 起票提案はレポートに提案として記載し、PR レビューでユーザーに確認する

---

## PR レビュー時のサマリ提示

PR 作成後、以下のサマリをユーザーに提示する：

```
オートメーションメンテナンス 全タスク完了しました。PR をレビューお願いします。

【分析結果サマリ】
- AT-001 新規候補スキャン: X件検出
- AT-002 既存候補再評価: X件変更提案
- AT-003 実装進捗確認: X件ステータス更新
- AT-004 backlog 起票提案: X件提案

【提案アクション】
- 新規候補登録: X件
- 優先度変更: X件
- ステータス更新: X件
- backlog 起票提案: X件

【PR URL】
[URL]
```

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | 共通パターン（§2〜§8）の参照先。共通ポリシーの変更時に参照箇所を確認 |
| `sessions/automation/_template/00_pre_investigation.md` | 事前調査の走査項目・テンプレート構成 |
| `sessions/automation/_template/01_plan.md` | 実施計画のテンプレート構成 |
| `sessions/automation/_template/03_report.md` | レポートのテンプレート構成（知見集約・課題集約セクション含む） |
| `sessions/automation/_template/04_gate_review.md` | ゲート判定のテンプレート構成 |
| `sessions/automation/_template/workers/_template/07_issues.md` | ワーカーセット別課題バッファのテンプレート |
| `docs/workflow.md` | オートメーションセッションフローの記述（人間向け可視化） |
| `agents/automation-worker.md` | ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/automation-evaluator.md` | 評価基準・レポート構成に影響する変更の場合 |
| `.claude/skills/triage-standard-policy/SKILL.md` | ペアリング要件・ライフサイクル定義の変更が標準ポリシーに影響する場合 |

---

## 頻度

気が向いたとき（ユーザー任意）。ただし前回実施日を `00_pre_investigation.md` に必ず記録する。
