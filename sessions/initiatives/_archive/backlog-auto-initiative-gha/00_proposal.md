# 改善施策提案: backlog-auto-initiative-gha

## 背景・課題

backlog に優先度「低」の項目が約23件滞留しており、手動での施策化が追いつかない。現在の L1 マネージャーセッションは人間の起動と壁打ちフェーズを前提としているため、低優先度の項目は後回しになり続ける構造的な問題がある。

## 目標

GitHub Actions の定期実行により、低優先度バックログ項目を自動で施策化する仕組みを構築する。
- 3時間ごとに候補を1件提示し、人間の承認後に Claude Code CLI で L1→L2 フローを自動実行する
- 低優先度バックログの消化速度を向上させる

## スコープ
### やること
- `.github/workflows/backlog-candidate-propose.yml`（Phase 1: 候補選択・Issue 作成）の作成
- `.github/workflows/backlog-auto-execute.yml`（Phase 2: 承認後の Claude Code 自動実行）の作成
- `.github/scripts/select-backlog-candidate.sh`（CSV パース・候補選択ロジック）の作成
- `docs/workflow.md` への自動施策化フローセクション追加

### やらないこと
- 優先度「中」「高」の項目の自動施策化（人間の判断が必要）
- `ai-driven-dev-patterns` や横断施策の自動実行（SDK 環境制約）
- `ANTHROPIC_API_KEY` の設定作業（手動で GitHub Secrets に追加）
- GitHub ラベル（`auto-initiative-pending` 等）の作成（手動設定）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- 低優先度バックログ23件を、承認ベースで段階的に自動消化
- L1 マネージャーの手動起動コストの削減
- バックログの滞留期間短縮

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| Claude Code の自動実行が不完全な成果物を生成する | 中 | PR レビューで人間がチェック。`--max-turns 30` で無限ループ防止 |
| API コスト増加 | 低 | `claude-sonnet-4-6` を使用しコスト最適化。承認制で実行頻度を制御 |
| Issue 通知の氾濫 | 低 | 同時1件の承認待ち制限で防止 |

## 壁打ちの背景

- **実行方式**: Claude Code CLI（`anthropics/claude-code-action@v1`）を選択。API 直接呼び出しより L1/L2 フローとの親和性が高い
- **承認フロー**: Issue での事前承認方式を採用。壁打ちフェーズの代替として機能し、人間の最終判断を残す
- **実行頻度**: 3時間ごとに候補提示。1件ずつ処理することで管理可能性を確保
- **対象制限**: `dev-process-improvement` リポジトリ内で完結する施策のみ対象（SDK 環境制約）

## 備考・設計パターン

2フェーズアーキテクチャ:
- Phase 1（cron 3h）: CSV パース → 候補選択 → Issue 作成
- Phase 2（label trigger）: Issue 承認 → Claude Code 実行 → PR 作成 → Issue クローズ

`anthropics/claude-code-action@v1` の主要パラメータ:
- `prompt`: L1 フローの非対話実行指示
- `claude_args`: `--max-turns 30 --model claude-sonnet-4-6`
- `anthropic_api_key`: `${{ secrets.ANTHROPIC_API_KEY }}`

---
**起票者**: L1
**起票日**: 2026-03-13
**ステータス**: 実施中
**backlog元ファイル**: なし（新規提案）
