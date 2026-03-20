# 改善施策提案: テンプレート構造統一改修

## 背景・課題

session-lifecycle-policy §1.4 で基本モデル（multi-phase manager パターン）を定義したが、現状の initiative テンプレートディレクトリ構造は以下の点で基本モデルと乖離している:

1. **フラット構造**: マネージャーファイルとワーカーファイルがルート直下に混在（15ファイル）。マネージャー/ワーカー層の分離がない
2. **ファイル名衝突**: Phase 2-3（計画）と Phase 4-5（実施）で同一ファイル名を再利用（`03_work_log.md`, `04_work_report.md`, `05_eval_plan.md`, `06_eval_report.md`）
3. **番号体系の不整合**: プレフィックス番号が飛び（00, 00a, 01, 02, 02a, 02b, 03〜07, 08, 09）で一貫性がない
4. **並列ディスパッチの冗長性**: W_template ファイル（`03_work_log_W_template.md`, `07_issues_W_template.md`）が必要。set コピー方式なら不要
5. **ワーカーファイルの責務混在**: `03_work_log.md` にタスク理解（壁打ち）と作業メモが混在。plan/log/report の3段階に分離すべき

## 目標

- initiative テンプレートのポリシー定義を multi-phase manager パターンに統一する
- 2-phase 構造（phase-1-planning / phase-2-execution）を定義し、ファイル名衝突を解消する
- ワーカーセットテンプレートを worker 3ファイル（plan/log/report）+ eval 3ファイル（plan/log/report）+ issues の7ファイル構成に統一する
- 並列ディスパッチを set コピー方式に統一し、W_template を廃止する

## スコープ

### やること
- session-lifecycle-policy §1.4.3（Initiative テンプレート定義）の改訂
- l1-manager SKILL.md のファイル参照パス・Phase 番号・並列ディスパッチ手順の更新
- エージェント定義（l2-worker, l2-evaluator, l2-plan-worker, l2-plan-evaluator）の担当ファイルテーブル更新
- parallel-dev.md の per-worker ファイル分離パターンを set コピー方式に更新
- commit-message.md のファイル参照があれば更新
- docs/workflow.md の連動更新

### やらないこと
- 実際のテンプレートファイル・ディレクトリ構造の改修（別施策で実施）
- single-phase セッション（triage, meta, bm, auto）の統一（別施策）
- impl の `_template/` sub-dir 導入（別施策）
- 既存セッションインスタンスの遡及変更

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- 全セッションタイプのテンプレートが基本モデルに準拠し、構造的な一貫性が向上
- SC-004/SC-009 チェックの例外ケースが減少
- ワーカーの作業品質向上（plan/log/report の分離により、各段階の目的が明確化）
- 並列ディスパッチの仕組みが簡素化（W_template 廃止、set コピーで統一）
- 新施策テンプレート設計時のリファレンスとして機能

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| ポリシー変更と実ファイル構造の乖離期間が発生 | 中 | 後続施策（実ファイル改修）を速やかに実施する。ポリシーに「移行中」ステータスを明記 |
| 既存エージェント定義のファイルパス参照漏れ | 中 | grep による網羅的なパス参照チェックをタスクに含める |
| ワーカーセットの plan/log/report 分離に伴う L2 エージェントの混乱 | 低 | 各ファイルの役割を明確に定義し、エージェント定義に記載 |

## 壁打ちの背景

### 2-phase 構造の採用理由
initiative のライフサイクルは大きく「計画」と「実施」に分かれる。現行では Phase 2-3（plan-worker/plan-evaluator）と Phase 4-5（worker/evaluator）で同一ファイル名を再利用しているが、これは multi-phase パターンでは phase ディレクトリで自然に分離される。co/sc の 3-phase パターンを参考に、initiative では 2-phase（planning/execution）が最も自然な分割となる。

### ワーカーセットの plan/log/report 分離
現行の `03_work_log.md` は壁打ち（タスク理解）と作業メモが混在している。これを3段階に分離する:
- **plan**: 着手前にタスクを理解し、不明点を解消して取り組む準備が整った状態を作る
- **log**: 作業中の判断背景・つまづきポイント・意思決定の詳細を随時記録
- **report**: plan + log + 成果物を振り返り、目的達成の確認と課題・改善点の発見

### スコープをポリシー修正に限定した理由
影響範囲が大きいため、まずポリシー（あるべき姿の定義）を固め、実ファイル改修は別施策で確実に行う2段階アプローチを採用。

### 段階的実施の判断
バックログでは3点（single-phase, initiative, impl）を推奨していたが、まず initiative から着手し、他は別施策で対応する。initiative が最も利用頻度が高く、改善効果が大きいため。

## 備考・設計パターン

### 新テンプレート構造（合意済み）

```
_template/
├── 00_wallbash_log.md              ← L1（壁打ちログ、最初に作成）
├── 01_proposal.md                  ← L1（壁打ちを受けて作成）
├── 02_plan.md                      ← L1
├── 03_tasks.md                     ← L1
├── 04_dispatch_log.md              ← L1
├── 05_gate_review.md               ← L1
├── 06_cost_record.md               ← L1
│
├── phase-1-planning/
│   ├── 01_gate.md
│   └── _template/
│       ├── 01_worker_plan.md          ← plan-worker: タスク理解・不明点解消
│       ├── 02_worker_log.md           ← plan-worker: 作業中の判断・メモ
│       ├── 03_worker_report.md        ← plan-worker: 振り返り・課題発見
│       ├── 04_eval_plan.md            ← plan-evaluator: 評価観点の整理
│       ├── 05_eval_log.md             ← plan-evaluator: 評価中の判断・メモ
│       ├── 06_eval_report.md          ← plan-evaluator: 評価結果・改善点
│       ├── 07_issues.md              ← 共有: 課題バッファ
│       └── 08_task_division.md        ← 成果物（最後）
│
└── phase-2-execution/
    ├── 01_gate.md
    └── _template/
        ├── 01_worker_plan.md          ← worker: タスク理解・不明点解消
        ├── 02_worker_log.md           ← worker: 作業中の判断・メモ
        ├── 03_worker_report.md        ← worker: 振り返り・課題発見
        ├── 04_eval_plan.md            ← evaluator: 評価観点の整理
        ├── 05_eval_log.md             ← evaluator: 評価中の判断・メモ
        ├── 06_eval_report.md          ← evaluator: 評価結果・改善点
        └── 07_issues.md              ← 共有: 課題バッファ
```

### 並列ディスパッチの set コピー方式
phase-2-execution の `_template/` を `set-1/`, `set-2/`, ... にコピーして各ワーカーに割り当てる。W_template ファイルは不要。

---
**起票者**: L1
**起票日**: 2026-03-19
**ステータス**: 実施中
**backlog元ファイル**: backlog/entries/テンプレート構造統一改修.md
