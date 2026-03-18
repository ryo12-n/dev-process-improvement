# ワーカータスク指示: Set-3

## 割り当て BM タスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| BM-003 | backlog/entries/ の前提条件 | 前提条件が変化したエントリを検出する。前回BM申し送り5件のスコープ更新確認含む | 全エントリの前提条件が現状と照合され、変化があるエントリが一覧化されている |
| BM-004 | backlog/entries/ の優先度 | 優先度の妥当性をレビューする。前回BM提案の反映状況確認含む | 全エントリの優先度妥当性がレビューされ、変更候補が一覧化されている |

## set-1/set-2 の結果（参照用）

### set-1 結果（BM-002: 解決状況確認）
- 部分的解消 4件: BL-033, BL-052, BL-077, BL-084
  - これらは完全解消ではないため、前提変化（BM-003）や優先度再評価（BM-004）の対象として考慮すること
- CSV/mdステータス不一致 4件: BL-004, BL-010, BL-012, BL-072（課題として起票済み）

### set-2 結果（BM-005: 重複・統合候補）
- 統合候補（高）3組: BL-054+BL-065, BL-055+BL-057, BL-030+BL-082
- 統合検討候補（中）7組（詳細は set-2 の 04_scan_report.md 参照）
- 統合候補に含まれるエントリの優先度は統合後の方針に依存するため、BM-004 では現状の優先度妥当性のみ評価すること

## BM-003 走査方針

### 前回BM申し送り: 5件のスコープ更新確認（roles/ → agents/ パス変更）
以下の5件が前回 BM で「スコープ更新が必要」と指摘されている。対応状況を確認すること:
1. 全ロールファイルrole-format-guide準拠確認修正
2. ハーネスエンジニアリング観点でのブラッシュアップ
3. 高度な並列化と協調プロトコル統合
4. dev-workflow-detail L1参照精査
5. ai-driven-dev-patterns_source-of-truth明示

### 環境変化チェックリスト
前回BM（2026-03-12）以降の主な環境変化:
- `.claude/rules/parallel-dev.md` 追加: 並列ディスパッチルール（Conflict Check Matrix, Wave, per-worker ファイル）
- `.claude/rules/gha-workflow-security.md` 追加: GHA セキュリティチェックリスト
- `.claude/rules/rebase-conflict-handling.md` 追加: rebase コンフリクト対応
- csv-conflict-prevention 施策完了: CSV は .md から自動生成に移行
- l1-manager-enhanced-planning 完了: plan-worker/evaluator 導入、並列ディスパッチ対応
- session-lifecycle-policy-rename 完了: triage-standard-policy → session-lifecycle-policy
- agency-agents-integration 完了: ドメインエージェント参照の仕組み確立

### 前提変化の影響分類
| 影響 | 定義 |
|------|------|
| 不要化 | 前提変化により施策自体が不要になった |
| スコープ変更が必要 | 前提変化により施策の範囲・内容の修正が必要 |
| 影響なし | 前提変化があるが施策内容に影響しない |

## BM-004 走査方針

### 前回BM提案の反映状況確認
前回 BM で以下の3件の優先度変更（中→高）が提案されている:
1. リンク整合性チェック標準化（ISS-054/ISS-042/MC-001 で繰り返し指摘）
2. sync-worker同期先コミット漏れ防止（小スコープ・即修正可能）
3. L2知見発見と修正適用のギャップ改善（ISS-052 根因）

### 優先度評価の観点
- 現在の課題管理状況（issues/entries/ の関連課題）との整合性
- 進行中・完了施策との関係（依存解消・前提変化による優先度変動）
- エントリの記述内容と現状の乖離度

## 走査時の注意事項

- ステータスが「完了」の7件は走査対象から除外可
- BM-003 は全85件（候補84 + initiative開始済1）を走査対象とする
- BM-004 は優先度変更が必要と判断したエントリのみ詳細に記載（全件の優先度妥当性確認は行うが、変更不要のエントリは一覧化不要）
- set-1/set-2 の結果は `sessions/backlog-maintenance/20260317/workers/set-1/04_scan_report.md` と `sessions/backlog-maintenance/20260317/workers/set-2/04_scan_report.md` で参照可能

---
**作成者**: バックログメンテナンスマネージャー
**作成日**: 2026-03-17
