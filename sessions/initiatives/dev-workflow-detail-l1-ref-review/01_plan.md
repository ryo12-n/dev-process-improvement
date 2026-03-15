# 実施計画: dev-workflow-detail L1参照精査

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | `dev-workflow-detail.md` の L1 参照を全て特定し、`manager-common-policy` の L1 定義と照合して修正要否を判断する | 1セッション | 残存参照の全件が「変更要」「変更不要（設計意図通り）」に分類されている |

## スケジュール

- Phase A: タスクリスト作成・Worker ディスパッチ
- Phase B: Worker によるファイル調査・照合・レポート作成
- Phase C: Evaluator による評価
- Phase D: ゲート判定・クローズ準備

## 成功基準（全体）

1. `ai-driven-dev-patterns/docs/design/dev-workflow-detail.md` の全 L1 参照（grep で確認）が精査済みである
2. 各参照について「`manager-common-policy` の L1 定義との整合性」が文書化されている
3. 変更が必要な参照については修正が完了している（または変更不要と判断された根拠が明記されている）

## リソース・前提条件

- `manager-common-policy` SKILL.md（`.claude/skills/manager-common-policy/SKILL.md`）: L1 の定義確認に使用
- `dev-workflow-detail.md`（`ai-driven-dev-patterns/docs/design/`）: 精査対象。GHA 環境では `gh api` 経由でアクセス可能
- 外部リポジトリアクセス: `gh api repos/ryo12-n/ai-driven-dev-patterns/contents/docs/design/dev-workflow-detail.md` で参照可能

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| GHA 環境で ai-driven-dev-patterns にアクセス不可 | 低 | 高 | `gh api` コマンドで内容を取得する |
| `manager-common-policy` の L1 定義が曖昧で判断基準が定まらない | 低 | 中 | 定義確認後に精査基準を明文化してから作業を進める |
| 変更不要と判断したが実際は変更が必要なケースを見落とす | 低 | 中 | Evaluator フェーズで独立したレビューを実施する |

---
**作成者**: L1
**作成日**: 2026-03-15
**最終更新**: 2026-03-15
