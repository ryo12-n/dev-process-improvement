# 壁打ちログ: impl-manager-refs-knowledge-read

> **このファイルの役割**: 壁打ちフェーズのコンテキスト保持用ログ。

---

## 現在の合意事項

### 施策の目的
l1-impl-manager の知見フローを「書き込み一方通行」から「読み書き双方向」にする。過去施策で蓄積した外部リポジトリの知見（構造理解・既知の制約・ハマりどころ）を実装時に活用できるようにする。

### スコープ
**やること:**
- l1-impl-manager/SKILL.md に refs/<リポ名>/knowledge.md 参照ステップを追加
- investigation-worker, design-worker, impl-plan-worker に知見読み込み手順を追加
- impl-worker はマネージャーからディスパッチ時に要約を受け取る形にする（直接 refs を読まない）
- ドメインエージェント参照（refs/agency-agents/knowledge.md）の仕組みを l1-manager から impl-manager に移植

**やらないこと:**
- refs の書き込みフロー（既に実装済み）の変更
- knowledge.md のフォーマット変更
- l1-manager 側の仕組みの変更

### 計画の方向性
- Phase 1-3 の各 worker は refs/knowledge.md を直接読む（調査・設計・計画フェーズは逐次実行のため効率的）
- Phase 4 の impl-worker はマネージャーがディスパッチ時に関連知見を要約して渡す（並列 Wave 実行のため効率重視）
- ドメインエージェント参照はタスク作成時に l1-impl-manager が選定し、worker へ指示に含める

### 未解決事項
なし

---

## イテレーション履歴

### Round 1 [2026-03-17]
**入力**: refs 配下の外部リポジトリ知見を実装マネージャーで参照・活用する仕組みを追加したい
**調査・推論**:
- l1-impl-manager/SKILL.md, 4つの worker エージェント、manager-common-policy を調査
- 書き込み（Phase 1 完了後 + クローズ時）は実装済みだが、読み込みは全エージェントで未実装を確認
- l1-manager のドメインエージェント参照の仕組みを比較参照
**更新内容**: 理解のサマリー・スコープ案・不明点を提示
**合意事項の変更**:
- impl-worker は直接 refs を読まず、マネージャーが要約を渡す方式に決定
- ドメインエージェント参照も今回の施策で一緒に移植する方針に決定

---
**作成日**: 2026-03-17
**施策ブランチ**: claude/l1-manager-VXDO2
