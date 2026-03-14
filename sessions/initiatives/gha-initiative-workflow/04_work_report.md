# 作業レポート: GHA Initiative ワークフロー

## サマリ

GHA 環境で initiative セッションを Issue ベースの対話型ワークフローとして実装した。壁打ち（wallbash）、実行（execute）、クローズ（close）の3ファイルを作成し、gha-guideline の §5 に権限マトリクスを追記した。全タスク（T-001〜T-006）を計画通り完了。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | initiative-wallbash.yml 作成 | ワークフローファイル作成 | 完了 | 計画通り。workflow_dispatch 対応も含む |
| T-002 | initiative-execute.yml 作成 | ワークフローファイル作成 | 完了 | PR コメント排除フィルタを追加 |
| T-003 | initiative-close.yml 作成 | ワークフローファイル作成 | 完了 | 計画通り |
| T-004 | gha-guideline §5 更新 | 3ワークフローの権限マトリクス追記 | 完了 | §5.1, §5.2, §5.3, 関連ファイル一覧を更新 |
| T-005 | 知見記録 | 作業中の知見をレポートに記録 | 完了 | 下記「作業中の知見」参照 |
| T-006 | 課題転記 | 07_issues.md の課題を確認・転記 | 完了 | 転記対象なし（施策内完結の知見1件のみ） |

## 成果物一覧
- `.github/workflows/initiative-wallbash.yml` — 壁打ちフェーズワークフロー
- `.github/workflows/initiative-execute.yml` — 実行フェーズワークフロー
- `.github/workflows/initiative-close.yml` — クローズフェーズワークフロー
- `.claude/skills/gha-guideline/SKILL.md` — §5 に3ワークフローの権限設計を追記（更新）

## 発生した課題
- なし（07_issues.md に知見1件を記録、転記不要と判断）

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | `issue_comment` トリガーは PR コメントでも発火するため、Issue 専用ワークフローでは `github.event.issue.pull_request == null` フィルタが必要 | gha-guideline §4 または新セクション | GHA の `issue_comment` イベントは Issues と PR の両方で発火する。initiative ワークフローのように Issue コメントのみに反応するワークフローでは明示的な除外が必要。gha-guideline のチェックリストに追加候補 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | initiative ワークフロー3つは同一の設計パターン（git は Claude 委任、gh/ラベル操作は Shell）を採用しており、backlog-auto-execute.yml と整合的 | 3層権限モデル（L1:GHA権限、L2:Claudeツール許可、L3:プロンプト指示）の整合性を保つため、gh コマンドは Shell ステップに統一した。Claude に `Bash(gh *)` を許可しない方針で、最小権限の原則に沿っている |

## 所感・次フェーズへの申し送り
- 3ワークフローは構文的に正しく作成済み。E2E テストは本施策スコープ外だが、実際のリポジトリでのラベル作成（`initiative-start`, `initiative`, `initiative:wallbashing`, `initiative:executing`, `initiative:gate-review`, `initiative:completed`）が前提条件となる
- execute ワークフローの `--max-turns 80` は計画・実行・評価・ゲート判定を一括で行うため高めに設定しているが、実運用で不足する場合は調整が必要

---
**作成者**: L2（実施）
**作成日**: 2026-03-14
