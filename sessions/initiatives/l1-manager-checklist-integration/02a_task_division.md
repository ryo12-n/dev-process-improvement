# File-Level Task Division: l1-manager-checklist-integration

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 1
- Dependency graph: なし（全タスク独立）

## Task Assignments

### T-001: l1-manager/SKILL.md に固定タスクを追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`
- **Read-only dependencies**: `.claude/skills/rule-change-checklist/SKILL.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**: 「タスクリストに含める固定タスク」セクションに条件付き固定タスクが追加されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: 連動更新（docs/workflow.md 等）
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `docs/workflow.md`（必要な場合）
- **Read-only dependencies**: `.claude/skills/rule-change-checklist/SKILL.md`（関連ファイル一覧）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**: 連動更新が必要なファイルが更新済み、または「連動更新不要」の判断が記録されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 |
|------|:-----:|:-----:|
| `.claude/skills/l1-manager/SKILL.md` | MODIFY | - |
| `docs/workflow.md` | - | MODIFY |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。
競合がある場合は Prerequisite tasks で依存関係を設定し、別 Wave に分離する。

## Wave Assignment

### Wave 1 (逐次実行)
- T-001, T-002（T-002 は T-001 完了後）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## Summary

- Total tasks: 2（+ 固定タスク T-003, T-004）
- Total waves: 1
- Estimated max parallelism: 1 worker
- Conflict count: 0

---
**作成者**: L1（壁打ちフェーズで作成）
**作成日**: 2026-03-18
