# rebase コンフリクト時の対応フロー

`git rebase` でコンフリクトが発生した場合、以下のステップで対応する。

## 対応フロー

1. **コンフリクト内容を確認**: 件数・複雑度を把握する
2. **少数・単純な場合**: 手動解決 → `git rebase --continue`
3. **複雑・大量な場合**: `git rebase --abort` → `git merge main` を検討
4. **ブランチ再作成 + force push は最終手段**: reflog からの復元が必要になるリスクがある

## 禁止事項

- コンフリクト解決の代替として `git branch -D` + force push を安易に使用しない
- force push 前にリモートブランチの状態を必ず確認する（`git fetch origin <branch>`）

---
**作成日**: 2026-03-15
**起票元**: backlog-id-and-issue-template 施策の知見
