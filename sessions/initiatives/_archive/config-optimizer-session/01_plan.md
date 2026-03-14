# 実施計画: config-optimizer-session

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | スキル・エージェント・テンプレートの作成 | SKILL.md + 4エージェント + テンプレート + リファレンス初期ファイルが作成されている |
| 2 | 既存ファイルの連動更新 | commit-message, session-flow-policy, triage-standard-policy, manager-common-policy, workflow.md が更新されている |

## 成功基準（全体）

1. session-flow-policy §5.1 のチェックリスト全項目を満たしている
2. SKILL.md に必須セクション（あなたの役割・作業フロー・やること・やらないこと）が含まれている
3. agents/ に worker × 3 + evaluator × 1 が定義されている
4. ペアリングの対称性要件（壁打ち・計画・レポート・知見・課題・停止ルール）を満たしている
5. コミットメッセージ規約に co-mgr/co-worker/co-eval が追加されている
6. workflow.md に新フロー記述が追加されている

## リソース・前提条件

- 参照パターン: l1-impl-manager（多フェーズゲート）、metacognition-manager（日付ベース）、plugin-reference（スナップショット）
- manager-common-policy §1〜§8 への準拠

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 既存ポリシーファイルとの整合性不備 | 中 | 中 | session-flow-policy §5.1 チェックリストで検証 |
| エージェント定義が冗長になる | 低 | 低 | impl-evaluator パターンに倣い簡潔に記述 |

---
**作成者**: L1
**作成日**: 2026-03-14
**最終更新**: 2026-03-14
