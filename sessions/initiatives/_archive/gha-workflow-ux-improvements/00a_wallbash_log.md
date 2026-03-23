# 壁打ちログ: gha-workflow-ux-improvements

> **このファイルの役割**: 壁打ちフェーズのコンテキスト保持用ログ。

---

## 現在の合意事項

### 施策の目的
GHA ワークフローの操作性を改善する（スケジュール調整・コマンド短縮・コピーしやすいUI・feedback 伝播・README 最新化）。

### スコープ
- やること: backlog-to-issue スケジュール変更、`@ai-task` → `@ai` 短縮、コマンド表示改善、全コマンド feedback 伝播、README 最新化
- やらないこと: ワークフローロジック変更、新規ワークフロー追加

### 計画の方向性
- ワークフロー YML 5ファイル + README + GHA スキル 4ファイルを対象に修正
- YAML・Markdown のみの変更（コード実装なし）

### 未解決事項
なし

---

## イテレーション履歴

### Round 1 [2026-03-19]
**入力**: ユーザーから4つの改善要望（スケジュール変更・@ai-task 撤廃検討・approve 後 feedback・README 最新化）
**調査・推論**:
- 全ワークフロー YML を読み、現状のトリガー条件・feedback 伝播状況を把握
- `@ai-task` 完全撤廃の弊害を分析し、短縮案 `@ai` を提案
- feedback ギャップ箇所を特定（`/start` → wallbash, `/approve` gate-review → close）
- README と実態の乖離を確認（不在ワークフロー記載、batch-approve 未記載）
**更新内容**: 00_proposal.md, 01_plan.md 作成
**合意事項の変更**:
- `@ai-task` → `@ai` に短縮（完全撤廃ではない）
- 全コマンドで feedback 伝播対応
- フェンスドコードブロックでコピーしやすく

---
**作成日**: 2026-03-19
**施策ブランチ**: claude/l1-manager-Zccmu
