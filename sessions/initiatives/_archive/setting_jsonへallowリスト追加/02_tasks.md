# タスクリスト: setting.json へ allow リスト追加

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | allow ルールの設計 | よくある操作を網羅した allow リストが決定 | 🔴 | ✅ |
| T-002 | settings.json への allow ルール追加 | settings.json に allow セクションが追加され構文エラーなし | 🔴 | ✅ |
| T-003 | コミット・PR作成 | PR #6 が作成されていること | 🔴 | ✅ |

### 追加した allow ルール一覧

| カテゴリ | ルール |
|---------|--------|
| ファイル操作 | `Read(*)`, `Edit(*)`, `Write(*)`, `Glob(*)`, `Grep(*)` |
| Git | `Bash(git *)` |
| GitHub CLI | `Bash(gh pr *)`, `Bash(gh api *)`, `Bash(gh run *)` |
| シェル (読み取り系) | `Bash(ls *)`, `Bash(ls)`, `Bash(wc *)`, `Bash(cat *)`, `Bash(head *)`, `Bash(tail *)`, `Bash(find *)`, `Bash(echo *)` |
| シェル (変更系) | `Bash(cp *)`, `Bash(mkdir *)`, `Bash(mv *)` |

---
**作成者**: L1
**最終更新**: 2026-03-07
