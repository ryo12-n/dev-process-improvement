# 外部リポジトリのテンプレート作成時に frontmatter 必須フィールドを事前調査すべき

## 背景
source-evaluation-cycle 施策で、ai-research-notebook に新テンプレートを作成した際、既存テンプレートの frontmatter フィールド（date, tags, task_type）との一貫性確認が worker の自主判断に依存していた。

## 提案
外部リポジトリにテンプレートを追加する施策では、L1 の計画段階で「既存テンプレートの frontmatter フィールド一覧の事前調査」をタスクに含める。

## 発見元
sessions/initiatives/source-evaluation-cycle（L2-worker / L2-evaluator 双方から指摘）
