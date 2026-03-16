# 外部リポジトリ知見: ai-driven-dev-patterns

## メタ情報

| 項目 | 内容 |
|------|------|
| 用途 | dev-process-improvement の施策でai-driven-dev-patternsを評価・改善する際の知見蓄積 |
| 有効期限 | 2026-06-16（初回記録から3ヶ月。定期レビューセッションで更新を検討） |
| 取得日 | 2026-03-15 |
| 取得方法 | GHA環境で `git clone https://github.com/...` → Glob/Read ツールで調査 |

## リポジトリ概要

| 項目 | 内容 |
|------|------|
| リポジトリ名 | ai-driven-dev-patterns |
| 主要技術スタック | Markdown（エージェント定義・ルール）、YAML（openspec/）、JSON（settings.json）|
| ディレクトリ構成 | `.claude/agents/`（8エージェント）、`.claude/skills/`（dispatcher等）、`.claude/rules/`（5ルール）、`docs/design/`（6ファイル）、`openspec/`、`sessions/` |

## 蓄積された知見

<!-- 最新の知見を上に追記する。施策ごとにセクションを追加する。 -->

| # | 施策名 | 日付 | 知見カテゴリ | 内容 | 元ログ |
|---|--------|------|------------|------|--------|
| 1 | harness-engineering-brushup | 2026-03-15 | アーキテクチャ | 全5観点スコア3/5（均一）。テストインフラ未整備（feature-builder/test-writer のTODO未解消）が唯一の機能不全ブロッカー。改善候補詳細は04_work_report.md参照 | sessions/initiatives/_archive/harness-engineering-brushup/04_work_report.md |
| 2 | harness-engineering-brushup | 2026-03-15 | 制約 | documentarian が参照する `rules/design-doc.md` と `rules/code-in-docs.md` が `.claude/rules/` に存在しない（参照切れ）。設計書作成時にルールが機能しないリスク | sessions/initiatives/_archive/harness-engineering-brushup/07_issues.md |
| 3 | harness-engineering-brushup | 2026-03-15 | ツール設計 | reviewer エージェントの `tools:` frontmatter に Bash が含まれるが、本文では「静的確認のみ」と定義。ツール宣言と説明文の整合性に不整合あり | sessions/initiatives/_archive/harness-engineering-brushup/04_work_report.md |

## ハーネスエンジニアリング5観点スコア（2026-03-15評価）

| 観点 | スコア | 最大の強み | 最大の弱み |
|------|--------|-----------|-----------|
| 1. コンテキスト管理 | 3/5 | 3層コスト分類・壁打ちフェーズ | クロスセッション状態管理なし |
| 2. ツール設計 | 3/5 | ロールごとのツール制限 | ツールポリシー分散管理 |
| 3. タスク分割・長距離走 | 3/5 | 1タスク1エージェント・フェーズゲート | テスト付きタスク分解が未完 |
| 4. 検証とガードレール | 3/5 | reviewer・テスト禁止ルール | テストインフラ未整備 |
| 5. 観測とログ | 3/5 | 知見義務化・ルーティング設計 | 定量メトリクスなし |

---
**初回記録日**: 2026-03-16
**起票施策**: harness-engineering-brushup
