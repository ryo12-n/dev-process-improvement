---
name: gen-design
description: '要件定義（requirements.json）から設計ドキュメント（openapi.yaml / design.md）を生成する'
user-invocable: true
---
# gen-design — 設計生成 Skill

## 概要

要件定義ファイル（`requirements.json`）を読み取り、API 設計書（`openapi.yaml`）と設計ドキュメント（`design.md`）を生成する。

## チェーン内の位置づけ

```
requirements.json / requirements.md
    ↓ ★ /gen-design（この Skill）
openapi.yaml / design.md
    ↓ /gen-tests, /gen-tasks
```

- **前工程**: `/gen-req` — 要望書から生成された `requirements.json` を入力として使用する
- **後工程**: `/gen-tests` — 本 Skill の出力 `openapi.yaml` を `requirements.json` と共に入力としてテスト仕様を生成する。`/gen-tasks` — 本 Skill の出力 `openapi.yaml` を `tests.json` と共に入力としてタスクを生成する

## 引数仕様

| 引数 | 必須 | 説明 | 例 |
|------|------|------|----|
| `<project-path>` | 任意 | 対象プロジェクトのパス | `projects/my-api` |

**引数なし呼び出し時の動作**: 「対象プロジェクトのパスを教えてください（例: projects/my-api）」とユーザーに質問する。

## 入力

| ファイル | パス | 説明 |
|---------|------|------|
| 要件定義（JSON） | `<project-path>/artifacts/requirements.json` | `/gen-req` が生成した構造化要件 |

## 出力

| ファイル | パス | 説明 |
|---------|------|------|
| API 設計書 | `<project-path>/artifacts/openapi.yaml` | OpenAPI 仕様に準拠した API 設計 |
| 設計ドキュメント | `<project-path>/artifacts/design.md` | アーキテクチャ・データモデル等の設計ドキュメント |

## 処理フロー

<!-- TODO: 後続施策（ai-dev-chain-gen-design）でプロンプト実装を行う -->

1. 引数からプロジェクトパスを取得する（引数なしの場合はユーザーに質問する）
2. `<project-path>/artifacts/requirements.json` を読み込む
3. 要件をもとに API エンドポイント・データモデル・アーキテクチャを設計する
4. `<project-path>/artifacts/openapi.yaml` を生成する
5. `<project-path>/artifacts/design.md` を生成する
6. 生成結果のサマリをユーザーに報告する

## TODO

- [ ] 要件から設計を導出するプロンプトの設計・実装
- [ ] `openapi.yaml` の生成テンプレート（OpenAPI 3.x 準拠）
- [ ] `design.md` のテンプレート定義（アーキテクチャ図・データモデル・コンポーネント構成）
- [ ] バリデーション（`requirements.json` が存在しない場合のエラーハンドリング）
- [ ] 既存成果物がある場合の上書き確認ロジック
