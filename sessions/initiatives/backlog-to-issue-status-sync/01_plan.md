# 実施計画: backlog-to-issue-status-sync

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | 調査・方針決定・計画作成 | 00_proposal.md, 01_plan.md 作成完了 |
| 2 | 計画ワーカーによるタスク分割 | 02a_task_division.md 作成完了 |
| 3 | 計画評価・タスクリスト作成 | 06_eval_report.md, 02_tasks.md 作成完了 |
| 4 | 実施ワーカーによる修正実装 | 全修正ファイルのコミット完了、04_work_report.md 作成 |
| 5 | 評価ワーカーによる品質検証 | 06_eval_report.md 作成完了 |
| 6 | ゲート判定・クローズ | 08_gate_review.md 判定完了 |

## 修正対象ファイル一覧

| # | ファイル | 変更種別 | 変更内容 |
|---|---------|---------|---------|
| 1 | `.github/workflows/backlog-to-issue.yml` | MODIFY | `--state all` → `--state open` 変更、ステータス更新ステップ追加、`contents: write` 権限追加 |
| 2 | `scripts/generate-csvs.py` | MODIFY | STATUS_MAP に `"起票済み": "起票済み"` を追加 |
| 3 | `backlog/README.md` | MODIFY | ステータス値の説明に「起票済み」を追加 |

## 成功基準（全体）

1. `scheduled-create` ジョブの重複チェックが `--state open` でオープン issue のみを検索する
2. issue 起票成功後に対象エントリ `.md` のステータスが「起票済み」に自動更新される
3. 更新されたエントリが `select-backlog-candidate.sh` の候補選定から除外される（`ステータス != "候補"` のため）
4. `scripts/generate-csvs.py` が「起票済み」ステータスを正しく CSV に反映する
5. GHA セキュリティチェックリスト（`.claude/rules/gha-workflow-security.md`）に準拠した実装

## リソース・前提条件

- `.github/workflows/backlog-to-issue.yml` の構造理解（scheduled-create / create-issue の2ジョブ構成）
- `scripts/generate-csvs.py` の STATUS_MAP の仕組み
- backlog エントリの `.md` メタ情報テーブル形式
- GHA の `contents: write` 権限で git commit & push が可能であること

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| sed による .md 更新でファイル形式が壊れる | 低 | 中 | メタ情報テーブル内のステータス行のみをピンポイント置換。正規表現を最小スコープに限定 |
| git push の認証失敗 | 低 | 中 | GITHUB_TOKEN に contents: write 権限があれば通常動作する。エラー時はステップ失敗として通知される |
| 他のワークフローとのコミット競合 | 低 | 低 | schedule トリガーは3時間間隔。万一失敗しても次回実行で正常化 |

---
**作成者**: L1
**作成日**: 2026-03-17
**最終更新**: 2026-03-17
