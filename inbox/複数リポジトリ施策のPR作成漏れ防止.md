# 複数リポジトリで作業する施策のPR作成漏れ防止

## 気づき

両方のリポジトリ（dev-process-improvement / ai-driven-dev-patterns）で変更を行う施策において、片方のPR作成が漏れた。クローズ手順やL1-managerのSKILL.mdに「複数リポジトリで作業した場合は全リポジトリでPR作成・承認依頼を行う」旨を明記すべき。

## 発生した状況

- roles-agents-migration 施策で、dev-process-improvement 側のPRは作成したが、ai-driven-dev-patterns 側のPR作成が漏れた
- ユーザー指摘で発覚し、事後的に作成

## 対応案

- L1-manager SKILL.md のクローズ手順に「作業対象が複数リポジトリの場合、全リポジトリでPR作成を確認する」チェック項目を追加
- または `.claude/rules/` に独立ルールとして追加

## 出典

施策: `sessions/initiatives/_archive/roles-agents-migration/`（2026-03-08）

---
**起票日**: 2026-03-08
