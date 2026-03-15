# 改善施策提案: initiative-metadata-comment

## 背景・課題
現在の initiative ワークフロー（execute / close / question）は、Issue 番号から PR を検索（`gh pr list --search`）し、ブランチをチェックアウトした後に Claude が `sessions/initiatives/` を Glob で探索して施策ディレクトリを特定している。この間接的なチェーン（Issue → PR検索 → ブランチ → Glob探索）は脆弱で、以下の問題がある:

- PR が見つからない場合にワークフローが失敗する
- 複数施策が同時進行する場合に誤った施策を参照する可能性がある
- Claude の施策ディレクトリ探索に無駄なターン数を消費する

## 目標
wallbash が施策開始時に Issue の最初のコメントとしてメタデータを投稿し、後続ワークフローがそこから直接 `initiative_dir` と `branch` を取得する方式に変更する。PR 検索ロジックを全廃する。

## スコープ
### やること
- wallbash に施策名抽出・メタデータコメント投稿ステップを追加
- dispatcher にメタデータ抽出ステップを追加し、sub-workflow に `initiative_dir` / `branch` をパススルー
- execute / close / question の inputs に `initiative_dir` / `branch` を追加し、PR 検索ロジックを削除
- README.md にメタデータコメントの説明を追加

### やらないこと
- backlog-to-issue.yml の変更（wallbash を dispatch するだけなので変更不要）
- メタデータコメントの編集・更新機能（初回投稿のみ）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果
- PR 検索の脆弱性を完全に排除
- Claude の施策ディレクトリ探索ターンを削減（直接パス指定）
- Issue 上でメタデータが人間にも可視化される

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| Claude が施策名を正しく出力しない | 中 | INITIATIVE_NAME プレフィックス形式で明示的に指示 |
| 既存 Issue にメタデータがない | 低 | 既存施策は手動でメタデータコメントを追加するか、フォールバックで PR 検索を残す |

## 壁打ちの背景
前施策（initiative-dispatcher）の `/question` ワークフロー調査で、Issue → 施策ディレクトリの紐付けが脆弱であることが判明。4つの方式（A: Issue本文, B: ラベル, C: タイトルID, D: 自動コメント）を壁打ちした結果、案D（wallbash が自動的にメタデータコメントを投稿）を採用。理由: Issue 本文を汚さず、ラベルの用途をフェーズ管理に限定でき、機械パース（HTML コメント）と人間可読（テーブル）を両立できる。

## 備考・設計パターン
メタデータコメントは HTML コメント（機械パース用）+ Markdown テーブル（人間可読）の二層構造:
```
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

---
**起票者**: L1
**起票日**: 2026-03-15
**ステータス**: 実施中
**backlog元ファイル**: なし
