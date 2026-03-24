# 評価計画: ai-dev-chain-gen-req — Set-2

## 壁打ちフェーズ [2026-03-24 12:00]

### 理解のサマリー
- 評価の目的: gen-req Skill のプロンプト実装（M3）が成功基準を満たしているか、成果物の品質を評価する
- 評価スコープ: SKILL.md の処理フロー実装、requirements.json のスキーマ準拠、requirements.md の人間可読性、overview.md との整合性
- 完了条件: 06_eval_report.md に評価レポートが作成され、「評価中の知見」セクションに記載がある。課題転記が完了している

### 前提条件チェック
- [x] 評価対象（03_worker_report.md）の完成度: 十分（T-001〜T-005 全て完了、成果物一覧・知見記録あり）
- [x] 評価基準（02_plan.md の成功基準）の明確さ: 評価可能（4項目の成功基準が明確に定義）
- [x] 評価に必要なツール・アクセス権限: 確認済み（全成果物が Read 可能、python3 で JSON バリデーション可能）
- [x] 参照ドメインエージェント: 指定なし → 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 参照ドメインエージェント

| エージェント名 | 参照パス | 評価への活用方針 |
|-------------|---------|---------------|
| なし | - | 03_tasks.md に Evaluator 向けエージェント指定なし |

## 評価対象

- `.claude/skills/gen-req/SKILL.md` — 処理フロー（プロンプト）実装
- `projects/_template/artifacts/requirements.json` — 出力スキーマテンプレート
- `projects/_template/artifacts/requirements.md` — 出力テンプレート
- `projects/test-gen-req/request.md` — テスト用サンプル要望書
- `projects/test-gen-req/artifacts/requirements.json` — テスト生成結果（JSON）
- `projects/test-gen-req/artifacts/requirements.md` — テスト生成結果（MD）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | SKILL.md の TODO 残存 | Grep で TODO を検索 | TODO が 0 件 |
| 2 | SKILL.md の処理フロー完全性 | 目視レビュー: 7ステップが実行可能なプロンプトとして十分具体的か | 各ステップに入力・処理・出力・エラーハンドリングが明示されている |
| 3 | requirements.json のスキーマ準拠 | python3 で JSON パース + 全フィールド存在・型チェック | SKILL.md ステップ5 のスキーマ定義の全フィールドが存在し、値が適切な型 |
| 4 | requirements.json の内容品質 | request.md と突合: FR/NFR/制約/前提/スコープ外が要望書の情報を網羅しているか | request.md の 8 セクション全ての情報が適切に変換されている |
| 5 | requirements.md の人間可読性 | 目視レビュー: SKILL.md ステップ6 のテンプレートに準拠しているか | テンプレート構造に準拠し、内容が JSON と一致 |
| 6 | overview.md との整合性 | overview.md の入出力仕様と SKILL.md の引数・入力・出力の整合確認 | 入力: request.md、出力: requirements.json / requirements.md が一致 |
| 7 | テンプレート（_template/）の整合性 | _template の JSON/MD がスキーマ構造と一致するか | 空テンプレートが SKILL.md のスキーマと同一構造 |

## 評価スケジュール
- 評価項目 1〜7 を順に実施し、結果を 06_eval_report.md に記載する

## 前提・制約
- 動作テストの「再実行」は行わない（ワーカーの手動実行結果を成果物として評価する）
- SKILL.md のプロンプト品質は「構造・網羅性・具体性」の観点で評価し、実際の Claude 実行品質は評価スコープ外

---
**作成者**: L2（評価）
**作成日**: 2026-03-24
