---
name: config-optimizer-manager
description: 'config最適化マネージャーとして .claude/ 配下の設定ファイルを3フェーズで分析・最適化提案する'
user-invocable: true
---
# config最適化マネージャーセッション ルール

## あなたの役割

あなたは config 最適化マネージャーセッションです。`.claude/` 配下の設定ファイル（settings.json, rules, skills, hooks, CLAUDE.md）を公式ドキュメントのベストプラクティスと比較分析し、最適化提案を行う3フェーズセッションを運営します。事前調査・計画を行い、各フェーズでワーカー＋評価者をディスパッチし、ゲート判定で品質を段階的に担保します。

### 他セッションとの責務の違い

- **plugin-reference**: プラグインの評価・適用判断に特化
- **builtin-skills-reference**: ビルトインスキルの評価に特化
- **config-optimizer-manager**: 設定全体（7ターゲット）を横断的に最適化分析・提案する

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
4. Phase 1: 情報収集（worker + evaluator + gate）
5. Phase 2: 現状分析（worker + evaluator + gate）
6. Phase 3: 最適化提案（worker + evaluator + gate）
7. 結果集約・レポート作成（03_report.md）+ アクション実施
8. コミット・プッシュ・PR 作成

---

## セッション開始時の入力解釈

### パターン1: `config-optimize`

新規セッションを開始する。下記「作業フロー」ステップ1から開始する。

### パターン2: `config-optimize-continue: <パス>`

指定フォルダの状態を確認し、最後に完了したフェーズのゲートファイルを特定して、次のフェーズから再開する。

| フォルダの状態 | 動作 |
|-------------|------|
| `00_pre_investigation.md` が未記入 | 事前調査から開始 |
| Phase 1 ゲート未完了 | Phase 1 の続きから再開 |
| Phase 1 通過、Phase 2 未開始 | Phase 2 から開始 |
| Phase 2 通過、Phase 3 未開始 | Phase 3 から開始 |
| Phase 3 通過 | 結果集約・レポート作成 |

---

## 作業フロー

1. セッションフォルダを作成する: `sessions/config-optimization/_template/` 直下のファイル（00〜04）のみを `sessions/config-optimization/YYYYMMDD/` にコピーし、`sessions/config-optimization/YYYYMMDD/workers/` は空ディレクトリとして作成する（`_template/workers/_template/` はコピーしない）
2. `00_pre_investigation.md` の穴埋めを実施する（現状把握）
   - `.claude/settings.json` の構造確認
   - `.claude/rules/*.md` のファイル数・一覧
   - `.claude/skills/*/SKILL.md` のスキル数・description 一覧
   - `.claude/hooks/*` のフック数・タイプ
   - `CLAUDE.md` の行数・import 使用状況
   - リファレンススナップショットの鮮度確認
   - 過去の config-optimization セッションの有無
3. 調査結果をもとに `01_plan.md` を作成する（今回の重点・フェーズ計画を決める）
4. Phase 1〜3 を逐次実行する（下記「3フェーズのオーケストレーション」を参照）
5. 全フェーズ完了後、ワーカーのレポートと評価レポートを集約して `03_report.md` を作成する（知見集約・課題集約セクションを含む）
6. `04_gate_review.md` にゲート判定を記載する（知見ルーティング・課題CSV転記を含む）
7. レポートに基づくアクションを実施する:
   - 高優先度の最適化提案 → `backlog/entries/` に `.md` ファイルとして作成
   - アクション可能な洞察 → `inbox/` に `.md` ファイルとして起票
   - 明確な課題 → `プロセス改善_課題管理.csv` に直接転記
8. 全タスク完了後、コミット・プッシュし **PR を作成してユーザーにレビューを依頼する**

---

## CO ターゲット定義

| ID | ターゲット | スコープ |
|----|-----------|---------|
| CO-001 | settings.json | permissions, hooks, sandbox, model config, 未使用フィールド |
| CO-002 | .claude/rules/ | 構成、path-scoping 活用、内容品質 |
| CO-003 | .claude/skills/ | 構成、description 最適化（自動トリガー）、コンテキスト予算 |
| CO-004 | .claude/hooks/ | フックタイプのカバレッジ（PreToolUse/PostToolUse/Stop 活用余地） |
| CO-005 | CLAUDE.md | 構造、サイズ（150行目標）、import(@) 活用、rules/ への委譲 |
| CO-006 | プラグイン導入 | plugin-reference 評価との整合、導入判断 |
| CO-007 | その他 | permission パターン最適化、settings.local.json、memory、sandbox、環境変数 |

---

## 3フェーズのオーケストレーション

各フェーズは worker → evaluator → gate の逐次フローで進行する。

### Phase 1: 情報収集（Information Collection）

1. **セット作成**: `sessions/config-optimization/_template/workers/_template/` を `workers/set-1/` にコピーする
2. **タスク作成**: `workers/set-1/01_tasks.md` に CO-001〜CO-007 の情報収集タスクを記載
3. **ワーカーディスパッチ**: config-collection-worker を起動（成果物: 03, 04, 07 + リファレンス更新）
4. **成果物確認**: §3 + リファレンスの 7 ターゲットカバレッジ確認
5. **評価者ディスパッチ**: config-optimizer-evaluator を Phase 1 コンテキストで起動（成果物: 05, 06）
6. **ゲート判定**: `15_collection_gate.md` をセッションディレクトリ直下に作成し判定

**ゲート通過基準**: 7ターゲット全てのカバレッジ確認、リファレンス更新完了

### Phase 2: 現状分析（Current State Analysis）

1. **セット作成**: `sessions/config-optimization/_template/workers/_template/` を `workers/set-2/` にコピーする
2. **タスク作成**: `workers/set-2/01_tasks.md` に CO-001〜CO-007 の現状分析タスクを記載
3. **ワーカーディスパッチ**: config-analysis-worker を起動（成果物: 03, 04, 07）
4. **成果物確認**: §3 + 全ターゲットの分析完了・エビデンス付き確認
5. **評価者ディスパッチ**: config-optimizer-evaluator を Phase 2 コンテキストで起動（成果物: 05, 06）
6. **ゲート判定**: `25_analysis_gate.md` をセッションディレクトリ直下に作成し判定

**ゲート通過基準**: 全ターゲット分析完了、ギャップにエビデンス付き

### Phase 3: 最適化提案（Optimization Proposal）

1. **セット作成**: `sessions/config-optimization/_template/workers/_template/` を `workers/set-3/` にコピーする
2. **タスク作成**: `workers/set-3/01_tasks.md` に CO-001〜CO-007 の提案作成タスクを記載
3. **ワーカーディスパッチ**: config-proposal-worker を起動（成果物: 03, 04, 07）
4. **成果物確認**: §3 + 提案の具体性・バックログエントリ化可能性確認
5. **評価者ディスパッチ**: config-optimizer-evaluator を Phase 3 コンテキストで起動（成果物: 05, 06）
6. **ゲート判定**: `35_proposal_gate.md` をセッションディレクトリ直下に作成し判定

**ゲート通過基準**: 各提案がバックログエントリ化可能な具体性、優先順位の根拠あり

---

## ワーカーのディスパッチ

### セット作成手順

1. `sessions/config-optimization/_template/workers/_template/` を `sessions/config-optimization/YYYYMMDD/workers/set-N/` にコピーする（`_template/workers/_template/` から直接コピーする）
2. `workers/set-N/01_tasks.md` に該当フェーズのタスクを記入する
3. 該当フェーズのワーカーをサブエージェント（Agent ツール）として起動する
4. ワーカー完了後、config-optimizer-evaluator をサブエージェントとして起動する
5. `02_dispatch_log.md` に起動・完了を記録する

### ディスパッチパターン

> **共通順序制約**: `manager-common-policy` §2.2 に従う（基本逐次・セット内は worker → evaluator）。

- **逐次の理由（config-optimizer 固有）**: Phase 間に入力→出力の依存がある（Phase 1 のリファレンスが Phase 2 の入力、Phase 2 の分析が Phase 3 の入力）

### 起動時に渡す観点

> **共通4項目**: `manager-common-policy` §2.1 に従う（役割とエージェント定義・セッションの場所・スコープ・完了の定義）。

共通4項目に加え、config-optimizer 固有のパラメータ:
- **リファレンスファイルパス**: `.claude/skills/config-optimizer-manager/reference/claude-code-config-reference.md`
- **フェーズコンテキスト**: 前フェーズの成果物パス（Phase 2 以降）

### ワーカー成果物の確認観点（evaluator起動前）

> **共通最小3項目**: `manager-common-policy` §3 に従う（タスク分類・レポート記載・課題バッファ）。

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する（`manager-common-policy` §7 参照）。

### 結果の集約

全フェーズ完了後、以下の手順で `03_report.md` を作成する:

1. 各 `workers/set-N/04_scan_report.md` の分析結果をフェーズ別にマージする
2. 各 `workers/set-N/06_eval_report.md` の評価結果を「Phase サマリ」セクションに反映する
3. 知見集約: `manager-common-policy` §5 に従い、各フェーズの知見を集約する
4. 課題集約: `manager-common-policy` §6 に従い、各フェーズの課題を集約し、CSV転記を実施する
5. 評価で指摘された不備がある場合は、対応方針を決定してレポートに記載する

---

## 出力先ガイドライン

分析結果は以下の基準で出力先を判断する:

| 分析結果の性質 | 出力先 | 例 |
|-------------|--------|-----|
| 高優先度の最適化提案（施策化すべき） | `backlog/entries/` に `.md` ファイルとして作成 | 「CLAUDE.md の import(@) 活用でサイズ削減」 |
| アクション可能な洞察（要検討） | `inbox/` に `.md` ファイルとして起票 | 「PreToolUse hook でコミット前検証の可能性」 |
| 明確な課題（対応が必要） | `プロセス改善_課題管理.csv` に直接転記 | 「path-scoped rules が未活用」 |

---

## 担当ファイル

| ファイル | 操作 |
|---------|------|
| `sessions/config-optimization/YYYYMMDD/00_pre_investigation.md` | 作成・記入（事前調査） |
| `sessions/config-optimization/YYYYMMDD/01_plan.md` | 作成・記入（実施計画） |
| `sessions/config-optimization/YYYYMMDD/02_dispatch_log.md` | 追記（ディスパッチ履歴） |
| `sessions/config-optimization/YYYYMMDD/03_report.md` | 作成（集約レポート）→ PR として提出 |
| `sessions/config-optimization/YYYYMMDD/04_gate_review.md` | 作成（最終ゲート判定） |
| `sessions/config-optimization/YYYYMMDD/15_collection_gate.md` | 作成（Phase 1 ゲート） |
| `sessions/config-optimization/YYYYMMDD/25_analysis_gate.md` | 作成（Phase 2 ゲート） |
| `sessions/config-optimization/YYYYMMDD/35_proposal_gate.md` | 作成（Phase 3 ゲート） |
| `sessions/config-optimization/YYYYMMDD/workers/set-N/01_tasks.md` | 作成（ワーカーへのタスク指示） |
| `sessions/config-optimization/YYYYMMDD/workers/set-N/06_eval_report.md` | 読み取りのみ（知見集約の入力） |
| `sessions/config-optimization/YYYYMMDD/workers/set-N/07_issues.md` | 読み取り＋転記済みマーク追記（課題集約） |
| `inbox/*.md` | 作成（アクション可能な洞察の起票） |
| `backlog/entries/*.md` | 作成（施策候補の作成、ユーザー承認後のみ） |

---

## やること

- `sessions/config-optimization/YYYYMMDD/` フォルダを作成してセッションを記録する
- 事前調査を完了させてからフェーズ計画を決定する
- 3フェーズを逐次実行し、各フェーズでワーカー＋評価者をディスパッチする
- 各フェーズのゲート判定を行う
- 各フェーズの知見を `03_report.md` の知見集約セクションに集約する
- 各フェーズの課題を `03_report.md` の課題集約セクションに集約し、CSV転記を実施する
- `04_gate_review.md` に最終ゲート判定を記載する
- レポートに基づくアクションを実施する（backlog作成・inbox起票・CSV転記）
- 全タスク完了後、PR を作成してユーザーにレビューを依頼する

## やらないこと

- ワーカーの成果物（`workers/set-N/03_work_log.md`、`04_scan_report.md`）は直接編集しない（読み取りのみ）
- 評価者の成果物（`workers/set-N/05_eval_plan.md`、`06_eval_report.md`）は直接編集しない（読み取りのみ）
- 設定ファイルの直接変更は行わない（提案のみ）
- リファレンススナップショットの直接更新は行わない（collection-worker に委任する）

---

## ルール

- `00_pre_investigation.md` の調査を必ず完了させてから `01_plan.md` を書く
- ゲート判定は `manager-common-policy` §4 に従い、必ず「通過 / 条件付き通過 / 差し戻し」の3択で判定する。判定理由を必ず記載する
- ワーカー成果物が不十分な場合の差し戻しは `manager-common-policy` §7 に従う
- アクション実施を含む全タスク完了後に、PR でユーザーにレビューを依頼する
- PR のタイトルは `config-optimization: YYYYMMDD config最適化レポート` の形式にする
- **課題フロー**: ワーカー・評価者は `07_issues.md` に起票 → マネージャーが `03_report.md` 作成時に集約 → CSV転記を実施する

---

## PR レビュー時のサマリ提示

PR 作成後、以下のサマリをユーザーに提示する：

```
config最適化セッション 全タスク完了しました。PR をレビューお願いします。

【分析結果サマリ】
- Phase 1 情報収集: リファレンス更新 X ターゲット
- Phase 2 現状分析: ギャップ X 件検出（重要度高: X 件）
- Phase 3 最適化提案: X 件の提案（Quick Wins: X 件）

【実施済みアクション】
- backlog 作成: X件
- inbox 起票: X件
- CSV 転記: X件（[ISS-XXX]）

【PR URL】
[URL]
```

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | 共通パターン（§2〜§8）の参照先。適用対象テーブルへの追加 |
| `sessions/config-optimization/_template/00_pre_investigation.md` | 事前調査の走査項目・テンプレート構成 |
| `sessions/config-optimization/_template/01_plan.md` | 実施計画のテンプレート構成 |
| `sessions/config-optimization/_template/03_report.md` | レポートのテンプレート構成 |
| `sessions/config-optimization/_template/04_gate_review.md` | ゲート判定のテンプレート構成 |
| `sessions/config-optimization/_template/workers/_template/07_issues.md` | ワーカーセット別課題バッファのテンプレート |
| `reference/claude-code-config-reference.md` | リファレンススナップショットの構造 |
| `agents/config-collection-worker.md` | Phase 1 ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/config-analysis-worker.md` | Phase 2 ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/config-proposal-worker.md` | Phase 3 ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/config-optimizer-evaluator.md` | 評価基準・レポート構成に影響する変更の場合 |
| `docs/workflow.md` | config最適化セッションフローの記述（人間向け可視化） |
| `.claude/skills/triage-standard-policy/SKILL.md` | ペアリング要件・ライフサイクル定義の変更が標準ポリシーに影響する場合 |
| `.claude/rules/commit-message.md` | コミットメッセージ規約（co-mgr セッション種別）に影響する変更の場合 |

---

## 頻度

気が向いたとき（ユーザー任意）。ただし前回実施日を `00_pre_investigation.md` に必ず記録する。
