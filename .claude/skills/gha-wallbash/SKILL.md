---
name: gha-wallbash
description: 'GHA initiative-wallbash ワークフロー専用スキル。壁打ちフェーズ（init: テンプレートコピー・ドラフト作成 / continue: フィードバック反映・ドラフト更新）を実行する。'
user-invocable: false
---
# GHA 壁打ちフェーズスキル

## コンテキスト

このファイルは GitHub Actions の `initiative-wallbash.yml` ワークフローから `claude-code-action` 経由で実行される自動化スキルです。リポジトリオーナーが設定したワークフローから呼び出されており、`permissions.allow` で許可されたツールのみが使用可能です。

## あなたの役割

あなたは initiative の壁打ちフェーズを実行するエージェントです。
壁打ちフェーズは **init**（初回）と **continue**（継続）の2モードで動作します。

- **init モード**: テンプレートコピー + `00_proposal.md`, `01_plan.md`, `02_tasks.md` のドラフト作成 + `00a_wallbash_log.md` の Round 1 記録
- **continue モード**: `00a_wallbash_log.md` を読んでコンテキスト復元 → フィードバック反映 → ドラフト更新 → ログ追記

### 成果物範囲

- `00_proposal.md` — 提案書ドラフト
- `01_plan.md` — 実施計画ドラフト
- `02_tasks.md` — タスクリストドラフト
- `00a_wallbash_log.md` — 壁打ちログ（コンテキスト保持）

## 作業フロー

### init モード（mode=init）

1. `/tmp/issue_body.txt` を Read ツールで読み取り、施策の背景・目的・スコープを把握する
2. `sessions/initiatives/_template/` を `sessions/initiatives/<施策名>/` にコピー
   - 施策名は Issue タイトルから適切な英語のケバブケース名を生成する
   - 以下の手順でコピーする:
     1. Glob ツールで `sessions/initiatives/_template/*.md` のファイル一覧を取得
     2. 各ファイルを Read ツールで読み取る
     3. 各ファイルを Write ツールで `sessions/initiatives/<施策名>/<ファイル名>` に書き込む（Write ツールはディレクトリを自動作成する）
3. コピー先の以下のファイルを編集する:
   - `00_proposal.md` — Issue 本文の内容を基にドラフトを作成（背景・目標・スコープ・壁打ち背景）
   - `01_plan.md` — 提案内容に基づく実施計画のドラフトを作成
   - `02_tasks.md` — 計画に基づくタスクリストのドラフトを作成
4. `00a_wallbash_log.md` に Round 1 を記録する:
   - 「現在の合意事項」セクションを更新（目的・スコープ・計画の方向性・未解決事項）
   - 「イテレーション履歴」に Round 1 を追記（入力: Issue 本文の要約、調査・推論、更新内容、合意事項の変更）
5. 壁打ちサマリーを標準出力に出力する:
   - 施策の目的・スコープ・完了条件の理解を箇条書きでまとめる
   - 不明点・確認事項を列挙する
   - 推奨される計画の方向性を提示する
   - ドラフトの概要（proposal/plan/tasks の要点）を提示する
6. 施策ブランチ `initiative/<施策名>` を作成し、変更をコミット・プッシュする
7. コミットメッセージは `[L1] <施策名>: 壁打ちフェーズ Round 1（テンプレートコピー・ドラフト作成）` の形式で

### continue モード（mode=continue）

1. 施策ディレクトリの `00a_wallbash_log.md` を Read ツールで読み取り、コンテキストを復元する
   - 「現在の合意事項」セクションから施策の目的・スコープ・計画方向性・未解決事項を把握する
   - 「イテレーション履歴」から過去のラウンドの経緯を把握する
2. フィードバック内容（`/tmp/feedback.txt` に保存済み）を Read ツールで読み取る
3. 既存のドラフト（`00_proposal.md`, `01_plan.md`, `02_tasks.md`）を読み取る
4. フィードバックを反映してドラフトを更新する:
   - フィードバックの指摘に対応して各ドラフトを修正する
   - 新たな調査が必要な場合はリポジトリ内を調査する
5. `00a_wallbash_log.md` を更新する:
   - 「現在の合意事項」セクションを最新の合意内容で上書きする
   - 「イテレーション履歴」に新しい Round N を追記する（入力: フィードバック内容、調査・推論、更新内容、合意事項の変更）
6. 壁打ちサマリーを標準出力に出力する:
   - 前回からの変更点を要約する
   - フィードバックへの対応内容を説明する
   - 残る未解決事項・次のアクションを提示する
7. 変更をコミット・プッシュする
8. コミットメッセージは `[L1] <施策名>: 壁打ちフェーズ Round N（フィードバック反映）` の形式で

## やること

- Issue 本文（init）またはフィードバック（continue）の読み取りと施策内容の把握
- テンプレートディレクトリのコピー（init のみ）
- `00_proposal.md`, `01_plan.md`, `02_tasks.md` のドラフト作成・更新
- `00a_wallbash_log.md` のコンテキスト記録
- 壁打ちサマリーの標準出力への出力
- 施策ブランチの作成（init のみ）・コミット・プッシュ

## やらないこと

- PR の作成（`/approve` 時に `initiative-execute.yml` が担当する）
- `gh` コマンドによる Issue・PR 操作
- `git rebase`, `git reset --hard` 等の破壊的 git 操作
- push が失敗した場合の rebase や force push（リトライのみ行う）
- `03_work_log.md` 〜 `08_gate_review.md` の作成・編集

## 制約

- 対象リポジトリは dev-process-improvement のみ
- コミットメッセージ規約（`.claude/rules/commit-message.md`）に従う
- 編集するファイルは `00_proposal.md`, `01_plan.md`, `02_tasks.md`, `00a_wallbash_log.md` のみ

---
**作成日**: 2026-03-15
**対応ワークフロー**: `.github/workflows/initiative-wallbash.yml`
