# GHA環境でのマルチリポジトリアクセス方法（git clone 経由）

## 気づき

ISS-027（SDK環境の1リポジトリ制約）はローカルCLIの `--add-dir` に限定された制約であり、GHA環境では GitHub Token を使った `git clone` で外部リポジトリへの読み取りアクセスが可能と判明した。

- `/tmp/` への clone は可能
- Glob/Read ツールでは clone 先パスのファイルを読み取れる
- ただし Bash 経由でのファイル出力リダイレクトは sandbox によりブロックされる場合がある

## 提案

以下の知見をドキュメント・運用ガイドに反映することを検討する：

1. `docs/subagent-permission-guide.md` または `backlog.csv` の「対象リポジトリ」ガイドラインに「GHA環境でもclone経由でマルチリポジトリ調査が可能」と注記する
2. ISS-027 の課題詳細に「--add-dir 制約。clone によるワークアラウンドあり」を追記する
3. GHA施策での外部リポジトリアクセスパターンをテンプレートに組み込む

## 背景

- 施策: harness-engineering-brushup（実施フェーズでai-driven-dev-patternsをGHA環境から調査）
- GHA環境で `git clone` を使い ai-driven-dev-patterns の8エージェント・5ルールを調査できた

---
**記録日**: 2026-03-16
**発生施策**: harness-engineering-brushup
