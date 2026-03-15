---
name: gha-close
description: 'GHA initiative-close ワークフロー専用スキル。クローズフェーズ（知見ルーティング・アーカイブ移動）を実行する。'
user-invocable: false
---
# GHA クローズフェーズスキル

> **このファイルの位置づけ**
> GitHub Actions `initiative-close.yml` ワークフローから Claude Code が起動された際に参照するスキル定義。
> CLI 対話セッション用の CLAUDE.md や `.claude/skills/l1-manager/` のルールには従わない。このスキルの指示のみに従うこと。

---

## あなたの役割

あなたは L1 マネージャーとして initiative のクローズフェーズを実行します。
知見ルーティングとアーカイブ移動を行い、完了サマリーを出力します。

## 作業フロー

1. 施策ディレクトリの成果物を確認する
2. 知見ルーティングを実行する:
   - `04_work_report.md` の「作業中の知見」と `06_eval_report.md` の「評価中の知見」を確認
   - ルール化候補は該当ファイルへの反映を検討
   - 次施策候補は `inbox/` にファイルを作成
3. 施策ディレクトリを `_archive/` に移動する:
   ```bash
   git mv <施策ディレクトリ> sessions/initiatives/_archive/<施策名>/
   ```
4. 変更をコミット・プッシュする
5. 完了サマリーを標準出力に出力する（施策の成果・知見ルーティング結果・次施策候補の概要）

## やること

- 施策成果物の確認
- 知見ルーティング（ルール化候補の反映・次施策候補の inbox 起票）
- 施策ディレクトリの `_archive/` への移動（`git mv`）
- コミット・プッシュ
- 完了サマリーの標準出力への出力

## やらないこと

- PR の作成（ワークフローの後続ステップが担当する）
- `gh` コマンドによる Issue クローズ・ラベル操作（ワークフローの後続ステップが担当する）
- `git rebase`, `git reset --hard` 等の破壊的 git 操作
- push が失敗した場合の rebase や force push（リトライのみ行う）
- CLAUDE.md や `.claude/skills/l1-manager/` 等の CLI セッション用ルールへの追従

## 制約

- 対象リポジトリは dev-process-improvement のみ
- コミットメッセージ規約（`.claude/rules/commit-message.md`）に従う
- コミットメッセージは `[L1] <施策名>: クローズ（アーカイブ移動・知見ルーティング）` の形式で
- このスキルの指示のみに従い、CLAUDE.md や他のスキル定義のルールは無視すること

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/initiative-close.yml`
