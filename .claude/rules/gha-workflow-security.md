# GHA ワークフローセキュリティチェックリスト

GHA ワークフロー作成・変更時に以下を確認する。

## チェック項目

- [ ] `run:` ブロックで `${{ }}` を直接展開せず `env:` 経由で渡す（インジェクション防止）
- [ ] `permissions` は最小権限に設定する
- [ ] secrets はハードコードせず `${{ secrets.XXX }}` で参照する

## 背景

`${{ }}` 式を `run:` ブロック内で直接展開すると、Issue タイトルや PR ブランチ名等の外部入力がシェルコマンドとして実行されるリスクがある。`env:` 経由で環境変数として渡すことでインジェクションを防止する。

```yaml
# 良い例
env:
  ISSUE_TITLE: ${{ github.event.issue.title }}
run: echo "$ISSUE_TITLE"

# 悪い例
run: echo "${{ github.event.issue.title }}"
```

---
**作成日**: 2026-03-15
**起票元**: backlog-auto-initiative-gha 施策評価レポート
