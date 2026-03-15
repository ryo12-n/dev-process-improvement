# 実施計画: GHA 壁打ちフェーズの独立・反復化

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | テンプレート・スキル・ワークフロー変更 | 全9ファイルの変更が完了し、構文エラーがないこと |

## スケジュール

1. テンプレート追加（`00a_wallbash_log.md` 新規作成、`02_tasks.md` 修正）
2. スキル変更（`gha-wallbash/SKILL.md`、`gha-execute/SKILL.md`）
3. ワークフロー変更（`initiative-wallbash.yml`、`initiative-dispatcher.yml`、`initiative-execute.yml`）
4. CLI アライメント（`l1-manager/SKILL.md`）
5. ドキュメント更新（`docs/workflow.md`）

## 成功基準（全体）

1. `sessions/initiatives/_template/00a_wallbash_log.md` が存在し、所定の構造を持つこと
2. `gha-wallbash/SKILL.md` が init/continue の2モードを定義していること
3. `initiative-wallbash.yml` が mode, feedback, branch, initiative_dir の inputs を持ち、mode=continue 時に既存ブランチをチェックアウトすること
4. `initiative-dispatcher.yml` が `/continue` コマンドを `initiative:wallbashing` フェーズで受け付け、wallbash ワークフローにルーティングすること
5. `initiative-execute.yml` が `phase=wallbashing` 時に PR を作成するステップを持つこと
6. `gha-execute/SKILL.md` が壁打ちドラフト（01/02）を活用する記述を持つこと
7. `docs/workflow.md` が新フロー（`/continue` ループ）を反映していること

## リソース・前提条件

- 対象リポジトリ: dev-process-improvement のみ
- GHA ワークフローの構文検証は `act` またはマニュアルレビューで行う
- E2E テストは施策完了後に手動で実施（Issue 作成 → `/start` → `/continue` → `/approve` の一連のフロー）

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| YAML 構文エラー | 中 | 中 | ワークフロー変更後に構文チェック |
| 後方互換の破壊 | 低 | 高 | execute スキルにフォールバック記述を追加 |
| `/continue` の routing ミス | 低 | 中 | dispatcher のルーティングロジックを既存パターンに倣う |

---
**作成者**: L1
**作成日**: 2026-03-15
**最終更新**: 2026-03-15
