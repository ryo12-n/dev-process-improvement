# 評価計画: session-artifacts-structure-refactor

## 壁打ちフェーズ [2026-03-16]

### 理解のサマリー
- 評価の目的: config-optimizer / impl テンプレートの phase ディレクトリ再構成が正しく完了し、旧ファイル名参照が残留していないことを検証する
- 評価スコープ: T-E01（旧ファイル名残存チェック）、T-E02（参照整合性検証）
- 完了条件: 06_eval_report.md に各成功基準に対するエビデンス付き達成度評価を記載。方針推奨を明記

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能
- [x] 評価に必要なツール・アクセス権限: 確認済み

### 不明点・確認事項
確認事項なし：評価開始

---

## 評価対象
- L2-worker の作業成果（T-001〜T-007）
- config-optimizer テンプレート + SKILL.md/agents の参照整合性
- impl テンプレート + SKILL.md/agents の参照整合性
- docs/workflow.md の連動更新
- 非対象テンプレートの未変更

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E01-1 | config-optimizer 旧ゲートファイル名残存 | `.claude/skills/`, `sessions/*/_template/`, `docs/` を対象に `15_collection_gate`, `25_analysis_gate`, `35_proposal_gate` を grep（既存インスタンス・施策ディレクトリ除外） | 0 件 |
| E01-2 | impl 旧ファイル名残存 | 同対象で `10_investigation`, `11_investigation`, `20_design`, `21_design`, `30_impl_plan`, `31_impl_plan`, `40_impl`, `41_impl`, `42_impl`, `43_impl`, `44_impl`, `45_impl` を grep（同除外条件） | 0 件 |
| E02-1 | config-optimizer SKILL.md + agents 参照の実在性 | SKILL.md/agents 内で参照されるファイルパスを抽出し、`sessions/config-optimization/_template/` 内に実在確認 | 全参照パスが実在 |
| E02-2 | impl SKILL.md + agents 参照の実在性 | SKILL.md/agents 内で参照されるファイルパスを抽出し、`sessions/impl/_template/` 内に実在確認 | 全参照パスが実在 |
| E02-3 | 非対象テンプレートの未変更確認 | triage, metacognition, BM, automation, sync のテンプレートを `git diff main` で確認 | 差分なし |
| SC-1 | config-optimizer phase ディレクトリ + gate ファイル存在 | `ls` で確認 | 3 phase ディレクトリ + 各 01_gate.md が存在 |
| SC-2 | impl テンプレート旧ファイル不在 | `ls sessions/impl/_template/` で確認 | ルート直下に `10_`〜`45_` プレフィックスファイルなし |
| SC-4 | docs/workflow.md 新構造反映 | workflow.md 内の旧ファイル名検索 + 新パス記載確認 | 旧ファイル名 0 件、新 phase パス記載あり |
| MR-1 | メタルール横断検証（フロー記述整合） | スキル定義のフロー記述と実ファイル構造の一致確認 | 一致 |
| MR-2 | メタルール横断検証（workflow.md 同期） | docs/workflow.md と SKILL.md の整合確認 | 整合 |
| MR-3 | メタルール横断検証（TG-008 基準） | triage-standard-policy/SKILL.md の確認 | 該当なしまたは反映済み |

## 評価スケジュール
- E01-1, E01-2 を並列実行 → E02-1, E02-2, E02-3 を実行 → SC/MR 検証 → レポート作成

## 前提・制約
- 既存セッションインスタンス（sessions/config-optimization/20260315/ 等）は変更スコープ外のため除外
- 施策ディレクトリ（sessions/initiatives/session-artifacts-structure-refactor/）内の 02_tasks.md 等の対応表参照も除外

---
**作成者**: L2（評価）
**作成日**: 2026-03-16
