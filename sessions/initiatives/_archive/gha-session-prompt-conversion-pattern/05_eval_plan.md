# 評価計画: GHA セッションプロンプト変換パターンガイド

## 壁打ちフェーズ [2026-03-15]

### 理解のサマリー
- 評価の目的: `gha-guideline/SKILL.md` に追加されたセクション7「セッションプロンプト変換パターン」の品質を、既存GHAスキル実装との整合性・テンプレート実用性・参照正確性・docs整合性の観点から評価する
- 評価スコープ: セクション7（7.1〜7.5）の内容、frontmatter更新、関連ファイル一覧更新、docs/workflow.md連動更新
- 完了条件: 01_plan.md の成功基準6項目に対する達成度判定が完了し、06_eval_report.md に記載されている

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク完了、知見記録・メタルール検証結果を含む）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（6項目すべて具体的で検証可能）
- [x] 評価に必要なツール・アクセス権限: 確認済み（対象ファイル・参照実装・knowledge.md すべてアクセス可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.claude/skills/gha-guideline/SKILL.md` セクション7（L268〜L367）
- `.claude/skills/gha-guideline/SKILL.md` frontmatter description
- `.claude/skills/gha-guideline/SKILL.md` 関連ファイル一覧
- `docs/workflow.md` のセクション7への参照行

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-1 | セクション7の内容が既存GHAスキル実装と整合しているか | 既存5スキル（wallbash/execute/close/question/test）の構造と7.2テンプレートを照合 | テンプレートの必須セクション・共通4項目が既存スキルの実装パターンを正確に反映している |
| E-2 | テンプレートの実用性 | 7.2のGHA SKILL.mdテンプレートと7.3のYAMLプロンプトテンプレートが、新規GHAスキル作成時のガイドとして十分か検証 | テンプレートに従えば既存スキルと同等の構造を持つスキルが作成できる |
| E-3 | アンチパターンのknowledge.md参照番号の正確性 | 7.5のアンチパターン表の各エントリ番号（#10, #12, #14, #15, #16, #17, #18）がknowledge.mdに実在し、内容が一致するか検証 | 全参照番号が実在し、アンチパターン表の説明がknowledge.mdの内容と整合している |
| E-4 | docs/workflow.mdとの整合性 | docs/workflow.mdにセクション7への参照が追加されているか確認 | 設計方針セクションにセクション7への参照リンクが存在する |
| E-5 | frontmatter descriptionの更新 | frontmatter descriptionが更新されているか確認 | 「変換パターン」に関する記述がdescriptionに含まれている |
| E-6 | 関連ファイル一覧の更新 | gha-test/SKILL.mdが関連ファイル一覧に追加されているか確認 | gha-test/SKILL.mdのエントリがテーブルに存在する |
| E-7 | メタルール横断検証（条件付き） | .claude/skills/配下の変更であるため、フロー記述整合性・workflow.md同期・TG-008基準連動を確認 | 3領域の検証結果が妥当であること |

## 評価スケジュール
- E-1〜E-7 を順に実施（単一セッション内で完了）

## 前提・制約
- 参照実装: `gha-wallbash/SKILL.md` + `initiative-wallbash.yml`
- knowledge.md: `refs/claude-code-action/knowledge.md`
- 01_plan.md の成功基準6項目に対して評価する

---
**作成者**: L2（評価）
**作成日**: 2026-03-15
