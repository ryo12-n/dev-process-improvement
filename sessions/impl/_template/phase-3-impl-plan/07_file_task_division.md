# File-Level Task Division: [施策名]

## Parallelism Analysis

- Maximum parallel workers: N
- Dependency graph: [describe]

## Task Assignments

### IMPL-001: [Short description]
- **Assigned files (CREATE)**: [files to create]
- **Assigned files (MODIFY)**: [files to modify with line hints]
- **Read-only dependencies**: [files to read but not modify]
- **Prerequisite tasks**: None / IMPL-XXX
- **Test command**: [specific test command]
- **Acceptance criteria**: [list of criteria]
- **Estimated complexity**: S/M/L

<!-- 追加タスクは同じフォーマットで IMPL-002, IMPL-003, ... と続ける -->

## Conflict Check Matrix

| File | IMPL-001 | IMPL-002 | ... |
|------|:--------:|:--------:|:---:|
| path/to/file | CREATE/MODIFY/READ/- | | |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。
競合がある場合は Prerequisite tasks で依存関係を設定し、別 Wave に分離する。

## Wave Assignment

### Wave 1 (並列実行可)
- IMPL-001, ...

### Wave 2 (Wave 1 完了後)
- IMPL-002 (depends on IMPL-001), ...

## Worktree Configuration

### Per-Worker Mapping

| Worker | Work Log | Issues | External Branch | Worktree Path |
|--------|----------|--------|-----------------|---------------|
| W1 | phase-4-impl/02_work_log_W1.md | 07_issues_W1.md | impl/<施策名>-W1 | <ext-repo>/.worktrees/impl-W1 |
| W2 | phase-4-impl/02_work_log_W2.md | 07_issues_W2.md | impl/<施策名>-W2 | <ext-repo>/.worktrees/impl-W2 |

<!-- ワーカー数に応じて行を追加 -->

## Summary

- Total tasks: N
- Total waves: N
- Estimated max parallelism: N workers

---
**作成者**: Impl Plan Worker
**作成日**: YYYY-MM-DD
