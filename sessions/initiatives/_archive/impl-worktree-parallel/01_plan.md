# 実施計画: impl-worktree-parallel

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | スキル・エージェント定義の変更 + テンプレート作成 | 全変更対象ファイルが整合的に更新されている |
| 2 | ドキュメント連動更新 + メタルール横断検証 | docs/workflow.md, docs/git-worktree-guideline.md が実態と一致 |

## 成功基準（全体）

1. impl-worker.md に worktree 対応の作業手順・per-worker issues・完了チェックリストが記載されている
2. SKILL.md に事前準備・マージ手順・3層検証チェックリスト（事前・ワーカー・事後）が記載されている
3. `07_issues_W_template.md` テンプレートが作成されている
4. `36_file_task_division.md`, `42_impl_work_report.md` テンプレートに worktree セクションが追加されている
5. impl-evaluator.md に Phase 4 worktree 関連評価基準が追加されている
6. impl-manager 配下の全ブランチ参照が `initiative/` → `impl/` に変更されている
7. `docs/workflow.md`, `docs/git-worktree-guideline.md` が変更内容と整合している
8. メタルール横断検証（フロー記述・workflow.md 同期・TG-008 基準連動）が合格している

## リソース・前提条件

- impl-manager 関連ファイルの現行構造を理解していること
- `docs/git-worktree-guideline.md` の既存内容を把握していること

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| ブランチ命名変更の影響範囲漏れ | 中 | 中 | 全 impl-manager 配下のファイルを grep で網羅検索 |
| チェックリストが冗長で実用性が低下 | 低 | 中 | 最小限の必須項目に絞り、回復手順を明記 |

---
**作成者**: L1
**作成日**: 2026-03-12
**最終更新**: 2026-03-12
