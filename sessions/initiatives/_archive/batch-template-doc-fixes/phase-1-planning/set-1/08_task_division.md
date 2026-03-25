# File-Level Task Division: batch-template-doc-fixes

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 5（T-001〜T-005 は全て独立ファイルを対象とし並列可能）
- Dependency graph: T-006（バックログエントリ削除・CSV更新）は T-001〜T-005 全完了後に実施

## Task Assignments

### T-001: docs/workflow.md 拡充（BL-054 + BL-065 統合）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `docs/workflow.md`
  - BL-054: 「GHA Initiative スキル」セクション（L482付近）の内容確認。既に wallbash/execute/close の記述が存在するため、不足があれば補完する。なければ BL-054 は既に解決済みとしてスキップ
  - BL-065: 「ビルトイン Skills 評価リファレンス」セクション（L995付近）の後、または「マネージャーセッション共通ポリシー」セクション（L897付近）の前に「リファレンス系スキル一覧」セクションを新設。以下の非起動型スキルを一覧化:
    - ポリシー系: manager-common-policy, session-flow-policy, session-lifecycle-policy
    - チェックリスト系: rule-change-checklist, format-conversion-checklist, repo-sync-checklist
    - リファレンス系: builtin-skills-reference, plugin-reference, manager-overview
    - ユーティリティ系: external-repo-cleanup, gha-guideline
    - GHA専用: gha-wallbash, gha-execute, gha-close, gha-question, gha-test（※既にGHA Initiativeセクションで記載済みのためクロスリファレンスのみ）
- **Read-only dependencies**: `.claude/skills/gha-wallbash/SKILL.md`, `.claude/skills/gha-execute/SKILL.md`, `.claude/skills/gha-close/SKILL.md`, 各 `user-invocable: false` スキルの SKILL.md
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - docs/workflow.md に「リファレンス系スキル一覧」セクションが追加されている
  - 全 `user-invocable: false` スキルが一覧に含まれている（GHA専用スキルは既存セクションへのクロスリファレンス可）
  - BL-054 について、既存 GHA Initiative セクションの内容を確認し、不足があれば補完されている
  - 既存セクションとの整合性が保たれている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: バックログエントリ旧フォーマット統一（BL-077）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `backlog/entries/` 内の以下13ファイル（現存確認後、存在するもののみ変換）
  - `agentsの公式ディレクトリ分け.md`（BL-036）
  - `ai-driven-dev-patterns-builtin-skills-eval.md`（BL-037）
  - `entries-pattern-inbox適用検討.md`（BL-038）
  - `メタ認知セット分割粒度・スキャンモード.md`（BL-039）
  - `スキャンレポート変更理由記載ルール.md`（BL-040）
  - `rules-skills移動時の波及更新パターン.md`（BL-041）
  - `session-flow-checklist-precision.md`（BL-042）
  - `triage-standard-policy適用マトリクス列数リスク.md`（BL-043）
  - `user-invocable-false-description-pattern.md`（BL-044）
  - `チェックリスト型スキルの標準テンプレート化.md`（BL-045）
  - `条件付き固定タスク配置ルール整備.md`（BL-046）
  - BL-047 対応ファイル（backlog.csv に欠番のため現存確認要）
  - `triage-action-subagent-delegation.md`（BL-049）
- **Read-only dependencies**: `backlog/_template.md`（現行テンプレート）, `.claude/skills/format-conversion-checklist/SKILL.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 現存する全対象ファイルが現行テンプレート形式に変換されている
  - 各ファイルに `依存する環境前提` フィールドが記載されている（不明な場合は「なし」）
  - 各ファイルに `起票時チェックリスト` セクションが付与されている
  - 各ファイルに `関連エントリ` セクションが標準形式で存在する
  - format-conversion-checklist スキルに従い同等性検証が完了している（検証記録を作業ログに記載）
  - BL-047 が欠番の場合はその旨を作業ログに記録
- **Estimated complexity**: M（件数は多いが定型作業）
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: チェックリスト型スキルテンプレート作成（BL-045）
- **Assigned files (CREATE)**: `.claude/templates/checklist-skill-template.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**: `.claude/skills/rule-change-checklist/SKILL.md`, `.claude/skills/format-conversion-checklist/SKILL.md`, `.claude/skills/repo-sync-checklist/SKILL.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `.claude/templates/checklist-skill-template.md` が作成されている
  - 3つの既存チェックリスト型スキルの共通構成パターン（frontmatter + 位置づけ説明 + チェックリスト本体 + 使い方 + 関連ファイル一覧）が抽出・テンプレート化されている
  - テンプレートにプレースホルダー（`<!-- 記入指示 -->`）が含まれている
  - repo-sync-checklist の `user-invocable: true` パターンも考慮されている（frontmatter の user-invocable をプレースホルダーにする等）
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: Claude Code Action バージョン追跡手順作成（BL-060）
- **Assigned files (CREATE)**: `docs/claude-code-action-version-tracking.md`
- **Assigned files (MODIFY)**: `CLAUDE.md`（docs/ ファイル分類テーブル L110付近に行追加）
- **Read-only dependencies**: `.github/workflows/` 内の claude-code-action を使用するワークフロー群（バージョン指定の現状確認用）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `docs/claude-code-action-version-tracking.md` が作成されている（運用ガイドカテゴリ）
  - バージョン追跡の手順（確認方法・更新手順・影響範囲の確認観点）が記載されている
  - CLAUDE.md の docs/ ファイル分類テーブルに `docs/claude-code-action-version-tracking.md | 運用ガイド | Claude Code Action バージョン追跡手順` が追加されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: refs メタ情報テンプレート標準化（BL-083）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `refs/_knowledge_template.md`
- **Read-only dependencies**: `refs/agency-agents/knowledge.md`（実践済みパターンの参照）, `CLAUDE.md`（メタ情報要件の確認）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `refs/_knowledge_template.md` に「メタ情報」セクションが追加されている
  - 用途・有効期限・取得日・取得方法の4フィールドがテンプレートに含まれている
  - CLAUDE.md 規定「参照物格納時は用途・有効期限のメタ情報を必ず記載すること」との整合が確保されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-006: バックログエントリ削除・CSV ステータス更新
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `backlog/backlog.csv`（対象6件のステータスを「完了」に更新し、施策ディレクトリ名に `batch-template-doc-fixes` を記入）
- **Assigned files (DELETE)**: 以下6件のバックログエントリを `git rm` で削除
  - `backlog/entries/docs-workflow-initiative-gha-update.md`（BL-054）
  - `backlog/entries/workflow-md-reference-skills-section.md`（BL-065）
  - `backlog/entries/backlog-entries-format-unification.md`（BL-077）
  - `backlog/entries/チェックリスト型スキルの標準テンプレート化.md`（BL-045）
  - `backlog/entries/claude-code-action-version-tracking.md`（BL-060）
  - `backlog/entries/refs-meta-info-template.md`（BL-083）
- **Read-only dependencies**: T-001〜T-005 の完了状態
- **Prerequisite tasks**: T-001, T-002, T-003, T-004, T-005
- **Acceptance criteria**:
  - 6件のバックログエントリファイルが `git rm` で削除されている
  - `backlog/backlog.csv` の該当6行のステータスが「完了」に更新されている
  - `backlog/backlog.csv` の該当6行の施策ディレクトリ名が `batch-template-doc-fixes` に更新されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 | T-006 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `docs/workflow.md` | MODIFY | - | - | - | - | - |
| `backlog/entries/agentsの公式ディレクトリ分け.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/ai-driven-dev-patterns-builtin-skills-eval.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/entries-pattern-inbox適用検討.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/メタ認知セット分割粒度・スキャンモード.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/スキャンレポート変更理由記載ルール.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/rules-skills移動時の波及更新パターン.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/session-flow-checklist-precision.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/triage-standard-policy適用マトリクス列数リスク.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/user-invocable-false-description-pattern.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/チェックリスト型スキルの標準テンプレート化.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/条件付き固定タスク配置ルール整備.md` | - | MODIFY | - | - | - | - |
| `backlog/entries/triage-action-subagent-delegation.md` | - | MODIFY | - | - | - | - |
| `.claude/templates/checklist-skill-template.md` | - | - | CREATE | - | - | - |
| `docs/claude-code-action-version-tracking.md` | - | - | - | CREATE | - | - |
| `CLAUDE.md` | - | - | - | MODIFY | - | - |
| `refs/_knowledge_template.md` | - | - | - | - | MODIFY | - |
| `backlog/backlog.csv` | - | - | - | - | - | MODIFY |
| `backlog/entries/docs-workflow-initiative-gha-update.md` | - | - | - | - | - | DELETE |
| `backlog/entries/workflow-md-reference-skills-section.md` | - | - | - | - | - | DELETE |
| `backlog/entries/backlog-entries-format-unification.md` | - | - | - | - | - | DELETE |
| `backlog/entries/チェックリスト型スキルの標準テンプレート化.md` | - | MODIFY | - | - | - | DELETE |
| `backlog/entries/claude-code-action-version-tracking.md` | - | - | - | - | - | DELETE |
| `backlog/entries/refs-meta-info-template.md` | - | - | - | - | - | DELETE |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, DELETE = 削除, `-` = 無関係

**競合検出**:
- `backlog/entries/チェックリスト型スキルの標準テンプレート化.md`: T-002（MODIFY）と T-006（DELETE）が競合 → T-006 は T-002 完了後に実施するため Wave 分離で解決済み
- その他のファイルに競合なし

## Wave Assignment

### Wave 1 (並列実行可)
- T-001（docs/workflow.md 拡充）
- T-002（バックログエントリ旧フォーマット統一）
- T-003（チェックリスト型スキルテンプレート作成）
- T-004（Claude Code Action バージョン追跡手順作成）
- T-005（refs メタ情報テンプレート標準化）

### Wave 2 (Wave 1 完了後)
- T-006（バックログエントリ削除・CSV ステータス更新）— depends on T-001〜T-005

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 全タスクがドキュメント・テンプレート整備であり、特定ドメイン知識は不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 6
- Total waves: 2
- Estimated max parallelism: 5 workers（Wave 1）
- Conflict count: 1（T-002/T-006 の `チェックリスト型スキルの標準テンプレート化.md` — Wave 分離で解決）

### 特記事項

1. **BL-054 の既存状態**: docs/workflow.md の「GHA Initiative スキル」セクション（L482-549）に wallbash/execute/close の記述が既に存在する。T-001 ワーカーは現状を確認し、不足部分のみ補完すること。完全に充足している場合は BL-054 相当を「既に解決済み」として作業ログに記録する
2. **BL-047 欠番**: backlog.csv に BL-047 が存在しない。T-002 ワーカーは BL-036〜BL-046 + BL-049 の12件を変換対象とし、BL-047 が欠番である旨を作業ログに記録する
3. **BL-077 対象エントリの現状**: 13件とも既にメタ情報テーブル形式（`## メタ情報` + テーブル）に部分変換済み。不足は `依存する環境前提` フィールド・`起票時チェックリスト` セクション等の補完が主な作業
4. **T-002 での format-conversion-checklist 適用**: フォーマット変換タスクのため、`.claude/skills/format-conversion-checklist/SKILL.md` を参照して同等性検証を実施し、検証記録を作業ログに記載すること

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-25
