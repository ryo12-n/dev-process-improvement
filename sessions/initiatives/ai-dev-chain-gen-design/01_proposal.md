# 改善施策提案: ai-dev-chain-gen-design

## 背景・課題

ai-dev-chain-gen-req 施策（M3）で、`/gen-req` スキルのプロンプト実装が完了し、`request.md` から `requirements.json` / `requirements.md` を自動生成できる状態になった。次工程の `/gen-design` は SKILL.md に処理フローの枠組みと TODO リストがあるが、実際のプロンプト実装がなく、`/gen-design` を実行しても設計ドキュメントは生成されない。

overview.md のマイルストーン M4 として `gen-design` Skill の中身実装が次のステップとして定義されている。

## 目標

- `/gen-design projects/<name>` コマンドで `requirements.json` から `openapi.yaml` / `design.md` を実際に生成できる状態にする
- `projects/test-gen-req/` の既存サンプルデータを使った動作テストで正常に生成されることを確認する
- overview.md の入出力仕様と整合した実装であることを確認する

## スコープ
### やること
- `gen-design/SKILL.md` の処理フロー（プロンプト）を実装する
- `openapi.yaml` の生成ガイド（OpenAPI 3.0.3 準拠）を確定する
- `design.md` の生成テンプレートを確定する（アーキテクチャ・データモデル・コンポーネント構成・API 設計方針・セキュリティ設計・ADR）
- バリデーション（`requirements.json` 不在時のエラーハンドリング）を実装する
- 既存成果物がある場合の上書き確認ロジックを実装する
- `projects/test-gen-req/` のサンプルデータで動作テストを実施する

### やらないこと
- 他の gen-* Skills（gen-tests / gen-ci / gen-tasks）の実装
- E2E チェーン全体の通し確認（M8）
- `projects/_template/` の構造変更（bootstrap で確定済み）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- `/gen-design` コマンド1つで要件定義から API 設計書と設計ドキュメントが生成され、手動での設計作業が不要になる
- 後工程（`/gen-tests`、`/gen-tasks`）への入力が標準フォーマットで供給されるようになる
- gen-req で確立したチェーン型 Skill のプロンプト設計パターンを踏襲し、一貫した品質を確保する

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| 要件の抽象度が高い場合に設計の具体性がばらつく | 中 | プロンプトに構造化ガイドラインを含め、制約（constraints）をアーキテクチャ決定の根拠として明示的に活用する |
| openapi.yaml のスキーマ変更が後工程に影響する | 低 | 現行テンプレート構造をベースとし、OpenAPI 3.0.3 標準に準拠する |
| FR から API エンドポイントへの対応付けが不正確になる可能性 | 中 | FR の acceptance_criteria を API 仕様の根拠として活用し、トレーサビリティを確保する |

## 壁打ちの背景

- gen-req で確立した 7 ステップ構造（引数取得 → バリデーション → 上書き確認 → データ抽出 → 生成1 → 生成2 → レポート）を踏襲する
- 動作テストは `projects/test-gen-req/artifacts/requirements.json`（BookShelf API）を入力として使用する
- SDK 環境のため `claude/l1-manager-al7in` ブランチを施策ブランチとして使用
- gen-req の知見: user_stories が空配列の FR が存在しうる → エンドポイント導出時に acceptance_criteria を主な根拠として活用する

## 備考・設計パターン

gen-req に続くチェーン型 Skill の 2 番目の実装であり、gen-req で確立したパターンの再現性を検証する意味もある。ここで確立した「要件 → 設計」の導出プロンプトは、後続の gen-tests / gen-tasks でも同様の構造化アプローチの参考になる。

---
**起票者**: L1
**起票日**: 2026-03-24
**ステータス**: 実施中
**backlog元ファイル**: なし
