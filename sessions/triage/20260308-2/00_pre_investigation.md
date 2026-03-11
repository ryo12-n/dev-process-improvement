# トリアージ事前調査: 2026-03-08（2回目）

## inbox 確認

- [x] 未処理アイテム数：13 件
- [x] 最古アイテムの日付：2026-02-24（ref_ai-driven-development-poc.md）
- [x] 注目すべきアイテム（タイトル列挙）：
  - backlog-archive-matching改善.md（backlog と archive の名前突合改善提案）
  - denyリスト変更提案への副作用分析必須化.md（deny 変更時の副作用分析ルール化）
  - inboxと課題管理とbacklogを管理方法見直し.md（ディレクトリ構造改善提案）
  - セッションタイプ間の責務の違い明記ルール.md（SKILL.md への責務差分セクション追加）

### 内訳

| 種別 | 件数 | 詳細 |
|------|------|------|
| ref ポインター | 4件 | ref_ai-driven-development-poc / ref_ai-functions / ref_openspec-official-summary / ref_個人PCローカル環境構築-手順書（前回から変更なし） |
| セッション気づき（metacognitive-improvement-enforcement 由来） | 3件 | triage-metacognition テンプレート共通化検討 / セッションタイプ間の責務の違い明記ルール / 適用マトリクス列数増加リスク |
| セッション気づき（subagent-permission-model 由来） | 3件 | CLI環境での権限継承の再検証 / denyリスト変更提案への副作用分析必須化 / 改善提案への適用対象環境明記 |
| セッション気づき（課題管理とinbox管理の方法見直し 由来） | 1件 | backlog-archive-matching改善 |
| セッション気づき（その他） | 1件 | inboxと課題管理とbacklogを管理方法見直し |
| 社内施策関連 | 1件 | 社内施策_devkitのコマンドやガイドの使用クロードのskillやRuleとして用意しておく |

## backlog 確認

- [x] 総件数：31 件（CSV）
- [x] 優先度 🔴（高）：0 件
- [x] 優先度未設定：0 件
- [x] ステータス「候補」のまま放置（30日以上）：0 件（最古は 2026-02-25、13日前）
- [x] 施策化済み候補（sessions/initiatives/ または _archive/ に対応施策あり）：0 件
  - 前回検出の claude-directory最適化(ai-driven-dev-patterns) → 要ユーザー確認（前回報告済み、未回答）
- [x] 特記事項：
  - 前回のデータ整合性問題2件は解消済み（CSV未記載→追加、.md不在→CSV削除）
  - 前回 backlog 追加の2件（sync-worker同期先コミット漏れ防止、マネージャーセッション共通ポリシー策定）が正しくCSVに登録されている

## 課題管理 CSV 確認（プロセス改善_課題管理.csv）

- [x] ステータス「起票」（未対応）：22 件
- [x] ステータス「方針確定」（未タスク化）：1 件（ISS-031）
- [x] 最古の未対応課題：ISS-006 (2026-02-23)
- [x] 特記事項：
  - ISS-045, ISS-046 は前回トリアージ以降の新規課題（subagent-permission-model 由来）
  - ISS-040 が前回以降クローズ済み（maintenance 対応完了）

## 進行中 initiative 確認

- [x] 進行中：0 件
- [x] ブロック中：0 件
- [x] アーカイブ待ち（ゲート通過済み・未移動）：0 件

## inbox 気づきエントリ確認

- [x] セッション終了時の気づきエントリ：9 件（ref ポインター4件を除く）
- [x] 処理候補のエントリ（タイトル列挙）：
  - backlog-archive-matching改善 → backlog化候補（L1クローズチェックリスト・命名規約改善）
  - denyリスト変更提案への副作用分析必須化 → ルール反映候補 or backlog化
  - inboxと課題管理とbacklogを管理方法見直し → backlog化候補（ディレクトリ構造改善）
  - CLI環境での権限継承の再検証 → backlog化候補（CLI環境でのallow/deny検証）
  - 改善提案への適用対象環境明記 → ルール反映候補（L2-worker タスク完了基準追記）
  - セッションタイプ間の責務の違い明記ルール → backlog化候補（SKILL.md テンプレート追記）
  - triage-metacognition テンプレート共通化検討 → 判断保留候補（セッションタイプ増加待ち）
  - 適用マトリクス列数増加リスク → 判断保留候補（4番目のセッションタイプ追加時に対応）
  - 社内施策_devkitのコマンドやガイドの使用… → backlog化候補（社内環境向け）

## ルール・workflow 整合性確認（.claude/skills/*.md ↔ docs/workflow.md）

- [x] 乖離なし（重大なものなし）
  - TG-008/TG-009 の詳細手順が triage-worker.md に定義、workflow.md では簡潔な記述（前回と同じ、影響: 低）
  - 全スキル/エージェントの関連ファイル一覧: 全参照先の実在を確認済み

## 前回トリアージからの変化

- 前回実施日：2026-03-08（20260308、同日1回目）
- inbox 増減：+9 件（metacognitive-improvement-enforcement / subagent-permission-model / 課題管理見直し等から）、-4 件（前回処理済み分削除）
- backlog 増減：+2 件（sync-worker同期先コミット漏れ防止、マネージャーセッション共通ポリシー策定）、-1 件（リポジトリ間テンプレート同期の検証チェックリスト削除）
- 完了施策：metacognitive-improvement-enforcement、subagent-permission-model、課題管理とinbox管理の方法見直し がアーカイブ済み
- 新規課題：ISS-045, ISS-046（subagent-permission-model 由来）
- ISS-040 がクローズ済み（前回 maintenance 対応推奨→実施完了）

## 調査サマリ・今回の重点

- 重点1：inbox 気づきエントリ9件の処理判断（ルール反映 / backlog化 / 判断保留）
- 重点2：新規課題 ISS-045, ISS-046 のステータス確認
- 重点3：backlog 関係性分析（新規2件追加後の依存・重複チェック）

## ワーカーセット数の推奨

- 推奨セット数：1 セット
- 割り当て方針：前回トリアージから数時間しか経過しておらず、変更は主に inbox 追加。inbox が9件と多めだが内容は3つの施策セッションからの気づきで文脈が明確。全TGタスクを1セットで処理する。

---
**調査者**: トリアージセッション
**調査日**: 2026-03-08
