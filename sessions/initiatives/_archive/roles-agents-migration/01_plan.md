# 実施計画: roles/ → .claude/agents/ 移行

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | 共通ルール分離 + ロール変換 + dev_manager 統合 + 参照更新 + roles/ 削除 | 全成功基準を満たすこと |

## 成功基準（全体）

1. `roles/` ディレクトリが削除されている
2. 8つの専門ロールが `.claude/agents/*.md` に YAML フロントマター付きで配置されている
3. `_base/common.md` の共通ルールが `.claude/rules/` に分離されている
4. `dev_manager` のオーケストレーションロジックが `.claude/skills/dispatcher/` に統合されている
5. `roles/` を参照していた全ファイル（歴史的記録を除く）のパスが更新されている
6. `grep -r 'roles/' --include='*.md'` で歴史的記録（docs/design/）以外にヒットしない

## リソース・前提条件

- 作業対象リポジトリ: `/home/nr202/projects/ai-driven-dev-patterns`
- 施策管理リポジトリ: `/home/nr202/projects/dev-process-improvement`
- Claude Code agents 仕様: YAML フロントマター（name, description, tools, model, skills 等）+ Markdown 本文
- `.claude/rules/` に配置したルールは全 agent に自動適用される

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 参照更新漏れ | 中 | 中 | 移行後に `grep -r 'roles/'` で残存チェック |
| agents 形式変換ミス | 低 | 中 | フロントマターのバリデーション、変換前後の内容 diff |
| dispatcher 統合の不整合 | 中 | 高 | 既存 dispatcher SKILL.md との差分を慎重に確認 |
| common.md 分割時の分類ミス | 低 | 中 | 分割方針を明確化（コミット規約・禁止事項・作業ループ等のテーマ別） |

---
**作成者**: L1
**作成日**: 2026-03-08
**最終更新**: 2026-03-08
