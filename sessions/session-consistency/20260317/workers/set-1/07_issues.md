# 課題バッファ: Phase 1

## 課題一覧

### ISS-TEMP-001: l2-plan-worker/l2-plan-evaluator の関連ファイル一覧に旧名称参照が残存
- **発見フェーズ**: Phase 1
- **発見者**: sc-collection-worker
- **重要度**: 中
- **内容**: `l1-manager/agents/l2-plan-worker.md` と `l1-manager/agents/l2-plan-evaluator.md` の「関連ファイル一覧」セクションで `.claude/skills/triage-standard-policy/SKILL.md` を参照しているが、当該ファイルは 2026-03-17 に `session-lifecycle-policy` にリネーム済みで存在しない
- **影響**: 関連ファイル一覧を参照して連動更新を行う際に、正しい参照先にたどり着けない。実質的な機能影響はないが、メタルール横断整合性の破綻
- **推奨対応**: 両ファイルの関連ファイル一覧の参照先を `.claude/skills/session-lifecycle-policy/SKILL.md` に更新する
- **CSV転記**: [未転記]

### ISS-TEMP-002: 04_scan_report.md テンプレートに旧名称セクション見出しが残存
- **発見フェーズ**: Phase 1
- **発見者**: sc-collection-worker
- **重要度**: 低
- **内容**: `sessions/session-consistency/_template/workers/_template/04_scan_report.md` の SC-006 セクション見出しが「SC-006: triage-standard-policy 適用マトリクス整合」となっているが、正しくは「session-lifecycle-policy」
- **影響**: テンプレートからコピーして作業する際にセクション見出しが旧名称のままになる。軽微な表記不整合
- **推奨対応**: テンプレートのセクション見出しを「SC-006: session-lifecycle-policy 適用マトリクス整合」に更新する
- **CSV転記**: [未転記]
