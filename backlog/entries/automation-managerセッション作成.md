# automation-managerセッション作成

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-031 |
| **優先度** | 🟡 中 |
| **ステータス** | 完了 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | automation-manager-session |
| **起票日** | 2026-03-10 |

## 課題・背景

施策「AI補助自動化ツール検討」で定型作業14件の洗い出し・費用対効果評価・ロードマップ策定を完了した。しかし現状では自動化候補の探索が一度きりの施策として実施されており、以下の課題がある。

- **新たな定型作業の見逃し**: skills/rules/agents の追加・変更に伴い新たな自動化候補が生まれるが、継続的に検出する仕組みがない
- **既存候補の陳腐化**: 優先度や実装難易度は環境変化で変わるが、再評価の機会がない
- **実装進捗の追跡不足**: hook 化などの自動化施策が backlog に起票されても、全体の進捗を俯瞰する場がない

## 期待効果

- 自動化候補の探索・評価・追跡を定期セッションとして制度化し、継続的な改善サイクルを確立する
- triage-manager / metacognition-manager と同様の定期実行型マネージャーセッションとして、既存アーキテクチャに統合する
- 費用対効果フレームワーク（頻度 × 手動コスト / 実装難易度）を標準化し、客観的な優先順位付けを行う

## 補足・参考情報

- **先行施策**: `sessions/initiatives/_archive/ai-automation-tool-review/` の成果物（評価フレームワーク・ロードマップ）をベースとする
- **成果物スコープ**: `.claude/skills/automation-manager/SKILL.md`, `agents/automation-worker.md`, `agents/automation-evaluator.md`, `sessions/automation/_template/`, `docs/workflow.md` 更新, `commit-message.md` 更新, `session-lifecycle-policy` ライフサイクル行列更新
- **ワーカータスク案**: AT-001（新規自動化候補スキャン）、AT-002（既存候補の再評価）、AT-003（実装進捗確認）、AT-004（backlog 起票提案）
- **コミットプレフィックス**: `[auto-mgr]`, `[auto-worker]`, `[auto-eval]`
- **関連 backlog**: SessionStart-hookブランチ整理自動化（行39）、PreToolUse-hookコミットメッセージバリデーション（行40）、PostToolUse-hookルール変更連動チェック（行41）は、本セッションで追跡対象となる自動化施策の例
