# 壁打ちログ: Phase/ワーカーセット構成の標準パターン化

> **このファイルの役割**: 壁打ちフェーズのコンテキスト保持用ログ。

---

## 現在の合意事項

### 施策の目的
3フェーズ×ワーカーセット構成の標準パターンを定義し、既存2マネージャーを統一する。

### スコープ
- やること: 標準パターン定義、テンプレート移動、SKILL.md/エージェント/ポリシー/workflow.md のパス更新
- やらないこと: 既存セッションデータ移行、メタテンプレート生成器（BL-090）

### 計画の方向性
- session-consistency 方式（Phase内配置）を基本とし、`workers/` 中間ディレクトリを廃止
- 標準パターン: `phase-N-xxx/_template/` → ランタイム `phase-N-xxx/set-1/`
- config-optimizer のルート `workers/` を各Phase内に分散移動

### 未解決事項
なし

---

## イテレーション履歴

### Round 1 [2026-03-19]
**入力**: backlog: phase-worker-set-standardization.md
**調査・推論**:
- session-consistency: `phase-N-xxx/workers/set-1/` パターン（Phase内に workers/ 中間ディレクトリ）
- config-optimizer: `workers/set-N/` パターン（ルート共有、set番号でPhase区別）
- バックログに「workers/ 中間ディレクトリ廃止」の提案あり
**更新内容**: 3つの不明点を提示し、ユーザーから回答取得
**合意事項の変更**:
1. session-consistency 方式（Phase内配置）＋ workers/ 廃止 → `phase-N-xxx/set-1/`
2. テンプレート変更のみ、既存セッションデータは移行しない
3. BL-090（メタテンプレート）とは分離

---
**作成日**: 2026-03-19
**施策ブランチ**: claude/l1-manager-NSRAs
