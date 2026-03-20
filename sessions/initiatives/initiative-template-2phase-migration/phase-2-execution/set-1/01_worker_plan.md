# ワーカー計画: initiative-template-2phase-migration — Set-1

## 壁打ちフェーズ [2026-03-20 03:00]

### 理解のサマリー
- タスクの目的: `sessions/initiatives/_template/` の実ディレクトリ構造を `session-lifecycle-policy` §1.4.3 の 2-phase 構造に改修する
- スコープ: ルートファイル7件のリネーム、phase-1-planning/phase-2-execution ディレクトリの作成、旧ファイル削除、ポリシー「移行中」注記解除
- 完了条件: T-001〜T-008 の全タスク完了、worker_report 記載
- set 番号: set-1（指定あり）

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（前施策でポリシー側は更新済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（git mv, mkdir, Write/Edit ツール）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（_template/ に旧16ファイル存在、phase-* は未作成）
- [x] set 番号確認: 指定あり: set-1
- [x] set ディレクトリの存在確認: 確認済み（phase-2-execution/set-1/ 存在）

### 不明点・確認事項
確認事項なし：実施開始

---

## 実施計画サマリ

T-001〜T-004 を順に実施する。T-001 は git mv で7件リネーム。T-002 は phase-1-planning ディレクトリ新規作成（gate + 8ファイル）。T-003 は phase-2-execution ディレクトリ新規作成（gate + 7ファイル）+ 旧ファイル8件削除。T-004 はポリシー注記削除 + 整合確認。T-005〜T-008 は固定タスクとして順次実施する。
