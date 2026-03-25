# 実施計画: ai-dev-chain-gen-tests

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 (計画) | SKILL.md の現状分析・プロンプト設計方針の策定 | テストケース導出のサブステップ構成が定義されている |
| 2 (実施) | SKILL.md プロンプト実装・backlog.md 更新 | gen-tests コマンドで tests.json / tests.md が正常生成される |

## 成功基準（全体）
1. `/gen-tests projects/test-gen-req` で `tests.json` / `tests.md` が正常に生成される
2. SKILL.md に TODO コメントが残っていない
3. tests.json が FR/NFR との traceability を持つ（related_requirements フィールド）
4. backlog.md のチェーン進捗テーブルが実態を反映している

## リソース・前提条件
- gen-req / gen-design の SKILL.md（7ステップパターンの参照）
- projects/_template/artifacts/tests.json（スキーマテンプレート）
- projects/test-gen-req/artifacts/（requirements.json, openapi.yaml が存在すること）

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| ステップ4のサブステップ設計が複雑化 | 中 | 中 | gen-design のサブステップ構成（4a〜4d）を参考に適切な粒度に分割 |
| tests.json の出力が大きくなりすぎる | 低 | 低 | テストスイート単位で構造化し、coverage_targets で範囲を制御 |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
