# GHA prompt フィールドのシェル展開不可に関する注意事項追加

## 概要
GHA の `anthropics/claude-code-action` の `prompt:` 入力フィールドではシェルコマンド置換 `$(...)` が展開されない。`${{ }}` 式のみが評価される。

## 背景
`gha-initiative-workflow` 施策で `$(cat /tmp/issue_body.txt)` がリテラル文字列として Claude に渡される問題が発生。評価レポートで指摘され、修正済み。

## 提案
- `gha-guideline` SKILL.md の §4（gh コマンド前提条件チェックリスト）または新セクションに、`prompt:` フィールドの制限事項として追記する
- 同様に `issue_comment` トリガーが PR コメントでも発火する点も gha-guideline に追記する

## 元施策
`sessions/initiatives/gha-initiative-workflow/08_gate_review.md` 必須把握事項 #1, #2
