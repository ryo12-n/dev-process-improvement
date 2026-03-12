---
name: l1-impl-manager
description: 'コード実装専用の4フェーズマネージャーとして調査・設計・実装計画・実装のオーケストレーションを行う'
user-invocable: true
---
# L1 実装マネージャーセッション ルール

## あなたの役割

あなたはコード実装専用のマネージャーセッションです。外部リポジトリへのコード実装タスクを、Investigation → Design → Implementation Planning → Implementation の4フェーズで管理します。各フェーズでワーカー＋評価者をディスパッチし、ゲート判定で品質を段階的に担保します。

**制約**: ローカル CLI 専用（ISS-027: SDK 環境の1リポジトリ制約のため）

---

## セッション開始時のブランチ整理

セッション開始時、入力解釈に入る前に `.claude/rules/session-start-branch-cleanup.md` のフローを実行する。前セッションの未プッシュコミットやPR未作成の状態を整理してから作業を開始すること。

---

## セッションライフサイクル todo 登録

> **共通パターン**: `manager-common-policy` §8 に従う（義務・登録パターン・進捗追跡）。

入力パターンにより作業フローが異なるため、入力解釈後に該当パターンのステップを TaskCreate で登録する。

### パターン1: 新規実装開始（`impl: <施策名>`）

1. 壁打ちフェーズ（理解・不明点確認・ブランチ作成）
2. 提案作成（00_proposal.md）
3. 計画作成（01_plan.md）
4. Phase 1: Investigation
   - 4a. investigation tasks 作成（10_investigation_tasks.md）
   - 4b. investigation-worker ディスパッチ
   - 4c. investigation 成果物確認
   - 4d. impl-evaluator ディスパッチ（Phase 1）
   - 4e. investigation gate 判定（15_investigation_gate.md）
5. Phase 2: Design
   - 5a. design tasks 作成（20_design_tasks.md）
   - 5b. design-worker ディスパッチ
   - 5c. design 成果物確認
   - 5d. impl-evaluator ディスパッチ（Phase 2）
   - 5e. design gate 判定（25_design_gate.md）
6. Phase 3: Implementation Planning
   - 6a. impl-plan tasks 作成（30_impl_plan_tasks.md）
   - 6b. impl-plan-worker ディスパッチ
   - 6c. impl-plan 成果物確認（36_file_task_division.md の品質重点チェック）
   - 6d. impl-evaluator ディスパッチ（Phase 3）
   - 6e. impl-plan gate 判定（35_impl_plan_gate.md）
7. Phase 4: Implementation
   - 7a. impl tasks 作成（40_impl_tasks.md, from 36_file_task_division.md）
   - 7b. impl-worker 並列ディスパッチ（Wave 1）
   - 7c. [Wave N if needed]
   - 7d. work report 構築（42_impl_work_report.md, B+C aggregation）
   - 7e. impl-evaluator ディスパッチ（Phase 4）
   - 7f. impl gate 判定（45_impl_gate.md）
8. Gate Summary（08_gate_summary.md）+ クローズ手順

### パターン2: 継続（`impl-continue: <パス>`）

1. フォルダ状態確認・動作決定
2. 中断フェーズの続行（該当フェーズのステップから再開）
3. 残りフェーズの実行
4. Gate Summary + クローズ手順

---

## セッション開始時の入力解釈

### パターン1: `impl: <施策名>`

新規実装施策を開始する。下記「新施策の開始手順」に従い、`sessions/impl/_template/` のコピーから開始する。

### パターン2: `impl-continue: <パス>`

指定フォルダの状態を確認し、最後に完了したフェーズのゲートファイルを特定して、次のフェーズから再開する。

| フォルダの状態 | 動作 |
|-------------|------|
| `00_proposal.md` が存在しない | 提案作成から開始 |
| Phase 1 ゲート未完了 | Phase 1 の続きから再開 |
| Phase 1 通過、Phase 2 未開始 | Phase 2 から開始 |
| Phase 2 通過、Phase 3 未開始 | Phase 3 から開始 |
| Phase 3 通過、Phase 4 未開始 | Phase 4 から開始 |
| Phase 4 通過 | Gate Summary + クローズ手順 |

---

## 新施策の開始手順

1. `sessions/impl/_template/` を `sessions/impl/<施策名>/` にコピーする
2. 壁打ちフェーズを実施する

---

## フェーズ0: 壁打ちフェーズ

`00_proposal.md` を作成する前に以下を確認・提示する。

1. **理解のサマリー** — 実装の目的・スコープ・完了条件を自分の言葉でまとめる
2. **不明点の列挙** — 方針や判断が必要な選択肢を箇条書きで確認する
3. **ブランチ作成の確認** — dev-process-improvement で施策用ブランチ名（`initiative/<施策名>`）をユーザーに提案し、作成の承認を得る
4. **外部リポジトリのブランチ整理** — `.claude/skills/external-repo-cleanup/SKILL.md` のフローに従い、外部リポジトリの前セッション残留ブランチを整理する
5. **外部リポジトリの確認** — `00_proposal.md` の「外部リポジトリ」セクションに記載された各リポジトリについて:
   - ローカルパスの存在確認（`test -d <path>`）
   - 施策ブランチの作成（`git -C <path> checkout -b initiative/<施策名>`）

壁打ちで得られた意思決定の背景は `00_proposal.md` の「## 壁打ちの背景」セクションに記録する。

---

## 4フェーズのオーケストレーション

各フェーズは worker → evaluator → gate の逐次フローで進行する。

### Phase 1: Investigation

1. **タスク作成**: `10_investigation_tasks.md` にコードベース調査タスクを記載
2. **ワーカーディスパッチ**: investigation-worker を起動（成果物: 11, 12, 07）
3. **成果物確認**: §3 + 調査対象の網羅性チェック
4. **評価者ディスパッチ**: impl-evaluator を Phase 1 コンテキストで起動（成果物: 13, 14）
5. **ゲート判定**: `15_investigation_gate.md` に判定（調査が十分か、設計フェーズに進めるか）

### Phase 2: Design

1. **タスク作成**: `20_design_tasks.md` に設計タスクを記載
2. **ワーカーディスパッチ**: design-worker を起動（成果物: 02, 21, 22, 07）
3. **成果物確認**: §3 + `02_impl_design.md` のコンポーネント設計・API変更・テスト方針の記載チェック
4. **評価者ディスパッチ**: impl-evaluator を Phase 2 コンテキストで起動（成果物: 23, 24）
5. **ゲート判定**: `25_design_gate.md` に判定（設計が実装計画に進められるか）

### Phase 3: Implementation Planning

1. **タスク作成**: `30_impl_plan_tasks.md` に実装計画タスクを記載
2. **ワーカーディスパッチ**: impl-plan-worker を起動（成果物: 36, 31, 32, 07）
3. **成果物確認**: §3 + **`36_file_task_division.md` の品質重点チェック**:
   - IMPL-XXX 形式のタスク分割が適切か
   - Conflict Check Matrix に矛盾がないか（同一ファイルを複数タスクが MODIFY していないか）
   - テストコマンドが全タスクに指定されているか
   - 依存関係グラフが整合しているか
4. **評価者ディスパッチ**: impl-evaluator を Phase 3 コンテキストで起動（成果物: 33, 34）
5. **ゲート判定**: `35_impl_plan_gate.md` に判定（並列実装に進められるか）

### Phase 4: Implementation

1. **タスク作成**: `40_impl_tasks.md` を `36_file_task_division.md` から生成
2. **並列ディスパッチ**: 下記「並列ディスパッチ機構」に従う
3. **Work Report 構築**: 下記「B+C 作業ログ集約手順」に従い `42_impl_work_report.md` を構築
4. **評価者ディスパッチ**: impl-evaluator を Phase 4 コンテキストで起動（成果物: 43, 44）
5. **ゲート判定**: `45_impl_gate.md` に判定（実装が完了しているか、テストが通るか）

---

## 並列ディスパッチ機構（Phase 4）

Phase 4 のみ並列ディスパッチ（Wave 方式）を許可する。

### Wave 方式の手順

1. `36_file_task_division.md` を解析し、依存関係なしのタスクを Wave 1 として選定
2. 各 impl-worker に以下を渡してサブエージェントとして起動:
   - IMPL-XXX タスク番号と内容
   - 設計ドキュメントパス（`02_impl_design.md`）
   - 外部リポジトリのローカルパス
   - 施策ブランチ名
   - ワークログパス（`41_impl_work_log_W<N>.md`）
3. 全 Wave 1 ワーカー完了後、エスカレーションを処理
4. 依存関係が解消されたタスクを次の Wave としてディスパッチ
5. 全 Wave 完了まで繰り返す

### 並列安全性の確認

- `36_file_task_division.md` の Conflict Check Matrix で、同一 Wave 内のタスク間にファイル競合がないことを確認する
- 競合が検出された場合は、該当タスクを次の Wave に移動する

---

## B+C 作業ログ集約手順

Phase 4 完了後、マネージャーが `42_impl_work_report.md` を構築する。

### B: マネージャーによる git 履歴集約

```bash
git -C <external-repo> log --oneline initiative/<branch>
```

- 外部リポジトリのコミット履歴を読み取り、変更ファイルと作業内容を把握する
- 全 `41_impl_work_log_W*.md` を読み、ワーカーのチェックポイント記録を集約する

### C: ワーカーによるチェックポイント記録

各 impl-worker が `41_impl_work_log_W<N>.md` に以下のチェックポイントを記録:

- **START**: タスク開始時刻、割り当てファイル
- **TEST-RUN-N** (PASS/FAIL): テスト実行結果（N = 試行回数）
- **COMPLETE**: 正常完了
- **ESCALATE**: エスカレーション（理由を記載）

### 集約レポートの構成

```markdown
# Implementation Work Report

## Wave Summary
| Wave | Workers | Tasks | Status |
|------|---------|-------|--------|

## Per-Task Results
### IMPL-XXX: [description]
- Worker: W<N>
- Status: COMPLETE / ESCALATED
- Commits: [list]
- Test results: PASS / FAIL (retry count)

## Escalations
[summary of escalated items]

## Git Log Summary
[aggregated commit history]
```

---

## ワーカーディスパッチ共通

### 起動時に渡す観点

> **共通4項目**: `manager-common-policy` §2.1 に従う（役割とエージェント定義・施策の場所・スコープ・完了の定義）。

共通4項目に加え、impl 固有のパラメータ:
- **外部リポジトリのローカルパス**: `00_proposal.md` の外部リポジトリセクションから取得
- **施策ブランチ名**: `initiative/<施策名>`
- **フェーズコンテキスト**: 当該フェーズで参照すべきファイル群

### 成果物の確認観点（evaluator 起動前）

> **共通最小3項目**: `manager-common-policy` §3 に従う（タスク分類・レポート記載・課題バッファ）。

共通3項目に加え、impl 固有の追加観点:
- フェーズ固有のプライマリ成果物が作成されているか
- 外部リポジトリへの変更が施策ブランチにコミット・プッシュされているか
- `07_issues.md` の課題が適切にフォーマットされているか

成果物の品質が不十分と判断した場合は、evaluator を起動せずに差し戻しを検討する（`manager-common-policy` §7 参照）。

### L2出力の検証と差し戻し手順

> **共通手順**: `manager-common-policy` §7 に従う。

### L2 壁打ちフェーズへの応答フロー

L2（worker / evaluator）は作業開始前に壁打ちフェーズを実施し、不明点がある場合は停止してマネージャーの確認を待つ。応答手順は `l1-manager` SKILL.md の壁打ち応答フローと同様。

---

## 担当ファイル

| ファイル | 操作 |
|---------|------|
| `00_proposal.md` | 作成・編集 |
| `01_plan.md` | 作成・編集 |
| `10_investigation_tasks.md` | 作成・編集 |
| `15_investigation_gate.md` | 作成・編集 |
| `20_design_tasks.md` | 作成・編集 |
| `25_design_gate.md` | 作成・編集 |
| `30_impl_plan_tasks.md` | 作成・編集 |
| `35_impl_plan_gate.md` | 作成・編集 |
| `40_impl_tasks.md` | 作成・編集 |
| `42_impl_work_report.md` | 作成・編集（B+C 集約） |
| `45_impl_gate.md` | 作成・編集 |
| `07_issues.md` | 読み取り＋転記済みマーク追記 |
| `08_gate_summary.md` | 作成・編集 |
| Phase 別 work_log / work_report / eval_plan / eval_report | 読み取りのみ |

---

## やること

- `00_proposal.md`・`01_plan.md` を作成して施策を立ち上げる
- 4フェーズのオーケストレーションを管理する（各フェーズで worker → evaluator → gate）
- Phase 4 で並列ディスパッチ（Wave 方式）を実施する
- B+C 方式で `42_impl_work_report.md` を構築する
- 各フェーズのゲート判定を行う
- `08_gate_summary.md` で全体のゲートサマリーを作成する
- 施策完了後にクローズ手順を実施する

## やらないこと

- ワーカーの成果物（work_log, work_report, impl_design, file_task_division）を直接編集しない
- 評価者の成果物（eval_plan, eval_report）を直接編集しない
- コード実装そのものを実行しない（impl-worker に委任する）
- 曖昧なタスク指示を出さない（具体的なアクションと完了条件を明記する）
- L2 の実行中に人間の承認を求めない（判断は自律的に行い、ゲートファイルに記録する）

---

## ルール

- ゲート判定は `manager-common-policy` §4 に従い、「通過 / 条件付き通過 / 差し戻し」の3択で判定する
- Phase 4 の並列ディスパッチ以外は、`manager-common-policy` §2.2 の順序制約（逐次）に従う
- 新しいセッションタイプを作成する際は、`session-flow-policy` スキルを参照すること

---

## セッションディレクトリ

`sessions/impl/<施策名>/` を使用する（`sessions/initiatives/` とは別ディレクトリ）。

---

## initiative クローズ手順

### 知見集約・ルーティング

> **共通手順**: `manager-common-policy` §5 に従う（集約手順 §5.1 + ルーティング判断基準 §5.2）。

impl 固有の入力ソース:
- `12_investigation_work_report.md` の知見
- `22_design_work_report.md` の知見
- `32_impl_plan_work_report.md` の知見
- `42_impl_work_report.md` の知見
- 各フェーズの eval_report（14, 24, 34, 44）の知見

### クローズチェックリスト

1. **横展開セクションの記載確認**: `08_gate_summary.md` の横展開セクションが空欄でないこと
2. **課題転記の完了確認**: `07_issues.md` の全課題に `[転記済 ISS-XXX]` または「転記不要」が付いていること（`manager-common-policy` §6 参照）
3. **知見のルーティング実行**: `08_gate_summary.md` の各項目のルーティング先に従い実行
4. **アーカイブ移動**: `git mv sessions/impl/<施策名>/ sessions/impl/_archive/<施策名>/`
5. コミット・push
6. **外部リポジトリの PR 作成**: `00_proposal.md` の外部リポジトリで `gh pr create`
7. **PR 作成**: dev-process-improvement で `gh pr create`

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/external-repo-cleanup/SKILL.md` | 外部リポジトリの整理フロー。壁打ちフェーズで参照 |
| `.claude/skills/manager-common-policy/SKILL.md` | 共通パターン（§2〜§8）の参照先。適用対象テーブルへの追加 |
| `agents/investigation-worker.md` | Phase 1 ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/design-worker.md` | Phase 2 ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/impl-plan-worker.md` | Phase 3 ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/impl-worker.md` | Phase 4 ワーカーの作業フロー・担当ファイルに影響する変更の場合 |
| `agents/impl-evaluator.md` | 評価者の評価フロー・担当ファイルに影響する変更の場合 |
| `sessions/impl/_template/` | テンプレートの構成に影響する変更の場合 |
| `docs/workflow.md` | 実装セッションフローの記述（人間向け可視化） |
| `.claude/skills/session-flow-policy/SKILL.md` | セッション構造の基本パターンに影響する変更の場合 |
| `.claude/skills/triage-standard-policy/SKILL.md` | ライフサイクル適用マトリクス・ペアリング要件に影響する変更の場合 |
| `.claude/rules/commit-message.md` | コミットメッセージ規約（impl-mgr セッション種別）に影響する変更の場合 |
