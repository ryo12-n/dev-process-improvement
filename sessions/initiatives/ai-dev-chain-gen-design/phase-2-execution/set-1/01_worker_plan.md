# ワーカー計画: ai-dev-chain-gen-design — Set-1

## 壁打ちフェーズ [2026-03-24 00:00]

### 理解のサマリー
- タスクの目的: `/gen-design` スキルのプロンプト実装を完成させ、requirements.json から openapi.yaml / design.md を自動生成できる状態にする
- スコープ: SKILL.md 実装、テンプレート整合更新、サンプルデータでの動作テスト、知見記録、課題転記
- 完了条件: SKILL.md に TODO なし、テンプレート整合、サンプル生成物が有効
- set 番号: set-1

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（gen-req 施策完了済み、requirements.json 存在）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read/Write/Edit ツール利用可能）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
- [x] set 番号確認: set-1
- [x] set ディレクトリの存在確認: 確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. T-001: SKILL.md のプロンプト実装（gen-req の 7 ステップパターン踏襲）
2. T-002: テンプレート（openapi.yaml / design.md）の整合更新
3. T-003: test-gen-req の requirements.json を入力として手動実行、成果物生成
4. T-004: 知見記録
5. T-005: 課題転記確認
