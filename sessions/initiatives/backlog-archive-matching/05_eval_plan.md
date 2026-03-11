# 評価計画: backlog-archive-matching改善

## 壁打ちフェーズ [2026-03-11]

### 理解のサマリー
- 評価の目的: L2-worker の成果物（7ファイルの変更）が01_plan.mdの成功基準8項目を満たしているか、相互整合性を含めて検証する
- 評価スコープ: backlog/_template.md, sessions/initiatives/_template/00_proposal.md, backlog/backlog.csv, .claude/skills/l1-manager/SKILL.md, .claude/skills/triage-manager/SKILL.md, docs/workflow.md, プロセス改善_課題管理.csv の変更内容
- 完了条件: 05_eval_plan.md と 06_eval_report.md が作成され、成功基準8項目に対する達成度が評価されていること

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能
- [x] 評価に必要なツール・アクセス権限: 確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
L2-worker による以下7ファイルの変更と相互整合性:
1. `backlog/_template.md` - 施策ディレクトリ名フィールド追加・対象リポジトリ必須化
2. `sessions/initiatives/_template/00_proposal.md` - backlog元ファイルフィールド追加
3. `backlog/backlog.csv` - 施策ディレクトリ名列追加
4. `.claude/skills/l1-manager/SKILL.md` - パターン1拡張・クローズチェックリスト9ステップ化
5. `.claude/skills/triage-manager/SKILL.md` - TG-002突合手順具体化
6. `docs/workflow.md` - 連動更新
7. `プロセス改善_課題管理.csv` - ISS-041ステータス更新

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | SC-1: L1クローズチェックリストにbacklog.csv行削除確認ステップ追加 | l1-manager/SKILL.md のクローズチェックリストを確認 | ステップ5として存在し、9ステップ構成で番号が正しいこと |
| 2 | SC-2: 施策開始時（パターン1）にbacklog.csv行削除が含まれている | l1-manager/SKILL.md のパターン1セクションを確認 | パターン1の手順にbacklog.csv行削除が明記されていること |
| 3 | SC-3: backlogテンプレートに「施策ディレクトリ名」フィールドが存在 | backlog/_template.md を確認 | メタ情報テーブルにフィールドが存在すること |
| 4 | SC-4: 00_proposal.mdテンプレートに「backlog元ファイル」フィールドが存在 | _template/00_proposal.md を確認 | メタ情報セクションにフィールドが存在すること |
| 5 | SC-5: backlog.csvに「施策ディレクトリ名」列が存在 | backlog.csv のヘッダー行を確認 | ヘッダーに列が存在し、既存行の列数が整合していること |
| 6 | SC-6: triage-managerのTG-002に具体的な突合手順が記述されている | triage-manager/SKILL.md のTG-002セクションを確認 | 手順が具体的（ステップ形式）で、フォールバック・対象リポ未記入チェックを含むこと |
| 7 | SC-7: docs/workflow.mdがルールファイルの変更と整合している | workflow.md とl1-manager/triage-manager を突合 | クローズチェックリスト（ステップ5）とTG-002の記述が整合していること |
| 8 | SC-8: rule-change-checklistの全項目が確認済み | 04_work_report.md のT-008実績を確認 | チェックリスト全項目の確認結果が記録されていること |
| 9 | 整合性: フィールド名の相互整合 | 全ファイル間でフィールド名・参照名が一致しているか突合 | 「施策ディレクトリ名」「backlog元ファイル」の名称がファイル間で統一されていること |
| 10 | 整合性: クローズチェックリストの注記参照番号 | l1-manager/SKILL.md の注記を確認 | ステップ番号参照が正しく更新されていること |

## 評価スケジュール
- 全項目を逐次評価し、結果を06_eval_report.mdに記載する

## 前提・制約
- 評価は変更済みファイルの現在の状態に基づいて実施する
- 既存backlogエントリへの遡及的フィールド追加はスコープ外

---
**作成者**: L2（評価）
**作成日**: 2026-03-11
