# ワーカータスク指示: Set-1

## 割り当て AT タスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| AT-001 | .claude/skills/, .claude/rules/, sessions/*/, docs/ | 前回（20260316）以降に追加・変更された skills/rules に伴う新たな定型作業を検出する | 走査対象の主要ファイルがチェックされ、新規候補が一覧化されている |
| AT-002 | automation-candidates/entries/*.md, CSV | 全16候補の優先度スコア・実装難易度・自動化手段の妥当性を環境変化に基づき再評価する | 全エントリの再評価が完了し、変更提案が一覧化されている |

## 補足指示

### AT-001 の重点走査対象

前回（20260316）以降に追加・変更されたスキル・ルール（計9コミット、46ファイル変更）:

- **新規追加**: session-consistency-manager（SKILL.md + agents 4ファイル + reference）、manager-overview（SKILL.md）
- **大幅更新**: triage-manager（112行追加）、l1-manager（enhanced-planning 関連）、l1-impl-manager（refs-knowledge-read 関連）
- **リネーム**: session-lifecycle-policy（旧 triage-standard-policy）
- **rules 変更**: commit-message.md（sc-mgr/sc-worker/sc-eval 追加）、gha-workflow-security.md、parallel-dev.md

既に登録済みの AC-001〜AC-016 との重複に注意すること。

### AT-002 の重点確認対象

- AC-002（コミットメッセージ hook）: BL-029 として backlog 起票済み。施策化状況を確認
- AC-012（ルール変更連動チェック hook）: BL-030 として backlog 起票済み。施策化状況を確認
- 前回の申し送り: 「BL-029, BL-030 の施策化状況を追跡」「候補管理の運用ガイドライン整備を検討」

---
**記入者**: オートメーションマネージャー
