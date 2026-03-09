# disallowedTools フィールド活用検討

## メタ情報

| 項目 | 内容 |
|------|------|
| **優先度** | 🔵 低 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-09 |

## 課題・背景

`tools` フィールドでは deferred tools（WebSearch, WebFetch, NotebookEdit 等）を制限できない（ISS-047）。`disallowedTools` フィールドによる明示的なツール禁止を検討し、L2-worker/L2-evaluator のエージェント定義に適用する可能性を調査する。

## 期待効果

- エージェントのツール使用範囲を意図通りに制限
- SDK 環境でのセキュリティ向上

## 実施案

- `disallowedTools` フィールドの仕様調査
- L2-worker/L2-evaluator への適用テスト
- docs/subagent-permission-guide.md の更新
