# バックログメンテナンス事前調査: 2026-03-17

## backlog 全体確認

- [x] 総エントリ数：92 件（BL-001〜BL-093、BL-061 欠番）
- [x] 優先度 🔴（高）：17 件
- [x] 優先度 🟡（中）：28 件
- [x] 優先度 🔵（低）：47 件
- [x] 優先度未設定：0 件
- [x] 最古エントリの起票日：2026-02-25（マルチAIエージェント共通ルール適用.md）
- [x] 90日以上滞留エントリ：0 件（最古でも20日）
- [x] 特記事項：前回BM（52件）から40件増加。高優先度が2→17に急増（前回BM提案の3件 + triage追加分）

## backlog.csv とファイル実体の整合性

- [x] CSV にあってファイルがないエントリ：0 件
- [x] ファイルがあって CSV にないエントリ：0 件
- [x] 整合性チェック結果：OK（csv-conflict-prevention 施策により .md → CSV 自動生成で整合性維持）

## 施策状況の確認

### 進行中施策（sessions/initiatives/）

- [x] 進行中：10 件
  - backlog-id-and-issue-template: 計画フェーズ（T-001〜T-005 定義済み）
  - backlog-to-issue-status-sync: ゲート通過済み（アーカイブ待ち）
  - csv-conflict-prevention: ゲート通過済み（アーカイブ待ち）
  - external-repo-cleanup-on-demand: 全フェーズ通過（ゲート未記入）
  - impl-worker-worklog-reliability: 計画フェーズ
  - l1-manager-enhanced-planning: ゲート通過済み（アーカイブ待ち）
  - session-lifecycle-policy-rename: ゲート通過済み（アーカイブ待ち）
  - skill-plugin-overlap-check-rule: ゲート通過済み（アーカイブ待ち）
  - sync-worker-target-commit: 差し戻し
  - triage-phase-gate-and-gha-sync: 差し戻し
- [x] backlog との関連：完了施策5件に対応する backlog エントリのステータス更新が必要な可能性

### アーカイブ済み施策（sessions/initiatives/_archive/）

- [x] アーカイブ済み：98 件
  - 直近のアーカイブ：automation-action-step, session-artifacts-structure-refactor, backlog-to-issue-schedule-frequency（2026-03-16）
- [x] 前回メンテナンス以降の新規アーカイブ：12 件
  - 2026-03-15: gha-issue-usage-guide, agency-agents-integration, backlog-to-issue-scheduled, gha-wallbash-iterative-phase, gha-session-prompt-conversion-pattern, backlog-template-legend-enhancement, refs-work-log-directory, dev-workflow-detail-l1-ref-review, gha-initiative-skills-separation（9件）
  - 2026-03-16: automation-action-step, session-artifacts-structure-refactor, backlog-to-issue-schedule-frequency（3件）

## 課題管理 CSV 確認

- [x] backlog 関連の未対応課題：6 件（ISS-058〜ISS-065 のうち backlog/BM 関連）
- [x] 特記事項：ISS-064（高）ai-driven-dev-patterns テストスクリプトパス未設定が TDD フロー非機能に影響

## 前回メンテナンスからの変化

- 前回実施日：2026-03-12
- backlog 増減：+40 件（52 → 92）
- 新規アーカイブ施策：12 件 + 未アーカイブ完了施策 5 件 = 計 17 件
- 環境変化（ルール追加・プロセス変更等）：
  - `.claude/rules/parallel-dev.md` 追加（2026-03-17）: 並列ディスパッチルール
  - `.claude/rules/gha-workflow-security.md` 追加（2026-03-15）: GHA セキュリティチェックリスト
  - `.claude/rules/rebase-conflict-handling.md` 追加（2026-03-15）: rebase コンフリクト対応
  - csv-conflict-prevention 施策完了: CSV は .md から自動生成に移行

### 前回 BM 申し送り事項のフォローアップ

| # | 申し送り事項 | 対応状況 |
|---|------------|---------|
| 1 | BM-003: 5件のスコープ更新（roles/ → agents/ パス変更） | 要確認（set-3 で検証） |
| 2 | permission-prompt-optimization 優先度不一致（CSV: 低 vs Entry: 中） | 要確認（set-3 で検証） |
| 3 | BM-005: 差分ベーススキャン推奨 | 今回採用（set-2 で実施） |
| 4 | 3件の優先度変更提案（中→高） | 優先度増加（2→17）を確認。詳細は set-3 で検証 |
| 5 | 3件の統合候補グループ | 要確認（set-2 で検証） |

## 調査サマリ・今回の重点

- 重点1：**BM-002 解決状況確認** — 17件の完了施策（アーカイブ12 + 未アーカイブ完了5）で解消された backlog エントリの特定
- 重点2：**BM-005 重複・統合候補** — 40件の急増（52→92）に伴う重複リスクの検出。差分ベース（BL-054以降 vs 既存）で効率化
- 重点3：**BM-003/BM-004 前提変化・優先度再評価** — 前回申し送りの5件スコープ更新確認 + 優先度急増（2→17）の妥当性検証

## ワーカーセット数の推奨

- backlog エントリ数：92 件
- 推奨セット数：3 セット（> 25件 → 3セット）
- 割り当て方針：
  - set-1: BM-001（簡易）+ BM-002（解決状況確認）— 全エントリ30日未満のため BM-001 は形式チェック。BM-002 は17件の完了施策との照合が主タスク
  - set-2: BM-005（重複・統合候補）— 差分ベースで新規40件 vs 既存52件の横断比較
  - set-3: BM-003（前提変化）+ BM-004（優先度再評価）— set-1/set-2 の結果を踏まえた判断が必要なため最後に実施

---
**調査者**: バックログメンテナンスマネージャー
**調査日**: 2026-03-17
