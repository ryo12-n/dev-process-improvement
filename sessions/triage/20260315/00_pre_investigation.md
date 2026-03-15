# トリアージ事前調査: 2026-03-15

## inbox 確認

- [x] 未処理アイテム数：23 件
- [x] 最古アイテムの日付：2026-03-09（推定、initiative 完了時期から）
- [x] 注目すべきアイテム（タイトル列挙）：
  - automation-manager-common-policy-addition.md（ポリシー追加提案）
  - automation-session-flow-policy-addition.md（ポリシー追加提案）
  - session-flow-policy-checklist-improvement.md（ISS-056 関連）
  - gha-workflow-security-checklist.md（ISS-058 関連）
  - refs-routing-template-unification.md（テンプレート統一提案）

## backlog 確認

- [x] 総件数：53 件（BL-001〜BL-053）
- [x] 優先度 🔴（高）：3 件（BL-011, BL-020, BL-024）
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古は BL-001 の 2026-03-03、12日前）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：1+ 件
  - BL-032（完了）: claude-code-plugin-skills-survey → ステータス「完了」だが CSV に残存
  - BL-020（進行中）: sync-worker-target-commit → 正常（進行中）
- [x] 特記事項：BL-031（automation-managerセッション作成）は inbox エントリと関連する可能性あり

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：24 件
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：ISS-052〜055 はメタ認知 20260311 で起票された4件。ISS-056〜058 は直近施策から起票

## 進行中 initiative 確認

- [x] 進行中：2 件
  - sync-worker-target-commit: 実装中（BL-020）
  - triage-phase-gate-and-gha-sync: ゲート未通過
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：5 件
  - automation-manager-session
  - claude-code-plugin-skills-survey
  - impl-worktree-parallel
  - phase-gate-standardization
  - sessionstart-hook-branch-cleanup
- [x] 状態不明（ゲートレビューなし/不完全）：3 件
  - backlog-id-and-issue-template（ゲートレビューなし）
  - impl-worker-worklog-reliability（ゲートレビューなし）
  - external-repo-cleanup-on-demand（ゲート不完全）

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：0 件（全23件が initiative からの知見エントリ）
- [x] 処理候補のエントリ（タイトル列挙）：
  - 全23件が完了済み initiative のゲートレビューからルーティングされた知見

## ルール・workflow 整合性確認（.claude/rules/*.md ↔ docs/workflow.md）

- [x] 乖離あり
  - README.md: l1-impl-manager, automation-manager, config-optimizer-manager 等 9+スキルが未記載
  - README.md: Implementation, Automation, Config-Optimization の3セッションタイプが未記載
  - docs/workflow.md: 大規模変更の有無は TG-006/TG-008 で詳細確認予定

## GHA ↔ Skills 整合性確認

- [x] `.github/gha-skills-mapping.yml` の存在確認：あり
- [x] 前回トリアージ以降に `.claude/skills/` または `.github/prompts/` に変更があったか：あり（大幅変更 — config-optimizer-manager 新設、automation-manager/l1-impl-manager 更新、共通ポリシー3件更新）

## 前回トリアージからの変化

- 前回実施日：2026-03-12（3日前）
- inbox 増減：-24件（前回処理）→ +23件（新規蓄積）= 実質 -1件
- backlog 増減：+1件（BL-053 新規追加）
- 完了施策：automation-manager-session, claude-code-plugin-skills-survey, impl-worktree-parallel, phase-gate-standardization, sessionstart-hook-branch-cleanup（5件ゲート通過）
- 新規課題：ISS-056, ISS-057, ISS-058

## 調査サマリ・今回の重点

- 重点1：inbox 23件の知見エントリ処理（全件が完了済み initiative からの知見）
- 重点2：アーカイブ候補5件の状態確認・レポート記載
- 重点3：TG-008 スキル定義チェック（config-optimizer-manager 新設、大幅なスキル更新あり）
- 重点4：README 乖離修正（9+スキル未記載）

## ワーカーセット数の推奨

- 走査ボリューム見積もり：inbox 23件 + backlog 53件 + CSV 27件 = 合計 103件
- 推奨セット数：6-7セット（フェーズ別分割）
- 割り当て方針：
  - Phase 1（状態収集）: 2セット並列（set-1: TG-001、set-2: TG-003/TG-004/TG-007）
  - Phase 2a（突合・整合性）: 2セット並列（set-3: TG-002、set-4: TG-006/TG-008）
  - Phase 2b（関係性分析）: 1セット（set-5: TG-005）
  - Phase 2c（リスク評価）: 条件付き 0-1セット（set-6: TG-009）
  - Phase 3（GHA整合性）: 1セット（set-7: TG-010）

---
**調査者**: トリアージマネージャー
**調査日**: 2026-03-15
