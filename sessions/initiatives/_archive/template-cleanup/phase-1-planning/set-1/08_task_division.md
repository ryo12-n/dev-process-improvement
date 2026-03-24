# File-Level Task Division: template-cleanup

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 3
- Dependency graph: なし（全タスク独立）

## Task Assignments

### T-001: initiatives テンプレートから 01_gate.md を削除

- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: なし
- **Assigned files (DELETE)**:
  - `sessions/initiatives/_template/phase-1-planning/01_gate.md`
  - `sessions/initiatives/_template/phase-2-execution/01_gate.md`
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `sessions/initiatives/_template/phase-1-planning/01_gate.md` が削除されている
  - `sessions/initiatives/_template/phase-2-execution/01_gate.md` が削除されている
  - 他セッションタイプ（triage, metacognition 等）の `01_gate.md` は変更されていない
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: スキル・ルールの更新（_template/ 削除ステップ追加 + 01_gate.md 参照除去）

- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**:
  - `.claude/skills/l1-manager/SKILL.md` — 「事前準備」セクション（L125-127 付近: `phase-2-execution/_template/ を set-N/ にコピー` の直後）に `_template/` 削除ステップを追加
  - `.claude/rules/parallel-dev.md` — §2.1「set ディレクトリの作成」セクション（L29 付近: `_template/ を set-N/ にコピー` の直後）に `_template/` 削除ステップを追加
  - `.claude/skills/session-lifecycle-policy/SKILL.md` — §1.4.3 Initiative テンプレート構成:
    - 基本モデルツリー（L123: `01_gate.md` 行）を削除
    - Initiative ツリー内の phase-1-planning（L193: `01_gate.md` 行）を削除
    - Initiative ツリー内の phase-2-execution（L205: `01_gate.md` 行）を削除
    - 構造上の特徴コメント（L216 付近）から `_template/` 削除に関する記述を追加（任意）
- **Read-only dependencies**:
  - `sessions/initiatives/template-cleanup/01_proposal.md`
  - `sessions/initiatives/template-cleanup/02_plan.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `l1-manager/SKILL.md` の set コピー手順に `_template/` 削除ステップが含まれている
  - `parallel-dev.md` §2.1 に `_template/` 削除が明記されている
  - `session-lifecycle-policy/SKILL.md` §1.4.3 から initiatives の `01_gate.md` が除去されている
  - 基本モデル（§1.4 冒頭ツリー）の `01_gate.md` は 3-phase 共通なので残す（initiatives 固有の §1.4.3 のみ除去）
  - `session-flow-policy/SKILL.md` は変更されていない（initiatives 固有の `01_gate.md` 記述がないため）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: 可視化文書・整合性リファレンスの連動更新

- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**:
  - `docs/workflow.md` — イニシアティブセッションフローの並列ディスパッチ部分（L58 付近: `_template/ を set-N/ にコピー` の直後）に `_template/` 削除ステップを追加
  - `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` — §4 テンプレート一覧テーブル initiatives 行（L122 付近）のファイル数を更新（phase-N/ 内の構成変更を反映）
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/SKILL.md`（T-002 の変更内容を正の情報源として参照）
  - `.claude/skills/session-lifecycle-policy/SKILL.md`（T-002 の変更内容を正の情報源として参照）
- **Prerequisite tasks**: None（並列実行可能。ただし T-002 と同時に作業する場合、変更前の正の情報源を参照してしまうリスクあり。各ワーカーは `02_plan.md` の変更仕様を共有情報源として使えばよい）
- **Acceptance criteria**:
  - `docs/workflow.md` のイニシアティブフローに `_template/` 削除ステップが追加されている
  - `session-consistency-reference.md` の initiatives テンプレート構成が `01_gate.md` 除去後の状態に更新されている
  - `docs/workflow.md` の 3-phase セッションフロー（config-optimization, session-consistency）の `01_gate.md` 記述は変更されていない
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 |
|------|:-----:|:-----:|:-----:|
| `sessions/initiatives/_template/phase-1-planning/01_gate.md` | DELETE | - | - |
| `sessions/initiatives/_template/phase-2-execution/01_gate.md` | DELETE | - | - |
| `.claude/skills/l1-manager/SKILL.md` | - | MODIFY | - |
| `.claude/rules/parallel-dev.md` | - | MODIFY | - |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | - | MODIFY | - |
| `docs/workflow.md` | - | - | MODIFY |
| `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` | - | - | MODIFY |

**凡例**: CREATE = 新規作成, MODIFY = 変更, DELETE = 削除, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE, MODIFY, または DELETE を持つ場合は競合。
**競合検出結果**: 競合なし。全タスクのファイル割当が完全に分離されている。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001, T-002, T-003

全タスクが独立しており、ファイル競合もないため、単一 Wave で並列実行可能。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 標準的なファイル削除・テキスト編集のみで、専門知識は不要 | Worker |
| なし | - | 整合性確認は 02_plan.md の成功基準に基づく照合のみ | Evaluator |

## Summary

- Total tasks: 3
- Total waves: 1
- Estimated max parallelism: 3 workers
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE/DELETE なし）

### 注意事項
- `session-flow-policy/SKILL.md` は `02_plan.md` に変更対象として挙がっているが、調査の結果 initiatives 固有の `01_gate.md` 記述は存在せず、記載されている `01_gate.md` は 3-phase 標準構成（triage, config-optimization 等）のもの。スコープ外のため変更不要と判断した。L1 はこの判断の妥当性を確認すること
- `session-lifecycle-policy/SKILL.md` の基本モデル（§1.4 冒頭の `multi-phase manager パターン`）は 3-phase 共通モデルであり、initiatives 固有ではないため `01_gate.md` を残す。§1.4.3 の initiatives 固有ツリーのみから除去する

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-24
