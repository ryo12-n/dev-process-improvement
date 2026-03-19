# GHA verdict 抽出と自動連鎖ディスパッチのステップ分離パターン

## 知見
GHA ワークフローで verdict 抽出と自動連鎖ディスパッチを実装する際、2つの処理を別ステップに分離することで、GitHub Actions のログ上で verdict の値と分岐結果が個別に確認でき、保守性・デバッグ性が向上する。

## 発見元
gha-pipeline-autorun 施策 L2-evaluator

## 適用先
GHA ワークフロー設計ガイドライン（`.claude/skills/gha-guideline/SKILL.md`）への追加候補

---
**起票日**: 2026-03-19
