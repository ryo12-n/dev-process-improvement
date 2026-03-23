# GHA コメント投稿の `--body-file` パターン推奨ルール追加

## 種別
ルール改善

## 内容
`.claude/rules/gha-workflow-security.md` のチェックリストに「HEREDOC 内のフェンスドコードブロックは `--body-file` パターンを推奨」を追加する。

フェンスドコードブロックに限らず、変数展開リスク回避の観点から全コメント投稿に `--body-file` を推奨するルールとする。

## パターン
```yaml
# 推奨パターン
- name: Post comment
  run: |
    cat > /tmp/comment.md << 'COMMENT_EOF'
    コメント本文（フェンスドコードブロック含む）
    COMMENT_EOF
    gh issue comment "$ISSUE_NUMBER" --body-file /tmp/comment.md

# 非推奨パターン
- name: Post comment
  run: |
    gh issue comment "$ISSUE_NUMBER" --body "..."
```

## 背景
gha-workflow-ux-improvements 施策（T-002）で発見。`gh issue comment --body "..."` の shell 文字列内にバッククォート3連を含めると shell 解釈と衝突するリスクがある。

## 発見元
sessions/initiatives/gha-workflow-ux-improvements/ (L2-worker / L2-evaluator)

---
**作成日**: 2026-03-19
