# 実施計画: メタ認知による改善の強制

## フェーズ構成

| フェーズ | 内容 | 期間 | 成功基準 |
|---------|------|------|----------|
| 1 | スキル・エージェント定義 + テンプレート作成 + 連動更新 | 1セッション | 全成果物が session-flow-policy / triage-standard-policy の基準を満たす |

## スケジュール

1. L2-worker: T-001〜T-006（スキル・テンプレート・連動更新の作成）+ T-007〜T-008（固定タスク）
2. L2-evaluator: 成果物の品質評価
3. ゲート判定: 通過判定

## 成功基準（全体）

1. `metacognition-manager` スキル + `metacognition-worker` / `metacognition-evaluator` エージェントが作成され、session-flow-policy の必須要素チェックリスト（セクション5.1）を全て満たす
2. `sessions/metacognition/_template/` が triage テンプレートと同等の構造で作成されている
3. commit-message.md / workflow.md / session-flow-policy / triage-standard-policy が連動更新されている
4. triage-standard-policy のペアリング対称性要件を満たしている

## リソース・前提条件

- triage-manager / triage-worker / triage-evaluator の既存定義をベースとして参照する
- sessions/ ディレクトリ構造（最新の main ブランチの状態）に準拠する

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| triage との責務境界が曖昧 | 中 | 中 | SKILL.md に triage との違いを明記する |
| 連動更新の漏れ | 低 | 高 | rule-change-checklist に従い更新対象を網羅する |
| テンプレートの構造不整合 | 低 | 中 | triage テンプレートを直接参照して構造を合わせる |

---
**作成者**: L1
**作成日**: 2026-03-08
**最終更新**: 2026-03-08
