# トリアージ事前調査: 2026-03-19

<!-- 実施前にこのテンプレートを埋めること。調査結果を 01_plan.md の判断材料とする。 -->

## inbox 確認

- [x] 未処理アイテム数：15 件
- [x] 最古アイテムの日付：2026-03-17（推定）
- [x] 注目すべきアイテム（タイトル列挙）：
  - SC-007スキャン手順改善_括弧内包含記述の確認.md — SC-007 走査手順にサブタイプ括弧内包含検出を追加
  - SCチェック後のアクション接続明確化.md — SC チェック結果→backlog/inbox への接続フロー定義
  - automation-20260318-count-definition.md — AT-002 変更提案数カウント定義の曖昧さ解消
  - automation-20260318-integration-score.md — AT-004 統合 backlog の優先度スコア算出方法
  - dispatcher-reject-retry-count-explicit.md — initiative-dispatcher reject ルートの retry_count 明示
  - gha-claude-dir-write-restriction.md — GHA 環境の .claude/ 書き込み制約と回避策
  - gha-constraint-check-in-proposal.md — 00_proposal テンプレートへの GHA 制約事前チェック追加
  - gha-metadata-extraction-composite-action.md — GHA メタデータ抽出ロジックの共通化提案
  - gha-task-division-step-name-reference.md — タスク分割ファイルでのステップ名参照推奨
  - gha-verdict-step-separation-pattern.md — GHA verdict/dispatch ステップ分離パターン
  - meta-rule-checklist-integration-proposal.md — l1-manager 固定タスクのメタルール/チェックリスト統合
  - non-initiative-cost-tracking.md — 非施策セッションへのコスト追跡拡張
  - success-criteria-grep-scope.md — 成功基準 grep スコープ制限ガイドライン
  - template-md-path-reference-check.md — テンプレート .md のパス参照走査対象追加
  - template-new-file-update-pattern.md — テンプレートファイル追加時の5ステップパターン定義

## backlog 確認

- [x] 総件数：104 件
- [x] 優先度 🔴（高）：11 件
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古エントリは 2026-02-25 で24日）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：前回 8 件検出済み、差分要確認
  - 前回検出分を引き継ぎ、新規 BL-095〜BL-106 との突合が必要
- [x] 特記事項：
  - 対象リポジトリ未記入エントリ：0 件（全エントリ記入済み）
  - BL-084: 並列セッション環境でのBL ID衝突防止（高優先度）
  - BL-104: SC-008 壊れた参照修正（高優先度）

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：37 件
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] 最古の未対応課題：ISS-013（日付要確認）
- [x] 特記事項：
  - 高優先度の未対応課題: ISS-059（GHA インジェクションリスク）、ISS-061（deny ルール非機能）、ISS-064（テストスクリプト未設定）、ISS-068（GHA .claude/ 書き込み制約）
  - ISS-066: CSV/md ステータス不一致（自動生成信頼性への影響）

## 進行中 initiative 確認

- [x] 進行中：5 件
  - external-repo-cleanup-on-demand: ゲートレビューテンプレートのみ（未判定）
  - sync-worker-target-commit: ゲートレビューテンプレートのみ（未判定）
  - triage-phase-gate-and-gha-sync: ゲートレビューテンプレートのみ（未判定）
  - backlog-id-and-issue-template: ゲートレビュー未作成
  - impl-worker-worklog-reliability: ゲートレビュー未作成
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：7 件
  - backlog-to-issue-status-sync
  - csv-conflict-prevention
  - l1-manager-checklist-integration
  - l1-manager-enhanced-planning
  - session-cost-measurement
  - session-lifecycle-policy-rename
  - skill-plugin-overlap-check-rule

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：15 件（全件が気づきエントリ）
- [x] 処理候補のエントリ（タイトル列挙）：
  - ルール改善系 9 件: SC-007, SCチェック後アクション, automation-count, automation-integration-score, dispatcher-retry, gha-verdict-step, meta-rule-checklist, success-criteria-grep, template-path-reference
  - backlog 候補系 4 件: gha-constraint-check-in-proposal, gha-metadata-extraction-composite-action, non-initiative-cost-tracking, template-new-file-update-pattern
  - ルール/docs 両方 1 件: gha-claude-dir-write-restriction
  - ルール改善系 1 件: gha-task-division-step-name-reference

## ルール・workflow 整合性確認（.claude/rules/*.md ↔ docs/workflow.md）

- [x] 前回トリアージ以降に多数のスキル変更あり（sc-mgr, l1-manager 等）→ ワーカー走査で確認

## GHA ↔ Skills 整合性確認

- [x] `.github/gha-skills-mapping.yml` の存在確認：あり
- [x] 前回トリアージ以降に `.claude/skills/` または `.github/prompts/` に変更があったか：あり（7コミット）

## refs/ 孤立エントリ確認

- [x] refs/ に 5 エントリ（_knowledge_template.md, _work_log_template.md, agency-agents, ai-driven-dev-patterns, claude-code-action, test）
- [x] inbox/ref_* ポインター：0 件
- [x] 孤立状態: 全エントリがポインターなし → ユーザーに確認が必要

## 前回トリアージからの変化

- 前回実施日：2026-03-18
- inbox 増減：+15 件（前回 9 件→全件処理→新規 15 件追加）
- backlog 増減：+10 件（94→104）
- 完了施策：直近アーカイブ 5 件（phase-worker-set-standardization 等）
- 新規課題：ISS-065〜ISS-068（4 件）

## 調査サマリ・今回の重点

- 重点1：inbox 15 件の分類・処理（全件が前回以降の新規エントリ、GHA 関連が多い）
- 重点2：アーカイブ待ち 7 件の initiative の処理
- 重点3：backlog 突合（新規 BL-095〜BL-106 の施策化状況確認）

## ワーカーセット数の推奨

- 走査ボリューム見積もり：inbox 15 件 + backlog 突合 10 件（新規分） + CSV 37 件 = 合計 62 件
- ただし前回から1日しか経過しておらず、backlog/CSV の大部分は前回確認済み
- 実質的な走査対象: inbox 15 件 + backlog 新規 10 件 + アーカイブ確認 7 件 + 整合性チェック = 約 35 件
- 推奨セット数：Phase 1 で 2 セット、Phase 2 以降は Phase 1 の結果次第で 1〜2 セット
- 割り当て方針：
  - Phase 1 set-1: TG-001（inbox 15件）、TG-003（CSV確認）
  - Phase 1 set-2: TG-004（initiative確認・アーカイブ待ち7件）、TG-007（refs孤立確認）
  - Phase 2a: TG-002（backlog突合）、TG-006（workflow整合性）、TG-008（セッション構造チェック）
  - Phase 2b: TG-005（backlog関係性分析）
  - Phase 2c: TG-009（情報欠損リスク評価、候補あれば）
  - Phase 3: TG-010（GHA整合性）

---
**調査者**: トリアージセッション
**調査日**: 2026-03-19
