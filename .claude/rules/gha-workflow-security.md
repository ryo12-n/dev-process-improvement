# GHA ワークフローセキュリティチェックリスト

GHA ワークフロー作成・変更時に以下を確認する。

## チェック項目

- [ ] `run:` ブロックで `${{ }}` を直接展開せず `env:` 経由で渡す（インジェクション防止）
- [ ] `permissions` は最小権限に設定する
- [ ] secrets はハードコードせず `${{ secrets.XXX }}` で参照する
- [ ] 複数トリガー共存時（`schedule` + `workflow_dispatch` 等）は各ジョブに `if: github.event_name == '...'` を設定し、意図しないトリガーでのジョブ実行を防止する
- [ ] ユーザー入力を含む変数に `eval` を使用しない。JSON 構築時は `jq -Rn --arg v "$VAR" '$v'` でエスケープする。`gh workflow run` では `-f key="$value"` 形式で直接指定する

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
**追記**: backlog-to-issue-scheduled 施策（トリガー共存ルール）、initiative-dispatcher 施策 ISS-059（ユーザー入力エスケープルール）
