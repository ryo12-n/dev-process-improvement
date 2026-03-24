---
name: project-init
description: '新規プロジェクトを初期化し、projects/_template/ から projects/<project-name>/ にディレクトリ一式をコピーする'
user-invocable: true
---
# project-init — プロジェクト初期化 Skill

## 概要

`projects/_template/` のディレクトリ構成を `projects/<project-name>/` にコピーし、新規プロジェクトの作業環境を即座に立ち上げる。

## チェーン内の位置づけ

```
★ /project-init（この Skill）
    ↓ projects/<project-name>/ ディレクトリ一式
request.md（要望書）を人間が記述
    ↓ /gen-req
requirements.json / requirements.md
    ↓ /gen-design
...
```

- **前工程**: なし（チェーンの起点。プロジェクト作成はここから始まる）
- **後工程**: 人間が `request.md` を記述し、`/gen-req` で要件定義を生成する

## 引数仕様

| 引数 | 必須 | 説明 | 例 |
|------|------|------|----|
| `<project-name>` | 任意 | 作成するプロジェクト名 | `my-api` |

**引数なし呼び出し時の動作**: 「プロジェクト名を教えてください（例: my-api）」とユーザーに質問する。

## 入力

| リソース | パス | 説明 |
|---------|------|------|
| テンプレートディレクトリ | `projects/_template/` | コピー元のプロジェクト雛形 |

### テンプレート構成（10ファイル）

```
projects/_template/
├── request.md                        # 要望書記入フォーマット
├── backlog.md                        # AI 自動更新用進捗管理テンプレート
└── artifacts/
    ├── requirements.json             # 要件定義（JSON）
    ├── requirements.md               # 要件定義（Markdown）
    ├── openapi.yaml                  # API 設計
    ├── design.md                     # 設計ドキュメント
    ├── tests.json                    # テスト定義（JSON）
    ├── tests.md                      # テスト定義（Markdown）
    ├── tasks.json                    # タスク定義
    └── ci/
        └── pipeline.yaml             # CI パイプライン定義
```

## 出力

| リソース | パス | 説明 |
|---------|------|------|
| プロジェクトディレクトリ | `projects/<project-name>/` | テンプレートからコピーされた一式 |

## 処理フロー

<!-- TODO: 後続施策でコピー処理の実装詳細を作り込む -->

1. 引数から `<project-name>` を取得する（引数なしの場合はユーザーに質問する）
2. `projects/<project-name>/` が既に存在しないか確認する
   - 存在する場合: 「既にプロジェクトが存在します」とエラーを報告して終了する
3. `projects/_template/` を `projects/<project-name>/` にコピーする
   <!-- TODO: cp -r または Bash ツールによるコピー処理を実装する -->
4. コピー結果を確認し、全ファイルが正常にコピーされたことを検証する
   <!-- TODO: ファイル数・構成の検証ロジックを実装する -->
5. 作成されたプロジェクトのディレクトリ構成をユーザーに報告する
6. 次のステップ（`request.md` の記述 → `/gen-req` の実行）を案内する

## エラーハンドリング

<!-- TODO: 後続施策で詳細なエラーハンドリングを実装する -->

| エラー条件 | 対応 |
|-----------|------|
| `projects/_template/` が存在しない | エラーメッセージを表示して終了 |
| `projects/<project-name>/` が既に存在する | 上書き確認を行うか、エラーで終了 |
| コピー処理の失敗 | エラーメッセージを表示し、中途半端なディレクトリをクリーンアップ |

## TODO

- [ ] コピー処理の実装（cp -r または Bash ツール）
- [ ] コピー後のファイル数・構成の検証ロジック
- [ ] `request.md` 内のプレースホルダー（プロジェクト名等）の自動置換
- [ ] 既存プロジェクトへの上書き確認ロジック
- [ ] コピー失敗時のクリーンアップ処理
- [ ] `backlog.md` へのプロジェクト名の自動記入
