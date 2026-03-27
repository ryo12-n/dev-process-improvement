# SDK 環境でのサブエージェント Write/Bash 権限制約

## 背景
sprint-skill-implementation 施策で L2 サブエージェント（Agent ツール経由）が Write/Bash ツールの権限を取得できず、3回連続でブロックされた。L1 が直接タスクを実行するフォールバックで対応した。

## 提案
- `docs/subagent-permission-guide.md` に SDK 環境でのサブエージェント権限制約を追記する
- または、L1 マネージャーの SKILL.md に「SDK 環境では L2 権限問題発生時に L1 直接実行にフォールバック可」のルールを追加する

## 発見元
sprint-skill-implementation 施策 phase-2-execution（L2-worker 3回ブロック）

---
**起票日**: 2026-03-27
