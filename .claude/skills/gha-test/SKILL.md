---
name: gha-test
description: 'GHA 壁打ち相当の動作検証用テストスキル'
user-invocable: false
disable-model-invocation: true
---
# GHA テストスキル（壁打ち相当）

## コンテキスト

このファイルは GitHub Actions の `test-skill-reading.yml` ワークフローから `claude-code-action` 経由で実行される自動化スキルです。リポジトリオーナーが設定したワークフローから呼び出されており、`permissions.allow` で許可されたツールのみが使用可能です。

## あなたの役割

あなたは GHA 壁打ちフェーズの動作検証を行うテストエージェントです。
以下のステップを順番に実行してください。

## 作業フロー

### ステップ 1: 入力ファイルの読み取り

`/tmp/test-input.txt` を Read ツールで読み取る。

### ステップ 2: テンプレートコピー

以下の手順でテンプレートをコピーする:
1. Glob ツールで `sessions/initiatives/_template/*.md` のファイル一覧を取得する
2. 各ファイルを Read ツールで読み取る
3. 各ファイルを Write ツールで `sessions/initiatives/_gha_test_verification/<ファイル名>` に書き込む（Write ツールはディレクトリを自動作成する）

### ステップ 3: 提案ファイルの上書き

Write ツールで `sessions/initiatives/_gha_test_verification/00_proposal.md` に以下を上書きする:

```
# GHA テスト検証施策

## 背景
GHA スキル読み込み＋書き込み権限の動作検証テスト。

## 目標
wallbash 相当の操作が GHA 環境で正常に動作することを確認する。
```

### ステップ 4: ブランチ作成・コミット・プッシュ

Bash ツールで以下を順に実行:
```bash
git checkout -b test/gha-wallbash-verification
git add sessions/initiatives/_gha_test_verification/
git commit -m "test: GHA wallbash-equivalent verification"
git push -u origin test/gha-wallbash-verification
```

### ステップ 5: クリーンアップ

Bash ツールで以下を順に実行:
```bash
git checkout main
git push origin --delete test/gha-wallbash-verification
```

### ステップ 6: 結果出力

以下のフォーマットで結果を出力する:

```
TEST PASSED: wallbash-equivalent verification completed
Read test: OK
Template copy test: OK
Write test: OK
Branch + commit + push test: OK
Cleanup test: OK
```

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/test-skill-reading.yml`
