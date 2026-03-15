# 改善施策提案: backlog-to-issue-scheduled

## 背景・課題
バックログに施策候補が60件以上蓄積されているが、手動で Issue 化・施策化するフローのため消化が進まない。既存の `backlog-candidate-propose.yml` は承認ステップが挟まるため自動化のボトルネックとなっている。

## 目標
バックログの施策候補を6時間に1件ずつ、優先度の低いものから順に自動で GitHub Issue に起票し、`initiative-wallbash.yml` まで連携させるワークフローを構築する。承認ステップを排除し、バックログの自動消化を実現する。

## スコープ
### やること
- `backlog-to-issue.yml` に `schedule` トリガー（6時間ごと）を追加
- `select-backlog-candidate.sh` を全優先度対応（低→中→高順）に改修、BL-ID 出力を追加
- 重複 Issue 防止の仕組みを追加（既存 Issue の BL-ID チェック）
- 不要になった `backlog-candidate-propose.yml` と `backlog-auto-execute.yml` を削除

### やらないこと
- 施策の自動実行（wallbash 以降は既存フローに委ねる）
- `ai-driven-dev-patterns` や `横断` 対象リポジトリの施策の自動起票
- 既存の `workflow_dispatch`（手動起票）の動作変更

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果
- バックログ消化の自動化: 人間の介入なしに1日4件（6時間に1件）のペースで Issue 起票・wallbash が進む
- 承認フローの簡略化: 不要な承認ステップの排除によるリードタイム短縮

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| 不要な Issue の大量作成 | 中 | 重複チェック + ステータス「候補」のみフィルタで防止 |
| wallbash の連続実行による API コスト増 | 低 | 6時間間隔で制御。必要に応じて cron 間隔を調整可能 |

## 壁打ちの背景
- 既存 `backlog-candidate-propose.yml` の承認フロー（Issue 作成→ラベル付与→自動実行）は不要と判断。直接 Issue 起票 + wallbash で十分
- 優先度は全て対象（低→中→高の順で処理）。高優先度を手動に残す案もあったが、ユーザー判断で全自動を選択
- 対象リポジトリは `dev-process-improvement` のみ。GHA 環境での外部リポ変更は制約あり（ISS-027）
- 重複防止は Issue タイトルの `[BL-XXX]` パターンで既存 Issue をチェックする方式

## 備考・設計パターン
- 既存の `backlog-to-issue.yml` のロジック（Issue 作成 + wallbash ディスパッチ）を最大限再利用する
- `select-backlog-candidate.sh` は優先度の数値変換（低=1, 中=2, 高=3）でソートを実現する

---
**起票者**: L1
**起票日**: 2026-03-15
**ステータス**: 起票
**backlog元ファイル**: なし（新規提案）
