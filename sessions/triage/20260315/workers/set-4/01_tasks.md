# ワーカータスク指示: Set-4

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-006 | rules/workflow | ルール・workflow 整合性チェック。.claude/skills/*/SKILL.md および agents/*.md と docs/workflow.md の記述乖離を確認。参考資料（ドラフト）ステータスチェック。refs/ 孤立エントリ確認 | 乖離の検出・記録完了 |
| TG-008 | skills/agents | セッション構造標準ポリシーチェック。.claude/skills/triage-standard-policy/SKILL.md の基準に基づき、新規・変更されたスキル/エージェント定義の準拠性を確認 | ファイル別チェック結果テーブル完成 |

## 走査時の注意事項

- **TG-006 走査対象**:
  - docs/workflow.md と各スキル SKILL.md の記述一致
  - 参考資料（ドラフト）: docs/coordination-protocol-guideline.md と docs/git-worktree-guideline.md のステータスバナー確認
  - refs/ 孤立エントリ確認（refs/ にポインターなしエントリがないか）
  - スキル定義の「関連ファイル一覧」セクションが実際の参照先と一致しているか

- **TG-008 重点走査対象**（前回 20260312 以降に新規・変更されたスキル）:
  1. **config-optimizer-manager**（新設）: SKILL.md + agents/config-collection-worker.md, config-analysis-worker.md, config-proposal-worker.md, config-optimizer-evaluator.md
  2. **automation-manager**（大幅更新）: SKILL.md + agents/automation-worker.md, automation-evaluator.md
  3. **l1-impl-manager**（大幅更新）: SKILL.md + agents/investigation-worker.md, design-worker.md, impl-plan-worker.md, impl-worker.md, impl-evaluator.md
  4. **共通ポリシー更新**: manager-common-policy, session-flow-policy, triage-standard-policy

- **TG-008 チェック項目**: triage-standard-policy SKILL.md を読み、A（ライフサイクル完備）、B（ペアリング整合性）、C（課題起票・ルーティング）、D（停止ルール・スコープ）の4観点でチェック

- **TG-009 実行条件の判断材料**: 本セットでは TG-009 は実施しない。ただし TG-006 の走査で削除・統合候補が見つかった場合は scan_report に記録し、マネージャーが Phase 2c で TG-009 を判断する

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-15
