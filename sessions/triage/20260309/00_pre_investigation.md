# トリアージ事前調査: 2026-03-09

## inbox 確認

- [x] 未処理アイテム数：19 件（うち ref_ ポインター 4件、判断保留 2件、新規 13件）
- [x] 最古アイテムの日付：前回トリアージ（20260308-2）からの判断保留分
- [x] 注目すべきアイテム（タイトル列挙）：
  - L2知見発見と修正適用のギャップ改善.md（プロセス改善の本質的課題）
  - rule-change-checklist_deny対称性チェック追加.md（ISS-050 と直結）
  - backlog-ideas-md整理.md（triage-manager 担当ファイルに ideas.md 記載あるが実ファイル不在）
  - disallowedToolsフィールド活用検討.md（ISS-047 と関連）
  - 複数リポジトリ施策のPR作成漏れ防止.md（外部リポ施策の運用課題）
  - エージェント名ケバブケース規則.md（命名規約の明文化）

## backlog 確認

- [x] 総件数：33 件（CSV）/ 30 件（entries/ ファイル）
- [x] 優先度 🔴（高）：0 件
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古 2026-03-01）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：1 件
  - claude-directory最適化(ai-driven-dev-patterns) → _archive/claude-directory最適化/（前回レポート済み・未回答）
- [x] 特記事項：CSV 33件 vs entries/ 30ファイルの差分要確認

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：23 件
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：ISS-027（高優先度・環境制約）は Claude Code Web のリポ制約で当面対応不可。ISS-051（gh -C 未サポート）は最新で中優先度

## 進行中 initiative 確認

- [x] 進行中：0 件
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：0 件

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：13 件（ref_ 4件と判断保留 2件を除く）
- [x] 処理候補のエントリ（タイトル列挙）：
  - L2知見発見と修正適用のギャップ改善.md
  - agentsの管理方法のガイドライン追記.md
  - backlog-ideas-md整理.md
  - disallowedToolsフィールド活用検討.md
  - entries-pattern-inbox適用検討.md
  - metacognition-managerの記述構造統一検討.md
  - rule-change-checklist_deny対称性チェック追加.md
  - エージェント名ケバブケース規則.md
  - ゲート判定基準での課題重大度の明文化.md
  - フォーマット変換の内容同等性基準.md
  - ルール分離テーマ別分割パターン.md
  - 共通ポリシー参照のblockquote形式標準化.md
  - 複数リポジトリ施策のPR作成漏れ防止.md

## ルール・workflow 整合性確認（.claude/skills/*.md ↔ docs/workflow.md）

- [x] 乖離なし
  - Skills/workflow の整合性は良好
  - ドラフト文書（coordination-protocol-guideline.md, git-worktree-guideline.md）のステータスバナーも適正
  - README.md の構成も実態と一致
  - 軽微な問題：triage-manager 担当ファイルテーブルに `backlog/ideas.md` が記載されているがファイル不在

## 前回トリアージからの変化

- 前回実施日：2026-03-08（20260308-2、2回目セッション）
- inbox 増減：+13 件（前回処理後から新規追加）
- backlog 増減：+5 件（前回 backlog 化分: backlog-archive-matching改善, denyリスト変更提案, inboxと課題管理とbacklog見直し, sync-worker同期先コミット漏れ防止, 社内施策_devkit）
- 完了施策：なし（前回以降新規施策なし）
- 新規課題：ISS-051（gh -C 未サポート）

## 調査サマリ・今回の重点

- 重点1：inbox 13件の新規エントリ処理（backlog 化 / ルール反映 / 却下の判断）
- 重点2：backlog CSV とファイルの差分解消（33件 vs 30ファイル）
- 重点3：triage-manager 担当ファイルテーブルの `backlog/ideas.md` 参照修正

## ワーカーセット数の推奨

- 推奨セット数：1 セット
- 割り当て方針：前回トリアージから1日しか経過しておらず、inbox 13件＋通常走査。1セットで全TGタスクをカバーする。

---
**調査者**: トリアージセッション
**調査日**: 2026-03-09
