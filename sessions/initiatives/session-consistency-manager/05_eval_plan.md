# 評価計画: session-consistency-manager

## 壁打ちフェーズ [2026-03-16 24:30]

### 理解のサマリー
- 評価の目的: L2-worker が作成した session-consistency-manager セッションタイプの成果物（SKILL.md、4エージェント定義、テンプレート15ファイル、連動ファイル5件更新）が session-flow-policy と triage-standard-policy の要件を満たしているかを検証する
- 評価スコープ: T-E01（session-flow-policy §5.1 チェックリスト）、T-E02（triage-standard-policy §3.2 チェック項目 A〜E）、T-E03（知見記録）、T-E04（課題転記）
- 完了条件: 06_eval_report.md に全チェック結果と推奨アクションが記載されている。知見テーブル両方に最低1行。07_issues.md の全課題に転記判定が付いている

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク T-001〜T-010 完了、22ファイル新規作成、5ファイル更新）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（3つの成功基準が明確に定義されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read, Write, Edit, Glob, Grep, Bash）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.claude/skills/session-consistency-manager/SKILL.md`（T-001 成果物）
- `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md`（T-002 成果物）
- `.claude/skills/session-consistency-manager/agents/sc-analysis-worker.md`（T-003 成果物）
- `.claude/skills/session-consistency-manager/agents/sc-proposal-worker.md`（T-004 成果物）
- `.claude/skills/session-consistency-manager/agents/sc-evaluator.md`（T-005 成果物）
- `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md`（T-005a 成果物）
- `sessions/session-consistency/_template/` 配下 15 ファイル（T-006 成果物）
- 連動更新 5 ファイル（T-007 成果物）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | session-flow-policy §5.1 チェックリスト（6項目） | SKILL.md・agents/ を §5.1 チェックリスト全項目で検証 | 6項目全て PASS |
| 2 | triage-standard-policy §3.2-A ライフサイクル完備 | §1.2 適用マトリクスの「必須」ステージがロール定義に含まれるか確認 | 「必須」ステージの欠落なし |
| 3 | triage-standard-policy §3.2-B ペアリング整合性 | 4ワーカー ↔ 1評価者のペアリングを検証 | 全ペアリング要件充足 |
| 4 | triage-standard-policy §3.2-C 課題起票・ルーティング | 課題起票方法・知見記録セクションの定義を確認 | 全ロール定義に明記あり |
| 5 | triage-standard-policy §3.2-D マネージャー共通ポリシー準拠 | ゲート判定・差し戻し手順の定義を確認 | 定義あり（直接記載または参照） |
| 6 | triage-standard-policy §3.2-E 停止ルール・スコープ + メタルール横断整合性 | やること/やらないこと・停止ルール・担当ファイルの定義を確認。テンプレートパス参照・workflow.md・TG-008 基準の整合を確認 | 全項目定義あり、メタルール整合 |
| 7 | 01_plan.md 成功基準1: §5.1 通過 | 評価項目1の結果を参照 | PASS |
| 8 | 01_plan.md 成功基準2: §3.2 A〜E 通過 | 評価項目2〜6の結果を参照 | PASS |
| 9 | 01_plan.md 成功基準3: 3フェーズ構造の対称性 | config-optimizer-manager と構造比較 | 3フェーズ構成が対称的 |

## 評価スケジュール
- T-E01 → T-E02 → T-E03 → T-E04 の順で実施

## 前提・制約
- L2-worker の成果物は直接編集しない（読み取りのみ）
- メタルール横断検証チェックリスト（適用条件該当: `.claude/skills/` 配下ファイルの変更あり）

---
**作成者**: L2（評価）
**作成日**: 2026-03-16
