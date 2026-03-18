# ワーカータスク指示: Set-1

## 割り当て BM タスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| BM-001 | backlog/entries/ | 起票日からの経過日数をチェックし、90日以上の長期滞留エントリを検出する。全エントリが30日未満のため形式チェック + 経過日数分布サマリのみで可 | 全エントリの経過日数が算出され、長期滞留が一覧化（0件見込み）。経過日数の分布（Top5最古）を記録 |
| BM-002 | backlog/entries/ vs _archive/ + 完了施策 | 以下17件の完了施策で解消された backlog エントリを検出する | 全92件の backlog エントリの解決状況が確認され、解消済みが一覧化されている |

## BM-002 照合対象の完了施策一覧

### アーカイブ済み施策（前回BM以降: 12件）

1. gha-issue-usage-guide — GHA Initiative ワークフローコメントにコマンドリファレンス追加
2. agency-agents-integration — agency-agents リポジトリの refs/ 統合・ドメインエージェントカタログ作成
3. backlog-to-issue-scheduled — backlog-to-issue スケジュールトリガー（6時間間隔）実装
4. gha-wallbash-iterative-phase — 壁打ちフェーズの分離・反復可能化（/continue コマンド）
5. gha-session-prompt-conversion-pattern — CLI→GHA 変換パターン文書化
6. backlog-template-legend-enhancement — backlog テンプレート凡例強化・環境前提セクション追加
7. refs-work-log-directory — refs/ 二層構造（work-logs/ + knowledge.md）確立
8. dev-workflow-detail-l1-ref-review — dev-workflow-detail.md の L1 参照精査
9. gha-initiative-skills-separation — CLI/GHA スキル分離（4つの GHA 専用スキル作成）
10. automation-action-step — automation-manager Step 7 アクション実行の詳細化
11. session-artifacts-structure-refactor — config-optimizer/impl テンプレートのフェーズ別ディレクトリ化
12. backlog-to-issue-schedule-frequency — backlog-to-issue スケジュール頻度を6h→3hに変更

### 未アーカイブ完了施策（ゲート通過済み: 5件）

13. backlog-to-issue-status-sync — backlog エントリのステータス変更を GitHub Issue に同期
14. csv-conflict-prevention — CSV コンフリクト防止（.md → CSV 自動生成）
15. skill-plugin-overlap-check-rule — skill/plugin 重複チェックルール CO-008 追加
16. l1-manager-enhanced-planning — L1 マネージャー拡張計画（並列ディスパッチ・plan-worker/evaluator）
17. session-lifecycle-policy-rename — session-phase → session-lifecycle リネーム

## 走査時の注意事項

- BM-001: 0件検出見込み。経過日数 Top5 最古エントリの一覧と、全体の経過日数分布サマリを記録すること
- BM-002: backlog エントリの「背景・課題」「改善提案」と完了施策の内容を照合する。部分的解消も検出対象
- BM-002: ステータスが「完了」の7件は既に解消済みのためスキップ可。残り85件（候補84 + initiative開始済1）を走査対象とする
- BM-002: 解消確度は「確実 / 可能性あり / 部分的解消」の3段階で記録する

---
**作成者**: バックログメンテナンスマネージャー
**作成日**: 2026-03-17
