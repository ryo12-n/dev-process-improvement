# トリアージ事前調査: 2026-03-08

## inbox 確認

- [x] 未処理アイテム数：6 件
- [x] 最古アイテムの日付：2026-02-24（ref_ai-driven-development-poc.md）
- [x] 注目すべきアイテム（タイトル列挙）：
  - `2つのリポジトリの部分的同期.md` — sessions ディレクトリ導入、triage archive、空テンプレート問題
  - `ai-driven-dev-patterns_source-of-truth明示.md` — ai-driven-dev-patterns に Source of Truth ルール追加

## backlog 確認

- [x] 総件数：32 件（backlog.csv ベース）
- [x] 優先度 🔴（高）：0 件
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古は 2026-03-01）
- [x] 施策化済み候補（initiatives/ または _archive/ に対応施策あり）：要確認
  - `課題管理とinbox管理の方法見直し` — CSV に「ファイル不在」と記載あり
- [x] 特記事項：backlog.csv の「課題管理とinbox管理の方法見直し」のファイル名が「（ファイル不在）」。実ファイルの確認が必要

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：9 件（ISS-006, 013, 016, 019, 020, 021, 022, 032, 033, 038, 039, 040）
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：ISS-040（triage-evaluator 壁打ちフェーズの policy 不整合）は前回トリアージで起票

## 進行中 initiative 確認

- [x] 進行中：0 件
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：0 件（initiatives/ 直下に _archive, _template のみ）

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：2 件
- [x] 処理候補のエントリ（タイトル列挙）：
  - `2つのリポジトリの部分的同期.md` — ディレクトリ構成改善のアイデア
  - `ai-driven-dev-patterns_source-of-truth明示.md` — Source of Truth 明示パターンの提案

## ルール・workflow 整合性確認（.claude/rules/*.md ↔ docs/workflow.md）

- [x] 乖離なし。スキル定義・エージェント定義・docs/workflow.md 間の整合性は良好。

## 前回トリアージからの変化

- 前回実施日：2026-03-07（20260307-3）
- inbox 増減：+2 件（2つのリポジトリの部分的同期, ai-driven-dev-patterns_source-of-truth明示）
- backlog 増減：+2 件（リポジトリ間テンプレート同期の検証チェックリスト, 別リポジトリ成果物の記法スタイル事前確認）
- 完了施策：triage-process-brushup（アーカイブ済み）
- 新規課題：ISS-040（triage-evaluator 壁打ちフェーズの policy 不整合）

## 調査サマリ・今回の重点

- 重点1：inbox 2件の新規エントリの処理（backlog化判断）
- 重点2：backlog の施策化済みチェック（TG-002）と関係性分析（TG-005）
- 重点3：起票済み課題の棚卸し（ISS-040 など前回起票分の対応判断）

## ワーカーセット数の推奨

- 推奨セット数：1 セット
- 割り当て方針：前回からの間隔が短く（1日）、inbox 2件・backlog 変更少。全TGタスクを1セットで処理可能。

---
**調査者**: トリアージセッション
**調査日**: 2026-03-08
