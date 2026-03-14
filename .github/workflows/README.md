# GitHub Actions ワークフロー

## 概要

本リポジトリの GitHub Actions ワークフローの一覧と使い方。

## ワークフロー一覧

| ワークフロー | トリガー | 用途 |
|-------------|---------|------|
| `initiative-wallbash.yml` | Issue ラベル / 手動 | 施策の壁打ちフェーズ |
| `initiative-execute.yml` | Issue コメント | 施策の実行フェーズ |
| `initiative-close.yml` | Issue コメント | 施策のクローズ |
| `backlog-to-issue.yml` | 手動 | バックログ → Issue 起票 → initiative チェーン連携 |
| `backlog-auto-execute.yml` | 手動 | バックログ施策の自動実行 |
| `backlog-candidate-propose.yml` | 手動 | バックログ候補の提案 |
| `daily-triage.yml` | スケジュール / 手動 | デイリートリアージ |

---

## Initiative ワークフロー

Issue ベースの対話型ワークフロー。施策の起票からクローズまでを3つのワークフローで実現する。

### 前提準備

#### 1. ラベルの作成

リポジトリに以下の6つのラベルを作成する:

| ラベル | 用途 |
|-------|------|
| `initiative-start` | 施策起票トリガー（ユーザーが付与） |
| `initiative` | 施策 Issue のマーカー |
| `initiative:wallbashing` | 壁打ち中 |
| `initiative:executing` | 実行中 |
| `initiative:gate-review` | ゲート判定待ち |
| `initiative:completed` | 完了 |

#### 2. Secrets の設定

リポジトリの Settings > Secrets > Actions に `ANTHROPIC_API_KEY` を設定する。

### 使い方

#### Step 1: Issue を作成

**方法 A: バックログから起票（推奨）**

Actions タブから「Backlog to Issue」を手動実行し、`initiative_name` にバックログの施策名を入力する。backlog.csv からエントリを読み取り、Issue が自動作成される。

**方法 B: 手動で Issue を作成**

Issue を作成し、施策の背景・目的・スコープを本文に記載する。`initiative-start` ラベルを付与する。

```
タイトル: ○○の改善
本文:
  ## 背景
  ...
  ## 目的
  ...
  ## スコープ
  ...
```

#### Step 2: 壁打ちサマリーを確認

`initiative-wallbash.yml` が自動起動し、以下を実行する:

- `sessions/initiatives/<施策名>/` にテンプレートをコピー
- `00_proposal.md` を作成
- 壁打ちサマリーを Issue コメントに投稿
- 施策ブランチ + PR を作成

ラベルが `initiative-start` → `initiative` + `initiative:wallbashing` に遷移する。

#### Step 3: 実行フェーズに進む

壁打ちサマリーを確認し、Issue に以下のコメントを投稿する:

```
/approve
```

フィードバックを添えることもできる:

```
/approve スコープをもう少し絞って、○○に集中してほしい
```

`initiative-execute.yml` が自動起動し、計画 → タスク実行 → 評価 → ゲート判定を一貫して実行する。完了後、ゲート判定サマリーが Issue コメントに投稿される。

ラベルが `initiative:wallbashing` → `initiative:executing` → `initiative:gate-review` に遷移する。

#### Step 4: ゲート判定を確認

ゲート判定サマリーを確認し、以下のいずれかをコメントする:

**承認する場合:**

```
/approve
```

`initiative-close.yml` が起動し、アーカイブ移動 → 知見ルーティング → Issue クローズを実行する。ラベルが `initiative:completed` に遷移する。

**差し戻す場合:**

```
/reject 理由やフィードバック
```

`initiative-execute.yml` が再起動し、フィードバックを反映して修正・再実行する。

#### Step 5: PR をマージ

施策完了後、自動作成された PR をマージして完了。

### フロー図

```
Issue 作成 + initiative-start ラベル
  │
  ▼
wallbash.yml ─── 壁打ちサマリーを Issue コメントに投稿
  │                ├── テンプレートコピー
  │                ├── 00_proposal.md 作成
  │                └── 施策ブランチ + PR 作成
  ▼
人間: /approve [フィードバック]
  │
  ▼
execute.yml ─── 自律実行
  │               ├── 01_plan.md, 02_tasks.md 作成
  │               ├── タスク実行 (03〜04)
  │               ├── 評価 (05〜06)
  │               ├── 課題記録 (07)
  │               └── ゲート判定 (08) → Issue コメントに投稿
  ▼
人間: /approve ──────────────┐
人間: /reject [理由] ──┐     │
  │                    │     │
  │    execute.yml ◀───┘     │
  │    (修正・再実行)         │
  │                          ▼
  │                    close.yml ─── クローズ処理
  │                       ├── 知見ルーティング (inbox/)
  │                       ├── アーカイブ移動 (_archive/)
  │                       └── Issue クローズ + ラベル更新
  │                          │
  │                          ▼
  └─────────────────── PR マージ（人間）
```

### 手動トリガー

ラベル付与でトリガーされなかった場合、Actions タブから `Initiative Wallbash` を手動実行できる。Issue 番号を入力して起動する。

### 注意事項

- 各ワークフローは `anthropics/claude-code-action@v1` を使用する
- `claude-sonnet-4-6` モデルを使用（execute は max-turns 80、wallbash/close は 30）
- PR コメントや bot コメントではトリガーされない（`issue_comment` のフィルタリング済み）
- gh 操作は Claude のツール権限ではなく Shell ステップで実行（最小権限の原則）
