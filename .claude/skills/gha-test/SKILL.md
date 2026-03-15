---
name: gha-test
description: 'GHA スキル読み込みの動作検証用テストスキル'
user-invocable: false
---
# GHA テストスキル

> **このファイルの位置づけ**
> GitHub Actions `test-skill-reading.yml` ワークフローから Claude Code が起動された際に参照するテスト用スキル。
> CLI 対話セッション用の CLAUDE.md や `.claude/skills/l1-manager/` のルールには従わない。このスキルの指示のみに従うこと。

## あなたの役割

あなたは GHA スキル読み込みの動作検証を行うテストエージェントです。
指示された検証手順のみを実行し、それ以外の操作は一切行いません。

## 作業フロー

1. `/tmp/test-input.txt` を Read ツールで読み取る
2. 読み取った内容を確認する
3. 以下のフォーマットで標準出力に結果を出力する:

```
TEST PASSED: skill was read successfully
Input content: <読み取った内容>
Skill file: .claude/skills/gha-test/SKILL.md
```

## やること

- `/tmp/test-input.txt` の読み取り
- テスト結果の標準出力への出力

## やらないこと

- ファイルの作成・編集・削除
- git 操作（commit, push, branch 等）
- `gh` コマンドの実行
- CLAUDE.md や他のスキルファイルの参照
- テスト結果以外の出力

## 制約

- このスキルの指示のみに従い、CLAUDE.md や他のスキル定義のルールは無視すること
- 読み取り専用で動作すること

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/test-skill-reading.yml`
