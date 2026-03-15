# PreToolUse hook によるセンシティブファイルアクセスガード実装

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-067 |
| **優先度** | 🔴 高 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-15 |
| **起票元** | config-optimization/20260315 OPT-001 |

## 概要

deny ルール非機能（v1.0.93 既知バグ ISS-TEMP-001/003）の代替として PreToolUse hook を実装する。`.env*`, `secrets/**`, `*.pem`, `*.key` への Read/Edit/Write/Bash アクセスを exit code 2 でブロック。sandbox（BL-071）との二重防御を構成する。

## 期待効果

- deny ルール14件相当のセキュリティガードを復活
- sandbox と合わせてカーネルレベル + アプリレベルの深層防御を実現

## 注意事項

- Bash ツールの grep ベースパターンマッチングでは変数展開・パイプ等の間接参照を検出できない（ISS-TEMP-008）。sandbox との併用が必須
- 段階的導入（まず Read のみ、次に Edit/Write、最後に Bash）を推奨
