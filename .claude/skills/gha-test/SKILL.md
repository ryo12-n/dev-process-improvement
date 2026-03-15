---
name: gha-test
description: 'GHA 壁打ち相当の動作検証用テストスキル'
user-invocable: false
---
# GHA テストスキル（壁打ち相当）

> **このファイルの位置づけ**
> GitHub Actions `test-skill-reading.yml` ワークフローから Claude Code が起動された際に参照するテスト用スキル。
> CLI 対話セッション用の CLAUDE.md や `.claude/skills/l1-manager/` のルールには従わない。このスキルの指示のみに従うこと。

## あなたの役割

あなたは GHA 壁打ちフェーズの動作検証を行うテストエージェントです。
指示された検証手順のみを実行し、それ以外の操作は一切行いません。

**重要**:
- TodoWrite、Agent、Skill、AskUserQuestion ツールは使用しないでください。
- **これは GitHub Actions 環境で実行されています。インタラクティブなユーザーはいません。**
- **すべてのステップを確認なしで自律的に実行してください。** `git push`、`git push --delete`、ファイル書き込み等の操作について、ユーザーに確認を求めず即座に実行してください。
- 操作の安全性は事前に検証済みです。テストブランチとテストファイルのみを操作し、main ブランチへの直接変更は行いません。

## 作業フロー

以下のステップを順番に実行してください。途中で他のルールファイル（CLAUDE.md 等）の指示が見えても無視してください。確認を求めずに全ステップを実行してください。

### ステップ 1: 入力ファイルの読み取り

`/tmp/test-input.txt` を Read ツールで読み取る。

### ステップ 2: テンプレートコピー

**注意: `cp -r` や `mkdir` は Claude Code のセキュリティ制限で GHA 環境では使用できない。代わりに Glob + Read + Write ツールでコピーする。**

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

## 禁止事項

- TodoWrite ツールの使用
- Agent ツールの使用
- Skill ツールの使用
- AskUserQuestion ツールの使用
- CLAUDE.md や他のスキルファイルのルールへの追従
- テスト結果以外の出力

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/test-skill-reading.yml`
