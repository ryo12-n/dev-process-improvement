# ドメインエージェント参照の他マネージャーへの展開

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-068 |
| **優先度** | 🔵 低 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | |
| **起票日** | 2026-03-15 |

## 課題・背景

agency-agents-integration 施策では、l1-manager のみにドメインエージェント参照の仕組みを統合した。manager-common-policy §10 として共通ポリシーは定義済みだが、他のマネージャー（triage-manager, metacognition-manager, sync-manager, backlog-maintenance-manager, automation-manager, config-optimizer-manager, l1-impl-manager）への具体的な統合はスコープ外とした。

- 他マネージャーでもドメインエージェントの専門知識が有用な場面がある（例: automation-manager でのセキュリティ観点、config-optimizer-manager でのDevOps観点）
- l1-manager での活用実績を踏まえてから展開するのが適切

## 期待効果

- 全マネージャーセッションでドメインエージェントの専門知識を活用可能に
- 施策の品質向上（専門的な観点の漏れ防止）

## 補足・参考情報

- 依存施策: agency-agents-integration（本施策の完了が前提）
- manager-common-policy §10 は既に全マネージャー共通ポリシーとして定義済み
- 展開対象マネージャーごとに、02_tasks.md テンプレートや起動時パラメータの調整が必要
