# ai-driven-dev-patterns: ツールポリシーの集中管理

## 気づき

ai-driven-dev-patterns の各エージェントは `tools:` を frontmatter で個別定義しているが、共通のツールポリシー（最小権限の定義・禁止ツール一覧）が集中管理されていない。変更漏れリスクと整合性の問題が発生しやすい。

具体的な不整合例として、`reviewer.md` は本文で「静的確認のみ」と定義しながら `tools: Bash` が含まれており、ツール宣言と説明文が矛盾している。

## 提案

以下の施策として起票する候補：

1. `.claude/rules/tool-policy.md` に共通ツールポリシー（ロール別最小権限マトリクス）を定義する
2. 各エージェントの `tools:` と本文説明の整合性を検証・修正する
3. 特に reviewer の Bash 使用可否を設計方針に基づき明確化する

## 背景

- 施策: harness-engineering-brushup（ハーネスエンジニアリング観点2: ツール設計 評価で発見）
- 評価スコア: 3/5、最大の弱み: ツールポリシー分散管理
- 対象リポジトリ: ai-driven-dev-patterns

---
**記録日**: 2026-03-16
**発生施策**: harness-engineering-brushup
