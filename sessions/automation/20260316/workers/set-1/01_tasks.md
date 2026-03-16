# ワーカータスク指示: Set-1

## 割り当て AT タスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| AT-001 | `.claude/skills/`, `.claude/rules/`, `sessions/*/`, `docs/` | 直近2週間のスキル・ルール追加・変更に伴い新たに生まれた定型作業を検出する | 走査対象の主要ファイルがチェックされ、新規候補が一覧化されている |
| AT-002 | `automation-candidates/entries/*.md`, CSV | 全14候補の優先度スコア・実装難易度・自動化手段の妥当性を環境変化に基づき再評価する | 全エントリの再評価が完了し、変更提案が一覧化されている |
| AT-003 | `backlog/entries/*.md`, `sessions/initiatives/`, `_archive/` | backlog起票済み候補（AC-001）の施策化・実装状況を追跡する。特にAC-001は hook 実装済みなのでステータス確認 | backlog起票済・施策化済ステータスの全候補の進捗が確認されている |
| AT-004 | AT-001〜AT-003 の結果 | 新規候補や優先度変更候補を backlog エントリとして起票提案する | 起票提案が具体的な理由とともに一覧化されている |

## 補足指示

- **初回メンテナンス**: 前回メンテナンス結果がないため、全候補を網羅的にスキャンすること
- **AC-001 重点確認**: SessionStart hook（`.claude/hooks/session-start-branch-cleanup.sh`）として実装済み。`sessions/initiatives/_archive/` の関連施策と合わせてステータス更新提案を作成すること
- **新規 rules 5件**: commit-message.md, gha-workflow-security.md, pr-url-output.md, rebase-conflict-handling.md, session-start-branch-cleanup.md — これらに関連する定型作業がないか重点チェック
- **新規 skills**: automation-manager, config-optimizer-manager, l1-impl-manager, GHA スキル群 — テンプレート操作・定型フロー等の自動化余地を確認
- **backlog との対応**: BL-029（AC-002関連）、BL-030（AC-012関連）、BL-067、BL-082 等 hook 関連エントリとの整合性確認

---
**記入者**: オートメーションマネージャー
