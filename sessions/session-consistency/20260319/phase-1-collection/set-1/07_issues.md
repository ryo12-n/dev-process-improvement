# 課題バッファ: Phase 1

## 課題一覧

### ISS-TEMP-001: SC-008 壊れた参照が2回のスキャンにわたり未修正
- **発見フェーズ**: Phase 1
- **発見者**: sc-collection-worker
- **重要度**: 中
- **内容**: `l1-manager/agents/l2-plan-worker.md`（195行目）および `l1-manager/agents/l2-plan-evaluator.md`（112行目、198行目）が `.claude/skills/triage-standard-policy/SKILL.md` を参照しているが、このファイルは 2026-03-17 に `session-lifecycle-policy` にリネーム済みで存在しない。前回スキャン（2026-03-17）で検出済みだが未修正のまま残存。
- **影響**: l2-plan-worker および l2-plan-evaluator が関連ファイル一覧の参照先として存在しないパスを記載しており、これらのファイル変更時の連動更新チェックが正しく機能しない。l2-plan-evaluator はメタルール横断検証のチェック項目内でも旧名称を使用している。
- **推奨対応**: 3箇所の `triage-standard-policy` を `session-lifecycle-policy` に置換する
- **CSV転記**: [未転記]

### ISS-TEMP-002: SC-007 の l2-plan-worker / l2-plan-evaluator「未登録」判定が事実と不一致
- **発見フェーズ**: Phase 1 評価
- **発見者**: sc-evaluator
- **重要度**: 低
- **内容**: スキャンレポートおよびリファレンスの SC-007 セクションで、l2-plan-worker と l2-plan-evaluator を commit-message 規約に「未登録の可能性がある」と記載しているが、`.claude/rules/commit-message.md` 37-38行目には「タスク実施・作業記録・レポート作成（l2-plan-worker を含む）」「評価計画・評価実施・レポート作成（l2-plan-evaluator を含む）」と明示的に記載されており、既に L2-worker / L2-evaluator のカテゴリに包含されている。
- **影響**: リファレンスに不正確な情報が残存し、Phase 2（Analysis）で誤った不整合として分析される可能性がある。
- **推奨対応**: リファレンスの SC-007「未登録セッションタイプ」テーブルから当該2件を削除し、スキャンレポートの SC-007 セクションも修正する。
- **CSV転記**: [未転記]
