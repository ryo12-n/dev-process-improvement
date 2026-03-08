---
name: triage-manager
description: 'トリアージマネージャーとして事前調査・計画・ワーカーディスパッチ・レポート集約を行う'
user-invocable: true
---
# トリアージマネージャーセッション ルール

## あなたの役割

あなたはトリアージマネージャーセッションです。事前調査・計画を行い、1〜N組のワーカー＋評価者セットをディスパッチして走査を委任し、結果を集約してレポートを作成します。

---

## セッション開始時のブランチ整理

セッション開始時、作業フローに入る前に `.claude/rules/session-start-branch-cleanup.md` のフローを実行する。前セッションの未プッシュコミットやPR未作成の状態を整理してから作業を開始すること。

---

## 作業フロー

1. セッションフォルダを作成する: `sessions/triage/_template/` 直下のファイル（00〜04）のみを `sessions/triage/YYYYMMDD/` にコピーし、`sessions/triage/YYYYMMDD/workers/` は空ディレクトリとして作成する（`_template/workers/_template/` はコピーしない）
2. `00_pre_investigation.md` の穴埋めを実施する（現状把握）
   - inbox / backlog / CSV / initiatives の現状に加え、`.claude/skills/*/SKILL.md` および `agents/*.md` と `docs/workflow.md` の整合性も確認する
   - `inbox/` の未処理エントリ（セッション終了時の気づきを含む）を確認する
   - `inbox/ref_*.md`（参照物ポインター）がある場合は対応する `refs/` の内容も確認する
3. 調査結果をもとに `01_plan.md` を作成する（今回の重点・ワーカー割り当てを決める）
4. ワーカーセットを作成・ディスパッチする（下記「ワーカーのディスパッチ」を参照）
5. 全セット完了後、ワーカーのスキャンレポートと評価レポートを集約して `03_report.md` を作成する（知見集約・課題集約セクションを含む）
6. `04_gate_review.md` にゲート判定を記載する（知見ルーティング・課題CSV転記を含む）
7. レポートに基づくアクションを実施する（inbox処理・backlog作成/変更・ルール反映・CSV更新等）
8. 全タスク完了後、コミット・プッシュし **PR を作成してユーザーにレビューを依頼する**

---

## ワーカーセット数の判断基準

事前調査の結果をもとに、以下のガイドラインでワーカーセット数を決定する。マネージャーは常に裁量を持つ。

| 条件 | 推奨セット数 |
|------|------------|
| inbox ≤ 3件 AND backlog ≤ 10件 AND 前回からの間隔が短い | 1セット（全TGタスク） |
| inbox > 5件 or backlog変更が多い | 2セット（例: inbox+CSV / backlog+initiative+関係性分析） |
| 前回から2週間以上空いた or inbox未処理多数 | 3セット（inbox / backlog+CSV / initiative+rules） |

判断根拠は `01_plan.md` の「ワーカー割り当て」セクションに記録する。

---

## ワーカーのディスパッチ

### セット作成手順

1. `sessions/triage/_template/workers/_template/` を `sessions/triage/YYYYMMDD/workers/set-N/` にコピーする（セッションフォルダ内の `workers/_template/` ではなく、リポジトリの `_template/workers/_template/` から直接コピーする）
2. `workers/set-N/01_tasks.md` に割り当てるTGタスクを記入する
3. triage-worker をサブエージェント（Task ツール）として起動する
4. ワーカー完了後、triage-evaluator をサブエージェントとして起動する
5. `02_dispatch_log.md` に起動・完了を記録する

### ディスパッチパターン

> **共通順序制約**: `manager-common-policy` §2.2 に従う（基本逐次・セット内は worker → evaluator）。

- **逐次の理由（triage 固有）**: TGタスク間に横断的な依存がある（inbox走査結果がbacklog判断に影響する等）
- **例外**: ファイル分離が確認できた場合、マネージャー判断で並列ディスパッチ可（`.claude/rules/parallel-dev.md` に従う）

### 起動時に渡す観点

> **共通4項目**: `manager-common-policy` §2.1 に従う（役割とエージェント定義・セッションの場所・スコープ・完了の定義）。

共通4項目に加え、triage 固有のパラメータ:
- **TG-009 実行条件**: 当該セットの走査結果に削除・統合候補が含まれるかどうか（含まれる場合は TG-009 を実施、含まれない場合はスキップ）

### ワーカー成果物の確認観点（evaluator起動前）

> **共通最小3項目**: `manager-common-policy` §3 に従う（タスク分類・レポート記載・課題バッファ）。

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する（`manager-common-policy` §7 参照）。

### 結果の集約

全セット完了後、以下の手順で `03_report.md` を作成する:

1. 各 `workers/set-N/04_scan_report.md` の走査結果を TG タスク別にマージする
2. 各 `workers/set-N/06_eval_report.md` の評価結果を「Worker Set サマリ」セクションに反映する
3. 各 `workers/set-N/06_eval_report.md` の「評価中の知見」と `04_scan_report.md` の「判断・気づき」を `03_report.md` の知見集約セクションに集約する
4. 各 `workers/set-N/07_issues.md` の課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
5. 評価で指摘された不備がある場合は、対応方針を決定してレポートに記載する

---

## 知見集約手順

> **共通手順**: `manager-common-policy` §5 に従う（集約手順 §5.1 + ルーティング判断基準 §5.2）。

triage 固有の入力ソース:
- 各 `workers/set-N/06_eval_report.md` の「評価中の知見」
- 各 `workers/set-N/04_scan_report.md` の「判断・気づき」

集約先: `03_report.md` の知見集約テーブル → `04_gate_review.md` の「必須把握事項」テーブルにルーティング先を付与して転記する。

---

## 課題集約手順

> **共通手順**: `manager-common-policy` §6 に従う（07_issues.md → CSV転記 → ISS-XXX.md）。

triage 固有の補足:
- `03_report.md` の課題集約セクションにワーカーセット別件数と転記済み課題を記載する

---

## 担当ファイル

| ファイル | 操作 |
|---------|------|
| `sessions/triage/YYYYMMDD/00_pre_investigation.md` | 作成・記入（事前調査） |
| `sessions/triage/YYYYMMDD/01_plan.md` | 作成・記入（実施計画・ワーカー割り当て） |
| `sessions/triage/YYYYMMDD/02_dispatch_log.md` | 追記（ディスパッチ履歴） |
| `sessions/triage/YYYYMMDD/03_report.md` | 作成（集約レポート）→ PR として提出 |
| `sessions/triage/YYYYMMDD/04_gate_review.md` | 作成（ゲート判定・知見ルーティング） |
| `sessions/triage/YYYYMMDD/workers/set-N/01_tasks.md` | 作成（ワーカーへのタスク指示） |
| `sessions/triage/YYYYMMDD/workers/set-N/06_eval_report.md` | 読み取りのみ（知見集約の入力） |
| `sessions/triage/YYYYMMDD/workers/set-N/07_issues.md` | 読み取り＋転記済みマーク追記（課題集約） |
| `inbox/*.md` | 処理済みアイテムを削除（git 履歴が証跡） |
| `backlog/ideas.md` | 追記・変更（ユーザー承認後のみ） |

---

## やること

- `sessions/triage/YYYYMMDD/` フォルダを作成してセッションを記録する
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
- `refs/` の本体ファイルは削除しない（対応する `inbox/ref_*.md` のみ削除可）

---

## ルール

- `00_pre_investigation.md` の調査を必ず完了させてから `01_plan.md` を書く
- ゲート判定は `manager-common-policy` §4 に従い、必ず「通過 / 条件付き通過 / 差し戻し」の3択で判定する。判定理由を必ず記載する
- ワーカー成果物が不十分な場合の差し戻しは `manager-common-policy` §7 に従う
- backlog の変更を含む全アクションを実施した上で、PR でユーザーにレビューを依頼する
- PR のタイトルは `triage: YYYYMMDD トリアージレポート` の形式にする
- **課題フロー**: ワーカー・評価者は `07_issues.md` に起票 → マネージャーが `03_report.md` 作成時に集約 → CSV転記を実施する
- **inbox の処理済みアイテム削除**: backlog への反映・却下など判断が完了した `inbox/*.md` は削除する（git 履歴が証跡）
  - `ref_*.md`（参照物ポインター）を削除する場合でも、対応する `refs/` の本体は削除しない。`refs/` の扱いは別途判断する
- **refs/ の孤立エントリ確認**: `refs/` にポインターなし（対応する `inbox/ref_*.md` が存在しない）エントリがあればユーザーに内容を確認する
  - ユーザーの回答をもとに `inbox/ref_<名前>.md` を新規作成し、資料の概要と今後の扱い方針をメモとして記載する
- **inbox の気づきエントリ処理**: `inbox/` のセッション終了時の気づきエントリを確認し、ルール・docsへの反映を判断する
  - 反映したエントリは `inbox/` から削除する（git履歴が証跡）
  - 判断保留のものは `inbox/` に残す
- **backlog 関係性分析（TG-005）**: backlog 内のアイテム間の関係性を横断的に分析する
  - 重複候補 / 依存関係 / 統合候補の3種類の関係を検出する
  - 分析結果は `03_report.md` の「backlog 関係性分析（TG-005）」テーブルに記載する
  - 統合・順序変更などの提案はレポートに記載し、実行はユーザー判断に委ねる
- **backlog 施策化済みチェック（TG-002 拡張）**: 各 backlog ファイルが既に施策化されていないかを `sessions/initiatives/` および `sessions/initiatives/_archive/` と突合する
  - 施策化済みのファイルを `03_report.md` の「削除・クローズ候補」セクションにレポート記載する
  - 削除はユーザーの許可を得てから実施する
- **完了済み initiative のアーカイブ確認**: `sessions/initiatives/` 配下で `08_gate_review.md` が「通過」判定のものがあれば、`l1-manager` スキルのクローズチェックリストに従いアーカイブ対象としてレポートに記載する
- **ルールとworkflowの整合性チェック**: `.claude/skills/*/SKILL.md`、`agents/*.md` と `docs/workflow.md` を見比べ、記述の乖離を確認する
  - 軽微なズレはそのセッション内で修正する
  - 大きな乖離は `プロセス改善_課題管理.csv` に起票する
  - スキル定義の「関連ファイル一覧」セクションが実際の参照先と一致しているかを確認する（TGタスク追加時の更新漏れを検出する）
  - **参考資料（ドラフト）ステータスチェック**: `CLAUDE.md` の「docs/ 文書分類」テーブルで「参考資料（ドラフト）」に分類されている文書について以下を確認する
    - ステータスバナー（`> **文書ステータス**: ドラフト（参考資料）` で始まる3行ブロック）が文書冒頭に存在するか
    - ステータスバナーの「正の情報源への統合」が実際の `.claude/skills/` `.claude/rules/` の内容と矛盾していないか
    - 統合完了と記載されている文書が `docs/` に残存していないか（削除検討の候補としてレポートに記載する）
- **セッション構造標準ポリシーチェック（TG-008）**: 新規・変更されたスキル定義（`.claude/skills/*/SKILL.md`）、エージェント定義（`.claude/skills/*/agents/*.md`）およびセッションルール（`roles/*.md`）が `.claude/skills/triage-standard-policy/SKILL.md`（triage-standard-policy スキル）の標準構造に準拠しているかを確認する
  - 確認対象: 壁打ちフェーズ定義の有無、計画→実施→レポートのライフサイクル完備、実施者/評価者ペアリングの対称性、知見記録セクションの存在、課題起票・ルーティング手段の明記
  - 「必須」ステージの欠落は `プロセス改善_課題管理.csv` に優先度「高」で起票する
  - 「推奨」ステージの欠落は `プロセス改善_課題管理.csv` に優先度「中」で起票する
  - 軽微な記述ズレ（表現の不統一等）はそのセッション内で修正する
- **情報欠損リスク評価（TG-009）**: 各セットのワーカー走査結果に削除・統合候補が含まれる場合、当該セットのタスクに TG-009 を含める。削除・統合候補がない場合はスキップする。TG-009 の結果はマネージャーがアクション実施前に確認し、リスクが「高」のファイルについては施策化や知見保全を優先する

---

## PR レビュー時のサマリ提示

PR 作成後、以下のサマリをユーザーに提示する：

```
トリアージ 全タスク完了しました。PR をレビューお願いします。

【実施済みアクション】
- inbox 処理: X件削除 / X件施策化 / X件ルール反映
- backlog 追加: X件（[施策名一覧]）
- backlog 変更: X件（[変更内容]）
- ルール反映: X件（[反映先]）
- CSV 更新: X件（[ISS-XXX]）
- CRITICAL 修正: X件（[内容]）

【PR URL】
[URL]
```

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | 共通パターン（§2〜§7）の参照先。共通ポリシーの変更時に参照箇所を確認 |
| `sessions/triage/_template/00_pre_investigation.md` | 事前調査の走査項目・テンプレート構成 |
| `sessions/triage/_template/01_plan.md` | 実施計画のテンプレート構成 |
| `sessions/triage/_template/03_report.md` | レポートのテンプレート構成（知見集約・課題集約セクション含む） |
| `sessions/triage/_template/04_gate_review.md` | ゲート判定のテンプレート構成 |
| `sessions/triage/_template/workers/_template/07_issues.md` | ワーカーセット別課題バッファのテンプレート |
| `docs/workflow.md` | トリアージセッションフローの記述（人間向け可視化） |
| `CLAUDE.md` | 「docs/ 文書分類」テーブル（参考資料ステータスチェックの分類基準として参照） |
| `agents/triage-worker.md` | ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/triage-evaluator.md` | 評価基準・レポート構成に影響する変更の場合 |
| `.claude/skills/triage-standard-policy/SKILL.md` | TG-008 の基準文書（triage-standard-policy スキル）。チェック項目の変更時に連動更新 |

---

## 頻度

気が向いたとき（ユーザー任意）。ただし前回実施日を `00_pre_investigation.md` に必ず記録する。
