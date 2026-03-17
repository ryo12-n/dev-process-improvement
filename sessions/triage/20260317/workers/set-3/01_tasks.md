# ワーカータスク指示: Set-3

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-002 | backlog | 施策化済みチェック。完了/進行中エントリの突合。対象リポジトリ未記入チェック | 削除・クローズ候補リスト確定 |
| TG-005 | backlog | backlog アイテム間の関係性（重複候補・依存関係・統合候補）を横断分析する | 分析結果テーブルが記載されている |
| TG-006 | rules/workflow | ルール・workflow 整合性チェック。参考資料ステータスチェック。README 整合性チェック | 乖離の検出・修正完了 |
| TG-008 | skills/agents | セッション構造標準ポリシーチェック（差分のみ） | チェック結果記録 |

## 走査時の注意事項

- TG-002 → TG-005 の論理順序を維持すること（TG-005 は TG-002 の削除・統合候補リストに依存）
- TG-006 と TG-008 は TG-002/TG-005 と独立して実施可
- backlog 84件（BL-001〜BL-083、BL-076/077 に重複採番あり）
- 対象リポジトリ未記入エントリが約31件（主に BL-037〜BL-075）
- 完了ステータス 3件: BL-002, BL-031, BL-064
- 進行中 1件: BL-020
- TG-002 の施策化済みチェック手順:
  1. backlog.csv の「施策ディレクトリ名」列が記入済み → sessions/initiatives/ および _archive/ で直接照合
  2. 空欄 → entries/ ファイル名と initiatives/ ディレクトリ名・00_proposal.md の「backlog元ファイル」で照合
  3. 一致 → 施策化済みと判定
- TG-008 は差分のみ: 前回 20260315-2 以降にマージされた施策（l1-manager-enhanced-planning, session-lifecycle-policy-rename, session-consistency-manager, impl-manager-refs-knowledge-read）で変更されたスキル/エージェント定義に限定
- 参考資料（ドラフト）対象: docs/coordination-protocol-guideline.md, docs/git-worktree-guideline.md

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-17
