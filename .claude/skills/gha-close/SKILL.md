---
name: gha-close
description: 'GHA initiative-close ワークフロー専用スキル。クローズフェーズ（知見ルーティング・アーカイブ移動）を実行する。'
user-invocable: false
---
# GHA クローズフェーズスキル

## コンテキスト

このファイルは GitHub Actions の `initiative-close.yml` ワークフローから `claude-code-action` 経由で実行される自動化スキルです。リポジトリオーナーが設定したワークフローから呼び出されており、`permissions.allow` で許可されたツールのみが使用可能です。

## あなたの役割

あなたは L1 マネージャーとして initiative のクローズフェーズを実行します。
知見ルーティングとアーカイブ移動を行い、完了サマリーを出力します。

## 作業フロー

1. 施策ディレクトリの成果物を確認する
2. 知見ルーティングを実行する:
   - `04_work_report.md` の「作業中の知見」と `06_eval_report.md` の「評価中の知見」を確認
   - ルール化候補は該当ファイルへの反映を検討
   - 次施策候補は `inbox/` にファイルを作成
   - 外部リポジトリの知見は `refs/<リポ名>/knowledge.md` に Write ツールで書き込む（Write ツールは親ディレクトリを自動作成するため mkdir は不要）
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

## 制約

- 対象リポジトリは dev-process-improvement のみ
- コミットメッセージ規約（`.claude/rules/commit-message.md`）に従う
- コミットメッセージは `[L1] <施策名>: クローズ（アーカイブ移動・知見ルーティング）` の形式で
- ファイル作成は Write ツールを使用する（`Bash(mkdir *)` は sandbox でブロックされる）
- ツール使用が sandbox にブロックされた場合、同じ操作のリトライは行わず代替手段に切り替える
- CSV は `scripts/generate-csvs.py` で .md から自動生成される。課題転記時は `issues/entries/ISS-XXX.md` を作成する

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/initiative-close.yml`
