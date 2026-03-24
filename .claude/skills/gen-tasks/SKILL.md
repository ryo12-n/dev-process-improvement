---
name: gen-tasks
description: 'API 設計とテスト仕様から実装タスク一覧（tasks.json）を生成する'
user-invocable: true
---
# gen-tasks — タスク生成 Skill

## 概要

API 設計書（`openapi.yaml`）とテスト仕様ファイル（`tests.json`）を読み取り、実装タスク一覧（`tasks.json`）を生成する。生成されたタスクは `l1-impl-manager` に引き渡して実装フェーズを開始できる。

## チェーン内の位置づけ

```
openapi.yaml + tests.json
    ↓ ★ /gen-tasks（この Skill）
tasks.json
    ↓ l1-impl-manager（既存 Skill）
実装コード / CI パス
```

- **前工程**: `/gen-design` — `openapi.yaml` を生成。`/gen-tests` — `tests.json` を生成。両方の成果物を入力として使用する
- **後工程**: `l1-impl-manager`（既存 Skill）— 本 Skill の出力 `tasks.json` をもとに実装タスクをオーケストレーションする

## 引数仕様

| 引数 | 必須 | 説明 | 例 |
|------|------|------|----|
| `<project-path>` | 任意 | 対象プロジェクトのパス | `projects/my-api` |

**引数なし呼び出し時の動作**: 「対象プロジェクトのパスを教えてください（例: projects/my-api）」とユーザーに質問する。

## 入力

| ファイル | パス | 説明 |
|---------|------|------|
| API 設計書 | `<project-path>/artifacts/openapi.yaml` | `/gen-design` が生成した OpenAPI 仕様 |
| テスト仕様（JSON） | `<project-path>/artifacts/tests.json` | `/gen-tests` が生成したテストケース一覧 |

## 出力

| ファイル | パス | 説明 |
|---------|------|------|
| タスク一覧 | `<project-path>/artifacts/tasks.json` | 構造化された実装タスク一覧（`l1-impl-manager` が消費可能な形式） |

## 処理フロー

<!-- TODO: 後続施策（ai-dev-chain-gen-tasks）でプロンプト実装を行う -->

1. 引数からプロジェクトパスを取得する（引数なしの場合はユーザーに質問する）
2. `<project-path>/artifacts/openapi.yaml` を読み込む
3. `<project-path>/artifacts/tests.json` を読み込む
4. API エンドポイントとテストケースをもとに、実装タスクを導出・構造化する
5. `<project-path>/artifacts/tasks.json` を生成する
6. 生成結果のサマリをユーザーに報告する

## TODO

- [ ] 設計・テスト仕様から実装タスクを導出するプロンプトの設計・実装
- [ ] `tasks.json` のスキーマ定義（タスク ID・種別・対象エンドポイント・関連テスト・依存関係等）
- [ ] `l1-impl-manager` が消費可能な形式の確認・調整
- [ ] バリデーション（前工程の成果物が存在しない場合のエラーハンドリング）
- [ ] 既存 `tasks.json` がある場合の上書き確認ロジック
- [ ] タスク間の依存関係グラフ生成ロジック
