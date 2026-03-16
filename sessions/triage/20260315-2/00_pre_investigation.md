# トリアージ事前調査: 2026-03-15（2回目）

## inbox 確認

- [x] 未処理アイテム数：17 件
- [x] 最古アイテムの日付：2026-03-15（前回トリアージ後に起票された新規アイテム）
- [x] 注目すべきアイテム（タイトル列挙）：
  - gha-skills-mapping-initiative-coverage.md（initiative 系ワークフローのマッピング追加提案）
  - gha-skills-mapping-initiative-registration.md（新規4スキルのマッピング登録）
  - gha-user-input-escape-rule.md（ISS-059 関連セキュリティ）
  - backlog-entries-format-unification.md（旧フォーマット13件の統一）
  - refs-meta-info-template.md（refs/ メタ情報標準化）
  - posttooluse-hook-quality-check.md（PostToolUse hook 自動検証）

## backlog 確認

- [x] 総件数：74 件（BL-001〜BL-074）
- [x] 優先度 🔴（高）：6 件（BL-011, BL-020, BL-024, BL-067, BL-068, BL-071）
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古は BL-001 起票日 2026-03-03、13日前）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：2 件
  - BL-002: dev-workflow-detail L1参照精査（完了）
  - BL-031: automation-managerセッション作成（完了）
- [x] 特記事項：前回トリアージ（20260315）で BL-054〜BL-065 を追加。その後 BL-066〜BL-074 が新規追加（9件）。BL-020 は「進行中」。

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：24 件
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：前回トリアージ以降に ISS-059〜ISS-062 が新規追加（4件）。ISS-059（シェルインジェクションリスク）・ISS-061（deny非機能性）・ISS-062（hook バイパスリスク）は高〜中優先度のセキュリティ関連。

## 進行中 initiative 確認

- [x] 進行中：5 件
  - backlog-id-and-issue-template: 計画済み・未着手
  - external-repo-cleanup-on-demand: 作業完了・評価待ち
  - impl-worker-worklog-reliability: 計画済み・未着手
  - sync-worker-target-commit: 進行中（BL-020 対応）
  - triage-phase-gate-and-gha-sync: 計画済み・未着手
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：0 件
  - 前回トリアージで5件のアーカイブ移動を実施済み

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：17 件（全て前回トリアージ後に起票）
- [x] 処理候補のエントリ（タイトル列挙）：
  - gha-skills-mapping-initiative-coverage.md
  - gha-skills-mapping-initiative-registration.md
  - gha-user-input-escape-rule.md
  - backlog-entries-format-unification.md
  - refs-meta-info-template.md
  - refs-intake-plan-verification.md
  - posttooluse-hook-quality-check.md
  - import-inline-expansion-limitation.md
  - plugin-staged-introduction.md

## ルール・workflow 整合性確認（.claude/rules/*.md ↔ docs/workflow.md）

- [x] 前回トリアージで manager-common-policy/README 整合性修正を実施済み。今回は新規乖離の有無を再確認する。

## GHA ↔ Skills 整合性確認

- [x] `.github/gha-skills-mapping.yml` の存在確認：あり
- [x] 前回トリアージ以降に `.claude/skills/` または `.github/prompts/` に変更があったか：要確認（前回トリアージ以降のコミットで変更があれば対象）

## 前回トリアージからの変化

- 前回実施日：2026-03-15（同日1回目）
- inbox 増減：+17 件（前回23件を処理後、17件新規発生）
- backlog 増減：+21 件（前回53件 → 現在74件。BL-054〜BL-074 追加）
- 完了施策：なし（前回以降に新たなゲート通過なし）
- 新規課題：ISS-059〜ISS-062（4件追加）

## 調査サマリ・今回の重点

- 重点1：inbox 17件の分類・処理（GHA 関連8件がクラスター化、refs 関連3件）
- 重点2：新規 backlog エントリ（BL-066〜BL-074）の品質確認と関係性分析
- 重点3：前回トリアージのアクション反映確認（ルール反映8件・backlog追加12件が適切に実施されているか）

## ワーカーセット数の推奨

- 走査ボリューム見積もり：inbox 17 件 + backlog 21 件（新規分） + CSV 4 件（新規分） = 合計 42 件
- 推奨セット数：2 セット（21〜50件 → フェーズ別にセット分割）
- 割り当て方針：
  - Set-1（Phase 1）: TG-001, TG-003, TG-004, TG-007（状態収集: inbox分類 + CSV棚卸し + initiative確認 + README整合性）
  - Set-2（Phase 2a+2b+3）: TG-002, TG-005, TG-006, TG-010（突合・関係性 + ルール整合性 + GHA整合性）
  - TG-008: スキップ（前回同日実施、スキル定義への変更なし）
  - TG-009: 条件付き（TG-002 で削除候補が出た場合のみ）

---
**調査者**: トリアージセッション
**調査日**: 2026-03-15
