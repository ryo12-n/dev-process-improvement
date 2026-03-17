# トリアージ事前調査: 2026-03-17

## inbox 確認

- [x] 未処理アイテム数：17 件
- [x] 最古アイテムの日付：2026-03-15（前回トリアージ 20260315-2 後に起票された新規）
- [x] 注目すべきアイテム（タイトル列挙）：
  - l1-direct-execution-bypasses-l2-flow.md（重大度高: L1がL2フローを迂回した問題）
  - subagent-commit-reliability.md（L2コミット・プッシュの信頼性問題）
  - backlog-id-collision-prevention.md（並列セッション環境でのID衝突リスク）
  - l1-impl-common-policy-missing.md（manager-common-policy §1 に l1-impl-manager 記載漏れ）
  - aidd-cross-session-knowledge-aggregation.md（ai-driven-dev-patterns 横断知識管理）
  - aidd-tool-policy-centralization.md（ai-driven-dev-patterns ツール権限集中管理）

## backlog 確認

- [x] 総件数：84 件（BL-001〜BL-083、BL-076/077 に重複採番あり）
- [x] 優先度 🔴（高）：5 件（BL-011, BL-024, BL-067, BL-068, BL-071）
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古は BL-001 起票日 2026-03-03、14日前）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：要確認（TG-002 で走査）
- [x] 特記事項：
  - BL-076/077 に重複採番あり（inbox/backlog-id-collision-prevention.md で既知）
  - 対象リポジトリ未記入エントリが約31件（主に BL-037〜BL-075 の範囲）
  - 完了ステータス 3件: BL-002, BL-031, BL-064
  - 進行中 1件: BL-020（sync-worker同期先コミット漏れ防止）

## 課題管理 CSV 確認

- [x] ステータス「起票」（未対応）：34 件
- [x] ステータス「方針確定」（未タスク化）：1 件
- [x] 最古の未対応課題：ISS-001 付近（要確認）
- [x] 特記事項：
  - 合計 65 件（ISS-001〜ISS-065）
  - クローズ 30 件、起票 34 件、方針確定 1 件
  - 対応中は 0 件

## 進行中 initiative 確認

- [x] 進行中：2 件
  - backlog-id-and-issue-template: ゲートレビュー未作成
  - impl-worker-worklog-reliability: ゲートレビュー未作成
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：7 件
  - csv-conflict-prevention
  - external-repo-cleanup-on-demand
  - l1-manager-enhanced-planning
  - session-lifecycle-policy-rename
  - skill-plugin-overlap-check-rule
  - sync-worker-target-commit
  - triage-phase-gate-and-gha-sync

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：17 件（全て気づき/提案系）
- [x] 処理候補のエントリ（タイトル列挙）：
  - l1-direct-execution-bypasses-l2-flow.md → ルール改善（L1ガードレール明記）
  - skill-file-table-completeness-check.md → ルール改善（担当ファイルテーブル網羅性チェック）
  - template-refactor-cross-reference-check.md → ルール改善（テンプレートリファクタ時相互参照チェック）
  - policy-subsection-numbering-rule.md → ルール改善（サブセクション番号付けルール）
  - l1-impl-common-policy-missing.md → 即時修正可能（§1テーブル更新）
  - refs-read-step-placement-pattern.md → ルール化候補
  - triage-policy-section-consistency-check.md → ルール改善
  - triage-standard-policy-checklist-gap.md → ルール改善
  - table-footnote-consistency-check.md → タスク完了条件改善
  - automation-candidates-sync-guideline.md → 運用手順明文化
  - backlog-id-collision-prevention.md → 施策化候補
  - subagent-commit-reliability.md → 施策化候補
  - gha-multirepository-access-via-clone.md → ドキュメント注記追加
  - knowledge-md-table-scalability.md → 将来課題
  - session-definition-meta-template.md → 将来課題
  - aidd-cross-session-knowledge-aggregation.md → ai-driven-dev-patterns 向け施策化
  - aidd-tool-policy-centralization.md → ai-driven-dev-patterns 向け施策化

## ルール・workflow 整合性確認（.claude/rules/*.md ↔ docs/workflow.md）

- [x] 前回 20260315-2 以降に `.claude/skills/` に多数の変更あり（施策5件以上がマージ）
- [x] 確認必要（TG-006 で走査）

## GHA ↔ Skills 整合性確認

- [x] `.github/gha-skills-mapping.yml` の存在確認：あり
- [x] 前回トリアージ以降に `.claude/skills/` または `.github/prompts/` に変更があったか：あり（多数の施策マージ）

## 前回トリアージからの変化

- 前回実施日：2026-03-15（20260315-2）
- inbox 増減：±0 件（前回 17 件 → 今回 17 件、ただし前回の inbox は全て処理済みで新規 17 件に入れ替わり）
- backlog 増減：+10 件（前回 74 件 → 今回 84 件）
- 完了施策：7 件がゲート通過・アーカイブ待ち
- 新規課題：ISS-059〜ISS-065 が前回以降追加（推定）

## 調査サマリ・今回の重点

- 重点1：inbox 17件の処理（特に l1-direct-execution-bypasses-l2-flow、backlog-id-collision-prevention 等の重大度高アイテム）
- 重点2：7件のアーカイブ待ち施策の確認・レポート
- 重点3：backlog 施策化済みチェック（前回からの10件増加分含む）

## ワーカーセット数の推奨

- 走査ボリューム見積もり：inbox 17 件 + backlog 84 件 + CSV 35 件 = 合計 136 件
- 推奨セット数：フェーズ別に最大2セット（合計 136 件 > 51件）
- 割り当て方針：
  - Phase 1（TG-001, TG-003, TG-004, TG-007）: 2セット（TG-001 は backlog 84件で重量級）
  - Phase 2a（TG-002, TG-006, TG-008）: 1セット（前回から2日、TG-008 は差分チェックのみ）
  - Phase 2b（TG-005）: Phase 2a に含める（低ボリューム時例外）
  - Phase 2c（TG-009）: 候補有無で判断
  - Phase 3（TG-010）: 1セット

---
**調査者**: トリアージセッション
**調査日**: 2026-03-17
