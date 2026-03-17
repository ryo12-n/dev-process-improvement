# File-Level Task Division: backlog-to-issue-status-sync

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 3
- Dependency graph: なし（全タスク独立）

## Task Assignments

### T-001: backlog-to-issue.yml の scheduled-create ジョブ修正
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `.github/workflows/backlog-to-issue.yml` (L105-108: permissions、L127: --state all → --state open、L150-171: issue起票後にステータス更新ステップ追加)
- **Read-only dependencies**: `.claude/rules/gha-workflow-security.md`、`backlog/entries/` 配下のエントリ形式（sed 置換対象の確認）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `--state all` が `--state open` に変更されている
  - issue 起票成功後にエントリ .md のステータスを「起票済み」に更新する sed ステップが追加されている
  - git commit & push ステップが追加されている
  - `contents: write` 権限が追加されている
  - GHA セキュリティチェックリスト（`${{ }}` 直接展開なし、`env:` 経由）に準拠
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: generate-csvs.py の STATUS_MAP 追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `scripts/generate-csvs.py` (L210-215: STATUS_MAP に `"起票済み": "起票済み"` を追加)
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - STATUS_MAP に `"起票済み": "起票済み"` が追加されている
  - 既存のマッピング（候補、initiative 開始済、進行中、完了）が影響を受けていない
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: backlog/README.md のステータス値説明更新
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `backlog/README.md` (L18: ステータス列の説明に「起票済み」を追加)
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - ステータス値の説明に「起票済み」が追加されている
  - 既存の説明（候補 / initiative 開始済）が維持されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 |
|------|:-----:|:-----:|:-----:|
| `.github/workflows/backlog-to-issue.yml` | MODIFY | - | - |
| `scripts/generate-csvs.py` | - | MODIFY | - |
| `backlog/README.md` | - | - | MODIFY |
| `.claude/rules/gha-workflow-security.md` | READ | - | - |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: 競合なし。全タスクが異なるファイルを MODIFY するため、並列実行可能。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001, T-002, T-003

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業のため | Worker |
| なし | - | プロセス改善の定型作業のため | Evaluator |

## Summary

- Total tasks: 3
- Total waves: 1
- Estimated max parallelism: 3 workers
- Conflict count: 0

---
**作成者**: L2 計画ワーカー（L1 が API エラー後に補完）
**作成日**: 2026-03-17
