# スキャン計画: Set-2

## 壁打ちフェーズ [2026-03-15 10:00]

### 理解のサマリー
- タスクの目的: backlog の品質確認・施策化済みチェック（TG-002）、関係性分析（TG-005）、ルール・workflow 整合性チェック（TG-006）、GHA ↔ Skills 整合性チェック（TG-010）の4タスクを走査し、構造化レポートを作成する
- スコープ: TG-002, TG-005, TG-006, TG-010（TG-009 は TG-002 で削除・統合候補が出た場合のみ）
- 完了条件: 各タスクの走査結果を 04_scan_report.md に構造化レポートとして記載。課題があれば 07_issues.md に起票

### 前提条件チェック
- [x] 割り当てTGタスクの内容を理解: 理解済み
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み
  - backlog/backlog.csv: 74件（BL-001〜BL-074、BL-032欠番、BL-061欠番）
  - backlog/entries/: 72ファイル存在
  - sessions/initiatives/: 6件進行中 + _template + _archive
  - sessions/initiatives/_archive/: 86件アーカイブ済み
  - .claude/rules/: 5ファイル
  - .claude/skills/: 24ディレクトリ
  - docs/: 6ファイル
  - .github/gha-skills-mapping.yml: 存在確認済み（2マッピング定義）
  - .github/workflows/: initiative 系4ワークフロー確認済み
  - .github/prompts/triage.md: 存在確認済み
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
| 1 | TG-002 | backlog | CSV 全74件の施策化済みチェック（initiatives/ + _archive/ 照合）。新規 BL-066〜BL-074 品質確認。完了済み BL-002/BL-031 処理確認 | 高 |
| 2 | TG-005 | backlog | 全74件の関係性分析。新規21件（BL-054〜BL-074）と既存エントリの重複・依存・統合候補検出 | 高 |
| 3 | TG-006 | rules/workflow | skills/ と docs/workflow.md の整合性チェック。README 整合性チェック。参考資料ステータスチェック。前回修正の反映確認 | 中 |
| 4 | TG-010 | GHA/Skills | gha-skills-mapping.yml の2マッピングのドリフト検出。initiative 系マッピング追加状況確認 | 中 |
| 5 | TG-009 | backlog | TG-002 の結果次第で条件付き実施（削除・統合候補の情報欠損リスク評価） | 低（条件付き） |

### 走査順序・依存関係
- TG-002 → TG-009（TG-002 で候補が出た場合のみ TG-009 実施）
- TG-005 は TG-002 と部分的に並行可能だが、逐次実施する
- TG-006, TG-010 は独立

### 注意事項・制約
- BL-002（完了）と BL-031（完了）の CSV 行が残存しているか確認する
- BL-066〜BL-074 はテンプレート準拠・対象リポジトリ記入・優先度設定を重点チェック
- TG-010: gha-skills-mapping.yml にはトリアージと L1 自動施策化の2マッピングのみ。initiative 系4スキル（gha-wallbash, gha-execute, gha-close, gha-question）のマッピングが追加されたか確認
- TG-006: docs/git-worktree-guideline.md の CLAUDE.md テーブルでの統合状況記載（「一部統合済み」）と実際のバナー内容を突合

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
