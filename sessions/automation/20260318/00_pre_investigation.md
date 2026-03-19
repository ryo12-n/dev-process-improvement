# オートメーションメンテナンス事前調査: 2026-03-18

## automation-candidates 全体確認

- [x] 総エントリ数：16 件
- [x] ステータス「候補」：11 件（AC-003〜AC-011, AC-013〜AC-016）
- [x] ステータス「backlog起票済」：2 件（AC-002, AC-012）
- [x] ステータス「施策化済」：0 件
- [x] ステータス「実装完了」：1 件（AC-001）
- [x] ステータス「却下」：0 件
- [x] 最終評価日が最も古い候補：全候補 2026-03-16（前回初回メンテナンスで一斉評価）
- [x] 特記事項：前回（20260316）が初回メンテナンス。新規候補 AC-015, AC-016 が追加されたばかり

## automation-candidates.csv とファイル実体の整合性

- [x] CSV にあってファイルがないエントリ：0 件
- [x] ファイルがあって CSV にないエントリ：0 件
- [x] 整合性チェック結果：OK

## スキル・ルールの変更状況

### 前回メンテナンス以降の追加・変更

- [x] `.claude/skills/` の変更：46 ファイル（9コミット）
  - 変更内容：
    - session-consistency-manager 新規追加（SKILL.md + agents 4ファイル + reference 1ファイル）
    - manager-overview 新規追加（SKILL.md）
    - l1-manager-enhanced-planning 関連変更（l1-manager, l1-impl-manager 等の更新）
    - session-lifecycle-policy リネーム（triage-standard-policy → session-lifecycle-policy）
    - triage-manager 大幅更新（112行追加）
    - manager-common-policy 更新
    - config-optimizer-manager 更新
    - backlog-maintenance-manager 更新
    - gha-close, gha-execute 更新
    - impl-manager-refs-knowledge-read 関連変更
- [x] `.claude/rules/` の変更：3 ファイル
  - 変更内容：commit-message.md（sc-mgr/sc-worker/sc-eval 追加）、gha-workflow-security.md（更新）、parallel-dev.md（更新）
- [x] `sessions/*/` テンプレートの変更：確認なし（テンプレート自体の変更は検出されず）

## 自動化関連の施策・backlog 確認

### 進行中施策（sessions/initiatives/）

- [x] 自動化関連施策：0 件（直接的な自動化実装施策は進行中にない）
  - 関連: l1-manager-enhanced-planning（計画フェーズの強化、間接的に自動化の品質向上に寄与）

### アーカイブ済み施策（sessions/initiatives/_archive/）

- [x] 自動化関連のアーカイブ：多数（automation-manager-session, backlog-auto-initiative-gha, session-branch-cleanup-flow 等）
  - 直近のアーカイブ：automation-action-step（自動化マネージャーのアクション実施ステップ追加）

### backlog 内の自動化関連エントリ

- [x] 自動化関連 backlog エントリ：4 件
  - BL-031: automation-manager セッション作成 → 完了
  - BL-055: GHA バックログメンテナンスセッション自動化 → 候補
  - BL-057: GHA メタ認知セッション自動化 → 候補
  - BL-089: automation-candidates と backlog のステータス連動更新プロセス明文化 → 候補

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] 自動化関連の未対応課題：1 件
  - ISS-060: 新セッションタイプ追加時の manager-common-policy §1/§9 連動更新漏れ（起票、中優先度）
- [x] 特記事項：前回起票された「候補管理と backlog のステータス乖離」は BL-089 として backlog に起票済み

## 前回メンテナンスからの変化

- 前回実施日：2026-03-16（初回メンテナンス）
- automation-candidates 増減：±0 件（前回で AC-015, AC-016 を登録済み。以降の追加なし）
- 新規スキル・ルール追加：session-consistency-manager（新規）、manager-overview（新規）、rules 3ファイル更新
- 環境変化（ツール追加・プロセス変更等）：
  - session-consistency-manager が新たに運用開始（初回実行 20260317）
  - session-lifecycle-policy にリネーム完了（旧 triage-standard-policy）
  - l1-manager-enhanced-planning により計画フェーズが強化（並列ディスパッチ対応等）
  - triage-manager が大幅更新（Phase ゲートチェック強化等）

## 調査サマリ・今回の重点

- 重点1：新規 session-consistency-manager / manager-overview スキル追加に伴う新たな定型作業の有無を検出（AT-001）
- 重点2：前回の変更提案（AC-001 実装完了、AC-002/AC-012 backlog起票済、AC-010/AC-014 優先度変更）が適切に反映されているか確認（AT-002）
- 重点3：BL-029（AC-002 コミットメッセージ hook）、BL-030（AC-012 ルール変更連動チェック hook）の施策化状況を追跡（AT-003）

## ワーカーセット数の推奨

- automation-candidates エントリ数：16 件
- 推奨セット数：2 セット（16〜30件の範囲に該当）
- 割り当て方針：
  - set-1: AT-001（新規候補スキャン）+ AT-002（既存候補の再評価）— スキャンと再評価は独立して実施可能
  - set-2: AT-003（実装進捗確認）+ AT-004（backlog起票提案）— 進捗確認の結果が起票提案に影響

---
**調査者**: オートメーションマネージャー
**調査日**: 2026-03-18
