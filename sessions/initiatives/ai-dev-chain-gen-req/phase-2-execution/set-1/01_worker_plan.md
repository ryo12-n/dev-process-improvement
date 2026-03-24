# ワーカー計画: ai-dev-chain-gen-req — Set-1

## 壁打ちフェーズ [2026-03-24 10:00]

### 理解のサマリー
- タスクの目的: gen-req SKILL.md のプロンプト実装（骨格→完全な Skill 化）とサンプル要望書での動作テスト
- スコープ: T-001〜T-005（テスト用プロジェクト作成、SKILL.md 実装、動作テスト、知見記録、課題転記）
- 完了条件: SKILL.md に TODO なし、test-gen-req で有効な JSON/MD 生成、作業レポート作成
- set 番号: 指定あり → set-1

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（bootstrap 施策で骨格作成済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read/Write/Edit/Bash）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（`projects/_template/`, `gen-req/SKILL.md`, `refs/ai-dev-chain/overview.md` 全て存在）
- [x] set 番号確認: 指定あり: set-1
- [x] set ディレクトリの存在確認: 確認済み
- [x] 外部リポジトリ成果物の記法スタイル確認（外部リポジトリあり施策のみ）: 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. **T-001**: `projects/_template/` を `projects/test-gen-req/` にコピーし、`request.md` に REST API 書籍管理システムのサンプル要望書を記述する
2. **T-002**: `gen-req/SKILL.md` の処理フロー（プロンプト）を完全実装する。TODO 5項目を解消し、`_template/artifacts/` のスキーマ・テンプレートも整合性を保って更新する
3. **T-003**: SKILL.md の処理フローに従い、`test-gen-req/request.md` から `requirements.json` / `requirements.md` を手動生成し、品質確認する
4. **T-004**: 知見を worker report に記録する
5. **T-005**: 課題の転記判断を行う
