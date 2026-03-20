# File-Level Task Division: [施策名]

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: N
- Dependency graph: [describe or "なし（全タスク独立）"]

## Task Assignments

### T-001: [Short description]
- **Assigned files (CREATE)**: [files to create]
- **Assigned files (MODIFY)**: [files to modify with line hints]
- **Read-only dependencies**: [files to read but not modify]
- **Prerequisite tasks**: None / T-XXX
- **Acceptance criteria**: [list of criteria]
- **Estimated complexity**: S/M/L
- **Recommended domain agent (Worker)**: [agent name or なし]
- **Recommended domain agent (Evaluator)**: [agent name or なし]

### T-002: [Short description]
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: -
- **Read-only dependencies**: -
- **Prerequisite tasks**: None / T-XXX
- **Acceptance criteria**: -
- **Estimated complexity**: S/M/L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | ... |
|------|:-----:|:-----:|:-----:|:---:|
| path/to/file_a | CREATE | - | READ | ... |
| path/to/file_b | MODIFY | MODIFY | - | ... |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。
競合がある場合は Prerequisite tasks で依存関係を設定し、別 Wave に分離する。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001, T-003, ...

### Wave 2 (Wave 1 完了後)
- T-002 (depends on T-001), ...

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## Summary

- Total tasks: N
- Total waves: N
- Estimated max parallelism: N workers
- Conflict count: N（同一ファイルへの複数 MODIFY/CREATE）

---
**作成者**: L2 計画ワーカー
**作成日**: YYYY-MM-DD
