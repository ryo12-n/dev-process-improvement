# 改善施策提案: initiative-dispatcher

## 背景・課題

現在の initiative ワークフロー（wallbash / execute / close）は `issue_comment` イベントで個別にトリガーされる。GitHub Actions は `issue_comment` を持つ**すべてのワークフロー**を評価するため、フェーズに該当しないワークフローも「Skipped」として Actions 履歴に残り、以下の問題が発生している:

1. **ノイズの蓄積**: フェーズに無関係なワークフローが Skipped ランとして記録され、Actions 履歴が汚れる
2. **可読性の低下**: 人間がどのアクションが実際に動いたか判別しにくい
3. **コマンド体系の非統一**: ラベル操作（`initiative-start`）とコメント操作（`/approve`, `/reject`）が混在し、人間の操作が分かりにくい

## 目標

1. 不要な Skipped ランを完全に排除する
2. 人間→AI の操作を `@ai-task /command` 形式に統一し、分かりやすいインターフェースを提供する
3. フェーズに応じた適切なワークフローのみが起動する仕組みを構築する

## スコープ
### やること
- ディスパッチャーワークフロー（`initiative-dispatcher.yml`）の新規作成
- Q&A ワークフロー（`initiative-question.yml`）の新規作成
- 既存 initiative ワークフロー（wallbash / execute / close）のトリガーを `workflow_dispatch` に変更
- `backlog-to-issue.yml` のディスパッチャー経由化
- `initiative-start` ラベルの廃止

### やらないこと
- `backlog-auto-execute.yml` の変更（自動実行パス、人間トリガーではない）
- `daily-triage.yml` の変更（定期実行タスク）
- `test-permissions.yml` の変更
- `backlog-candidate-propose.yml` の変更
- ワークフロー内の Claude プロンプト内容の変更（トリガー・入力部分のみ変更）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- Actions 履歴から Skipped ランが排除され、実行されたワークフローのみが表示される
- `@ai-task /command` の統一インターフェースにより、人間にとって操作が直感的になる
- ディスパッチャーによるルーティングで、フェーズ不一致時にエラーメッセージが返る（サイレント失敗の排除）

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| `workflow_dispatch` で Issue コンテキストの受け渡しに漏れ | 中 | inputs の設計を現行のコンテキスト抽出ロジックと照合 |
| `gh workflow run` の権限要件（`actions: write`） | 低 | GITHUB_TOKEN で同一リポジトリ内の dispatch は可能 |
| 移行中の二重発火 | 低 | 全変更を1コミットでアトミックに適用 |

## 壁打ちの背景

### 方式の選定
- 案A（ディスパッチャーのみ）と案B（ディスパッチャー＋コマンド体系見直し）を検討し、案Bを選択
- 理由: ディスパッチャー導入と同時にコマンド体系を統一することで、人間側の操作改善も同時に達成できる

### コマンド形式
- `@ai-task` プレフィックスを必須とする（後方互換の素コマンドは受け付けない）
- 理由: 明示的なAI宛て指示であることを示し、誤発火を防止する

### `/question` コマンド
- 本施策のスコープに含め、`initiative-question.yml` として新規作成する
- 施策ファイルを読み取り専用で参照し、Issue コメントで回答する

### `initiative-start` ラベル
- 完全廃止する（トリガーとしてもメタデータとしても使用しない）
- `backlog-to-issue.yml` は Issue 作成後に `gh workflow run` で wallbash を直接 dispatch する

### スコープ外の判断
- `backlog-auto-execute.yml`: 自動実行パスであり人間トリガーではないため、ディスパッチャーの対象外
- `daily-triage.yml`: 定期実行タスクであり、人間→AI の橋渡しではないため対象外

## 備考・設計パターン

### ルーティングテーブル

| コマンド | 必要なラベル | 起動先 |
|---------|------------|--------|
| `/start` | なし（initiative ラベルがないこと） | `initiative-wallbash.yml` |
| `/approve` | `initiative:wallbashing` | `initiative-execute.yml` |
| `/reject` | `initiative:gate-review` | `initiative-execute.yml` |
| `/approve` | `initiative:gate-review` | `initiative-close.yml` |
| `/question` | `initiative`（任意フェーズ） | `initiative-question.yml` |

### ラベルライフサイクル（変更後）

```
(ラベルなし)
  ↓ @ai-task /start
initiative + initiative:wallbashing
  ↓ @ai-task /approve
initiative + initiative:executing → initiative + initiative:gate-review
  ↓ @ai-task /approve (完了) or /reject (差し戻し)
initiative + initiative:completed (Issue close)
```

---
**起票者**: L1
**起票日**: 2026-03-15
**ステータス**: 実施中
**backlog元ファイル**: なし
