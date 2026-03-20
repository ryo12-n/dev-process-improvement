# タスクリスト: initiative-template-2phase-migration

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | テンプレートファイルのリネーム・再配置が主作業 | Worker |
| なし | - | 同上 | Evaluator |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-008 | Wave 1 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | 小規模施策（S）、1ワーカー逐次実行 |

---

## タスク一覧

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | マネージャールートファイルのリネーム（7件） | 旧ファイル7件削除・新ファイル7件配置・内容同一 | 🔴 | ✅ |
| T-002 | phase-1-planning ディレクトリ作成（ゲート + ワーカーセット8ファイル） | `phase-1-planning/01_gate.md` 存在、`_template/` に8ファイル配置 | 🔴 | ✅ |
| T-003 | phase-2-execution ディレクトリ作成 + 旧ファイル削除 | `phase-2-execution/01_gate.md` 存在、`_template/` に7ファイル配置、旧ファイル8件削除済み | 🔴 | ✅ |
| T-004 | ポリシー「移行中」注記解除 + l1-manager 整合確認 | 注記削除、l1-manager 整合確認済み、旧ファイル名の残存参照0件 | 🔴 | ✅ |
| T-005 | 知見記録（固定） | 「ルール化候補」「参考情報」の両テーブルに最低1行記載 | 🔴 | ✅ |
| T-006 | メタルール横断検証（固定 — ルール変更施策） | 3領域の検証結果が worker_report に記載 | 🔴 | ✅ |
| T-007 | rule-change-checklist 確認（固定 — ルール変更施策） | 全7項目の結果が worker_log に記録 | 🔴 | ✅ |
| T-008 | 課題転記（固定） | 全課題に転記済/転記不要の判断 | 🔴 | ✅ |

## タスク詳細

### T-001: マネージャールートファイルのリネーム（7件）

旧番号体系のルートファイルを新番号体系にリネームする。`git mv` を使用。

| 旧ファイル | 新ファイル |
|-----------|-----------|
| `00a_wallbash_log.md` | `00_wallbash_log.md` |
| `00_proposal.md` | `01_proposal.md` |
| `01_plan.md` | `02_plan.md` |
| `02_tasks.md` | `03_tasks.md` |
| `02b_dispatch_log.md` | `04_dispatch_log.md` |
| `08_gate_review.md` | `05_gate_review.md` |
| `09_cost_record.md` | `06_cost_record.md` |

### T-002: phase-1-planning ディレクトリの作成

`phase-1-planning/01_gate.md` と `phase-1-planning/_template/` 配下の計画ワーカーセット 7 ファイル + `08_task_division.md` を作成する。

- `01_gate.md`: Phase ゲート記録テンプレート（新規作成）
- `_template/01_worker_plan.md`: plan-worker 壁打ち（`l2-plan-worker.md` 定義準拠）
- `_template/02_worker_log.md`: plan-worker 作業ログ
- `_template/03_worker_report.md`: plan-worker レポート
- `_template/04_eval_plan.md`: plan-evaluator 評価計画
- `_template/05_eval_log.md`: plan-evaluator 評価ログ
- `_template/06_eval_report.md`: plan-evaluator 評価レポート
- `_template/07_issues.md`: 課題バッファ
- `_template/08_task_division.md`: タスク分割成果物（旧 `02a_task_division.md` から移動）

**注意**: `01_worker_plan.md` の壁打ちチェック項目は plan-worker 向け（計画理解・ファイル特定）。phase-2 の worker 向け（依存タスク完了・環境準備）とは異なる。

### T-003: phase-2-execution ディレクトリの作成 + 旧ファイル削除

`phase-2-execution/01_gate.md` と `phase-2-execution/_template/` 配下の実施ワーカーセット 7 ファイルを作成し、旧ファイルを削除する。

- `01_gate.md`: Phase ゲート記録テンプレート（新規作成）
- `_template/01_worker_plan.md`: worker 壁打ち（旧 `03_work_log.md` の壁打ちセクション由来）
- `_template/02_worker_log.md`: worker 作業ログ（旧 `03_work_log.md` の作業ログセクション由来）
- `_template/03_worker_report.md`: worker レポート（旧 `04_work_report.md` 由来）
- `_template/04_eval_plan.md`: evaluator 評価計画（旧 `05_eval_plan.md` 由来）
- `_template/05_eval_log.md`: evaluator 評価ログ（新規作成）
- `_template/06_eval_report.md`: evaluator 評価レポート（旧 `06_eval_report.md` 由来）
- `_template/07_issues.md`: 課題バッファ（旧 `07_issues.md` 由来）

**削除対象**: `03_work_log.md`, `03_work_log_W_template.md`, `04_work_report.md`, `05_eval_plan.md`, `06_eval_report.md`, `07_issues.md`, `07_issues_W_template.md`, `02a_task_division.md`

### T-004: ポリシー「移行中」注記解除 + 整合確認

1. `session-lifecycle-policy/SKILL.md` §1.4.3 の「移行中」注記バナー（行180）を削除
2. `l1-manager/SKILL.md` の関連ファイル一覧のパスが新構造と整合していることを確認
3. 旧ファイル名（`00_proposal.md`, `00a_wallbash_log.md`, `02a_task_division.md`, `02b_dispatch_log.md`, `08_gate_review.md`, `09_cost_record.md`）への残存参照を `.claude/skills/` と `.claude/rules/` で grep 確認

### T-005〜T-008: 固定タスク

上記タスク一覧テーブルの完了条件を参照。

---
**作成者**: L1
**最終更新**: 2026-03-20
