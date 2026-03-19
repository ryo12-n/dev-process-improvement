# File-Level Task Division: gha-workflow-ux-improvements

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 4（Wave 1 の T-001〜T-004）
- Dependency graph: T-005（README 全面更新）は T-001〜T-004 の完了に依存。T-001〜T-004 は互いに独立（変更対象ファイルが重複しない）。

## Task Assignments

### T-001: initiative-dispatcher.yml — `@ai-task` → `@ai` 変更 + feedback 伝播追加

- **Assigned files (MODIFY)**:
  - `.github/workflows/initiative-dispatcher.yml`
    - ステップ `dispatch` ジョブの `if` 条件: `@ai-task` → `@ai`（L12）
    - ステップ `Parse command`: `@ai-task` → `@ai`（コメント L35、grep パターン L36、sed パターン L47）
    - ステップ `Route and dispatch`:
      - `start` case: `gh workflow run initiative-wallbash.yml` に `-f feedback="$ARGS"` を追加（L143-144）
      - `approve` + `gate-review` case: `gh workflow run initiative-close.yml` に `-f feedback="$ARGS"` を追加（L190-193）
    - ステップ `Route and dispatch`: エラーメッセージ内の `@ai-task` → `@ai`（L40, L241 の `error_message`）
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  1. `@ai-task` が dispatcher.yml 内に残っていないこと
  2. `/start` ディスパッチ時に `feedback` パラメータが wallbash に渡されること
  3. `/approve`（gate-review）ディスパッチ時に `feedback` パラメータが close に渡されること
  4. 全エラーメッセージが `@ai` を参照していること
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: initiative-wallbash.yml — コメント表示のフェンスドコードブロック化 + `@ai` 反映 + feedback prompt 追加

- **Assigned files (MODIFY)**:
  - `.github/workflows/initiative-wallbash.yml`
    - ステップ `Post initiative metadata`（L152-180）: コマンドリファレンステーブル内の `@ai-task` → `@ai`。コマンド表示をフェンスドコードブロックに変更
    - ステップ `Post wallbash summary to issue`（L182-215）: 次ステップ案内の `@ai-task` → `@ai`。コマンド表示をフェンスドコードブロックに変更
    - ステップ `Run Claude Code`（L75-111）: init モード時にも `/tmp/feedback.txt` に保存するステップを追加（または prompt に feedback 参照を追加）
  - `.claude/skills/gha-wallbash/SKILL.md`
    - init モードの作業フロー ステップ1: feedback ファイル（`/tmp/feedback.txt`）が存在する場合はそれも参照する旨を追記
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  1. コマンドリファレンステーブルのコマンドが `@ai` を使用していること
  2. コマンド表示がフェンスドコードブロック（バッククォート3連）で囲まれていること
  3. init モードでも feedback が Claude prompt に渡されること
  4. gha-wallbash/SKILL.md に feedback 参照の記述があること
- **Estimated complexity**: M
- **Risk**: HEREDOC 内でのフェンスドコードブロック（バッククォート3連）は YAML のブロックスカラー `|` と組み合わせると問題なく動作するが、`gh issue comment --body "..."` の文字列内にバッククォート3連を含める場合は shell エスケープとの衝突に注意。`cat > /tmp/comment.md` + `--body-file` パターンの採用を検討すること
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: initiative-execute.yml — コメント表示のフェンスドコードブロック化 + `@ai` 反映

- **Assigned files (MODIFY)**:
  - `.github/workflows/initiative-execute.yml`
    - ステップ `Post gate review summary to issue`（L200-234）: 次ステップ案内の `@ai-task` → `@ai`。コマンド表示をフェンスドコードブロックに変更
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  1. 次ステップ案内のコマンドが `@ai` を使用していること
  2. コマンド表示がフェンスドコードブロックで囲まれていること
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: backlog-to-issue.yml — cron 間隔変更 + `@ai` 反映 + フェンスドコードブロック化

- **Assigned files (MODIFY)**:
  - `.github/workflows/backlog-to-issue.yml`
    - `on.schedule.cron`: `*/30 * * * *` → `0 */3 * * *`（L5）
    - ステップ `Create issue`（create-issue ジョブ、L68-91）: Issue 本文内の `@ai-task /start` → `@ai /start`、フェンスドコードブロック化（L86）
    - ステップ `Create issue`（scheduled-create ジョブ、L150-171）: scheduled-create ジョブには使い方ガイドが含まれていないため変更不要であることを確認
- **Read-only dependencies**: なし
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  1. cron が `0 */3 * * *` に変更されていること
  2. create-issue ジョブの Issue 本文のコマンド案内が `@ai /start` を使用していること
  3. コマンド表示がフェンスドコードブロックで囲まれていること
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: README.md 全面最新化 + initiative-close.yml への feedback input 追加 + gha-close/SKILL.md feedback 記載

- **Assigned files (MODIFY)**:
  - `.github/workflows/README.md` — 全面書き換え:
    - `@ai-task` → `@ai`（全箇所）
    - コマンドリファレンスを最新化
    - フロー図を最新化（`@ai` 反映）
    - ワークフロー一覧の修正:
      - 削除: `backlog-auto-execute.yml`, `backlog-candidate-propose.yml`（存在しない）
      - 追加: `initiative-batch-approve.yml`, `initiative-question.yml`
      - `backlog-to-issue.yml` のトリガーを `schedule / 手動` に修正
    - メタデータコメントセクションの `@ai-task` → `@ai` 反映
  - `.github/workflows/initiative-close.yml` — feedback input 追加:
    - `on.workflow_dispatch.inputs` に `feedback` パラメータを追加（required: false, type: string, default: ''）
    - ステップ `Run Claude Code` の prompt に feedback を追加（`フィードバック: ${{ inputs.feedback }}`）
  - `.claude/skills/gha-close/SKILL.md`:
    - 作業フロー ステップ1 付近: feedback がある場合はクローズサマリーに反映する旨を追記
- **Read-only dependencies**:
  - `.github/workflows/initiative-dispatcher.yml`（T-001 変更後の最終状態を参照して README のフロー図・コマンドリファレンスの整合性を確認）
  - `.github/workflows/initiative-wallbash.yml`（T-002 変更後の最終状態を参照）
  - `.github/workflows/initiative-execute.yml`（T-003 変更後の最終状態を参照）
  - `.github/workflows/backlog-to-issue.yml`（T-004 変更後の最終状態を参照）
  - `.github/workflows/initiative-batch-approve.yml`（README 記載用に読み取り）
  - `.github/workflows/initiative-question.yml`（README 記載用に読み取り）
- **Prerequisite tasks**: T-001, T-002, T-003, T-004
- **Acceptance criteria**:
  1. README 内に `@ai-task` が残っていないこと
  2. ワークフロー一覧に存在しないファイル（`backlog-auto-execute.yml`, `backlog-candidate-propose.yml`）が含まれていないこと
  3. ワークフロー一覧に `initiative-batch-approve.yml`, `initiative-question.yml` が含まれていること
  4. `backlog-to-issue.yml` のトリガーが `schedule / 手動` と記載されていること
  5. initiative-close.yml に `feedback` input が追加されていること
  6. initiative-close.yml の Claude prompt に feedback が含まれていること
  7. gha-close/SKILL.md に feedback 参照の記述があること
- **Estimated complexity**: L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|
| `.github/workflows/initiative-dispatcher.yml` | MODIFY | - | - | - | READ |
| `.github/workflows/initiative-wallbash.yml` | - | MODIFY | - | - | READ |
| `.github/workflows/initiative-execute.yml` | - | - | MODIFY | - | READ |
| `.github/workflows/backlog-to-issue.yml` | - | - | - | MODIFY | READ |
| `.github/workflows/initiative-close.yml` | - | - | - | - | MODIFY |
| `.github/workflows/README.md` | - | - | - | - | MODIFY |
| `.claude/skills/gha-wallbash/SKILL.md` | - | MODIFY | - | - | - |
| `.claude/skills/gha-close/SKILL.md` | - | - | - | - | MODIFY |
| `.claude/skills/gha-execute/SKILL.md` | - | - | - | - | - |
| `.claude/skills/gha-question/SKILL.md` | - | - | - | - | - |
| `.github/workflows/initiative-batch-approve.yml` | - | - | - | - | READ |
| `.github/workflows/initiative-question.yml` | - | - | - | - | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。
競合がある場合は Prerequisite tasks で依存関係を設定し、別 Wave に分離する。

**競合検出結果**: 競合なし。全 MODIFY 対象ファイルは各タスクで排他的に割り当てられている。T-005 は T-001〜T-004 の変更結果を READ するため、依存関係により Wave 2 に配置する。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001: initiative-dispatcher.yml（`@ai-task` → `@ai` + feedback 伝播）
- T-002: initiative-wallbash.yml（コメント表示 + feedback prompt）
- T-003: initiative-execute.yml（コメント表示）
- T-004: backlog-to-issue.yml（cron + コメント表示）

### Wave 2 (Wave 1 完了後)
- T-005: README.md 全面更新 + initiative-close.yml feedback + gha-close/SKILL.md（depends on T-001, T-002, T-003, T-004）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | GHA 専門性はプロセス改善の一般知識の範囲内 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 5
- Total waves: 2
- Estimated max parallelism: 4 workers（Wave 1）
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）
- 注意事項: T-002 のフェンスドコードブロック実装時に HEREDOC 内の shell エスケープに注意（Risk として記載済み）
- スキルファイルの `@ai-task` 置換は不要（grep で確認済み、0件）。gha-wallbash/SKILL.md と gha-close/SKILL.md は feedback 参照追加のみ
- gha-execute/SKILL.md、gha-question/SKILL.md は変更不要

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-19
