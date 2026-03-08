---
name: fork-sync
description: 'upstream/origin の双方向 git 同期。対象リポジトリを選択し、ブランチ + PR 方式で fast-forward マージを行う'
user-invocable: true
allowed-tools: ["Read", "Bash", "Glob"]
---
# fork-sync --- upstream/origin 双方向 git 同期

## 概要

upstream（外部リポジトリ）と origin（社内リポジトリ）の main ブランチを fast-forward マージで同期するスキル。
複数リポジトリを一元管理し、対話的にリポジトリと同期方向を選択して実行する。

**main への直接 push は行わない。** 同期用ブランチを作成し、PR を通じて差分確認・マージする。

> **sync-manager との違い**: sync-manager はリポジトリ間の構成・ルール・テンプレートの同期（ファイルコピー・差分適用）を行う。本スキルは upstream ↔ origin の git レベルの同期（fetch → ff-only merge → PR）のみを行う。

## 設定ファイル

同期対象リポジトリの一覧は同ディレクトリの `repos.json` で管理する。
スキル実行時に以下のパスから読み込む:

```
.claude/skills/fork-sync/repos.json
```

---

## 対話フロー

### Step 1: リポジトリ選択

`repos.json` を読み込み、`repositories` 配列から番号付きリストを生成してユーザーに提示する。

```
同期するリポジトリを選択してください:
1. ai-driven-dev-patterns
2. dev-process-improvement
```

ユーザーの番号入力を待つ。

### Step 2: 同期方向の選択

```
同期方向を選択してください:
1. upstream → origin（upstream で PR マージした場合）
2. origin → upstream（origin で PR マージした場合）
```

ユーザーの番号入力を待つ。

### Step 3: 選択内容の確認

選択結果をまとめて表示し、実行確認を行う。

```
以下の内容で同期を実行します:
- リポジトリ: {name}
- 方向: {upstream → origin / origin → upstream}
- ローカルパス: {local_path}

実行してよいですか？
```

### Step 4: 同期用ブランチの作成

選択されたリポジトリの `local_path` に移動し、同期用ブランチを作成する。

```bash
cd {local_path}
git checkout main
git pull origin main
```

ブランチ名の規則:
- upstream → origin の場合: `sync/upstream-to-origin-YYYYMMDD`
- origin → upstream の場合: `sync/origin-to-upstream-YYYYMMDD`

同日に複数回実行する場合は連番を付与する（`-YYYYMMDD-2`）。

```bash
git checkout -b sync/{direction}-YYYYMMDD
```

### Step 5: 同期実行

ブランチ上で以下を順に実行する。

1. **未コミット変更の確認**
   ```bash
   git diff --quiet && git diff --cached --quiet
   ```
   未コミット変更がある場合はエラーメッセージを表示して中断する。

2. **ソースリモートから fetch**
   - upstream → origin の場合: `git fetch upstream`
   - origin → upstream の場合: `git fetch origin`

3. **fast-forward マージ**
   - upstream → origin の場合: `git merge --ff-only upstream/main`
   - origin → upstream の場合: `git merge --ff-only origin/main`

   fast-forward できない場合はエラーメッセージを表示し、「同時マージが発生した場合の対処」を案内して中断する。

### Step 6: 差分の表示

```bash
git log --oneline main..HEAD
git diff main
```

同期された変更内容をユーザーに提示する。

### Step 7: ブランチ push + PR 作成

ユーザーに確認後、ブランチを push して PR を作成する。

**upstream → origin の場合:**

```bash
git push -u origin sync/{direction}-YYYYMMDD
```

PR 作成:
```bash
gh pr create --base main --head sync/{direction}-YYYYMMDD \
  --title "[sync] {direction}: {name} main ブランチを同期" \
  --body "upstream の最新変更を origin に同期する。"
```

**origin → upstream の場合:**

```bash
# upstream push 用アカウントに切り替え
gh auth switch --user {accounts.upstream}

git push -u upstream sync/{direction}-YYYYMMDD

# upstream 側で PR 作成
gh pr create --repo {upstream_url} --base main --head sync/{direction}-YYYYMMDD \
  --title "[sync] {direction}: {name} main ブランチを同期" \
  --body "origin の最新変更を upstream に同期する。"

# アカウントを元に戻す
gh auth switch --user {accounts.origin}
```

### Step 8: gh pr create 失敗時のフォールバック

`gh pr create` が失敗した場合（Enterprise Managed User 制限等）、以下を実施する:

1. ブランチが push 済みであることを確認する
2. GitHub の PR 作成 URL を提示する:
   ```
   https://github.com/{owner}/{repo}/pull/new/sync/{direction}-YYYYMMDD
   ```
3. PR タイトルと本文をユーザーにコピー可能な形式で提示する

### Step 9: 完了メッセージ

同期結果をまとめて表示する。

```
同期完了:
- リポジトリ: {name}
- 方向: {direction}
- ブランチ: sync/{direction}-YYYYMMDD
- PR: {PR URL またはフォールバック URL}

PR をマージして同期を完了してください。
```

---

## エラーハンドリング

### 未コミット変更がある場合

```
ERROR: 未コミットの変更があります。
すべての変更をコミットしてから再実行してください。
```

中断する。ユーザーにコミットを促す。

### fast-forward できない場合（同時マージ）

```
ERROR: fast-forward マージができませんでした。
origin と upstream の両方で同時に変更がマージされた可能性があります。

対処方法:
1. git fetch upstream && git fetch origin
2. git merge upstream/main（コンフリクトがあれば手動解消）
3. 解消後、両方のリモートに push して同期を回復
```

中断する。手動対処を案内する。

### gh アカウントが未登録の場合

```
ERROR: {account} アカウントが gh に登録されていません。
gh auth login でアカウントを追加してから再実行してください。
```

origin → upstream 同期の場合のみ発生しうる。中断する。

### ローカルパスが存在しない場合

```
ERROR: ローカルパス {local_path} が存在しません。
repos.json の設定を確認してください。
```

### gh pr create が失敗した場合

上記 Step 8 のフォールバック手順を実行する。PR 作成 URL とタイトル・本文を提示する。

---

## やること

- `repos.json` を読み込んでリポジトリ一覧を番号付きで提示する
- ユーザーの選択に基づき同期用ブランチを作成し、git 同期を実行する
- ブランチを push して PR を作成する（main への直接 push は行わない）
- `gh pr create` 失敗時はフォールバック URL を提示する
- origin → upstream 同期時に gh auth switch を実行し、完了後に元に戻す

## やらないこと

- main ブランチへの直接 push（PR 経由でマージする）
- PR のマージ（ユーザーが GitHub 上で実施する）
- リポジトリの構成同期（ファイルコピー等）は行わない（それは sync-manager の役割）
- repos.json に存在しないリポジトリの同期
- repos.json の編集（リポジトリの追加・削除は手動で repos.json を編集する）
