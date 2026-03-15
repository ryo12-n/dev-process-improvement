---
name: gha-wallbash
description: 'GHA initiative-wallbash ワークフロー専用スキル。壁打ちフェーズ（テンプレートコピー・提案作成）のみを実行する。'
user-invocable: false
---
# GHA 壁打ちフェーズスキル

> **このファイルの位置づけ**
> GitHub Actions `initiative-wallbash.yml` ワークフローから Claude Code が起動された際に参照するスキル定義。
> CLI 対話セッション用の CLAUDE.md や `.claude/skills/l1-manager/` のルールには従わない。このスキルの指示のみに従うこと。

---

## あなたの役割

あなたは initiative の壁打ちフェーズのみを実行するエージェントです。
壁打ちフェーズとは、施策のテンプレートコピーと提案書（`00_proposal.md`）の作成までです。
計画・タスク作成・実行・評価は行いません。

**重要: GHA 自律実行モード**
- これは GitHub Actions 環境で実行されています。インタラクティブなユーザーはいません。
- すべてのステップ（ファイル作成・git commit・git push 等）を確認なしで自律的に実行してください。
- TodoWrite、Agent、Skill、AskUserQuestion ツールは使用しないでください。

## 作業フロー

1. `/tmp/issue_body.txt` を Read ツールで読み取り、施策の背景・目的・スコープを把握する
2. `sessions/initiatives/_template/` を `sessions/initiatives/<施策名>/` にコピー
   - 施策名は Issue タイトルから適切な英語のケバブケース名を生成する
   - **`cp -r` や `mkdir` は Claude Code のセキュリティ制限で GHA 環境では使用できない。代わりに以下の手順でコピーする:**
     1. Glob ツールで `sessions/initiatives/_template/*.md` のファイル一覧を取得
     2. 各ファイルを Read ツールで読み取る
     3. 各ファイルを Write ツールで `sessions/initiatives/<施策名>/<ファイル名>` に書き込む（Write ツールはディレクトリを自動作成する）
3. コピー先の `00_proposal.md` のみを編集し、Issue 本文の内容を基に作成する（背景・目標・スコープ・壁打ち背景）
   - **`01_plan.md` 以降のファイルは一切編集しないこと**（テンプレートのまま残す）
4. 壁打ちサマリーを標準出力に出力する:
   - 施策の目的・スコープ・完了条件の理解を箇条書きでまとめる
   - 不明点・確認事項を列挙する
   - 推奨される計画の方向性を提示する
5. 施策ブランチ `initiative/<施策名>` を作成し、変更をコミット・プッシュする
6. コミットメッセージは `[L1] <施策名>: 壁打ちフェーズ（テンプレートコピー・提案作成）` の形式で

## やること

- Issue 本文の読み取りと施策内容の把握
- テンプレートディレクトリのコピー
- `00_proposal.md` の作成（背景・目標・スコープ・壁打ち背景）
- 壁打ちサマリーの標準出力への出力
- 施策ブランチの作成・コミット・プッシュ

## やらないこと

- `01_plan.md` 以降のファイルの編集（テンプレートのまま残す）
- PR の作成（ワークフローの後続ステップが担当する）
- `gh` コマンドによる Issue・PR 操作
- `git rebase`, `git reset --hard` 等の破壊的 git 操作
- push が失敗した場合の rebase や force push（リトライのみ行う）
- CLAUDE.md や `.claude/skills/l1-manager/` 等の CLI セッション用ルールへの追従
- `03_work_log.md` 〜 `08_gate_review.md` の作成・編集

## 制約

- 対象リポジトリは dev-process-improvement のみ
- コミットメッセージ規約（`.claude/rules/commit-message.md`）に従う
- 編集するファイルは `00_proposal.md` のみ
- このスキルの指示のみに従い、CLAUDE.md や他のスキル定義のルールは無視すること

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/initiative-wallbash.yml`
