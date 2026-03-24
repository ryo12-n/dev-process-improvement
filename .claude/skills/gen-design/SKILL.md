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

以下のステップを順番に実行する。

---

### ステップ 1: プロジェクトパスの取得

- 引数 `<project-path>` が指定されている場合、そのパスを使用する
- 引数が指定されていない場合、ユーザーに質問する:
  > 対象プロジェクトのパスを教えてください（例: `projects/my-api`）

以降、取得したパスを `PROJECT` と表記する。

---

### ステップ 2: バリデーション（入力チェック）

以下のチェックを順に実行する。いずれかで失敗した場合、エラーメッセージを表示して処理を中止する。

#### 2a. requirements.json の存在確認

`PROJECT/artifacts/requirements.json` が存在するか確認する（Read ツールで読み込みを試みる）。

- **存在しない場合**: 以下のメッセージを表示して処理を中止する:
  > エラー: `PROJECT/artifacts/requirements.json` が見つかりません。
  > 先に `/gen-req PROJECT` を実行して要件定義を生成してください。

#### 2b. requirements.json の内容チェック

読み込んだ `requirements.json` に以下の必須フィールドが存在し、空でないことを確認する:

1. `project.name` — 空文字でないこと
2. `project.description` — 空文字でないこと
3. `functional_requirements` — 空配列でないこと（1件以上の FR が必要）

- **必須フィールドが不足・空の場合**: 以下のメッセージを表示して処理を中止する:
  > エラー: `requirements.json` の内容が不十分です。不足フィールド: [フィールド名一覧]
  > `/gen-req PROJECT` で要件定義を再生成してください。

- **NFR・constraints が空の場合**: 警告を表示し続行する:
  > 警告: 非機能要件（NFR）/ 制約事項が未定義です。デフォルトの設計方針を適用します。

---

### ステップ 3: 既存ファイルの上書き確認

`PROJECT/artifacts/openapi.yaml` または `PROJECT/artifacts/design.md` が既に存在し、かつプレースホルダーではない実質的な内容を含む場合、ユーザーに上書き確認を行う:

> `openapi.yaml` / `design.md` が既に存在します。上書きしてよいですか？
> - 上書きする場合: 「はい」と回答してください
> - 中止する場合: 「いいえ」と回答してください

**判定基準**: `info.title` が `"[プロジェクト名] API"` のまま（openapi.yaml）、またはセクションが全てコメントのみ（design.md）の場合はプレースホルダーとみなし、確認なしで上書きする。

---

### ステップ 4: 要件からの設計導出

`requirements.json` の内容を分析し、API エンドポイント・データモデル・アーキテクチャを設計する。以下の 4 サブステップで導出する。

#### 4a. エンドポイント設計（FR → API パス）

各 `functional_requirements` の `acceptance_criteria` を分析し、必要な API エンドポイントを導出する。

**導出ルール**:
- 各 acceptance_criteria の動詞・操作から HTTP メソッドを決定する:
  - 「登録できる」「作成できる」「送信できる」→ `POST`
  - 「取得できる」「確認できる」「参照できる」「一覧を取得」→ `GET`
  - 「更新できる」「変更できる」「設定できる」→ `PUT` / `PATCH`
  - 「削除できる」→ `DELETE`
- acceptance_criteria のリソース名からパスを決定する（RESTful 規約に従う）:
  - コレクション: `/resources`（複数形）
  - 個別リソース: `/resources/{id}`
  - ネストリソース: `/resources/{id}/sub-resources`
  - アクション: `/resources/{id}/action`（承認・却下等の状態変更）
- `user_stories` が空配列の FR も `acceptance_criteria` から同様にエンドポイントを導出する
- 各エンドポイントに対応する FR ID をトレーサビリティとして記録する

#### 4b. データモデル設計（エンドポイント → スキーマ）

ステップ 4a のエンドポイントで必要となるリクエスト/レスポンスのデータ構造を設計する。

**導出ルール**:
- エンドポイントのリソース名から主要エンティティを抽出する
- `acceptance_criteria` に記載された属性（「タイトル・著者・出版社」等）をプロパティとして定義する
- エンティティ間の関係（1対多・多対多）を `acceptance_criteria` の文脈から推定する
- 共通パターンを抽出する:
  - ページネーション: `PaginatedResponse` スキーマ
  - エラーレスポンス: `ErrorResponse` スキーマ
  - ID・タイムスタンプ: 全エンティティ共通属性

#### 4c. アーキテクチャ設計（constraints + NFR → 技術方針）

`constraints`（技術制約）と `non_functional_requirements` を分析し、アーキテクチャ方針を決定する。

**導出ルール**:
- `constraints` の言語/フレームワーク指定 → コンポーネントの技術スタックを決定
- `constraints` の DB 指定 → データストア層の構成を決定
- `constraints` のインフラ指定 → デプロイ構成を決定
- `NFR (performance)` → キャッシュ戦略・インデックス設計方針を決定
- `NFR (security)` → 認証・認可方式、暗号化方針を決定
- `NFR (availability)` → 冗長化・ヘルスチェック方針を決定
- `NFR (scalability)` → スケーリング戦略を決定
- constraints が空の場合はデフォルト方針（Node.js + PostgreSQL）を適用する

#### 4d. セキュリティ設計（NFR security + FR 認証系 → セキュリティ方針）

`non_functional_requirements` の `security` カテゴリと、認証・認可に関連する FR を統合してセキュリティ設計を導出する。

**導出ルール**:
- 認証方式: FR の acceptance_criteria から認証要件を抽出（JWT、OAuth 等）
- 認可方式: FR のロール・権限に関する acceptance_criteria から RBAC / ABAC を決定
- セキュリティスキーム: OpenAPI の `securitySchemes` に反映する
- パスワード管理: NFR の暗号化要件を反映する

---

### ステップ 5: openapi.yaml の生成

ステップ 4 の設計結果を、OpenAPI 3.0.3 準拠の YAML ファイルとして生成する。

#### openapi.yaml 構造

```yaml
openapi: "3.0.3"
info:
  title: "<project.name> API"
  version: "<project.version>"
  description: "<project.description>"

servers:
  - url: http://localhost:3000
    description: ローカル開発環境

paths:
  # ステップ 4a で導出したエンドポイントを定義
  # 各エンドポイントには以下を含める:
  #   - summary: エンドポイントの説明
  #   - operationId: キャメルケースの一意な操作ID
  #   - tags: リソース名でグループ化
  #   - parameters: パスパラメータ・クエリパラメータ
  #   - requestBody: POST/PUT/PATCH の場合
  #   - responses: 成功レスポンス + エラーレスポンス
  #   - security: 認証が必要な場合
  #   - x-fr-id: 対応する FR ID（トレーサビリティ用カスタム拡張）

components:
  schemas:
    # ステップ 4b で導出したデータモデルを定義
    # 各スキーマには以下を含める:
    #   - type: object
    #   - required: 必須プロパティ一覧
    #   - properties: 各プロパティの型・説明・制約
    # 共通スキーマ:
    #   - ErrorResponse: { code, message, details }
    #   - PaginatedResponse: { items, total, page, per_page }

  securitySchemes:
    # ステップ 4d で導出したセキュリティスキームを定義
    # 例: bearerAuth: { type: http, scheme: bearer, bearerFormat: JWT }
```

**生成ルール**:
- すべてのパスにレスポンスとして `200`/`201`（成功）と `400`/`401`/`404`/`500`（エラー）を含める
- リクエスト/レスポンスの `schema` は `$ref` で `components/schemas` を参照する
- `tags` はリソース名（Books, Loans, Users 等）でグループ化する
- ページネーション対応のエンドポイントには `page`, `per_page` クエリパラメータを定義する
- 認証が必要なエンドポイントには `security: [bearerAuth: []]` を設定する（公開エンドポイントを除く）
- `x-fr-id` カスタム拡張でエンドポイントと FR の対応を明示する

**出力先**: `PROJECT/artifacts/openapi.yaml`

---

### ステップ 6: design.md の生成

ステップ 4 の設計結果を、以下のテンプレートに従って Markdown ファイルとして生成する。`openapi.yaml` と内容が一致していることを保証する。

#### design.md テンプレート

````markdown
# 設計ドキュメント: <project.name>

> このファイルは `/gen-design` が `requirements.json` から自動生成しました。
> `openapi.yaml` と対になる人間向け設計説明書です。

---

## 1. アーキテクチャ概要

<!-- ステップ 4c の結果を記述 -->
<!-- 以下を含める:
     - システム全体の構成概要（1〜3段落）
     - constraints から導出した技術スタックの説明
     - NFR から導出した設計方針の説明
-->

## 2. コンポーネント構成

| コンポーネント | 役割 | 技術スタック |
|-------------|------|------------|
<!-- constraints から導出したコンポーネント一覧 -->
<!-- 例: API サーバー / データベース / キャッシュ / 認証モジュール -->

## 3. データモデル

<!-- ステップ 4b の結果を記述 -->

### エンティティ一覧

| エンティティ | 説明 | 主要属性 |
|------------|------|---------|
<!-- openapi.yaml の components/schemas から主要エンティティを一覧化 -->

### エンティティ関連図

<!-- エンティティ間の関係（1対多・多対多）をテキストで説明 -->

## 4. API 設計方針

- **認証方式**: <!-- ステップ 4d の認証方式 -->
- **エラーハンドリング**: <!-- ErrorResponse スキーマの説明 -->
- **バージョニング**: <!-- URL パスまたはヘッダーによるバージョニング方針 -->
- **ページネーション**: <!-- ページネーション方式の説明 -->

### エンドポイント一覧

| メソッド | パス | 説明 | 対応 FR |
|---------|------|------|---------|
<!-- openapi.yaml の paths から一覧を生成 -->

## 5. インフラ構成

<!-- ステップ 4c の constraints（インフラ指定）から記述 -->
<!-- 以下を含める:
     - ローカル開発環境の構成（Docker Compose 等）
     - 本番環境の想定構成
     - NFR (availability) から導出した冗長化方針
-->

## 6. セキュリティ設計

<!-- ステップ 4d の結果を記述 -->
<!-- 以下を含める:
     - 認証・認可の方式と実装方針
     - パスワード管理
     - NFR (security) から導出したセキュリティ対策
     - API アクセス制御（ロール別のエンドポイントアクセス）
-->

## 7. 設計上の決定事項（ADR）

| # | 決定 | 理由 | 代替案 |
|---|------|------|--------|
<!-- 設計導出過程での主要な判断を ADR 形式で記録 -->
<!-- 各行: constraints/NFR からなぜその設計を選んだかを説明 -->

---
**生成元**: `requirements.json`
**生成日**: <YYYY-MM-DD>
**生成 Skill**: `/gen-design`
````

**出力先**: `PROJECT/artifacts/design.md`

---

### ステップ 7: 生成結果の報告

生成完了後、以下の形式でユーザーにサマリを報告する:

> **gen-design 完了**
>
> - **プロジェクト**: <プロジェクト名>
> - **API エンドポイント数**: <paths の数> 件
> - **データモデル数**: <components/schemas の数> 件
> - **セキュリティスキーム**: <securitySchemes の説明>
> - **対応 FR**: <FR ID 一覧と対応エンドポイント数>
> - **対応 NFR**: <NFR ID 一覧と反映先>
>
> 生成ファイル:
> - `PROJECT/artifacts/openapi.yaml`
> - `PROJECT/artifacts/design.md`
>
> 次のステップ: `/gen-tests PROJECT` でテスト仕様を生成できます。
