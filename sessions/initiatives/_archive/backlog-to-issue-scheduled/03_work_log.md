# 作業履歴: backlog-to-issue-scheduled

## 壁打ちフェーズ [2026-03-15 12:00]

### 理解のサマリー
- タスクの目的: バックログから定期的に Issue を自動起票する GHA ワークフローを構築する。承認ステップを排除し、6時間ごとに候補を1件ずつ自動消化する
- スコープ: (1) `select-backlog-candidate.sh` の全優先度対応・BL-ID 出力追加、(2) `backlog-to-issue.yml` への schedule トリガー追加、(3) 不要ワークフロー2件の削除
- 完了条件: T-001〜T-006 全完了、作業履歴・レポート記録済み、全変更コミット済み

### 前提条件チェック
- [x] 依存タスクの完了状態: 依存なし（独立タスク群）
- [x] 必要ツール・コマンドの利用可否: 確認済み（git, Bash）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
  - `select-backlog-candidate.sh` 存在確認済み
  - `backlog-to-issue.yml` 存在確認済み
  - `backlog-candidate-propose.yml` 存在確認済み（削除対象）
  - `backlog-auto-execute.yml` 存在確認済み（削除対象）
  - ブランチ `claude/l1-manager-Vs9fN` にいることを確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. **T-001**: `select-backlog-candidate.sh` を改修（優先度フィルタ撤廃、ソート順変更、`id` 出力追加）
2. **T-002**: `backlog-to-issue.yml` に `scheduled-create` ジョブを追加（schedule トリガー、候補選定、重複チェック、Issue 作成、wallbash ディスパッチ）
3. **T-003**: `backlog-candidate-propose.yml` を `git rm` で削除
4. **T-004**: `backlog-auto-execute.yml` を `git rm` で削除
5. **T-005**: 知見を `04_work_report.md` に記録
6. **T-006**: `07_issues.md` の課題を確認・転記判断

順序: T-001 → T-002 → T-003 → T-004 → コミット → T-005 → T-006 → 最終コミット

---

## 作業ログ

### [2026-03-15 12:10] タスクID: T-001
**状態**: 完了
**作業内容**:
- `select-backlog-candidate.sh` の改修を確認（L1 が既にブランチ上で実施済み）
- 優先度フィルタを撤廃し全優先度対応に変更済み
- ソート順を優先度ASC（低=1,中=2,高=3）→起票日ASCに変更済み
- 出力に `id`（BL-XXX）を追加済み
- CSV ヘッダのコメントも ID 列追加に合わせて更新済み
**成果物**: `.github/scripts/select-backlog-candidate.sh`（改修済み）
**課題・気づき**: L1 が事前に改修を実施していたため、差分確認のみで完了

### [2026-03-15 12:15] タスクID: T-002
**状態**: 完了
**作業内容**:
- `backlog-to-issue.yml` に `schedule` トリガー（`cron: '0 */6 * * *'`）を追加
- 既存 `create-issue` ジョブに `if: github.event_name == 'workflow_dispatch'` 条件を追加（schedule 時に実行されないよう制御）
- `scheduled-create` ジョブを新設:
  - checkout → `select-backlog-candidate.sh` 実行 → 候補なし時の正常終了
  - 重複チェック（`gh issue list --search "[BL-XXX] in:title"` で全状態検索）
  - バックログエントリ読み込み → Issue 作成 → `initiative-wallbash.yml` ディスパッチ
- GHA セキュリティルール準拠: すべての `${{ }}` 式を `env:` 経由で渡す
  - `BACKLOG_ID`, `INITIATIVE_NAME`, `ENTRY_CONTENT`, `ENTRY_FILE`, `ISSUE_NUMBER` を環境変数化
**成果物**: `.github/workflows/backlog-to-issue.yml`（schedule トリガー + scheduled-create ジョブ追加）
**課題・気づき**:
- 既存 `create-issue` ジョブの line 54, 79 に `${{ steps.find.outputs.file }}` の `run:` 内直接展開が残存（セキュリティルール非準拠）。ただし `workflow_dispatch` の `inputs` 由来の制御された値であり、スコープ外のため手を加えなかった → 07_issues.md に起票

### [2026-03-15 12:20] タスクID: T-003
**状態**: 完了
**作業内容**:
- `git rm .github/workflows/backlog-candidate-propose.yml` で削除
**成果物**: ファイル削除（git staging 済み）

### [2026-03-15 12:20] タスクID: T-004
**状態**: 完了
**作業内容**:
- `git rm .github/workflows/backlog-auto-execute.yml` で削除
**成果物**: ファイル削除（git staging 済み）

### [2026-03-15 12:25] タスクID: T-005
**状態**: 完了
**作業内容**:
- `04_work_report.md` を作成
- 「ルール化候補」に1件記載: schedule/workflow_dispatch 共存時のジョブ条件明示
- 「参考情報」に1件記載: `gh issue list --search --state all` による重複チェック手法
**成果物**: `04_work_report.md`

### [2026-03-15 12:30] タスクID: T-006
**状態**: 完了
**作業内容**:
- `07_issues.md` の未転記課題を確認（1件: 既存 create-issue ジョブの GHA セキュリティルール非準拠箇所）
- 施策固有の改善提案であり、他施策での再発性は低いと判断 → 転記不要
**成果物**: `07_issues.md`（転記判断を追記）

