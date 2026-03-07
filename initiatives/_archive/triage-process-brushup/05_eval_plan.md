# 評価計画: triage-process-brushup

## 壁打ちフェーズ [2026-03-07]

### 理解のサマリー
- 評価の目的: ai-driven-dev-patterns のトリアージプロセスが dev-process-improvement 側と同等の品質・網羅性にブラッシュアップされたことを検証する
- 評価スコープ: フェーズ1〜3（T-001〜T-016）の全成果物。ai-driven-dev-patterns リポジトリ（ブランチ: initiative/triage-process-brushup）のテンプレート・スキル定義、dev-process-improvement の backlog ファイル
- 完了条件: 7つの評価重点項目すべてに対する判定が完了し、06_eval_report.md に記載されている

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全16タスクの実績・成果物一覧・知見記録が記載済み）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（6項目の成功基準が定量的に記載）
- [x] 評価に必要なツール・アクセス権限: 確認済み（ai-driven-dev-patterns リポジトリへの読み取りアクセス可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- ai-driven-dev-patterns リポジトリ（ブランチ: initiative/triage-process-brushup）
  - `triage/_template/workers/_template/` 配下 7ファイル
  - `triage/_template/` 配下マネージャーテンプレート 5ファイル
  - `.claude/skills/triage/` 配下スキル定義 3ファイル
- dev-process-improvement リポジトリ
  - `backlog/ai-driven-dev-patterns-triage-standard-policy作成.md`

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | ファイル構造の完全性 | `triage/_template/workers/_template/` の ls でファイル一覧を確認 | 01〜07 の7ファイルが全て存在する |
| 2 | 参照整合性 | スキル定義3ファイル + テンプレート全体を grep で旧番号（02_work_log, 03_scan_report, 04_eval_report）残存チェック | 旧番号への参照が0件 |
| 3 | TG体系の完全性 | triage-worker.md を読み、TG-001〜TG-009 の走査ガイド見出しを確認 | 9タスク全ての走査ガイドが存在する |
| 4 | 課題フローの一貫性 | スキル定義3ファイル + テンプレート全体を grep で「CSV に直接起票」等の残存チェック | CSV直接起票の記述が0件、07_issues.md 経由のフローが定義されている |
| 5 | 知見セクションの存在 | 04_scan_report.md / 06_eval_report.md テンプレートを読み、知見テーブル構成を確認 | ルール化候補テーブル + 参考情報テーブルが両ファイルに存在する |
| 6 | 用語の適応 | スキル定義 + テンプレート全体を grep で initiatives/, プロセス改善_課題管理, L1, L2 の残存チェック | dev-process-improvement 固有用語が0件 |
| 7 | dev-process-improvement 側との対称性 | 両リポジトリのワーカーテンプレート構成・マネージャーテンプレート構成・スキル定義の主要構造要素を比較 | 壁打ち/計画/知見記録/課題バッファ/ゲート判定の5要素が両リポジトリで存在する |

## 前提・制約
- ai-driven-dev-patterns リポジトリは initiative/triage-process-brushup ブランチ上で評価する
- 過去のセッション実績（triage/20260305/ 等）はスコープ外

---
**作成者**: L2（評価）
**作成日**: 2026-03-07
