# L1 タスク作成時のスキルファイル網羅確認ステップ追加

## 背景

sessionstart-hook-branch-cleanup 施策の T-003 で、タスクリストに6つのマネージャースキルを列挙したが、automation-manager が漏れていた。L2-worker が自律的に発見して対応したが、常に検出できるとは限らない。

## 提案

L1 マネージャーが `02_tasks.md` で対象スキルファイルを列挙する際、`grep -r` 等で関連セクションを持つファイルを網羅的に検索するステップを L1 のタスク作成ガイドに追加する。

## 発見元

- 施策: `sessions/initiatives/sessionstart-hook-branch-cleanup/`
- worker 知見 #1、evaluator 知見 #1

---
**起票日**: 2026-03-13
