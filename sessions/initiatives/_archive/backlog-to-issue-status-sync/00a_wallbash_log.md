# 壁打ちログ: backlog-to-issue-status-sync

> **このファイルの役割**: 壁打ちフェーズのコンテキスト保持用ログ。

---

## 現在の合意事項

### 施策の目的
backlog-to-issue ワークフローの重複チェック不具合修正と、issue 起票後のバックログステータス自動更新を実装する。

### スコープ
- やること: scheduled-create ジョブの `--state all` → `--state open` 変更、エントリ .md のステータス自動更新、STATUS_MAP 追加、README 更新
- やらないこと: workflow_dispatch ジョブの変更、既存エントリの遡及修正

### 計画の方向性
- GHA ワークフロー内で `sed` + git commit & push によりエントリ .md を直接更新
- `contents: write` 権限を scheduled-create ジョブに追加
- 新ステータス値「起票済み」を導入

### 未解決事項
なし

---

## イテレーション履歴

### Round 1 [2026-03-17]
**入力**: ユーザーからログファイル `refs/test/job-logs (21).txt` の確認依頼。BL-012 がクローズ済み issue の重複としてスキップされた事象。
**調査・推論**: ワークフロー L127 の `--state all` が根本原因。加えて backlog.csv のステータス未更新により候補が繰り返し選ばれる問題を特定。
**更新内容**: 00_proposal.md を作成。
**合意事項の変更**: ステータス値「起票済み」、CSV は .md から自動生成のため .md を直接更新する方式で合意。

---
**作成日**: 2026-03-17
**施策ブランチ**: claude/l1-manager-6J2U4
