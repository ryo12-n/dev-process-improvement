# トリアージ事前調査: 2026-03-12

## inbox 確認

- [x] 未処理アイテム数：24 件
- [x] 最古アイテムの日付：不明（git blame 未実施、ただし ref_* 系は 2026-03-04 以前から存在）
- [x] 注目すべきアイテム（タイトル列挙）：
  - meta_* 系 6件（メタ認知 20260311 セッションからの気づき）
  - ai-driven-dev-patterns-builtin-skills-eval.md（ADP側ビルトインスキル評価提案）
  - user-invocable-false-description-pattern.md（スキル設定パターン提案）
  - rules-skills移動時の波及更新パターン.md
  - sync-worker同期先コミット漏れ防止.md（backlog にも同名エントリあり）

## backlog 確認

- [x] 総件数：36 件（CSV 行数、空行除く）
- [x] 優先度 高：2 件（SessionStart-hookブランチ整理自動化、Claude Code標準plugin・skills情報整理）
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古は 2026-02-25 で15日）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：要ワーカー走査
- [x] ステータス「完了」残存：1 件（AI補助自動化ツール検討 — entries/ にファイル残存）
- [x] 特記事項：
  - sync-worker同期先コミット漏れ防止 が inbox と backlog entries 両方に存在（重複可能性）
  - backlog.csv 末尾行 38 が空行

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：24 件
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] ステータス「タスク化済」：1 件（ISS-041）
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：
  - ISS-052〜055 は 20260311 メタ認知セッションで新規起票
  - ISS-041 はタスク化済みだがクローズ判定未実施

## 進行中 initiative 確認

- [x] 進行中：1 件
  - external-repo-cleanup-on-demand：08_gate_review.md がテンプレート状態（未完了）
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：0 件
  - builtin-skills-evaluation、claude-dir-optimization-adp は _archive/ に移動済み

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：14 件（meta_* 6件 + 通常 8件）
- [x] 処理候補のエントリ（タイトル列挙）：
  - meta_csv-status-update-mechanism.md
  - meta_knowledge-routing-iss-id.md
  - meta_routing-execution-verification.md
  - meta_rule-change-checklist-docs-scope.md
  - meta_scan-mode-and-set-granularity.md
  - meta_scan-report-change-reason.md
  - ai-driven-dev-patterns-builtin-skills-eval.md
  - user-invocable-false-description-pattern.md
  - rules-skills移動時の波及更新パターン.md
  - sync-worker同期先コミット漏れ防止.md
  - agentsの公式ディレクトリ分け.md
  - entries-pattern-inbox適用検討.md
  - session-flow-checklist-precision.md
  - triage-standard-policy-table-width.md
  - triage-metacognition テンプレート共通化検討.md
  - チェックリスト型スキルの標準テンプレート化.md
  - 条件付き固定タスク適用条件パスパターン重複.md
  - 条件付き固定タスク配置ルール整備.md
  - 費用対効果評価フレームワークの標準化.md
  - 適用マトリクス列数増加リスク.md

## ルール・workflow 整合性確認（.claude/rules/*.md ↔ docs/workflow.md）

- [ ] 要ワーカー走査（TG-008 スコープ）

## 前回トリアージからの変化

- 前回実施日：2026-03-09
- inbox 増減：+10 件程度（meta_* 6件 + 通常 4件が新規追加）
- backlog 増減：+2 件（Claude Code標準plugin・skills情報整理、施策間の競合防止方針策定）
- 完了施策：builtin-skills-evaluation（アーカイブ済み）、claude-dir-optimization-adp（アーカイブ済み）
- 新規課題：ISS-052〜055（メタ認知 20260311 で起票）

## 調査サマリ・今回の重点

- 重点1：meta_* 気づきエントリ 6件の処理判断（メタ認知セッションからのプロセス改善提案）
- 重点2：inbox 24件の分類・処理（特に backlog との重複チェック）
- 重点3：backlog 36件の施策化済みチェック・関係性分析

## ワーカーセット数の推奨

- 走査ボリューム見積もり：inbox 20 件 + backlog 36 件 + CSV 26 件 = 合計 82 件
- 推奨セット数：2 セット（ボリュームは 51件以上だが前回から3日で大部分がキャリーオーバー。新規追加は inbox 10件 + CSV 4件）
- 割り当て方針：
  - Set-1: TG-001（inbox 走査 24件）、ルール・workflow 整合性、README 整合性、参考資料ステータスチェック
  - Set-2: TG-002（backlog 施策化済みチェック）、TG-005（backlog 関係性分析）、CSV 棚卸し、refs/ 孤立エントリ確認

---
**調査者**: トリアージセッション
**調査日**: 2026-03-12
