# タスクリスト: sprint-skill-implementation

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-008 | 逐次ディスパッチ |
| L2-evaluator | 全タスクの成果物評価 | worker 完了後に起動 |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-008 | Wave 1 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | 5施策タスク + 3固定タスク |

> **方式**: 逐次（1ワーカーずつ）

---

## タスク一覧

### T-001: ディレクトリ構成の整備（git mv + アーカイブ作成 + 変数名統一）
- **やること**:
  1. `templates/sprint_template/` の5ファイル（plan.md, todo.md, work_log.md, review.md, knowledge.md）を `sessions/sprints/_template/` に `git mv` で移動する
  2. `sessions/sprints/_archive/.gitkeep` を作成する
  3. `sessions/sprints/_template/knowledge.md` 内の変数名を統一する（行41付近の `{{repo}}` → `{{repository_name}}`）
  4. 移動前に `grep -r "sprint_template"` で既存参照箇所を確認し、アクティブファイル（アーカイブ済み施策内・inbox 実施計画書は除外）に参照があれば更新する
- **完了条件**:
  - `sessions/sprints/_template/` に5ファイルが存在する
  - `sessions/sprints/_archive/` ディレクトリが存在する（`.gitkeep` あり）
  - `templates/sprint_template/` が削除されている（`git mv` による移動済み）
  - `sessions/sprints/_template/knowledge.md` 内の `{{repo}}` が `{{repository_name}}` に統一されている
- **優先度**: 🔴
- **ステータス**: ⬜

### T-002: sprint-planner SKILL.md の作成
- **やること**:
  1. `.claude/skills/sprint-planner/SKILL.md` を作成する
  2. 内容は `inbox/sprint-skill-implementation 実施計画書.md` の「sprint-planner SKILL.md 仕様」セクションを基にする
  3. **指摘B 対応**: 起動パターンセクションに、各パターンの具体的なユーザー発話例を追加し、他ロール（generator / evaluator）との区別を明確にする。例: 「新規スプリント作成は planner のみが担う」「再開時は planner を `/sprint-planner` で起動」等
  4. **指摘C 対応**: 「フォルダ状態に応じた分岐」セクションの「全タスク done」行に、「親タスク（T-XXX）のステータスを done に更新」が planner の責務である旨を明記する
- **完了条件**:
  - `.claude/skills/sprint-planner/SKILL.md` が存在する
  - フロントマター（name / description / user-invocable）が記載されている
  - 起動パターン2つ（new / 再開）が記載され、他ロールとの区別が明確である
  - 「フォルダ状態に応じた分岐」に親タスク管理が planner の責務として明記されている
  - TodoWrite 登録例、壁打ちルール、担当ファイルテーブル、やらないことが記載されている
- **優先度**: 🔴
- **ステータス**: ⬜

### T-003: sprint-generator SKILL.md の作成
- **やること**:
  1. `.claude/skills/sprint-generator/SKILL.md` を作成する
  2. 内容は `inbox/sprint-skill-implementation 実施計画書.md` の「sprint-generator SKILL.md 仕様」セクションを基にする
  3. **指摘B 対応**: 起動パターンセクションに、generator として起動する場合のユーザー発話例を追加し、他ロールとの区別を明確にする。例: 「タスクを実行する場合は `/sprint-generator` で起動」等
- **完了条件**:
  - `.claude/skills/sprint-generator/SKILL.md` が存在する
  - フロントマターが記載されている
  - 起動パターンが記載され、generator 固有の起動文脈が明確化されている
  - タスク選択ルール（自律判断・一括提示・承認後自走）が記載されている
  - work_log.md 記録ルール・DEVIATION フォーマットが記載されている
  - todo.md 更新ルールテーブル、担当ファイルテーブル、やらないことが記載されている
- **優先度**: 🔴
- **ステータス**: ⬜

### T-004: sprint-evaluator SKILL.md の作成
- **やること**:
  1. `.claude/skills/sprint-evaluator/SKILL.md` を作成する
  2. 内容は `inbox/sprint-skill-implementation 実施計画書.md` の「sprint-evaluator SKILL.md 仕様」セクションを基にする
  3. **指摘B 対応**: 起動パターンセクションに、evaluator として起動する場合のユーザー発話例を追加し、他ロールとの区別を明確にする。例: 「レビューする場合は `/sprint-evaluator` で起動」等
- **完了条件**:
  - `.claude/skills/sprint-evaluator/SKILL.md` が存在する
  - フロントマターが記載されている
  - 起動パターンが記載され、evaluator 固有の起動文脈が明確化されている
  - レビュー基準（3値判定: ✅/❌/⚠️）が記載されている
  - review.md 記録ルール（Round 追記・IMP 連番）、次アクションガイド出力が記載されている
  - 担当ファイルテーブル、やらないことが記載されている
- **優先度**: 🔴
- **ステータス**: ⬜

### T-005: inbox 整理・コミットメッセージ規約起票
- **やること**:
  1. `inbox/sprint-folder-definition.md` を `git rm` で削除する（本施策でカバー済み）
  2. `inbox/sprint-template-variable-unification.md` を `git rm` で削除する（T-001 でカバー済み）
  3. `inbox/sprint-commit-message-session-type.md` を作成し、コミットメッセージ規約（`.claude/rules/commit-message.md`）に sprint-planner / sprint-generator / sprint-evaluator の3ロールに対応する session-type の追加提案を記載する
- **完了条件**:
  - `inbox/sprint-folder-definition.md` が削除されている
  - `inbox/sprint-template-variable-unification.md` が削除されている
  - `inbox/sprint-commit-message-session-type.md` が作成されており、3ロールの session-type 追加提案が記載されている
- **優先度**: 🟡
- **ステータス**: ⬜

---

## 固定タスク（実施ワーカー向け）

### T-006: 作業中の知見記録
- **やること**: 作業中に発見した知見を `phase-2-execution/set-1/03_worker_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載）
- **完了条件**: 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある
- **優先度**: 🔴
- **ステータス**: ⬜

### T-007: ルール変更チェックリスト確認
- **やること**: `rule-change-checklist` スキル（`.claude/skills/rule-change-checklist/SKILL.md`）のチェックリスト全7項目を確認する。本施策は `.claude/skills/` 配下に新規ファイルを作成するため、パス変更走査対象の網羅性・deny リスト対称性・テンプレート連動更新・コミットメッセージ規約確認を特に確認すること
- **完了条件**: チェックリストの全7項目（確認済み / 修正済み / 該当なし）の結果が `phase-2-execution/set-1/02_worker_log.md` に記録されている
- **優先度**: 🔴
- **ステータス**: ⬜
- **適用対象環境**: CLI / SDK 横断

### T-008: 課題転記確認
- **やること**: `phase-2-execution/set-1/07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` として作成する（CSV は自動生成）。転記時は `issues/_template.md` をコピーして作成する
- **完了条件**: 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている
- **優先度**: 🔴
- **ステータス**: ⬜

---
**作成者**: L1
**最終更新**: 2026-03-26
