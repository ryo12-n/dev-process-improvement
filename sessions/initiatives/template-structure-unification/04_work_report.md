# 作業レポート: テンプレート構造統一改修

## サマリ

initiative テンプレートのポリシー・スキル定義・エージェント定義を新構造（2-phase + ワーカーセット 7 ファイル + set コピー方式）に更新した。T-001〜T-007 で 7 つの正の情報源を更新し、T-008 で docs/workflow.md の連動更新、T-009〜T-012 で検証・固定タスクを完了した。全 12 タスクが完了し、旧ファイル名・旧パス・per-worker/W_template への参照は initiative 関連セクションから全て除去された。

## タスク実績

| ID | タスク | 完了条件 | 実績 | 差異・備考 |
|----|--------|---------|------|-----------|
| T-001 | session-lifecycle-policy §1.4.3 改訂 | §1.4.3 が 2-phase 構造を定義、§1.4.2 に initiative 向け 7 ファイル追加、§1.3 パターン A 更新、W_template 除去、「移行中」注記 | 完了 | 計画通り |
| T-002 | l1-manager SKILL.md 更新 | 全旧ファイル名更新、Phase 番号一貫、set コピー方式反映、per-worker 除去 | 完了 | 計画通り |
| T-003 | l2-plan-worker 担当ファイルテーブル更新 | phase-1-planning 配下の plan/log/report 体系反映 | 完了 | 計画通り |
| T-004 | l2-plan-evaluator 担当ファイルテーブル更新 | phase-1-planning 配下の eval_plan/eval_log/eval_report 反映、05_eval_log.md 追加 | 完了 | 計画通り |
| T-005 | l2-worker 担当ファイルテーブル更新 | phase-2-execution 配下の plan/log/report 反映、per-worker 除去、set 方式更新 | 完了 | 計画通り |
| T-006 | l2-evaluator 担当ファイルテーブル更新 | phase-2-execution 配下の eval_plan/eval_log/eval_report 反映、05_eval_log.md 追加 | 完了 | 計画通り |
| T-007 | parallel-dev.md を set コピー方式に改訂 | per-worker 除去、W_template 除去、set コピー方式定義、順次時 set-1 固定、統合手順更新 | 完了 | 計画通り |
| T-008 | docs/workflow.md の連動更新 | イニシアティブフロー図・ファイル権限マトリクス・固定タスク等の全ファイル名参照を更新 | 完了 | GHA/impl セクションは対象外（別体系） |
| T-009 | メタルール横断検証 | 3 領域（フロー記述・workflow.md・TG-008 基準）の検証結果を記載 | 完了 | 全領域で整合性を確認 |
| T-010 | rule-change-checklist 確認 | 全 7 項目の確認結果を 03_work_log.md に記録 | 完了 | 該当なし 4 項目、確認済み 3 項目 |
| T-011 | 作業中の知見を記録 | 「ルール化候補」「参考情報」各テーブルに最低 1 行 | 完了 | 本ファイル |
| T-012 | 課題の転記確認 | 全課題に転記済み/転記不要の判断 | 完了 | 課題なし |

## 成果物一覧

| 成果物 | パス | 備考 |
|--------|------|------|
| session-lifecycle-policy 更新 | `.claude/skills/session-lifecycle-policy/SKILL.md` | §1.3 パターン A + §1.4.1〜§1.4.3 |
| l1-manager SKILL.md 更新 | `.claude/skills/l1-manager/SKILL.md` | パターン 1/2 + 並列ディスパッチ |
| l2-plan-worker 更新 | `.claude/skills/l1-manager/agents/l2-plan-worker.md` | 担当ファイルテーブル + フロー |
| l2-plan-evaluator 更新 | `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` | 担当ファイルテーブル + フロー |
| l2-worker 更新 | `.claude/skills/l1-manager/agents/l2-worker.md` | 担当ファイルテーブル + フロー |
| l2-evaluator 更新 | `.claude/skills/l1-manager/agents/l2-evaluator.md` | 担当ファイルテーブル + フロー |
| parallel-dev.md 更新 | `.claude/rules/parallel-dev.md` | set コピー方式 |
| docs/workflow.md 更新 | `docs/workflow.md` | 連動更新 |
| 作業ログ | `sessions/initiatives/template-structure-unification/03_work_log.md` | 全タスクの作業履歴 |
| 作業レポート | `sessions/initiatives/template-structure-unification/04_work_report.md` | 本ファイル |

## 課題参照

07_issues.md: 課題なし（未転記メモなし）

## メタルール横断検証結果（T-009）

### 1. メタルールフロー記述

変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているかを確認した。

| ファイル | 検証結果 | 詳細 |
|---------|---------|------|
| `.claude/skills/l1-manager/SKILL.md` | 整合 | 旧ファイル名参照なし。Phase 番号・set コピー方式・新ファイル名が一貫 |
| `.claude/skills/l1-manager/agents/l2-worker.md` | 整合 | phase-2-execution/set-N/ 配下の plan/log/report 体系。per-worker 参照なし |
| `.claude/skills/l1-manager/agents/l2-evaluator.md` | 整合 | phase-2-execution/set-N/ 配下の eval_plan/eval_log/eval_report 体系 |
| `.claude/skills/l1-manager/agents/l2-plan-worker.md` | 整合 | phase-1-planning/set-N/ 配下の plan/log/report 体系 |
| `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` | 整合 | phase-1-planning/set-N/ 配下の eval_plan/eval_log/eval_report 体系 |
| `.claude/rules/parallel-dev.md` | 整合 | set コピー方式。per-worker/W_template 参照なし |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | 整合 | §1.3 パターン A + §1.4.3 が新構造を定義 |

### 2. workflow.md 同期

T-008 で更新した docs/workflow.md のイニシアティブセクションが、正の情報源と整合していることを確認した。

- フロー図: 新ファイル名・set コピー方式を反映
- フェーズゲートチェック: 05_gate_review.md を参照
- 壁打ちフェーズ: phase-*/set-N/01_worker_plan.md / 04_eval_plan.md を参照
- 固定タスク: 新ファイル名を参照
- ファイル権限マトリクス: 3テーブル（マネージャールート・ワーカーセット・共通）に再構成済み

### 3. TG-008 基準連動

session-lifecycle-policy の §1.4.3 が新テンプレート構造を定義済み。TG-008 チェックリスト（triage-manager/SKILL.md 内）は汎用的な観点（壁打ち定義・ライフサイクル完備・ペアリング対称性等）でチェックしており、特定のファイル名に依存しないため、追加更新は不要。

## 作業中の知見

### ルール化候補（.claude/rules/ や skills/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | docs/workflow.md のファイル権限マトリクスは、2-phase 構造では「マネージャールートファイル」と「ワーカーセットファイル」に分離する方が可読性が高い | T-008 | docs/workflow.md | フラット構造では全ファイルを1テーブルで表現できたが、phase-*/set-N/ のパスが入ると1テーブルでは冗長になる。3テーブル（マネージャールート・ワーカーセット・共通）への分離パターンを他の multi-phase セッション（co, sc 等）にも適用検討可能 |
| 2 | GHA ワークフローが独自のファイル命名体系を持つため、initiative ポリシー変更時に GHA セクションの更新は独立判断が必要 | T-008 | docs/workflow.md GHA セクション | GHA Initiative スキル（gha-wallbash 等）は CLI のスキル定義とは独立しており、テンプレート実体の変更後に GHA 側を対応する2段階アプローチが適切 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | §1.4.2 のワーカーセット 7 ファイルは initiative 向けと 3-phase 向けで命名が異なる（worker_plan vs scan_plan 等） | T-001 分析（計画ワーカーから引継ぎ） | 将来の single-phase 統一施策で命名規則の標準化が必要。現時点では併存が妥当 |
| 2 | parallel-dev.md の変更は §2〜§4 全セクションに及び、per-worker から set コピーへの概念的な転換が大きい | T-007, T-008 | 後続施策（実テンプレート改修）で per-worker → set 方式のマイグレーション手順が必要になる場合がある |

---
**作成者**: L2（実施ワーカー）
**作成日**: 2026-03-20
