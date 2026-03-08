# 作業履歴: roles/ → .claude/agents/ 移行

## 壁打ちフェーズ [2026-03-08 15:00]

### 理解のサマリー
- タスクの目的: ai-driven-dev-patterns リポジトリの `roles/` ディレクトリを廃止し、Claude Code ネイティブの `.claude/agents/` + `.claude/skills/` + `.claude/rules/` 構成に移行する
- スコープ: T-001〜T-008（共通ルール分離、8ロール変換、dev_manager統合、参照更新、roles/削除、知見記録、連動更新チェック、課題転記）
- 完了条件: 全タスク完了、ai-driven-dev-patterns 側でコミット済み、dev-process-improvement 側で作業ログ・レポート記録済み

### 前提条件チェック
- [x] 依存タスクの完了状態: T-001〜T-005は順序依存あり。それ以外は独立
- [x] 必要ツール・コマンドの利用可否: 確認済み（git, ファイル操作）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
  - ai-driven-dev-patterns: roles/ に9ファイル + _base/common.md が存在
  - .claude/agents/ は未作成（新規作成が必要）
  - .claude/rules/ に既存6ファイルあり
  - .claude/skills/dispatcher/SKILL.md が既存

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. **T-001**: common.md のセクション3〜8を3つのルールファイルに分離。commit-message.md との統合
2. **T-002**: 8つの専門ロールを .claude/agents/*.md に変換（YAML フロントマター付き）
3. **T-003**: dev_manager.md のオーケストレーションロジックを dispatcher SKILL.md に統合
4. **T-004**: roles/ を参照している全ファイル（docs/design/ 除く）のパス更新
5. **T-005**: roles/ ディレクトリを git rm -r で削除
6. **T-006**: 知見を 04_work_report.md に記録
7. **T-007**: ルール変更連動更新チェックリスト実施
8. **T-008**: 07_issues.md の課題転記確認

ai-driven-dev-patterns 側でブランチ `initiative/roles-agents-migration` を作成してから作業開始。

---

## 作業ログ

### [2026-03-08 15:05] タスクID: T-001
**状態**: 完了
**作業内容**:
- `roles/_base/common.md` のセクション3（基本的な作業ループ）、セクション6（完了報告の形式）、セクション7（セッション間引き継ぎプロトコル）+ エラー・ブロック時の対応を `.claude/rules/agent-common-workflow.md` に分離
- セクション4（共通禁止事項）を `.claude/rules/agent-restrictions.md` に分離
- セクション8（worktree 環境での共通ルール）を `.claude/rules/worktree-rules.md` に分離
- セクション5（コミット規約）を既存の `.claude/rules/commit-message.md` に統合（`roles/_base/common.md` への参照を自己完結型に変更）
- セクション1（アーキテクチャ説明）とセクション2（リポジトリ構造）は CLAUDE.md に既にあるため移行不要
**成果物**: `.claude/rules/agent-common-workflow.md`, `.claude/rules/agent-restrictions.md`, `.claude/rules/worktree-rules.md`, `.claude/rules/commit-message.md`（更新）

### [2026-03-08 15:15] タスクID: T-002
**状態**: 完了
**作業内容**:
- 8つの専門ロールを `.claude/agents/*.md` に YAML フロントマター付きで変換
- ファイル名は `_` を `-` に変換（Claude Code agents のケバブケース命名規則に準拠）
- 各ファイルに `name`, `description`, `tools`, `model` フロントマターを付与
- `tools:` フィールドで reviewer は Read, Grep, Glob, Bash のみに制限（Write/Edit なし）
- `common.md` への参照（「作業開始前に common.md を読んでください」）を削除
- ロール定義の内容・ロジックは変更なし（フォーマット変換のみ）
**成果物**: `.claude/agents/feature-builder.md`, `test-writer.md`, `reviewer.md`, `bug-fixer.md`, `refactorer.md`, `optimizer.md`, `documentarian.md`, `openspec-specialist.md`

### [2026-03-08 15:25] タスクID: T-003
**状態**: 完了
**作業内容**:
- `roles/dev_manager.md` のオーケストレーションロジックを `.claude/skills/dispatcher/SKILL.md` に統合
- 既存の dispatcher 機能（シナリオ判定・分類フロー・セッション型レジストリ）を「パート1: シナリオ分類」として維持
- dev_manager の機能（セッション管理、ロール起動、並列起動、フェーズゲート判定、知見収集、課題管理）を「パート2: オーケストレーション」として追加
- ロール起動の参照先を `.claude/agents/` に変更
- description を更新して統合後の役割を反映
**成果物**: `.claude/skills/dispatcher/SKILL.md`（更新）

### [2026-03-08 15:35] タスクID: T-004
**状態**: 完了
**作業内容**:
- `grep -r 'roles/' --include='*.md'` で残存参照を検出（docs/design/ を除く約40ファイル）
- 主な置換パターン:
  - `roles/<role>.md` → `.claude/agents/<role>.md`（ケバブケースに変換）
  - `roles/_base/common.md` → `.claude/rules/` の適切なファイル名
  - `roles/dev_manager.md` → `.claude/skills/dispatcher/SKILL.md`
  - `roles/` → `.claude/agents/`（ディレクトリ参照）
  - `roles/*.md` → `.claude/agents/*.md`
- 更新対象: CLAUDE.md, README.md, docs/, .claude/skills/, .claude/rules/, sessions/, triage/, backlog/, inbox/
- 更新後、`grep -r 'roles/' --include='*.md'` で docs/design/ 以外にヒットなしを確認
**成果物**: 約40ファイルのパス更新

### [2026-03-08 15:40] タスクID: T-005
**状態**: 完了
**作業内容**:
- T-001〜T-004 の完了を確認
- `git rm -r roles/` で roles/ ディレクトリを削除（10ファイル）
**成果物**: roles/ ディレクトリ削除

### [2026-03-08 15:45] タスクID: T-007
**状態**: 完了
**作業内容**:
ルール変更連動更新チェックリスト（rule-change-checklist スキル）を実施。

**1. 関連ファイル一覧の確認**:
- [x] 変更ファイルの「関連ファイル一覧」セクションを確認した
  - commit-message.md: 関連ファイル一覧なし（独立）
  - dispatcher SKILL.md: 関連ファイル一覧に記載のファイルは全て更新済み
  - rule-change-checklist SKILL.md: 関連ファイル一覧の参照パスを更新済み
- [x] 一覧に記載された各ファイルについて、連動更新の要否を判断した
- [x] 連動更新が必要なファイルを更新した

**2. docs/ の更新**:
- [x] 変更内容が `docs/` のどのドキュメントに影響するかを特定した
  - docs/design-process-guide.md: ロール参照パス更新済み
  - docs/session-guide.md: ロール参照パス更新済み
  - docs/git-worktree-guideline.md: ロール参照パス更新済み
  - docs/design/ 配下: 歴史的設計書として保持（更新不要）
- [x] 該当するドキュメントを更新した
- [x] 更新後のドキュメントが変更後のルールと整合していることを確認した

**3. 品質基準ポリシーの連動更新**:
- [x] 変更内容が品質基準に影響するか確認した → 該当なし（ファイル配置変更のみで品質ゲート基準は変更なし）

**4. テンプレートの連動更新**:
- [x] `sessions/_template/report.md`: roles/ 参照を .claude/agents/ に更新済み
- [x] `sessions/initiatives/_template/04_work_report.md`: 更新済み
- [x] `sessions/initiatives/_template/06_eval_report.md`: 更新済み

**5. コミットメッセージ規約の確認**:
- [x] `.claude/rules/commit-message.md`: scope の `roles` を `agents` に更新済み。新セッション種別の追加は不要

