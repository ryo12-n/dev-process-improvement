---
name: fork-sync
description: 'upstream/origin の双方向 git 同期。対象リポジトリを選択し fast-forward マージで同期する'
user-invocable: true
allowed-tools: ["Read", "Bash", "Glob"]
---
# fork-sync --- upstream/origin 双方向 git 同期

## 概要

upstream（外部リポジトリ）と origin（社内リポジトリ）の main ブランチを fast-forward マージで同期するスキル。
複数リポジトリを一元管理し、対話的にリポジトリと同期方向を選択して実行する。

> **sync-manager との違い**: sync-manager はリポジトリ間の構成・ルール・テンプレートの同期（ファイルコピー・差分適用）を行う。本スキルは upstream ↔ origin の git レベルの同期（fetch → ff-only merge → push）のみを行う。

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

### Step 4: 同期実行

選択されたリポジトリの `local_path` に移動し、以下を順に実行する。

1. **未コミット変更の確認**
   ```bash
   cd {local_path}
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

4. **差分の表示**
   ```bash
   git log --oneline -5
   git diff {target_remote}/main
   ```

### Step 5: push 前確認

**push は自動実行しない。** 差分を表示した後、ユーザーに確認を求める。

- upstream → origin の場合:
  ```
  上記の内容で origin に push します。実行してよいですか？
  ```

- origin → upstream の場合:
  ```
  上記の内容で upstream に push します。
  gh アカウントを ryo12-n に切り替えて push します。実行してよいですか？
  ```

### Step 6: push 実行

ユーザーが承認したら push を実行する。

- upstream → origin の場合:
  ```bash
  git push origin main
  ```

- origin → upstream の場合:
  ```bash
  gh auth switch --user {accounts.upstream}
  git push upstream main
  gh auth switch --user {accounts.origin}
  ```

### Step 7: 完了メッセージ

同期結果をまとめて表示する。

```
同期完了:
- リポジトリ: {name}
- 方向: {direction}
- push 先: {remote}
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

---

## やること

- `repos.json` を読み込んでリポジトリ一覧を番号付きで提示する
- ユーザーの選択に基づき git 同期を実行する
- push 前に必ずユーザー確認を取る
- origin → upstream 同期時に gh auth switch を実行し、完了後に元に戻す

## やらないこと

- push を自動実行しない（ユーザー確認必須）
- リポジトリの構成同期（ファイルコピー等）は行わない（それは sync-manager の役割）
- repos.json に存在しないリポジトリの同期
- repos.json の編集（リポジトリの追加・削除は手動で repos.json を編集する）
