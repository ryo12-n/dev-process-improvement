# gha-skills-mapping.yml に initiative 系ワークフローのマッピングを追加

## 背景
`.github/gha-skills-mapping.yml` に triage-gha と l1-auto-execute-gha のマッピングのみ登録されており、initiative 系ワークフロー（wallbash, execute, close, question, dispatcher）のマッピングが未登録。TG-010 でのドリフト検出精度に影響する。

## 提案
initiative 系ワークフローのマッピングエントリを `gha-skills-mapping.yml` に追加する。

## 起票元
`sessions/initiatives/gha-wallbash-iterative-phase/07_issues.md` + `08_gate_review.md` 横展開セクション
