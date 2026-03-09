# 開発プロセス改善ワークフロー

> **このファイルの位置づけ**
> `.claude/skills/` 配下のスキル・エージェント定義が正の情報源（Source of Truth）。
> このファイルはルールファイルの内容を人間が理解するための可視化・要約です。
> ルールを変更した場合は、このファイルも合わせて更新してください。

## イニシアティブセッション フロー

```
[L1 マネージャー]
  ブランチ整理: .claude/rules/session-start-branch-cleanup.md のフローを実行
    → 現在ブランチ確認 → 未プッシュコミットがあれば push → PR未作成なら作成 → main に切り替え・最新化
    → 外部リポジトリの整理: アクティブ施策の 00_proposal.md を走査し、外部リポにも同様のフローを実行
    ※ L2 サブエージェントは対象外（L1 の責務）
                                                                    ↓
  フェーズ0: 壁打ち（理解のサマリー・不明点をユーザーに確認）
    → 調査・方針決定 → 提案(00_proposal.md) → 計画(01_plan.md) → タスク作成(02_tasks.md)
    → 外部リポジトリがある場合: 00_proposal.md に記載し、外部リポに施策ブランチを作成
    ※ 02_tasks.md には CSV 転記の固定タスクを必ず含める（後述）
                                                                    ↓
[L2 ワーカー（実施）] ← L1 が Task ツールでサブエージェントとして起動
  壁打ちフェーズ → 03_work_log.md に実施計画サマリを記載 → タスク実施 → 作業記録を追記
  → 04_work_report.md を作成（知見セクションへの記載を含む）
  ※ 外部リポ変更時: 00_proposal.md の外部リポセクション確認 → 施策ブランチにチェックアウト
    → コミット・プッシュ（main 直接コミット禁止・push 省略禁止）
  ※ 課題発見時: 07_issues.md に一時メモ → 施策完了時に CSV へ転記
                                                                    ↓
  L1: worker 成果物を確認（タスク完了状態・CSV転記状態）→ 品質不十分なら差し戻し
                                                                    ↓
[L2 ワーカー（評価）] ← L1 が Task ツールでサブエージェントとして起動（worker 完了後に順次起動）
  壁打ちフェーズ → 05_eval_plan.md → 評価実施 → 06_eval_report.md（知見セクションへの記載を含む）
  → 課題があれば 07_issues.md に追記 → CSV へ転記
                                                                    ↓
[L1 マネージャー]
  04・06・07 を確認 → 08_gate_review.md にゲート判定を記入
    → 通過     : 次フェーズのタスクを 02_tasks.md に追記
    → 条件付き : 条件対応タスクを追記 → L2 に差し戻し
    → 差し戻し : 計画修正 → 02_tasks.md 修正 → L2 に差し戻し
                                                                    ↓
  施策完了（全フェーズ通過）時:
    → initiative クローズ手順を実施
      1. 横展開セクション記載確認（08 の必須把握事項・次施策候補が空欄でないこと）
      2. 課題転記の完了確認（07 の全課題に [転記済 ISS-XXX] or 転記不要）
      3. 知見のルーティング実行（CSV / backlog / inbox / なし）
      4. backlog ファイルの削除確認
      5. git mv sessions/initiatives/<施策名>/ sessions/initiatives/_archive/<施策名>/
      6. コミット・push
      7. 外部リポジトリがある場合: 各外部リポで施策ブランチから main への PR を作成
      8. PR 作成（dev-process-improvement 本体）
```

### 壁打ちフェーズ（フェーズ0）

各セッション（L1・L2 共通）は作業着手前に壁打ちフェーズを実施する。

- **L1**: `00_proposal.md` 作成前に理解のサマリー・不明点を提示し、ユーザーに確認する
- **L2-worker**: `03_work_log.md` 冒頭にサマリー・前提条件チェック・不明点を記録。不明点があれば停止してL1の確認を待つ
- **L2-evaluator**: `05_eval_plan.md` 冒頭に同様のフォーマットで記録

### L2 サブエージェントの起動

L1 は L2 を **Task ツール（サブエージェント）** として順番に起動する。L2-worker が完了してから L2-evaluator を起動すること（並列起動しない）。

起動時に渡す情報: 役割とルールファイル、施策パス、タスク範囲、完了の定義

### 固定タスク（02_tasks.md に必ず含める）

| 対象 | やること | 完了条件 |
|------|---------|---------|
| L2-worker（レポート作成時） | `04_work_report.md` の「作業中の知見」に知見を記録 | 「ルール化候補」「参考情報」各テーブルに最低1行 |
| L2-worker（最終タスク） | `07_issues.md` の未転記課題を CSV へ転記し、`issues/entries/ISS-XXX.md` を作成 | 全課題に `[転記済 ISS-XXX]` or 「転記不要」が付いている |
| L2-evaluator（レポート作成時） | `06_eval_report.md` の「評価中の知見」に知見を記録 | 「ルール化候補」「参考情報」各テーブルに最低1行 |
| L2-evaluator（最終タスク） | 評価中発見の課題を `07_issues.md` 起票 → CSV 転記 → `issues/entries/ISS-XXX.md` 作成 | 同上 |

## トリアージセッション フロー

```
0. ブランチ整理  → .claude/rules/session-start-branch-cleanup.md のフローを実行
                   → 現在ブランチ確認 → 未プッシュあれば push → PR未作成なら作成
                   → main に切り替え・最新化してから作業フローへ
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
                   ・走査ボリューム（inbox + backlog + CSV 対象件数の合計）をもとにセット数を決定
                     ≤20件→1セット / 21〜50件→2セット / 51件以上→3セット
                   ・1セットあたり TG タスク 3件以下を目安とする
3. ワーカーセット作成・ディスパッチ
                   3a. triage-worker をサブエージェントとして起動
                       → inbox / backlog / CSV を走査・分類
                       ・backlog 関係性分析（TG-005）: backlog アイテム間の関係性を横断分析
                         → 重複候補・依存関係・統合候補を検出し、04_scan_report.md に記載
                       ・backlog 施策化済みチェック（TG-002 拡張）:
                         各 backlog ファイルを sessions/initiatives/ + _archive/ と突合し、
                         施策化済みアイテムを「削除・クローズ候補」としてレポートに記載
                         → 削除はユーザー許可後に実施
                       ・完了済み initiative（ゲート通過済み・未アーカイブ）を検出し、
                         クローズチェックリスト検証後にアーカイブ対象としてレポートに記載
                           ・参考資料（ドラフト）ステータスチェック:
                         `CLAUDE.md` の「docs/ 文書分類」テーブルで参考資料に分類された文書の
                         ステータスバナー存在確認・統合状況と skills の矛盾チェック・統合完了文書の残存チェック
                   ・セッション構造標準ポリシーチェック（TG-008）:
                         `.claude/skills/l1-manager/`, `.claude/skills/triage-manager/`, `roles/*.md` を
                         `.claude/skills/triage-standard-policy/SKILL.md` の基準と突合し、
                         ライフサイクル完備・ペアリング整合性・課題起票手段・停止ルールを確認
                         → 「必須」欠落は CSV に優先度「高」で起票
                         → 「推奨」欠落は CSV に優先度「中」で起票
                         → 軽微な記述ズレはそのセッション内で修正
                       ・情報欠損リスク評価（TG-009）【条件付き実行】:
                         走査結果に削除・統合候補がある場合のみ実施
                         → 各候補ファイルの知見数・参照リンク数・具体的データを棚卸し
                         → 統合候補は統合先との情報対比を実施
                         → リスク評価テーブル（ファイル名・含有知見数・参照リンク数・消失リスク・推奨アクション）を作成
                         → リスク「高」のファイルは施策化や知見保全を優先
                         → 削除・統合候補がない場合はスキップ
                   3b. ワーカー完了後、triage-evaluator をサブエージェントとして起動
                       → ワーカーの走査結果を評価（網羅性・判断の妥当性・優先度の整合性）
                       → 06_eval_report.md を作成
                   ※ セット内は worker → evaluator の逐次起動（並列起動禁止）
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
0. ブランチ整理  → .claude/rules/session-start-branch-cleanup.md のフローを実行
                   → 現在ブランチ確認 → 未プッシュあれば push → PR未作成なら作成
                   → main に切り替え・最新化してから作業フローへ
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

## リポジトリ間同期セッション フロー

```
[sync-manager]
  ブランチ整理: .claude/rules/session-start-branch-cleanup.md のフローを実行
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
  → 04_sync_report.md を作成（知見セクションへの記載を含む）
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

4つのマネージャーセッション（l1-manager, triage-manager, metacognition-manager, sync-manager）に共通する運用パターンを一元的に定義するポリシー。各マネージャースキルは固有ロジックを自身の SKILL.md に記載し、共通パターンは本ポリシーを参照する。

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
| §1 | 適用対象 | l1, triage, metacognition, sync の4マネージャー |
| §2 | ワーカーディスパッチパターン | 共通4項目（役割・場所・スコープ・完了定義）+ 順序制約（基本逐次） |
| §3 | 成果物確認観点 | 共通最小3項目（タスク分類・レポート記載・課題バッファ） |
| §4 | ゲート判定基準 | 通過 / 条件付き通過 / 差し戻しの3択 |
| §5 | 知見集約手順 | worker/evaluator の知見を集約 + ルーティング判断基準 |
| §6 | 課題集約手順 | 07_issues.md → CSV転記 → ISS-XXX.md |
| §7 | 差し戻し手順 | 成果物チェック → NG ならフィードバック・再起動 |
| §8 | 関連ファイル一覧 | 4マネージャースキル + session-flow-policy + triage-standard-policy + workflow.md |

各マネージャースキルは共通パターンを `manager-common-policy §N` の形式で参照し、固有のロジック（l1 のクローズ手順、triage の TG タスク等）は自身の SKILL.md に残す。

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
