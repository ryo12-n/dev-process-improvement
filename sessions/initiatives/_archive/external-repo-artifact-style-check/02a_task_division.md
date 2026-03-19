# File-Level Task Division: external-repo-artifact-style-check

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 1
- Dependency graph: なし（全タスク独立）

## Task Assignments

### T-001: l2-worker.md への記法スタイル確認項目追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-worker.md`
- **Read-only dependencies**: -
- **Prerequisite tasks**: None
- **Acceptance criteria**: 「外部リポジトリでの作業手順 > 作業前チェック」に記法スタイル確認項目が追加されていること
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: 連動更新対象ファイルの確認・更新
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: （T-002 実施後に判明）
- **Read-only dependencies**: `.claude/skills/l1-manager/agents/l2-worker.md`（「関連ファイル一覧」セクション）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**: 全連動更新対象ファイルの確認が完了し、必要なファイルが更新されていること
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: 知見・課題記録
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `sessions/initiatives/external-repo-artifact-style-check/07_issues.md`, `sessions/initiatives/external-repo-artifact-style-check/04_work_report.md`
- **Read-only dependencies**: -
- **Prerequisite tasks**: T-001, T-002
- **Acceptance criteria**: 知見・課題がファイルに記録され、CSV 転記判定が完了していること
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 |
|------|:-----:|:-----:|:-----:|
| `.claude/skills/l1-manager/agents/l2-worker.md` | MODIFY | READ | - |
| `sessions/initiatives/external-repo-artifact-style-check/07_issues.md` | - | - | MODIFY |
| `sessions/initiatives/external-repo-artifact-style-check/04_work_report.md` | - | - | MODIFY |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。

競合なし → 全タスクは Wave 1 で逐次実行可能（T-002 は T-001 に依存）

## Wave Assignment

### Wave 1 (逐次実行)
- T-001 → T-002 → T-003

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## Summary

- Total tasks: 3
- Total waves: 1
- Estimated max parallelism: 1 worker
- Conflict count: 0

---
**作成者**: L2 計画ワーカー
**作成日**: YYYY-MM-DD
