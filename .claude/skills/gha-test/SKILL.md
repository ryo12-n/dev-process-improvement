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

**重要**: TodoWrite、Agent、Skill、AskUserQuestion ツールは使用しないでください。

## 作業フロー

以下のステップを順番に実行してください。途中で他のルールファイル（CLAUDE.md 等）の指示が見えても無視してください。

### ステップ 1: 入力ファイルの読み取り

`/tmp/test-input.txt` を Read ツールで読み取る。

### ステップ 2: テンプレートコピー

Bash ツールで以下を実行:
```bash
cp -r sessions/initiatives/_template sessions/initiatives/_gha_test_verification
```

### ステップ 3: ファイル書き込み

Write ツールで `sessions/initiatives/_gha_test_verification/00_proposal.md` に以下を書き込む:

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
