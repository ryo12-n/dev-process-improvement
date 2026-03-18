# 課題バッファ: Phase 2（現状分析）

## 課題一覧

### ISS-TEMP-001: session-lifecycle-policy §1.3 に config最適化系・実装系が欠落
- **発見フェーズ**: Phase 2
- **発見者**: sc-analysis-worker
- **重要度**: 中
- **内容**: session-lifecycle-policy の §1.2 適用マトリクスには co-manager/co-worker/co-evaluator（config最適化系）と impl-manager/impl-worker/impl-evaluator（実装系）の列が存在するが、§1.3 記録先ファイル対応テーブルにはこれら2系統の列が存在しない。session-flow-policy §5.1 のチェックリストに「§1.2 と §1.3 の列が一致していること」が含まれているにもかかわらず、漏れが発生している。
- **影響**: §1.3 テーブルを参照してセッション記録先を判断する際に、config最適化系・実装系の記録先が不明になる。実運用では各セッション定義に記録先が記載されているため直接的な影響は小さいが、ポリシー文書としての網羅性に欠ける。
- **推奨対応**: §1.3 テーブルに「config最適化系」「実装系」の列を追加する
- **CSV転記**: [未転記]

### ISS-TEMP-002: l2-plan-worker/evaluator に triage-standard-policy の壊れた参照が3箇所残存
- **発見フェーズ**: Phase 2
- **発見者**: sc-analysis-worker
- **重要度**: 中
- **内容**: 2026-03-17 に triage-standard-policy が session-lifecycle-policy にリネームされたが、l2-plan-worker.md（行195）と l2-plan-evaluator.md（行112, 行198）に旧名称 `triage-standard-policy` への参照が3箇所残存している。Phase 1 では関連ファイル一覧の2箇所のみ検出されていたが、Phase 2 の分析で l2-plan-evaluator.md のメタルール横断検証チェックリスト内（行112）に追加の壊れた参照を発見した。
- **影響**: リネーム後のファイル実体が存在しないため、これらの参照に従って操作しようとした場合にファイル不在エラーが発生する可能性がある。特に行112のチェック項目は、施策がルール変更を含む場合に l2-plan-evaluator が実行するメタルール横断検証で使用されるため、評価の正確性に影響しうる。
- **推奨対応**: 3箇所すべての `triage-standard-policy` を `session-lifecycle-policy` に修正する
- **CSV転記**: [未転記]

### ISS-TEMP-003: リネーム時の残存参照チェック手順が未整備
- **発見フェーズ**: Phase 2
- **発見者**: sc-analysis-worker
- **重要度**: 低
- **内容**: triage-standard-policy → session-lifecycle-policy のリネーム時に3箇所の参照更新漏れが発生した。現在のルール・チェックリストにはリネーム時の全文検索（`Grep` 等）による残存参照チェック手順が明文化されていない。関連ファイル一覧の更新チェックはドキュメント整合性ルール（CLAUDE.md）でカバーされているが、本文中のインライン参照は対象外となっている。
- **影響**: 今後のリネーム・移動時にも同様の更新漏れが発生するリスクがある
- **推奨対応**: リネーム時のチェックリストに「旧名称で全文検索を行い、残存参照がゼロであることを確認する」ステップを追加する
- **CSV転記**: [未転記]
