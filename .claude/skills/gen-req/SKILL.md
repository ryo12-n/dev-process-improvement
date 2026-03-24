---
name: gen-req
description: '要望書（request.md）から要件定義（requirements.json / requirements.md）を生成する'
user-invocable: true
---
# gen-req — 要件定義生成 Skill

## 概要

ユーザーが記述した要望書（`request.md`）を読み取り、構造化された要件定義ファイル（`requirements.json` / `requirements.md`）を生成する。

## チェーン内の位置づけ

```
request.md（要望書）
    ↓ ★ /gen-req（この Skill）
requirements.json / requirements.md
    ↓ /gen-design
```

- **前工程**: なし（チェーンの起点。人間が `request.md` を記述する）
- **後工程**: `/gen-design` — 本 Skill の出力 `requirements.json` を入力として設計ドキュメントを生成する

## 引数仕様

| 引数 | 必須 | 説明 | 例 |
|------|------|------|----|
| `<project-path>` | 任意 | 対象プロジェクトのパス | `projects/my-api` |

**引数なし呼び出し時の動作**: 「対象プロジェクトのパスを教えてください（例: projects/my-api）」とユーザーに質問する。

## 入力

| ファイル | パス | 説明 |
|---------|------|------|
| 要望書 | `<project-path>/request.md` | ユーザーが記述したシステム要望 |

## 出力

| ファイル | パス | 説明 |
|---------|------|------|
| 要件定義（JSON） | `<project-path>/artifacts/requirements.json` | 構造化された要件一覧（機械可読） |
| 要件定義（Markdown） | `<project-path>/artifacts/requirements.md` | 人間向けの要件定義ドキュメント |

## 処理フロー

<!-- TODO: 後続施策（ai-dev-chain-gen-req）でプロンプト実装を行う -->

1. 引数からプロジェクトパスを取得する（引数なしの場合はユーザーに質問する）
2. `<project-path>/request.md` を読み込む
3. 要望書の内容を分析し、要件を抽出・構造化する
4. `<project-path>/artifacts/requirements.json` を生成する
5. `<project-path>/artifacts/requirements.md` を生成する
6. 生成結果のサマリをユーザーに報告する

## TODO

- [ ] 要望書から要件を抽出するプロンプトの設計・実装
- [ ] `requirements.json` のスキーマ定義
- [ ] `requirements.md` のテンプレート定義
- [ ] バリデーション（`request.md` が存在しない場合のエラーハンドリング）
- [ ] 既存 `requirements.json` がある場合の上書き確認ロジック
