# 同期事前調査: 2026-03-08

## 同期パラメータ

- 同期元リポジトリ: dev-process-improvement
- 同期先リポジトリ: ai-driven-dev-patterns
- 同期方向: dev-process-improvement → ai-driven-dev-patterns

## 同期元リポジトリの現状（dev-process-improvement）

- [x] `.claude/skills/` の構成: l1-manager/, triage-manager/, sync-manager/, session-flow-policy/, triage-standard-policy/, repo-sync-checklist/, rule-change-checklist/ （各マネージャーに agents/ サブディレクトリあり）
- [x] `.claude/rules/` の構成: commit-message.md, session-start-branch-cleanup.md
- [x] `sessions/` の構成: initiatives/_template/ (00-08), triage/_template/, sync/_template/ (00-08), _archive/
- [x] テンプレートの有無: 3種類のテンプレート（initiative, triage, sync）が整備済み
- [x] 直近の変更（同期に影響しうるもの）:
  - repo-sync-verification-checklist 施策完了（検証チェックリストの7観点を repo-sync-checklist に統合）
  - sync-checklist-skill 施策完了（repo-sync-checklist スキルの正式化）
  - sync-manager スキル新規作成（入力の選択形式化、エージェント定義整備）
  - session-start-branch-cleanup ルール新規作成

## 同期先リポジトリの現状（ai-driven-dev-patterns）

- [x] `.claude/skills/` の構成: dispatcher/, role-format-guide/, triage/ (agents: triage-manager/worker/evaluator), parallel-dev/, claude-directory-guide/, openspec-* (13スキル)
- [x] `.claude/rules/` の構成: commit-message.md, sync.md, design-doc.md (空), code-in-docs.md (空), pr-creation-fallback.md
- [x] `sessions/` の構成: _template/, _archive/ （initiatives/ サブディレクトリなし）
- [x] テンプレートの有無: sessions/_template/ あり（構成は未確認・要比較）
- [x] 直近の変更:
  - dev-process-improvement リポジトリ分離完了（3/7）
  - Claude ディレクトリ構造最適化（常時参照の83%削減）
  - トリアージマネージャーセッション最適化
  - デザインプロセスガイド・知見ルーティングドキュメント作成

## 同期対象の特定

### 同期候補ファイル・ディレクトリ

| # | ファイル/ディレクトリ | 同期元の状態 | 同期先の状態 | 同期判断 |
|---|---------------------|-------------|-------------|---------|
| 1 | `.claude/rules/commit-message.md` | session-type 6種対応、sync系追加済み | 基本形式あり、sync系未対応 | 比較・統一 |
| 2 | `.claude/rules/session-start-branch-cleanup.md` | 6ステップフロー確立済み | 存在しない | 導入候補 |
| 3 | `.claude/skills/session-flow-policy/SKILL.md` | マネージャー=スキル、ワーカー=エージェントの標準パターン定義 | 存在しない（dispatcher パターンで代替） | 導入候補 |
| 4 | `.claude/skills/rule-change-checklist/SKILL.md` | ルール変更時の連動更新チェックリスト | 存在しない | 導入候補 |
| 5 | `.claude/skills/triage-standard-policy/SKILL.md` | ライフサイクル適用マトリクス・ペアリング要件定義 | 存在しない（triage/ に独自実装あり） | 比較・適用検討 |
| 6 | `sessions/initiatives/_template/` | 00-08 の番号付きファイル | sessions/_template/ あり（構成比較必要） | 比較・統一 |
| 7 | `sessions/initiatives/_archive/` | 完了済み施策の移動先 | sessions/_archive/ あり | 構造確認 |

### 同期対象外（理由付き）

| # | ファイル/ディレクトリ | 対象外の理由 |
|---|---------------------|-------------|
| 1 | `.claude/skills/sync-manager/` | 同期管理はdev-process-improvement固有のプロセス。ai-driven-dev-patternsでは不要 |
| 2 | `.claude/skills/repo-sync-checklist/` | 同上。同期チェックリストはdev-process-improvement側の責務 |
| 3 | `.claude/skills/triage-manager/` | ai-driven-dev-patternsに独自のtriage/スキルが既存。構成が異なるため直接同期不可 |
| 4 | `.claude/skills/l1-manager/` | ai-driven-dev-patternsはdispatcher+dev_managerパターン。直接の1:1対応がない |
| 5 | `sessions/triage/`, `sessions/sync/` | dev-process-improvement固有のセッション種別 |
| 6 | `docs/workflow.md` | dev-process-improvement固有のワークフロー可視化。同期先には独自docsあり |
| 7 | セッション成果物（作業ログ等） | チェックリスト セクション4 の規定により同期対象外 |

## 前回同期からの変化

- 前回同期日: 2026-02-27（partial-repo-sync 施策）
- 前回以降の主な変更:
  - sync-manager スキル・エージェント体系の新規構築
  - repo-sync-checklist スキルの正式化（7つの検証観点を含む）
  - session-start-branch-cleanup ルールの新規追加
  - session-flow-policy の確立
  - rule-change-checklist の新規追加
  - triage-standard-policy のライフサイクルマトリクス更新

## 調査サマリ

- 注意点1: ai-driven-dev-patterns は「自己完結型」のリポジトリ境界ポリシーを持つ。同期元から持ち込むファイルが同期先のポリシーに違反しないよう、パス参照やリポジトリ固有の記述を適応させる必要がある
- 注意点2: ai-driven-dev-patterns は dispatcher+roles パターン、dev-process-improvement は l1-manager+agents パターンと、セッション管理の基本アーキテクチャが異なる。「統一すべきポイント」（チェックリスト セクション3）の適用は、パターンの違いを考慮した上で行う必要がある
- 注意点3: 前回同期（partial-repo-sync）以降、dev-process-improvement側で多くの新規ルール・スキルが作成されている。初回導入の要素が多いため、スコープを絞って段階的に進めることを推奨

---
**調査者**: sync-manager
**調査日**: 2026-03-08
