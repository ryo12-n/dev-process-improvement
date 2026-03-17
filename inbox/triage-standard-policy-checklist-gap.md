# session-flow-policy チェックリストに triage-standard-policy 連動更新を追加

## 背景
l1-manager-enhanced-planning 施策フェーズ1で、新エージェント（l2-plan-worker / l2-plan-evaluator）追加時に triage-standard-policy の走査対象リスト（§3.1）のみ更新され、ペアリング構造テーブル（§2.1）と適用マトリクス（§1.2）の更新が漏れた。

## 提案
session-flow-policy §5.1 の新セッションタイプ追加時チェックリストに以下を追加:
- triage-standard-policy §3.1 走査対象リストの更新（既存）
- triage-standard-policy §2.1 ペアリング構造テーブルの更新（追加）
- triage-standard-policy §1.2 適用マトリクスの更新（追加）

## 起票元
sessions/initiatives/l1-manager-enhanced-planning/ 施策フェーズ1 評価レポート

---
**起票日**: 2026-03-17
