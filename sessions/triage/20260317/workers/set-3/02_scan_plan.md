# スキャン計画: Set-3

## 壁打ちフェーズ [2026-03-17 10:00]

### 理解のサマリー
- タスクの目的: backlog の施策化済みチェック・突合・対象リポジトリ未記入チェック（TG-002）、backlog アイテム間関係性分析（TG-005）、ルール・workflow 整合性チェック（TG-006）、セッション構造標準ポリシーチェック（TG-008、差分のみ）
- スコープ: backlog/ 84件、.claude/skills/、.claude/rules/、docs/、README.md、sessions/initiatives/（読み取りのみ）
- 完了条件: 削除・クローズ候補リスト確定、対象リポジトリ未記入リスト作成、関係性分析テーブル作成、乖離検出結果記録、ポリシーチェック結果記録、04_scan_report.md 作成

### 前提条件チェック
- [x] 割り当てTGタスクの内容を理解: 理解済み
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み（backlog/ 82エントリ、initiatives/ 11件+_archive/ 94件、docs/ 6ファイル）
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
| 1 | TG-002 | backlog | backlog.csv の施策ディレクトリ名列 + initiatives/ _archive/ 突合。完了/進行中エントリ確認。対象リポジトリ列チェック | 中 |
| 2 | TG-005 | backlog | TG-002 結果を基に、エントリ間の重複候補・依存関係・統合候補を分析 | 中 |
| 3 | TG-006 | rules/workflow/docs | .claude/skills/ と docs/workflow.md の整合性、参考資料ステータスバナーチェック、README 整合性 | 中 |
| 4 | TG-008 | skills/agents | 前回20260315-2以降に変更されたスキル/エージェント定義を session-lifecycle-policy に照合 | 中 |

### 走査順序・依存関係
- TG-002 → TG-005（TG-005 は TG-002 の結果に依存）
- TG-006、TG-008 は TG-002/TG-005 と独立して実施可（ただし順次実施）

### 注意事項・制約
- backlog 84件（BL-001〜BL-083、BL-076/077 に重複採番あり）
- 完了ステータス 3件: BL-002, BL-031, BL-064 / 進行中 1件: BL-020
- TG-008 は差分のみ（前回 20260315-2 以降の変更: l1-manager-enhanced-planning, session-lifecycle-policy-rename, session-consistency-manager, impl-manager-refs-knowledge-read 等）
- 参考資料（ドラフト）対象: docs/coordination-protocol-guideline.md, docs/git-worktree-guideline.md

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-17
