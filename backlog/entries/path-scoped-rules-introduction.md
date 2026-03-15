# path-scoped rules 導入と commit-message.md 分離

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-070 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-15 |
| **起票元** | config-optimization/20260315 OPT-002 |

## 概要

rules/ の5ファイル（292行）に path-scoped rules を導入し、起動時読み込みを ~73行に削減する。commit-message.md（139行）はコア部分（35行）と sessions/ スコープの詳細テーブルに分離。session-start-branch-cleanup.md（88行）は docs/design/ に移動。

## 期待効果

- 起動時の rules/ コンテキスト消費を ~75% 削減（292行→~73行）
- commit-message.md の構造的肥大化問題を解消
