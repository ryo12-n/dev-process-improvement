# ワーカー計画: sprint-skill-implementation — Set-1

## 壁打ちフェーズ [2026-03-26 10:00]

### 理解のサマリー
- タスクの目的: sprint-planner / sprint-generator / sprint-evaluator の3つの SKILL.md を作成し、`sessions/sprints/` のディレクトリ構成を整備する
- スコープ: T-001〜T-008（5施策タスク + 3固定タスク）
- 完了条件: 全タスク完了、worker_report 作成、worker_log 記録、全変更コミット・プッシュ済み
- set 番号: set-1（指定あり）

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（Phase 1 計画完了済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（git mv, git rm, Read, Write, Edit, Bash）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（`templates/sprint_template/` に5ファイル存在、`sessions/sprints/` 未作成）
- [x] set 番号確認: 指定あり: set-1
- [x] set ディレクトリの存在確認: 確認済み（`phase-2-execution/set-1/` 存在）
- [x] 外部リポジトリ成果物の記法スタイル確認: 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. **T-001**: `templates/sprint_template/` → `sessions/sprints/_template/` に git mv、`_archive/.gitkeep` 作成、knowledge.md 変数名統一、参照確認（アーカイブ・inbox は除外）
2. **T-002**: `.claude/skills/sprint-planner/SKILL.md` 作成（指摘B: 起動パターン明確化、指摘C: 親タスク管理責務明記）
3. **T-003**: `.claude/skills/sprint-generator/SKILL.md` 作成（指摘B: 起動パターン明確化）
4. **T-004**: `.claude/skills/sprint-evaluator/SKILL.md` 作成（指摘B: 起動パターン明確化）
5. **T-005**: inbox 2ファイル削除 + コミットメッセージ規約 session-type 追加提案作成
6. **T-006**: 作業中の知見記録（worker_report に記載）
7. **T-007**: rule-change-checklist 全7項目確認
8. **T-008**: 課題転記確認
