# オートメーションメンテナンス事前調査: 2026-03-16

## automation-candidates 全体確認

- [x] 総エントリ数：14 件
- [x] ステータス「候補」：13 件（AC-002〜AC-014）
- [x] ステータス「backlog起票済」：1 件（AC-001）
- [x] ステータス「施策化済」：0 件
- [x] ステータス「実装完了」：0 件
- [x] ステータス「却下」：0 件
- [x] 最終評価日が最も古い候補：全候補が 2026-03-10（初回評価時の一括登録）
- [x] 特記事項：AC-001（セッション開始時のブランチ整理）は hook 実装済みで SessionStart hook として稼働中。ステータスを「実装完了」に更新提案

## automation-candidates.csv とファイル実体の整合性

- [x] CSV にあってファイルがないエントリ：0 件
- [x] ファイルがあって CSV にないエントリ：0 件
- [x] 整合性チェック結果：OK

## スキル・ルールの変更状況

### 前回メンテナンス以降の追加・変更

前回メンテナンス：なし（初回実施）。直近2週間（2026-03-02〜）の変更を対象とする。

- [x] `.claude/rules/` の変更：5 ファイル新規追加
  - commit-message.md, gha-workflow-security.md, pr-url-output.md, rebase-conflict-handling.md, session-start-branch-cleanup.md
- [x] `.claude/skills/` の変更：多数（40+ ファイル）
  - 新規: automation-manager, config-optimizer-manager, l1-impl-manager（各エージェント含む）
  - GHA スキル群: gha-close, gha-execute, gha-guideline, gha-question, gha-test, gha-wallbash
  - 更新: manager-common-policy, triage-manager, sync-manager, metacognition-manager, session-flow-policy, rule-change-checklist
- [x] `sessions/*/` テンプレートの変更：automation テンプレート新規作成
  - sessions/automation/_template/ 一式

## 自動化関連の施策・backlog 確認

### 進行中施策（sessions/initiatives/）

- [x] 自動化関連施策：2 件
  - external-repo-cleanup-on-demand: L2評価フェーズ（AC-014 関連）
  - impl-worker-worklog-reliability: L1計画フェーズ

### アーカイブ済み施策（sessions/initiatives/_archive/）

- [x] 自動化関連のアーカイブ：3 件
  - automation-manager-session: automation-manager スキル作成（BL-031 → 完了）
  - gha-initiative-skills-separation: GHA スキル分離
  - backlog-to-issue-scheduled: backlog → issue 定期変換

### backlog 内の自動化関連エントリ

- [x] 自動化関連 backlog エントリ：7 件
  - BL-029: PreToolUse-hook コミットメッセージバリデーション（中・候補）← AC-002 関連
  - BL-030: PostToolUse-hook ルール変更連動チェック（中・候補）← AC-012 関連
  - BL-053: L1マネージャー実作業禁止の構造的強制（中・候補）
  - BL-055: gha-backlog-maintenance-automation（中・候補）
  - BL-057: gha-metacognition-automation（中・候補）
  - BL-067: pretooluse-hook-security-guard（高・候補）
  - BL-082: posttooluse-hook-quality-check（中・候補）

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] 自動化関連の未対応課題：1 件
  - ISS-060: 新セッションタイプ追加時の manager-common-policy §1/§9 連動更新漏れ（automation-manager 追加時の不備）
- [x] 特記事項：ISS-061（settings.json deny rules non-functional）、ISS-062（PreToolUse hook pattern matching bypass risk）は hook 実装の前提条件に影響する可能性あり

## 前回メンテナンスからの変化

- 前回実施日：なし（初回実施）
- automation-candidates 増減：— （初回）
- 新規スキル・ルール追加：rules 5件、skills 多数（上記参照）
- 環境変化：GHA ワークフロー群の整備、config-optimizer/l1-impl-manager の新設、SessionStart hook の稼働開始

## 調査サマリ・今回の重点

- 重点1：AC-001（ブランチ整理）は既に hook 実装済み → ステータス更新提案
- 重点2：直近2週間のスキル・ルール大幅追加に伴う新規自動化候補の検出（AT-001）
- 重点3：既存14候補の優先度・実装難易度の再評価（環境変化を反映）

## ワーカーセット数の推奨

- automation-candidates エントリ数：14 件
- 推奨セット数：1 セット（≤15件 → 1セット）
- 割り当て方針：全ATタスク（AT-001〜AT-004）を1セットで実施

---
**調査者**: オートメーションマネージャー
**調査日**: 2026-03-16
