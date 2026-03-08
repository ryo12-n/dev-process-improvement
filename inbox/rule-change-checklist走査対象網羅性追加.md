# rule-change-checklist に走査対象の網羅性確認項目を追加する

## 背景

施策「2つのリポジトリの部分的同期」（partial-repo-sync）で、パス移動後の grep 検証において `backlog/` ディレクトリが走査対象から漏れ、旧パスの残存が evaluator でようやく検出された。

現在の rule-change-checklist は「テンプレート」「docs/workflow.md」「TG-008」等の確認項目はあるが、ルートレベルの全ディレクトリを走査対象に含めるかどうかの確認項目がない。

## 提案

rule-change-checklist スキルに以下の確認項目を追加する：
- 「パス変更・リネームを含む施策では、ルートレベルの全ディレクトリ（backlog/, inbox/, refs/, issues/ 等）を grep 走査対象に含めたか」

## 関連
- ISS-042（プロセス改善_課題管理.csv に転記済み）
- 発見元施策: `sessions/initiatives/partial-repo-sync/`
