# 実施計画: GHA施策パイプライン一気通貫実行と並列化

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | 一気通貫実行の実装（execute.yml 自動連鎖 + gha-execute スキル修正 + dispatcher 修正） | execute 完了後に verdict を抽出し、通過時は close を自動ディスパッチ、差し戻し時は自動リトライする |
| 2 | 並列化の実装（cron 間隔短縮 + batch-approve ワークフロー新規作成） | 30分間隔で起票され、一括 approve で複数施策を同時実行できる |

## 成功基準（全体）
1. `initiative-execute.yml` 完了後、ゲート判定「通過」の場合に `initiative-close.yml` が自動ディスパッチされる
2. ゲート判定「差し戻し」の場合に最大2回の自動リトライが実行され、上限超過時は停止して Issue にコメントされる
3. `backlog-to-issue.yml` が30分間隔でバックログを起票する
4. `initiative-batch-approve.yml` が壁打ち完了済みの全施策に対して execute を一括ディスパッチする
5. GHA セキュリティチェックリスト全項目を満たす

## リソース・前提条件
- 既存の `initiative-execute.yml`、`initiative-close.yml`、`initiative-dispatcher.yml`、`backlog-to-issue.yml` が正常動作していること
- `gha-execute/SKILL.md` の Claude 実行出力が `claude-execution-output.json` に保存される既存仕様を利用

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| GATE_VERDICT マーカーが Claude 出力に含まれない | 中 | 高 | フォールバック: マーカー未検出時は gate-review ラベルで停止（従来動作） |
| 自動リトライの無限ループ | 低 | 高 | retry_count 上限2回 + 超過時の Issue コメント通知 |
| 30分間隔での API レート制限 | 低 | 中 | 候補なし時は早期終了（既存ロジック） |

---
**作成者**: L1
**作成日**: 2026-03-19
**最終更新**: 2026-03-19
