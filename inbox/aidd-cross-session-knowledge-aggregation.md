# ai-driven-dev-patterns: クロスセッション知識集約の仕組み整備

## 気づき

ai-driven-dev-patterns はセッション状態をファイル（sessions/配下）にのみ依存しており、セッション横断でのメモリ・状態集約の仕組みがない。dev-process-improvement の `refs/<リポ名>/knowledge.md` モデルが有効な参考になる。

具体的な問題：
- セッション完了後の知見が sessions/ に埋もれ、横断参照が困難
- 次セッション開始時に過去の設計判断・技術的制約を再調査する必要がある
- 複数施策を通じて同じ問題を再発見するリスクがある

## 提案

以下の施策として起票する候補：

1. `refs/` または `knowledge/` ディレクトリを ai-driven-dev-patterns に導入する
2. dispatcher エージェントの知見ルーティングステップに「knowledge.md への記録」を追加する
3. dev-process-improvement の manager-common-policy §5.3 相当のルールを ai-driven-dev-patterns 向けに定義する

## 背景

- 施策: harness-engineering-brushup（ハーネスエンジニアリング観点1: コンテキスト管理 評価で発見）
- 評価スコア: 3/5、改善候補: セッション横断でのメモリ/状態集約
- 対象リポジトリ: ai-driven-dev-patterns

---
**記録日**: 2026-03-16
**発生施策**: harness-engineering-brushup
