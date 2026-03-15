# 計画: backlog-id-and-issue-template

## フェーズ1: 実施

### タスク一覧

1. backlog.csv に ID 列を先頭に追加し、既存行に BL-001〜BL-053 を採番
2. backlog/_template.md のメタ情報にバックログ ID 行を追加
3. backlog/entries/*.md のメタ情報に BL-xxx ID を追記（CSV の行順に対応）
4. .github/workflows/backlog-to-issue.yml の入力を BL-xxx ID に変更
5. backlog/README.md の CSV 列構成説明を更新

### 完了条件

- backlog.csv の全行に一意の BL-xxx ID が付与されている
- _template.md に ID フィールドが存在する
- entries/*.md のメタ情報に ID が記載されている
- backlog-to-issue.yml が BL-xxx ID を受け付ける
- README.md が更新済み

---
**作成日**: 2026-03-14
