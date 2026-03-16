# 開発プロセス改善ワークフロー

> **このファイルの位置づけ**
> `.claude/skills/` 配下のスキル・エージェント定義が正の情報源（Source of Truth）。
> このファイルはルールファイルの内容を人間が理解するための可視化・要約です。
> ルールを変更した場合は、このファイルも合わせて更新してください。

## イニシアティブセッション フロー

```
[L1 マネージャー]
  ブランチ整理: SessionStart hook（.claude/hooks/session-start-branch-cleanup.sh）により自動実行
    → 現在ブランチ確認 → 未プッシュコミットがあれば push → PR未作成なら作成 → main に切り替え・最新化
    ※ L2 サブエージェントは対象外（L1 の責務）
    ※ hook の出力（JSON）を確認し、エラーや警告があればユーザーに報告する
                                                                    ↓
  フェーズ0: 壁打ち（理解のサマリー・不明点をユーザーに確認）
    → 調査・方針決定 → 提案(00_proposal.md) → 計画(01_plan.md) → タスク作成(02_tasks.md)
    → 外部リポジトリがある場合: external-repo-cleanup スキルで前セッションのブランチ整理 → 00_proposal.md に記載し、施策ブランチを作成
    → ドメインエージェント選定（任意）: refs/agency-agents/knowledge.md を参照し、施策タイプに適したエージェントを選定
      → 02_tasks.md の「参照ドメインエージェント」セクションに記載（該当なしなら「なし」）
    ※ 02_tasks.md には CSV 転記の固定タスクを必ず含める（後述）
                                                                    ↓
  Phase A→B チェック記録（08_gate_review.md — Worker ディスパッチ前チェック5項目を記録）
                                                                    ↓
[L2 ワーカー（実施）] ← L1 が Task ツールでサブエージェントとして起動
  参照ドメインエージェントがある場合: 02_tasks.md の指定に従いエージェント定義を Read（専門知識として参照のみ、役割は引き受けない）
  壁打ちフェーズ → 03_work_log.md に実施計画サマリを記載 → タスク実施 → 作業記録を追記
  → 04_work_report.md を作成（知見セクションへの記載を含む）
  ※ 外部リポ変更時: 00_proposal.md の外部リポセクション確認 → 施策ブランチにチェックアウト
    → コミット・プッシュ（main 直接コミット禁止・push 省略禁止）
  ※ 課題発見時: 07_issues.md に一時メモ → 施策完了時に CSV へ転記
                                                                    ↓
  L1: worker 成果物を確認（タスク完了状態・CSV転記状態）
    + Phase B→C チェック記録（08_gate_review.md — Evaluator ディスパッチ前チェック8項目を記録）
    → 品質不十分なら差し戻し
                                                                    ↓
[L2 ワーカー（評価）] ← L1 が Task ツールでサブエージェントとして起動（worker 完了後に順次起動）
  壁打ちフェーズ → 05_eval_plan.md → 評価実施 → 06_eval_report.md（知見セクションへの記載を含む）
  → 課題があれば 07_issues.md に追記 → CSV へ転記
                                                                    ↓
[L1 マネージャー]
  Phase C→D チェック記録（08_gate_review.md — 最終ゲート判定前チェック5項目を記録）
  04・06・07 を確認 → 08_gate_review.md にゲート判定を記入
    → 通過     : 次フェーズのタスクを 02_tasks.md に追記
    → 条件付き : 条件対応タスクを追記 → L2 に差し戻し
    → 差し戻し : 計画修正 → 02_tasks.md 修正 → L2 に差し戻し
                                                                    ↓
  施策完了（全フェーズ通過）時:
    → initiative クローズ手順を実施
      1. 横展開セクション記載確認（08 の必須把握事項・次施策候補が空欄でないこと）
      2. 課題転記の完了確認（07 の全課題に [転記済 ISS-XXX] or 転記不要）
      3. 知見のルーティング実行（CSV / refs / backlog / inbox / なし）
      4. backlog ファイルの削除確認
      5. backlog.csv エントリの削除確認（00_proposal.md の backlog元ファイル or 施策名で特定）
      6. git mv sessions/initiatives/<施策名>/ sessions/initiatives/_archive/<施策名>/
      7. コミット・push
      8. 外部リポジトリがある場合: 各外部リポで施策ブランチから main への PR を作成
      9. PR 作成（dev-process-improvement 本体）
```

### フェーズゲートチェック（08_gate_review.md への累積記録）

L1 マネージャーは施策のライフサイクル中、3段階のフェーズチェックを `08_gate_review.md` に累積記録する。

| チェック | タイミング | 項目数 | 内容 |
|---------|-----------|--------|------|
| Phase A→B | Worker ディスパッチ前 | 5項目 | 提案の完全性・成功基準の評価可能性・タスクID/完了条件/優先度・固定タスク・施策ブランチ |
| Phase B→C | Evaluator ディスパッチ前 | 8項目 | タスク分類・レポート記載・計画対比実績・知見セクション・課題バッファ・CSV転記・外部リポ・メタルール検証 |
| Phase C→D | 最終ゲート判定前 | 5項目 | 評価計画カバー率・エビデンス品質・知見セクション・未転記課題・方針推奨 |

各チェックの結果は同一ファイル（`08_gate_review.md`）に順次追記され、施策全体のフェーズ遷移記録として残る。

### 壁打ちフェーズ（フェーズ0）

各セッション（L1・L2 共通）は作業着手前に壁打ちフェーズを実施する。

- **L1**: `00_proposal.md` 作成前に理解のサマリー・不明点を提示し、ユーザーに確認する
- **L2-worker**: `03_work_log.md` 冒頭にサマリー・前提条件チェック・不明点を記録。不明点があれば停止してL1の確認を待つ
- **L2-evaluator**: `05_eval_plan.md` 冒頭に同様のフォーマットで記録

### L2 サブエージェントの起動

L1 は L2 を **Task ツール（サブエージェント）** として順番に起動する。L2-worker が完了してから L2-evaluator を起動すること（並列起動しない）。

起動時に渡す情報: 役割とルールファイル、施策パス、タスク範囲、完了の定義、参照ドメインエージェント（任意、§10.3 参照）

### 固定タスク（02_tasks.md に必ず含める）

| 対象 | やること | 完了条件 |
|------|---------|---------|
| L2-worker（レポート作成時） | `04_work_report.md` の「作業中の知見」に知見を記録 | 「ルール化候補」「参考情報」各テーブルに最低1行 |
| L2-worker（最終タスク） | `07_issues.md` の未転記課題を CSV へ転記し、`issues/entries/ISS-XXX.md` を作成 | 全課題に `[転記済 ISS-XXX]` or 「転記不要」が付いている |
| L2-evaluator（レポート作成時） | `06_eval_report.md` の「評価中の知見」に知見を記録 | 「ルール化候補」「参考情報」各テーブルに最低1行 |
| L2-evaluator（最終タスク） | 評価中発見の課題を `07_issues.md` 起票 → CSV 転記 → `issues/entries/ISS-XXX.md` 作成 | 同上 |
| L2-worker（ルール・テンプレート変更時） | メタルール横断検証（フロー記述・workflow.md・TG-008基準）を実施し結果を記録 | 3領域の検証結果が `04_work_report.md` に記載 |

## 実装マネージャーセッション フロー

> **正の情報源**: `.claude/skills/l1-impl-manager/SKILL.md`
> **制約**: ローカル CLI 専用（ISS-027: SDK 環境の1リポジトリ制約のため）

```
[impl-manager]
  ブランチ整理: SessionStart hook（.claude/hooks/session-start-branch-cleanup.sh）により自動実行
                                                                    |
  入力: impl: <施策名> / impl-continue: <パス>
                                                                    |
  フェーズ0: 壁打ち（理解のサマリー・不明点確認）
    → 提案(00_proposal.md) → 計画(01_plan.md)
    → 外部リポジトリのブランチ準備（impl/<施策名>）
                                                                    |
  Phase 1: Investigation ─────────────────────────────────────────────
    → phase-1-investigation/01_tasks.md 作成
    → investigation-worker ディスパッチ（成果物: phase-1-investigation/02, 03, 07）
    → impl-evaluator ディスパッチ Phase 1（成果物: phase-1-investigation/04, 05）
    → phase-1-investigation/06_gate.md にゲート判定
                                                                    |
  Phase 2: Design ────────────────────────────────────────────────────
    → phase-2-design/01_tasks.md 作成
    → design-worker ディスパッチ（成果物: 02_impl_design, phase-2-design/02, 03, 07）
    → impl-evaluator ディスパッチ Phase 2（成果物: phase-2-design/04, 05）
    → phase-2-design/06_gate.md にゲート判定
                                                                    |
  Phase 3: Implementation Planning ───────────────────────────────────
    → phase-3-impl-plan/01_tasks.md 作成
    → impl-plan-worker ディスパッチ（成果物: phase-3-impl-plan/07, 02, 03, 07）
      ※ phase-3-impl-plan/07_file_task_division.md が Phase 4 の入力
    → impl-evaluator ディスパッチ Phase 3（成果物: phase-3-impl-plan/04, 05）
    → phase-3-impl-plan/06_gate.md にゲート判定
                                                                    |
  Phase 4: Implementation（並列ディスパッチ: Wave 方式 + worktree）─────
    → phase-4-impl/01_tasks.md を phase-3-impl-plan/07_file_task_division.md から生成
    → 事前準備:
      ・外部リポに per-worker worktree を作成（impl/<施策名>-W<N> ブランチ）
      ・per-worker 課題ファイル（07_issues_W<N>.md）を作成
      ・per-worker ワークログ（phase-4-impl/02_work_log_W<N>.md）をテンプレートからコピーし既知値を事前記入
      ・事前検証チェックリストを実行
    → Wave 1: 依存関係なしの IMPL-XXX を並列ディスパッチ
      各 impl-worker: worktree パスでコード実装 → テスト（max 3 リトライ）
                      → テンプレート事前配置済みのセクションを埋める形でチェックポイント記録（phase-4-impl/02_work_log_W<N>.md）
                      → 課題起票（07_issues_W<N>.md）
                      → ワーカー完了チェックリスト記録
                      → COMPLETE or ESCALATE
    → Wave 完了後処理:
      ・事後検証チェックリスト実行
      ・per-worker ブランチを施策ブランチにマージ（--no-ff）
      ・マージ後テスト実行
      ・per-worker 課題を 07_issues.md に統合
      ・worktree クリーンアップ
    → [Wave N: 依存解消後に追加ディスパッチ]
    → B+C 集約: git log（per-worker ブランチ含む）+ 全 work_log から phase-4-impl/03_work_report.md 構築
      ※ 事後検証で復元したチェックポイントは [RECONSTRUCTED] マーク付き、復元件数を Reconstruction Count に記録
    → impl-evaluator ディスパッチ Phase 4（成果物: phase-4-impl/04, 05）
      ※ Phase 4 追加評価項目: per-worker マージ完了・マージ後テスト・範囲外変更なし・課題統合完了
    → phase-4-impl/06_gate.md にゲート判定
                                                                    |
  Gate Summary + クローズ
    → 08_gate_summary.md（4フェーズの総括）
    → 知見集約・ルーティング
    → アーカイブ移動 → コミット・push → PR 作成
```

### 4フェーズ構成

| Phase | 目的 | プライマリ成果物 | ワーカー |
|-------|------|----------------|---------|
| 1: Investigation | コードベース調査 | phase-1-investigation/03_work_report.md | investigation-worker |
| 2: Design | 設計ドキュメント作成 | 02_impl_design.md | design-worker |
| 3: Implementation Planning | ファイルレベルタスク分割 | phase-3-impl-plan/07_file_task_division.md | impl-plan-worker |
| 4: Implementation | コード実装 | phase-4-impl/03_work_report.md (B+C集約) | impl-worker (並列) |

### B+C 作業ログ集約

- **B (マネージャー集約)**: `git -C <external-repo> log --oneline impl/<branch>` + per-worker ブランチの git log + 全 `phase-4-impl/02_work_log_W*.md` + 全 `07_issues_W*.md` を読み、`phase-4-impl/03_work_report.md` を構築
- **C (ワーカーチェックポイント)**: 各 impl-worker が START / TEST-RUN-N (PASS/FAIL) / COMPLETE / ESCALATE を `phase-4-impl/02_work_log_W<N>.md` に記録

### セッションディレクトリ

`sessions/impl/<施策名>/` を使用（`sessions/initiatives/` とは別ディレクトリ）

### ファイル番号体系

| ディレクトリ | フェーズ | 主要ファイル |
|-------------|---------|-----------|
| ルート直下 | Global | 00_proposal, 01_plan, 02_impl_design, 07_issues, 08_gate_summary |
| phase-1-investigation/ | Phase 1 (Investigation) | 01_tasks, 02_work_log, 03_work_report, 04_eval_plan, 05_eval_report, 06_gate |
| phase-2-design/ | Phase 2 (Design) | 01_tasks, 02_work_log, 03_work_report, 04_eval_plan, 05_eval_report, 06_gate |
| phase-3-impl-plan/ | Phase 3 (Impl Planning) | 01_tasks, 02_work_log, 03_work_report, 04_eval_plan, 05_eval_report, 06_gate, 07_file_task_division |
| phase-4-impl/ | Phase 4 (Implementation) | 01_tasks, 03_work_report (B+C), 04_eval_plan, 05_eval_report, 06_gate + 動的 02_work_log_W<N> |

---

## トリアージセッション フロー

```
0. ブランチ整理  → SessionStart hook（.claude/hooks/session-start-branch-cleanup.sh）により自動実行
                   → 現在ブランチ確認 → 未プッシュあれば push → PR未作成なら作成
                   → main に切り替え・最新化してから作業フローへ
                   ※ hook の出力（JSON）を確認し、エラーや警告があればユーザーに報告する
1. 事前調査      → sessions/triage/YYYYMMDD/00_pre_investigation.md を埋める
                   【必須走査項目】
                   ・inbox / backlog / CSV / initiative の現状把握
                   ・inbox/ の未処理エントリ確認（セッション終了時の気づきを含む）
                   ・**ルール・workflow 整合性チェック（必須）**:
                     `.claude/skills/` 配下のスキル・エージェント定義と `docs/workflow.md` を突合し、記述の乖離を確認する
                     → 軽微な乖離はそのセッション内で修正する
                     → 大きな乖離は CSV に起票して次回以降に対応
                   ・**README 整合性チェック（必須、SDK / CLI 共通）**:
                     `README.md` のディレクトリ構成図・セッション種別テーブル・スキル定義テーブル・ドキュメントマップが実態と一致しているかを確認する
                     → 軽微なズレはそのセッション内で修正する
                     → 大きな乖離は CSV に起票して次回以降に対応
                   ・refs/ の孤立エントリ確認（inbox/ref_*.md が存在しないエントリ）
                     → 発見したらユーザーに内容と扱いを確認する
                     → ユーザーの回答をもとに inbox/ref_<名前>.md を新規作成
                        （概要 + 今後の扱い方針: 施策化検討 / 参照のみ保持 / 削除 を記載）
                     → refs/ の本体は削除しない（扱いは別途判断）
2. 実施計画作成  → sessions/triage/YYYYMMDD/01_plan.md を作成
                   （今回の重点・走査タスクを決める）
                   ・走査ボリューム（inbox + backlog + CSV 対象件数の合計）をもとにフェーズ別セット数を決定
                     ≤20件→全フェーズ1セット逐次 / 21〜50件→フェーズ別分割 / 51件以上→各フェーズ最大2セット
                   ・1セットあたり TG タスク 3件以下を目安とする
3. フェーズゲート構造に従いワーカーセットをディスパッチ
   【Phase 1: 状態収集】（TG-001, TG-003, TG-004, TG-007 — 全タスク独立、並列可）
                   3a. triage-worker をサブエージェントとして起動
                       → inbox / CSV / initiative / 気づきエントリを走査
                   3b. ワーカー完了後、triage-evaluator を起動 → 06_eval_report.md を作成
                   ※ Phase 1 ゲート: 全タスクの scan_report セクション完成を確認

   【Phase 2a: 突合・整合性】（TG-002, TG-006, TG-008 — 独立、Phase 1 完了後）
                       ・backlog 施策化済みチェック（TG-002）:
                         各 backlog エントリを sessions/initiatives/ + _archive/ と突合
                         → 削除・クローズ候補をレポートに記載
                       ・ルール・workflow 整合性チェック（TG-006）:
                         スキル定義と docs/workflow.md、README 整合性チェック、
                         参考資料（ドラフト）ステータスチェックを実施
                       ・セッション構造標準ポリシーチェック（TG-008、条件付き）:
                         前回以降に skills/agents に変更がある場合のみ実施
                   ※ Phase 2a ゲート: TG-002 の削除/統合候補リスト確定

   【Phase 2b: 関係性分析】（TG-005 — TG-002 に依存、Phase 2a 完了後）
                       ・backlog 関係性分析（TG-005）: backlog アイテム間の関係性を横断分析
                         → 重複候補・依存関係・統合候補を検出
                   ※ Phase 2b ゲート: 関係性テーブル完成

   【Phase 2c: リスク評価】（TG-009 — 条件付き、Phase 2b 完了後）
                       ・情報欠損リスク評価（TG-009）【条件付き実行】:
                         走査結果に削除・統合候補がある場合のみ実施
                         → リスク評価テーブルを作成
                         → 削除・統合候補がない場合はスキップ

   【Phase 3: GHA整合性】（TG-010 — 独立）
                       ・GHA ↔ Skills 整合性チェック（TG-010）:
                         `.github/gha-skills-mapping.yml` のマニフェストに基づき
                         GHA プロンプト/ワークフローとスキル定義のドリフトを検出
                         → CRITICAL / WARNING / INFO でドリフト重大度を判定

                   ※ 各フェーズ内でセット分割する場合、セット内は worker → evaluator の逐次起動
                   ※ 低ボリューム時（≤20件）は全フェーズを1セットで逐次実行可
4. 作業履歴      → sessions/triage/YYYYMMDD/02_dispatch_log.md に記録
5. 結果集約      → 全セット完了後、各 set の scan_report + eval_report を集約
6. レポート作成  → sessions/triage/YYYYMMDD/03_report.md を作成（知見集約・課題集約セクションを含む）
7. ゲート判定    → sessions/triage/YYYYMMDD/04_gate_review.md を作成（知見ルーティング・横展開事項を含む）
8. アクション実施 → inbox処理・backlog作成/変更・ルール反映・CSV更新等を実施
9. 後処理        → 処理済み inbox アイテムを削除（git 履歴が証跡）
10. PR 作成      → 全タスク完了後にコミット・プッシュし、PR を作成
11. ユーザーレビュー → PR でまとめてレビュー・承認
```

> **課題起票の考え方**
> トリアージのワーカー・評価者は、発見した課題を `07_issues.md`（ワーカーセット別バッファ）に起票します。
> CSV への直接起票は行いません。マネージャーがレポート集約時に全セットの `07_issues.md` を確認し、
> 施策横断で再発しうる課題を `プロセス改善_課題管理.csv` に転記します。
> まだ判断できない粒度の粗いメモは `03_work_log.md` の「判断・気づき」欄に書いておき、
> 走査完了後に課題と確定したものだけ `07_issues.md` に起票してください。

---

## メタ認知セッション フロー

```
0. ブランチ整理  → SessionStart hook（.claude/hooks/session-start-branch-cleanup.sh）により自動実行
                   → 現在ブランチ確認 → 未プッシュあれば push → PR未作成なら作成
                   → main に切り替え・最新化してから作業フローへ
                   ※ hook の出力（JSON）を確認し、エラーや警告があればユーザーに報告する
1. 事前調査      → sessions/metacognition/YYYYMMDD/00_pre_investigation.md を埋める
                   【必須走査項目】
                   ・sessions/initiatives/_archive/ 内の施策確認
                   ・プロセス改善_課題管理.csv の現状把握
                   ・過去の 08_gate_review.md の横展開セクション確認
                   ・過去の 04_work_report.md / 06_eval_report.md の知見セクション確認
2. 実施計画作成  → sessions/metacognition/YYYYMMDD/01_plan.md を作成
                   （今回の重点・MC タスク選定・ワーカー割り当てを決める）
3. ワーカーセット作成・ディスパッチ
                   3a. metacognition-worker をサブエージェントとして起動
                       → MC タスクを実行（下記 MC タスク一覧参照）
                       → 04_scan_report.md に構造化された分析結果を作成
                   3b. ワーカー完了後、metacognition-evaluator をサブエージェントとして起動
                       → ワーカーの分析結果を評価（完全性・分析品質・エビデンス品質）
                       → 06_eval_report.md を作成
                   ※ セット内は worker → evaluator の逐次起動（並列起動禁止）
4. 作業履歴      → sessions/metacognition/YYYYMMDD/02_dispatch_log.md に記録
5. 結果集約      → 全セット完了後、各 set の scan_report + eval_report を集約
6. レポート作成  → sessions/metacognition/YYYYMMDD/03_report.md を作成（知見集約・課題集約セクションを含む）
7. ゲート判定    → sessions/metacognition/YYYYMMDD/04_gate_review.md を作成（知見ルーティング・横展開事項を含む）
8. アクション実施 → 分析結果に基づくアクションを実施
                   ・アクション可能な洞察 → inbox/ に .md ファイルとして起票
                   ・明確な課題 → プロセス改善_課題管理.csv に直接転記
                   ・明確な施策候補 → backlog/entries/ に .md ファイルとして作成
9. PR 作成      → 全タスク完了後にコミット・プッシュし、PR を作成
10. ユーザーレビュー → PR でまとめてレビュー・承認
```

### MC タスク一覧

| ID | 名称 | スキャン対象 | 目的 |
|----|------|------------|------|
| MC-001 | 施策横断の知見パターン抽出 | `_archive/*/04_work_report.md`, `06_eval_report.md` の知見セクション | 反復する知見パターンの検出 |
| MC-002 | ゲートレビュー引継ぎ追跡 | `_archive/*/08_gate_review.md` の横展開セクション | ルーティング宣言の実行漏れ検出 |
| MC-003 | 課題パターン分析 | `プロセス改善_課題管理.csv` | 再発カテゴリ・停滞課題の検出 |
| MC-004 | プロセス効率分析 | `_archive/*/01_plan.md` + `04_work_report.md` | 計画対実績の乖離パターン |
| MC-005 | ルーティング実行追跡 | gate_review ルーティング宣言 vs inbox/backlog/CSV 実態 | 宣言済み未実行の検出 |

### triage との責務の違い

- **triage**: inbox/backlog/CSV の日常的なハウスキーピング + ルール準拠チェック
- **metacognition**: 過去の施策アーカイブを横断的に分析し、反復パターン・未回収知見・プロセス効率を評価する「振り返り」セッション

> **課題起票の考え方**
> メタ認知のワーカー・評価者は、発見した課題を `07_issues.md`（ワーカーセット別バッファ）に起票します。
> CSV への直接起票は行いません。マネージャーがレポート集約時に全セットの `07_issues.md` を確認し、
> 施策横断で再発しうる課題を `プロセス改善_課題管理.csv` に転記します。

---

## バックログメンテナンスセッション フロー

```
0. ブランチ整理  → SessionStart hook（.claude/hooks/session-start-branch-cleanup.sh）により自動実行
                   → 現在ブランチ確認 → 未プッシュあれば push → PR未作成なら作成
                   → main に切り替え・最新化してから作業フローへ
                   ※ hook の出力（JSON）を確認し、エラーや警告があればユーザーに報告する
1. 事前調査      → sessions/backlog-maintenance/YYYYMMDD/00_pre_investigation.md を埋める
                   【必須走査項目】
                   ・backlog/entries/ 内の全エントリの起票日・優先度・ステータス確認
                   ・backlog/backlog.csv とファイル実体の整合性確認
                   ・sessions/initiatives/ および _archive/ の施策状況確認
                   ・プロセス改善_課題管理.csv の関連課題確認
2. 実施計画作成  → sessions/backlog-maintenance/YYYYMMDD/01_plan.md を作成
                   （今回の重点・BM タスク選定・ワーカー割り当てを決める）
                   ・backlog エントリ数をもとにセット数を決定
                     ≤10件→1セット / 11〜25件→2セット / >25件→3セット
3. ワーカーセット作成・ディスパッチ
                   3a. backlog-maintenance-worker をサブエージェントとして起動
                       → BM タスクを実行（下記 BM タスク一覧参照）
                       → 04_scan_report.md に構造化された走査結果を作成
                   3b. ワーカー完了後、backlog-maintenance-evaluator をサブエージェントとして起動
                       → ワーカーの走査結果を評価（完全性・判断品質・エビデンス品質）
                       → 06_eval_report.md を作成
                   ※ セット内は worker → evaluator の逐次起動（並列起動禁止）
4. 作業履歴      → sessions/backlog-maintenance/YYYYMMDD/02_dispatch_log.md に記録
5. 結果集約      → 全セット完了後、各 set の scan_report + eval_report を集約
6. レポート作成  → sessions/backlog-maintenance/YYYYMMDD/03_report.md を作成（知見集約・課題集約セクションを含む）
7. ゲート判定    → sessions/backlog-maintenance/YYYYMMDD/04_gate_review.md を作成（知見ルーティング・横展開事項を含む）
8. アクション実施 → レポートに基づくアクションを実施
                   ・削除・クローズ候補 → ユーザー承認後に backlog から削除
                   ・優先度変更候補 → ユーザー承認後に backlog を更新
                   ・統合候補 → ユーザー承認後に backlog エントリを統合
9. PR 作成      → 全タスク完了後にコミット・プッシュし、PR を作成
10. ユーザーレビュー → PR でまとめてレビュー・承認
```

### BM タスク一覧

| ID | 名称 | スキャン対象 | 目的 |
|----|------|------------|------|
| BM-001 | 長期滞留エントリの検出 | `backlog/entries/*.md` の起票日 | 起票日からの経過日数をチェックし、長期滞留（90日以上）のエントリを検出 |
| BM-002 | 関連施策での解決状況確認 | `backlog/entries/*.md` vs `_archive/` | アーカイブ済み施策で解消された backlog エントリを検出 |
| BM-003 | 前提条件の変化チェック | `backlog/entries/*.md` の背景・前提 | 環境変化・依存施策の状況変化により前提が崩れたエントリを検出 |
| BM-004 | 優先度の妥当性レビュー | `backlog/entries/*.md` の優先度 | 起票時の優先度が現状と乖離しているエントリを検出し、再評価 |
| BM-005 | 重複・統合候補の検出 | `backlog/entries/*.md` 横断比較 | 類似する backlog エントリを検出し、統合提案 |

### triage との責務の違い

- **triage（TG-002）**: backlog の状態確認が主目的。全項目のステータスチェックに走査時間を割く
- **backlog-maintenance**: backlog エントリの陳腐化を深掘り分析する専用セッション（前提変化の追跡・解決済み判定・優先度再評価・重複統合）

> **課題起票の考え方**
> バックログメンテナンスのワーカー・評価者は、発見した課題を `07_issues.md`（ワーカーセット別バッファ）に起票します。
> CSV への直接起票は行いません。マネージャーがレポート集約時に全セットの `07_issues.md` を確認し、
> 施策横断で再発しうる課題を `プロセス改善_課題管理.csv` に転記します。

---

## 自動施策化フロー（GitHub Actions）

> **正の情報源**: `.github/workflows/backlog-candidate-propose.yml`, `.github/workflows/backlog-auto-execute.yml`

低優先度バックログ項目を GitHub Actions で自動施策化する2フェーズアーキテクチャ。人間の承認を挟むことで安全性を確保しつつ、滞留する低優先度項目の消化を自動化する。

### 対象条件

- 優先度: 低
- ステータス: 候補
- 対象リポジトリ: dev-process-improvement

### 2フェーズアーキテクチャ

```
Phase 1: backlog-candidate-propose.yml (cron: 3時間ごと / workflow_dispatch)
  1. 承認待ち Issue（auto-initiative-pending ラベル）の存在チェック → 既にあればスキップ
  2. backlog.csv をパースし、対象条件に合致する最古の1件を選択
  3. GitHub Issue を自動作成（auto-initiative-pending ラベル付き）
                              |
                    人間が Issue を確認
                    → 承認: auto-initiative-approved ラベルを付与
                    → 却下: Issue をクローズ
                              |
Phase 2: backlog-auto-execute.yml (on: issues - labeled)
  トリガー条件: auto-initiative-approved ラベル付与 AND auto-initiative-pending ラベル存在
  1. Issue title から施策名を抽出
  2. anthropics/claude-code-action@v1 で L1 フローを非対話実行
     - _template コピー → proposal/plan/tasks 作成
     - L2-worker 実行 → L2-evaluator 実行
     - gate_review 作成 → backlog エントリ削除
  3. Issue クローズ（auto-initiative-done ラベル付与）
```

### ラベルフロー

| ラベル | 付与タイミング | 意味 |
|--------|-------------|------|
| `auto-initiative-pending` | Phase 1 で Issue 作成時 | 承認待ち |
| `auto-initiative-approved` | 人間が承認時 | 実行許可 |
| `auto-initiative-done` | Phase 2 完了時 | 施策化完了 |

### 手動設定（施策完了後に必要）

- **Secrets**: `ANTHROPIC_API_KEY` を GitHub Actions secrets に追加
- **Labels**: 上記3ラベルをリポジトリに作成

---

## GHA Initiative スキル

> **正の情報源**: `.claude/skills/gha-wallbash/SKILL.md`, `.claude/skills/gha-execute/SKILL.md`, `.claude/skills/gha-close/SKILL.md`, `.claude/skills/gha-question/SKILL.md`

GitHub Actions の initiative ワークフローから Claude Code を起動する際に使用する GHA 専用スキル。CLI 対話セッション用のスキル（l1-manager 等）とは分離されており、各ワークフローに1:1で対応する。

### スキル一覧

| スキル | 対応ワークフロー | 責務 | 読み書き |
|--------|----------------|------|---------|
| `gha-wallbash` | `initiative-wallbash.yml` | 壁打ちフェーズ（init: テンプレートコピー・ドラフト作成 / continue: フィードバック反映・ドラフト更新） | 読み書き |
| `gha-execute` | `initiative-execute.yml` | 実行フェーズ（approve: 計画〜ゲート判定 / reject: 差し戻し修正） | 読み書き |
| `gha-close` | `initiative-close.yml` | クローズフェーズ（知見ルーティング・アーカイブ移動） | 読み書き |
| `gha-question` | `initiative-question.yml` | 質問回答（施策ファイルの読み取り専用） | 読み取り専用 |

### GHA Initiative フロー

```
/start（Issue コメント）
  → dispatcher: initiative-wallbash.yml を mode=init で dispatch
  → wallbash (init): テンプレートコピー + 00_proposal, 01_plan, 02_tasks のドラフト作成
                      + 00a_wallbash_log.md に Round 1 記録
                      + 施策ブランチ作成・コミット・プッシュ
                      + 壁打ちサマリーを Issue コメントに投稿
  → [Issue コメントでレビュー]

/continue <feedback>（Issue コメント、何度でも繰り返し可能）
  → dispatcher: initiative-wallbash.yml を mode=continue で dispatch
  → wallbash (continue): 00a_wallbash_log.md からコンテキスト復元
                          → フィードバック反映 → ドラフト更新
                          → 00a_wallbash_log.md に Round N 追記
  → [Issue コメントでレビュー]

/approve [feedback]（Issue コメント）
  → dispatcher: initiative-execute.yml を dispatch
  → execute: PR 作成 → 壁打ちドラフトを活用して計画・タスク最終化
             → L2-worker → L2-evaluator → ゲート判定
             → ゲート判定サマリーを Issue コメントに投稿
  → [ゲート判定レビュー]

/approve（ゲート判定後）
  → dispatcher: initiative-close.yml を dispatch
  → close: 知見ルーティング → アーカイブ移動
```

#### 壁打ちフェーズの成果物

| ファイル | 説明 |
|---------|------|
| `00_proposal.md` | 提案書ドラフト |
| `01_plan.md` | 実施計画ドラフト |
| `02_tasks.md` | タスクリストドラフト |
| `00a_wallbash_log.md` | 壁打ちログ（コンテキスト保持: 現在の合意事項 + イテレーション履歴） |

#### コンテキスト保持の仕組み

`00a_wallbash_log.md` は2つのセクションで構成される:
- **現在の合意事項**: 毎回上書き。continue モードでの読み込み対象
- **イテレーション履歴**: 追記。各ラウンドの入力・調査・更新内容を記録

### 設計方針

- 各スキルは `user-invocable: false` で、GHA ワークフローからのみ使用される
- ワークフロー YAML の `prompt:` にはスキルファイルの Read 指示 + 動的コンテキスト（Issue 番号、ブランチ名等）のみを記載する
- スキルファイル内で「CLAUDE.md や l1-manager のルールには従わない」旨を明記し、スコープ制御問題（knowledge.md #7, #8）に対処する
- 権限設計の詳細は `.claude/skills/gha-guideline/SKILL.md` セクション5を参照
- CLI セッションスキルを GHA スキルに変換する際の手順は `.claude/skills/gha-guideline/SKILL.md` セクション7を参照

---

## オートメーションメンテナンスセッション フロー

```
0. ブランチ整理  → SessionStart hook（.claude/hooks/session-start-branch-cleanup.sh）により自動実行
                   → 現在ブランチ確認 → 未プッシュあれば push → PR未作成なら作成
                   → main に切り替え・最新化してから作業フローへ
                   ※ hook の出力（JSON）を確認し、エラーや警告があればユーザーに報告する
1. 事前調査      → sessions/automation/YYYYMMDD/00_pre_investigation.md を埋める
                   【必須走査項目】
                   ・automation-candidates/entries/ 内の全エントリのステータス・優先度スコア・最終評価日確認
                   ・automation-candidates/automation-candidates.csv とファイル実体の整合性確認
                   ・.claude/skills/、.claude/rules/ の追加・変更状況確認
                   ・backlog/entries/ 内の自動化関連エントリ確認
                   ・sessions/initiatives/ および _archive/ の自動化関連施策状況確認
                   ・プロセス改善_課題管理.csv の関連課題確認
2. 実施計画作成  → sessions/automation/YYYYMMDD/01_plan.md を作成
                   （今回の重点・AT タスク選定・ワーカー割り当てを決める）
                   ・automation-candidates エントリ数をもとにセット数を決定
                     ≤15件→1セット / 16〜30件→2セット / >30件→3セット
3. ワーカーセット作成・ディスパッチ
                   3a. automation-worker をサブエージェントとして起動
                       → AT タスクを実行（下記 AT タスク一覧参照）
                       → 04_scan_report.md に構造化された走査結果を作成
                   3b. ワーカー完了後、automation-evaluator をサブエージェントとして起動
                       → ワーカーの走査結果を評価（完全性・判断品質・エビデンス品質）
                       → 06_eval_report.md を作成
                   ※ セット内は worker → evaluator の逐次起動（並列起動禁止）
4. 作業履歴      → sessions/automation/YYYYMMDD/02_dispatch_log.md に記録
5. 結果集約      → 全セット完了後、各 set の scan_report + eval_report を集約
6. レポート作成  → sessions/automation/YYYYMMDD/03_report.md を作成（知見集約・課題集約セクションを含む）
7. ゲート判定    → sessions/automation/YYYYMMDD/04_gate_review.md を作成（知見ルーティング・横展開事項を含む）
8. アクション実施 → レポートに基づくアクションを実施
                   ・新規候補登録 → automation-candidates/entries/ に追加、CSV に行を追加
                   ・ステータス変更 → automation-candidates CSV + entries を更新
                   ・優先度変更 → automation-candidates CSV + entries を更新
                   ・backlog 起票提案 → backlog/entries/ に作成、backlog.csv に行を追加
                   ・知見ルーティング → inbox/*.md にアクション可能な洞察を起票
                   ・課題 CSV 転記 → プロセス改善_課題管理.csv に転記
9. PR 作成      → 全タスク完了後にコミット・プッシュし、PR を作成
10. ユーザーレビュー → PR でまとめてレビュー・承認
```

### AT タスク一覧

| ID | 名称 | スキャン対象 | 目的 |
|----|------|------------|------|
| AT-001 | 新規自動化候補スキャン | `.claude/skills/`, `.claude/rules/`, `sessions/*/`, `docs/` | skills/rules/テンプレートの追加・変更に伴い新たに生まれた定型作業を検出 |
| AT-002 | 既存候補の再評価 | `automation-candidates/entries/*.md`, CSV | 優先度スコア・実装難易度・自動化手段の妥当性を環境変化に基づき再評価 |
| AT-003 | 実装進捗確認 | `backlog/entries/*.md`, `sessions/initiatives/`, `_archive/` | backlog 起票済み候補の施策化・実装状況を追跡 |
| AT-004 | backlog 起票提案 | AT-001〜AT-003 の結果 | 新規候補や優先度変更候補を backlog エントリとして起票提案 |

### triage・backlog-maintenance との責務の違い

- **triage**: inbox/backlog/CSV の日常的なハウスキーピング + ルール準拠チェック
- **backlog-maintenance**: backlog エントリの陳腐化を深掘り分析する専用セッション
- **automation**: skills/rules/テンプレートの定型作業を走査し、自動化候補の発見・再評価・進捗追跡を行う専用セッション

> **課題起票の考え方**
> オートメーションのワーカー・評価者は、発見した課題を `07_issues.md`（ワーカーセット別バッファ）に起票します。
> CSV への直接起票は行いません。マネージャーがレポート集約時に全セットの `07_issues.md` を確認し、
> 施策横断で再発しうる課題を `プロセス改善_課題管理.csv` に転記します。

---

## config最適化セッション フロー

```
[config-optimizer-manager]
  ブランチ整理: SessionStart hook により自動実行
                                                                    |
  入力: config-optimize / config-optimize-continue: <パス>
                                                                    |
  事前調査: sessions/config-optimization/YYYYMMDD/00_pre_investigation.md
    - .claude/ 構造サーベイ（settings.json, rules, skills, hooks, CLAUDE.md）
    - リファレンススナップショット鮮度確認
    - 過去セッション確認
                                                                    |
  計画: 01_plan.md
    - CO ターゲット（CO-001〜CO-008）のスコープ決定
    - フェーズ計画作成
                                                                    |
  Phase 1: 情報収集 ─────────────────────────────────────────────────
    タスク作成: workers/set-1/01_tasks.md                            |
    ワーカー: config-collection-worker（WebSearch/WebFetch）          |
      → reference/claude-code-config-reference.md を更新             |
      → workers/set-1/04_scan_report.md を作成                       |
    評価者: config-optimizer-evaluator（Phase 1 コンテキスト）        |
    ゲート: phase-1-collection/01_gate.md                             |
                                                                    |
  Phase 2: 現状分析 ─────────────────────────────────────────────────
    タスク作成: workers/set-2/01_tasks.md                            |
    ワーカー: config-analysis-worker                                 |
      → .claude/ 全体をリファレンスと比較分析                        |
      → workers/set-2/04_scan_report.md を作成                       |
    評価者: config-optimizer-evaluator（Phase 2 コンテキスト）        |
    ゲート: phase-2-analysis/01_gate.md                               |
                                                                    |
  Phase 3: 最適化提案 ───────────────────────────────────────────────
    タスク作成: workers/set-3/01_tasks.md                            |
    ワーカー: config-proposal-worker                                 |
      → Impact × Effort 優先順位付き提案を作成                      |
      → workers/set-3/04_scan_report.md を作成                       |
    評価者: config-optimizer-evaluator（Phase 3 コンテキスト）        |
    ゲート: phase-3-proposal/01_gate.md                               |
                                                                    |
  集約: 03_report.md                                                 |
    - フェーズ別結果マージ                                           |
    - 知見集約（§5）、課題集約（§6）                                 |
  最終ゲート: 04_gate_review.md                                      |
                                                                    |
  アクション:                                                        |
    高優先度提案 → backlog/entries/                                  |
    洞察 → inbox/                                                    |
    課題 → プロセス改善_課題管理.csv                                  |
                                                                    |
  コミット・プッシュ・PR 作成
```

> **CO ターゲット（最適化対象）**
> CO-001: settings.json / CO-002: rules / CO-003: skills / CO-004: hooks / CO-005: CLAUDE.md / CO-006: プラグイン / CO-007: その他（memory, sandbox 等） / CO-008: スキル/プラグイン機能重複

> **3フェーズ構成**
> Phase 1（情報収集）の collection-worker のみ WebSearch/WebFetch ツールを使用します。
> Phase 2（現状分析）は .claude/ 全体をリファレンスと比較し、Phase 3（最適化提案）は分析結果から優先順位付き提案を作成します。
> 単一 evaluator（config-optimizer-evaluator）が全フェーズを評価します。

---

## セッション一貫性チェックセッション フロー

```
[session-consistency-manager]
  ブランチ整理: SessionStart hook により自動実行
                                                                    |
  入力: session-consistency / session-consistency-continue: <パス>
                                                                    |
  事前調査: sessions/session-consistency/YYYYMMDD/00_pre_investigation.md
    - .claude/skills/ 配下の全セッション定義サーベイ
    - triage-standard-policy / session-flow-policy / manager-common-policy の現状確認
    - 過去セッション確認
                                                                    |
  計画: 01_plan.md
    - SC ターゲット（SC-001〜SC-008）のスコープ決定
    - フェーズ計画作成
                                                                    |
  Phase 1: 情報収集 ─────────────────────────────────────────────────
    タスク作成: workers/set-1/01_tasks.md                            |
    ワーカー: sc-collection-worker                                   |
      → reference/session-consistency-reference.md を更新             |
      → workers/set-1/04_scan_report.md を作成                       |
    評価者: sc-evaluator（Phase 1 コンテキスト）                      |
    ゲート: phase-1-collection/01_gate.md                             |
                                                                    |
  Phase 2: 現状分析 ─────────────────────────────────────────────────
    タスク作成: workers/set-2/01_tasks.md                            |
    ワーカー: sc-analysis-worker                                     |
      → セッション定義をリファレンスと比較分析                        |
      → workers/set-2/04_scan_report.md を作成                       |
    評価者: sc-evaluator（Phase 2 コンテキスト）                      |
    ゲート: phase-2-analysis/01_gate.md                               |
                                                                    |
  Phase 3: 改善提案 ───────────────────────────────────────────────
    タスク作成: workers/set-3/01_tasks.md                            |
    ワーカー: sc-proposal-worker                                     |
      → Impact × Effort 優先順位付き提案を作成                      |
      → workers/set-3/04_scan_report.md を作成                       |
    評価者: sc-evaluator（Phase 3 コンテキスト）                      |
    ゲート: phase-3-proposal/01_gate.md                               |
                                                                    |
  集約: 03_report.md                                                 |
    - フェーズ別結果マージ                                           |
    - 知見集約（§5）、課題集約（§6）                                 |
  最終ゲート: 04_gate_review.md                                      |
                                                                    |
  アクション:                                                        |
    高優先度提案 → backlog/entries/                                  |
    洞察 → inbox/                                                    |
    課題 → プロセス改善_課題管理.csv                                  |
                                                                    |
  コミット・プッシュ・PR 作成
```

> **SC ターゲット（チェック対象）**
> SC-001: SKILL.md 必須セクション / SC-002: エージェント必須セクション / SC-003: ペアリング対称性 / SC-004: テンプレート完備性 / SC-005: 相互参照整合性 / SC-006: ポリシー準拠 / SC-007: コミットメッセージ規約 / SC-008: ドキュメント反映

> **3フェーズ構成**
> Phase 1（情報収集）で全セッション定義を収集し reference を更新、Phase 2（現状分析）で SC ターゲット別にギャップを分析、Phase 3（改善提案）で分析結果から優先順位付き提案を作成します。
> 単一 evaluator（sc-evaluator）が全フェーズを評価します。

> **TG-008 との関係**
> TG-008（トリアージのセッション構造チェック）とは完全独立。TG-008 はトリアージセッション内の走査項目であり、session-consistency は専用マネージャーセッションとして深掘りチェックを行います。

---

## リポジトリ間同期セッション フロー

```
[sync-manager]
  ブランチ整理: SessionStart hook（.claude/hooks/session-start-branch-cleanup.sh）により自動実行
                                                                    |
  入力: sync: <target-repo> [<direction>]
                                                                    |
  1. セッションフォルダ作成  → sessions/sync/YYYYMMDD/ にテンプレートをコピー
  2. 事前調査              → 00_pre_investigation.md（両リポジトリの現状把握・同期対象の特定）
  3. 同期計画作成          → 01_plan.md（同期方向・対象ファイル・成功基準）
                                                                    |
[sync-worker] ← sync-manager が Task ツールでサブエージェントとして起動
  壁打ちフェーズ → 03_work_log.md に記録
  → repo-sync-checklist セクション1〜4 に従い同期作業を実施
  → 同期先リポジトリで変更をコミット・プッシュ（ブランチ: sync/YYYYMMDD）
  → 04_sync_report.md を作成（知見セクション・同期先コミット情報への記載を含む）
  ※ 課題発見時: 07_issues.md に起票
                                                                    |
  sync-manager: worker 成果物を確認 → 品質不十分なら差し戻し
                                                                    |
[sync-evaluator] ← sync-manager が Task ツールでサブエージェントとして起動（worker 完了後に起動）
  壁打ちフェーズ → 05_eval_plan.md に記録
  → repo-sync-checklist セクション5 の7つの検証観点で同期結果を評価
  → 06_eval_report.md を作成（知見セクションへの記載を含む）
  → 課題があれば 07_issues.md に起票
                                                                    |
[sync-manager]
  04・06・07 を確認 → 08_gate_review.md にゲート判定を記入
    → 通過     : 同期完了
    → 条件付き : 修正作業を実施
    → 差し戻し : 計画修正 → worker に再ディスパッチ
                                                                    |
  コミット・push → PR 作成 → ユーザーレビュー
```

### 同期セッションのファイルオーナーシップ

| ファイル | sync-manager | sync-worker | sync-evaluator |
|---------|:------------:|:-----------:|:--------------:|
| 00_pre_investigation.md | ✏️ 作成・編集 | 👁️ 読取 | 👁️ 読取 |
| 01_plan.md | ✏️ 作成・編集 | 👁️ 読取 | 👁️ 読取 |
| 02_dispatch_log.md | ✏️ 追記 | - | - |
| 03_work_log.md | 👁️ 読取 | ✏️ 作成・編集 | 👁️ 読取 |
| 04_sync_report.md | 👁️ 読取 | ✏️ 作成・編集 | 👁️ 読取 |
| 05_eval_plan.md | 👁️ 読取 | - | ✏️ 作成・編集 |
| 06_eval_report.md | 👁️ 読取 | - | ✏️ 作成・編集 |
| 07_issues.md | 📝 転記済みマーク追記 | ✏️ 起票 | ✏️ 起票 |
| 08_gate_review.md | ✏️ 作成・編集 | - | - |

---

## マネージャーセッション共通ポリシー

> **正の情報源**: `.claude/skills/manager-common-policy/SKILL.md`

8つのマネージャーセッション（l1-manager, triage-manager, metacognition-manager, sync-manager, backlog-maintenance-manager, automation-manager, config-optimizer-manager, session-consistency-manager）に共通する運用パターンを一元的に定義するポリシー。各マネージャースキルは固有ロジックを自身の SKILL.md に記載し、共通パターンは本ポリシーを参照する。

### ポリシー3層構造の位置づけ

```
session-flow-policy      ← 「構造」（新セッション作成時のテンプレート）
triage-standard-policy   ← 「ライフサイクル・ペアリング」（横断的整合性基準）
manager-common-policy    ← 「運用パターン」（マネージャーの共通手順）
```

3つは補完関係にあり、重複しない。

### 共通パターン一覧

| セクション | 内容 | 概要 |
|-----------|------|------|
| §1 | 適用対象 | l1, triage, metacognition, sync, backlog-maintenance, automation, config-optimizer, session-consistency の8マネージャー |
| §2 | ワーカーディスパッチパターン | 共通4項目（役割・場所・スコープ・完了定義）+ 順序制約（基本逐次） |
| §3 | 成果物確認観点 | 共通最小3項目（タスク分類・レポート記載・課題バッファ）+ 確認結果の `08_gate_review.md` 記録義務 |
| §4 | ゲート判定基準 | 通過 / 条件付き通過 / 差し戻しの3択 |
| §5 | 知見集約手順 | worker/evaluator の知見を集約 + ルーティング判断基準 |
| §6 | 課題集約手順 | 07_issues.md → CSV転記 → ISS-XXX.md |
| §7 | 差し戻し手順 | 成果物チェック → NG ならフィードバック・再起動 |
| §8 | セッションライフサイクル todo 登録 | ブランチ整理後・作業フロー前に TaskCreate でステップ登録、TaskUpdate で進捗追跡 |
| §9 | 関連ファイル一覧 | 8マネージャースキル + session-flow-policy + triage-standard-policy + workflow.md |
| §10 | ドメインエージェント参照 | refs/agency-agents/knowledge.md のカタログから施策タイプに適したエージェントを選定し、L2 に専門知識として参照させる（任意） |

各マネージャースキルは共通パターンを `manager-common-policy §N` の形式で参照し、固有のロジック（l1 のクローズ手順、triage の TG タスク等）は自身の SKILL.md に残す。各マネージャーは §8 に従い、セッション開始時に自身の作業フローステップを TaskCreate で登録し、TaskUpdate で進捗を追跡する。

---

## docs/ 文書分類ポリシー

> **正の情報源**: `CLAUDE.md`「ドキュメント整合性ルール > docs/ 文書分類」セクション

`docs/` 配下の文書は3カテゴリに分類され、カテゴリごとに管理ルールが異なる。

| カテゴリ | 管理ルール | 該当ファイル |
|---------|-----------|------------|
| 可視化文書 | ルール変更時に連動更新必須 | `workflow.md` |
| 運用ガイド | 独立管理（整合性チェック不要） | `management-system-guide.md`, `subagent-permission-guide.md`, `implementation.md` |
| 参考資料（ドラフト） | ステータスバナー必須。Skills 統合後に削除検討 | `coordination-protocol-guideline.md`, `git-worktree-guideline.md` |

- 新規 `docs/` ファイル作成時は `CLAUDE.md` の分類テーブルにカテゴリを追加すること
- トリアージセッションで参考資料のステータスバナーと統合状況の整合性を確認する

---

## ルール変更時の連動更新

> **正の情報源**: `.claude/skills/rule-change-checklist/SKILL.md`

`.claude/skills/` や `.claude/rules/` 配下のファイルを変更する施策では、連動更新の漏れを防ぐために以下を確認する。

1. **関連ファイル一覧の確認**: 変更ファイルの「関連ファイル一覧」セクションを確認し、連動更新先を特定する
2. **docs/workflow.md の更新**: ルール変更後に本ファイルを更新する
3. **TG-008 基準の連動更新**: `triage-standard-policy/SKILL.md` のチェック基準に影響する場合は更新する
4. **テンプレートの連動更新**: `sessions/initiatives/_template/` や `sessions/triage/_template/` に影響がないか確認する

詳細な手順とチェックリストは `.claude/skills/rule-change-checklist/SKILL.md`（rule-change-checklist スキル）を参照。

---

## フォーマット変換時の同等性検証

> **正の情報源**: `.claude/skills/format-conversion-checklist/SKILL.md`

フォーマット変換（構造変更・形式変更）を行うタスクで、変換前後の内容同等性を検証するためのチェックリスト。dev-process-improvement / ai-driven-dev-patterns 両リポジトリに適用する。

### 省略可/不可の判断基準

**判断基準**: 「この要素がなくなった場合、読者は同じ作業を再現できるか？」

- **省略不可**: コード・コマンド例、数値・閾値、手順の順序・依存関係、条件分岐・例外処理、参照先・リンク、テーブルの全行、注意事項・禁止事項
- **省略可**: 装飾的な表現、冗長な繰り返し、メタ的なコメント、旧フォーマット固有の構造要素（変換先に置き換え済みの場合）

### 同等性検証手順（3ステップ）

1. **変換前の要素棚卸し**: 構造要素・コード例・参照・条件・データの数と内容を記録
2. **変換後の要素照合**: 棚卸し結果と突合し、全要素が保持されていることを確認
3. **差分の分類と判断**: フォーマット差異（許容）/ 意図的省略（許容）/ 意図しない欠落（不許容・復元）/ 内容変更（不許容・復元）

割合閾値は使用しない。変換時は常に全要素を検証する。

### 使い方

- **L1**: フォーマット変換タスクの完了条件に「format-conversion-checklist スキルに従い同等性検証が完了している」を含める
- **L2-worker**: フォーマット変換後、コミット前にチェックリストのステップ 1〜3 を実施し、検証記録テンプレートで結果を `03_work_log.md` に記録する
- **L2-evaluator**: 検証記録の存在・棚卸し結果の実態一致・省略不可要素の保持を評価する

詳細な手順・検証記録テンプレート・関連ファイル一覧は `.claude/skills/format-conversion-checklist/SKILL.md` を参照。

---

## ビルトイン Skills 評価リファレンス

> **正の情報源**: `.claude/skills/builtin-skills-reference/SKILL.md`

Claude Code に同梱されるビルトイン（バンドル）skills の、dev-process-improvement プロジェクトにおける適用可能性の評価結果。新規 skill の評価や、ビルトイン skill の利用判断時に参照する。

### 評価サマリー（2026-03-12 時点）

| Skill | 適用可能性 | 推奨利用場面 |
|-------|-----------|------------|
| `/simplify` | 低 | 本プロジェクトでの積極活用場面なし |
| `/batch` | 中 | `.claude/skills/` や `docs/` の大規模一括更新（条件付き） |
| `/debug` | 中 | セッション失敗・サブエージェント問題のアドホック診断 |
| `/loop` | 低 | 本プロジェクトでの積極活用場面なし |
| `/claude-api` | 対象外 | API 実装を含まないため適用場面なし |

### 総合方針

- **状況に応じて活用**: `/debug`（セッション問題診断）、`/batch`（大規模一括更新、文書間整合性が不要な場合のみ）
- **活用しない**: `/simplify`（コード主体向け）、`/loop`（長期セッション前提）、`/claude-api`（API 実装なし）

各 skill の詳細評価（機能概要・具体的利用シーン・制約事項）は `.claude/skills/builtin-skills-reference/SKILL.md` を参照。

---

## コミットメッセージ規約

> **正の情報源**: `.claude/rules/commit-message.md`

すべてのコミットは以下の形式に従う。

```
[<session-type>] <category>: <summary>
```

### セッション種別と category

| 作業種別 | session-type | category | 例 |
|---------|-------------|----------|-----|
| 施策作業 | `L1` / `L2-worker` / `L2-evaluator` | sessions/initiatives/ 配下のディレクトリ名 | `[L2-worker] commit-message-rules: ルールファイルを作成` |
| トリアージ（マネージャー） | `triage-mgr` | `YYYYMMDD` | `[triage-mgr] 20260305: 事前調査・ワーカー割り当て` |
| トリアージ（ワーカー） | `triage-worker` | `YYYYMMDD` | `[triage-worker] 20260305: set-1 inbox/CSV スキャン完了` |
| トリアージ（評価者） | `triage-eval` | `YYYYMMDD` | `[triage-eval] 20260305: set-1 評価レポート作成` |
| メタ認知（マネージャー） | `meta-mgr` | `YYYYMMDD` | `[meta-mgr] 20260308: 事前調査・ワーカー割り当て` |
| メタ認知（ワーカー） | `meta-worker` | `YYYYMMDD` | `[meta-worker] 20260308: set-1 MC-001/MC-002 分析完了` |
| メタ認知（評価者） | `meta-eval` | `YYYYMMDD` | `[meta-eval] 20260308: set-1 評価レポート作成` |
| リポジトリ同期（git レベル） | `sync` | 同期方向 | `[sync] upstream-to-origin: main ブランチを同期` |
| 同期セッション（マネージャー） | `sync-mgr` | `YYYYMMDD` | `[sync-mgr] 20260308: 事前調査・ワーカー割り当て` |
| 同期セッション（ワーカー） | `sync-worker` | `YYYYMMDD` | `[sync-worker] 20260308: 同期作業完了・レポート作成` |
| 同期セッション（評価者） | `sync-eval` | `YYYYMMDD` | `[sync-eval] 20260308: 評価レポート作成` |
| バックログメンテナンス（マネージャー） | `bm-mgr` | `YYYYMMDD` | `[bm-mgr] 20260310: 事前調査・ワーカー割り当て` |
| バックログメンテナンス（ワーカー） | `bm-worker` | `YYYYMMDD` | `[bm-worker] 20260310: set-1 BM-001〜BM-003 走査完了` |
| バックログメンテナンス（評価者） | `bm-eval` | `YYYYMMDD` | `[bm-eval] 20260310: set-1 評価レポート作成` |
| オートメーション（マネージャー） | `auto-mgr` | `YYYYMMDD` | `[auto-mgr] 20260313: 事前調査・ワーカー割り当て` |
| オートメーション（ワーカー） | `auto-worker` | `YYYYMMDD` | `[auto-worker] 20260313: set-1 AT-001〜AT-004 走査完了` |
| オートメーション（評価者） | `auto-eval` | `YYYYMMDD` | `[auto-eval] 20260313: set-1 評価レポート作成` |
| config最適化（マネージャー） | `co-mgr` | `YYYYMMDD` | `[co-mgr] 20260314: 事前調査・Phase 1 ワーカーディスパッチ` |
| config最適化（ワーカー） | `co-worker` | `YYYYMMDD` | `[co-worker] 20260314: Phase 1 情報収集完了・リファレンス更新` |
| config最適化（評価者） | `co-eval` | `YYYYMMDD` | `[co-eval] 20260314: Phase 2 評価レポート作成` |
| セッション一貫性（マネージャー） | `sc-mgr` | `YYYYMMDD` | `[sc-mgr] 20260316: 事前調査・Phase 1 ワーカーディスパッチ` |
| セッション一貫性（ワーカー） | `sc-worker` | `YYYYMMDD` | `[sc-worker] 20260316: Phase 1 情報収集完了・リファレンス更新` |
| セッション一貫性（評価者） | `sc-eval` | `YYYYMMDD` | `[sc-eval] 20260316: Phase 2 評価レポート作成` |
| 実装セッション（マネージャー） | `impl-mgr` | 施策名 | `[impl-mgr] feature-x: Phase 1 調査タスク作成` |
| 実装セッション（ワーカー） | `impl-worker` | 施策名 | `[impl-worker] feature-x: IMPL-001 実装完了` |
| 実装セッション（評価者） | `impl-evaluator` | 施策名 | `[impl-evaluator] feature-x: Phase 2 評価レポート作成` |
| 保守作業 | `maintenance` | 作業対象名 | `[maintenance] settings: deny ルールを追加` |

### 禁止事項

- `git push --force` の使用
- 意味のないコミットメッセージ（`update`, `fix`, `wip` 等のみ）
- `[session-type]` プレフィックスのないコミット
- category のないコミット

---

## ファイルのオーナーシップ

> 記号の凡例: ✏️ 作成・編集可 / 👁️ 読取のみ / ☑️ チェック更新のみ / 📝 判断・代理更新（条件付き）
>
> ※ `.claude/skills/` 配下の各スキル・エージェント定義では「担当ファイル」セクションにテキスト形式（「作成・編集」「読み取りのみ」「追記」等）で記載しています。上記の emoji 記号はこのワークフロー文書での表記であり、以下の対応関係で統一されています。
> - ✏️ = 作成・編集 / 追記・編集
> - 👁️ = 読み取りのみ
> - ☑️ = チェックボックス更新のみ（「読み取りのみ（チェックボックス更新は可）」に対応）
> - 📝 = 条件付き操作（詳細は脚注を参照）

| ファイル | L1 | L2(実施) | L2(評価) |
|---------|-----|---------|---------|
| 00_proposal.md | ✏️ 作成・編集 | 👁️ 読取 | 👁️ 読取 |
| 01_plan.md | ✏️ 作成・編集 | 👁️ 読取 | 👁️ 読取 |
| 02_tasks.md | ✏️ 作成・編集 | ☑️ チェック更新可 | 👁️ 読取 |
| 03_work_log.md | 👁️ 読取（判断根拠を末尾に追記可）*1 | ✏️ 作成・編集 | 👁️ 読取 |
| 04_work_report.md | 👁️ 読取 | ✏️ 作成・編集 | 👁️ 読取 |
| 05_eval_plan.md | 👁️ 読取 | 👁️ 読取 | ✏️ 作成・編集 |
| 06_eval_report.md | 👁️ 読取 | 👁️ 読取 | ✏️ 作成・編集 |
| 07_issues.md | 📝 転記判断・代理転記（resume 不可時のみ）*2 | ✏️ 一時メモ起票 | ✏️ 一時メモ起票 |
| 08_gate_review.md | ✏️ 作成・編集 | 👁️ 読取 | 👁️ 読取 |
| プロセス改善_課題管理.csv | ✏️ 対応方針確定・タスク化 | ✏️ 転記 | ✏️ 転記 |
| issues/entries/ISS-XXX.md | 📝 代理作成（resume 不可時のみ） | ✏️ 作成（CSV転記時） | ✏️ 作成（CSV転記時） |

*1: L1 の判断根拠（分岐の理由・起動の意思決定）は `03_work_log.md` の末尾に記録する（`skills/l1-manager/SKILL.md` 参照）。
*2: L1 が `07_issues.md` の CSV 転記を行うのは、L2-worker を resume できない場合（コンテキスト消失・セッション期限切れ等）に限る。通常は L2-worker を resume して転記を依頼する（`skills/l1-manager/SKILL.md` 参照）。


## 課題管理フロー

課題は以下の2つの管理単位で運用する。

| 管理単位 | 役割 | 格納先 |
|---------|------|--------|
| CSV（`プロセス改善_課題管理.csv`） | 全体俯瞰のハブ・インデックス | リポジトリルート |
| 課題詳細ファイル | CSV の1行では書ききれない詳細情報 | `issues/entries/ISS-XXX.md` |

> **inbox との使い分け**: `inbox/` は人間起票のアイデア・提案専用。AI が起票する課題は `issues/` + CSV に一元化する。

### 起票（L2 が行う）
1. 施策実施中に課題・知見・リスクを発見したら `07_issues.md` に一時メモを書く
2. 施策完了時または定期レビュー時に、施策をまたいで再発しうる課題を `プロセス改善_課題管理.csv` へ転記する
3. 転記時に `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する
4. 転記した項目は `07_issues.md` に `[転記済 ISS-XXX]` を記して削除する

### 対応方針確定・タスク化（L1 が行う）
1. CSV の `ステータス = 起票` の行を確認する
2. 対応するかどうかを判断し、`対応方針_確定` 列と `確定日` 列を埋める
3. タスク化する場合は `ステータス = タスク化済`、`タスク化先` 列に施策名・タスクIDを記入する
4. 対応しない場合は `ステータス = 対応不要` にして `備考` に理由を書く

### CSV の列定義

| 列名 | 説明 | 値の例 |
|------|------|--------|
| ID | ISS-001 から連番 | ISS-001 |
| 起票日 | YYYY-MM-DD | 2026-02-21 |
| カテゴリ | 課題の分類 | ツール / プロセス / ドキュメント / テンプレート |
| 種別 | 課題の性質 | 不具合 / 改善提案 / リスク / 知見 |
| タイトル | 1行のタイトル | - |
| 課題詳細 | 何が起きたか（3行以内推奨） | - |
| 対応方針_案 | 起票時点の案（`[案]` 接頭辞で未確定を明示） | [案] テンプレートに注意書きを追加する |
| ステータス | 対応状況 | 起票 / 方針確定 / タスク化済 / クローズ / 対応不要 |
| 優先度 | 高 / 中 / 低 | 中 |
| 関連施策 | 発生した施策名 | openspec-process-integration |
| タスク化先 | タスクIDや施策名 | - |
| 対応方針_確定 | L1 が確定した対応内容 | - |
| 確定日 | YYYY-MM-DD | - |
| 備考 | 補足コメント | - |
| 詳細ファイル | `issues/entries/ISS-XXX.md` へのパス | issues/entries/ISS-038.md |
