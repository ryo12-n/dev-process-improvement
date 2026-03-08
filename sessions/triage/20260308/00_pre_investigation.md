# トリアージ事前調査: 2026-03-08

## inbox 確認

- [x] 未処理アイテム数：8 件
- [x] 最古アイテムの日付：2026-02-24（ref_ai-driven-development-poc.md）
- [x] 注目すべきアイテム（タイトル列挙）：
  - rule-change-checklist走査対象網羅性追加.md（ISS-042関連、ルール反映候補）
  - sync-worker同期先コミット漏れ防止.md（sync-worker.md修正提案）
  - 全セッションのマネージャーにディスパッチのセットルール展開.md（大きめの施策候補）
  - 対称性確認テーブルの推奨プラクティス化.md（session-flow-policy追記候補）

### 内訳

| 種別 | 件数 | 詳細 |
|------|------|------|
| ref ポインター | 4件 | ref_ai-driven-development-poc / ref_ai-functions / ref_openspec-official-summary / ref_個人PCローカル環境構築-手順書 |
| セッション気づき | 4件 | rule-change-checklist走査対象網羅性追加 / sync-worker同期先コミット漏れ防止 / 全セッションのマネージャーにディスパッチのセットルール展開 / 対称性確認テーブルの推奨プラクティス化 |

## backlog 確認

- [x] 総件数：29 件（CSV）
- [x] 優先度 🔴（高）：0 件
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古は 2026-02-25、13日前）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：1 件
  - claude-directory最適化(ai-driven-dev-patterns) → _archive/claude-directory最適化/ に対応施策あり
- [x] 特記事項：
  - データ整合性問題2件:
    1. `ai-driven-dev-patterns-triage-standard-policy作成.md` が backlog/ にあるが CSV に未記載
    2. `リポジトリ間テンプレート同期の検証チェックリスト` が CSV にあるが .md ファイルが存在しない

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：17 件
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：
  - ISS-041〜044 は今日（20260308）起票の新規課題
  - ISS-006 は openspec 関連で外部依存あり（openspec ライフサイクル未定義）

## 進行中 initiative 確認

- [x] 進行中：0 件
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：0 件

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：4 件
- [x] 処理候補のエントリ（タイトル列挙）：
  - rule-change-checklist走査対象網羅性追加 → ルール反映候補（rule-change-checklistスキルに項目追加）
  - sync-worker同期先コミット漏れ防止 → backlog化 or maintenance対応候補
  - 全セッションのマネージャーにディスパッチのセットルール展開 → backlog化候補（大規模）
  - 対称性確認テーブルの推奨プラクティス化 → ルール反映候補（session-flow-policyに追記）

## ルール・workflow 整合性確認（.claude/skills/*.md ↔ docs/workflow.md）

- [x] 乖離なし（軽微なもの1件のみ）
  - TG-009 の詳細手順が triage-worker.md に定義されているが workflow.md では簡潔な記述に留まる（影響: 低）
  - スキル/エージェントの関連ファイル一覧: 全参照先の実在を確認済み
  - ペアリング対称性: 全3ペア（L2/triage/sync）で対称性確認済み

## 前回トリアージからの変化

- 前回実施日：2026-03-07（20260307-3、同日3回目）
- inbox 増減：+1 件（sync-worker同期先コミット漏れ防止.md が新規追加）
- backlog 増減：+1 件（ai-driven-dev-patterns_source-of-truth明示 が新規追加）
- 完了施策：なし
- 新規課題：ISS-041〜044（4件、sync/20260308 セッションから）

## 調査サマリ・今回の重点

- 重点1：inbox 気づきエントリ4件の処理判断（ルール反映 or backlog化）
- 重点2：backlog データ整合性問題の解消（施策化済み1件、CSV/ファイル不整合2件）
- 重点3：新規課題 ISS-041〜044 のステータス確認

## ワーカーセット数の推奨

- 推奨セット数：1 セット
- 割り当て方針：前回トリアージから1日しか経過しておらず、inbox変更が軽微。全TGタスクを1セットで処理する。

---
**調査者**: トリアージセッション
**調査日**: 2026-03-08
