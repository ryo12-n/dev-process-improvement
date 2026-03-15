# sandbox 有効化 + settings.local.json 導入

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-071 |
| **優先度** | 🔴 高 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-15 |
| **起票元** | config-optimization/20260315 OPT-007 |

## 概要

sandbox を有効化しカーネルレベルのファイルシステム・ネットワーク制限を導入する。PreToolUse hook（BL-067）と合わせて二重防御を構成。settings.local.json を個人設定分離先として導入する。

## 期待効果

- deny ルール非機能の最確実な代替手段（カーネルレベル強制）
- Bash 経由のセンシティブファイルアクセスをOS レベルで防止
- settings.local.json で個人設定を分離

## 注意事項

- sandbox がビルドツールや外部コマンドの実行を制限する可能性
- 段階的導入（まず sandbox のみ、次に network 制限）を推奨
