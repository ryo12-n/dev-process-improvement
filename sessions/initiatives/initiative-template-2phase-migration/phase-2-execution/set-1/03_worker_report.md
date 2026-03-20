# 作業レポート: initiative-template-2phase-migration — Set-1

## サマリ

`sessions/initiatives/_template/` の実ディレクトリ構造を `session-lifecycle-policy` §1.4.3 の 2-phase 構造に完全移行した。マネージャールートファイル 7 件のリネーム（T-001、前セッションで実施済み）、phase-1-planning ディレクトリの新規作成（gate + 8 ファイル）、phase-2-execution ディレクトリの新規作成（gate + 7 ファイル）+ 旧ファイル 8 件の削除、ポリシー「移行中」注記の解除と残存参照の修正を完了した。テンプレート構造がポリシー定義と完全に一致する状態になった。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | マネージャールートファイルのリネーム（7件） | git mv で 7 ファイルリネーム | 前セッションで完了済み（コミット d09381a） | 差異なし |
| T-002 | phase-1-planning ディレクトリ作成 | gate + _template 8 ファイル | 計画通り作成 | 差異なし |
| T-003 | phase-2-execution ディレクトリ作成 + 旧ファイル削除 | gate + _template 7 ファイル + 旧 8 件削除 | 計画通り作成・削除 | 差異なし |
| T-004 | ポリシー「移行中」注記解除 + 整合確認 | 注記削除 + grep 確認 | 注記削除 + manager-common-policy, session-flow-policy の旧ファイル名参照を修正 | 残存参照 2 件を追加修正 |
| T-005 | 知見記録 | 知見テーブル記載 | 下記記載 | 差異なし |
| T-006 | メタルール横断検証 | 3 領域検証 | 下記記載 | 差異なし |
| T-007 | rule-change-checklist 確認 | 全 7 項目確認 | worker_log に全項目記録 | 差異なし |
| T-008 | 課題転記 | 転記判断 | 施策横断課題なし → 転記不要 | 差異なし |

## 成果物一覧

- `sessions/initiatives/_template/phase-1-planning/01_gate.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/01_worker_plan.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/02_worker_log.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/03_worker_report.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/04_eval_plan.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/05_eval_log.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/06_eval_report.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/07_issues.md` (CREATE)
- `sessions/initiatives/_template/phase-1-planning/_template/08_task_division.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/01_gate.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/_template/01_worker_plan.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/_template/02_worker_log.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/_template/03_worker_report.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/_template/04_eval_plan.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/_template/05_eval_log.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/_template/06_eval_report.md` (CREATE)
- `sessions/initiatives/_template/phase-2-execution/_template/07_issues.md` (CREATE)
- `.claude/skills/session-lifecycle-policy/SKILL.md` (MODIFY: 移行中注記削除)
- `.claude/skills/manager-common-policy/SKILL.md` (MODIFY: 02a_task_division.md → 08_task_division.md)
- `.claude/skills/session-flow-policy/SKILL.md` (MODIFY: 02a_task_division.md → 08_task_division.md, per-worker ファイル → set ディレクトリ)

## 発生した課題

施策横断課題なし。

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | テンプレート構造変更時は session-consistency-reference.md のファイル一覧も更新対象にすべき | T-004 grep 走査 | `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` | rule-change-checklist のチェック項目6「テンプレートの連動更新」に session-consistency-reference.md の走査を追加する価値がある |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | GHA スキル（gha-wallbash, gha-execute, gha-question）が旧ファイル名（00a_wallbash_log.md, 00_proposal.md, 08_gate_review.md）を参照している | T-004 grep 走査 | BL-119 で対応予定。GHA スキルは独自の命名体系を持つため initiative テンプレートとは独立して管理される |

## メタルール横断検証（T-006）

### 1. メタルールフロー記述

変更対象パス（`sessions/initiatives/_template/`）を参照しているスキル・エージェント定義のフロー記述を確認:

- `l1-manager/SKILL.md`: 前施策で phase-*/set-N/ パターンに更新済み。新テンプレート構造と整合
- `l2-worker.md`: phase-2-execution/set-N/ パターンで記述済み。関連ファイル一覧もテンプレートの新パスを参照
- `l2-evaluator.md`: 同上
- `l2-plan-worker.md`: phase-1-planning/set-N/ パターンで記述済み
- `l2-plan-evaluator.md`: 同上
- `manager-common-policy/SKILL.md`: §2.3 の `02a_task_division.md` 参照を `phase-1-planning/set-N/08_task_division.md` に修正済み
- `session-flow-policy/SKILL.md`: §4.2 の `02a_task_division.md` 参照を修正済み。per-worker ファイル参照を set ディレクトリ参照に修正済み

**結果**: 整合

### 2. docs/workflow.md

- イニシアティブセクション: 前施策で phase-*/set-N/ パターンに更新済み。テンプレートファイル名の直接参照なし
- GHA セクション: `00a_wallbash_log.md`, `00_proposal.md` を参照しているが、GHA 独自の命名体系のため BL-119 スコープ

**結果**: 整合（GHA 部分は BL-119 で対応）

### 3. TG-008 基準

テンプレート構造の変更はライフサイクルステージ・ペアリング対称性要件に影響しない（ファイル配置の変更のみ、ステージ定義や必須要素の変更なし）。

**結果**: 変更不要

## 所感・次フェーズへの申し送り

- テンプレート構造がポリシー §1.4.3 と完全一致する状態になった
- session-consistency-reference.md の initiatives ファイル一覧は旧構造のままだが、SC セッション次回実行時に自動的に検出・更新される参照データのため、本施策での修正は見送った
- GHA スキルの旧ファイル名参照は BL-119 で対応予定

---
**作成者**: L2（実施）
**作成日**: 2026-03-20
