# Phase/ワーカーセット構成の標準パターン化

## 提案の概要

session-consistency-manager と config-optimizer-manager で共通する「3フェーズ×ワーカーセット」のディレクトリ構成を、マネージャーセッションの標準構成として抽象化・共通化する。

## 背景

- session-consistency-manager で `workers/set-N/` を `phase-N-xxx/workers/set-1/` に再配置済み（2026-03-18）
- config-optimizer-manager にも同一構造があり、同様の変更が必要
- 両マネージャーは同じ「Phase 1→2→3 逐次実行 × Phase ごとに1ワーカーセット」パターンを持つ
- このパターンを標準化すれば、将来の3フェーズマネージャー追加時にも一貫した構造を提供できる

## 具体的な改善内容

### 1. `workers/` 中間ディレクトリの廃止

現在（session-consistency-manager 修正後）:
```
phase-1-collection/
├── 01_gate.md
└── workers/set-1/  ← workers/ が冗長
```

提案:
```
phase-1-collection/
├── 01_gate.md
└── set-1/  ← Phase 配下に直接配置
```

Phase ディレクトリ配下に置く時点で「ワーカーの成果物」は自明なため、`workers/` は不要。

### 2. 標準パターンの抽象化

以下を共通パターンとして定義する:
- テンプレート構造: `_template/phase-N-xxx/set-1/` (7ファイル: 01_tasks〜07_issues)
- ゲートファイル: `phase-N-xxx/01_gate.md`
- セット番号: Phase 内で set-1 始まり（複数セット時に set-2, set-3 と増やす）

### 3. 適用対象

- session-consistency-manager: `workers/` 中間ディレクトリを削除
- config-optimizer-manager: 現在の `workers/set-N/` フラット構造を Phase 配下に再配置 + `workers/` 廃止
- 将来の3フェーズマネージャー: 標準パターンに準拠

## 優先度の判断材料

- Impact: 中（構造の一貫性・可読性向上、新マネージャー追加時のガイドライン）
- Effort: 中（2マネージャーのスキル定義・エージェント定義・テンプレートの修正）
- session-consistency-manager は直前の修正から差分が小さい（`workers/` 削除のみ）

## 起票日

2026-03-18

## 起票元

session-consistency-manager 20260317 セッション後のユーザーとの協議
