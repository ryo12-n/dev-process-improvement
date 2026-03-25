# 実施計画: batch-gha-minor-fixes

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | 4タスク一括実施・評価 | 下記成功基準(全体)を満たす |

## 成功基準（全体）
1. `gha-skills-mapping.yml` に initiative ワークフロー4件のマッピングが追加されている
2. GHA スキル6件の frontmatter に `disable-model-invocation: true` が設定されている
3. `gha-guideline/SKILL.md` に責務移動の対検証パターンが追記されている
4. `gha-guideline/SKILL.md` のセクション7.2 付近に用途クラス別「やらないこと」テンプレートが追記されている

## タスク概要

| # | BL-ID | タスク | 対象ファイル |
|---|-------|--------|------------|
| 1 | BL-080 | gha-skills-mapping.yml にマッピング4件追加 | `.github/gha-skills-mapping.yml` |
| 2 | BL-069 | GHA スキル6件に disable-model-invocation 追加 | `.claude/skills/gha-*/SKILL.md` (6件) |
| 3 | BL-081 | 責務移動の対検証パターン追記 | `.claude/skills/gha-guideline/SKILL.md` |
| 4 | BL-079 | 用途クラス別「やらないこと」テンプレート追記 | `.claude/skills/gha-guideline/SKILL.md` |

## リソース・前提条件
- 全タスク dev-process-improvement 内で完結、外部リポジトリ不要
- タスク3, 4 は同一ファイルへの追記だがセクションが異なるため競合なし

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| disable-model-invocation が GHA 起動に影響 | 低 | 低 | GHA は明示的起動のため影響なし |
| マッピング追加時の既存エントリとの不整合 | 低 | 低 | 既存構造を踏襲 |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
