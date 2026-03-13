# 実施計画: automation-managerセッション作成

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | 全成果物作成（スキル定義・テンプレート・候補管理・連動更新） | 1セッション | 下記の成功基準を全て満たすこと |

## スケジュール

単一フェーズで完結する施策。L2-worker に全タスクを一括ディスパッチし、L2-evaluator で検証する。

## 成功基準（全体）

1. `.claude/skills/automation-manager/SKILL.md` が session-flow-policy §2 の必須要素を含む
2. `agents/` にワーカー・評価者ペアが存在し、ペアリング対称性が確保されている
3. `sessions/automation/_template/` が triage/backlog-maintenance テンプレートと同等構成
4. `automation-candidates/` に CSV + entries + README + _template が揃い、AC-001〜AC-014 が登録済み
5. commit-message.md に `[auto-mgr]`, `[auto-worker]`, `[auto-eval]` が追加済み
6. triage-standard-policy のライフサイクル適用マトリクスに3行追加済み
7. docs/workflow.md に automation セッションフロー記述が追加済み

## リソース・前提条件

- 先行施策「ai-automation-tool-review」のアーカイブ（R-001〜R-014）が参照可能
- backlog-maintenance-manager が参照実装として利用可能
- manager-common-policy, session-flow-policy, triage-standard-policy が安定版

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| session-flow-policy の必須要素漏れ | 低 | 中 | §5.1 チェックリストで検証 |
| 先行施策データの移行漏れ | 低 | 低 | R-001〜R-014 の1対1対応を確認 |

---
**作成者**: L1
**作成日**: 2026-03-13
**最終更新**: 2026-03-13
