# 実施計画: backlog-auto-initiative-gha

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | GHA ワークフロー・スクリプト作成 | 3ファイルが作成され、YAML 構文が正しいこと |
| 2 | docs 更新・知見記録 | `docs/workflow.md` に自動施策化フローが追記されていること |

## 成功基準（全体）

1. `.github/workflows/backlog-candidate-propose.yml` が作成され、cron + workflow_dispatch の2トリガーが定義されていること
2. `.github/workflows/backlog-auto-execute.yml` が作成され、`auto-initiative-approved` ラベルトリガーで `claude-code-action@v1` が実行される構成であること
3. `.github/scripts/select-backlog-candidate.sh` が作成され、CSV パースが正しく動作すること
4. セキュリティ: API キーがハードコードされていないこと、permissions が最小権限であること

## リソース・前提条件

- `anthropics/claude-code-action@v1` が利用可能であること
- リポジトリに GitHub Actions が有効であること
- 施策完了後に手動設定が必要: `ANTHROPIC_API_KEY` の Secrets 登録、3種のラベル作成

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| claude-code-action の仕様変更 | 低 | 中 | `@v1` メジャーバージョン固定で安定化 |
| CSV パースの文字化け・エッジケース | 中 | 低 | UTF-8 前提、日本語対応テスト |
| 自動実行の成果物品質が低い | 中 | 中 | PR レビューで人間がチェック |

---
**作成者**: L1
**作成日**: 2026-03-13
**最終更新**: 2026-03-13
