# 実施計画: l1-impl-manager セッションタイプの新設

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | SKILL.md + エージェント定義5本の作成 | 4フェーズオーケストレーションフローが定義され、各エージェントの責務・入出力が明確 |
| 2 | テンプレートファイル群の作成（sessions/impl/_template/） | 全テンプレートファイルがフェーズプレフィックス番号で整理され、L1/L2の担当ファイルが明確 |
| 3 | 既存ファイルの連動更新 + メタルール横断検証 | commit-message.md, docs/workflow.md, triage-standard-policy が更新済み |

## スケジュール

1. Phase 1: スキル・エージェント定義の作成
2. Phase 2: テンプレートファイルの作成
3. Phase 3: 連動更新・横断検証

## 成功基準（全体）

1. `.claude/skills/l1-impl-manager/SKILL.md` が存在し、4フェーズのオーケストレーションフロー（Investigation → Design → Implementation Planning → Implementation）が定義されている
2. `.claude/skills/l1-impl-manager/agents/` に5つのエージェント定義（investigation-worker, design-worker, impl-plan-worker, impl-worker, impl-evaluator）が存在する
3. `sessions/impl/_template/` にフェーズプレフィックス番号付きの全テンプレートファイルが存在する
4. `.claude/rules/commit-message.md` に `impl-mgr`, `impl-worker`, `impl-evaluator` のセッション種別が追加されている
5. `docs/workflow.md` に l1-impl-manager セッションフローの記述が追加されている
6. `session-flow-policy` との整合性が確認されている（マネージャー=スキル、ワーカー=エージェントの構造）

## 成果物一覧

### スキル・エージェント定義

| ファイル | 内容 |
|---------|------|
| `.claude/skills/l1-impl-manager/SKILL.md` | マネージャーセッション定義（入力パターン・ライフサイクルtodo・4フェーズオーケストレーション・並列ディスパッチ・B+C作業ログ集約） |
| `.claude/skills/l1-impl-manager/agents/investigation-worker.md` | Phase 1: コードベース調査ワーカー |
| `.claude/skills/l1-impl-manager/agents/design-worker.md` | Phase 2: 設計ドキュメント作成ワーカー |
| `.claude/skills/l1-impl-manager/agents/impl-plan-worker.md` | Phase 3: ファイルレベルタスク分割ワーカー |
| `.claude/skills/l1-impl-manager/agents/impl-worker.md` | Phase 4: コード実装ワーカー（テストリトライ・エスカレーション付き） |
| `.claude/skills/l1-impl-manager/agents/impl-evaluator.md` | 全フェーズ共通評価者 |

### テンプレート（sessions/impl/_template/）

| ファイル | フェーズ | 担当 |
|---------|---------|------|
| `00_proposal.md` | Global | L1 |
| `01_plan.md` | Global | L1 |
| `02_impl_design.md` | Phase 2 出力 | Design Worker |
| `07_issues.md` | Global | All |
| `08_gate_summary.md` | Global | L1 |
| `10_investigation_tasks.md` | Phase 1 | L1 |
| `11_investigation_work_log.md` | Phase 1 | Investigation Worker |
| `12_investigation_work_report.md` | Phase 1 | Investigation Worker |
| `13_investigation_eval_plan.md` | Phase 1 | Evaluator |
| `14_investigation_eval_report.md` | Phase 1 | Evaluator |
| `15_investigation_gate.md` | Phase 1 | L1 |
| `20_design_tasks.md` | Phase 2 | L1 |
| `21_design_work_log.md` | Phase 2 | Design Worker |
| `22_design_work_report.md` | Phase 2 | Design Worker |
| `23_design_eval_plan.md` | Phase 2 | Evaluator |
| `24_design_eval_report.md` | Phase 2 | Evaluator |
| `25_design_gate.md` | Phase 2 | L1 |
| `30_impl_plan_tasks.md` | Phase 3 | L1 |
| `31_impl_plan_work_log.md` | Phase 3 | Impl Plan Worker |
| `32_impl_plan_work_report.md` | Phase 3 | Impl Plan Worker |
| `33_impl_plan_eval_plan.md` | Phase 3 | Evaluator |
| `34_impl_plan_eval_report.md` | Phase 3 | Evaluator |
| `35_impl_plan_gate.md` | Phase 3 | L1 |
| `36_file_task_division.md` | Phase 3 出力 | Impl Plan Worker |
| `40_impl_tasks.md` | Phase 4 | L1 |
| `42_impl_work_report.md` | Phase 4 | L1（B+C集約） |
| `43_impl_eval_plan.md` | Phase 4 | Evaluator |
| `44_impl_eval_report.md` | Phase 4 | Evaluator |
| `45_impl_gate.md` | Phase 4 | L1 |

※ Phase 4 の `41_impl_work_log_W*.md` は動的生成（テンプレートなし）

### 連動更新

| ファイル | 更新内容 |
|---------|---------|
| `.claude/rules/commit-message.md` | `impl-mgr`, `impl-worker`, `impl-evaluator` セッション種別を追加 |
| `docs/workflow.md` | l1-impl-manager セッションフローの記述を追加 |
| `.claude/skills/triage-standard-policy/SKILL.md` | ライフサイクル適用マトリクスに l1-impl-manager を追加 |
| `.claude/skills/session-flow-policy/SKILL.md` | セッションタイプ一覧に l1-impl-manager を追加（必要に応じて） |

## リソース・前提条件

- `manager-common-policy` の共通パターン（§2-§8）を再利用する
- `session-flow-policy` のマネージャー=スキル、ワーカー=エージェント構造に従う
- 既存の `l1-manager`, `sync-manager` のパターンを参考にする

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| SKILL.md が肥大化してコンテキストを圧迫 | 中 | 中 | 共通パターンは manager-common-policy への参照で記述量を抑える |
| テンプレートファイル数が多く作成漏れが発生 | 中 | 低 | フェーズごとに整理し、チェックリストで確認 |
| 連動更新の漏れ | 中 | 中 | メタルール横断検証タスクで網羅的に確認 |

---
**作成者**: L1
**作成日**: 2026-03-12
**最終更新**: 2026-03-12
