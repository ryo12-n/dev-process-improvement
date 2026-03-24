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
2. `functional_requirements` — 空配列でないこと（1件以上の FR が必要）

- **必須フィールドが不足・空の場合**: 以下のメッセージを表示して処理を中止する:
  > エラー: `requirements.json` の内容が不十分です。不足フィールド: [フィールド名一覧]
  > `/gen-req PROJECT` で要件定義を再生成してください。

#### 2c. openapi.yaml の存在確認

`PROJECT/artifacts/openapi.yaml` が存在するか確認する（Read ツールで読み込みを試みる）。

- **存在しない場合**: 以下のメッセージを表示して処理を中止する:
  > エラー: `PROJECT/artifacts/openapi.yaml` が見つかりません。
  > 先に `/gen-design PROJECT` を実行して設計ドキュメントを生成してください。

#### 2d. openapi.yaml の内容チェック

読み込んだ `openapi.yaml` に以下の必須フィールドが存在し、プレースホルダーでないことを確認する:

1. `info.title` — `"[プロジェクト名] API"` のままでないこと
2. `paths` — 空でないこと（1件以上のエンドポイントが必要）

- **必須フィールドが不足・プレースホルダーの場合**: 以下のメッセージを表示して処理を中止する:
  > エラー: `openapi.yaml` の内容が不十分です。不足フィールド: [フィールド名一覧]
  > `/gen-design PROJECT` で設計ドキュメントを再生成してください。

---

### ステップ 3: 既存ファイルの上書き確認

`PROJECT/artifacts/tests.json` または `PROJECT/artifacts/tests.md` が既に存在し、かつプレースホルダーではない実質的な内容を含む場合、ユーザーに上書き確認を行う:

> `tests.json` / `tests.md` が既に存在します。上書きしてよいですか？
> - 上書きする場合: 「はい」と回答してください
> - 中止する場合: 「いいえ」と回答してください

**判定基準**: `project.name` が空文字（JSON）、または `test_suites` が空配列の場合はプレースホルダーとみなし、確認なしで上書きする。

---

### ステップ 4: テストケースの導出

`requirements.json` と `openapi.yaml` の内容を分析し、テストスイート・テストケースを導出する。以下の 4 サブステップで導出する。

#### 4a. 機能要件（FR）→ テストケース導出

各 `functional_requirements` の `acceptance_criteria` を分析し、機能テストケースを導出する。

**導出ルール**:
- 各 FR の `acceptance_criteria` 1 項目につき、原則 1 つ以上のテストケースを作成する
- テストケースの `related_requirements` に対応する FR ID を記録する（トレーサビリティ）
- テストの種別（`type`）は以下の基準で決定する:
  - 単一機能の確認 → `unit`
  - 複数コンポーネント連携の確認 → `integration`
  - ユーザーシナリオ全体の確認 → `e2e`
- 各テストケースについて以下を決定する:
  - **id**: `TC-001` からの連番
  - **title**: テストの簡潔なタイトル（日本語、30文字以内目安）
  - **description**: テスト内容の詳細説明
  - **preconditions**: テスト実行の前提条件（データ準備・状態設定等）
  - **steps**: テスト手順のステップ配列
  - **expected_result**: 期待される結果
  - **priority**: `high` / `medium` / `low` — FR の priority を継承する

**正常系・異常系の網羅**:
- 各 acceptance_criteria に対して、正常系テストケースを必ず 1 件作成する
- 入力バリデーション・権限チェック等が含意される場合は、異常系テストケースも作成する
  - 必須項目未入力 → バリデーションエラーのテスト
  - 認証・認可が必要 → 未認証/権限不足のテスト
  - 存在しないリソースへのアクセス → 404 エラーのテスト

#### 4b. エンドポイント → API テスト導出

`openapi.yaml` の `paths` を走査し、API レベルのテストケースを導出する。

**導出ルール**:
- 各エンドポイント（メソッド + パス）につき、以下のテストケースを作成する:
  - **正常系**: 正しいリクエストに対して期待されるレスポンス（ステータスコード・ボディ）が返ることを確認
  - **バリデーションエラー**: 不正なリクエストボディ・パラメータに対して `400` が返ることを確認
  - **認証エラー**: `security` が設定されたエンドポイントに対して、認証なしで `401` が返ることを確認
  - **存在しないリソース**: パスパラメータ `{id}` を持つエンドポイントに対して、存在しない ID で `404` が返ることを確認
- テストの `type` は `integration` を基本とする
- エンドポイントの `x-fr-id` カスタム拡張を `related_requirements` に転記する（トレーサビリティ）
- 4a で既に同等のテストケースが導出されている場合は重複を排除する（同一の acceptance_criteria と endpoint の組み合わせ）

#### 4c. 非機能要件（NFR）→ 非機能テスト導出

`non_functional_requirements` を分析し、非機能テストケースを導出する。

**導出ルール**:
- NFR の `category` に応じてテストの種類を決定する:
  - `performance` → パフォーマンステスト（レスポンスタイム計測、負荷テスト）
  - `security` → セキュリティテスト（脆弱性チェック、認証テスト、SQLインジェクション等）
  - `availability` → 可用性テスト（ヘルスチェック、障害復旧）
  - `scalability` → スケーラビリティテスト（同時接続、スループット）
  - `maintainability` → コード品質テスト（静的解析、テストカバレッジ）
  - `other` → その他テスト（NFR の description に基づき判断）
- 各テストケースの `expected_result` に NFR の `metric` と `target` を反映する
  - 例: NFR の metric が「レスポンスタイム」、target が「500ms以内」→ expected_result: 「レスポンスタイムが500ms以内であること」
- テストの `type` は `performance` / `security` / `e2e` のいずれかを設定する
- `related_requirements` に対応する NFR ID を記録する

#### 4d. カバレッジ分析

4a〜4c で導出したテストケースの網羅性を分析する。

**分析項目**:
- **FR カバレッジ**: 全 FR の acceptance_criteria がテストケースでカバーされていることを確認する
  - 未カバーの acceptance_criteria がある場合、追加テストケースを作成する
- **エンドポイントカバレッジ**: 全エンドポイント（メソッド + パス）がテストケースでカバーされていることを確認する
  - 未カバーのエンドポイントがある場合、追加テストケースを作成する
- **NFR カバレッジ**: 全 NFR がテストケースでカバーされていることを確認する
  - metric/target が定量的な NFR は必ずテストケースを持つことを保証する

**カバレッジ目標**:
- `unit`: FR の acceptance_criteria カバー率 80% 以上
- `integration`: 全エンドポイントに正常系・異常系テスト
- `e2e`: 主要ユーザーシナリオ（high priority の FR に対応するフロー）をカバー

---

### ステップ 5: tests.json の生成

ステップ 4 で導出したテストケースを、以下のスキーマに従って JSON ファイルとして生成する。

#### tests.json スキーマ

```json
{
  "project": {
    "name": "<string: プロジェクト名（requirements.json から転記）>",
    "version": "<string: セマンティックバージョン（requirements.json から転記）>"
  },
  "test_suites": [
    {
      "id": "<string: 'TS-NNN' 形式の連番>",
      "name": "<string: テストスイート名>",
      "type": "<string: 'unit' | 'integration' | 'e2e' | 'performance' | 'security'>",
      "target_component": "<string: テスト対象コンポーネント名（エンドポイントパス、モジュール名等）>",
      "test_cases": [
        {
          "id": "<string: 'TC-NNN' 形式の連番（全スイート通しで一意）>",
          "title": "<string: テストケースタイトル>",
          "description": "<string: テスト内容の詳細説明>",
          "preconditions": ["<string: 前提条件>"],
          "steps": ["<string: テスト手順の各ステップ>"],
          "expected_result": "<string: 期待される結果>",
          "priority": "<string: 'high' | 'medium' | 'low'>",
          "related_requirements": ["<string: 'FR-NNN' または 'NFR-NNN' 形式の関連要件 ID>"]
        }
      ]
    }
  ],
  "coverage_summary": {
    "total_test_cases": "<number: テストケース総数>",
    "by_type": {
      "unit": "<number: unit テスト数>",
      "integration": "<number: integration テスト数>",
      "e2e": "<number: e2e テスト数>",
      "performance": "<number: performance テスト数>",
      "security": "<number: security テスト数>"
    },
    "by_priority": {
      "high": "<number: high 優先度テスト数>",
      "medium": "<number: medium 優先度テスト数>",
      "low": "<number: low 優先度テスト数>"
    },
    "requirement_coverage": {
      "functional": {
        "total_requirements": "<number: FR 総数>",
        "covered_requirements": "<number: テストケースが紐づく FR 数>",
        "coverage_rate": "<string: カバー率（例: '100%'）>"
      },
      "non_functional": {
        "total_requirements": "<number: NFR 総数>",
        "covered_requirements": "<number: テストケースが紐づく NFR 数>",
        "coverage_rate": "<string: カバー率（例: '100%'）>"
      }
    },
    "endpoint_coverage": {
      "total_endpoints": "<number: openapi.yaml のエンドポイント総数>",
      "covered_endpoints": "<number: テストケースが紐づくエンドポイント数>",
      "coverage_rate": "<string: カバー率（例: '100%'）>"
    }
  }
}
```

**出力先**: `PROJECT/artifacts/tests.json`

**テストスイートの構成ルール**:
- テストスイートはテストの `type` とテスト対象の組み合わせでグループ化する
  - 例: `TS-001: Books API - unit`, `TS-002: Books API - integration`, `TS-003: Performance Tests`
- `target_component` はテスト対象を識別できる粒度で記述する（エンドポイントパス `/books`、モジュール名等）
- テストケース ID（`TC-NNN`）は全スイート通しで一意な連番とする

**注意事項**:
- JSON は整形済み（インデント 2 スペース）で出力する
- 文字列値に改行を含めない（改行が必要な場合は複数文に分割する）
- 空配列は `[]` として出力する（省略しない）

---

### ステップ 6: tests.md の生成

ステップ 4 で導出したテストケースを、以下のテンプレートに従って Markdown ファイルとして生成する。JSON と内容が一致していることを保証する。

#### tests.md テンプレート

````markdown
# テスト仕様書: <プロジェクト名>

> このファイルは `/gen-tests` が `requirements.json` と `openapi.yaml` から自動生成しました。
> JSON（`tests.json`）の人間向け可読版です。

---

## 1. テスト概要

| 項目 | 値 |
|------|-----|
| プロジェクト名 | <project.name> |
| バージョン | <project.version> |
| テストケース総数 | <total_test_cases> 件 |
| テスト種別内訳 | unit: X / integration: Y / e2e: Z / performance: P / security: S |

## 2. カバレッジサマリ

### 要件カバレッジ

| 分類 | 総数 | カバー数 | カバー率 |
|------|------|---------|---------|
| 機能要件（FR） | <total> | <covered> | <rate> |
| 非機能要件（NFR） | <total> | <covered> | <rate> |

### エンドポイントカバレッジ

| 総数 | カバー数 | カバー率 |
|------|---------|---------|
| <total> | <covered> | <rate> |

### FR-テストケース トレーサビリティマトリクス

| FR ID | FR タイトル | テストケース ID | カバー状態 |
|-------|-----------|----------------|-----------|
<!-- 各 FR に対応するテストケースを一覧化。未カバーの FR は「未カバー」と表示 -->

## 3. テストスイート詳細

<!-- テストスイートごとに以下のブロックを繰り返す -->

### <TS.id>: <TS.name>

- **種別**: <TS.type>
- **対象コンポーネント**: <TS.target_component>

<!-- テストケースごとに以下を繰り返す -->

#### <TC.id>: <TC.title>

- **説明**: <TC.description>
- **優先度**: <TC.priority>
- **関連要件**: <TC.related_requirements を ', ' 区切りで表示>
- **前提条件**:
  - <各 precondition を箇条書き>
- **テスト手順**:
  1. <各 step を番号付きリストで表示>
- **期待結果**: <TC.expected_result>

---
**生成元**: `requirements.json`, `openapi.yaml`
**生成日**: <YYYY-MM-DD>
**生成 Skill**: `/gen-tests`
````

**出力先**: `PROJECT/artifacts/tests.md`

---

### ステップ 7: 生成結果の報告

生成完了後、以下の形式でユーザーにサマリを報告する:

> **gen-tests 完了**
>
> - **プロジェクト**: <プロジェクト名>
> - **テストケース総数**: <total_test_cases> 件
> - **種別内訳**: unit: X / integration: Y / e2e: Z / performance: P / security: S
> - **優先度内訳**: high: X / medium: Y / low: Z
> - **FR カバレッジ**: <covered>/<total> (<rate>)
> - **NFR カバレッジ**: <covered>/<total> (<rate>)
> - **エンドポイントカバレッジ**: <covered>/<total> (<rate>)
>
> 生成ファイル:
> - `PROJECT/artifacts/tests.json`
> - `PROJECT/artifacts/tests.md`
>
> 次のステップ: `/gen-ci PROJECT` で CI パイプラインを生成、または `/gen-tasks PROJECT` でタスクを生成できます。
