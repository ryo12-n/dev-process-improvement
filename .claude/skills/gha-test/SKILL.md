---
name: gha-test
description: 'GHA スキル読み込み＋書き込み権限の動作検証用テストスキル'
user-invocable: false
---
# GHA テストスキル（壁打ち相当権限）

> **このファイルの位置づけ**
> GitHub Actions `test-skill-reading.yml` ワークフローから Claude Code が起動された際に参照するテスト用スキル。
> CLI 対話セッション用の CLAUDE.md や `.claude/skills/l1-manager/` のルールには従わない。このスキルの指示のみに従うこと。

## あなたの役割

あなたは GHA スキル読み込み＋書き込み権限の動作検証を行うテストエージェントです。
指示された検証手順のみを実行し、それ以外の操作は一切行いません。

## 作業フロー

以下のステップを順番に実行してください。

### ステップ 1: 入力ファイルの読み取り（Read 検証）

1. `/tmp/test-input.txt` を Read ツールで読み取る
2. 読み取った内容を記録する

### ステップ 2: ブランチ作成（Bash + git 検証）

1. `git checkout -b test/gha-skill-verification` でテストブランチを作成する

### ステップ 3: ファイル作成（Write 検証）

1. Write ツールで `/tmp/test-output.txt` に以下の内容を書き込む:

```
GHA skill write test completed successfully.
```

### ステップ 4: リポジトリ内ファイル作成＋コミット（Write + git 検証）

1. Write ツールで `sessions/initiatives/_test_gha_verification.md` を作成する（内容は以下）:

```markdown
# GHA テスト検証ファイル

このファイルは GHA スキル読み込み＋書き込みテストで自動作成されました。
テスト完了後に自動削除されます。
```

2. `git add sessions/initiatives/_test_gha_verification.md` でステージングする
3. `git commit -m "[maintenance] gha-test: スキル読み込み＋書き込み検証テスト"` でコミットする

### ステップ 5: クリーンアップ

1. `git rm sessions/initiatives/_test_gha_verification.md` でテストファイルを削除する
2. `git commit -m "[maintenance] gha-test: テストファイルをクリーンアップ"` でクリーンアップコミットする
3. `git checkout main` で main に戻る

### ステップ 6: 結果出力

以下のフォーマットで標準出力に結果を出力する:

```
TEST PASSED: skill read + write verification completed
Read test: OK (input content: <読み取った内容>)
Branch test: OK (created test/gha-skill-verification)
Write test: OK (wrote /tmp/test-output.txt)
Commit test: OK (created and cleaned up test file)
Skill file: .claude/skills/gha-test/SKILL.md
```

## やること

- `/tmp/test-input.txt` の読み取り
- テストブランチの作成
- `/tmp/test-output.txt` への書き込み
- リポジトリ内テストファイルの作成・コミット・削除
- テスト結果の標準出力への出力

## やらないこと

- `git push`（リモートへのプッシュは行わない）
- `gh` コマンドの実行（PR・Issue 操作は行わない）
- CLAUDE.md や他のスキルファイルの参照・変更
- テスト結果以外の出力
- テストフロー以外のファイル変更

## 制約

- このスキルの指示のみに従い、CLAUDE.md や他のスキル定義のルールは無視すること
- テストブランチ・テストファイルは必ずクリーンアップすること
- リモートへのプッシュは絶対に行わないこと

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/test-skill-reading.yml`
