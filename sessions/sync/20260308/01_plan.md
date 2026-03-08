# 同期計画: 2026-03-08

## 同期パラメータ

- 同期元（{source_repo}）: dev-process-improvement (`/home/nr202/projects/dev-process-improvement/`)
- 同期先（{target_repo}）: ai-driven-dev-patterns (`/home/nr202/projects/ai-driven-dev-patterns/`)
- 同期方向: dev-process-improvement → ai-driven-dev-patterns
- 同期スコープ（{sync_scope}）: `.claude/rules/`, `.claude/skills/`（一部）, `sessions/initiatives/_template/`

## 同期対象ファイルリスト

| # | ファイル/ディレクトリ | 同期方針 | 備考 |
|---|---------------------|---------|------|
| 1 | `.claude/rules/commit-message.md` | 統一 | 同期先の既存ファイルと比較し、session-type の網羅性を統一する |
| 2 | `.claude/rules/session-start-branch-cleanup.md` | 導入 | 同期先に新規導入。パス参照を同期先に適応させる |
| 3 | `.claude/skills/rule-change-checklist/SKILL.md` | 導入 | 同期先に新規導入。関連ファイル一覧のパスを同期先に適応させる |
| 4 | `.claude/skills/session-flow-policy/SKILL.md` | 導入 | 同期先に新規導入。同期先のdispatcher+rolesパターンとの整合を取る |
| 5 | `sessions/initiatives/_template/` | 統一 | 同期先の sessions/_template/ と比較し、番号付きテンプレート構造を統一する |

## 成功基準

1. 統一対象ファイル（#1, #5）の内容が同期元と同期先で整合している（差異許容ポイントを除く）
2. 導入対象ファイル（#2, #3, #4）が同期先に存在し、パス参照が同期先で有効である
3. 同期先の既存ポリシー（CLAUDE.md のリポジトリ境界ポリシー）に違反していない

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 同期先のコミットメッセージ規約との競合 | 中 | 既存の開発フローが混乱する | 差分を比較し、追加のみ行う（既存の定義は削除しない） |
| パス参照の不整合 | 高 | ファイル内リンクが壊れる | 同期後にパス参照を全件確認（evaluator の 5.4 で検証） |
| session-flow-policy が dispatcher パターンと矛盾 | 中 | 二重の標準が生まれる | 同期先の既存パターンを尊重し、補完的な位置づけで導入する |

## ワーカーへの指示

### 同期ワーカー

- チェックリスト参照先: `.claude/skills/repo-sync-checklist/SKILL.md` セクション1〜4
- 同期対象: 上記ファイルリスト #1〜#5 に従う
- 注意事項:
  - 同期先のリポジトリ境界ポリシー（CLAUDE.md）を事前に確認し、違反しないこと
  - パス参照（`sessions/initiatives/` 等）を同期先のディレクトリ構造に合わせて適応させること
  - 既存ファイル（commit-message.md, sessions/_template/）は差分マージ。新規ファイルはコピー後に適応

### 評価ワーカー

- 検証基準: `.claude/skills/repo-sync-checklist/SKILL.md` セクション5（7つの検証観点）
- パラメータ具体値:
  - `{source_repo}`: dev-process-improvement (`/home/nr202/projects/dev-process-improvement/`)
  - `{target_repo}`: ai-driven-dev-patterns (`/home/nr202/projects/ai-driven-dev-patterns/`)
  - `{sync_scope}`: `.claude/rules/commit-message.md`, `.claude/rules/session-start-branch-cleanup.md`, `.claude/skills/rule-change-checklist/SKILL.md`, `.claude/skills/session-flow-policy/SKILL.md`, `sessions/initiatives/_template/`
- 注意事項:
  - 差異許容の判断が妥当かを特に重点的に検証すること（同期先固有の要素を誤って上書きしていないか）
  - パス参照の有効性検証（5.4）では、同期先のディレクトリ構造に適応済みであることを確認

---
**作成者**: sync-manager
**作成日**: 2026-03-08
