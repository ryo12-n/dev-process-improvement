# 実施計画: GHA Initiative ワークフロー

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | ワークフロー3ファイル作成 + gha-guideline 更新 | 3ファイルが構文的に正しく、ラベル設計が完了 |

## 成功基準（全体）
1. `initiative-wallbash.yml` が `issues:labeled` と `workflow_dispatch` でトリガーされ、壁打ちサマリーを Issue コメントに投稿する
2. `initiative-execute.yml` が `/approve` コメントで起動し、計画・実行・評価・ゲート判定を自律実行する
3. `initiative-close.yml` が `/approve` コメントでアーカイブ・Issue クローズを行う
4. フェーズ間の状態引き継ぎが PR ブランチ経由で機能する
5. `gha-guideline` に新ワークフローの権限マトリクスが追記されている

## リソース・前提条件
- `anthropics/claude-code-action@v1` が利用可能であること
- `ANTHROPIC_API_KEY` シークレットが設定済みであること
- 既存の `backlog-auto-execute.yml` のパターンを踏襲する

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| issue_comment が bot 自身のコメントで再トリガーする | 中 | 中 | user.login フィルタ |
| PR 検索で Issue 番号から正しい PR が見つからない | 低 | 高 | PR 本文に Issue 番号をリンクし、検索精度を確保 |

---
**作成者**: L1
**作成日**: 2026-03-14
**最終更新**: 2026-03-14
