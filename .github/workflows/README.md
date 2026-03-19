# GitHub Actions ワークフロー

## クイックスタート

1. **Issue を作成**し、施策の背景・目的・スコープを本文に記載する
2. Issue に `@ai /start` とコメント → AI が壁打ちサマリー（proposal/plan/tasks のドラフト含む）を投稿
3. フィードバックがあれば `@ai /continue <フィードバック>` で壁打ちを繰り返す（何度でも可）
4. 内容を承認し `@ai /approve` とコメント → AI が PR 作成 + 自律実行しゲート判定を投稿
5. ゲート判定を確認し `@ai /approve` とコメント → AI がクローズ処理を実行
6. 自動作成された PR をマージして完了

> バックログから起票する場合は Actions タブから「Backlog to Issue」を手動実行する（BL-XXX 形式で ID を指定）。Issue 作成後に壁打ちフェーズが自動起動する。

---

## コマンドリファレンス

すべてのコマンドは `@ai /command` 形式で Issue コメントに投稿する。

| コマンド | 用途 | 使用可能なフェーズ |
|---------|------|-----------------|
| `@ai /start` | 施策を開始（壁打ちフェーズ） | ラベルなし |
| `@ai /continue <フィードバック>` | 壁打ちを継続（フィードバック反映・ドラフト更新） | wallbashing |
| `@ai /approve` | 現フェーズを承認して次へ進む | wallbashing / gate-review |
| `@ai /reject` | ゲート判定を差し戻して修正を指示 | gate-review |
| `@ai /question` | 施策の現状について質問する | 任意のフェーズ |

### 使用例

```
@ai /start
```

```
@ai /continue スコープをもう少し絞って、○○に集中してほしい
```

```
@ai /approve
```

```
@ai /reject ○○の部分が不十分。△△を修正してほしい
```

```
@ai /question 現在のタスク進捗はどうなっている？
```

> コマンドの後に自然言語でフィードバックや質問を追加できる。

---

## フロー図

```
Issue 作成
  │
  ▼
@ai /start
  │
  ▼
[dispatcher] → [wallbash init] ── 壁打ちサマリーを Issue コメントに投稿
  │                               ├── テンプレートコピー
  │                               ├── 00_proposal, 01_plan, 02_tasks ドラフト作成
  │                               ├── 00a_wallbash_log.md に Round 1 記録
  │                               ├── 📋 メタデータコメント投稿
  │                               └── 施策ブランチ作成（PR は作成しない）
  ▼
@ai /continue <フィードバック>  ← 何度でも繰り返し可能
  │
  ▼
[dispatcher] → [wallbash continue] ── フィードバック反映・ドラフト更新
  │                                    ├── 00a_wallbash_log.md からコンテキスト復元
  │                                    └── Round N 追記
  ▼
@ai /approve [フィードバック]
  │
  ▼
[dispatcher] → [execute] ── PR 作成 + 自律実行（メタデータから施策を特定）
  │              ↑           ├── 壁打ちドラフトを活用して 01_plan, 02_tasks 最終化
  │              │           ├── タスク実行 (03〜04)
  │              │           ├── 評価 (05〜06)
  │              │           ├── 課題記録 (07)
  │              │           └── ゲート判定 (08) → Issue コメントに投稿
  │              │
@ai /reject [理由]
  │
  ▼
@ai /approve
  │
  ▼
[dispatcher] → [close] ── クローズ処理（メタデータから施策を特定）
                            ├── 知見ルーティング (inbox/)
                            ├── アーカイブ移動 (_archive/)
                            └── Issue クローズ + ラベル更新
                               │
                               ▼
                           PR マージ（人間）
```

---

## メタデータコメント

`@ai /start` 実行時に、壁打ちワークフローが自動的に Issue の最初のコメントとしてメタデータを投稿する。後続ワークフロー（execute / close / question）はこのメタデータから施策ディレクトリとブランチを取得する。

### フォーマット

```html
<!-- initiative-metadata
initiative_name: <施策名>
initiative_dir: sessions/initiatives/<施策名>/
branch: initiative/<施策名>
-->
📋 **施策メタデータ**
| 項目 | 値 |
|------|-----|
| 施策名 | `<施策名>` |
| ディレクトリ | `sessions/initiatives/<施策名>/` |
| ブランチ | `initiative/<施策名>` |
```

- HTML コメント部分: ワークフローが機械的にパースして使用
- テーブル部分: 人間が Issue 上で確認できる可視化

> メタデータコメントが見つからない場合、ディスパッチャーはエラーを返す。

---

## ラベル一覧

リポジトリに以下のラベルを作成しておく:

| ラベル | 用途 |
|-------|------|
| `initiative` | 施策 Issue のマーカー |
| `initiative:wallbashing` | 壁打ち中 |
| `initiative:executing` | 実行中 |
| `initiative:gate-review` | ゲート判定待ち |
| `initiative:completed` | 完了 |

---

## ワークフロー一覧

### Initiative 系（ディスパッチャー経由）

| ワークフロー | トリガー | 用途 |
|-------------|---------|------|
| `initiative-dispatcher.yml` | Issue コメント (`@ai`) | コマンド解析・メタデータ取得・ルーティング |
| `initiative-wallbash.yml` | workflow_dispatch | 壁打ちフェーズ（init: ドラフト作成・メタデータ投稿 / continue: フィードバック反映） |
| `initiative-execute.yml` | workflow_dispatch | 実行フェーズ（計画〜評価〜ゲート判定） |
| `initiative-close.yml` | workflow_dispatch | クローズ（アーカイブ・知見ルーティング） |
| `initiative-question.yml` | workflow_dispatch | 施策への質問応答（読み取り専用） |
| `initiative-batch-approve.yml` | workflow_dispatch | gate-review フェーズの施策を一括承認 |

### バックログ・トリアージ系

| ワークフロー | トリガー | 用途 |
|-------------|---------|------|
| `backlog-to-issue.yml` | schedule（3時間間隔） / 手動 | バックログ → Issue 起票 → 壁打ち自動開始 |
| `daily-triage.yml` | スケジュール / 手動 | デイリートリアージ |

---

## セットアップ

リポジトリの Settings > Secrets > Actions に `ANTHROPIC_API_KEY` を設定する。
