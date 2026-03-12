# 同期計画: 2026-03-12

<!-- 00_pre_investigation.md の結果を受けて作成 -->

## 同期パラメータ

- 同期元（{source_repo}）: dev-process-improvement (`/home/nr202/projects2/dev-process-improvement/`)
- 同期先（{target_repo}）: ai-driven-dev-patterns (`/home/nr202/projects2/ai-driven-dev-patterns/`)
- 同期方向: dev-process-improvement → ai-driven-dev-patterns
- 同期スコープ（{sync_scope}）: `.claude/rules/`, `.claude/skills/`（直接同期＋差分適応＋概念移植）

## 同期対象ファイルリスト

### A. 直接同期（ファイルレベルの反映）

| # | ファイル/ディレクトリ | 同期方針 | 備考 |
|---|---------------------|---------|------|
| A-1 | `.claude/rules/session-start-branch-cleanup.md` → `.claude/skills/dispatcher/session-start-branch-cleanup.md` | バグ修正反映 | ISS-051（`gh -C` → `cd && gh`）。配置は dispatcher/ 内を維持 |
| A-2 | `.claude/rules/pr-url-output.md` → `.claude/rules/pr-url-output.md` | 新規導入 | 汎用ルール。適応不要 |

### B. 差分参照＋適応反映

| # | ソース | ターゲット | 反映内容 |
|---|--------|----------|---------|
| B-1 | `.claude/rules/commit-message.md` | `.claude/rules/commit-message.md` | (1) triage→triage-mgr/worker/eval 3分割 (2) 禁止事項に session-type・category 必須追加 (3) メタデータフッター追加 |
| B-2 | `.claude/skills/rule-change-checklist/SKILL.md` | `.claude/skills/rule-change-checklist/SKILL.md` | deny リストチェック追加、パス走査対象拡充をターゲットコンテキストに適応 |
| B-3 | `.claude/skills/session-flow-policy/SKILL.md` | `.claude/skills/session-flow-policy/SKILL.md` | ペアリング対称性テーブルの6要件化を適応反映 |

### C. 概念移植（manager-common-policy → dispatcher）

| # | ソースの概念 | ターゲットの反映先 | 反映内容 |
|---|------------|------------------|---------|
| C-1 | §2.1 ディスパッチ4項目 | `dispatcher/SKILL.md` | ロール起動時の必須4項目チェックリスト追加 |
| C-2 | §3 成果物品質ゲート | `dispatcher/SKILL.md` | reviewer 起動前の3点確認追加 |
| C-3 | §5.2 知見ルーティング | `dispatcher/SKILL.md` | 4択マトリクス（CSV/backlog/inbox/none）追加 |
| C-4 | §6 課題CSV転記 | `dispatcher/SKILL.md` | セッション内 vs 横断の分類＋マーキング追加 |
| C-5 | §8 ライフサイクル todo | `dispatcher/SKILL.md` | TaskCreate による進捗追跡パターン追加 |

### D. 概念移植（triage-standard-policy → triage/）

| # | ソースの概念 | ターゲットの反映先 | 反映内容 |
|---|------------|------------------|---------|
| D-1 | ペアリング対称性 | `triage/triage-evaluator.md` | 知見セクション構造化（2テーブル形式 + 最低要件） |
| D-2 | 成果物確認チェックリスト | `triage/triage-manager.md` | 3点確認追加 |
| D-3 | 知見記録完全性 | `triage/triage-worker.md` | 最低1件の知見記録要件明示 |

### E. 対象外（理由付き）

| 対象 | 理由 |
|------|------|
| manager-common-policy 全体 | L1/L2 固有。C-1〜C-5 で概念のみ移植 |
| triage-standard-policy 全体 | dev-process-improvement 固有。D-1〜D-3 で概念のみ移植 |
| l1/triage/sync/meta/bm-manager | dev-process-improvement 固有のセッション管理 |
| builtin-skills-reference | 評価結果がリポジトリコンテキスト依存 |
| external-repo-cleanup | ターゲットは外部リポジトリ施策を持たない |
| format-conversion-checklist | ターゲットに現時点でフォーマット変換タスクなし |
| fork-sync | リポジトリ固有設定 |

## 成功基準

1. A-1: ISS-051 修正がターゲットの dispatcher/session-start-branch-cleanup.md に反映されている
2. A-2: pr-url-output.md がターゲットの .claude/rules/ に存在する
3. B-1〜B-3: ソースの差分がターゲットのコンテキストに適応された形で反映されている
4. C-1〜C-5: dispatcher/SKILL.md に概念移植セクションが追加されている
5. D-1〜D-3: triage/ 内の各ファイルに改善が反映されている
6. 全ファイルのパス参照がターゲットのディレクトリ構造で有効である

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 概念移植がターゲットの既存構造と矛盾 | 中 | セクション番号の衝突・二重定義 | worker に「追記のみ、既存セクション番号を尊重」を指示 |
| dispatcher/SKILL.md が肥大化 | 中 | 可読性低下 | サブセクション粒度で収まるか確認。過大なら別ファイルに分離 |
| commit-message.md の triage 3分割が既存履歴と不整合 | 低 | 混乱 | 既存の `triage` タイプは残し追加のみ（後方互換） |

## ワーカーへの指示

### 同期ワーカー

- チェックリスト参照先: `.claude/skills/repo-sync-checklist/SKILL.md` セクション1〜4
- 同期対象: 上記 A-1〜A-2, B-1〜B-3, C-1〜C-5, D-1〜D-3 に従う
- 注意事項:
  - ターゲットの既存構造を尊重し、追記ベースで概念移植する
  - L1/L2 用語をターゲットの用語（dev_manager/specialist role）に置換する
  - パス参照はターゲットのディレクトリ構造に合わせて適応する
  - commit-message.md の triage 3分割は既存の `triage` タイプを削除せず追加する（後方互換）

### 評価ワーカー

- 検証基準: `.claude/skills/repo-sync-checklist/SKILL.md` セクション5（7つの検証観点）
- パラメータ具体値:
  - `{source_repo}`: dev-process-improvement (`/home/nr202/projects2/dev-process-improvement/`)
  - `{target_repo}`: ai-driven-dev-patterns (`/home/nr202/projects2/ai-driven-dev-patterns/`)
  - `{sync_scope}`: A-1〜D-3 の全対象ファイル（9ファイル）
- 注意事項:
  - 概念移植の適応品質を重点検証（L1/L2 用語残存、パス参照不整合）
  - dispatcher/SKILL.md の肥大化度合いを評価
  - commit-message.md の後方互換性を確認

---
**作成者**: sync-manager
**作成日**: 2026-03-12
