# 評価計画: backlogメンテナンスセッション作成

## 壁打ちフェーズ [2026-03-10]

### 理解のサマリー
- 評価の目的: 実施ワーカーが作成した backlog-maintenance セッションタイプの成果物（SKILL.md、worker.md、evaluator.md、テンプレート、連動更新）が、session-flow-policy・ペアリング対称性要件・既存セッションタイプとの構造的一貫性を満たしているかを検証する
- 評価スコープ: E-001〜E-006（session-flow-policy §5.1 チェックリスト評価、ペアリング対称性検証、構造一貫性評価、連動更新網羅性検証、知見記録、課題CSV転記）
- 完了条件: 05_eval_plan.md に壁打ちフェーズと評価計画が記録され、06_eval_report.md に全評価項目の判定結果と「評価中の知見」セクションが記載されている

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク T-001〜T-012 が完了、成果物一覧・知見記録あり）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（7つの成功基準が明記）
- [x] 評価に必要なツール・アクセス権限: 確認済み（全評価対象ファイルを読み取り可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.claude/skills/backlog-maintenance-manager/SKILL.md`
- `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md`
- `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md`
- `sessions/backlog-maintenance/_template/` 配下の全ファイル（12ファイル）
- `docs/workflow.md` の backlog-maintenance セクション
- `.claude/rules/commit-message.md` の bm-mgr, bm-worker, bm-eval セクション
- `.claude/skills/session-flow-policy/SKILL.md` §5 テーブル
- `.claude/skills/manager-common-policy/SKILL.md` §1 テーブル
- `.claude/skills/triage-standard-policy/SKILL.md` 適用マトリクス

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-001 | session-flow-policy §5.1 チェックリスト評価 | §5.1 の6項目を backlog-maintenance 成果物に照合 | 全6項目がクリアされている |
| E-002 | ペアリング対称性要件（§3.2）の充足検証 | worker.md と evaluator.md の6要素（壁打ち・計画・レポート・知見記録・課題起票・停止ルール）を対比 | 6要素全てが両方に存在する |
| E-003 | 既存セッションタイプとの構造一貫性評価 | triage, metacognition の SKILL.md・worker・evaluator と構造比較（命名・セクション構成・ファイル構成） | 命名規則・セクション構成・ファイル構成が一貫している |
| E-004 | 連動更新の網羅性検証 | 変更された5ファイル（workflow.md, commit-message.md, session-flow-policy, manager-common-policy, triage-standard-policy）の更新内容を検証 | 各ファイルに backlog-maintenance の情報が適切に追加されている |
| E-005 | 知見記録 | 評価中に発見した知見を分類・記録 | 「ルール化候補」「参考情報」の両テーブルに最低1行記載 |
| E-006 | 課題のCSV転記 | 施策をまたぐ課題の有無を確認し、あれば転記 | 全課題に転記済みまたは転記不要の判断が付いている |

## 評価スケジュール
- E-001〜E-004: 順に評価を実施し、結果を 06_eval_report.md に記載
- E-005: 評価中に並行して知見を記録
- E-006: 評価完了後に課題を確認・転記

## 前提・制約
- 評価は読み取りのみで実施。成果物の直接修正は行わない
- 比較対象: triage-manager, metacognition-manager の既存実装

---
**作成者**: L2（評価）
**作成日**: 2026-03-10
