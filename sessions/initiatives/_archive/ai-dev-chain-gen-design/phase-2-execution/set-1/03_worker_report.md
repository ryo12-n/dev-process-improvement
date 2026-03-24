# 作業レポート: ai-dev-chain-gen-design — Set-1

## サマリ

T-002〜T-005 を完了した。テンプレート（openapi.yaml / design.md）を SKILL.md のプロンプト定義と整合させ、test-gen-req の requirements.json からサンプル設計ドキュメントを生成した。生成物は OpenAPI 3.0.3 準拠の有効な YAML であり、28 エンドポイント・6 主要エンティティ・全 FR/NFR のトレーサビリティが確保されている。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | SKILL.md プロンプト実装 | 前セッション | 前セッション完了 | 前セッションで完了済み |
| T-002 | テンプレート更新 | テンプレート2ファイルを SKILL.md と整合 | 完了 | openapi.yaml: 共通スキーマ・セキュリティ・エラーレスポンス追加。design.md: 7セクション構成・メタ情報を SKILL.md テンプレートと完全一致 |
| T-003 | サンプルデータ動作テスト | requirements.json → openapi.yaml + design.md 生成 | 完了 | 28 エンドポイント、13 スキーマ（6主要エンティティ+リクエスト/レスポンス+共通）、YAML バリデーション通過 |
| T-004 | 知見記録 | レポート作成 | 完了 | 本レポート |
| T-005 | 課題転記 | 未転記課題確認 | 完了 | 未転記課題なし。新規 ISS 作成不要 |

## 成果物一覧

- `projects/_template/artifacts/openapi.yaml` — テンプレート更新（SKILL.md ステップ5 整合）
- `projects/_template/artifacts/design.md` — テンプレート更新（SKILL.md ステップ6 整合）
- `projects/test-gen-req/artifacts/openapi.yaml` — サンプル生成物（BookShelf API、28エンドポイント）
- `projects/test-gen-req/artifacts/design.md` — サンプル生成物（BookShelf API、7セクション設計書）

## 発生した課題

なし。07_issues.md に未転記メモなし。

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | テンプレートと SKILL.md の構造定義は厳密に同期すべき | T-002 | `projects/_template/artifacts/`, SKILL.md | テンプレートが SKILL.md の構造定義と乖離していると、生成時にどちらを正とするか判断が必要になる。SKILL.md 側を正（Source of Truth）とし、テンプレートはプレースホルダーとして SKILL.md の構造を反映する方針が適切 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | acceptance_criteria の動詞→HTTPメソッド変換は高精度で機械的に実行可能 | T-003 ステップ4a | FR-001〜FR-007 の acceptance_criteria から 28 エンドポイントを導出した。「登録できる→POST」「取得できる→GET」「更新できる→PUT」「削除できる→DELETE」の対応は SKILL.md の導出ルール通りに明確に決まった |
| 2 | ワークフロー系 FR（FR-004 貸出リクエスト→承認）はエンティティ分離の設計判断が必要 | T-003 ステップ4b | LoanRequest（リクエスト）と Loan（貸出レコード）を分離するか統合するかの判断が必要だった。承認時に Loan が作成されるワークフローを考慮し、分離を選択した。この種の設計判断は SKILL.md のルールだけでは自動化しきれず、ドメイン理解が必要 |

## 所感・次フェーズへの申し送り

- テンプレートと SKILL.md の整合は完了。gen-design スキルの Skill 実装として必要なプロンプト・テンプレート・サンプルが揃った状態
- サンプル生成物（BookShelf API）は実際のプロジェクトに近い複雑度（7 FR、4 NFR、5 constraints）で検証できた
- 後工程（/gen-tests、/gen-tasks）の入力として openapi.yaml が利用可能な状態

---
**作成者**: L2（実施）
**作成日**: 2026-03-24
