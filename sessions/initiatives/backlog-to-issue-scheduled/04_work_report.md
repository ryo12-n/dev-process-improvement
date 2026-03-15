# 作業レポート: backlog-to-issue-scheduled

## サマリ
バックログから定期的に Issue を自動起票する GHA ワークフローを構築した。`backlog-to-issue.yml` に 6 時間ごとの schedule トリガーと `scheduled-create` ジョブを追加し、候補選定・重複チェック・Issue 作成・wallbash ディスパッチの一連のフローを実装した。不要になった `backlog-candidate-propose.yml` と `backlog-auto-execute.yml` を削除した。全タスク（T-001〜T-006）を完了。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | `select-backlog-candidate.sh` 改修 | 全優先度対応・BL-ID 出力追加 | L1 により事前改修済み。差分確認のみ | 差異なし（成果物は計画通り） |
| T-002 | `backlog-to-issue.yml` schedule トリガー追加 | scheduled-create ジョブ新設 | 計画通り実装。既存ジョブに `if` 条件を追加 | 既存ジョブへの `if` 条件追加は計画外だが必要な措置 |
| T-003 | `backlog-candidate-propose.yml` 削除 | `git rm` で削除 | 計画通り | - |
| T-004 | `backlog-auto-execute.yml` 削除 | `git rm` で削除 | 計画通り | - |
| T-005 | 知見記録 | レポートに記載 | 本セクションに記載 | - |
| T-006 | 課題 CSV 転記確認 | 未転記課題の転記判断 | 1件の改善提案を確認、施策内完結と判断し転記不要 | - |

## 成果物一覧
- `.github/workflows/backlog-to-issue.yml`（schedule トリガー + scheduled-create ジョブ追加）
- `.github/scripts/select-backlog-candidate.sh`（全優先度対応・BL-ID 出力追加、L1 による事前改修）
- `.github/workflows/backlog-candidate-propose.yml`（削除）
- `.github/workflows/backlog-auto-execute.yml`（削除）

## 発生した課題
- 既存 `create-issue` ジョブの `${{ }}` 直接展開（GHA セキュリティルール非準拠）: スコープ外のため改善提案として `07_issues.md` に起票。リスクは低い。

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | schedule と workflow_dispatch を共存させる際は、各ジョブに `if: github.event_name == '...'` を明示的に付与すべき | GHA ワークフロー設計 | schedule トリガー追加時に既存の workflow_dispatch 用ジョブが schedule でも実行されてしまう問題を防止するため。今回 `create-issue` ジョブに `if` を追加する必要があった |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | `gh issue list --search "[BL-XXX] in:title" --state all` で全状態（open/closed）の Issue を検索できる。重複チェックには `--state all` が必要 | schedule で定期実行する場合、既にクローズされた Issue と同じ BL-ID の再起票を防ぐため |

## 所感・次フェーズへの申し送り
- 全タスクを計画通り完了。T-001 は L1 が事前に実施済みだったため差分確認のみとなった
- 既存 `create-issue` ジョブのセキュリティルール非準拠箇所は本施策のスコープ外だが、次回改修時に対応することを推奨
- schedule トリガーの動作確認は GHA 環境でのみ可能（ローカルでは検証不可）。評価者による構文・ロジックレビューを推奨

---
**作成者**: L2（実施）
**作成日**: 2026-03-15
