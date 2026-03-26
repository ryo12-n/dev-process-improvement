# File-Level Task Division: batch-skill-session-tweaks

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 7（全タスクがファイル書き込み先で独立）
- Dependency graph: なし（全タスク独立）

## Task Assignments

### T-001: BL-017 l2-worker に別リポジトリ成果物の記法スタイル事前確認チェック追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/agents/l2-worker.md`（「壁打ちフェーズ」セクションの「前提条件チェック」リスト内。既存の「外部リポジトリ成果物の記法スタイル確認」チェック項目（line 46 付近）の説明を拡充し、具体的な確認手順ガイダンスを追加する）
- **Read-only dependencies**: `backlog/entries/別リポジトリ成果物の記法スタイル事前確認.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 壁打ちフェーズの前提条件チェックに記法スタイル事前確認の具体的なガイダンスが追記されている
  - 既存のチェック項目（line 46）との重複がなく、補完的な内容になっている
  - 確認手順として「既存ファイルの記法スタイル（見出し形式・絵文字使用・リスト記法等）を事前確認する」旨が含まれている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: BL-027 metacognition-manager に知見集約・課題集約セクション追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/metacognition-manager/SKILL.md`（「結果の集約」サブセクション（line 117-124 付近）の後に独立した「知見集約手順」「課題集約手順」セクションを追加する。triage-manager SKILL.md の同名セクション（line 158-177）を構造テンプレートとして参照し、metacognition 固有の入力ソースに置き換える）
- **Read-only dependencies**: `.claude/skills/triage-manager/SKILL.md`（知見集約手順・課題集約手順の構造参照）、`.claude/skills/manager-common-policy/SKILL.md`（§5, §6 の共通手順参照）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 「知見集約手順」セクションが独立して存在する（triage-manager と同構造）
  - 「課題集約手順」セクションが独立して存在する（triage-manager と同構造）
  - `manager-common-policy` §5, §6 への参照が正しく記載されている
  - metacognition 固有の入力ソース（`phase-1-analysis/set-N/06_eval_report.md`、`04_scan_report.md`）が正しく記載されている
  - 既存の「結果の集約」セクション内の記述と矛盾しない
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: BL-040 metacognition-worker にスキャンレポート走査対象変更理由記載ガイダンス追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/metacognition-manager/agents/metacognition-worker.md`（「スキャンレポートの構成（04_scan_report.md）」セクション（line 133-166 付近）に、タスク指示からの走査対象変更時の理由記載ガイダンスを追記する）
- **Read-only dependencies**: `backlog/entries/スキャンレポート変更理由記載ルール.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - スキャンレポート構成ガイドに「タスク指示（01_tasks.md）からの変更点がある場合は、走査概要セクションに変更理由を明記する」旨のガイダンスが追記されている
  - ガイダンスの位置がスキャンレポート構成セクション内で自然な場所にある
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: BL-042 session-flow-policy §5.1 チェックリストに不足箇所を追記
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/session-flow-policy/SKILL.md`（§5.1「新セッションタイプ追加時のチェックリスト」（line 305-316 付近）に不足している連動更新箇所を追記する）
- **Read-only dependencies**: `.claude/skills/session-lifecycle-policy/SKILL.md`（§1.3, §2.1 のテーブル構造確認）、`backlog/entries/session-flow-checklist-precision.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 以下の連動更新箇所がチェックリストに追記されている:
    - `session-lifecycle-policy` §2.1 ペアリング構造テーブルへの追加
    - 変更対象ファイルの「関連ファイル一覧」セクションの更新
  - 既存のチェック項目と重複していない（§1.3 記録先対応テーブルは既に line 313 でカバー済み）
  - チェックリスト形式（`- [ ]` 記法）が統一されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-005: BL-043 session-lifecycle-policy テーブル幅肥大化の調査・分析
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: -（成果物は `phase-2-execution/set-N/03_worker_report.md` 内の調査レポートセクション）
- **Read-only dependencies**: `.claude/skills/session-lifecycle-policy/SKILL.md`（§1.2 適用マトリクス全体）、`backlog/entries/triage-standard-policy適用マトリクス列数リスク.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - 以下の調査結果が worker_report に記載されている:
    - 現在のテーブル構成（行数×列数）の把握
    - 可読性低下の具体的な原因分析
    - 今後のセッションタイプ追加時のスケーラビリティ評価
    - 再設計案の選択肢列挙（転置、分割、YAML化等）と各案のメリット・デメリット
  - 具体的な再設計案が backlog エントリとして切り出し可能な形式で記述されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-006: BL-052 backlog-maintenance-worker に CSV 機械集計手順と優先度クロスチェック追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md`（2箇所: (1) BM-004 走査手順（line 86-89 付近）に CSV 機械集計手順と CSV/エントリ間の優先度照合ステップを追記。(2) スキャンレポート構成の BM-004 セクション（line 160-164 付近）に優先度不一致検出結果テーブルを追加）
- **Read-only dependencies**: `backlog/entries/backlog-maintenance-worker走査手順改善.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - BM-004 走査手順に「CSV から機械的に集計した値を使用する」ルールが追記されている
  - BM-004 走査手順に「backlog.csv の優先度列とエントリファイル内の優先度を照合する」ステップが追記されている
  - スキャンレポート構成の BM-004 セクションに優先度不一致検出結果テーブル（または照合結果列）が追加されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-007: BL-062 l1-manager にテンプレート事前適用検討ガイダンス追加
- **Assigned files (CREATE)**: -
- **Assigned files (MODIFY)**: `.claude/skills/l1-manager/SKILL.md`（Phase A の `03_tasks.md` 作成関連セクション（line 124 付近、または「タスクリストに含める固定タスク」セクション（line 228）の前）に、タスク設計時にテンプレートの事前適用を検討するガイダンスを追記する）
- **Read-only dependencies**: `backlog/entries/l1-pre-applied-template-task-design.md`
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `03_tasks.md` 作成のガイダンスとして、ワーカーの作業効率向上のためテンプレートの事前適用（テンプレートコピーを L1 が事前に実施し、ワーカーにはコピー済みファイルの編集を指示する等）を検討する旨のガイダンスが追記されている
  - ガイダンスは「検討する」であり、強制ではないこと
  - 適用例（テンプレートコピーの事前実施等）が示されている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 | T-005 | T-006 | T-007 |
|------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| `.claude/skills/l1-manager/agents/l2-worker.md` | MODIFY | - | - | - | - | - | - |
| `.claude/skills/metacognition-manager/SKILL.md` | - | MODIFY | - | - | - | - | - |
| `.claude/skills/metacognition-manager/agents/metacognition-worker.md` | - | - | MODIFY | - | - | - | - |
| `.claude/skills/session-flow-policy/SKILL.md` | - | - | - | MODIFY | - | - | - |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | - | - | - | - | READ | - | - |
| `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md` | - | - | - | - | - | MODIFY | - |
| `.claude/skills/l1-manager/SKILL.md` | - | - | - | - | - | - | MODIFY |
| `.claude/skills/triage-manager/SKILL.md` | - | READ | - | - | - | - | - |
| `.claude/skills/manager-common-policy/SKILL.md` | - | READ | - | - | - | - | - |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出ルール**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つ場合は競合。
競合がある場合は Prerequisite tasks で依存関係を設定し、別 Wave に分離する。

**競合検出結果**: 競合なし。全7タスクの MODIFY 対象ファイルが完全に分離されている。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001, T-002, T-003, T-004, T-005, T-006, T-007

全タスクが Wave 1 で並列実行可能。Wave 2 以降は不要。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業（追記のみ）であり、専門エージェント不要 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 7
- Total waves: 1
- Estimated max parallelism: 7 workers
- Conflict count: 0（全タスクのファイル書き込み先が独立）

### 補足
- T-005（BL-043）は調査タスクであり、成果物はファイル変更ではなく worker_report 内のレポートとなる。他タスクとの競合はない
- 全タスクが S/M 複雑度の追記作業であり、1ワーカーでの逐次実行が現実的。L1 判断で1ワーカー逐次を推奨

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-26
