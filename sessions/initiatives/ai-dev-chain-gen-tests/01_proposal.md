# 改善施策提案: ai-dev-chain-gen-tests

## 背景・課題
ai-dev-chain の M5 マイルストーンとして `/gen-tests` Skill のプロンプト実装が定義されている。gen-req（BL-104）と gen-design（BL-105）が完了し、`requirements.json` と `openapi.yaml` の生成が可能になった。SKILL.md にはフレームワーク（7ステップ構造・入出力定義）が存在するが、ステップ4（テストケース導出）のプロンプト実装が TODO のまま残っている。また、test-gen-req プロジェクトの `backlog.md` チェーン進捗テーブルが初期状態のままで実態と乖離している。

## 目標
1. `/gen-tests` コマンドで `requirements.json` + `openapi.yaml` からテスト仕様（`tests.json` / `tests.md`）を自動生成できる状態にする
2. test-gen-req の `backlog.md` チェーン進捗テーブルを実態に合わせて更新する

## スコープ
### やること
- SKILL.md のステップ4（テストケース導出）プロンプト実装
- tests.json スキーマ定義の詳細化
- tests.md テンプレートの定義
- エラーハンドリング（前工程成果物の不在時）
- 上書き確認ロジック
- backlog.md チェーン進捗テーブルの更新（gen-req, gen-design を done に）

### やらないこと
- gen-ci / gen-tasks の実装（後続施策）
- テスト仕様の自動実行機能
- 新規プロジェクトでの検証（既存 test-gen-req で確認）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果
- gen-req → gen-design → gen-tests のチェーンが通しで動作する状態になる
- x-fr-id トレーサビリティにより、テストケースと FR の対応付けが自動検証可能になる
- BookShelf API で 7 FR + 4 NFR に対応するテストスイート（unit / integration / e2e）が生成される

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| テストケース導出ロジックの品質が不十分 | 中 | gen-req/gen-design の確立パターンを踏襲。評価者による品質チェック |
| tests.json スキーマがテンプレートと乖離 | 低 | projects/_template/artifacts/tests.json を基盤として使用 |

## 壁打ちの背景
- gen-req / gen-design と同じ7ステップパターンを踏襲する方針で合意
- backlog.md 更新は別施策にせず、本施策のタスクとして含める方針で合意
- 成功基準は「BookShelf API で tests.json / tests.md が正常生成」「SKILL.md に TODO が残っていない」

## 備考・設計パターン
gen-req / gen-design で確立した7ステップパターンを踏襲する。ステップ4のサブステップ構成は gen-tests 固有のテスト導出ロジックに合わせて設計する。

---
**起票者**: L1
**起票日**: 2026-03-24
**ステータス**: 承認済
**backlog元ファイル**: ai-dev-chain-gen-tests.md
