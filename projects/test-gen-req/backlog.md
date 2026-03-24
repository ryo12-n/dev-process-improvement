# バックログ: [プロジェクト名]

> このファイルは AI（Skills チェーン）が自動更新する進捗管理テーブルです。
> 人間が直接編集することも可能ですが、`/gen-tasks` 実行時に自動更新されます。

---

## ステータス定義

| ステータス | 意味 | 更新タイミング |
|-----------|------|--------------|
| `pending` | 未着手 | `/gen-tasks` でタスク生成時 |
| `in_progress` | 作業中 | 実装ワーカーが着手時 |
| `review` | レビュー待ち | 実装完了・PR 作成時 |
| `done` | 完了 | レビュー承認・マージ後 |
| `blocked` | ブロック中 | 依存タスクや外部要因で停止時 |

## 更新ルール

1. **ステータス遷移**: `pending` → `in_progress` → `review` → `done`（逆行禁止）
2. **ブロック**: 任意のステータスから `blocked` に遷移可。解消後は元のステータスに戻す
3. **自動更新**: `/gen-tasks` 実行時に `tasks.json` からこのテーブルを再生成する。手動追記した行は `source: manual` で保護される
4. **優先度**: `high` > `medium` > `low`。実装順序は依存関係を優先する

## チェーン進捗

| フェーズ | Skill | 成果物 | ステータス | 最終実行日 |
|---------|-------|--------|-----------|-----------|
| 要件定義 | `/gen-req` | `artifacts/requirements.json`, `artifacts/requirements.md` | `done` | 2026-03-24 |
| 設計 | `/gen-design` | `artifacts/openapi.yaml`, `artifacts/design.md` | `done` | 2026-03-24 |
| テスト設計 | `/gen-tests` | `artifacts/tests.json`, `artifacts/tests.md` | `pending` | - |
| CI 設計 | `/gen-ci` | `artifacts/ci/pipeline.yaml` | `pending` | - |
| タスク生成 | `/gen-tasks` | `artifacts/tasks.json` | `pending` | - |

## タスク一覧

<!-- /gen-tasks 実行時に自動生成される。手動追記する場合は source: manual を付与すること -->

| ID | タイトル | 優先度 | ステータス | 依存 | 担当 | source |
|----|---------|--------|-----------|------|------|--------|
| <!-- T-001 --> | <!-- タスク名 --> | <!-- high/medium/low --> | `pending` | <!-- T-XXX --> | <!-- - --> | `auto` |

---
**最終更新**: 2026-03-24
**更新者**: system
