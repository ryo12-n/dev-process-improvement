# 設計ドキュメント: BookShelf API

> このファイルは `/gen-design` が `requirements.json` から自動生成しました。
> `openapi.yaml` と対になる人間向け設計説明書です。

---

## 1. アーキテクチャ概要

BookShelf API は、社内チーム向けの書籍管理システムである。蔵書の登録・検索・貸出管理を REST API で提供し、フロントエンドは別プロジェクトとして分離する。

技術スタックは constraints に基づき TypeScript + Express.js をアプリケーション層、PostgreSQL 15+ をデータストア層として採用する。ローカル開発環境は Docker Compose で構成し、将来的に AWS ECS へのデプロイを想定する。

NFR に基づく設計方針として、1000冊規模での検索レスポンス 500ms 以内を達成するために PostgreSQL の全文検索インデックス（GIN インデックス）を活用する。認証は JWT ベースとし、パスワードは bcrypt でハッシュ化する。同時 50 ユーザー・蔵書 10,000 冊の規模に対応するため、コネクションプーリングを適用する。

## 2. コンポーネント構成

| コンポーネント | 役割 | 技術スタック |
|-------------|------|------------|
| API サーバー | REST API エンドポイントの提供、リクエスト処理 | TypeScript + Express.js |
| データベース | 書籍・ユーザー・貸出データの永続化 | PostgreSQL 15+ |
| 認証モジュール | JWT トークンの発行・検証、RBAC によるアクセス制御 | jsonwebtoken + bcrypt |
| ISBN 外部連携 | ISBN から書誌情報を自動取得 | OpenBD API（外部） |
| コンテナ基盤 | ローカル開発環境の構成 | Docker Compose |

## 3. データモデル

### エンティティ一覧

| エンティティ | 説明 | 主要属性 |
|------------|------|---------|
| User | システム利用者（管理者・一般利用者） | id, email, name, role, password_hash |
| Book | 蔵書情報 | id, isbn, title, author, publisher, published_date, category_id, is_available |
| Tag | 書籍に付与する分類タグ | id, name |
| Category | 書籍のカテゴリ | id, name, description |
| LoanRequest | 貸出リクエスト（承認ワークフロー） | id, book_id, user_id, status, reason |
| Loan | 貸出レコード（承認後に作成） | id, book_id, user_id, status, loan_date, due_date, return_date |

### エンティティ関連図

- **User → LoanRequest**: 1対多。1人の利用者が複数の貸出リクエストを送信できる。
- **User → Loan**: 1対多。1人の利用者が複数の書籍を同時に借りられる。
- **Book → LoanRequest**: 1対多。1冊の書籍に対して複数の貸出リクエストが存在しうる（キュー方式）。
- **Book → Loan**: 1対多。1冊の書籍が時系列で複数回貸し出される（同時に active は1件のみ）。
- **Book → Tag**: 多対多。中間テーブル（book_tags）で管理する。
- **Book → Category**: 多対1。1冊の書籍は1つのカテゴリに属する。

## 4. API 設計方針

- **認証方式**: JWT Bearer トークン認証。`/auth/register` と `/auth/login` は認証不要。その他のエンドポイントは `Authorization: Bearer <token>` ヘッダーが必須。
- **エラーハンドリング**: 全エラーレスポンスは `ErrorResponse` スキーマ（code, message, details）で統一する。HTTP ステータスコードは 400（リクエストエラー）、401（認証エラー）、404（リソース未検出）、500（サーバーエラー）を使用する。
- **バージョニング**: 初期バージョンでは URL パスにバージョンを含めない（v1 相当）。将来のメジャー変更時に `/v2/` プレフィックスを導入する。
- **ページネーション**: `page` と `per_page` クエリパラメータによるオフセットベースのページネーション。レスポンスは `PaginatedResponse`（items, total, page, per_page）で統一する。

### エンドポイント一覧

| メソッド | パス | 説明 | 対応 FR |
|---------|------|------|---------|
| POST | /auth/register | ユーザー登録 | FR-007 |
| POST | /auth/login | ログイン（JWT 発行） | FR-007 |
| POST | /auth/logout | ログアウト | FR-007 |
| GET | /users/me | 自分のユーザー情報取得 | FR-007 |
| GET | /books | 書籍一覧取得 | FR-001 |
| POST | /books | 書籍登録（ISBN 自動取得対応） | FR-001 |
| GET | /books/{bookId} | 書籍詳細取得 | FR-001 |
| PUT | /books/{bookId} | 書籍情報更新 | FR-001 |
| DELETE | /books/{bookId} | 書籍削除 | FR-001 |
| GET | /books/search | 書籍検索（キーワード・複数条件） | FR-003 |
| GET | /books/{bookId}/tags | 書籍のタグ一覧取得 | FR-002 |
| PUT | /books/{bookId}/tags | 書籍のタグ設定（全置換） | FR-002 |
| GET | /tags | タグ一覧取得 | FR-002 |
| POST | /tags | タグ作成 | FR-002 |
| PUT | /tags/{tagId} | タグ更新 | FR-002 |
| DELETE | /tags/{tagId} | タグ削除 | FR-002 |
| GET | /categories | カテゴリ一覧取得 | FR-002 |
| POST | /categories | カテゴリ作成 | FR-002 |
| PUT | /categories/{categoryId} | カテゴリ更新 | FR-002 |
| DELETE | /categories/{categoryId} | カテゴリ削除 | FR-002 |
| GET | /loan-requests | 貸出リクエスト一覧取得 | FR-004 |
| POST | /loan-requests | 貸出リクエスト送信 | FR-004 |
| POST | /loan-requests/{requestId}/approve | 貸出リクエスト承認 | FR-004 |
| POST | /loan-requests/{requestId}/reject | 貸出リクエスト却下 | FR-004 |
| GET | /loans | 貸出一覧取得 | FR-005 |
| POST | /loans/{loanId}/return | 書籍返却 | FR-005 |
| GET | /loans/history | 貸出履歴取得 | FR-005 |
| GET | /loans/overdue | 延滞一覧取得 | FR-006 |

## 5. インフラ構成

### ローカル開発環境

Docker Compose で以下のコンテナを構成する:

- **app**: TypeScript + Express.js アプリケーション（ポート 3000）
- **db**: PostgreSQL 15（ポート 5432）
- **db-migration**: マイグレーション実行用（起動時に実行して終了）

### 本番環境（想定）

AWS ECS（Fargate）でのデプロイを想定する:

- **ECS Service**: Express.js アプリケーションコンテナ
- **RDS (PostgreSQL)**: マネージド PostgreSQL インスタンス
- **ALB**: ロードバランサー + ヘルスチェック

### 可用性方針（NFR-003: 99.5%）

- ECS タスクを最低2台で冗長化する
- RDS のマルチ AZ 配置を適用する
- ALB のヘルスチェックエンドポイント（`/health`）を設ける

## 6. セキュリティ設計

### 認証・認可

- **認証方式**: JWT Bearer トークン。`/auth/login` で発行し、Authorization ヘッダーで送信する。トークン有効期限は 24 時間とする。
- **認可方式**: RBAC（Role-Based Access Control）。`admin`（管理者）と `user`（一般利用者）の2ロールを定義する。

### ロール別アクセス制御

| 操作 | admin | user |
|------|-------|------|
| 書籍 CRUD | 全操作可 | 参照のみ |
| タグ・カテゴリ管理 | 全操作可 | 参照のみ |
| 貸出リクエスト送信 | 可 | 可 |
| 貸出リクエスト承認・却下 | 可 | 不可 |
| 全ユーザーの貸出一覧 | 可 | 自分のみ |
| 延滞一覧 | 可 | 自分のみ |

### パスワード管理（NFR-002）

- パスワードは bcrypt（コストファクター 10）でハッシュ化して保存する
- 平文パスワードはメモリ上でのみ扱い、ログに出力しない

### その他のセキュリティ対策

- CORS: 許可オリジンをホワイトリスト管理する
- Rate Limiting: API 全体に対してリクエストレート制限を適用する（同時 50 ユーザー対応、NFR-004）
- SQL インジェクション防止: パラメータ化クエリを使用する（ORM / Query Builder 経由）
- 入力バリデーション: リクエストボディ・パラメータの型・長さ・形式を検証する

## 7. 設計上の決定事項（ADR）

| # | 決定 | 理由 | 代替案 |
|---|------|------|--------|
| 1 | TypeScript + Express.js を採用 | constraints で指定。チーム内の技術スタックと一致 | NestJS（フレームワーク変更はスコープ外） |
| 2 | PostgreSQL 15+ を採用 | constraints で指定。全文検索（GIN インデックス）が検索性能要件（NFR-001）に有効 | MySQL（全文検索の日本語対応が弱い） |
| 3 | JWT Bearer 認証を採用 | FR-007 の acceptance_criteria で JWT が明示。ステートレスで水平スケーリングに有利 | セッションベース認証（スケーラビリティに不利） |
| 4 | オフセットベースのページネーション | 蔵書 10,000 冊規模（NFR-004）ではオフセット方式で十分な性能 | カーソルベース（小規模データでは過剰） |
| 5 | 貸出リクエスト→承認の2段階ワークフロー | FR-004 の acceptance_criteria で承認・却下プロセスが明示 | 即時貸出（要件に合致しない） |
| 6 | Docker Compose によるローカル開発環境 | constraints で指定。本番は AWS ECS を想定 | ネイティブインストール（環境差異が生じやすい） |

---
**生成元**: `requirements.json`
**生成日**: 2026-03-24
**生成 Skill**: `/gen-design`
