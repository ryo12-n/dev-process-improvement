# per-worker ファイル自動生成

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-094 |
| **優先度** | 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-18 |
| **依存する環境前提** | CLI / SDK |

## 課題・背景

並列ディスパッチ時に `_template/03_work_log_W_template.md` と `_template/07_issues_W_template.md` を per-worker ファイル（`03_work_log_W<N>.md`、`07_issues_W<N>.md`）にコピーし、ワーカー番号やタスクIDなどの既知値を事前記入する作業が手動で行われている。`parallel-dev.md` §2 の手順に従うが、毎回のコピー・置換・Conflict Check Matrix 検証が定型的で手動コストがある。

## 期待効果

- per-worker ファイル生成の自動化により、並列ディスパッチ準備の手動コストを削減
- 生成ミス（ワーカー番号の誤り、テンプレート未更新等）の防止

## 補足・参考情報

- 検出元: AT-001（20260318 オートメーション走査）
- 関連ルール: `.claude/rules/parallel-dev.md` §2
- AC-017（per-worker ファイル自動生成）として automation-candidates に登録済み
- AC-004（テンプレートコピーと施策ディレクトリ作成）とは対象が異なる
- 実装方針: `cp` + `sed` によるテンプレート化スクリプト

## 関連エントリ

- AC-017: per-worker ファイル自動生成（automation-candidates）
- AC-004: テンプレートコピーと施策ディレクトリ作成（関連するが対象スコープが異なる）
