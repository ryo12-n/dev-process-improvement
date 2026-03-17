# ワーカータスク指示: Set-2

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-003 | CSV | ステータス「起票」34件+「方針確定」1件の対応方針を検討する | 各アイテムに対応方針案が記載されている |
| TG-004 | initiative | 進行中9施策（うちアーカイブ待ち7件）の状態を確認する | 全施策の状態がスキャンレポートに記録されている |

## 走査時の注意事項

- CSV（issues）の状態: 合計65件、起票34件、方針確定1件、クローズ30件
- 起票34件は全件の対応方針案を検討すること。件数が多いため、類似課題はグルーピングして効率化を推奨
- 進行中 initiative 9件の内訳:
  - アーカイブ待ち（ゲート通過済み）7件: csv-conflict-prevention, external-repo-cleanup-on-demand, l1-manager-enhanced-planning, session-lifecycle-policy-rename, skill-plugin-overlap-check-rule, sync-worker-target-commit, triage-phase-gate-and-gha-sync
  - 進行中（ゲートレビュー未作成）2件: backlog-id-and-issue-template, impl-worker-worklog-reliability
- アーカイブ待ち施策は l1-manager のクローズチェックリストに従いアーカイブ候補として記録すること

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-17
