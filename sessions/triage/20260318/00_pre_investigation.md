# トリアージ事前調査: 2026-03-18

<!-- 実施前にこのテンプレートを埋めること。調査結果を 01_plan.md の判断材料とする。 -->

## inbox 確認

- [x] 未処理アイテム数：9 件
- [x] 最古アイテムの日付：2026-03-17
- [x] 注目すべきアイテム（タイトル列挙）：
  - backlog-entry-minimum-description.md — backlog エントリ起票時の記述粒度最低基準
  - bm-001-threshold-tiering.md — BM-001 閾値の段階化（30/60/90日）
  - commit-message規約l2-plan明確化.md — commit-message 規約の l2-plan session-type 明確化
  - SC走査対象インライン参照拡大.md — SC チェック走査対象をインライン参照に拡大
  - claude-templates-update-checklist.md — .claude/templates/ 追加時の CLAUDE.md 連動更新チェックリスト化
  - SCチェック結果フィードバックループ定義.md — SC チェック結果のフィードバックループ定義
  - bm-report-to-backlog-trigger.md — BM レポート→backlog 変更の実行トリガー明確化
  - evaluator対称性テーブル統一.md — evaluator 対称性確認テーブル統一
  - phase-worker-set-standardization.md — Phase/ワーカーセット構成の標準パターン化

## backlog 確認

- [x] 総件数：94 件
- [x] 優先度 🔴（高）：9 件
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：8 件
  - BL-002: dev-workflow-detail-l1-ref-review
  - BL-004: harness-engineering-brushup
  - BL-010: backlog-template-legend-enhancement
  - BL-012: knowledge-table-origin-column-backport
  - BL-020: sync-worker-target-commit
  - BL-031: automation-manager-session
  - BL-064: skill-plugin-overlap-check-rule
  - BL-072: session-artifacts-structure-refactor
- [x] 特記事項：前回トリアージ（20260317）で BL-084〜BL-093 を新規追加済み。BL-076/077 の二重採番を BL-084/085 に再割当済み

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：36 件
- [x] ステータス「方針確定」（未タスク化）：1 件
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：ISS-067（BL ID 二重採番）は前回トリアージで起票済み

## 進行中 initiative 確認

- [x] 進行中：2 件
  - backlog-id-and-issue-template — タスク 0/5 未着手（3日間停滞）
  - impl-worker-worklog-reliability — タスク 0/5 未着手（3日間停滞）
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：6 件
  - backlog-to-issue-status-sync（2026-03-17 通過）
  - csv-conflict-prevention（2026-03-16 通過）
  - l1-manager-enhanced-planning（2026-03-17 通過、Phase 3 完了）
  - session-cost-measurement（2026-03-18 通過）
  - session-lifecycle-policy-rename（2026-03-17 通過）
  - skill-plugin-overlap-check-rule（2026-03-16 通過）
- [x] ゲート未完了：3 件
  - external-repo-cleanup-on-demand（テンプレート状態）
  - sync-worker-target-commit（テンプレート状態）
  - triage-phase-gate-and-gha-sync（テンプレート状態）

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：4 件
- [x] 処理候補のエントリ（タイトル列挙）：
  - backlog-entry-minimum-description.md — BM-005 ウォークスルーからの気づき
  - bm-001-threshold-tiering.md — BM 20260317 からの気づき
  - bm-report-to-backlog-trigger.md — BM 20260317 からの気づき
  - claude-templates-update-checklist.md — cost-effectiveness-eval-framework からの気づき

## refs/ 孤立エントリ確認

- [x] 孤立エントリ（inbox/ref_*.md なし）：4 件
  - refs/agency-agents/ — inbox ポインターなし
  - refs/ai-driven-dev-patterns/ — inbox ポインターなし（knowledge.md あり）
  - refs/claude-code-action/ — inbox ポインターなし（knowledge.md あり）
  - refs/test/ — inbox ポインターなし（ジョブログファイル）

## ルール・workflow 整合性確認（.claude/rules/*.md ↔ docs/workflow.md）

- [x] 乖離なし（前回 20260317 で確認済み、以降の変更は session-consistency-manager 関連の 2 コミットのみ）

## GHA ↔ Skills 整合性確認

- [x] `.github/gha-skills-mapping.yml` の存在確認：あり
- [x] 前回トリアージ以降に `.claude/skills/` または `.github/prompts/` に変更があったか：あり（session-consistency-manager 関連 2 コミット）

## 前回トリアージからの変化

- 前回実施日：2026-03-17
- inbox 増減：+9 件（全て新規。前回処理済みアイテムは削除済み）
- backlog 増減：±0 件（前回で BL-084〜BL-093 追加済み、それ以降の追加なし）
- 完了施策：session-cost-measurement（新たにゲート通過）
- 新規課題：なし

## 調査サマリ・今回の重点

- 重点1：inbox 9 件の分類・処理（改善提案 5 件 + 気づきエントリ 4 件）
- 重点2：アーカイブ待ち 6 施策の確認・レポート記載
- 重点3：refs/ 孤立エントリ 4 件のユーザー確認依頼
- 重点4：session-consistency-manager 関連変更の GHA 整合性確認

## ワーカーセット数の推奨

- 走査ボリューム見積もり：inbox 9 件 + backlog 突合 8 件 + CSV 37 件 = 合計 54 件
- ただし前回トリアージから 1 日しか経過しておらず、backlog・CSV は大半が確認済み
- 実質的な新規走査対象：inbox 9 件 + initiatives 突合 11 件 + GHA 変更確認 = 約 22 件
- 推奨：全フェーズ 1 セットで逐次実行（低ボリューム扱い）
  - Phase 1〜2 の TG タスクを1セットにまとめる
  - TG-008: 前回（20260317）で走査済み、新規スキル変更は session-consistency-manager のみ → 差分チェックに限定
  - TG-009: 削除・統合候補の有無に応じて実施判断
  - TG-010: session-consistency-manager 関連変更の GHA 整合性のみ差分チェック

---
**調査者**: トリアージセッション
**調査日**: 2026-03-18
