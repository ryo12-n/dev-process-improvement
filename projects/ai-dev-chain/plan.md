# 全体計画書: ai-dev-chain

## 目的
人間が要望書（`request.md`）を書くと、Claude Code の Skills チェーンがシステム開発を自動的に進める仕組みを構築する。

```
request.md（要望書）
    ↓ /gen-req
requirements.json / requirements.md
    ↓ /gen-design
openapi.yaml / design.md
    ↓ /gen-tests
tests.json / tests.md
    ↓ /gen-ci
ci/pipeline.yaml（GitHub Actions）
    ↓ 人間レビュー＆承認
    ↓ /gen-tasks
tasks.json
    ↓ l1-impl-manager（既存 Skill）
実装コード / CI パス
```

## スコープ
- 実装先リポジトリ: `dev-process-improvement`
- 動作環境: Claude Code CLI（`/スキル名` コマンドで呼び出し）
- サンプルプロジェクト: `projects/bookshelf-api/`
- 恒久計画書: `refs/ai-dev-chain/overview.md`

## 施策一覧

| # | 施策名 | 概要 | BL-ID | 優先度 | ステータス |
|---|--------|------|-------|--------|-----------|
| 1 | ai-dev-chain-bootstrap | `projects/_template/` と project-init Skill の骨格作成 | - | 高 | 完了 |
| 2 | ai-dev-chain-gen-req | gen-req Skill プロンプト実装 | BL-104 | 高 | 完了 |
| 3 | ai-dev-chain-gen-design | gen-design Skill プロンプト実装 | BL-105 | 高 | 完了 |
| 4 | ai-dev-chain-gen-tests | gen-tests Skill プロンプト実装 | BL-106 | 中 | 完了 |
| 5 | ai-dev-chain-gen-ci | gen-ci Skill プロンプト実装 | BL-107相当 | 中 | 未着手 |
| 6 | ai-dev-chain-gen-tasks | gen-tasks Skill プロンプト実装 | - | 中 | 未着手 |
| 7 | ai-dev-chain-e2e | サンプル要望書で E2E 通し確認 | - | 低 | 未着手 |

## マイルストーン

| # | マイルストーン | 完了条件 | ステータス |
|---|-------------|---------|-----------|
| M1 | テンプレート・骨格作成 | `projects/_template/` と project-init Skill が存在 | 完了 |
| M2 | project-init Skill 作成 | `/project-init` でプロジェクトディレクトリが生成される | 完了 |
| M3 | gen-req Skill 作成 | `/gen-req` で requirements.json/md が正常生成される | 完了 |
| M4 | gen-design Skill 作成 | `/gen-design` で openapi.yaml/design.md が正常生成される | 完了 |
| M5 | gen-tests Skill 作成 | `/gen-tests` で tests.json/md が正常生成される | 完了 |
| M6 | gen-ci Skill 作成 | `/gen-ci` で ci/pipeline.yaml が正常生成される | 未着手 |
| M7 | gen-tasks Skill 作成 | `/gen-tasks` で tasks.json が正常生成される | 未着手 |
| M8 | E2E 通し確認 | サンプル要望書からチェーン全体が通しで動作する | 未着手 |

## 方針・制約
- 各 Skill は gen-req/gen-design で確立した7ステップパターンを踏襲する
- 検証は `projects/bookshelf-api/`（BookShelf API）で行う
- 各 Skill の実装は独立した initiative として管理する
- `refs/ai-dev-chain/overview.md` が恒久計画書（Source of Truth）。本ファイルはプロジェクト管理用の派生

---
**作成日**: 2026-03-25
**最終更新**: 2026-03-25
