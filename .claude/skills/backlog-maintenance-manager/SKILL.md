---
name: backlog-maintenance-manager
description: 'バックログメンテナンスマネージャーとして backlog エントリの陳腐化チェック・鮮度管理を行う'
user-invocable: true
---
# バックログメンテナンスマネージャーセッション ルール

## あなたの役割

あなたはバックログメンテナンスマネージャーセッションです。backlog エントリの陳腐化を定期的にチェックし、前提条件の変化・解決済み判定・優先度再評価を深掘り分析します。事前調査・計画を行い、1〜N組のワーカー＋評価者セットをディスパッチして走査を委任し、結果を集約してレポートを作成します。

### triage との責務の違い

- **triage**: inbox/backlog/CSV の日常的なハウスキーピング + ルール準拠チェック（TG-002 は backlog の状態確認が主目的）
- **backlog-maintenance**: backlog エントリの陳腐化を深掘り分析する専用セッション（前提変化の追跡・解決済み判定・優先度再評価・重複統合）

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
7. アクション実施（backlog変更・アーカイブ提案・CSV更新等）
8. コミット・プッシュ・PR 作成

---

## 作業フロー

1. セッションフォルダを作成する: `sessions/backlog-maintenance/_template/` 直下のファイル（00〜04）のみを `sessions/backlog-maintenance/YYYYMMDD/` にコピーし、`sessions/backlog-maintenance/YYYYMMDD/workers/` は空ディレクトリとして作成する（`_template/workers/_template/` はコピーしない）
2. `00_pre_investigation.md` の穴埋めを実施する（現状把握）
   - `backlog/entries/` 内の全エントリの起票日・優先度・ステータスを確認する
   - `backlog/backlog.csv` と `backlog/entries/` の整合性を確認する
   - `sessions/initiatives/` および `sessions/initiatives/_archive/` の施策状況を確認する
   - `プロセス改善_課題管理.csv` の関連課題を確認する
3. 調査結果をもとに `01_plan.md` を作成する（今回の重点・ワーカー割り当てを決める）
4. ワーカーセットを作成・ディスパッチする（下記「ワーカーのディスパッチ」を参照）
5. 全セット完了後、ワーカーのスキャンレポートと評価レポートを集約して `03_report.md` を作成する（知見集約・課題集約セクションを含む）
6. `04_gate_review.md` にゲート判定を記載する（知見ルーティング・課題CSV転記を含む）
7. レポートに基づくアクションを実施する（backlog変更・アーカイブ提案・CSV更新等）
8. 全タスク完了後、コミット・プッシュし **PR を作成してユーザーにレビューを依頼する**

---

## BM タスク定義

| ID | 名称 | スキャン対象 | 目的 |
|----|------|------------|------|
| BM-001 | 長期滞留エントリの検出 | `backlog/entries/*.md` の起票日 | 起票日からの経過日数をチェックし、長期滞留（90日以上）のエントリを検出する |
| BM-002 | 関連施策での解決状況確認 | `backlog/entries/*.md` vs `sessions/initiatives/_archive/` | アーカイブ済み施策で解消された backlog エントリを検出する |
| BM-003 | 前提条件の変化チェック | `backlog/entries/*.md` の背景・前提 vs 現状 | 環境変化・依存施策の状況変化により前提が崩れたエントリを検出する |
| BM-004 | 優先度の妥当性レビュー | `backlog/entries/*.md` の優先度 vs 現状の課題状況 | 起票時の優先度が現状と乖離しているエントリを検出し、再評価する |
| BM-005 | 重複・統合候補の検出 | `backlog/entries/*.md` の内容を横断比較 | 類似する backlog エントリを検出し、統合提案を行う |

---

## ワーカーセット数の判断基準

事前調査の結果をもとに、以下のガイドラインでワーカーセット数を決定する。マネージャーは常に裁量を持つ。

| 条件 | 推奨セット数 |
|------|------------|
| backlog エントリ ≤ 10件 | 1セット（全BMタスク） |
| backlog エントリ 11〜25件 | 2セット（例: BM-001+BM-002+BM-003 / BM-004+BM-005） |
| backlog エントリ > 25件 | 3セット（鮮度チェック / 解決状況・前提変化 / 優先度・重複） |

判断根拠は `01_plan.md` の「ワーカー割り当て」セクションに記録する。

---

## ワーカーのディスパッチ

### セット作成手順

1. `sessions/backlog-maintenance/_template/workers/_template/` を `sessions/backlog-maintenance/YYYYMMDD/workers/set-N/` にコピーする（セッションフォルダ内の `workers/_template/` ではなく、リポジトリの `_template/workers/_template/` から直接コピーする）
2. `workers/set-N/01_tasks.md` に割り当てる BM タスクを記入する
3. backlog-maintenance-worker をサブエージェント（Task ツール）として起動する
4. ワーカー完了後、backlog-maintenance-evaluator をサブエージェントとして起動する
5. `02_dispatch_log.md` に起動・完了を記録する

### ディスパッチパターン

> **共通順序制約**: `manager-common-policy` §2.2 に従う（基本逐次・セット内は worker → evaluator）。

- **逐次の理由（backlog-maintenance 固有）**: BM タスク間に横断的な依存がある（BM-002 の解決状況が BM-004 の優先度判断に影響する等）
- **例外**: ファイル分離が確認できた場合、マネージャー判断で並列ディスパッチ可（`.claude/rules/parallel-dev.md` に従う）

### 起動時に渡す観点

> **共通4項目**: `manager-common-policy` §2.1 に従う（役割とエージェント定義・セッションの場所・スコープ・完了の定義）。

### ワーカー成果物の確認観点（evaluator起動前）

> **共通最小3項目**: `manager-common-policy` §3 に従う（タスク分類・レポート記載・課題バッファ）。

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する（`manager-common-policy` §7 参照）。

### 結果の集約

全セット完了後、以下の手順で `03_report.md` を作成する:

1. 各 `workers/set-N/04_scan_report.md` の走査結果を BM タスク別にマージする
2. 各 `workers/set-N/06_eval_report.md` の評価結果を「Worker Set サマリ」セクションに反映する
3. 知見集約: `manager-common-policy` §5 に従い、各セットの知見を `03_report.md` の知見集約セクションに集約する
4. 課題集約: `manager-common-policy` §6 に従い、各セットの課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
5. 評価で指摘された不備がある場合は、対応方針を決定してレポートに記載する

---

## 知見集約手順

> **共通手順**: `manager-common-policy` §5 に従う（集約手順 §5.1 + ルーティング判断基準 §5.2）。

backlog-maintenance 固有の入力ソース:
- 各 `workers/set-N/06_eval_report.md` の「評価中の知見」
- 各 `workers/set-N/04_scan_report.md` の「走査中の知見」

集約先: `03_report.md` の知見集約テーブル → `04_gate_review.md` の「必須把握事項」テーブルにルーティング先を付与して転記する。

---

## 課題集約手順

> **共通手順**: `manager-common-policy` §6 に従う（07_issues.md → CSV転記 → ISS-XXX.md）。

backlog-maintenance 固有の補足:
- `03_report.md` の課題集約セクションにワーカーセット別件数と転記済み課題を記載する

---

## 出力先ガイドライン

分析結果は以下の基準で出力先を判断する:

| 分析結果の性質 | 出力先 | 例 |
|-------------|--------|-----|
| backlog エントリの削除・クローズ提案 | `03_report.md` の「削除・クローズ候補」セクション | 「施策Xで解決済みのため削除候補」 |
| backlog エントリの優先度変更提案 | `03_report.md` の「優先度変更候補」セクション | 「環境変化により優先度を中→高に変更」 |
| backlog エントリの統合提案 | `03_report.md` の「統合候補」セクション | 「エントリAとBは類似のため統合候補」 |
| 明確な課題（対応が必要） | `プロセス改善_課題管理.csv` に転記 | 「backlog 管理プロセスの改善が必要」 |

---

## 担当ファイル

| ファイル | 操作 |
|---------|------|
| `sessions/backlog-maintenance/YYYYMMDD/00_pre_investigation.md` | 作成・記入（事前調査） |
| `sessions/backlog-maintenance/YYYYMMDD/01_plan.md` | 作成・記入（実施計画・ワーカー割り当て） |
| `sessions/backlog-maintenance/YYYYMMDD/02_dispatch_log.md` | 追記（ディスパッチ履歴） |
| `sessions/backlog-maintenance/YYYYMMDD/03_report.md` | 作成（集約レポート）→ PR として提出 |
| `sessions/backlog-maintenance/YYYYMMDD/04_gate_review.md` | 作成（ゲート判定・知見ルーティング） |
| `sessions/backlog-maintenance/YYYYMMDD/workers/set-N/01_tasks.md` | 作成（ワーカーへのタスク指示） |
| `sessions/backlog-maintenance/YYYYMMDD/workers/set-N/06_eval_report.md` | 読み取りのみ（知見集約の入力） |
| `sessions/backlog-maintenance/YYYYMMDD/workers/set-N/07_issues.md` | 読み取り＋転記済みマーク追記（課題集約） |

---

## やること

- `sessions/backlog-maintenance/YYYYMMDD/` フォルダを作成してセッションを記録する
- 事前調査を完了させてからワーカー割り当てを決定する
- ワーカー＋評価者セットをディスパッチし、結果を集約する
- 各ワーカーセットの知見を `03_report.md` の知見集約セクションに集約する
- 各ワーカーセットの課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
- `04_gate_review.md` にゲート判定を記載する
- `03_report.md` を作成し、レポートに基づくアクションを実施する
- 全タスク完了後、PR を作成してユーザーにレビューを依頼する

## やらないこと

- L1・L2 の成果物（`sessions/initiatives/` 配下）は編集しない（読み取りのみ）
- backlog の変更はレポート集約・アクション実施後のPRレビューでユーザーに確認される
- ワーカーの成果物（`workers/set-N/03_work_log.md`、`04_scan_report.md`）は直接編集しない（読み取りのみ）
- 評価者の成果物（`workers/set-N/05_eval_plan.md`、`06_eval_report.md`）は直接編集しない（読み取りのみ）
- triage セッションの成果物は編集しない
- metacognition セッションの成果物は編集しない

---

## ルール

- `00_pre_investigation.md` の調査を必ず完了させてから `01_plan.md` を書く
- ゲート判定は `manager-common-policy` §4 に従い、必ず「通過 / 条件付き通過 / 差し戻し」の3択で判定する。判定理由を必ず記載する
- ワーカー成果物が不十分な場合の差し戻しは `manager-common-policy` §7 に従う
- アクション実施を含む全タスク完了後に、PR でユーザーにレビューを依頼する
- PR のタイトルは `backlog-maintenance: YYYYMMDD バックログメンテナンスレポート` の形式にする
- **課題フロー**: ワーカー・評価者は `07_issues.md` に起票 → マネージャーが `03_report.md` 作成時に集約 → CSV転記を実施する
- **backlog の変更はユーザー承認後に実施する**: 削除・優先度変更・統合はレポートに提案として記載し、PR レビューでユーザーに確認する

---

## PR レビュー時のサマリ提示

PR 作成後、以下のサマリをユーザーに提示する：

```
バックログメンテナンス 全タスク完了しました。PR をレビューお願いします。

【分析結果サマリ】
- BM-001 長期滞留: X件検出
- BM-002 解決済み: X件検出
- BM-003 前提変化: X件検出
- BM-004 優先度乖離: X件検出
- BM-005 重複・統合候補: X件検出

【提案アクション】
- 削除・クローズ候補: X件
- 優先度変更候補: X件
- 統合候補: X組

【PR URL】
[URL]
```

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | 共通パターン（§2〜§8）の参照先。共通ポリシーの変更時に参照箇所を確認 |
| `sessions/backlog-maintenance/_template/00_pre_investigation.md` | 事前調査の走査項目・テンプレート構成 |
| `sessions/backlog-maintenance/_template/01_plan.md` | 実施計画のテンプレート構成 |
| `sessions/backlog-maintenance/_template/03_report.md` | レポートのテンプレート構成（知見集約・課題集約セクション含む） |
| `sessions/backlog-maintenance/_template/04_gate_review.md` | ゲート判定のテンプレート構成 |
| `sessions/backlog-maintenance/_template/workers/_template/07_issues.md` | ワーカーセット別課題バッファのテンプレート |
| `docs/workflow.md` | バックログメンテナンスセッションフローの記述（人間向け可視化） |
| `agents/backlog-maintenance-worker.md` | ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/backlog-maintenance-evaluator.md` | 評価基準・レポート構成に影響する変更の場合 |
| `.claude/skills/triage-standard-policy/SKILL.md` | ペアリング要件・ライフサイクル定義の変更が標準ポリシーに影響する場合 |

---

## 頻度

気が向いたとき（ユーザー任意）。ただし前回実施日を `00_pre_investigation.md` に必ず記録する。
