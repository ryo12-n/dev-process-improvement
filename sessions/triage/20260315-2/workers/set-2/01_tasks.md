# ワーカータスク指示: Set-2

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-002 | backlog | 新規21件（BL-054〜BL-074）の品質確認。施策化済みチェック（全74件対象）。完了済み BL-002/BL-031 の処理。対象リポジトリ未記入チェック | 削除・クローズ候補リスト確定 |
| TG-005 | backlog | 新規21件を含む全74件の関係性分析（重複候補・依存関係・統合候補） | 関係性テーブル完成、統合/削除候補の有無確定 |
| TG-006 | rules/workflow | ルール・workflow 整合性チェック。参考資料（ドラフト）ステータスチェック。前回修正（manager-common-policy §1/§9、README）の反映確認 | 乖離の検出・修正完了 |
| TG-010 | GHA/Skills | `.github/gha-skills-mapping.yml` に基づくドリフト検出。前回トリアージで推奨された initiative ワークフロー3件のマッピング追加状況を確認 | 全マッピングのチェック完了、ドリフト重大度判定済み |

## 走査時の注意事項

- TG-002: BL-002（完了）とBL-031（完了）は施策化済みかつ完了。CSV行の処理を確認。新規 BL-066〜BL-074 の品質（テンプレート準拠・対象リポジトリ記入・優先度設定）に特に注目。
- TG-005: 前回トリアージで重複3組・依存8組・統合6グループを検出済み。今回は新規21件（特に BL-066〜BL-074）が既存エントリとの関係性を持つかに注目。
- TG-006: 前回修正として manager-common-policy §1/§9 に automation-manager と config-optimizer-manager を追加、README に起動型スキル4件を追加。これらが実際に反映されているかを確認。参考資料（ドラフト）は `docs/coordination-protocol-guideline.md` と `docs/git-worktree-guideline.md` の2件。
- TG-010: 前回トリアージで initiative ワークフロー3件（wallbash, execute, close）のマッピング追加を推奨。新規作成された gha-initiative 系4スキル（gha-wallbash, gha-execute, gha-close, gha-question）との整合性を確認。
- TG-009: TG-002 で削除・統合候補が出た場合のみ実施すること。

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-15
