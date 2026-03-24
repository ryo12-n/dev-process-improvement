---
name: gen-ci
description: 'テスト仕様（tests.json）から CI パイプライン定義（ci/pipeline.yaml）を生成する'
user-invocable: true
---
# gen-ci — CI パイプライン生成 Skill

## 概要

テスト仕様ファイル（`tests.json`）を読み取り、GitHub Actions 用の CI パイプライン定義（`ci/pipeline.yaml`）を生成する。

## チェーン内の位置づけ

```
tests.json
    ↓ ★ /gen-ci（この Skill）
ci/pipeline.yaml
    ↓ 人間レビュー＆承認
```

- **前工程**: `/gen-tests` — テスト仕様から生成された `tests.json` を入力として使用する
- **後工程**: 人間レビュー＆承認。CI パイプラインはチェーンの末端の一つであり、自動的に後続 Skill を呼び出さない

## 引数仕様

| 引数 | 必須 | 説明 | 例 |
|------|------|------|----|
| `<project-path>` | 任意 | 対象プロジェクトのパス | `projects/my-api` |

**引数なし呼び出し時の動作**: 「対象プロジェクトのパスを教えてください（例: projects/my-api）」とユーザーに質問する。

## 入力

| ファイル | パス | 説明 |
|---------|------|------|
| テスト仕様（JSON） | `<project-path>/artifacts/tests.json` | `/gen-tests` が生成したテストケース一覧 |

## 出力

| ファイル | パス | 説明 |
|---------|------|------|
| CI パイプライン | `<project-path>/artifacts/ci/pipeline.yaml` | GitHub Actions ワークフロー定義 |

## 処理フロー

<!-- TODO: 後続施策（ai-dev-chain-gen-ci）でプロンプト実装を行う -->

1. 引数からプロジェクトパスを取得する（引数なしの場合はユーザーに質問する）
2. `<project-path>/artifacts/tests.json` を読み込む
3. テスト仕様をもとに CI パイプラインのステップ・ジョブ構成を設計する
4. `<project-path>/artifacts/ci/pipeline.yaml` を生成する（GitHub Actions 形式）
5. 生成結果のサマリをユーザーに報告する

## TODO

- [ ] テスト仕様から CI パイプラインを導出するプロンプトの設計・実装
- [ ] `pipeline.yaml` のテンプレート定義（GitHub Actions 形式）
- [ ] テスト種別（単体・結合・E2E）に応じたジョブ分割ロジック
- [ ] バリデーション（`tests.json` が存在しない場合のエラーハンドリング）
- [ ] 既存パイプラインがある場合の上書き確認ロジック
- [ ] セキュリティチェック（`.claude/rules/gha-workflow-security.md` 準拠）
