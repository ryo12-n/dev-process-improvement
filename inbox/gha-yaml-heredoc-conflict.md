# GHA ワークフロー: YAML ブロックスカラーと HEREDOC の競合

## 知見

GHA ワークフローの `run: |` ブロックスカラー内で HEREDOC を使う場合、HEREDOC の内容がインデントなし（column 1）だと YAML パーサーがブロックスカラーの終了と解釈し、構文エラーになる。

## 症状

- GitHub が `workflow_dispatch` トリガーを認識しない（422 エラー）
- `Invalid workflow file - You have an error in your yaml syntax on line XXX` エラー
- ワークフローが UI の Actions タブに表示されない、または dispatch できない

## 原因の仕組み

YAML ブロックスカラー（`|`）は、最初の内容行のインデントレベルで境界を決める。HEREDOC 内容がインデントなしで書かれると、YAML パーサーにとってはブロックの外に出た扱いになる。特にマークダウンテーブルの `|` が YAML 構文として誤認される。

```yaml
# NG: HEREDOC 内容が column 1
        run: |
          gh pr edit "$pr_number" --body "$(cat <<PRBODY
## Title
| col1 | col2 |   ← YAML パーサーが構文エラーと判断
PRBODY
          )"
```

## 対策

`cat > /tmp/file.md << DELIMITER` + `--body-file` 方式に変更する。HEREDOC 内容を `run: |` のインデントレベルに揃えれば、YAML パーサーがブロックスカラー内として正しく解釈する。

```yaml
# OK: HEREDOC 内容をインデントレベルに揃え、ファイル経由で渡す
        run: |
          cat > /tmp/pr_body.md << PRBODY
          ## Title
          | col1 | col2 |
          PRBODY
          gh pr edit "$pr_number" --body-file /tmp/pr_body.md
```

## 教訓

- コメント追加や空コミットでは YAML パーサーの再評価は起きない（コメントは YAML にとって無変更）
- YAML 構文エラーがあるとファイル全体が無効になり、`on:` セクションのトリガー定義も認識されなくなる
- GHA ワークフローでマルチライン文字列を扱う場合、YAML ブロックスカラーとシェルの HEREDOC の二重構造を意識する必要がある

---
**作成日**: 2026-03-15
**起票元**: gha-workflow-dispatch-fix 作業中の発見
