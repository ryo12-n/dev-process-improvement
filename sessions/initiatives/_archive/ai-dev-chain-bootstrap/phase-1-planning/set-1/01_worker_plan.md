# ワーカー計画: ai-dev-chain-bootstrap — Set-1

## 壁打ちフェーズ [2026-03-24 00:00]

### 理解のサマリー
- タスクの目的: AI Dev Chain の土台作り。`projects/_template/` ディレクトリと 6 Skills の SKILL.md 骨格を作成する
- スコープ: テンプレートファイル（request.md, backlog.md, artifacts/配下 8 ファイル）+ 6 Skills の SKILL.md（project-init, gen-req, gen-design, gen-tests, gen-ci, gen-tasks）
- 完了条件: 全プレースホルダーファイルが存在し、6 Skills が `user-invocable: true` で認識可能な状態

### 前提条件チェック
- [x] 施策計画（02_plan.md）の内容を理解: 理解済み
- [x] 提案書（01_proposal.md）の確認: 確認済み
- [x] 変更対象ファイル群の特定: 特定済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：計画開始

---

## 分析計画サマリ

### 調査結果

- `projects/` ディレクトリは未作成（全ファイル CREATE）
- `.claude/skills/` 配下に gen-* / project-init ディレクトリは未作成（全ファイル CREATE）
- 既存 Skill（l1-manager）のフロントマター構造を確認済み: `name`, `description`, `user-invocable` フィールド使用

### 分割方針

- Phase A（テンプレート）と Phase B（Skills）は独立しているが、project-init Skill は _template の構成を READ 参照する
- Phase A 内の全ファイルは互いに独立（別ディレクトリ・別ファイル）→ 1 タスクにまとめて効率化
- Phase B 内の 6 Skills は互いに独立（別ディレクトリ）→ project-init は _template を READ 参照するため Phase A 依存、残り 5 Skills は独立
- 5 gen-* Skills は構造が同一（フロントマター + 入出力仕様 + TODO）のため、並列可能
