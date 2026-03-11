# 実施計画: Invalid settings への対応

## 対象ファイル

- `.claude/settings.json`

## 修正内容

### 1. `$schema` URL の修正

| Before | After |
|--------|-------|
| `https://cdn.jsdelivr.net/npm/@anthropic-ai/claude-code@latest/config-schema.json` | `https://json.schemastore.org/claude-code-settings.json` |

### 2. Read/Write ルールの構文修正

`file_path:*pattern*` → glob パターン形式

| Before | After |
|--------|-------|
| `Read(file_path:*.env*)` | `Read(./.env*)` |
| `Read(file_path:*secrets/*)` | `Read(./secrets/**)` |
| `Read(file_path:*.pem)` | `Read(**/*.pem)` |
| `Read(file_path:*.key)` | `Read(**/*.key)` |
| `Write(file_path:*.env*)` | `Write(./.env*)` |
| `Write(file_path:*secrets/*)` | `Write(./secrets/**)` |

### 3. Bash ルールの構文修正

`command:*pattern*` → プレフィックスマッチ形式（末尾 `*` のみ）

| Before | After |
|--------|-------|
| `Bash(command:*rm -rf*)` | `Bash(rm -rf *)` |
| `Bash(command:*>.env*)` | （削除: リダイレクト構文はプレフィックスマッチ不可） |
| `Bash(command:*cat .env*)` | `Bash(cat .env*)` |
| `Bash(command:*cat secrets/*)` | `Bash(cat secrets/*)` |

## 検証方法

- Claude Code 再起動後 `/doctor` で「Invalid Settings」が表示されないことを確認

---
**作成日**: 2026-03-07
