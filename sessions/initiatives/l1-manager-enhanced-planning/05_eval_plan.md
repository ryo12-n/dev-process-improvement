# 評価計画: l1-manager-enhanced-planning（施策フェーズ1）

## 壁打ちフェーズ [2026-03-17 12:00]

### 理解のサマリー
- 評価の目的: 施策フェーズ1（計画ワーカー導入 + フェーズ再構築の基盤）の成果物が成功基準を満たしているか、エビデンスベースで評価する
- 評価スコープ: 新規作成3件（l2-plan-worker.md, l2-plan-evaluator.md, 02a_task_division.md テンプレート）+ 既存変更7件（l1-manager SKILL.md, 02_tasks.md, 08_gate_review.md, manager-common-policy, docs/workflow.md, session-flow-policy, triage-standard-policy）
- 完了条件: 06_eval_report.md にエビデンスベースの評価結果と方針推奨が記載されている

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク完了報告あり）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能
- [x] 評価に必要なツール・アクセス権限: 確認済み

### 不明点・確認事項
確認事項なし：評価開始

---

## 評価項目

### EV-1: フェーズ構造の整合性

| # | 評価観点 | 評価方法 | 判定基準 |
|---|---------|---------|---------|
| 1-1 | Phase A/B/C/D の残存参照がないこと | l1-manager SKILL.md, workflow.md, 08_gate_review.md テンプレートに対する grep | 0件 |
| 1-2 | Phase 1〜6 の定義が SKILL.md 内で一貫していること | Phase 番号と担当者（L1/L2-plan-worker/L2-plan-evaluator/L2-worker/L2-evaluator）の対応をテーブル形式で検証 | 全6フェーズに担当者が明記されている |
| 1-3 | セッションライフサイクル todo が Phase 1〜6 に対応していること | SKILL.md パターン1 のステップ数とフェーズカバレッジを確認 | 全フェーズがステップとして含まれている |

### EV-2: エージェント定義の品質

| # | 評価観点 | 評価方法 | 判定基準 |
|---|---------|---------|---------|
| 2-1 | l2-plan-worker.md が session-flow-policy §3 の必須6セクションを備えていること | セクション見出しの照合 | 6/6 セクション完備 |
| 2-2 | l2-plan-evaluator.md が session-flow-policy §3 の必須6セクションを備えていること | セクション見出しの照合 | 6/6 セクション完備 |
| 2-3 | ペアリング対称性要件（session-flow-policy §3.2）を満たしていること | 対称性確認テーブルの検証 | 6要素すべてが両方に存在 |
| 2-4 | YAML フロントマターが命名規約（§3.4 ケバブケース）に準拠していること | name フィールドの検証 | ケバブケースのみ |
| 2-5 | 関連ファイル一覧が記載されていること | セクション存在確認 | 両エージェントに関連ファイル一覧セクションが存在 |

### EV-3: テンプレートの完全性

| # | 評価観点 | 評価方法 | 判定基準 |
|---|---------|---------|---------|
| 3-1 | 02a_task_division.md テンプレートが l2-plan-worker.md 内のフォーマット定義と整合していること | フォーマット定義のセクション構造とテンプレートのセクション構造を照合 | 全セクションが一致 |
| 3-2 | 02_tasks.md テンプレートに Worker Set Assignment / Set Dispatch Order が追加されていること | セクション存在確認 | 両セクションが存在 |
| 3-3 | 02_tasks.md テンプレートのドメインエージェント欄が Worker/Evaluator に分離されていること | テーブル構造の確認 | 「対象」列が Worker/Evaluator に分かれている |
| 3-4 | 08_gate_review.md テンプレートが5段階フェーズチェック構造になっていること | Phase 1→2, 2→3, 3→4, 4→5, 5→6 の各セクション存在確認 | 5セクションすべて存在 |

### EV-4: メタルール横断検証（T-E03）

| # | 評価観点 | 評価方法 | 判定基準 |
|---|---------|---------|---------|
| 4-1 | l1-manager SKILL.md のフロー記述と新エージェント定義が整合していること | SKILL.md の Phase 2〜3 ディスパッチ手順がエージェント定義の入出力と一致するか検証 | 入出力の不一致が0件 |
| 4-2 | docs/workflow.md が skills/ の変更と同期していること | workflow.md のイニシアティブフローが Phase 1〜6 構造であること、計画ワーカーフェーズが含まれていることを確認 | 構造の不一致が0件 |
| 4-3 | triage-standard-policy SKILL.md の走査対象に l2-plan-worker.md, l2-plan-evaluator.md が含まれていること | TG-008 走査対象リストの確認 | 両ファイルがリストに含まれている |
| 4-4 | session-flow-policy SKILL.md のセッションタイプ一覧に plan-worker/evaluator が含まれていること | テーブルの確認 | L1/L2 施策フロー行にplan-worker/evaluatorが含まれている |
| 4-5 | triage-standard-policy のペアリング構造テーブルに plan-worker/evaluator ペアが含まれていること | ペアリング構造テーブルの確認 | ペアが明記されている |
| 4-6 | triage-standard-policy の適用マトリクスに plan-worker/evaluator の列が含まれていること | 適用マトリクスの列ヘッダ確認 | 列が存在する |

### EV-5: 成功基準の達成度

| # | 成功基準 | 評価方法 |
|---|---------|---------|
| 5-1 | 計画ワーカーが 02a_task_division.md を出力し、L1が02_tasks.mdの作成に活用できる | l2-plan-worker.md の出力定義と SKILL.md の Phase 2〜3 フローで02a→02の変換パスが定義されていることを確認 |
| 5-2 | フェーズ構造が Phase 1〜6 に正しく再構築されている | EV-1 の結果を集約 |
| 5-3 | 新エージェント定義が session-flow-policy の必須要素を満たしている | EV-2 の結果を集約 |
| 5-4 | テンプレートが新フェーズ構造と整合している | EV-3 の結果を集約 |
| 5-5 | docs/workflow.md が skills/ の変更と同期している | EV-4 の結果を集約 |

---
**作成者**: L2-evaluator
**作成日**: 2026-03-17
