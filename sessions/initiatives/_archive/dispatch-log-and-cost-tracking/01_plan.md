# 実施計画: dispatch-log-and-cost-tracking

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | テンプレート作成（02b_dispatch_log.md, 09_cost_record.md） | テンプレートが initiative の Phase 構造に適合し、トリアージの dispatch_log パターンとの整合性がある |
| 2 | 08_gate_review.md テンプレートへのフェーズコストセクション追加 | 各 Phase チェックにコスト小計行があり、最終ゲートに全体コスト集計がある |
| 3 | L1 マネージャースキルへのディスパッチログ・コスト記録手順の組み込み | ディスパッチ時・ゲートチェック時の記録手順が SKILL.md に記載されている |
| 4 | 既存テンプレート（session-cost-measurement.md）との整合性確認・更新 | サンプリング方式の記述が全施策方式に更新されている。料金リファレンスの参照関係が明確 |

## スケジュール

1. テンプレート新設（02b_dispatch_log.md, 09_cost_record.md）
2. 08_gate_review.md テンプレート更新
3. L1 スキル更新
4. 既存テンプレート整合性確認
5. メタルール横断検証（workflow.md, session-lifecycle-policy 等）

## 成功基準（全体）

1. `_template/02b_dispatch_log.md` が作成され、initiative の Phase 2〜5 に対応するディスパッチ記録構造を持つこと
2. `_template/09_cost_record.md` が作成され、フェーズ別・セッション種別のコスト集計テーブルを持つこと
3. `_template/08_gate_review.md` の各 Phase チェックにフェーズコスト小計行が追加されていること
4. `l1-manager/SKILL.md` にディスパッチログ記録・コスト記録の手順が組み込まれていること
5. `.claude/templates/session-cost-measurement.md` がサンプリング方式から全施策方式に整合していること

## リソース・前提条件

- 前施策 `session-cost-measurement` の成果物（テンプレート・ディレクトリ構造）が利用可能
- トリアージの `02_dispatch_log.md` テンプレートを参考パターンとして利用
- 変更対象: `_template/`（新設2ファイル + 既存1ファイル更新）、`l1-manager/SKILL.md`、`.claude/templates/session-cost-measurement.md`

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| L1 スキルの肥大化で可読性低下 | 中 | 中 | 既存フローへの最小限の追記。新セクションではなく既存手順への行追加を優先 |
| 08_gate_review テンプレート変更が既存施策に影響 | 低 | 低 | 新セクション追加のみ。既存チェック項目は変更しない |
| トークン数が常に取得できるとは限らない | 中 | 低 | N/A 許容を明記。経過時間をフォールバック |

---
**作成者**: L1
**作成日**: 2026-03-19
**最終更新**: 2026-03-19
