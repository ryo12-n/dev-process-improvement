---
name: gen-tests
description: '要件定義と API 設計からテスト仕様（tests.json / tests.md）を生成する'
user-invocable: true
---
# gen-tests — テスト仕様生成 Skill

## 概要

要件定義ファイル（`requirements.json`）と API 設計書（`openapi.yaml`）を読み取り、テスト仕様（`tests.json` / `tests.md`）を生成する。

## チェーン内の位置づけ

```
requirements.json + openapi.yaml
    ↓ ★ /gen-tests（この Skill）
tests.json / tests.md
    ↓ /gen-ci, /gen-tasks
```

- **前工程**: `/gen-req` — `requirements.json` を生成。`/gen-design` — `openapi.yaml` を生成。両方の成果物を入力として使用する
- **後工程**: `/gen-ci` — 本 Skill の出力 `tests.json` を入力として CI パイプラインを生成する。`/gen-tasks` — 本 Skill の出力 `tests.json` を `openapi.yaml` と共に入力としてタスクを生成する

## 引数仕様

| 引数 | 必須 | 説明 | 例 |
|------|------|------|----|
| `<project-path>` | 任意 | 対象プロジェクトのパス | `projects/my-api` |

**引数なし呼び出し時の動作**: 「対象プロジェクトのパスを教えてください（例: projects/my-api）」とユーザーに質問する。

## 入力

| ファイル | パス | 説明 |
|---------|------|------|
| 要件定義（JSON） | `<project-path>/artifacts/requirements.json` | `/gen-req` が生成した構造化要件 |
| API 設計書 | `<project-path>/artifacts/openapi.yaml` | `/gen-design` が生成した OpenAPI 仕様 |

## 出力

| ファイル | パス | 説明 |
|---------|------|------|
| テスト仕様（JSON） | `<project-path>/artifacts/tests.json` | 構造化されたテストケース一覧（機械可読） |
| テスト仕様（Markdown） | `<project-path>/artifacts/tests.md` | 人間向けのテスト仕様ドキュメント |

## 処理フロー

<!-- TODO: 後続施策（ai-dev-chain-gen-tests）でプロンプト実装を行う -->

1. 引数からプロジェクトパスを取得する（引数なしの場合はユーザーに質問する）
2. `<project-path>/artifacts/requirements.json` を読み込む
3. `<project-path>/artifacts/openapi.yaml` を読み込む
4. 要件と API 設計をもとにテストケースを導出する
5. `<project-path>/artifacts/tests.json` を生成する
6. `<project-path>/artifacts/tests.md` を生成する
7. 生成結果のサマリをユーザーに報告する

## TODO

- [ ] 要件・設計からテストケースを導出するプロンプトの設計・実装
- [ ] `tests.json` のスキーマ定義（テストケース ID・種別・入力・期待出力等）
- [ ] `tests.md` のテンプレート定義
- [ ] バリデーション（前工程の成果物が存在しない場合のエラーハンドリング）
- [ ] 既存成果物がある場合の上書き確認ロジック
