# GHA コメント投稿の `--body-file` パターン全面統一

## 種別
次施策候補

## 内容
close.yml のクローズサマリーと backlog-to-issue.yml の scheduled-create ジョブが `--body` パターンのまま残っている。実害はないが一貫性の観点から `--body-file` パターンへの統一を検討する。

## 対象ファイル
- `.github/workflows/initiative-close.yml`: クローズサマリーコメント
- `.github/workflows/backlog-to-issue.yml`: scheduled-create ジョブの Issue 作成

## 背景
gha-workflow-ux-improvements 施策で wallbash/execute/backlog-to-issue(create-issue) の3ファイルは `--body-file` パターンに変換済み。上記2箇所はスコープ外として残した。

## 発見元
sessions/initiatives/gha-workflow-ux-improvements/ (L2-evaluator)

---
**作成日**: 2026-03-19
