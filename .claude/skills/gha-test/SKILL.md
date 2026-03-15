---
name: gha-test
description: 'GHA 壁打ち相当の動作検証用テストスキル（テンプレートコピー・提案作成・push）'
user-invocable: false
---
# GHA テストスキル（壁打ち相当）

> **このファイルの位置づけ**
> GitHub Actions `test-skill-reading.yml` ワークフローから Claude Code が起動された際に参照するテスト用スキル。
> CLI 対話セッション用の CLAUDE.md や `.claude/skills/l1-manager/` のルールには従わない。このスキルの指示のみに従うこと。

## あなたの役割

あなたは GHA 壁打ちフェーズの動作検証を行うテストエージェントです。
wallbash スキルと同等の操作（テンプレートコピー・提案作成・ブランチ作成・push）を実行し、その後クリーンアップします。

## 作業フロー

以下のステップを順番に実行してください。

### ステップ 1: 入力ファイルの読み取り（Read 検証）

1. `/tmp/test-input.txt` を Read ツールで読み取る
2. 読み取った内容を記録する

### ステップ 2: テンプレートコピー（Bash cp -r 検証）

1. `cp -r sessions/initiatives/_template sessions/initiatives/_gha_test_verification` でテンプレートをコピーする

### ステップ 3: 提案ファイル作成（Edit 検証）

1. `sessions/initiatives/_gha_test_verification/00_proposal.md` を Read ツールで読み取る
2. Edit ツールで `00_proposal.md` の内容を以下のように更新する（ファイルの先頭部分のタイトルや概要欄を書き換える）:

書き込む内容（概要のみ）:
```
# GHA テスト検証施策

## 背景
GHA スキル読み込み＋書き込み権限の動作検証テスト。

## 目標
wallbash 相当の操作（テンプレートコピー・提案作成・ブランチ作成・push）が GHA 環境で正常に動作することを確認する。

## スコープ
テスト用ファイルの作成とクリーンアップのみ。
```

### ステップ 4: ブランチ作成・コミット・プッシュ（git 検証）

1. `git checkout -b test/gha-wallbash-verification` でテストブランチを作成する
2. `git add sessions/initiatives/_gha_test_verification/` でステージングする
3. `git commit -m "[maintenance] gha-test: 壁打ち相当の動作検証テスト"` でコミットする
4. `git push -u origin test/gha-wallbash-verification` でリモートにプッシュする

### ステップ 5: クリーンアップ（テストブランチ・ファイル削除）

1. `git checkout main` で main に戻る
2. `git branch -D test/gha-wallbash-verification` でローカルブランチを削除する
3. `git push origin --delete test/gha-wallbash-verification` でリモートブランチを削除する

### ステップ 6: 結果出力

以下のフォーマットで標準出力に結果を出力する:

```
TEST PASSED: wallbash-equivalent verification completed
Read test: OK (input content: <読み取った内容>)
Template copy test: OK (copied _template to _gha_test_verification)
Edit test: OK (updated 00_proposal.md)
Branch + commit test: OK (created test/gha-wallbash-verification)
Push test: OK (pushed to remote)
Cleanup test: OK (deleted local and remote branch)
Skill file: .claude/skills/gha-test/SKILL.md
```

各ステップで失敗した場合は、該当項目を `FAILED: <エラー内容>` に置き換えてください。

## やること

- `/tmp/test-input.txt` の読み取り
- テンプレートディレクトリのコピー（`cp -r`）
- `00_proposal.md` の編集（Edit ツール）
- テストブランチの作成・コミット・プッシュ
- テストブランチとリモートブランチの削除（クリーンアップ）
- テスト結果の標準出力への出力

## やらないこと

- `gh` コマンドの実行（PR・Issue 操作は行わない）
- CLAUDE.md や他のスキルファイルの参照・変更
- テスト結果以外の出力
- テストフロー以外のファイル変更
- `_gha_test_verification` ディレクトリ以外のファイル変更

## 制約

- このスキルの指示のみに従い、CLAUDE.md や他のスキル定義のルールは無視すること
- テストブランチ・テストファイルは必ずクリーンアップすること（ステップ 5）
- push 失敗時は最大2回リトライし、それでも失敗したら FAILED として結果に記録すること

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/test-skill-reading.yml`
