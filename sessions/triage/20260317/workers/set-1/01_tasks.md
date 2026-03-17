# ワーカータスク指示: Set-1

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-001 | inbox | 全未処理アイテム17件を「backlog候補 / 却下 / 即時反映 / 対応不要」に分類する | 全件に分類が付いている |
| TG-007 | inbox | セッション終了時の気づきエントリ17件を処理する（TG-001 と統合して実施） | 処理結果が記録されている |

## 走査時の注意事項

- inbox に 17件のエントリがある。全てが前回トリアージ（20260315-2）後に起票された新規アイテム
- ref_*.md ポインターファイルは存在しない
- 特に重大度が高いもの:
  - l1-direct-execution-bypasses-l2-flow.md（L1がL2フローを迂回した問題 → ルール改善必要）
  - backlog-id-collision-prevention.md（並列セッション環境でのID衝突リスク）
  - subagent-commit-reliability.md（L2コミット・プッシュの信頼性問題）
- aidd-cross-session-knowledge-aggregation.md と aidd-tool-policy-centralization.md は ai-driven-dev-patterns 向けの施策候補
- TG-001 と TG-007 は統合して処理する（inbox アイテムは全て気づきエントリ）
- 分類時に「即時反映」カテゴリも使用可能（ルール修正など軽微で即時対応可能なもの）

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-17
