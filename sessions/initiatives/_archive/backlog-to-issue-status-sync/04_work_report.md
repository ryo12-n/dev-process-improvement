# 作業レポート: backlog-to-issue-status-sync（実施フェーズ）

## サマリ

T-001〜T-005 の全タスクを完了した。GHA ワークフロー修正（重複チェック改善・ステータス自動更新ステップ追加・権限変更）、generate-csvs.py の STATUS_MAP 追加、backlog/README.md のステータス値説明更新を実施した。全変更は GHA セキュリティチェックリストに準拠している。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | backlog-to-issue.yml の scheduled-create ジョブ修正 | 3箇所修正（permissions、--state、ステータス更新ステップ追加） | 完了 | 計画通り。`${{ }}` は `env:` 経由で渡し、GHA セキュリティチェックリスト準拠 |
| T-002 | generate-csvs.py の STATUS_MAP 追加 | `"起票済み": "起票済み"` を1行追加 | 完了 | 計画通り |
| T-003 | backlog/README.md のステータス値説明更新 | ステータス列に「起票済み」追加 | 完了 | 計画通り |
| T-004 | 作業中の知見を記録する | 知見セクションに記載 | 完了 | 下記「作業中の知見」参照 |
| T-005 | 課題の転記確認 | 未転記課題の確認 | 完了 | 転記対象の課題なし |

## 成果物一覧

- `.github/workflows/backlog-to-issue.yml`: scheduled-create ジョブの3箇所修正
- `scripts/generate-csvs.py`: STATUS_MAP に1行追加
- `backlog/README.md`: ステータス列説明を更新

## 発生した課題

- なし

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | GHA ワークフロー内での git commit & push は contents: write 権限が必要 | T-001 | `.github/workflows/` | schedule トリガーのジョブで .md ファイルを更新する際、contents: read → write への昇格が必要。gha-workflow-security.md の「最小権限」原則との兼ね合いで、必要な場合のみ write を付与する方針が妥当 |
| 2 | GHA ステップで sed + git commit & push を行う場合、`if` 条件で前提ステップの成功を明示的にチェックすべき | T-001 | `.github/workflows/` | issue 起票成功後にのみステータス更新を行うため、`if: steps.select.outputs.has_candidate == 'true' && steps.dup_check.outputs.existing_count == '0'` の条件を明示。Create issue ステップが失敗した場合は後続ステップも自動的にスキップされるが、条件を明示することで意図を明確にできる |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | `select-backlog-candidate.sh` のフィルタ条件は「ステータス == 候補」のみで、ステータス値の追加により自動的に候補選定から除外される | T-001/T-002 | CSV 自動生成とフィルタスクリプトの連携設計。.md のステータスを「起票済み」に変更するだけで、次回スケジュール実行時の候補から外れる |
| 2 | `--state all` から `--state open` への変更により、クローズ済み issue の再起票が可能になる | T-001 | 一度クローズされた issue を持つバックログエントリでも、ステータスを「候補」に戻せば再度 issue 起票が可能になる柔軟な設計 |

## 所感・次フェーズへの申し送り

- 全タスクが計画通りに完了し、差異なし
- GHA セキュリティチェックリストへの準拠を確認済み（`${{ }}` 直接展開なし、`env:` 経由、最小権限、トリガー共存時の `if` 設定）
- 実際の動作検証は GHA 環境での実行が必要（評価フェーズで確認予定）

---
**作成者**: L2-worker
**作成日**: 2026-03-17
