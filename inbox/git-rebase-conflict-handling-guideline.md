# rebase コンフリクト時の対応方針ガイドライン

## 気づきの背景

backlog-id-and-issue-template 施策で `git rebase main` 時に backlog.csv のコンフリクトが1件発生した際、コンフリクト解決ではなくブランチを `git branch -D` で削除して main から作り直し、`--force-with-lease` で push した。結果として前回の9コミットの履歴が失われ、reflog からの復元が必要になった。

## 気づき

- **rebase コンフリクトが少数の場合は `git rebase --continue` で解決する方がシンプル**で、履歴も保たれる
- **`git branch -D` + force push は破壊的操作であり最終手段**。reflog から復元可能とはいえ、まず非破壊的な手段（コンフリクト解決 → `--continue`）を試すべき
- **リモートブランチの再取得という選択肢がある**: force push 前であれば `git fetch origin <branch>` で元の状態を取得し、そこから作業を再開できた

## 期待効果

- ブランチ履歴の不要な破壊を防止
- force push の頻度を減らし、協調作業時のリスクを低減
- session-start-branch-cleanup ルールや commit-message ルールとの整合性維持

## 提案

- `.claude/rules/` または既存のガイドラインに「rebase コンフリクト時の対応フロー」を追加検討
  - Step 1: コンフリクト内容を確認（件数・複雑度）
  - Step 2: 少数・単純なら手動解決 → `git rebase --continue`
  - Step 3: 複雑・大量なら `git rebase --abort` → `git merge main` を検討
  - Step 4: ブランチ再作成 + force push は最終手段
