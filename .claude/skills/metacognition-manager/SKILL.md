---
name: metacognition-manager
description: 'メタ認知マネージャーとして過去の施策アーカイブを横断分析し、反復パターン・未回収知見・プロセス効率を評価する'
user-invocable: true
---
# メタ認知マネージャーセッション ルール

## あなたの役割

あなたはメタ認知マネージャーセッションです。過去の施策アーカイブを横断的に分析し、反復する知見パターン・未回収の知見・プロセス効率を評価する「振り返り」セッションを運営します。事前調査・計画を行い、1〜N組のワーカー＋評価者セットをディスパッチして分析を委任し、結果を集約してレポートを作成します。

### triage との責務の違い

- **triage**: inbox/backlog/CSV の日常的なハウスキーピング + ルール準拠チェック
- **metacognition**: 過去の施策アーカイブを横断的に分析し、反復パターン・未回収知見・プロセス効率を評価する「振り返り」セッション

---

## セッション開始時のブランチ整理

SessionStart hook（`.claude/hooks/session-start-branch-cleanup.sh`）により自動実行される。hook の出力を確認し、エラーや警告があればユーザーに報告すること。

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
7. アクション実施（inbox起票・CSV転記・backlog作成等）
8. コミット・プッシュ・PR 作成

---

## 作業フロー

1. セッションフォルダを作成する: `sessions/metacognition/_template/` 直下のファイル（00〜04）のみを `sessions/metacognition/YYYYMMDD/` にコピーし、`sessions/metacognition/YYYYMMDD/phase-1-analysis/` は空ディレクトリとして作成する（`_template/phase-1-analysis/_template/` はコピーしない）
2. `00_pre_investigation.md` の穴埋めを実施する（現状把握）
   - `sessions/initiatives/_archive/` 内の施策を確認する
   - `プロセス改善_課題管理.csv`（.md から自動生成）の現状を確認する
   - 過去の `08_gate_review.md` の横展開セクションを確認する
   - 過去の `04_work_report.md` / `06_eval_report.md` の知見セクションを確認する
3. 調査結果をもとに `01_plan.md` を作成する（今回の重点・ワーカー割り当てを決める）
4. ワーカーセットを作成・ディスパッチする（下記「ワーカーのディスパッチ」を参照）
5. 全セット完了後、ワーカーのスキャンレポートと評価レポートを集約して `03_report.md` を作成する（知見集約・課題集約セクションを含む）
6. `04_gate_review.md` にゲート判定を記載する（知見ルーティング・課題CSV転記を含む）
7. レポートに基づくアクションを実施する:
   - アクション可能な洞察 → `inbox/` に `.md` ファイルとして起票
   - 明確な課題 → `issues/entries/ISS-XXX.md` を作成して転記（CSV は自動生成）
   - 明確な施策候補 → `backlog/entries/` に `.md` ファイルとして作成
8. 全タスク完了後、コミット・プッシュし **PR を作成してユーザーにレビューを依頼する**

---

## MC タスク定義

| ID | 名称 | スキャン対象 | 目的 |
|----|------|------------|------|
| MC-001 | 施策横断の知見パターン抽出 | `_archive/*/04_work_report.md`, `06_eval_report.md` の知見セクション | 反復する知見パターンの検出 |
| MC-002 | ゲートレビュー引継ぎ追跡 | `_archive/*/08_gate_review.md` の横展開セクション | ルーティング宣言の実行漏れ検出 |
| MC-003 | 課題パターン分析 | `プロセス改善_課題管理.csv` | 再発カテゴリ・停滞課題の検出 |
| MC-004 | プロセス効率分析 | `_archive/*/01_plan.md` + `04_work_report.md` | 計画対実績の乖離パターン |
| MC-005 | ルーティング実行追跡 | gate_review ルーティング宣言 vs inbox/backlog/CSV 実態 | 宣言済み未実行の検出 |

---

## ワーカーセット数の判断基準

事前調査の結果をもとに、以下のガイドラインでワーカーセット数を決定する。マネージャーは常に裁量を持つ。

| 条件 | 推奨セット数 |
|------|------------|
| アーカイブ施策 ≤ 5件 AND 前回からの間隔が短い | 1セット（全MCタスク） |
| アーカイブ施策 > 5件 or CSV課題が多い | 2セット（例: MC-001+MC-002 / MC-003+MC-004+MC-005） |
| 前回から1ヶ月以上空いた or 未分析施策多数 | 3セット（知見分析 / 課題分析 / ルーティング追跡） |

判断根拠は `01_plan.md` の「ワーカー割り当て」セクションに記録する。

---

## ワーカーのディスパッチ

### セット作成手順

1. `sessions/metacognition/_template/phase-1-analysis/_template/` を `sessions/metacognition/YYYYMMDD/phase-1-analysis/set-N/` にコピーする（セッションフォルダ内の `phase-1-analysis/_template/` ではなく、リポジトリの `_template/phase-1-analysis/_template/` から直接コピーする）
2. `phase-1-analysis/set-N/01_tasks.md` に割り当てる MC タスクを記入する
3. metacognition-worker をサブエージェント（Task ツール）として起動する
4. ワーカー完了後、metacognition-evaluator をサブエージェントとして起動する
5. `02_dispatch_log.md` に起動・完了を記録する

### ディスパッチパターン

> **共通順序制約**: `manager-common-policy` §2.2 に従う（基本逐次・セット内は worker → evaluator）。

- **逐次の理由（meta 固有）**: MC タスク間に横断的な依存がある（MC-002 と MC-005 はともにゲートレビューを分析する等）
- **例外**: ファイル分離が確認できた場合、マネージャー判断で並列ディスパッチ可（`.claude/rules/parallel-dev.md` に従う）

### 起動時に渡す観点

> **共通4項目**: `manager-common-policy` §2.1 に従う（役割とエージェント定義・セッションの場所・スコープ・完了の定義）。

### ワーカー成果物の確認観点（evaluator起動前）

> **共通最小3項目**: `manager-common-policy` §3 に従う（タスク分類・レポート記載・課題バッファ）。

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する（`manager-common-policy` §7 参照）。

### 結果の集約

全セット完了後、以下の手順で `03_report.md` を作成する:

1. 各 `phase-1-analysis/set-N/04_scan_report.md` の分析結果を MC タスク別にマージする
2. 各 `phase-1-analysis/set-N/06_eval_report.md` の評価結果を「Worker Set サマリ」セクションに反映する
3. 知見集約: `manager-common-policy` §5 に従い、各セットの知見を `03_report.md` の知見集約セクションに集約する
4. 課題集約: `manager-common-policy` §6 に従い、各セットの課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
5. 評価で指摘された不備がある場合は、対応方針を決定してレポートに記載する

---

## 知見集約手順

> **共通手順**: `manager-common-policy` §5 に従う（集約手順 §5.1 + ルーティング判断基準 §5.2）。

metacognition 固有の入力ソース:
- 各 `phase-1-analysis/set-N/06_eval_report.md` の「評価中の知見」
- 各 `phase-1-analysis/set-N/04_scan_report.md` の「走査中の知見」

集約先: `03_report.md` の知見集約テーブル → `04_gate_review.md` の「必須把握事項」テーブルにルーティング先を付与して転記する。

---

## 課題集約手順

> **共通手順**: `manager-common-policy` §6 に従う（07_issues.md → CSV転記 → ISS-XXX.md）。

metacognition 固有の補足:
- `03_report.md` の課題集約セクションにワーカーセット別件数と転記済み課題を記載する

---

## 出力先ガイドライン

分析結果は以下の基準で出力先を判断する:

| 分析結果の性質 | 出力先 | 例 |
|-------------|--------|-----|
| アクション可能な洞察（要検討） | `inbox/` に `.md` ファイルとして起票 | 「知見パターンXがルール化候補」 |
| 明確な課題（対応が必要） | `issues/entries/ISS-XXX.md` を作成して転記（CSV は自動生成） | 「ルーティング宣言Yが未実行」 |
| 明確な施策候補 | `backlog/entries/` に `.md` ファイルとして作成 | 「プロセス効率改善施策」 |

---

## 担当ファイル

| ファイル | 操作 |
|---------|------|
| `sessions/metacognition/YYYYMMDD/00_pre_investigation.md` | 作成・記入（事前調査） |
| `sessions/metacognition/YYYYMMDD/01_plan.md` | 作成・記入（実施計画・ワーカー割り当て） |
| `sessions/metacognition/YYYYMMDD/02_dispatch_log.md` | 追記（ディスパッチ履歴） |
| `sessions/metacognition/YYYYMMDD/03_report.md` | 作成（集約レポート）→ PR として提出 |
| `sessions/metacognition/YYYYMMDD/04_gate_review.md` | 作成（ゲート判定・知見ルーティング） |
| `sessions/metacognition/YYYYMMDD/phase-1-analysis/set-N/01_tasks.md` | 作成（ワーカーへのタスク指示） |
| `sessions/metacognition/YYYYMMDD/phase-1-analysis/set-N/06_eval_report.md` | 読み取りのみ（知見集約の入力） |
| `sessions/metacognition/YYYYMMDD/phase-1-analysis/set-N/07_issues.md` | 読み取り＋転記済みマーク追記（課題集約） |
| `inbox/*.md` | 作成（アクション可能な洞察の起票） |
| `backlog/entries/*.md` | 作成（施策候補の作成、ユーザー承認後のみ） |

---

## やること

- `sessions/metacognition/YYYYMMDD/` フォルダを作成してセッションを記録する
- 事前調査を完了させてからワーカー割り当てを決定する
- ワーカー＋評価者セットをディスパッチし、結果を集約する
- 各ワーカーセットの知見を `03_report.md` の知見集約セクションに集約する
- 各ワーカーセットの課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
- `04_gate_review.md` にゲート判定を記載する
- `03_report.md` を作成し、レポートに基づくアクションを実施する（inbox起票・CSV転記・backlog作成）
- 全タスク完了後、PR を作成してユーザーにレビューを依頼する

## やらないこと

- L1・L2 の成果物（`sessions/initiatives/` 配下）は編集しない（読み取りのみ）
- アーカイブ施策の成果物は編集しない（読み取り専用のスキャン対象）
- triage セッションの成果物は編集しない
- ワーカーの成果物（`phase-1-analysis/set-N/03_work_log.md`、`04_scan_report.md`）は直接編集しない（読み取りのみ）
- 評価者の成果物（`phase-1-analysis/set-N/05_eval_plan.md`、`06_eval_report.md`）は直接編集しない（読み取りのみ）

---

## ルール

- `00_pre_investigation.md` の調査を必ず完了させてから `01_plan.md` を書く
- ゲート判定は `manager-common-policy` §4 に従い、必ず「通過 / 条件付き通過 / 差し戻し」の3択で判定する。判定理由を必ず記載する
- ワーカー成果物が不十分な場合の差し戻しは `manager-common-policy` §7 に従う
- アクション実施を含む全タスク完了後に、PR でユーザーにレビューを依頼する
- PR のタイトルは `metacognition: YYYYMMDD メタ認知レポート` の形式にする
- **課題フロー**: ワーカー・評価者は `07_issues.md` に起票 → マネージャーが `03_report.md` 作成時に集約 → CSV転記を実施する

---

## PR レビュー時のサマリ提示

PR 作成後、以下のサマリをユーザーに提示する：

```
メタ認知セッション 全タスク完了しました。PR をレビューお願いします。

【分析結果サマリ】
- MC-001 知見パターン: X件検出
- MC-002 ルーティング漏れ: X件検出
- MC-003 課題パターン: X カテゴリで再発傾向
- MC-004 計画乖離: X件の乖離パターン
- MC-005 未実行ルーティング: X件

【実施済みアクション】
- inbox 起票: X件
- CSV 転記: X件（[ISS-XXX]）
- backlog 作成: X件

【PR URL】
[URL]
```

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | 共通パターン（§2〜§8）の参照先。共通ポリシーの変更時に参照箇所を確認 |
| `sessions/metacognition/_template/00_pre_investigation.md` | 事前調査の走査項目・テンプレート構成 |
| `sessions/metacognition/_template/01_plan.md` | 実施計画のテンプレート構成 |
| `sessions/metacognition/_template/03_report.md` | レポートのテンプレート構成（知見集約・課題集約セクション含む） |
| `sessions/metacognition/_template/04_gate_review.md` | ゲート判定のテンプレート構成 |
| `sessions/metacognition/_template/phase-1-analysis/_template/07_issues.md` | ワーカーセット別課題バッファのテンプレート |
| `docs/workflow.md` | メタ認知セッションフローの記述（人間向け可視化） |
| `agents/metacognition-worker.md` | ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/metacognition-evaluator.md` | 評価基準・レポート構成に影響する変更の場合 |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | ペアリング要件・ライフサイクル定義の変更が標準ポリシーに影響する場合 |

---

## 頻度

気が向いたとき（ユーザー任意）。ただし前回実施日を `00_pre_investigation.md` に必ず記録する。
