# 実施計画: 2つのリポジトリの部分的同期

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | dev-process-improvement 側の構成変更（ディレクトリ移動・テンプレート改善・パス更新） | sessions/ 配下にディレクトリが移動され、全参照が更新されている |
| 2 | ai-driven-dev-patterns 同期準備（チェックリスト作成） | 同期チェックリストが作成され、差異が整理されている |

## フェーズ1: dev-process-improvement 側の構成変更

### 1-1. sessions/ ディレクトリ導入とディレクトリ移動
- `sessions/triage/` と `sessions/initiatives/` を作成
- 既存の `triage/` → `sessions/triage/`、`initiatives/` → `sessions/initiatives/` を `git mv` で移動
- `sessions/triage/_archive/` を新規作成

### 1-2. テンプレートコピー改善
- triage-manager スキル定義のコピー手順を変更
- セッション作成時: `triage/_template/` の直下ファイル（00〜04）のみコピーし、`workers/` ディレクトリは空で作成する
- ワーカーセット作成時: リポジトリの `_template/workers/_template/` から直接 `workers/set-N/` にコピーする

### 1-3. 参照パスの一括更新

影響ファイル一覧（事前調査で特定済み）:

**`.claude/` 配下（9ファイル）**:
- `.claude/skills/l1-manager/SKILL.md`
- `.claude/skills/l1-manager/agents/l2-worker.md`
- `.claude/skills/l1-manager/agents/l2-evaluator.md`
- `.claude/skills/triage-manager/SKILL.md`
- `.claude/skills/triage-manager/agents/triage-worker.md`
- `.claude/skills/triage-manager/agents/triage-evaluator.md`
- `.claude/skills/rule-change-checklist/SKILL.md`
- `.claude/rules/commit-message.md`
- `.claude/rules/session-start-branch-cleanup.md`

**`docs/` 配下（5ファイル）**:
- `docs/workflow.md`
- `docs/management-system-guide.md`
- `docs/implementation.md`
- `docs/coordination-protocol-guideline.md`
- `docs/git-worktree-guideline.md`

**ルート**:
- `CLAUDE.md`

## フェーズ2: ai-driven-dev-patterns 同期準備

### 2-1. 同期チェックリスト作成
- dev-process-improvement の sessions/ 構成を基に、ai-driven-dev-patterns に導入すべき要素を一覧化
- 差異が許容されるポイントと統一すべきポイントを明記

## 成功基準（全体）

1. `sessions/triage/` と `sessions/initiatives/` にディレクトリが移動され、旧パスが存在しない
2. triage セッション作成時に `workers/_template/` がセッションフォルダ内に生成されない
3. 全スキル定義・ルールファイル・ドキュメントのパス参照が新パスに更新されている
4. ai-driven-dev-patterns への同期チェックリストが作成されている

## リソース・前提条件

- 本施策完了後に「リポジトリ間テンプレート同期の検証チェックリスト」施策が後続する可能性がある

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| パス参照の更新漏れ | 中 | 高 | grep で旧パスを網羅的に検索し、漏れを検証する |
| git mv による履歴分断 | 低 | 中 | ディレクトリ単位で git mv し、コミットメッセージに移動元を明記 |

---
**作成者**: L1
**作成日**: 2026-03-08
**最終更新**: 2026-03-08
