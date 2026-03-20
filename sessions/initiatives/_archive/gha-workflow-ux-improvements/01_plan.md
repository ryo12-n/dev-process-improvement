# 実施計画: gha-workflow-ux-improvements

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | ワークフロー YML 変更（T1〜T4） | 全 YML が構文的に正しく、変更意図が反映されている |
| 2 | README 最新化（T5） | README の記載が実態と一致している |
| 3 | GHA スキル・コメントテンプレート整合性確認 | `@ai` への変更がスキルファイル・コメント投稿箇所に一貫して反映されている |

## 変更対象ファイル一覧

| # | ファイル | 変更内容 |
|---|---------|---------|
| 1 | `.github/workflows/backlog-to-issue.yml` | cron `*/30 * * * *` → `0 */3 * * *` |
| 2 | `.github/workflows/initiative-dispatcher.yml` | `@ai-task` → `@ai`（トリガー条件・コマンドパース・エラーメッセージ） |
| 3 | `.github/workflows/initiative-dispatcher.yml` | `/start` 時に feedback（args）を wallbash に渡す |
| 4 | `.github/workflows/initiative-dispatcher.yml` | `/approve`（gate-review）時に feedback を close に渡す |
| 5 | `.github/workflows/initiative-close.yml` | `feedback` input 追加 + Claude prompt に反映 |
| 6 | `.github/workflows/initiative-wallbash.yml` | `/start` 時の feedback を Claude prompt に反映（init モードでも `/tmp/feedback.txt` に保存） |
| 7 | `.github/workflows/initiative-wallbash.yml` | コメント投稿のコマンド表示をフェンスドコードブロックに変更 + `@ai` 反映 |
| 8 | `.github/workflows/initiative-execute.yml` | コメント投稿のコマンド表示をフェンスドコードブロックに変更 + `@ai` 反映 |
| 9 | `.github/workflows/backlog-to-issue.yml` | Issue 作成時のガイド表示を `@ai` + フェンスドコードブロックに変更 |
| 10 | `.github/workflows/README.md` | 全面最新化（コマンドリファレンス・ワークフロー一覧・フロー図） |
| 11 | `.claude/skills/gha-wallbash/SKILL.md` | `@ai-task` → `@ai` の記載更新（該当箇所がある場合） |
| 12 | `.claude/skills/gha-execute/SKILL.md` | 同上 |
| 13 | `.claude/skills/gha-close/SKILL.md` | feedback input の活用記載追加 + `@ai` 更新 |
| 14 | `.claude/skills/gha-question/SKILL.md` | `@ai-task` → `@ai` の記載更新（該当箇所がある場合） |

## 成功基準（全体）
1. `@ai /start`, `@ai /continue`, `@ai /approve`, `@ai /reject`, `@ai /question` の全コマンドが dispatcher で正しくパースされる
2. 全コマンドで feedback（args）が下流ワークフローに渡され、Claude の prompt に含まれる
3. Issue コメント上のコマンド表示がフェンスドコードブロックで表示される
4. backlog-to-issue のスケジュールが3時間間隔になっている
5. README.md の記載が実態のワークフロー構成と一致している

## リソース・前提条件
- 変更は YAML・Markdown ファイルのみ（コード実装なし）
- テスト実行は不要（YAML の構文チェックと目視確認）

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| YAML 構文エラー | 低 | 高（ワークフロー停止） | フェンスドコードブロックの HEREDOC エスケープに注意 |
| フェンスドコードブロックの Markdown 入れ子問題 | 中 | 中 | Issue コメント投稿でバッククォート3連が HEREDOC 内で壊れないよう、別の引用方式を検討 |

---
**作成者**: L1
**作成日**: 2026-03-19
**最終更新**: 2026-03-19
