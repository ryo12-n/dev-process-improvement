# ワーカー計画: sprint-skill-implementation — Set-1

## 壁打ちフェーズ [2026-03-26 10:00]

### 理解のサマリー
- タスクの目的: sprint-planner / sprint-generator / sprint-evaluator の3つの SKILL.md を作成し、`sessions/sprints/` ディレクトリ構成を整備する施策のファイルレベルタスク分割を行う
- スコープ: 3フェーズ（ディレクトリ整備、SKILL.md 作成、inbox 整理）の全タスクを CREATE/MODIFY/READ アノテーション付きで分割し、並列安全性を検証する
- 完了条件: `08_task_division.md` が作成され、Wave Assignment と Conflict Check Matrix が定義されている

### 前提条件チェック
- [x] 施策計画（02_plan.md）の内容を理解: 理解済み — 3フェーズ構成、成功基準11項目を確認
- [x] 提案書（01_proposal.md）の確認: 確認済み — 背景・目標・スコープ・指摘B/C の対応方針を確認
- [x] 変更対象ファイル群の特定: 特定済み — 下記分析計画サマリ参照

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：計画開始

---

## 分析計画サマリ

### 変更対象ファイル群

**フェーズ1: ディレクトリ構成の整備**
- `templates/sprint_template/` の5ファイル → `sessions/sprints/_template/` に `git mv`
- `sessions/sprints/_archive/.gitkeep` の CREATE
- `sessions/sprints/_template/knowledge.md` の MODIFY（変数名統一 `{{repo}}` → `{{repository_name}}`）

**フェーズ2: SKILL.md 作成**
- `.claude/skills/sprint-planner/SKILL.md` の CREATE（指摘B: 起動パターン明確化、指摘C: 親タスク管理者明記を反映）
- `.claude/skills/sprint-generator/SKILL.md` の CREATE（指摘B: 起動パターン明確化を反映）
- `.claude/skills/sprint-evaluator/SKILL.md` の CREATE（指摘B: 起動パターン明確化を反映）

**フェーズ3: inbox 整理・起票**
- `inbox/sprint-folder-definition.md` の DELETE
- `inbox/sprint-template-variable-unification.md` の DELETE
- `inbox/sprint-commit-message-session-type.md` の CREATE（コミットメッセージ規約への起票）

### 分割方針
- フェーズ1 は `git mv` + ファイル変更のため先行実行が必要（フェーズ2 の SKILL.md がテンプレートパスを参照するため）
- フェーズ2 の3つの SKILL.md は互いに独立しており並列可能
- フェーズ3 は他フェーズに依存しないが、軽量タスクのため1タスクにまとめる
