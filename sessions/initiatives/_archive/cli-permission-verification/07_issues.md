# 課題メモ（施策内バッファ）: CLI環境での権限継承の再検証

> **このファイルの役割**: 施策実施中に気づいた課題・知見・リスクの一時メモ置き場。
> 施策完了（または定期レビュー）時に `プロセス改善_課題管理.csv` へ転記する

## 転記ルール

- 施策スコープ外・他の施策でも再発しうる課題 → **CSV に転記**
- 当施策内だけで完結する軽微な修正メモ → 転記不要（クローズ扱い）
- 転記済みの項目には `[転記済 ISS-XXX]` を末尾に追記する

---

## 未転記メモ

### [2026-03-08] deferred tools が tools フィールドの制限を迂回する
- **種別**: 知見
- **内容**: エージェント定義の `tools` フィールドで指定したツール以外でも、ToolSearch 経由の deferred tools（WebSearch, WebFetch, NotebookEdit, TaskCreate, EnterWorktree, CronCreate 等）は制限されず利用可能。tools フィールドは初期ロードツールの定義であり、deferred tools の制限メカニズムではない。
- **対応方針（案）**: tools フィールドは意図の文書化として維持する。完全なツール制限が必要な場合は `disallowedTools` の活用を検討する。ガイドに記載済み。
- **関連タスク**: T-004
[転記済 ISS-047]

### [2026-03-08] deny リスト設計時の Read/Write/Edit 網羅性チェック不足
- **種別**: 改善提案
- **内容**: settings.json の deny リストで `.env` や `secrets/` に対して Read と Write は deny していたが、Edit が deny されていなかった。Edit ツールでもファイル内容の変更が可能なため、機密ファイル保護には Read/Write/Edit の3ツールを全て deny する必要がある。
- **対応方針（案）**: 本施策で Edit deny パターンを追加済み。deny リスト変更時のチェック観点として「Read/Write/Edit の3ツール網羅性確認」を rule-change-checklist に追加することを提案。
- **関連タスク**: T-006
[転記済 ISS-048]

### [2026-03-08] [評価者] Write deny パターンの `*.pem`/`*.key` 欠落
- **種別**: 不具合（設定漏れ）
- **内容**: T-006 で Edit deny パターンを追加した際、Write 側の `Write(**/*.pem)` と `Write(**/*.key)` が追加されなかった。Read/Edit には `**/*.pem`/`**/*.key` の deny があるが Write にはない。ISS-048 で指摘した Read/Write/Edit 網羅性チェック不足と同種のパターンが、修正作業自体で再発している。
- **対応方針（案）**: settings.json に `Write(**/*.pem)`, `Write(**/*.key)` を追加する。施策内で完結する修正のため CSV 転記不要。
- **関連タスク**: T-006（評価 E-6 で検出）
転記不要（施策内完結の修正事項。根本原因は ISS-048 で起票済み）
