# File-Level Task Division: backlog-inventory-batch

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 1
- Dependency graph: T-001 → T-002 → T-003（逐次依存）

逐次1ワーカー構成とする。理由:
- T-001（削除）は T-002（分類）の前提（削除済みファイルを分類対象から除外するため）
- T-003（グルーピング）は T-002 の分類結果に依存
- 全体の作業量が1ワーカーで十分処理可能（推定2-3時間相当）

## Task Assignments

### T-001: 完了済みエントリ41件の git rm 削除

- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: なし
- **Assigned files (DELETE)**: `backlog/entries/` 配下の41件（下記リスト）
  - `00_proposal-GHA制約事前チェック.md`
  - `GHA-claude-dir書き込み制約文書化.md`
  - `GHA-verdictステップ分離パターン.md`
  - `GHAメタデータ抽出共通化.md`
  - `SC-006-impl系追加.md`
  - `SCチェック後アクション接続明確化.md`
  - `aidd-cross-session-knowledge-aggregation.md`
  - `aidd-tool-policy-centralization.md`
  - `automation-candidates-sync-guideline.md`
  - `automation-managerセッション作成.md`
  - `automation統合スコア算出定義.md`
  - `backlog-IDとissueテンプレート.md`
  - `backlog-entry-minimum-description.md`
  - `backlog-id-collision-prevention.md`
  - `backlogテンプレート凡例強化.md`
  - `bm-001-threshold-tiering.md`
  - `bm-report-to-backlog-trigger.md`
  - `claude-templates-update-checklist.md`
  - `dev-workflow-detail L1参照精査.md`
  - `evaluator-symmetry-table-unification.md`
  - `gha-multirepository-access-via-clone.md`
  - `gha-workflow-old-filename-update.md`
  - `refs-read-step-placement-pattern.md`
  - `sc-feedback-loop-definition.md`
  - `sc-inline-reference-scan-expansion.md`
  - `session-artifacts-structure-refactor.md`
  - `session-definition-meta-template.md`
  - `skill-file-table-completeness-check.md`
  - `skill-plugin-overlap-check-rule.md`
  - `subagent-commit-reliability.md`
  - `template-composition-spec.md`
  - `template-refactor-cross-reference-check.md`
  - `テンプレートmdパス参照チェック.md`
  - `テンプレート新設5ステップパターン.md`
  - `ディスパッチログ・コスト記録の自動収集ツール.md`
  - `トリアージフェーズゲートとGHA同期.md`
  - `ハーネスエンジニアリング観点でのブラッシュアップ.md`
  - `メタルール・チェックリスト統合.md`
  - `成功基準grepスコープ制限.md`
  - `知見集約テーブル発見元列のinitiatives逆移植.md`
  - `非initiative-コスト追跡.md`
- **Read-only dependencies**: `/tmp/real_completed.txt`（削除対象リスト）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 41件すべてが `git rm` で削除されている
  - `backlog/entries/` に残存78件のみが存在する
  - git status で41件の削除が staged されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: 残存78件の粒度分類（S/M/L）

- **Assigned files (CREATE)**: なし（分類結果は T-003 の成果物に統合）
- **Assigned files (MODIFY)**: `phase-2-execution/set-1/02_worker_log.md`（分類作業の中間記録）
- **Read-only dependencies**: `backlog/entries/` 配下の残存78件（全件読み取り）、`02_plan.md`（粒度基準テーブル）
- **Prerequisite tasks**: T-001（削除後のクリーンな状態で作業する）
- **Acceptance criteria**:
  - 78件すべてに粒度ラベル（S/M/L）が付与されている
  - 分類基準: S=1-2ファイル変更・設計判断不要、M=3-5ファイル変更・軽い設計判断、L=6+ファイル変更・アーキテクチャ設計
  - 迷った場合は M に分類（02_plan.md の方針に準拠）
- **Estimated complexity**: M（78件の内容読み取りが主作業）
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: 軽微エントリのテーマ別グルーピングとバッチ施策名付与

- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `phase-2-execution/set-1/03_worker_report.md`（分類結果一覧表・テーマ別グルーピング・バッチ施策名候補を記載）
- **Read-only dependencies**: T-002 の分類結果（worker_log 内の中間記録）、`backlog/entries/` 配下の S 分類エントリ
- **Prerequisite tasks**: T-002
- **Acceptance criteria**:
  - S 分類エントリが以下のテーマ軸でグルーピングされている:
    - GHA関連（ワークフロー、スキル）
    - テンプレート・ドキュメント
    - ルール・ポリシー
    - 参照修正・リネーム追従
    - ai-driven-dev-patterns 関連
    - その他
  - 各テーマグループにバッチ施策名候補（例: `batch-gha-minor-fixes`）が付与されている
  - M/L 分類エントリは「個別施策として残す」旨が明記されている
  - 全78件の粒度分類一覧表が `03_worker_report.md` に記載されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 |
|------|:-----:|:-----:|:-----:|
| `backlog/entries/*`（完了済み41件） | DELETE | - | - |
| `backlog/entries/*`（残存78件） | - | READ | READ |
| `phase-2-execution/set-1/02_worker_log.md` | - | MODIFY | READ |
| `phase-2-execution/set-1/03_worker_report.md` | - | - | MODIFY |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, DELETE = 削除, `-` = 無関係

**競合検出結果**: 競合なし。全タスクが異なるファイルを操作し、逐次依存で分離されている。

## Wave Assignment

### Wave 1
- T-001: 完了済みエントリ41件の git rm 削除

### Wave 2 (Wave 1 完了後)
- T-002: 残存78件の粒度分類（T-001 に依存）

### Wave 3 (Wave 2 完了後)
- T-003: テーマ別グルーピング・バッチ施策名付与（T-002 に依存）

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 定型的なバックログ整理作業であり、ドメイン固有の知識は不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 3
- Total waves: 3（逐次実行）
- Estimated max parallelism: 1 worker
- Conflict count: 0
- 備考: T-001 は機械的な `git rm` 操作（S）、T-002 は78件の内容読み取りと判断（M、主作業）、T-003 は分類結果の整理と命名（M）。全体として1ワーカーの逐次実行が効率的。

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-24
