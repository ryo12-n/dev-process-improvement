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
7. アクション実施（inbox処理・backlog変更・ルール反映・CSV更新等）
8. コミット・プッシュ・PR 作成

---

## 作業フロー

1. セッションフォルダを作成する: `sessions/triage/_template/` 直下のファイル（00〜04）のみを `sessions/triage/YYYYMMDD/` にコピーし、`sessions/triage/YYYYMMDD/phase-1-scan/` は空ディレクトリとして作成する（`_template/phase-1-scan/_template/` はコピーしない）
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

## フェーズゲート構造

TG タスクはフェーズ間の依存関係に基づき、以下の5フェーズで段階的にディスパッチする。各フェーズ内のタスクは独立しており並列ディスパッチ可能だが、フェーズ間はゲートで区切る。

### フェーズ定義

| フェーズ | タスク | 並列性 | ゲート条件 |
|---------|--------|--------|-----------|
| Phase 1: 状態収集 | TG-001, TG-003, TG-004, TG-007 | 4タスク独立 → 最大2セット並列 | 全タスクの scan_report セクション完成 |
| Phase 2a: 突合・整合性 | TG-002, TG-006, TG-008（条件付き） | 3タスク独立 → 最大2セット並列 | TG-002 の削除/統合候補リスト確定 |
| Phase 2b: 関係性分析 | TG-005 | TG-002 に依存 | 関係性テーブル完成、統合/削除候補の有無確定 |
| Phase 2c: リスク評価 | TG-009（条件付き） | TG-002 + TG-005 に依存 | 全候補のリスク評価完了（候補なしならスキップ） |
| Phase 3: GHA整合性 | TG-010 | 独立 | 全マッピングのチェック完了、ドリフト重大度判定済み |

### フェーズゲートの方式

フェーズゲートは **軽量インラインゲート** で実施する。マネージャーのディスパッチロジック内で完結し、フェーズごとの `gate_review.md` は作成しない。

1. マネージャーが Phase N のワーカーセットをディスパッチする
2. ワーカー + 評価者が完了する
3. マネージャーが scan_report を確認し、ゲート条件を判定する
4. ゲート通過 → Phase N+1 をディスパッチ（必要な出力を次フェーズのコンテキストとして渡す）
5. ゲート不通過 → `02_dispatch_log.md` に理由を記録し、再ディスパッチまたは下流フェーズのスキップを判断する

### 後方互換: 低ボリューム時の逐次実行

走査ボリューム ≤ 20件の場合、全フェーズを1セットで逐次実行してよい。フェーズ構造は論理的に維持する（TG-005 は TG-002 の後に実行する等）が、物理的なセット分割は不要。

---

## ワーカーセット数の判断基準

事前調査の結果をもとに、以下の手順でワーカーセット数を決定する。マネージャーは常に裁量を持つ。

### ステップ1: 走査ボリュームの見積もり

以下の合計を「走査ボリューム」として算出する（`00_pre_investigation.md` に記録）：
- inbox 分類対象件数（`ref_*` ポインターの確認のみは除く）
- backlog 突合・分析対象件数
- CSV 確認対象件数（ステータス「起票」等）

### ステップ2: セット数の決定

セット数は **フェーズ単位** で割り当てる。各フェーズ内で最大2セットを使用可能。

| 走査ボリューム | 推奨方式 | 備考 |
|-------------|---------|------|
| ≤ 20件 | 全フェーズ1セット逐次実行 | 前回からの間隔が短い場合は TG-008 等のスキップも検討 |
| 21〜50件 | フェーズ別にセット分割 | Phase 1 で2セット（重量タスク TG-001 を分離）等 |
| 51件以上 | フェーズ別に最大2セット | 各フェーズ内でタスクドメイン別に分散 |

### セット割り当てのガイドライン

- **1セットあたり TG タスク 3件以下** を目安とする
- 単一 TG タスクの対象が15件以上の場合、そのタスクだけで1セット分の負荷と見なす
- **間隔はスコープ（実施する TG タスクの選定）に影響するが、セット数の上書き理由にはしない** — 短い間隔は TG-008 スキップ等で走査タスク自体を減らす根拠にはなるが、残ったタスクのボリュームが多い場合は複数セットに分割する
- **フェーズ間の依存を尊重する**: Phase 2b (TG-005) は Phase 2a (TG-002) 完了後にディスパッチする。Phase 2c (TG-009) は Phase 2b 完了後にディスパッチする

判断根拠は `01_plan.md` の「ワーカー割り当て」セクションに記録する。

---

## ワーカーのディスパッチ

### セット作成手順

1. `sessions/triage/_template/phase-1-scan/_template/` を `sessions/triage/YYYYMMDD/phase-1-scan/set-N/` にコピーする（セッションフォルダ内の `phase-1-scan/_template/` ではなく、リポジトリの `_template/phase-1-scan/_template/` から直接コピーする）
2. `phase-1-scan/set-N/01_tasks.md` に割り当てるTGタスクを記入する
3. triage-worker をサブエージェント（Task ツール）として起動する
4. ワーカー完了後、triage-evaluator をサブエージェントとして起動する
5. `02_dispatch_log.md` に起動・完了を記録する

### ディスパッチパターン

> **共通順序制約**: `manager-common-policy` §2.2 に従う（基本逐次・セット内は worker → evaluator）。

- **フェーズ間は逐次**: フェーズゲート構造に従い、Phase N 完了後に Phase N+1 をディスパッチする
- **フェーズ内は並列可**: 同一フェーズ内のタスクはファイル分離が確認できるため、マネージャー判断で並列ディスパッチ可（`.claude/rules/parallel-dev.md` に従う）
- **低ボリューム時の例外**: 走査ボリューム ≤ 20件の場合、全フェーズを1セットで逐次実行可（フェーズ内のタスク順序はフェーズ定義に従う）

### 起動時に渡す観点

> **共通4項目**: `manager-common-policy` §2.1 に従う（役割とエージェント定義・セッションの場所・スコープ・完了の定義）。

共通4項目に加え、triage 固有のパラメータ:
- **TG-009 実行条件**: 当該セットの走査結果に削除・統合候補が含まれるかどうか（含まれる場合は TG-009 を実施、含まれない場合はスキップ）

### ワーカー成果物の確認観点（evaluator起動前）

> **共通最小3項目**: `manager-common-policy` §3 に従う（タスク分類・レポート記載・課題バッファ）。

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する（`manager-common-policy` §7 参照）。

### 結果の集約

全セット完了後、以下の手順で `03_report.md` を作成する:

1. 各 `phase-1-scan/set-N/04_scan_report.md` の走査結果を TG タスク別にマージする
2. 各 `phase-1-scan/set-N/06_eval_report.md` の評価結果を「Worker Set サマリ」セクションに反映する
3. 各 `phase-1-scan/set-N/06_eval_report.md` の「評価中の知見」と `04_scan_report.md` の「判断・気づき」を `03_report.md` の知見集約セクションに集約する
4. 各 `phase-1-scan/set-N/07_issues.md` の課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
5. 評価で指摘された不備がある場合は、対応方針を決定してレポートに記載する

---

## 知見集約手順

> **共通手順**: `manager-common-policy` §5 に従う（集約手順 §5.1 + ルーティング判断基準 §5.2）。

triage 固有の入力ソース:
- 各 `phase-1-scan/set-N/06_eval_report.md` の「評価中の知見」
- 各 `phase-1-scan/set-N/04_scan_report.md` の「判断・気づき」

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
| `sessions/triage/YYYYMMDD/phase-1-scan/set-N/01_tasks.md` | 作成（ワーカーへのタスク指示） |
| `sessions/triage/YYYYMMDD/phase-1-scan/set-N/06_eval_report.md` | 読み取りのみ（知見集約の入力） |
| `sessions/triage/YYYYMMDD/phase-1-scan/set-N/07_issues.md` | 読み取り＋転記済みマーク追記（課題集約） |
| `inbox/*.md` | 処理済みアイテムを削除（git 履歴が証跡） |

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
- ワーカーの成果物（`phase-1-scan/set-N/03_work_log.md`、`04_scan_report.md`）は直接編集しない（読み取りのみ）
- 評価者の成果物（`phase-1-scan/set-N/05_eval_plan.md`、`06_eval_report.md`）は直接編集しない（読み取りのみ）
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
- **backlog 施策化済みチェック（TG-002 拡張）**: 各 backlog エントリが既に施策化されていないかを `sessions/initiatives/` および `sessions/initiatives/_archive/` と突合する。以下の手順で実施する:
  1. `backlog/backlog.csv` の「施策ディレクトリ名」列が記入されているエントリは、その値で `sessions/initiatives/` および `_archive/` を直接照合する
  2. 「施策ディレクトリ名」列が空欄のエントリは、`backlog/entries/<ファイル名>` と `sessions/initiatives/` 配下のディレクトリ名・各施策の `00_proposal.md` の「backlog元ファイル」フィールドで照合する（フォールバック）
  3. 上記で一致が見つかった場合、施策化済みと判定する
  4. 施策化済みのファイルを `03_report.md` の「削除・クローズ候補」セクションにレポート記載する
  5. `backlog/entries/*.md` のステータスが「完了」でないものを「未クローズエントリ」として検出・レポートする（CSV は .md から自動生成）
  - **対象リポジトリ未記入チェック**: `backlog/entries/` の各ファイルおよび `backlog.csv` で「対象リポジトリ」が未記入のエントリを検出し、レポートに記載する
  - 削除はユーザーの許可を得てから実施する
- **完了済み initiative のアーカイブ確認**: `sessions/initiatives/` 配下で `08_gate_review.md` が「通過」判定のものがあれば、`l1-manager` スキルのクローズチェックリストに従いアーカイブ対象としてレポートに記載する
- **ルールとworkflowの整合性チェック**: `.claude/skills/*/SKILL.md`、`agents/*.md` と `docs/workflow.md` を見比べ、記述の乖離を確認する
  - 軽微なズレはそのセッション内で修正する
  - 大きな乖離は `issues/entries/ISS-XXX.md` を作成して起票する（CSV は自動生成）
  - スキル定義の「関連ファイル一覧」セクションが実際の参照先と一致しているかを確認する（TGタスク追加時の更新漏れを検出する）
  - **参考資料（ドラフト）ステータスチェック**: `CLAUDE.md` の「docs/ 文書分類」テーブルで「参考資料（ドラフト）」に分類されている文書について以下を確認する
    - ステータスバナー（`> **文書ステータス**: ドラフト（参考資料）` で始まる3行ブロック）が文書冒頭に存在するか
    - ステータスバナーの「正の情報源への統合」が実際の `.claude/skills/` `.claude/rules/` の内容と矛盾していないか
    - 統合完了と記載されている文書が `docs/` に残存していないか（削除検討の候補としてレポートに記載する）
  - **README 整合性チェック（SDK / CLI 共通）**: `README.md` の以下の4セクションが実態と一致しているかを確認する
    - ディレクトリ構成図: `.claude/rules/`、`.claude/skills/`（起動型のみ）、`sessions/`、`backlog/`、`issues/` の各エントリが実ファイル・ディレクトリと一致しているか
    - セッション種別テーブル: 起動型スキルが全て記載されているか
    - AI 向けスキル定義テーブル: 起動型スキルとその agents が全て記載されているか
    - ドキュメントマップ: リンク先が実在するファイルを指しているか
    - 乖離発見時のアクション: 軽微なズレはそのセッション内で修正する。大きな乖離は `issues/entries/ISS-XXX.md` を作成して起票する（CSV は自動生成）
- **セッション構造標準ポリシーチェック（TG-008）**: 新規・変更されたスキル定義（`.claude/skills/*/SKILL.md`）、エージェント定義（`.claude/skills/*/agents/*.md`）およびセッションルール（`roles/*.md`）が `session-lifecycle-policy`（§1: ライフサイクルパターン、§2: ペアリング要件）の標準構造に準拠しているかを確認する（チェックリストは本ファイルの「TG-008 チェックリスト」セクションを参照）
  - 確認対象: 壁打ちフェーズ定義の有無、計画→実施→レポートのライフサイクル完備、実施者/評価者ペアリングの対称性、知見記録セクションの存在、課題起票・ルーティング手段の明記
  - 「必須」ステージの欠落は `issues/entries/ISS-XXX.md` を作成して起票する（優先度: 高、CSV は自動生成）
  - 「推奨」ステージの欠落は `issues/entries/ISS-XXX.md` を作成して起票する（優先度: 中、CSV は自動生成）
  - 軽微な記述ズレ（表現の不統一等）はそのセッション内で修正する
- **情報欠損リスク評価（TG-009）**: 各セットのワーカー走査結果に削除・統合候補が含まれる場合、当該セットのタスクに TG-009 を含める。削除・統合候補がない場合はスキップする。TG-009 の結果はマネージャーがアクション実施前に確認し、リスクが「高」のファイルについては施策化や知見保全を優先する
- **GHA ↔ Skills 整合性チェック（TG-010）**: `.github/gha-skills-mapping.yml` のマッピングマニフェストに基づき、GHA プロンプト/ワークフローとスキル定義の間のドリフトを検出する
  - マニフェスト内の各マッピングについて、チェックポイント（task_ids, workflow_steps, report_sections, file_templates, file_numbers）を突合する
  - inherent_differences（期待される差異）が実際にまだ有効かを検証する
  - ドリフト重大度: CRITICAL（Skill にあるが GHA にないタスクID等、機能欠落の可能性）/ WARNING（ワークフローステップ・レポート構造の不一致）/ INFO（軽微な差異、inherent_differences の確認結果）
  - CRITICAL ドリフトは `issues/entries/ISS-XXX.md` を作成して起票する（CSV は自動生成）。WARNING は `03_report.md` に記載しアクション方針を決定する
  - マニフェストファイルが存在しない場合は `07_issues.md` に起票し、TG-010 をスキップする

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

## TG-008 チェックリスト（セッション構造標準ポリシー準拠）

> TG-008 の基準チェックリスト。ライフサイクルパターン・ペアリング要件の定義は `session-lifecycle-policy` を参照。

### 走査対象

- `.claude/skills/l1-manager/SKILL.md`
- `.claude/skills/l1-manager/agents/l2-worker.md`
- `.claude/skills/l1-manager/agents/l2-evaluator.md`
- `.claude/skills/triage-manager/SKILL.md`
- `.claude/skills/triage-manager/agents/triage-worker.md`
- `.claude/skills/triage-manager/agents/triage-evaluator.md`
- `.claude/skills/metacognition-manager/SKILL.md`
- `.claude/skills/metacognition-manager/agents/metacognition-worker.md`
- `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md`
- `.claude/skills/sync-manager/SKILL.md`
- `.claude/skills/sync-manager/agents/sync-worker.md`
- `.claude/skills/sync-manager/agents/sync-evaluator.md`
- `.claude/skills/backlog-maintenance-manager/SKILL.md`
- `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md`
- `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md`
- `.claude/skills/automation-manager/SKILL.md`
- `.claude/skills/automation-manager/agents/automation-worker.md`
- `.claude/skills/automation-manager/agents/automation-evaluator.md`
- `.claude/skills/l1-impl-manager/SKILL.md`
- `.claude/skills/l1-impl-manager/agents/investigation-worker.md`
- `.claude/skills/l1-impl-manager/agents/design-worker.md`
- `.claude/skills/l1-impl-manager/agents/impl-plan-worker.md`
- `.claude/skills/l1-impl-manager/agents/impl-worker.md`
- `.claude/skills/l1-impl-manager/agents/impl-evaluator.md`
- `.claude/skills/config-optimizer-manager/SKILL.md`
- `.claude/skills/config-optimizer-manager/agents/config-collection-worker.md`
- `.claude/skills/config-optimizer-manager/agents/config-analysis-worker.md`
- `.claude/skills/config-optimizer-manager/agents/config-proposal-worker.md`
- `.claude/skills/config-optimizer-manager/agents/config-optimizer-evaluator.md`
- `.claude/skills/session-consistency-manager/SKILL.md`
- `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md`
- `.claude/skills/session-consistency-manager/agents/sc-analysis-worker.md`
- `.claude/skills/session-consistency-manager/agents/sc-proposal-worker.md`
- `.claude/skills/session-consistency-manager/agents/sc-evaluator.md`
- 新規作成または変更されたロール定義ファイル（`roles/*.md` を含む）

### チェック項目

#### A. ライフサイクル完備チェック

- [ ] `session-lifecycle-policy` §1.2 の適用マトリクスで「必須」となっているステージが、ロール定義に含まれているか
- [ ] 壁打ちフェーズの定義があるか（記録先ファイル・フォーマットが明記されているか）
- [ ] 計画ステージが適切に定義されているか（マネージャー系は立案、ワーカー系は実施/評価計画）
- [ ] レポートの構成が明記されているか
- [ ] 「推奨」ステージの欠落がないか（欠落している場合は課題として起票）

#### B. ペアリング整合性チェック

- [ ] 実施者と対応する評価者の両方のロール定義が存在するか
- [ ] 実施者の成果物が評価者の入力として参照されているか（担当ファイルテーブルで確認）
- [ ] ペアリングの対称性要件（`session-lifecycle-policy` §2.3）が満たされているか
- [ ] オーケストレーターのルール定義に、実施者→評価者の起動順序が明記されているか

#### C. 課題起票・ルーティングチェック

- [ ] 課題起票の方法（中間バッファ経由 or CSV直接起票）がロール定義に明記されているか
- [ ] 知見記録セクション（「ルール化候補」「参考情報」の分類テーブル）が定義されているか
- [ ] 知見集約のルーティング先が明記されているか（マネージャー系のみ）

#### D. マネージャー共通ポリシー準拠チェック

- [ ] ゲート判定基準の定義があるか（直接記載または `manager-common-policy` §4 参照）
- [ ] 差し戻し手順の定義があるか（直接記載または `manager-common-policy` §7 参照）

#### E. 停止ルール・スコープチェック

- [ ] 「やること」「やらないこと」セクションが存在し、スコープが明確か
- [ ] 停止ルールが定義されているか
- [ ] 停止時の起票/報告フォーマットが明記されているか
- [ ] 担当ファイルテーブルがあり、各ファイルの操作権限（読み取り/編集/追記）が明記されているか

#### F. メタルール横断整合性チェック

- [ ] テンプレートファイルのパス参照がスキル・エージェント定義内のフロー記述と一致しているか
- [ ] `.claude/skills/` 配下の変更が `docs/workflow.md` の対応セクションに反映されているか
- [ ] `.claude/rules/` 配下のルール変更が本チェックリスト（TG-008）の基準に反映されているか

### 不適合時のアクション

| 不適合の種類 | アクション |
|-------------|----------|
| 「必須」ステージの欠落 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 高、CSV は自動生成） |
| 「推奨」ステージの欠落 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 中、CSV は自動生成） |
| ペアリング不整合 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 高、CSV は自動生成） |
| フォーマット不備（停止ルール・担当ファイル等の欠落） | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 低、CSV は自動生成） |
| 軽微な記述ズレ（表現の不統一等） | トリアージセッション内で修正 |
| テンプレート・ルールとメタルールの不整合 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 中、CSV は自動生成）。軽微なパス参照ズレはセッション内で修正 |

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | 共通パターン（§2〜§8）の参照先。共通ポリシーの変更時に参照箇所を確認 |
| `sessions/triage/_template/00_pre_investigation.md` | 事前調査の走査項目・テンプレート構成 |
| `sessions/triage/_template/01_plan.md` | 実施計画のテンプレート構成 |
| `sessions/triage/_template/03_report.md` | レポートのテンプレート構成（知見集約・課題集約セクション含む） |
| `sessions/triage/_template/04_gate_review.md` | ゲート判定のテンプレート構成 |
| `sessions/triage/_template/phase-1-scan/_template/07_issues.md` | ワーカーセット別課題バッファのテンプレート |
| `docs/workflow.md` | トリアージセッションフローの記述（人間向け可視化） |
| `CLAUDE.md` | 「docs/ 文書分類」テーブル（参考資料ステータスチェックの分類基準として参照） |
| `agents/triage-worker.md` | ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/triage-evaluator.md` | 評価基準・レポート構成に影響する変更の場合 |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | ライフサイクルパターン・ペアリング要件の定義（TG-008 チェックリストから参照） |
| `.github/gha-skills-mapping.yml` | TG-010 のマッピングマニフェスト。TG タスク追加・スキル定義変更時に連動更新 |
| `.github/prompts/triage.md` | GHA トリアージプロンプト。TG タスク追加・フロー変更時に連動更新 |

---

## 頻度

気が向いたとき（ユーザー任意）。ただし前回実施日を `00_pre_investigation.md` に必ず記録する。
