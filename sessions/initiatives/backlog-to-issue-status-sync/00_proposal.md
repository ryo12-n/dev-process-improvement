# 改善施策提案: backlog-to-issue-status-sync

## 背景・課題

`backlog-to-issue.yml` の `scheduled-create` ジョブに2つの欠陥が発見された（`refs/test/job-logs (21).txt` で確認）。

### 問題1: 重複チェックの過剰検出
- L127 で `gh issue list --search "[${BACKLOG_ID}] in:title" --state all` を使用
- クローズ済み issue もヒットし、再起票が必要なバックログエントリがスキップされる
- **実例**: BL-012 は過去に起票→クローズ済みだが、再度候補として選ばれた際にクローズ済み issue を検出して「Duplicate issue found for BL-012. Skipping.」となった

### 問題2: backlog エントリのステータス未更新
- issue 起票後に `backlog/entries/*.md` のステータスが「候補」のまま放置される
- `select-backlog-candidate.sh` は `ステータス == "候補"` でフィルタするため、起票済みエントリが何度も候補に選ばれ続ける
- 3時間ごとのスケジュール実行で毎回同じエントリが選ばれ、重複チェックでスキップされるという無駄なサイクルが発生

## 目標

1. 重複チェックをオープン issue のみに限定し、クローズ済み issue の再起票を可能にする
2. issue 起票後に backlog エントリのステータスを「起票済み」に自動更新し、候補選定からの除外を確実にする

## スコープ
### やること
- `.github/workflows/backlog-to-issue.yml` の `--state all` → `--state open` 変更（scheduled-create ジョブ）
- 同ワークフローの `scheduled-create` ジョブに issue 起票後のエントリ `.md` ステータス更新 + git commit & push ステップを追加
- `contents: write` 権限の追加（scheduled-create ジョブ）
- `scripts/generate-csvs.py` の STATUS_MAP に「起票済み」マッピングを追加
- `backlog/README.md` のステータス値説明を更新

### やらないこと
- `create-issue` ジョブ（workflow_dispatch）の変更（手動実行は L1 管理下のため別途検討）
- backlog.csv の直接編集（CSV は自動生成のため .md の更新で対応）
- 既存の起票済みエントリ（BL-012 等）の遡及的なステータス修正

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- クローズ済み issue があるバックログエントリの再起票が可能になる
- 起票済みエントリが候補選定で再選択されなくなり、GHA の無駄な実行サイクルが解消される
- バックログのステータス管理が自動化され、手動更新の漏れが防止される

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| GHA の contents:write 追加によるセキュリティリスク | 低 | scheduled-create ジョブ内のみ、かつ backlog/entries/ 配下のみを変更。gha-workflow-security チェックリストに従いインジェクション防止を徹底 |
| git commit & push の競合（他のワークフローと同時実行時） | 低 | schedule トリガーは3時間間隔のため競合可能性は極めて低い。万一失敗しても次回実行で正常化する |

## 壁打ちの背景

- **ステータス値**: 「起票済み」を新規追加。既存の「候補 / initiative 開始済」に加え、issue 起票→initiative 開始の中間ステータスとして定義。`select-backlog-candidate.sh` は「候補」のみフィルタするため、「起票済み」にすれば自動的に候補から除外される
- **CSV 更新方式**: CSV は `scripts/generate-csvs.py` により `.md` から自動生成されるため、`.md` のステータスを直接更新する方式を採用。GHA 内で `sed` による `.md` 更新 + git commit & push で対応する
- **workflow_dispatch ジョブ（create-issue）**: 手動実行は L1 が管理するフローであり、ステータス更新は L1 の運用で対処可能なためスコープ外とした

## 備考・設計パターン

GHA ワークフロー内での git 操作は `.claude/rules/gha-workflow-security.md` のセキュリティチェックリストに従う。特に `${{ }}` の直接展開を避け `env:` 経由で渡すこと。

---
**起票者**: L1
**起票日**: 2026-03-17
**ステータス**: 起票
**backlog元ファイル**: なし（ログ調査からの直接施策化）
