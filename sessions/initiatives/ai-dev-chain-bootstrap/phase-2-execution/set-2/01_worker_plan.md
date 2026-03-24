# ワーカー計画: ai-dev-chain-bootstrap — Set-2

## 壁打ちフェーズ [2026-03-24 10:00]

### 理解のサマリー
- タスクの目的: 5つの gen-* Skills（gen-req / gen-design / gen-tests / gen-ci / gen-tasks）の SKILL.md 骨格を作成する
- スコープ: `.claude/skills/gen-*/SKILL.md` 5ファイルの新規作成。骨格のみでプロンプト実装は後続施策
- 完了条件: 全5ファイルに YAML フロントマター・引数仕様・入出力仕様・チェーン前後関係・TODO コメントが記載されていること
- set 番号: 指定あり → set-2

### 前提条件チェック
- [x] 依存タスクの完了状態: 依存なし（T-003 は Wave 1 で T-001 と並列実行可）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Write ツールでファイル作成可能）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（.claude/skills/ ディレクトリ存在、gen-* ディレクトリは未作成で新規作成が必要）
- [x] set 番号確認: 指定あり: set-2
- [x] set ディレクトリの存在確認: 確認済み（phase-2-execution/set-2/ 配下にテンプレートファイルが存在）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. `refs/ai-dev-chain/overview.md` の Skills 一覧と入出力仕様を基に、5つの SKILL.md を順次作成
2. 各ファイルは共通構造（YAML フロントマター → 概要 → 引数仕様 → 入出力仕様 → チェーン前後関係 → 処理フロー → TODO）で統一
3. l1-manager/SKILL.md のフロントマター構造（`name`, `description`, `user-invocable: true`）を踏襲
4. 作成順序: gen-req → gen-design → gen-tests → gen-ci → gen-tasks（チェーンの上流から下流へ）
