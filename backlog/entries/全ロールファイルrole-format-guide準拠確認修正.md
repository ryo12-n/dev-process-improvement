# 全ロールファイル role-format-guide 準拠確認・修正

## メタ情報

| 項目 | 内容 |
|------|------|
| **優先度** | 🔵 低 |
| **ステータス** | 候補 |
| **対象リポジトリ** | ai-driven-dev-patterns |
| **起票日** | 2026-03-04 |

## 課題・背景

「role-format-guide 準拠確認チェックリスト」施策で reviewer.md のセクション順序不適合を検出した（「成功条件」が「やること」の前に配置されている）。他のロールファイルにも同様の不適合がある可能性がある。

## 期待効果

- 全エージェント定義ファイル（`.claude/agents/` 配下）の role-format-guide 準拠度を統一する
- チェックリストを活用した体系的な品質確認

## 補足・参考情報

- 元施策: role-format-guide 準拠確認チェックリスト 08_gate_review.md 次施策候補
- チェックリスト: `.claude/rules/role-format-guide.md` の「付録: 準拠確認チェックリスト」を使用
- **前提変化（2026-03-12 BM-003 検出）**: roles/ → .claude/agents/ 移行完了。対象パスを `roles/*.md` から `.claude/agents/` 配下に変更
