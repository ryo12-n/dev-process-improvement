# コミットメッセージ規約

## 適用対象

dev-process-improvement 配下で行うすべての git コミットに適用する。

施策の一環として外部リポジトリ（`00_proposal.md` の「外部リポジトリ」セクションに記載されたリポジトリ）を変更する場合も、同じ規約を適用する。

---

## 形式

```
[<session-type>] <category>: <summary>

<details>
```

### パラメータ

| パラメータ | 必須 | 説明 |
|-----------|------|------|
| `session-type` | 必須 | コミットを行うセッション種別（下記テーブル参照） |
| `category` | 必須 | 施策名またはカテゴリ（下記テーブル参照） |
| `summary` | 必須 | 1行の要約（50文字以内推奨） |
| `details` | 任意 | 変更したファイル一覧、作業内容の詳細（複数行可） |

---

## セッション種別と category の対応

### 施策作業（sessions/initiatives/ 配下の作業）

| session-type | category | 用途 | 例 |
|-------------|----------|------|-----|
| `L1` | sessions/initiatives/ 配下のディレクトリ名 | 提案・計画・タスク作成・ゲート判定 | `[L1] commit-message-rules: 提案・計画を作成` |
| `L2-worker` | 同上 | タスク実施・作業記録・レポート作成（l2-plan-worker を含む） | `[L2-worker] commit-message-rules: ルールファイルを作成` |
| `L2-evaluator` | 同上 | 評価計画・評価実施・レポート作成 | `[L2-evaluator] commit-message-rules: 評価レポートを作成` |

### 非施策作業（EVL-001 対応）

| session-type | category | 用途 | 例 |
|-------------|----------|------|-----|
| `triage-mgr` | `YYYYMMDD` | マネージャー: 事前調査・計画・ディスパッチ・集約レポート | `[triage-mgr] 20260305: 事前調査・ワーカー割り当て` |
| `triage-worker` | `YYYYMMDD` | ワーカー: 走査実行・スキャンレポート | `[triage-worker] 20260305: set-1 inbox/CSV スキャン完了` |
| `triage-eval` | `YYYYMMDD` | 評価者: 評価レポート | `[triage-eval] 20260305: set-1 評価レポート作成` |
| `meta-mgr` | `YYYYMMDD` | マネージャー: 事前調査・計画・ディスパッチ・集約レポート | `[meta-mgr] 20260308: 事前調査・ワーカー割り当て` |
| `meta-worker` | `YYYYMMDD` | ワーカー: MC タスク走査・スキャンレポート | `[meta-worker] 20260308: set-1 MC-001/MC-002 分析完了` |
| `meta-eval` | `YYYYMMDD` | 評価者: 評価レポート | `[meta-eval] 20260308: set-1 評価レポート作成` |
| `sync` | 同期方向（`upstream-to-origin` / `origin-to-upstream`） | git レベルの単純同期（ブランチ同期等） | `[sync] upstream-to-origin: main ブランチを同期` |
| `sync-mgr` | `YYYYMMDD` | マネージャー: 事前調査・計画・ディスパッチ・ゲート判定 | `[sync-mgr] 20260308: 事前調査・ワーカー割り当て` |
| `sync-worker` | `YYYYMMDD` | ワーカー: 同期作業実行・同期レポート | `[sync-worker] 20260308: 同期作業完了・レポート作成` |
| `sync-eval` | `YYYYMMDD` | 評価者: 検証チェックリストに基づく評価レポート | `[sync-eval] 20260308: 評価レポート作成` |
| `bm-mgr` | `YYYYMMDD` | マネージャー: 事前調査・計画・ディスパッチ・集約レポート | `[bm-mgr] 20260310: 事前調査・ワーカー割り当て` |
| `bm-worker` | `YYYYMMDD` | ワーカー: BM タスク走査・スキャンレポート | `[bm-worker] 20260310: set-1 BM-001〜BM-003 走査完了` |
| `bm-eval` | `YYYYMMDD` | 評価者: 評価レポート | `[bm-eval] 20260310: set-1 評価レポート作成` |
| `auto-mgr` | `YYYYMMDD` | マネージャー: 事前調査・計画・ディスパッチ・集約レポート | `[auto-mgr] 20260313: 事前調査・ワーカー割り当て` |
| `auto-worker` | `YYYYMMDD` | ワーカー: AT タスク走査・スキャンレポート | `[auto-worker] 20260313: set-1 AT-001〜AT-004 走査完了` |
| `auto-eval` | `YYYYMMDD` | 評価者: 評価レポート | `[auto-eval] 20260313: set-1 評価レポート作成` |
| `impl-mgr` | 施策名 | マネージャー: 4フェーズオーケストレーション・ゲート判定 | `[impl-mgr] feature-x: Phase 1 調査タスク作成・ワーカーディスパッチ` |
| `impl-worker` | 施策名 | ワーカー: コード実装・テスト・チェックポイント記録 | `[impl-worker] feature-x: IMPL-001 実装完了・テストPASS` |
| `impl-evaluator` | 施策名 | 評価者: フェーズ評価レポート作成 | `[impl-evaluator] feature-x: Phase 2 評価レポート作成` |
| `co-mgr` | `YYYYMMDD` | マネージャー: 事前調査・計画・ディスパッチ・ゲート判定・集約レポート | `[co-mgr] 20260314: 事前調査・Phase 1 ワーカーディスパッチ` |
| `co-worker` | `YYYYMMDD` | ワーカー: 情報収集・現状分析・最適化提案 | `[co-worker] 20260314: Phase 1 情報収集完了・リファレンス更新` |
| `co-eval` | `YYYYMMDD` | 評価者: 評価レポート | `[co-eval] 20260314: Phase 2 評価レポート作成` |
| `sc-mgr` | `YYYYMMDD` | マネージャー: 事前調査・計画・ディスパッチ・ゲート判定・集約レポート | `[sc-mgr] 20260316: 事前調査・Phase 1 ワーカーディスパッチ` |
| `sc-worker` | `YYYYMMDD` | ワーカー: 情報収集・現状分析・改善提案 | `[sc-worker] 20260316: Phase 1 情報収集完了・リファレンス更新` |
| `sc-eval` | `YYYYMMDD` | 評価者: 評価レポート | `[sc-eval] 20260316: Phase 2 評価レポート作成` |
| `maintenance` | 作業対象を示す名前 | 設定変更・リファクタ等の保守作業 | `[maintenance] settings: $schema と deny ルールを追加` |

---

## 例

### 施策作業のコミット

```
[L2-worker] coordination-protocol: ガイドライン文書を作成

- docs/coordination-protocol-guideline.md を新規作成
- 03_work_log.md に作業履歴を記録
- 04_work_report.md に作業レポートを作成
```

### 非施策作業のコミット

```
[triage-mgr] 20260303: 事前調査・ワーカー割り当て・集約レポート作成

- 00_pre_investigation.md, 01_plan.md を作成
- set-1, set-2 をディスパッチ
- 03_report.md を作成し PR 提出
```

```
[maintenance] settings: $schema と deny ルールを追加

- .claude/settings.json に JSON Schema バリデーションを追加
- .env, secrets/ の deny ルールを設定
```

### 実装セッションのコミット

```
[impl-mgr] feature-x: Phase 1 調査タスク作成・investigation-worker ディスパッチ

- 10_investigation_tasks.md を作成
- investigation-worker をディスパッチ
```

```
[impl-worker] feature-x: IMPL-001 実装完了・テストPASS

- src/module.ts を変更
- テスト3回中1回目でPASS
- 41_impl_work_log_W1.md にチェックポイント記録
```

### メタ認知セッションのコミット

```
[meta-mgr] 20260308: 事前調査・ワーカー割り当て・集約レポート作成

- 00_pre_investigation.md, 01_plan.md を作成
- set-1 をディスパッチ
- 03_report.md を作成し PR 提出
```

---

## 禁止事項

- `git push --force` の使用
- 意味のないコミットメッセージ（`update`, `fix`, `wip` 等のみ）
- session-type のないコミットメッセージ（`[session-type]` プレフィックスは必須）
- category のないコミットメッセージ（施策名またはカテゴリは必須）

---

**作成日**: 2026-03-03
**情報源**: `docs/coordination-protocol-guideline.md` セクション2.2
**関連施策**: `sessions/initiatives/commit-message-rules/`
