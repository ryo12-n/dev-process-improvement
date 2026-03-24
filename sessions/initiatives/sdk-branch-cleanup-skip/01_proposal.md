# 改善施策提案: sdk-branch-cleanup-skip

## 背景・課題

SessionStart hook（`.claude/hooks/session-start-branch-cleanup.sh`）は前セッションの残留ブランチを整理するために設計されている。しかし SDK 環境（Claude Code Web）では:

1. `claude/<session-type>-<id>` ブランチが事前に割り当てられる
2. hook がこのブランチを main に戻そうとすると、割り当て済みブランチから離脱する
3. PR 作成も SDK のブランチ管理と競合する

## 目標

SDK 環境で SessionStart hook のブランチ整理をスキップし、割り当て済みブランチを維持する。

## スコープ
### やること
- `.claude/hooks/session-start-branch-cleanup.sh` に SDK 環境判定を追加
- `.claude/rules/session-start-branch-cleanup.md` に SDK スキップ仕様を追記

### やらないこと
- l1-manager SKILL.md の変更（hook 側で完結）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

SDK 環境でのセッション開始時の不要なブランチ操作が排除され、安定してセッションを開始できる。

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| `claude/` で始まる手動ブランチの誤判定 | 低 | 運用上 `claude/` プレフィックスは SDK 専用のため問題なし |

## 壁打ちの背景

SDK 環境では `claude/` プレフィックスのブランチが事前割り当てされる制約がある（ISS-027 関連）。ブランチ名で判定する方式はシンプルかつ確実。

---
**起票者**: L1
**起票日**: 2026-03-24
**ステータス**: 実施中
**backlog元ファイル**: なし（セッション中の新規提案）
