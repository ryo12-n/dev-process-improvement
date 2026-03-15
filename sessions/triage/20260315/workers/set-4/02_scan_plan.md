# スキャン計画: Set-4

## 壁打ちフェーズ [2026-03-15 10:00]

### 理解のサマリー
- タスクの目的: TG-006（ルール/workflow整合性チェック）とTG-008（セッション構造標準ポリシーチェック）の走査を実施し、乖離・不適合を検出する
- スコープ:
  - TG-006: docs/workflow.md と .claude/skills/ の乖離、参考資料ステータスバナー確認、refs/ 孤立確認、docs/ 分類テーブル網羅性
  - TG-008: 重点対象（config-optimizer-manager, automation-manager, l1-impl-manager, 共通ポリシー3件）のA/B/C/Dチェック
- 完了条件: 乖離の検出・記録完了、ファイル別チェック結果テーブル完成

### 前提条件チェック
- [x] 割り当てTGタスクの内容を理解: 理解済み
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み（docs/, .claude/skills/, refs/ すべて存在確認済み）
- [x] 走査に必要なツール・アクセス権限: 確認済み

### 不明点・確認事項
なし

### マネージャー確認結果
確認事項なし：実施開始

---

## スキャン計画

### 走査対象

| # | TGタスクID | 対象 | 走査方法 | 想定所要時間 |
|---|----------|------|---------|------------|
| 1 | TG-006 | docs/workflow.md vs .claude/skills/ | workflow.md を読み、各スキル SKILL.md と記述を比較。特に config-optimizer-manager, automation-manager の反映確認 | 中 |
| 2 | TG-006 | 参考資料ステータスチェック | docs/coordination-protocol-guideline.md, docs/git-worktree-guideline.md のバナー確認 | 小 |
| 3 | TG-006 | refs/ 孤立確認 | refs/ 内エントリと inbox/ ポインター有無を突合 | 小 |
| 4 | TG-006 | docs/ 分類テーブル網羅性 | docs/ 実ファイルと CLAUDE.md テーブルの突合 | 小 |
| 5 | TG-008 | config-optimizer-manager（新設） | SKILL.md + agents 4件の A/B/C/D チェック | 中 |
| 6 | TG-008 | automation-manager（大幅更新） | SKILL.md + agents 2件の A/B/C/D チェック | 中 |
| 7 | TG-008 | l1-impl-manager（大幅更新） | SKILL.md + agents 5件の A/B/C/D チェック | 中 |
| 8 | TG-008 | 共通ポリシー3件 | manager-common-policy, session-flow-policy, triage-standard-policy の整合性確認 | 小 |

### 走査順序・依存関係
- TG-006 → TG-008 の順で実施（TG-006 で全体把握してから TG-008 の詳細チェックに入る）
- TG-006 内: workflow.md 比較 → 参考資料 → refs/ → docs/ 網羅性
- TG-008 内: triage-standard-policy 基準把握（済み） → 重点対象の順次チェック

### 注意事項・制約
- 軽微な記述ズレはセッション内修正候補としてレポートに記載（修正は行わない）
- TG-009 は本セットでは実施しない（削除・統合候補が見つかった場合は scan_report に記録のみ）

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
