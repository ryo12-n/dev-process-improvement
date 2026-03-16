# 実施計画: session-consistency-manager

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | スキル・エージェント定義の作成（SKILL.md + 4エージェント + リファレンステンプレート） | 6ファイルが session-flow-policy の必須要素を満たす |
| 2 | セッションテンプレートの作成（sessions/session-consistency/_template/） | 15ファイルが config-optimizer テンプレートと対称的な構造 |
| 3 | 連動ファイルの更新 | commit-message.md, manager-common-policy, session-flow-policy, triage-standard-policy, docs/workflow.md の5ファイル更新完了 |

## 成功基準（全体）
1. session-flow-policy §5.1 の新セッションタイプ追加チェックリスト全項目を通過する
2. triage-standard-policy §3.2 のチェック項目（A〜E）を自セッションに適用し、自己整合性が確認できる
3. config-optimizer-manager と対称的な3フェーズ構造が実現されている

## リソース・前提条件
- config-optimizer-manager の SKILL.md・エージェント定義・テンプレートを参照パターンとして使用
- session-flow-policy, manager-common-policy, triage-standard-policy の最新版を基準とする

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| ファイル数が多く作業漏れが発生する | 中 | 中 | チェックリストで管理し、完了確認を逐次行う |
| 連動更新の適用マトリクスが複雑で不整合が残る | 中 | 高 | triage-standard-policy の適用マトリクスは慎重に列追加を行う |

---
**作成者**: L1
**作成日**: 2026-03-16
**最終更新**: 2026-03-16
