# 改善施策提案: batch-gha-minor-fixes

## 背景・課題
backlog-inventory-batch 施策で棚卸し・分類された78件のうち、GHA 関連の S 分類4件が未消化。
- `gha-skills-mapping.yml` に initiative ワークフロー4件のマッピングが未登録（CRITICAL ドリフト: ISS-063）
- GHA スキル6件に `disable-model-invocation` 設定が未追加（CLI でのコンテキスト消費・誤起動リスク）
- GHA ワークフロー間の責務移動検証パターンが評価テンプレートに未定義
- GHA スキル「やらないこと」セクションの用途クラス別テンプレートが未整備

## 目標
4件のバックログエントリを一括で消化し、GHA 関連の設定・ドキュメントの整合性を改善する。

## スコープ
### やること
- `gha-skills-mapping.yml` に initiative ワークフロー4件のマッピング追加（BL-080）
- GHA スキル6件に `disable-model-invocation: true` を frontmatter に追加（BL-069）
- `gha-guideline/SKILL.md` に責務移動の対検証パターンを追記（BL-081）
- `gha-guideline/SKILL.md` のセクション7.2 に用途クラス別「やらないこと」テンプレートを追記（BL-079）

### やらないこと
- GHA ワークフロー YAML の新規作成・ロジック変更
- 既存 GHA スキルの作業フロー・やることセクションの変更
- gha-skills-mapping.yml の構造・スキーマ変更

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果
- TG-010 CRITICAL ドリフト1件解消
- CLI セッションで ~600 トークンのコンテキスト予算節約
- GHA スキル変更施策の評価品質向上（責務移動検証パターンの制度化）
- 新規 GHA スキル作成時の判断効率化（用途クラス別テンプレート）

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| disable-model-invocation 設定がスキルの GHA 起動に影響 | 低 | GHA からは明示的に起動されるため影響なし（設定はモデル自動起動のみ抑制） |
| マッピング追加時の既存エントリとの不整合 | 低 | 既存マッピング構造を踏襲して追加 |

## 壁打ちの背景
- BL-069 の対象スキルは現時点の走査結果（gha-close, gha-execute, gha-guideline, gha-question, gha-test, gha-wallbash の6件）で確定
- BL-079 のテンプレート化は独立ファイルではなく `gha-guideline/SKILL.md` への追記方式で合意

---
**起票者**: L1
**起票日**: 2026-03-24
**ステータス**: 実施中
**backlog元ファイル**: gha-skills-disable-model-invocation.md, gha-skills-mapping-initiative-registration.md, gha-workflow-responsibility-transfer-verification.md, gha-skill-usage-class-template.md
