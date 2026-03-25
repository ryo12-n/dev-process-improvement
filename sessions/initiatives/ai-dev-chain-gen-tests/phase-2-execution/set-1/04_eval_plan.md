# 評価計画: ai-dev-chain-gen-tests — Set-1

## 壁打ちフェーズ [2026-03-25 10:00]

### 理解のサマリー
- 評価の目的: gen-tests SKILL.md のプロンプト実装が正しく機能するかを、BookShelf API プロジェクトの requirements.json / openapi.yaml を入力として手動シミュレーション実行し検証する
- 評価スコープ: SKILL.md の処理フロー（ステップ1〜7）全体のシミュレーション実行と、生成成果物（tests.json / tests.md）の品質評価
- 完了条件: 8つの評価項目すべてに対して判定を行い、評価レポートを作成すること

### 前提条件チェック
- [x] 評価対象（SKILL.md）の完成度: 十分（ワーカーが実装済み）
- [x] 評価基準（02_plan.md の成功基準）の明確さ: 評価可能（8項目の判定基準が明確）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read / Write / Bash ツールが利用可能）
- [x] 参照ドメインエージェント: 指定なし → 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 参照ドメインエージェント

| エージェント名 | 参照パス | 評価への活用方針 |
|-------------|---------|---------------|
| なし | - | - |

## 評価対象

1. `/home/user/dev-process-improvement/.claude/skills/gen-tests/SKILL.md` — gen-tests スキルのプロンプト定義
2. 生成成果物: `projects/test-gen-req/artifacts/tests.json` / `tests.md`

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | tests.json が正常生成される | SKILL.md のスキーマに準拠した valid JSON が生成されるか確認 | project, test_suites, coverage_summary の全フィールドが存在し、型が正しいこと |
| 2 | tests.md が正常生成される | SKILL.md のテンプレートに準拠した Markdown が生成されるか確認 | テスト概要・カバレッジサマリ・トレーサビリティマトリクス・テストスイート詳細の全セクションが存在すること |
| 3 | TODO コメント不在 | SKILL.md 内の TODO コメントを Grep で検索 | TODO コメントが0件であること |
| 4 | FR トレーサビリティ | tests.json の related_requirements に FR-XXX が含まれるか確認 | 全テストケースの related_requirements に FR-XXX 形式の ID が1つ以上含まれること |
| 5 | NFR トレーサビリティ | tests.json の related_requirements に NFR-XXX が含まれるか確認 | NFR テストスイート内のテストケースに NFR-XXX 形式の ID が含まれること |
| 6 | エンドポイントカバレッジ | openapi.yaml の全 28 エンドポイントに対応するテストが存在するか確認 | 全エンドポイントに最低1つのテストケースが対応すること |
| 7 | coverage_summary の正確性 | coverage_summary の数値とテストケース実数を照合 | total_test_cases、by_type、by_priority の数値がテストケース実数と完全一致すること |
| 8 | JSON-Markdown 一致性 | tests.json と tests.md の内容を照合 | テストケース数・ID・タイトル・内容が一致していること |

## 評価スケジュール
- SKILL.md のバリデーションシミュレーション（ステップ2）
- テストケース導出シミュレーション（ステップ4a〜4d）
- tests.json / tests.md 生成（ステップ5〜6）
- 生成結果の評価（8項目）
- 評価ログ・レポート作成

## 前提・制約
- BookShelf API プロジェクトの requirements.json（FR 7件、NFR 4件）と openapi.yaml（28エンドポイント）を入力とする
- SKILL.md の処理フローを忠実にシミュレーションする（実際のスキル呼び出しではなく手動実行）

---
**作成者**: L2（評価）
**作成日**: 2026-03-25
