# 評価計画: l1-impl-manager セッションタイプの新設

## 壁打ちフェーズ [2026-03-12 12:00]

### 理解のサマリー
- 評価の目的: l1-impl-manager セッションタイプの新設施策（SKILL.md、エージェント定義5本、テンプレート29本、連動更新4件）の品質を、01_plan.md の成功基準6項目に基づいて評価する
- 評価スコープ: スキル・エージェント定義、テンプレートファイル群、連動更新（commit-message.md, workflow.md, triage-standard-policy, session-flow-policy）、メタルール横断検証
- 完了条件: 06_eval_report.md に評価結果・知見を記録し、07_issues.md に発見した課題を起票する

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全18タスク完了報告あり、メタルール横断検証結果も記載）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（6項目が具体的に定義されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read, Glob, Grep で全成果物にアクセス可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象

- `.claude/skills/l1-impl-manager/SKILL.md`
- `.claude/skills/l1-impl-manager/agents/` 配下の5エージェント定義
- `sessions/impl/_template/` 配下の29テンプレートファイル
- `.claude/rules/commit-message.md`（連動更新部分）
- `docs/workflow.md`（連動更新部分）
- `.claude/skills/triage-standard-policy/SKILL.md`（連動更新部分）
- `.claude/skills/session-flow-policy/SKILL.md`（連動更新部分）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-01 | 成功基準1: SKILL.md の存在と4フェーズオーケストレーションフロー | SKILL.md を読み、4フェーズ（Investigation/Design/Implementation Planning/Implementation）のフロー記述を確認 | 4フェーズのオーケストレーションフローが明確に定義されている |
| E-02 | 成功基準2: 5つのエージェント定義の存在 | agents/ ディレクトリの5ファイルの存在と内容確認 | investigation-worker, design-worker, impl-plan-worker, impl-worker, impl-evaluator が存在する |
| E-03 | 成功基準3: テンプレートファイルの存在とフェーズプレフィックス番号 | sessions/impl/_template/ の全ファイルを Glob で確認し、番号体系の一貫性を検証 | 全テンプレートファイルが存在し、フェーズプレフィックス番号で整理されている |
| E-04 | 成功基準4: commit-message.md への種別追加 | commit-message.md を読み、impl-mgr, impl-worker, impl-evaluator の記載を確認 | 3種別がテーブルに追加され、例が含まれている |
| E-05 | 成功基準5: workflow.md への記述追加 | workflow.md を読み、l1-impl-manager セクションの存在と内容を確認 | 4フェーズ構成が可視化されている |
| E-06 | 成功基準6: session-flow-policy との整合性 | session-flow-policy のセッションタイプ一覧とマネージャー=スキル/ワーカー=エージェント構造を確認 | マネージャー=スキル、ワーカー=エージェントの構造が守られている |
| E-07 | SKILL.md の品質（manager-common-policy 参照） | SKILL.md 内の §2-§8 参照箇所を確認し、共通パターンの適切な参照を検証 | 共通パターンは参照で記述、固有ロジックのみ SKILL.md に記載 |
| E-08 | エージェント定義の品質（session-flow-policy §3 準拠） | 各エージェント定義に必須要素（役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）があるか確認 | 全必須要素が揃っている |
| E-09 | ペアリング対称性（session-flow-policy §3.2） | impl-evaluator の対称性確認テーブルを検証し、4ワーカーとの対称性を確認 | 壁打ち・計画・レポート・知見記録・課題起票・停止ルールが全エージェントで対称 |
| E-10 | 担当ファイルの重複分離 | 各エージェントの担当ファイルテーブルを突合し、書き込み権限の重複がないか確認 | 書き込み対象ファイルが重複なく分離されている |
| E-11 | 36_file_task_division.md テンプレートの品質 | IMPL-XXX 形式と Conflict Check Matrix のフォーマットを確認 | IMPL-XXX 形式のタスク定義と Conflict Check Matrix が含まれている |
| E-12 | 42_impl_work_report.md テンプレートの品質 | B+C 集約フォーマットの構成を確認 | Wave Summary, Per-Task Results, Escalations, Git Log Summary が含まれている |
| E-13 | メタルール横断検証: フロー記述の整合性 | SKILL.md のフロー記述と各エージェント定義の担当ファイルの一致を確認 | 不整合なし |
| E-14 | メタルール横断検証: workflow.md の同期 | workflow.md の記述が SKILL.md の実態と整合しているか確認 | 4フェーズ構成・並列ディスパッチ・B+C集約が正しく可視化されている |
| E-15 | メタルール横断検証: TG-008 基準連動 | triage-standard-policy のマトリクス・ペアリング構造・走査対象を確認 | l1-impl-manager 関連の追加が適切に行われている |

## 評価スケジュール
- 成功基準6項目の達成度評価（E-01〜E-06）
- 品質詳細評価（E-07〜E-12）
- メタルール横断検証（E-13〜E-15）
- 課題起票・知見記録

## 前提・制約
- 実際にコード実装施策を実行しての動作検証はスコープ外（静的レビューのみ）
- manager-common-policy §1 テーブルへの l1-impl-manager 追加は本施策のスコープ外（04_work_report.md に記載あり）

---
**作成者**: L2（評価）
**作成日**: 2026-03-12
