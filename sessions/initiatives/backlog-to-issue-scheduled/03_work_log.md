# 作業履歴: backlog-to-issue-scheduled

## 壁打ちフェーズ [2026-03-15 12:00]

### 理解のサマリー
- タスクの目的: バックログから定期的に Issue を自動起票する GHA ワークフローを構築する。承認ステップを排除し、6時間ごとに候補を1件ずつ自動消化する
- スコープ: (1) `select-backlog-candidate.sh` の全優先度対応・BL-ID 出力追加、(2) `backlog-to-issue.yml` への schedule トリガー追加、(3) 不要ワークフロー2件の削除
- 完了条件: T-001〜T-006 全完了、作業履歴・レポート記録済み、全変更コミット済み

### 前提条件チェック
- [x] 依存タスクの完了状態: 依存なし（独立タスク群）
- [x] 必要ツール・コマンドの利用可否: 確認済み（git, Bash）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
  - `select-backlog-candidate.sh` 存在確認済み
  - `backlog-to-issue.yml` 存在確認済み
  - `backlog-candidate-propose.yml` 存在確認済み（削除対象）
  - `backlog-auto-execute.yml` 存在確認済み（削除対象）
  - ブランチ `claude/l1-manager-Vs9fN` にいることを確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. **T-001**: `select-backlog-candidate.sh` を改修（優先度フィルタ撤廃、ソート順変更、`id` 出力追加）
2. **T-002**: `backlog-to-issue.yml` に `scheduled-create` ジョブを追加（schedule トリガー、候補選定、重複チェック、Issue 作成、wallbash ディスパッチ）
3. **T-003**: `backlog-candidate-propose.yml` を `git rm` で削除
4. **T-004**: `backlog-auto-execute.yml` を `git rm` で削除
5. **T-005**: 知見を `04_work_report.md` に記録
6. **T-006**: `07_issues.md` の課題を確認・転記判断

順序: T-001 → T-002 → T-003 → T-004 → コミット → T-005 → T-006 → 最終コミット

---

## 作業ログ

