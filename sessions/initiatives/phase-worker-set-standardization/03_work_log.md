# 作業履歴: phase-worker-set-standardization

> **並列ディスパッチ時の注意**: Worker ID（`W<N>`）が指定されている場合は、本ファイルではなく per-worker ファイル（`03_work_log_W<N>.md`）に記録すること。テンプレート: `_template/03_work_log_W_template.md`

## 壁打ちフェーズ [2026-03-19 10:00]

### 理解のサマリー
- タスクの目的: 既存2マネージャー（session-consistency-manager, config-optimizer-manager）のテンプレート・SKILL.md・エージェント定義・ポリシーファイル・docs/workflow.md のパス参照を `phase-N-xxx/_template/` / `phase-N-xxx/set-1/` の標準パターンに統一するためのファイルレベルタスク分割を作成する
- スコープ: テンプレートディレクトリの再配置、SKILL.md 2ファイル・エージェント定義 8ファイルのパス参照更新、ポリシー 2ファイルのセクション追加、docs/workflow.md の2フロー図更新
- 完了条件: `02a_task_division.md` が CREATE/MODIFY/READ アノテーション・Conflict Check Matrix・Wave Assignment 付きで完成し、`04_work_report.md` に計画レポートが記載されていること

### 前提条件チェック
- [x] 施策計画（01_plan.md）の内容を理解: 理解済み — 5フェーズ構成（テンプレート移動→パス参照更新→ポリシー更新→docs更新→横断検証）
- [x] 提案書（00_proposal.md）の確認: 確認済み — `workers/` 中間ディレクトリ廃止、`phase-N-xxx/set-1/` 標準パターン統一
- [x] 変更対象ファイル群の特定: 特定済み — 下記調査結果参照

### 調査結果

#### session-consistency テンプレート（現状）
- `phase-1-collection/workers/_template/` に7ファイル（01_tasks〜07_issues）
- `phase-2-analysis/workers/_template/` に7ファイル
- `phase-3-proposal/workers/_template/` に7ファイル
- 変更: `workers/_template/` → `_template/` に移動（workers/ 中間ディレクトリ削除）

#### config-optimization テンプレート（現状）
- `workers/_template/` にルートレベルで7ファイル（全Phase 共有）
- 各 `phase-N-xxx/` には `01_gate.md` のみ
- 変更: ルート `workers/_template/` を削除し、各 `phase-N-xxx/_template/` に7ファイルを配置

#### SKILL.md パス参照（grep 結果）
- session-consistency-manager: `phase-N-xxx/workers/_template/` → `phase-N-xxx/_template/`、`phase-N-xxx/workers/set-1/` → `phase-N-xxx/set-1/`
- config-optimizer-manager: `workers/_template/` → `phase-N-xxx/_template/`、`workers/set-N/` → `phase-N-xxx/set-1/`

#### エージェント定義パス参照（grep 結果）
- sc-collection-worker: `phase-1-collection/workers/set-1/` → `phase-1-collection/set-1/`
- sc-analysis-worker: `phase-2-analysis/workers/set-1/` + `phase-1-collection/workers/set-1/` 参照
- sc-proposal-worker: `phase-3-proposal/workers/set-1/` + `phase-2-analysis/workers/set-1/` 参照
- sc-evaluator: `phase-N-xxx/workers/set-1` テーブルのパス更新
- config-collection-worker: `workers/set-1/` → `phase-1-collection/set-1/`
- config-analysis-worker: `workers/set-2/` → `phase-2-analysis/set-1/`、`workers/set-1/` 参照も更新
- config-proposal-worker: `workers/set-3/` → `phase-3-proposal/set-1/`、`workers/set-2/` 参照も更新
- config-optimizer-evaluator: `workers/set-N/` → `phase-N-xxx/set-1/`

#### ポリシーファイル
- session-flow-policy: §4.3 追加（3フェーズセッションの標準ディレクトリ構成）— 新セクション
- session-lifecycle-policy: §1.3 に config最適化系列が欠落 — 列追加

#### docs/workflow.md
- L634-695: config最適化フロー — `workers/set-N/` パスを `phase-N-xxx/set-1/` に更新
- L698-761: セッション一貫性フロー — `phase-N-xxx/workers/set-1/` パスを `phase-N-xxx/set-1/` に更新

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：計画開始

---

## 実施計画サマリ

1. 全変更対象ファイルを5フェーズに沿ってタスクに分割
2. テンプレートディレクトリ操作（Phase 1）は他タスクの前提となるため Wave 1 に配置
3. SKILL.md・エージェント定義のパス参照更新（Phase 2）は独立性が高い → 並列化の可能性を検討
4. ポリシーファイル更新（Phase 3）・docs更新（Phase 4）はパス参照完了後に実施
5. 横断検証（Phase 5）は全変更完了後

---

## 作業ログ

### [2026-03-19 10:10] 計画項目: ファイルレベルタスク分割
**状態**: 完了
**作業内容**:
- 全変更対象ファイルの現状を Glob/Grep/Read で調査完了
- パス参照パターンの変更前後を特定
- タスク分割の設計を開始

### [2026-03-19 10:30] 計画項目: 02a_task_division.md 作成
**状態**: 完了
**作業内容**:
- 10タスクに分割（T-001〜T-010）
- 全タスクに CREATE/MODIFY/READ アノテーション付与
- Conflict Check Matrix 作成: 競合 0 件（全タスクのファイル書き込みが排他的）
- Wave Assignment 作成: 3 Wave（Wave 1: テンプレート操作+ポリシー、Wave 2: パス参照更新6タスク並列、Wave 3: 横断検証）
**判断・気づき**:
- T-008（session-lifecycle-policy §1.3）はテンプレート変更に依存しないため Wave 1 に配置可能と判断
- config-optimizer の変更は session-consistency より複雑（パス体系が根本的に異なるため）
- Wave 2 の最大並列度は 6 だが、実際の並列ディスパッチはマネージャーの判断に委ねる

### [2026-03-19 10:40] 計画項目: 04_work_report.md 作成
**状態**: 完了
**作業内容**:
- 計画レポート・知見を 04_work_report.md に記載
