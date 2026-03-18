# スキャン計画: Set-1

## 壁打ちフェーズ [2026-03-18]

### 理解のサマリー
- タスクの目的: 前回（20260316）以降に追加・変更された skills/rules を走査し新規自動化候補を検出する（AT-001）。既存16候補の再評価を実施する（AT-002）
- スコープ: .claude/skills/ の新規追加（session-consistency-manager, manager-overview）、大幅更新（triage-manager, l1-manager, l1-impl-manager）、リネーム（session-lifecycle-policy）、rules 変更（commit-message.md, gha-workflow-security.md, parallel-dev.md）。既存 AC-001〜AC-016 全件
- 完了条件: 新規候補が一覧化され、全16候補の再評価が変更提案テーブルとして整理されている

### 前提条件チェック
- [x] 割り当て AT タスクの内容を理解: 理解済み
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み

### 不明点・確認事項
なし

### 壁打ちフェーズ結果
確認事項なし：実施開始

---

## スキャン計画

### 走査対象
- `.claude/skills/session-consistency-manager/SKILL.md` + agents 4ファイル + reference（新規追加）
- `.claude/skills/manager-overview/SKILL.md`（新規追加）
- `.claude/skills/triage-manager/SKILL.md`（大幅更新: 112行追加、フェーズゲート構造・TG-010 等）
- `.claude/skills/l1-manager/SKILL.md`（大幅更新: enhanced-planning 関連）
- `.claude/skills/l1-impl-manager/SKILL.md`（大幅更新: refs-knowledge-read 関連）
- `.claude/skills/session-lifecycle-policy/SKILL.md`（リネーム: triage-standard-policy → session-lifecycle-policy、sc ロール追加）
- `.claude/skills/manager-common-policy/SKILL.md`（§1 適用対象に session-consistency-manager 追加、§10 ドメインエージェント参照追加）
- `.claude/rules/commit-message.md`（sc-mgr/sc-worker/sc-eval 追加）
- `.claude/rules/gha-workflow-security.md`（ユーザー入力エスケープルール追加）
- `.claude/rules/parallel-dev.md`（worktree escalation パス追加）
- `automation-candidates/entries/AC-001.md` 〜 `AC-016.md`（全件再評価）
- `backlog/entries/PreToolUse-hookコミットメッセージバリデーション.md`（BL-029 状況確認）
- `backlog/entries/PostToolUse-hookルール変更連動チェック.md`（BL-030 状況確認）

### 走査順序
1. AT-001: 新規・変更 skills/rules を1つずつ走査し、定型作業パターンを検出する
2. AT-001: 既存候補 AC-001〜AC-016 との重複チェック
3. AT-002: BL-029（AC-002）・BL-030（AC-012）の施策化状況を確認する
4. AT-002: 新規スキル追加・変更による既存候補への影響を評価する
5. AT-002: 全16候補の変更提案を整理する

### 判断基準
- 新規候補: 定型的（手順が固定的）・反復的（複数回発生）・ミスしやすい（手動だとエラーが起きやすい）の3条件で検出
- 再評価: 環境変化（新規スキル追加・backlog 施策化状況・運用経験）による優先度スコア・実装難易度・自動化手段の変更が必要か
- 重複除外: 既存 AC-001〜AC-016 のスコープと重複する作業は新規候補としない

---
**作成者**: オートメーションワーカー
**作成日**: 2026-03-18
