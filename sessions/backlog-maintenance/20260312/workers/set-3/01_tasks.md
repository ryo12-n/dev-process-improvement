# ワーカータスク指示: Set-3

## 割り当て BM タスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| BM-005 | backlog/entries/ 横断 | 全52件の backlog エントリのタイトル・課題内容を横断比較し、類似テーマ・重複スコープのエントリを検出する。統合候補のペアについて統合の妥当性と統合後の施策名・スコープ案を記録する | 重複・統合候補が一覧化され、統合案が記載されている |

## 走査時の注意事項

- 事前調査で以下のテーマクラスターが検出されている。これらを起点に横断比較を実施すること：
  - **hooks 系**: SessionStart-hookブランチ整理自動化、PreToolUse-hookコミットメッセージバリデーション、PostToolUse-hookルール変更連動チェック（3件）
  - **agents 系**: agentsの公式ディレクトリ分け、agentsの管理方法のガイドライン追記、role-format-guideのagents対応更新（3件）
  - **テンプレート系**: チェックリスト型スキル標準テンプレート化、triage-metacognitionテンプレート共通化検討、sessionsテンプレート間連携ガイド（3件）
  - **ai-driven-dev-patterns 横展開系**: ai-driven-dev-patterns-triage-standard-policy作成、ai-driven-dev-patterns-builtin-skills-eval、メタ認知セッションのai-driven-dev-patterns展開、ai-driven-dev-patterns_source-of-truth明示（4件）
  - **同期系**: 同期対象リスト管理と差分ベース反映計画、sync-worker同期先コミット漏れ防止（2件）
  - **コンテキスト最適化系**: 長文rulesのコンテキストコスト最適化、permission-prompt-optimization、disallowedToolsフィールド活用検討（3件）
- 上記クラスター以外にも類似エントリがないか全件を確認すること
- 統合候補は「完全重複」「部分重複（統合推奨）」「テーマ近接（個別管理推奨）」の3段階で分類すること

---
**作成者**: バックログメンテナンスマネージャー
**作成日**: 2026-03-12
