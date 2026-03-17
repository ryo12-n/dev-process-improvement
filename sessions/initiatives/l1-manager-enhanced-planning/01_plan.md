# 実施計画: l1-manager-enhanced-planning

## フェーズ構成

| 施策フェーズ | 内容 | 成功基準 |
|------------|------|----------|
| 1 | 計画ワーカー導入 + フェーズ再構築（基盤） | 計画ワーカーが 02a_task_division.md を出力し、L1が活用できる |
| 2 | 並列ワーカーディスパッチ | 独立タスクセットが同時実行される |
| 3 | ドメインエージェント深層統合 | Evaluator にドメインエージェントが注入され、有効性フィードバックが機能する |

## スケジュール

- 施策フェーズ1: 計画ワーカー導入 + フェーズ再構築
  - 新規: l2-plan-worker.md, l2-plan-evaluator.md, 02a_task_division.md テンプレート
  - 変更: SKILL.md, 02_tasks.md, 08_gate_review.md, manager-common-policy, workflow.md
- 施策フェーズ2: 並列ワーカーディスパッチ（施策フェーズ1のゲート通過後）
  - 新規: parallel-dev.md
  - 変更: SKILL.md, l2-worker.md, テンプレート群, manager-common-policy, session-flow-policy
- 施策フェーズ3: ドメインエージェント深層統合（施策フェーズ2のゲート通過後）
  - 変更: l2-evaluator.md, SKILL.md, manager-common-policy, テンプレート群, knowledge.md

## 成功基準（全体）

1. 計画ワーカーが `02a_task_division.md` を出力し、L1が02_tasks.mdの作成に活用できる
2. 並列ディスパッチが実施され、独立タスクセットが同時実行される
3. Evaluator にドメインエージェントが注入され、評価品質が向上する
4. ドメインエージェント有効性フィードバックが knowledge.md に記録される
5. 各フェーズ間でゲート判定が実施され、品質が段階的に確認される

## リソース・前提条件

- impl-plan-worker（`.claude/skills/l1-impl-manager/agents/impl-plan-worker.md`）を参考パターンとして使用
- 新しいフェーズ構造（Phase 1〜6）への移行は SKILL.md と全テンプレートの同期更新が必要
- manager-common-policy と session-flow-policy の整合性を保つ

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 計画ワーカーが低品質な出力を出す | 中 | 中 | Phase 2→3 ゲートで必ず検証。差し戻しフローを定義 |
| 並列ディスパッチでファイル衝突 | 低 | 高 | コンフリクトマトリクスによる事前検証 + L1の承認ゲート |
| ドメインエージェントがノイズになる | 中 | 低 | 有効性フィードバックで追跡し、不要なら施策単位で除外可能 |
| 全施策必須で小規模施策のオーバーヘッド増 | 高 | 中 | 計画ワーカーを軽量に設計（小規模施策では最小限の出力で済むようにする） |

---
**作成者**: L1
**作成日**: 2026-03-17
**最終更新**: 2026-03-17
