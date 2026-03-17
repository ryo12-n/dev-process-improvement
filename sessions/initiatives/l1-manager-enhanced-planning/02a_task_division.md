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
**作成者**: L2-plan-worker
**作成日**: 2026-03-17
