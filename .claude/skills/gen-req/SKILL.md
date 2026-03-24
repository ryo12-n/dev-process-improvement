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

#### 2a. request.md の存在確認

`PROJECT/request.md` が存在するか確認する（Read ツールで読み込みを試みる）。

- **存在しない場合**: 以下のメッセージを表示して処理を中止する:
  > エラー: `PROJECT/request.md` が見つかりません。
  > 要望書を作成してから再実行してください。テンプレートは `projects/_template/request.md` を参照してください。

#### 2b. request.md の内容チェック

読み込んだ `request.md` に以下の 8 セクションが存在し、各セクションにプレースホルダーではない具体的な内容が記述されているか確認する:

1. プロジェクト概要
2. 背景・動機
3. ユーザーストーリー
4. 機能要件（概要レベル）
5. 非機能要件
6. 技術制約・前提条件
7. 対象外（スコープ外）
8. 成功基準

- **空のセクションがある場合**: 警告を表示し、ユーザーに続行するか確認する:
  > 警告: 以下のセクションが未記入です: [セクション名一覧]
  > 未記入のセクションは要件に反映されません。このまま続行しますか？

---

### ステップ 3: 既存ファイルの上書き確認

`PROJECT/artifacts/requirements.json` または `PROJECT/artifacts/requirements.md` が既に存在し、かつプレースホルダーではない実質的な内容を含む場合、ユーザーに上書き確認を行う:

> `requirements.json` / `requirements.md` が既に存在します。上書きしてよいですか？
> - 上書きする場合: 「はい」と回答してください
> - 中止する場合: 「いいえ」と回答してください

**判定基準**: ファイルの `project.name` が空文字（JSON）、または `[プロジェクト名]` のままの場合はプレースホルダーとみなし、確認なしで上書きする。

---

### ステップ 4: 要件の抽出・構造化

`request.md` の内容を分析し、以下の観点で要件を抽出・構造化する。

#### 4a. プロジェクト情報の抽出

- セクション 1（プロジェクト概要）からプロジェクト名と概要説明を抽出する
- バージョンは `"0.1.0"` を初期値とする

#### 4b. 機能要件（FR）の抽出

セクション 3（ユーザーストーリー）とセクション 4（機能要件）を統合し、機能要件を抽出する。

各機能要件について以下を決定する:
- **ID**: `FR-001` からの連番
- **title**: 要件の簡潔なタイトル（日本語、20文字以内目安）
- **description**: 要件の詳細説明
- **priority**: `high` / `medium` / `low` — ユーザーストーリーでの言及頻度・成功基準との関連度で判断
- **user_stories**: 関連するユーザーストーリーの配列（`request.md` セクション 3 から対応するものを転記）
- **acceptance_criteria**: 受入基準の配列（ユーザーストーリーと機能要件の記述から具体的なテスト可能な基準を導出する）

**抽出のガイドライン**:
- セクション 4 の箇条書き 1 項目が原則 1 つの FR に対応する
- ただし、関連性が強い項目はグループ化してよい（例: CRUD 操作は 1 つの FR にまとめる）
- ユーザーストーリーは複数の FR に関連しうる（多対多の関係）
- 受入基準はテスト可能な形式で記述する（「〜できること」「〜が返されること」等）

#### 4c. 非機能要件（NFR）の抽出

セクション 5（非機能要件）から非機能要件を抽出する。

各非機能要件について以下を決定する:
- **ID**: `NFR-001` からの連番
- **category**: `performance` / `security` / `availability` / `scalability` / `maintainability` / `other`
- **title**: 要件の簡潔なタイトル
- **description**: 要件の詳細説明
- **metric**: 測定指標（例: 「レスポンスタイム」「稼働率」）
- **target**: 目標値（例: 「500ms以内」「99.5%」）

#### 4d. 制約事項・前提条件・スコープ外の抽出

- セクション 6（技術制約・前提条件）→ `constraints`（技術的な制約）と `assumptions`（前提条件）に分離する
  - 言語・フレームワーク・DB・インフラの指定 → `constraints`
  - 環境の前提（「チーム内利用」等）→ `assumptions`
- セクション 7（対象外）→ `out_of_scope`

各項目は文字列の配列として格納する。

---

### ステップ 5: requirements.json の生成

ステップ 4 で構造化した内容を、以下のスキーマに従って JSON ファイルとして生成する。

#### requirements.json スキーマ

```json
{
  "project": {
    "name": "<string: プロジェクト名>",
    "version": "<string: セマンティックバージョン（初期値 '0.1.0'）>",
    "description": "<string: プロジェクト概要（1〜3文）>"
  },
  "functional_requirements": [
    {
      "id": "<string: 'FR-NNN' 形式の連番>",
      "title": "<string: 要件タイトル>",
      "description": "<string: 要件の詳細説明>",
      "priority": "<string: 'high' | 'medium' | 'low'>",
      "user_stories": ["<string: ユーザーストーリー文>"],
      "acceptance_criteria": ["<string: 受入基準>"]
    }
  ],
  "non_functional_requirements": [
    {
      "id": "<string: 'NFR-NNN' 形式の連番>",
      "category": "<string: 'performance' | 'security' | 'availability' | 'scalability' | 'maintainability' | 'other'>",
      "title": "<string: 要件タイトル>",
      "description": "<string: 要件の詳細説明>",
      "metric": "<string: 測定指標>",
      "target": "<string: 目標値>"
    }
  ],
  "constraints": ["<string: 技術的制約>"],
  "assumptions": ["<string: 前提条件>"],
  "out_of_scope": ["<string: スコープ外項目>"]
}
```

**出力先**: `PROJECT/artifacts/requirements.json`

**注意事項**:
- JSON は整形済み（インデント 2 スペース）で出力する
- 文字列値に改行を含めない（改行が必要な場合は複数文に分割する）
- 空配列は `[]` として出力する（省略しない）

---

### ステップ 6: requirements.md の生成

ステップ 4 で構造化した内容を、以下のテンプレートに従って Markdown ファイルとして生成する。JSON と内容が一致していることを保証する。

#### requirements.md テンプレート

```markdown
# 要件定義書: <プロジェクト名>

> このファイルは `/gen-req` が `request.md` から自動生成しました。
> JSON（`requirements.json`）の人間向け可読版です。

---

## 1. プロジェクト情報

| 項目 | 値 |
|------|-----|
| プロジェクト名 | <project.name> |
| バージョン | <project.version> |
| 概要 | <project.description> |

## 2. 機能要件

<!-- FR ごとに以下のブロックを繰り返す -->

### <FR.id>: <FR.title>

- **説明**: <FR.description>
- **優先度**: <FR.priority>
- **ユーザーストーリー**:
  - <各 user_story を箇条書き>
- **受入基準**:
  - [ ] <各 acceptance_criteria をチェックボックス付き箇条書き>

## 3. 非機能要件

<!-- NFR ごとに以下のブロックを繰り返す -->

### <NFR.id>: <NFR.title>

- **カテゴリ**: <NFR.category>
- **説明**: <NFR.description>
- **メトリクス**: <NFR.metric>
- **目標値**: <NFR.target>

## 4. 制約事項

- <各 constraint を箇条書き>

## 5. 前提条件

- <各 assumption を箇条書き>

## 6. スコープ外

- <各 out_of_scope を箇条書き>

---
**生成元**: `request.md`
**生成日**: <YYYY-MM-DD>
**生成 Skill**: `/gen-req`
```

**出力先**: `PROJECT/artifacts/requirements.md`

---

### ステップ 7: 生成結果の報告

生成完了後、以下の形式でユーザーにサマリを報告する:

> **gen-req 完了**
>
> - **プロジェクト**: <プロジェクト名>
> - **機能要件**: <FR 件数> 件（high: X / medium: Y / low: Z）
> - **非機能要件**: <NFR 件数> 件
> - **制約事項**: <件数> 件
> - **前提条件**: <件数> 件
> - **スコープ外**: <件数> 件
>
> 生成ファイル:
> - `PROJECT/artifacts/requirements.json`
> - `PROJECT/artifacts/requirements.md`
>
> 次のステップ: `/gen-design PROJECT` で設計ドキュメントを生成できます。
