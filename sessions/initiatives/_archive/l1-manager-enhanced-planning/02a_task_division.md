# File-Level Task Division: l1-manager-enhanced-planning

## 施策フェーズ2: 並列ワーカーディスパッチ

### Parallelism Analysis
- Maximum parallel workers: 4（Wave 2 の T2-002〜T2-005）
- Dependency graph: T2-001 → {T2-002, T2-003, T2-004, T2-005} → {T2-006, T2-007}
- 設計方針: dev-process-improvement は文書中心リポジトリのため、git worktree による物理隔離は不要。per-worker ファイル分離（`03_work_log_W<N>.md`, `07_issues_W<N>.md`）で競合を回避する方式を採用（git-worktree-guideline §4 の判断に準拠）

### Task Assignments

#### T2-001: parallel-dev.md（並列開発ルール）の新規作成
- **Assigned files (CREATE)**: `.claude/rules/parallel-dev.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `.claude/skills/l1-impl-manager/SKILL.md`（並列ディスパッチ機構の参考パターン）、`docs/git-worktree-guideline.md`（worktree 判断基準）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 並列ディスパッチの前提条件（Conflict Check Matrix 検証済み・Wave 割当定義済み・per-worker ファイル作成済み）が定義されている
  - per-worker ファイル分離パターン（03_work_log_W<N>.md, 07_issues_W<N>.md）が定義されている
  - Wave 方式の運用ルール（Wave 内は並列、Wave 間は逐次）が定義されている
  - 成果物統合手順（per-worker ファイル → 本体ファイルへの統合）が定義されている
  - worktree 方式への escalation パス（将来の拡張用フック）が記載されている
  - manager-common-policy §2.2 からの参照に応答できる構造になっている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T2-002: l1-manager SKILL.md の Phase 4 並列ディスパッチ機構追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`（Phase 4 セクション、L2 への指示の出し方セクション）
- **Read-only dependencies**: `.claude/rules/parallel-dev.md`（T2-001 の成果物）、`.claude/skills/l1-impl-manager/SKILL.md`（参考パターン）
- **Prerequisite tasks**: T2-001
- **Acceptance criteria**:
  - Phase 4 セクションに並列ディスパッチの事前準備手順（per-worker ファイル作成、Conflict Check Matrix 検証）が記載されている
  - Wave ディスパッチ手順（同一 Wave 内の複数 worker を並列起動）が記載されている
  - Wave 完了後処理（per-worker ファイル統合、成果物確認）が記載されている
  - L2-worker 起動時に渡す per-worker 固有情報（Worker ID、per-worker ファイルパス）が明記されている
  - セッションライフサイクル todo にパターン1 の並列ディスパッチステップが反映されている
  - 関連ファイル一覧に parallel-dev.md が追加されている
- **Estimated complexity**: L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T2-003: l2-worker.md の per-worker ファイル対応
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-worker.md`（担当ファイル、壁打ちフェーズ、作業フロー）
- **Read-only dependencies**: `.claude/rules/parallel-dev.md`（T2-001 の成果物）
- **Prerequisite tasks**: T2-001
- **Acceptance criteria**:
  - 担当ファイルテーブルに per-worker ファイル（`03_work_log_W<N>.md`, `07_issues_W<N>.md`）が追加されている
  - 壁打ちフェーズのチェック内容に「Worker ID の確認」「per-worker ファイルの存在確認」が追加されている
  - 作業フローに「per-worker ファイルへの記録」の手順が追加されている（並列実行時は本体ファイルではなく per-worker ファイルに記録）
  - 「やること」に per-worker ファイルへの記録が追加されている
  - 順次実行時（従来方式）との判別条件が明記されている（Worker ID が指定されている場合は per-worker ファイルを使用）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T2-004: テンプレート群の更新（per-worker テンプレート追加 + 02_tasks.md 拡張）
- **Assigned files (CREATE)**: `sessions/initiatives/_template/03_work_log_W_template.md`, `sessions/initiatives/_template/07_issues_W_template.md`
- **Assigned files (MODIFY)**: `sessions/initiatives/_template/02_tasks.md`（Set Dispatch Order に並列/逐次の区分を追加）、`sessions/initiatives/_template/03_work_log.md`（per-worker テンプレート参照注記追加）
- **Read-only dependencies**: `.claude/rules/parallel-dev.md`（T2-001 の成果物）
- **Prerequisite tasks**: T2-001
- **Acceptance criteria**:
  - `03_work_log_W_template.md` が作成され、Worker ID・担当タスク・per-worker 固有の壁打ちフェーズ・作業ログセクションを含む
  - `07_issues_W_template.md` が作成され、Worker ID・課題起票セクションを含む
  - `02_tasks.md` テンプレートの Set Dispatch Order に「並列/逐次」区分が追加されている
  - `03_work_log.md` テンプレートに per-worker テンプレートの存在と使い分けに関する注記が追加されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T2-005: manager-common-policy + session-flow-policy の更新
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/manager-common-policy/SKILL.md`（§2.2 並列ディスパッチ条件の詳細化）、`.claude/skills/session-flow-policy/SKILL.md`（§4.2 並列ディスパッチ条件の更新）
- **Read-only dependencies**: `.claude/rules/parallel-dev.md`（T2-001 の成果物）
- **Prerequisite tasks**: T2-001
- **Acceptance criteria**:
  - manager-common-policy §2.2 に per-worker ファイル分離パターンの説明と parallel-dev.md への参照が追加されている
  - manager-common-policy §2.2 に Wave 完了後の成果物統合手順への言及が追加されている
  - session-flow-policy §4.2 に per-worker ファイル作成が前提条件として追加されている
  - session-flow-policy §4.2 の条件リストに「per-worker ファイルが作成されていること」が追加されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T2-006: 固定タスク — 知見記録 + CSV 転記 + メタルール横断検証
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `04_work_report.md`（知見セクション追記）、`07_issues.md`（課題確認・転記判断追記）
- **Read-only dependencies**: 全成果物ファイル（T2-001〜T2-005 の成果物を検証）
- **Prerequisite tasks**: T2-001〜T2-005
- **Acceptance criteria**:
  - `04_work_report.md` の「作業中の知見」セクションに「ルール化候補」「参考情報」各1行以上の記載がある
  - `07_issues.md` の課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている
  - メタルール横断検証3領域の結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている
    - メタルールフロー記述: parallel-dev.md を参照しているスキル・エージェント定義のフロー記述が実態と一致
    - workflow.md 同期: docs/workflow.md の並列ディスパッチ関連記述が変更内容と整合
    - TG-008 基準連動: triage-standard-policy の走査対象に parallel-dev.md が追加（必要な場合）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T2-007: docs/workflow.md の並列ディスパッチ可視化更新
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `docs/workflow.md`（イニシアティブフローの Phase 4 セクションに並列ディスパッチの可視化を追加）
- **Read-only dependencies**: `.claude/skills/l1-manager/SKILL.md`（T2-002 の成果物）、`.claude/rules/parallel-dev.md`（T2-001 の成果物）
- **Prerequisite tasks**: T2-001, T2-002
- **Acceptance criteria**:
  - docs/workflow.md の Phase 4 セクションに並列ディスパッチの流れ（Wave 方式・per-worker ファイル分離・成果物統合）が可視化されている
  - 逐次ディスパッチとの判断基準が記載されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### Conflict Check Matrix

| File | T2-001 | T2-002 | T2-003 | T2-004 | T2-005 | T2-006 | T2-007 |
|------|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| `.claude/rules/parallel-dev.md` | CREATE | READ | READ | READ | READ | READ | READ |
| `.claude/skills/l1-manager/SKILL.md` | - | MODIFY | - | - | - | READ | READ |
| `.claude/skills/l1-manager/agents/l2-worker.md` | - | - | MODIFY | - | - | READ | - |
| `_template/02_tasks.md` | - | - | - | MODIFY | - | - | - |
| `_template/03_work_log.md` | - | - | - | MODIFY | - | - | - |
| `_template/03_work_log_W_template.md` | - | - | - | CREATE | - | - | - |
| `_template/07_issues_W_template.md` | - | - | - | CREATE | - | - | - |
| `manager-common-policy/SKILL.md` | - | - | - | - | MODIFY | READ | - |
| `session-flow-policy/SKILL.md` | - | - | - | - | MODIFY | READ | - |
| `04_work_report.md` | - | - | - | - | - | MODIFY | - |
| `07_issues.md` | - | - | - | - | - | MODIFY | - |
| `docs/workflow.md` | - | - | - | - | - | READ | MODIFY |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つケースはなし。全タスクのファイル書き込み先が分離されている。

### Wave Assignment

#### Wave 1 (先行実行 — 他タスクの依存先)
- T2-001: parallel-dev.md 新規作成

#### Wave 2 (Wave 1 完了後 — 並列実行可)
- T2-002: l1-manager SKILL.md 変更
- T2-003: l2-worker.md 変更
- T2-004: テンプレート群の更新
- T2-005: manager-common-policy + session-flow-policy 変更
- T2-007: docs/workflow.md 更新

#### Wave 3 (Wave 2 完了後)
- T2-006: 固定タスク（知見記録・CSV 転記・メタルール横断検証）

### Domain Agent Recommendations
施策フェーズ2 はプロセス改善の定型作業（ルール追加・スキル更新・テンプレート拡張）であるため、ドメインエージェント参照は不要。

### Summary
- Total tasks: 7
- Total waves: 3
- Estimated max parallelism: 5 workers（Wave 2）
- 新規作成ファイル: 3（parallel-dev.md, 03_work_log_W_template.md, 07_issues_W_template.md）
- 変更ファイル: 7（SKILL.md, l2-worker.md, 02_tasks.md テンプレート, 03_work_log.md テンプレート, manager-common-policy, session-flow-policy, docs/workflow.md）
- 設計方針: per-worker ファイル分離方式（worktree 不要）。impl-manager のハイブリッド方式を l1-manager 向けに簡略化

---

## 施策フェーズ3: ドメインエージェント深層統合

### Parallelism Analysis
- Maximum parallel workers: 5（Wave 1 の T3-001〜T3-005）
- Dependency graph: {T3-001, T3-002, T3-003, T3-004, T3-005} → {T3-006, T3-007}
- 設計方針: l2-worker.md の既存ドメインエージェント参照パターン（作業フロー step 1 で `refs/agency-agents/<部門>/<エージェント名>.md` を Read し、専門知識として参照）を l2-evaluator.md に対称的に拡張する。加えて、Evaluator の評価結果を knowledge.md にフィードバックするループを構築する

### Task Assignments

#### T3-001: l2-evaluator.md にドメインエージェント参照フローを追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-evaluator.md`（作業フロー step 1、壁打ちフェーズ、担当ファイル、やること）
- **Read-only dependencies**: `.claude/skills/l1-manager/agents/l2-worker.md`（既存パターンの参照）、`refs/agency-agents/knowledge.md`（カタログ構造の参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 作業フロー step 1 に「`02_tasks.md` の『参照ドメインエージェント』セクションの Evaluator 向けエージェントを Read し、専門的な観点・チェックリスト・ベストプラクティスを評価に活かす」手順が追加されている
  - 壁打ちフェーズの前提条件チェックに「参照ドメインエージェントの確認:（指定あり / なし）」が追加されている
  - 担当ファイルテーブルに `refs/agency-agents/` が読み取りのみとして追加されている
  - 「やること」セクションにドメインエージェント参照が追加されている
  - l2-worker.md のパターンとの対称性が保たれている（「エージェントの役割を引き受けるのではなく、専門知識として参照するだけ」制約が明記）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T3-002: l1-manager SKILL.md の L2-evaluator ディスパッチ手順にドメインエージェント参照伝達を明記
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`（Phase 5 L2-evaluator ディスパッチセクション、起動時に渡す観点セクション）
- **Read-only dependencies**: `.claude/skills/manager-common-policy/SKILL.md`（§10.3 の渡し方参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - Phase 5 の evaluator ディスパッチ手順に「`02_tasks.md` の Evaluator 向けドメインエージェントが指定されている場合、エージェントのパスと参照理由を L2-evaluator に伝達する」手順が明記されている
  - 起動時に渡す観点に「参照ドメインエージェント（Evaluator 向け、任意）」が追加されている
  - manager-common-policy §10.3 への参照が含まれている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T3-003: manager-common-policy §10 に Evaluator 向け具体的手順を追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.claude/skills/manager-common-policy/SKILL.md`（§10 セクション — §10.5 を新設）
- **Read-only dependencies**: `.claude/skills/l1-manager/agents/l2-evaluator.md`（Evaluator の作業フロー参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - §10.5「Evaluator 向けドメインエージェント参照の具体的手順」が新設されている
  - Evaluator 固有の参照観点（評価計画への反映方法・評価基準への活用方法）が記載されている
  - Worker 向け（§10.3 の既存内容）との差異が明確に区別されている
  - ドメインエージェント有効性フィードバックの責務（Evaluator → knowledge.md へのルーティング）が定義されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T3-004: テンプレート群の更新（05_eval_plan.md + 06_eval_report.md）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `sessions/initiatives/_template/05_eval_plan.md`（ドメインエージェント参照セクション追加）、`sessions/initiatives/_template/06_eval_report.md`（ドメインエージェント有効性フィードバックセクション追加）
- **Read-only dependencies**: `sessions/initiatives/_template/03_work_log.md`（Worker 側のドメインエージェント参照パターン参考）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `05_eval_plan.md` に「参照ドメインエージェント」セクションが追加され、エージェント名・参照パス・評価への活用方針を記載する欄がある
  - `06_eval_report.md` に「ドメインエージェント有効性フィードバック」セクションが追加され、以下の欄がある:
    - 参照したドメインエージェント名
    - 有効だった観点（評価品質向上に寄与した具体的観点）
    - 不要/ノイズだった観点
    - knowledge.md への推奨更新事項（推奨マッピングの追加/削除/変更）
  - 既存セクションの構造を壊さない
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T3-005: refs/agency-agents/knowledge.md に Evaluator 向け推奨マッピングを追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `refs/agency-agents/knowledge.md`（施策タイプ別推奨マッピングセクションの拡張）
- **Read-only dependencies**: `.claude/skills/l1-manager/agents/l2-evaluator.md`（Evaluator の評価フロー参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 施策タイプ別推奨マッピングテーブルに「Evaluator 向け推奨」列が追加されている、または Evaluator 向け別建てテーブルが作成されている
  - Worker 向けと Evaluator 向けで異なるエージェントが推奨される施策タイプが明確に区別されている（例: ルール変更は Worker に specialized-workflow-architect、Evaluator に testing-workflow-optimizer）
  - フィードバック受領セクション（Evaluator の 06_eval_report.md から知見を蓄積するためのテーブル構造）が追加されている
  - 既存の Worker 向け推奨は変更しない
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T3-006: 固定タスク — 知見記録 + CSV 転記 + メタルール横断検証
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `04_work_report.md`（知見セクション追記）、`07_issues.md`（課題確認・転記判断追記）
- **Read-only dependencies**: 全成果物ファイル（T3-001〜T3-005 の成果物を検証）
- **Prerequisite tasks**: T3-001〜T3-005
- **Acceptance criteria**:
  - `04_work_report.md` の「作業中の知見」セクションに「ルール化候補」「参考情報」各1行以上の記載がある
  - `07_issues.md` の課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている
  - メタルール横断検証3領域の結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている
    - メタルールフロー記述: l2-evaluator.md を参照している l1-manager SKILL.md・manager-common-policy のフロー記述が実態と一致
    - workflow.md 同期: docs/workflow.md の Phase 5 セクションがドメインエージェント参照を反映
    - TG-008 基準連動: triage-standard-policy の走査対象・チェック基準がドメインエージェント関連の変更を反映（必要な場合）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

#### T3-007: docs/workflow.md にドメインエージェント深層統合の可視化を追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `docs/workflow.md`（Phase 5 評価ワーカーディスパッチセクションにドメインエージェント参照行追加、ドメインエージェントフィードバックループの可視化追加）
- **Read-only dependencies**: `.claude/skills/l1-manager/agents/l2-evaluator.md`（T3-001 の成果物）、`.claude/skills/manager-common-policy/SKILL.md`（T3-003 の成果物）
- **Prerequisite tasks**: T3-001, T3-003
- **Acceptance criteria**:
  - Phase 5 の評価ワーカーセクションに「参照ドメインエージェントがある場合: 02_tasks.md の Evaluator 向け指定に従いエージェント定義を Read」行が追加されている
  - ドメインエージェントフィードバックループ（06_eval_report.md → knowledge.md）の可視化が追加されている
  - manager-common-policy §10 のサマリーテーブルにフィードバックループの記載が追加されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### Conflict Check Matrix

| File | T3-001 | T3-002 | T3-003 | T3-004 | T3-005 | T3-006 | T3-007 |
|------|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| `.claude/skills/l1-manager/agents/l2-evaluator.md` | MODIFY | - | - | - | - | READ | - |
| `.claude/skills/l1-manager/SKILL.md` | - | MODIFY | - | - | - | READ | - |
| `.claude/skills/manager-common-policy/SKILL.md` | - | - | MODIFY | - | - | READ | READ |
| `_template/05_eval_plan.md` | - | - | - | MODIFY | - | - | - |
| `_template/06_eval_report.md` | - | - | - | MODIFY | - | - | - |
| `refs/agency-agents/knowledge.md` | - | - | - | - | MODIFY | READ | - |
| `04_work_report.md` | - | - | - | - | - | MODIFY | - |
| `07_issues.md` | - | - | - | - | - | MODIFY | - |
| `docs/workflow.md` | - | - | - | - | - | READ | MODIFY |
| `.claude/skills/l1-manager/agents/l2-worker.md` | READ | - | - | - | - | - | - |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つケースはなし。全タスクのファイル書き込み先が分離されている。

### Wave Assignment

#### Wave 1 (並列実行可 — ファイル書き込み先が完全分離)
- T3-001: l2-evaluator.md ドメインエージェント参照フロー追加
- T3-002: l1-manager SKILL.md evaluator ディスパッチ手順更新
- T3-003: manager-common-policy §10.5 新設
- T3-004: テンプレート群更新（05_eval_plan.md + 06_eval_report.md）
- T3-005: knowledge.md Evaluator 向け推奨マッピング追加

#### Wave 2 (Wave 1 完了後)
- T3-006: 固定タスク（知見記録・CSV 転記・メタルール横断検証）
- T3-007: docs/workflow.md ドメインエージェント深層統合可視化

### Domain Agent Recommendations
施策フェーズ3 はドメインエージェント統合の仕組み構築（メタ作業）であるため、ドメインエージェント参照は不要。ドメインエージェントの「使い方」を設計する施策であり、ドメインエージェント自体を参照する施策ではない。

### Summary
- Total tasks: 7
- Total waves: 2
- Estimated max parallelism: 5 workers（Wave 1）
- 新規作成ファイル: 0
- 変更ファイル: 7（l2-evaluator.md, SKILL.md, manager-common-policy, 05_eval_plan.md テンプレート, 06_eval_report.md テンプレート, knowledge.md, docs/workflow.md）
- 設計方針: l2-worker.md の既存ドメインエージェント参照パターンを l2-evaluator.md に対称的に拡張。加えて、06_eval_report.md → knowledge.md のフィードバックループを構築し、ドメインエージェント推奨の継続的改善を実現する

---
**作成者**: L2-plan-worker
**作成日**: 2026-03-17
