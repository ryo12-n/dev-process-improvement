# File-Level Task Division: 費用対効果評価フレームワークの標準化

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `02_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 1（逐次ディスパッチで十分）
- Dependency graph: T-001 → T-002 → T-003 → T-004（線形依存）
  - T-001: 基底テンプレート作成（独立）
  - T-002: 既存テンプレートへの追跡コメント追加（T-001 の成果物パスに依存）
  - T-003: CLAUDE.md の更新（T-001 のディレクトリ確定に依存）
  - T-004: メタルール横断検証（T-003 の CLAUDE.md 変更内容に依存）

## Task Assignments

### T-001: 基底テンプレート `.claude/templates/cost-effectiveness-evaluation.md` の新規作成
- **Assigned files (CREATE)**: `.claude/templates/cost-effectiveness-evaluation.md`
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**:
  - `sessions/initiatives/_archive/ai-automation-tool-review/04_work_report.md`（L97-121: 4軸定義・算出式・評価テーブルのソース）
  - `automation-candidates/_template.md`（L31-38: 既存の費用対効果分析セクション。基底テンプレートとの一貫性確認用）
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - ファイルが `.claude/templates/cost-effectiveness-evaluation.md` に存在する
  - 4軸定義（頻度・手動コスト・実装難易度）の各レベル説明を含む
  - 算出式（優先度スコア = 頻度 x 手動コスト / 実装難易度）を含む
  - 汎用評価テーブルテンプレートを含む（自動化候補固有カラムは汎用化）
  - カスタマイズ指針セクション（ドメイン固有の軸追加方法等）を含む
  - SC-1 を充足する
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: `automation-candidates/_template.md` に追跡コメントを追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `automation-candidates/_template.md`（L31「## 費用対効果分析」の直上に追跡コメント1行追加）
- **Read-only dependencies**:
  - `.claude/templates/cost-effectiveness-evaluation.md`（T-001 の成果物。追跡コメントのパス参照用）
- **Prerequisite tasks**: T-001
- **Acceptance criteria**:
  - `## 費用対効果分析` セクションの直上に追跡コメントが追加されている
  - `grep -r "基底テンプレート .claude/templates/cost-effectiveness-evaluation.md" automation-candidates/` が結果を返す
  - SC-2 を充足する
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: CLAUDE.md のディレクトリ構成テーブル・文書分類ポリシーテーブルに `.claude/templates/` を追加
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: `CLAUDE.md`
  - L64（`| `templates/` | 施策テンプレート |` の後）: ディレクトリ構成テーブルに `.claude/templates/` の行を追加
  - L165（`| 人間用 | 人間 | ...` の後）: 文書分類ポリシーテーブルに `.claude/templates/` の行を追加
- **Read-only dependencies**: なし
- **Prerequisite tasks**: T-001（`.claude/templates/` のディレクトリ用途が確定している必要がある）
- **Acceptance criteria**:
  - ディレクトリ構成テーブルに `.claude/templates/` の行が存在し、用途が記載されている
  - 文書分類ポリシーテーブルに `.claude/templates/` の行が存在し、読者・配置先・用途例が記載されている
  - SC-3 を充足する
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-004: メタルール横断検証（CLAUDE.md 変更の影響確認）
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**: なし（検証のみ。問題発見時は T-003 の修正として対応）
- **Read-only dependencies**:
  - `CLAUDE.md`（T-003 で変更された内容）
  - `.claude/rules/`（既存ルールとの整合性確認）
  - `.claude/skills/`（既存スキルとの整合性確認）
  - `docs/workflow.md`（可視化文書の更新要否確認）
- **Prerequisite tasks**: T-003
- **Acceptance criteria**:
  - CLAUDE.md に追加された `.claude/templates/` の記載が、既存のディレクトリ構成・文書分類ポリシーと矛盾しないことを確認
  - `docs/workflow.md`（可視化文書）の更新要否を判断し、必要に応じて更新を実施
  - 既存の `.claude/rules/` や `.claude/skills/` で `.claude/templates/` に言及すべき箇所がないことを確認
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 | T-004 |
|------|:-----:|:-----:|:-----:|:-----:|
| `.claude/templates/cost-effectiveness-evaluation.md` | CREATE | READ | - | - |
| `automation-candidates/_template.md` | READ | MODIFY | - | - |
| `CLAUDE.md` | - | - | MODIFY | READ |
| `sessions/initiatives/_archive/ai-automation-tool-review/04_work_report.md` | READ | - | - | - |
| `.claude/rules/*` | - | - | - | READ |
| `.claude/skills/*` | - | - | - | READ |
| `docs/workflow.md` | - | - | - | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: 同一ファイルに対して複数タスクが CREATE または MODIFY を持つケースなし。ファイル書き込み競合は存在しない。

ただし、論理的依存関係（T-002 は T-001 の成果物パスを参照、T-003 は T-001 のディレクトリ用途に依存、T-004 は T-003 の変更内容を検証）があるため、逐次実行とする。

## Wave Assignment

### Wave 1（逐次実行）
- T-001 → T-002 → T-003 → T-004

小規模施策（4タスク、すべて S〜M 複雑度）のため、単一ワーカーによる逐次ディスパッチが最適。並列化のオーバーヘッド（per-worker ファイル作成・統合）が作業量を上回る。

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | プロセス改善の定型作業のため汎用ワーカーで十分 | Worker |
| なし | - | プロセス改善の定型作業のため汎用評価者で十分 | Evaluator |

## Summary

- Total tasks: 4
- Total waves: 1（逐次実行）
- Estimated max parallelism: 1 worker
- Conflict count: 0（同一ファイルへの複数 MODIFY/CREATE なし）
- 推奨ディスパッチ方式: 逐次（1ワーカーが T-001〜T-004 を順に実行）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-17
