# 実施計画: 費用対効果評価フレームワークの標準化

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | 基底テンプレート作成・既存テンプレート連携・CLAUDE.md 更新 | 1セッション | SC-1〜SC-3 |

## スケジュール

単一フェーズの小規模施策。1 worker + 1 evaluator の逐次ディスパッチで完了する。

## 成功基準（全体）

1. **SC-1**: `.claude/templates/cost-effectiveness-evaluation.md` が存在し、T-003 の4軸定義（頻度・手動コスト・実装難易度）・算出式・レベル説明・評価テーブルテンプレート・カスタマイズ指針を含む
2. **SC-2**: `automation-candidates/_template.md` に基底テンプレートへの追跡コメントがあり、`grep -r "基底テンプレート .claude/templates/cost-effectiveness-evaluation.md" automation-candidates/` が結果を返す
3. **SC-3**: `CLAUDE.md` のディレクトリ構成テーブルと文書分類ポリシーテーブルに `.claude/templates/` の行が追加されている

## リソース・前提条件

- ソースフレームワーク: `sessions/initiatives/_archive/ai-automation-tool-review/04_work_report.md` T-003（L97-121）
- 既存消費者: `automation-candidates/_template.md`（L31-38）
- 対象リポジトリ: dev-process-improvement のみ

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 基底テンプレートの軸定義が既存テーブルと微妙に異なる | 低 | 低 | T-003 原文を忠実に転記し、AC テンプレートとの一致を検証する |

---
**作成者**: L1
**作成日**: 2026-03-17
**最終更新**: 2026-03-17
