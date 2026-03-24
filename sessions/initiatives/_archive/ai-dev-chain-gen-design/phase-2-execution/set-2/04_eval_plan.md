# 評価計画: ai-dev-chain-gen-design — Set-2

## 壁打ちフェーズ [2026-03-24 10:00]

### 理解のサマリー
- 評価の目的: gen-design Skill の成果物（SKILL.md、テンプレート、サンプル生成物）の品質検証
- 評価スコープ: SKILL.md 完成度、テンプレート整合性、サンプル品質、チェーン整合性の4観点
- 完了条件: 4観点すべての判定結果を 06_eval_report.md に記録し、知見テーブルに最低1行記載

### 前提条件チェック
- [x] 評価対象（03_worker_report.md）の完成度: 十分
- [x] 評価基準（02_plan.md の成功基準）の明確さ: 評価可能（L1 から4観点が明示指定）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read, Bash, Grep で全ファイル読み込み可能）
- [x] 参照ドメインエージェント: 指定なし → 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 参照ドメインエージェント
なし

## 評価対象
1. `.claude/skills/gen-design/SKILL.md` — 処理フロー（7ステップ）のプロンプト実装
2. `projects/_template/artifacts/openapi.yaml` — テンプレート
3. `projects/_template/artifacts/design.md` — テンプレート
4. `projects/test-gen-req/artifacts/openapi.yaml` — サンプル生成 API 設計書
5. `projects/test-gen-req/artifacts/design.md` — サンプル生成設計ドキュメント
6. `projects/test-gen-req/artifacts/requirements.json` — 入力要件定義

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | SKILL.md の完成度 | 7ステップの処理フロー確認、TODO 残存チェック、gen-req との構造整合性確認 | TODO なし、全ステップが実行可能な詳細度 |
| 2 | テンプレート整合性 | テンプレートと SKILL.md ステップ5/6 の構造比較 | テンプレートが SKILL.md の出力構造と一致 |
| 3 | サンプル生成結果の品質 | YAML バリデーション、FR/NFR 対応検証、$ref 解決確認、x-fr-id トレーサビリティ確認 | OpenAPI 3.0.3 準拠、全 FR/NFR マッピング完了 |
| 4 | チェーン整合性 | gen-req/gen-tests/gen-tasks の入出力パス・形式との整合確認 | 前後工程の Skill と入出力パス・形式が一致 |

## 評価スケジュール
- 2026-03-24: 全4項目の評価実施・レポート作成

## 前提・制約
- 成果物のファイル読み込みによる静的検証が中心（実際の Skill 実行テストは対象外）

---
**作成者**: L2（評価）
**作成日**: 2026-03-24
