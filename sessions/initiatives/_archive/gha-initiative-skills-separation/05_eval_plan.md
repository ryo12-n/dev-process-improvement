# 評価計画: GHA 用 initiative skills の分離

## 壁打ちフェーズ [2026-03-15]

### 理解のサマリー
- 評価の目的: GHA initiative ワークフロー4つに対応する専用スキルファイルの作成、YAML プロンプトリファクタ、execution_file 修正横展開、ドキュメント更新が成功基準を満たしているか評価する
- 評価スコープ: 4スキルファイル（gha-wallbash/execute/close/question）、4ワークフロー YAML、gha-guideline 権限マトリクス、docs/workflow.md、inbox 削除
- 完了条件: 05_eval_plan.md と 06_eval_report.md が作成され、成功基準に対する達成度評価と次フェーズへの推奨が記載されていること

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能
- [x] 評価に必要なツール・アクセス権限: 確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.claude/skills/gha-wallbash/SKILL.md`, `gha-execute/SKILL.md`, `gha-close/SKILL.md`, `gha-question/SKILL.md`（4スキルファイル）
- `.github/workflows/initiative-wallbash.yml`, `initiative-execute.yml`, `initiative-close.yml`, `initiative-question.yml`（4ワークフロー YAML）
- `.claude/skills/gha-guideline/SKILL.md`（権限マトリクス更新）
- `docs/workflow.md`（GHA スキルセクション追加）
- `inbox/gha-execution-file-fix-rollout.md`（削除確認）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | スキルファイル存在・構造 | 4ファイルの存在確認 + SKILL.md 標準構造（frontmatter + あなたの役割 / 作業フロー / やること / やらないこと）への準拠確認 | 4ファイルすべてが存在し、標準構造に準拠 |
| 2 | YAML プロンプトリファクタ | 4ワークフロー YAML の `prompt:` がスキルファイル参照 + 動的コンテキスト + リマインダーのみで構成されているか確認 | 4ファイルすべてがリファクタ済み |
| 3 | execution_file jq 抽出パターン | execute/close/question の3ワークフローで wallbash と同一の jq パターンが適用されているか確認 | 3ファイルすべてで統一パターン適用 |
| 4 | gha-guideline 権限マトリクス更新 | セクション5のワークフロー一覧・権限マトリクス・設計判断に4ワークフローが記載されているか確認 | 4ワークフローすべてが登録済み |
| 5 | docs/workflow.md 更新 | GHA スキルの記述（スキル一覧・設計方針）が追加されているか確認 | セクションが存在し、4スキルが記載 |
| 6 | inbox ファイル削除 | `inbox/gha-execution-file-fix-rollout.md` が削除されているか確認 | ファイルが存在しない |
| 7 | スキルの制約網羅性 | 各スキルの「やらないこと」が元の YAML 埋め込み制約を網羅しているか確認 | 主要な制約（CLI ルール非追従、PR 非作成、破壊的操作禁止等）が含まれている |
| 8 | GHA セキュリティルール準拠 | `run:` ブロックで `${{ }}` を直接展開せず `env:` 経由で渡しているか確認 | 違反なし |
| 9 | メタルール横断検証 | (1) フロー記述整合性 (2) workflow.md 同期 (3) TG-008 基準連動 | 3領域すべてで不適合なし、または起票済み |

## 評価スケジュール
- 全評価項目を一括で実施（単一セッション内で完了）

## 前提・制約
- 実際の GHA ワークフロー動作検証（Issue 作成 → ワークフロー起動）は本評価スコープ外
- スキルファイルの内容の「正しさ」は構造・制約網羅性で判定し、Claude の実行時動作は評価しない

---
**作成者**: L2（評価）
**作成日**: 2026-03-15
