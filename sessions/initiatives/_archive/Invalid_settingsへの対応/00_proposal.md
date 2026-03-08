# 改善施策提案: Invalid settings への対応

## 背景・課題

`.claude/settings.json` に構文エラーがあり、ファイル全体がスキップされていた。
これにより deny ルール（危険コマンド・機密ファイルアクセスの拒否）が一切機能していないセキュリティ上の問題が発生していた。

### エラー内容

1. **`$schema` の URL が不正**: `cdn.jsdelivr.net` の非公式 URL を使用していた
2. **Read/Write ルールの構文エラー**: `file_path:*pattern*`（Bash 専用の `:*` 構文）を Read/Write に使用していた
3. **Bash ルールの構文エラー**: `command:*pattern*` で `*` を中間に使用していた（プレフィックスマッチは末尾 `*` のみ有効）

## 目標

- settings.json のエラーを解消し、deny ルールを正常に機能させる

## スコープ

### やること
- `$schema` URL の修正
- Read/Write deny ルールを glob パターン形式に修正
- Bash deny ルールをプレフィックスマッチ形式に修正

### やらないこと
- deny ルールの追加・拡張（既存ルールの修正のみ）

## 備考

Claude Code `/doctor` コマンドで「Invalid Settings」セクションの有無により検証した。

---
**起票者**: L1
**起票日**: 2026-03-07
**ステータス**: 完了
