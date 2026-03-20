# タスクリスト: gha-workflow-ux-improvements

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-009 | 逐次 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | 全タスク S〜M の YAML 編集。並列のオーバーヘッドに見合わないため逐次 |

---

## タスク一覧

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | dispatcher.yml: `@ai-task` → `@ai` + feedback 伝播 | dispatcher.yml 内に `@ai-task` 残存なし、feedback が wallbash/close に渡される | 🔴 | ✅ |
| T-002 | wallbash.yml: コメント表示改善 + `@ai` + init feedback | コマンドがフェンスドコードブロック + `@ai`、init で feedback が prompt に渡る | 🔴 | ✅ |
| T-003 | execute.yml: コメント表示改善 + `@ai` | コマンドがフェンスドコードブロック + `@ai` | 🔴 | ✅ |
| T-004 | backlog-to-issue.yml: cron 3h + `@ai` | cron `0 */3 * * *`、Issue 本文が `@ai /start` | 🔴 | ✅ |
| T-005 | close.yml feedback + gha スキル更新 + README 全面最新化 | close.yml に feedback input、gha-wallbash/close SKILL に feedback 記述、README 実態一致 | 🔴 | ✅ |
| T-006 | 知見記録（固定タスク） | ルール化候補・参考情報の両テーブルに最低1行 | 🔴 | ✅ |
| T-007 | メタルール横断検証（固定・ルール変更） | 3領域の検証結果が work_report に記載 | 🔴 | ✅ |
| T-008 | ルール変更チェックリスト（固定・ルール変更） | 全7項目の結果が work_log に記録 | 🔴 | ✅ |
| T-009 | 課題 CSV 転記確認（固定タスク） | 全課題に転記済/転記不要の判断 | 🔴 | ✅ |

## タスク詳細

### T-001: initiative-dispatcher.yml — `@ai-task` → `@ai` 変更 + feedback 伝播追加

**やること**:
1. `dispatch` ジョブの `if` 条件の `@ai-task` → `@ai` に変更
2. `Parse command` ステップの grep/sed パターンの `@ai-task` → `@ai` に変更
3. `Route and dispatch` ステップの `start` case に `-f feedback="$ARGS"` を追加
4. `Route and dispatch` ステップの `approve` + `gate-review` case に `-f feedback="$ARGS"` を追加
5. 全エラーメッセージの `@ai-task` → `@ai` に変更

**完了条件**:
- [ ] dispatcher.yml 内に `@ai-task` が残っていない
- [ ] `/start` ディスパッチ時に `feedback` パラメータが wallbash に渡される
- [ ] `/approve`（gate-review）ディスパッチ時に `feedback` パラメータが close に渡される

### T-002: initiative-wallbash.yml — コメント表示改善 + `@ai` + init feedback

**やること**:
1. `Post initiative metadata` ステップ: `@ai-task` → `@ai`、コマンド表示をフェンスドコードブロックに変更
2. `Post wallbash summary to issue` ステップ: `@ai-task` → `@ai`、コマンド表示をフェンスドコードブロックに変更
3. init モードでも feedback を受け取れるように: `Save feedback to file` ステップの `if` 条件を削除（init/continue 両方で feedback 保存）
4. `Run Claude Code` ステップの prompt に init モードでの feedback 参照を追加

**補足**: HEREDOC 内にフェンスドコードブロック（バッククォート3連）を含める場合、`--body-file` パターンの採用を推奨。`cat > /tmp/comment.md << 'COMMENT_EOF'` でファイル作成し `gh issue comment --body-file /tmp/comment.md` で投稿する

**完了条件**:
- [ ] コマンドリファレンスのコマンドが `@ai` を使用している
- [ ] コマンド表示がフェンスドコードブロックで囲まれている
- [ ] init モードでも feedback が Claude prompt に渡される

### T-003: initiative-execute.yml — コメント表示改善 + `@ai`

**やること**:
1. `Post gate review summary to issue` ステップ: `@ai-task` → `@ai`、コマンド表示をフェンスドコードブロックに変更

**補足**: T-002 同様、`--body-file` パターンを推奨

**完了条件**:
- [ ] 次ステップ案内のコマンドが `@ai` を使用している
- [ ] コマンド表示がフェンスドコードブロックで囲まれている

### T-004: backlog-to-issue.yml — cron 間隔変更 + `@ai` 反映

**やること**:
1. `on.schedule.cron` を `*/30 * * * *` → `0 */3 * * *` に変更
2. `Create issue` ステップ（create-issue ジョブ）の Issue 本文内の `@ai-task /start` → `@ai /start`、フェンスドコードブロック化
3. scheduled-create ジョブには使い方ガイドが含まれていないため変更不要（確認のみ）

**完了条件**:
- [ ] cron が `0 */3 * * *` に変更されている
- [ ] create-issue ジョブの Issue 本文が `@ai /start` を使用している

### T-005: close.yml feedback + gha スキル更新 + README 全面最新化

**やること**:
1. `.github/workflows/initiative-close.yml`: `on.workflow_dispatch.inputs` に `feedback` パラメータ追加（required: false, type: string, default: ''）+ `Run Claude Code` ステップの prompt に feedback 行追加
2. `.claude/skills/gha-wallbash/SKILL.md`: init モードの作業フローに feedback ファイル参照の記述を追加
3. `.claude/skills/gha-close/SKILL.md`: feedback がある場合はクローズ処理に反映する旨を追記
4. `.github/workflows/README.md` 全面更新:
   - `@ai-task` → `@ai`（全箇所）
   - コマンドリファレンスを `@ai` に更新
   - フロー図を `@ai` に更新
   - ワークフロー一覧: `backlog-auto-execute.yml`, `backlog-candidate-propose.yml` 削除。`initiative-batch-approve.yml`, `initiative-question.yml` 追加
   - `backlog-to-issue.yml` のトリガー: `schedule(3時間間隔) / 手動`
   - メタデータコメントセクションのコマンドリファレンスを `@ai` に更新

**完了条件**:
- [ ] initiative-close.yml に `feedback` input が追加されている
- [ ] initiative-close.yml の Claude prompt に feedback が含まれている
- [ ] gha-wallbash/SKILL.md に init モード時の feedback 参照記述がある
- [ ] gha-close/SKILL.md に feedback 活用の記述がある
- [ ] README 内に `@ai-task` が残っていない
- [ ] README のワークフロー一覧が実態と一致している（存在しないワークフローなし、存在するワークフロー全て記載）

### T-006: 知見記録（固定タスク）

**やること**: 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載）

**完了条件**:
- [ ] 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある

### T-007: メタルール横断検証（固定タスク・ルール変更施策）

**適用条件**: `.claude/skills/gha-wallbash/SKILL.md`, `.claude/skills/gha-close/SKILL.md` を変更するため該当

**やること**: 以下3領域のメタルール横断検証を実施し、結果を `04_work_report.md` に記録する
1. メタルールフロー記述: 変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているか確認・修正
2. workflow.md 同期: `docs/workflow.md` の該当セクションが変更内容と整合しているか確認・更新
3. TG-008 基準連動: `session-lifecycle-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新

**完了条件**:
- [ ] 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている

### T-008: ルール変更チェックリスト確認（固定タスク・ルール変更施策）

**やること**: `rule-change-checklist` スキル（`.claude/skills/rule-change-checklist/SKILL.md`）のチェックリスト全7項目を確認する。T-007 がカバーしていない項目（パス変更走査対象の網羅性・deny リスト対称性・テンプレート連動更新・コミットメッセージ規約確認）を特に確認すること

**完了条件**:
- [ ] チェックリストの全7項目の結果が `03_work_log.md` に記録されている

### T-009: 課題の CSV 転記確認（固定タスク）

**やること**: `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` に作成する。転記時は `issues/_template.md` をコピーして作成し、課題詳細を記載する

**完了条件**:
- [ ] 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている

---
**作成者**: L1
**最終更新**: 2026-03-19
