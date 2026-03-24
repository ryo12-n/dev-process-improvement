# File-Level Task Division: ai-dev-chain-bootstrap

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 3
- Dependency graph: T-002（project-init Skill）は T-001（テンプレート作成）を READ 参照するため依存関係あり。T-003 は独立。

## Task Assignments

### T-001: `projects/_template/` ディレクトリと全プレースホルダーファイル作成

- **Assigned files (CREATE)**:
  - `projects/_template/request.md`
  - `projects/_template/backlog.md`
  - `projects/_template/artifacts/requirements.json`
  - `projects/_template/artifacts/requirements.md`
  - `projects/_template/artifacts/openapi.yaml`
  - `projects/_template/artifacts/design.md`
  - `projects/_template/artifacts/tests.json`
  - `projects/_template/artifacts/tests.md`
  - `projects/_template/artifacts/tasks.json`
  - `projects/_template/artifacts/ci/pipeline.yaml`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**:
  - `refs/ai-dev-chain/overview.md`（リポジトリ追加構成セクション — ディレクトリ構造の参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 全 10 ファイルが作成されている
  - `request.md` に要望書記入フォーマット（セクション見出し + 記入ガイド）が含まれている
  - `backlog.md` に進捗管理テンプレート（ステータス一覧 + 更新ルール）が含まれている
  - `artifacts/` 配下の各ファイルが最小限のプレースホルダー構造を持つ（空ファイルではなく、スキーマ or セクション骨格）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: `project-init` Skill の SKILL.md 骨格作成

- **Assigned files (CREATE)**:
  - `.claude/skills/project-init/SKILL.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/SKILL.md`（フロントマター構造の参照）
  - `refs/ai-dev-chain/overview.md`（Skill 仕様の参照）
  - `projects/_template/`（コピー対象ディレクトリの構成確認）
- **Prerequisite tasks**: T-001（`projects/_template/` が存在する必要がある）
- **Acceptance criteria**:
  - YAML フロントマター（`name: project-init`, `description`, `user-invocable: true`）が正しく設定されている
  - 引数仕様（`<project-name>`、なしの場合はユーザーへ質問）が記載されている
  - 処理フロー（`projects/_template/` を `projects/<project-name>/` にコピー）が記載されている
  - TODO コメントで後続実装箇所が明示されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: 5 gen-* Skills の SKILL.md 骨格作成

- **Assigned files (CREATE)**:
  - `.claude/skills/gen-req/SKILL.md`
  - `.claude/skills/gen-design/SKILL.md`
  - `.claude/skills/gen-tests/SKILL.md`
  - `.claude/skills/gen-ci/SKILL.md`
  - `.claude/skills/gen-tasks/SKILL.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**:
  - `.claude/skills/l1-manager/SKILL.md`（フロントマター構造の参照）
  - `refs/ai-dev-chain/overview.md`（各 Skill の入出力仕様の参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 5 ファイル全てに YAML フロントマター（`name`, `description`, `user-invocable: true`）が正しく設定されている
  - 各 Skill に引数仕様（`<project-path>`、なしの場合はユーザーへ質問）が記載されている
  - 各 Skill に入出力仕様（overview.md の Skills 一覧に準拠）が記載されている
  - 各 Skill にチェーン内の前後関係（前工程の成果物を入力とし、自工程の成果物を出力する旨）が記載されている
  - TODO コメントで後続実装箇所が明示されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 |
|------|:-----:|:-----:|:-----:|
| `projects/_template/request.md` | CREATE | - | - |
| `projects/_template/backlog.md` | CREATE | - | - |
| `projects/_template/artifacts/requirements.json` | CREATE | - | - |
| `projects/_template/artifacts/requirements.md` | CREATE | - | - |
| `projects/_template/artifacts/openapi.yaml` | CREATE | - | - |
| `projects/_template/artifacts/design.md` | CREATE | - | - |
| `projects/_template/artifacts/tests.json` | CREATE | - | - |
| `projects/_template/artifacts/tests.md` | CREATE | - | - |
| `projects/_template/artifacts/tasks.json` | CREATE | - | - |
| `projects/_template/artifacts/ci/pipeline.yaml` | CREATE | - | - |
| `projects/_template/` (directory) | - | READ | - |
| `.claude/skills/project-init/SKILL.md` | - | CREATE | - |
| `.claude/skills/gen-req/SKILL.md` | - | - | CREATE |
| `.claude/skills/gen-design/SKILL.md` | - | - | CREATE |
| `.claude/skills/gen-tests/SKILL.md` | - | - | CREATE |
| `.claude/skills/gen-ci/SKILL.md` | - | - | CREATE |
| `.claude/skills/gen-tasks/SKILL.md` | - | - | CREATE |
| `refs/ai-dev-chain/overview.md` | READ | READ | READ |
| `.claude/skills/l1-manager/SKILL.md` | - | READ | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: 競合なし。全タスクの CREATE 対象ファイルは完全に分離されている。T-002 は T-001 の成果物を READ するため依存関係あり（Wave 分離で対応）。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001（テンプレート作成）, T-003（5 gen-* Skills 作成）

### Wave 2 (Wave 1 完了後)
- T-002（project-init Skill 作成 — T-001 の `projects/_template/` を READ 参照するため）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 汎用ファイル作成のためドメイン特化不要 | Worker |
| なし | - | 汎用ファイル作成のためドメイン特化不要 | Evaluator |

## Summary

- Total tasks: 3
- Total waves: 2
- Estimated max parallelism: 2 workers（Wave 1 で T-001 と T-003 を並列実行）
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）

### 設計判断の補足

1. **T-001 を 1 タスクにまとめた理由**: `projects/_template/` 配下の 10 ファイルは全て新規作成かつ相互依存なし。個別タスクに分けると管理オーバーヘッドが増すだけなので、1 ワーカーに一括で割り当てる方が効率的。
2. **T-003 を 1 タスクにまとめた理由**: 5 gen-* Skills は構造が同一（フロントマター + 引数仕様 + 入出力仕様 + TODO）で、1 ワーカーがテンプレートを作って横展開する方が品質・効率ともに良い。
3. **T-002 を Wave 2 にした理由**: project-init は `_template/` の構成を把握した上で SKILL.md を書く必要がある。T-001 が先に完了していれば、ワーカーは実際のディレクトリ構成を参照して正確な処理フローを記述できる。

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-24
