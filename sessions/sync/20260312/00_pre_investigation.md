# 同期事前調査: 2026-03-12

## 同期パラメータ

- 同期元リポジトリ: dev-process-improvement (`/home/nr202/projects2/dev-process-improvement/`)
- 同期先リポジトリ: ai-driven-dev-patterns (`/home/nr202/projects2/ai-driven-dev-patterns/`)
- 同期方向: dev-process-improvement → ai-driven-dev-patterns

## 同期元リポジトリの現状

- [x] `.claude/skills/` の構成: 15スキル（l1-manager, triage-manager, sync-manager, metacognition-manager, backlog-maintenance-manager, repo-sync-checklist, manager-common-policy, session-flow-policy, triage-standard-policy, rule-change-checklist, format-conversion-checklist, builtin-skills-reference, external-repo-cleanup, fork-sync, parallel-dev は無し）。5マネージャーに各2エージェント（worker/evaluator）
- [x] `.claude/rules/` の構成: 3ファイル（commit-message.md, session-start-branch-cleanup.md, pr-url-output.md）
- [x] `sessions/` の構成: initiatives/, triage/, metacognition/, sync/ の4種
- [x] テンプレートの有無: sessions/initiatives/_template/, sessions/sync/_template/ 等
- [x] 直近の変更（同期に影響しうるもの）:
  - backlog-maintenance セッションタイプ新設（commit-message.md に bm-* 追加）
  - external-repo-cleanup スキル新設
  - format-conversion-checklist スキル新設
  - builtin-skills-reference スキル新設
  - session-start-branch-cleanup: gh -C → cd && gh 修正（ISS-051）
  - rule-change-checklist: deny リストチェック項目追加、パス走査対象拡充
  - session-flow-policy: ペアリング対称性テーブル詳細化（6要件）
  - manager-common-policy: §8 セッションライフサイクル todo 登録を新設

## 同期先リポジトリの現状

- [x] `.claude/skills/` の構成: 18スキル（dispatcher, 10個のopenspec系, parallel-dev, claude-directory-guide, role-format-guide, triage, rule-change-checklist, session-flow-policy）。triage/ 内に manager/worker/evaluator
- [x] `.claude/rules/` の構成: 4ファイル（agent-common-workflow.md, agent-restrictions.md, commit-message.md, pr-creation-fallback.md）
- [x] `sessions/` の構成: initiatives/, triage/ 等
- [x] テンプレートの有無: sessions/_template/, sessions/initiatives/_template/
- [x] 直近の変更:
  - claude-dir-optimization-adp: rules/ → skills/ へファイル移動（session-start-branch-cleanup → dispatcher/内へ）
  - roles/ → .claude/agents/ 移行
  - triage-process-brushup: 3ロール分割に移行

## 同期対象の特定

### 同期候補ファイル・ディレクトリ

| # | ファイル/ディレクトリ | 同期元の状態 | 同期先の状態 | 同期判断 |
|---|---------------------|-------------|-------------|---------|
| 1 | `.claude/rules/commit-message.md` | bm-* セッション種別追加済み | Conventional Commits ベースの独自規約 | **対象外**: パラダイムが異なる（施策管理 vs コード開発）。強制統一は両方のワークフローを壊す |
| 2 | `.claude/skills/rule-change-checklist/SKILL.md` | deny リストチェック追加、パス走査対象拡充 | 前回同期後に適応済み版あり | **差分参照**: ソースの更新内容を参照し、ターゲットに適用可能な改善を個別判断 |
| 3 | `.claude/skills/session-flow-policy/SKILL.md` | ペアリング対称性テーブル6要件に詳細化 | 独自アーキテクチャ（dispatcher→specialist）に適応済み | **差分参照**: ペアリング対称性の改善を参照し、ターゲット版に反映可能か判断 |
| 4 | `.claude/rules/session-start-branch-cleanup.md` → `.claude/skills/dispatcher/session-start-branch-cleanup.md` | ISS-051 修正（gh -C → cd && gh） | dispatcher/ 内に移動済み | **同期**: バグ修正（ISS-051）を反映。ファイル配置はターゲットの dispatcher/ 内を維持 |
| 5 | `.claude/skills/external-repo-cleanup/SKILL.md` | 新設（2026-03-10） | 存在しない | **検討**: ターゲットでの外部リポジトリ整理ニーズを確認して判断 |
| 6 | `.claude/skills/format-conversion-checklist/SKILL.md` | 新設（2026-03-10） | 存在しない | **検討**: ターゲットでのフォーマット変換タスクの有無を確認して判断 |
| 7 | `.claude/skills/builtin-skills-reference/SKILL.md` | 新設（2026-03-12） | 存在しない | **対象外**: 評価結果はリポジトリ固有（Markdown vs コード）。ターゲットでは独自評価が必要 |
| 8 | `.claude/rules/pr-url-output.md` | 存在（2026-03-08〜） | 存在しない | **同期**: 汎用ルール。前回同期で未同期だった可能性 |

### 同期対象外（理由付き）

| # | ファイル/ディレクトリ | 対象外の理由 |
|---|---------------------|-------------|
| 1 | `.claude/skills/manager-common-policy/` | dev-process-improvement 固有のマネージャーパターン。ターゲットは dispatcher モデル |
| 2 | `.claude/skills/triage-standard-policy/` | dev-process-improvement 固有のトリアージ基準。ターゲットは独自トリアージ |
| 3 | `.claude/skills/l1-manager/`, `triage-manager/`, `sync-manager/`, `metacognition-manager/`, `backlog-maintenance-manager/` | dev-process-improvement 固有のセッション管理。ターゲットは dispatcher が担当 |
| 4 | `.claude/skills/fork-sync/` | fork 同期設定。リポジトリ固有 |
| 5 | `.claude/skills/builtin-skills-reference/` | 評価結果がリポジトリコンテキスト依存 |

## 前回同期からの変化

- 前回同期日: 2026-03-08
- 前回の同期対象: commit-message.md（統一）、session-start-branch-cleanup.md（導入）、rule-change-checklist（導入）、session-flow-policy（導入）、sessions/initiatives/_template/（統一）
- 前回以降の主な変更:
  - **ソース側**: backlog-maintenance 新設、external-repo-cleanup 新設、format-conversion-checklist 新設、builtin-skills-reference 新設、ISS-051 修正
  - **ターゲット側**: claude-dir-optimization-adp（rules/→skills/ 移動）、roles/→.claude/agents/ 移行、triage-process-brushup（3ロール分割）

## 調査サマリ

- 注意点1: 両リポジトリのアーキテクチャが前回同期時より分岐が進んでいる（ソース: マネージャー5種+共通ポリシー体制、ターゲット: dispatcher+specialist体制）。機械的なファイルコピーではなく、差分参照＋個別適応が必要
- 注意点2: ターゲット側で claude-dir-optimization-adp により rules/ → skills/ のファイル移動が行われたため、ソースの rules/ にあるファイルをターゲットに同期する際は配置先の確認が必要
- 注意点3: ISS-051 のバグ修正（gh -C → cd && gh）は実用上重要な修正であり、確実に同期すべき
- 注意点4: pr-url-output.md は前回同期で漏れた可能性がある汎用ルール。ターゲットにも適用可能

---
**調査者**: sync-manager
**調査日**: 2026-03-12
