# ワーカータスク指示: Set-1

<!-- マネージャーが 01_plan.md のワーカー割り当てに基づいて記入する -->

## 割り当てTGタスク

全フェーズ逐次実行（フェーズ内の論理順序を維持すること）。

### Phase 1: 状態収集

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-001 | inbox | 全 15 件を「backlog候補 / ルール反映 / 却下 / 保留」に分類する | 全件に分類・理由が付いている |
| TG-003 | CSV | 高優先度の起票課題（ISS-059, 061, 064, 068）の対応状況を確認。新規 ISS-065〜068 の内容を確認 | 対応状況が記録されている |
| TG-004 | initiative | アーカイブ待ち 7 件（backlog-to-issue-status-sync, csv-conflict-prevention, l1-manager-checklist-integration, l1-manager-enhanced-planning, session-cost-measurement, session-lifecycle-policy-rename, skill-plugin-overlap-check-rule）と進行中 5 件の状態確認 | 全施策の状態がスキャンレポートに記録 |
| TG-007 | refs | refs/ の孤立エントリ（inbox/ref_* ポインターなし）を確認・報告: agency-agents, ai-driven-dev-patterns, claude-code-action, test, _knowledge_template.md, _work_log_template.md | 報告が記録されている |

### Phase 2a: 突合・整合性チェック

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-002 | backlog | 新規 BL-095〜BL-106 の施策化状況を sessions/initiatives/ および _archive/ と突合。施策化済み/未クローズ検出。対象リポジトリ未記入チェック | 削除・クローズ候補リスト確定 |
| TG-006 | rules/workflow | ルール・workflow 整合性チェック。参考資料ステータスチェック。README 整合性チェック。スキル定義の関連ファイル一覧チェック | 乖離の検出・記録 |

### Phase 2b: 関係性分析

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-005 | backlog | 新規 BL-095〜BL-106 と既存エントリの関係性（重複候補・依存関係・統合候補）を分析 | 分析結果テーブル完成 |

### Phase 3: GHA 整合性

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-010 | GHA/Skills | gha-skills-mapping.yml に基づく GHA ↔ Skills のドリフト検出 | 全マッピングチェック完了、ドリフト重大度判定済み |

## 走査時の注意事項

- TG-008 は SC セッション（20260319）で包括的に実施済みのためスキップ
- TG-009 は TG-002/TG-005 で削除・統合候補が出た場合のみ実施
- Phase の論理順序を維持すること（TG-005 は TG-002 の後に実行）
- inbox の全 15 件は前回トリアージ（20260318）以降の新規エントリ
- GHA 関連の知見エントリが多い（6件）ため、gha-guideline スキルとの関連に注意

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-19
