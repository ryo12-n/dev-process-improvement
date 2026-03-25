# ワーカー計画: batch-rule-policy-minor-additions — Set-1

## 壁打ちフェーズ [2026-03-25 10:00]

### 理解のサマリー
- タスクの目的: 7件のルール・ポリシーファイルへの軽微追記 + 連動更新 + 固定タスクをバッチ処理する
- スコープ: T-001〜T-013（Wave 1: T-001〜T-007、Wave 2: T-008、Wave 3: T-009〜T-013）
- 完了条件: 全13タスクの完了 + git commit
- set 番号: 指定あり → set-1（逐次ディスパッチ）

### 前提条件チェック
- [x] 依存タスクの完了状態: 該当なし（Wave 1 は依存なし）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read/Edit/Write/Bash）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（全対象ファイル存在確認済み）
- [x] set 番号確認: 指定あり: set-1
- [x] set ディレクトリの存在確認: 確認済み
- [x] 外部リポジトリ成果物の記法スタイル確認（外部リポジトリあり施策のみ）: 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

### Wave 1: T-001〜T-007（ルール・ポリシー追記 7件）
1. T-001: rule-change-checklist に deny リスト副作用分析セクション追加
2. T-002: manager-common-policy §4 に課題重大度判定基準追加
3. T-003: manager-common-policy §5.4 にリファレンス文書粒度基準追加
4. T-004: session-flow-policy §2 に description 設計パターン追記
5. T-005: l1-manager の固定タスクセクションにサブヘッダ追加（構造のみ）
6. T-006: session-flow-policy §2・§3 に「関連ファイル一覧」追加
7. T-007: session-flow-policy §3 末尾にエージェント管理ガイドライン追加

### Wave 2: T-008（連動更新）
8. T-008: docs/workflow.md を T-001〜T-007 に対応して更新

### Wave 3: T-009〜T-013（固定タスク）
9. T-009: 知見記録
10. T-010: メタルール横断検証
11. T-011: rule-change-checklist 全7項目確認
12. T-012: 課題転記確認
13. T-013: projects/backlog-batch-execution 更新
