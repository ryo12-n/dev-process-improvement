# File-Level Task Division: gha-pipeline-autorun

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 4
- Dependency graph: T-001 は T-005 の GATE_VERDICT 出力定義に論理的に依存するが、ファイル書き込み競合はないため同一 Wave で並列実行可能。ただし T-001 実装者は T-005 で定義する `GATE_VERDICT: <判定>` 形式を前提として verdict 抽出ロジックを構築する必要がある（提案書の設計パターンで合意済み）。

## Task Assignments

### T-001: initiative-execute.yml に自動連鎖ディスパッチを追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.github/workflows/initiative-execute.yml`（260行）
  - L4-15: `retry_count` 入力パラメータを `inputs:` ブロックに追加（type: number, required: false, default: 0）
  - L159-179 付近（`Extract gate review summary` ステップ後）: verdict 抽出ステップを新規追加。`claude-execution-output.json` から `GATE_VERDICT: <判定>` マーカーを grep で抽出し `GITHUB_OUTPUT` に `verdict` を出力
  - L252-259 付近（`Update labels to gate-review` ステップ後）: 自動連鎖ディスパッチステップを新規追加。verdict に基づき以下を分岐:
    - `通過` → `initiative-close.yml` をディスパッチ
    - `差し戻し` → retry_count < 2 なら `initiative-execute.yml` を retry_count+1 でセルフディスパッチ、retry_count >= 2 なら Issue にコメントして停止
    - verdict 未検出 → 従来動作（`gate-review` ラベルで停止、人間待ち）
- **Read-only dependencies**:
  - `.github/workflows/initiative-close.yml`（ディスパッチ先のインターフェース確認: inputs の形式）
  - `.claude/rules/gha-workflow-security.md`（セキュリティチェックリスト）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `retry_count` 入力が追加されている（type: number, required: false, default: 0）
  - verdict 抽出ステップが `claude-execution-output.json` から `GATE_VERDICT:` マーカーを抽出し `verdict` 出力に設定する
  - verdict=`通過` 時に `initiative-close.yml` がディスパッチされる（issue_number, initiative_dir, branch を渡す）
  - verdict=`差し戻し` 時に retry_count < 2 なら `initiative-execute.yml` をセルフディスパッチ（retry_count+1, command=reject, phase=gate-review を渡す）
  - retry_count >= 2 の場合、Issue にコメントして `gate-review` ラベルで停止する
  - verdict 未検出時は従来動作（`gate-review` ラベルで停止）を維持する
  - `${{ }}` を `run:` ブロックで直接展開していない（`env:` 経由）
  - `permissions` が既存の最小権限を維持している（actions: write の追加が必要 — `gh workflow run` でのディスパッチに必要）
- **Estimated complexity**: L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: initiative-dispatcher.yml の approve (wallbashing) ルートに retry_count=0 を追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.github/workflows/initiative-dispatcher.yml`（258行）
  - L175-181 付近（approve + wallbashing ルートの `gh workflow run initiative-execute.yml` 呼び出し部分）: `-f retry_count="0"` を追加
- **Read-only dependencies**:
  - `.claude/rules/gha-workflow-security.md`（セキュリティチェックリスト）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - approve (wallbashing) ルートの `gh workflow run initiative-execute.yml` に `-f retry_count="0"` が追加されている
  - 既存のパラメータ（issue_number, command, feedback, phase, initiative_dir, branch）が変更されていない
  - `${{ }}` を `run:` ブロックで直接展開していない（既存準拠）
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: backlog-to-issue.yml の cron 間隔を30分に変更
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.github/workflows/backlog-to-issue.yml`（195行）
  - L5: `cron: '0 */3 * * *'` → `cron: '*/30 * * * *'` に変更
- **Read-only dependencies**:
  - `.claude/rules/gha-workflow-security.md`（セキュリティチェックリスト）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - cron 式が `*/30 * * * *` に変更されている
  - `scheduled-create` ジョブの `if: github.event_name == 'schedule'` が維持されている（トリガー共存ルール準拠）
  - 他の既存ロジック（候補選定、重複チェック、Issue 作成、wallbash ディスパッチ、ステータス更新）に変更がない
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: initiative-batch-approve.yml を新規作成
- **Assigned files (CREATE)**: `.github/workflows/initiative-batch-approve.yml`
- **Assigned files (MODIFY)**: -
- **Read-only dependencies**:
  - `.github/workflows/initiative-dispatcher.yml`（dispatch パターン・メタデータ取得の参考）
  - `.github/workflows/initiative-execute.yml`（ディスパッチ先のインターフェース確認）
  - `.claude/rules/gha-workflow-security.md`（セキュリティチェックリスト）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `workflow_dispatch` トリガーのみ（schedule トリガーなし — 提案書の設計方針に従い手動限定）
  - `initiative:wallbashing` ラベルが付いた open Issue を一覧取得する
  - 各 Issue のメタデータコメント（`initiative-metadata`）から initiative_dir, branch を抽出する
  - 各 Issue に対して `initiative-execute.yml` をディスパッチする（issue_number, command=approve, phase=wallbashing, initiative_dir, branch, retry_count=0）
  - ディスパッチ結果のサマリーを Actions ログに出力する（何件処理したか、スキップしたか）
  - メタデータが見つからない Issue はスキップし、warning を出力する
  - `${{ }}` を `run:` ブロックで直接展開していない（`env:` 経由）
  - `permissions` は最小権限（contents: read, issues: read, actions: write）
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: gha-execute/SKILL.md に GATE_VERDICT 出力形式の制約を追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/gha-execute/SKILL.md`（69行）
  - L31 付近（`/approve` フローのステップ 9「ゲート判定サマリーを標準出力に出力する」の後）: GATE_VERDICT 出力形式の制約を追加。ゲート判定完了時に `GATE_VERDICT: 通過` または `GATE_VERDICT: 差し戻し` をサマリー出力の末尾に含めることを必須とする
  - L42 付近（`/reject` フローのステップ 6「ゲート判定サマリーを標準出力に出力する」の後）: 同様の GATE_VERDICT 出力制約を追加
  - L44-49 付近（「やること」セクション）: GATE_VERDICT マーカーの出力を追加
  - L59-63 付近（「制約」セクション）: GATE_VERDICT 形式の制約を追加
- **Read-only dependencies**:
  - `sessions/initiatives/gha-pipeline-autorun/00_proposal.md`（GATE_VERDICT 設計パターンの参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `/approve` フローと `/reject` フローの両方で、ゲート判定サマリーに `GATE_VERDICT: 通過` または `GATE_VERDICT: 差し戻し` を含める指示が記載されている
  - マーカー文字列の形式が `GATE_VERDICT: <判定>` で固定されている（grep での抽出を前提）
  - マーカーはサマリー出力の末尾に独立行として出力する指示になっている
  - 既存のフロー・制約との整合性が保たれている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|
| `.github/workflows/initiative-execute.yml` | MODIFY | - | - | - | - |
| `.github/workflows/initiative-dispatcher.yml` | - | MODIFY | - | - | - |
| `.github/workflows/backlog-to-issue.yml` | - | - | MODIFY | - | - |
| `.github/workflows/initiative-batch-approve.yml` | - | - | - | CREATE | - |
| `.claude/skills/gha-execute/SKILL.md` | - | - | - | - | MODIFY |
| `.github/workflows/initiative-close.yml` | READ | - | - | - | - |
| `.claude/rules/gha-workflow-security.md` | READ | READ | READ | READ | - |
| `sessions/initiatives/gha-pipeline-autorun/00_proposal.md` | - | - | - | - | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: 競合なし。全タスクの MODIFY/CREATE 対象ファイルは完全に独立している。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001（initiative-execute.yml MODIFY）
- T-002（initiative-dispatcher.yml MODIFY）
- T-003（backlog-to-issue.yml MODIFY）
- T-004（initiative-batch-approve.yml CREATE）
- T-005（gha-execute/SKILL.md MODIFY）

**補足**: 全タスクが Wave 1 で並列実行可能。T-001 と T-005 は論理的依存（GATE_VERDICT 形式の定義→抽出）があるが、形式は提案書で `GATE_VERDICT: <判定>` と合意済みのため、ファイル書き込み競合なし・論理的にも独立して実装可能。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | GHA ワークフロー YAML とスキル定義の変更であり、汎用ワーカーで対応可能 | Worker |
| なし | - | GHA セキュリティチェックリストに基づく評価は汎用評価者で対応可能 | Evaluator |

## Summary

- Total tasks: 5
- Total waves: 1
- Estimated max parallelism: 5 workers（ただし T-002, T-003, T-005 は S 規模のため、4 workers に集約しても可）
- Conflict count: 0（全タスクの MODIFY/CREATE 対象ファイルが完全に独立）

### 注意事項
- **GHA セキュリティチェックリスト**: 全タスク（特に T-001, T-004）で `.claude/rules/gha-workflow-security.md` の全項目を確認すること
- **T-001 の permissions 変更**: `initiative-execute.yml` に `actions: write` 権限の追加が必要（`gh workflow run` でのディスパッチに必要）。現在の permissions ブロック（L35-39）に追加する
- **T-001 と T-005 の論理的整合性**: 両タスクの実装者は `GATE_VERDICT: 通過` / `GATE_VERDICT: 差し戻し` の形式を共有すること。T-001 は grep パターン `GATE_VERDICT:` で抽出し、T-005 はこの形式を SKILL.md に明記する

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-19
