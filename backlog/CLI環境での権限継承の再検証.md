# CLI環境での権限継承の再検証

## メタ情報

| 項目 | 内容 |
|------|------|
| **優先度** | 🔵 低 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-08 |

## 課題・背景

`subagent-permission-model` 施策で Agent SDK 環境での allow/deny リスト・tools フィールドの動作検証を実施したが、CLI 環境（対話型）での検証は未実施。SDK 環境では deny リストや tools 制限が機能しないことが判明したが（ISS-045, ISS-046）、CLI 環境での挙動は未確認。

## 期待効果

- SDK/CLI 環境差の正確な理解と運用ガイドの精緻化
- deny リスト・tools フィールドの適用範囲の明確化

## 補足・参考情報

- 発見元: `inbox/CLI環境での権限継承の再検証.md`
- 関連課題: ISS-045, ISS-046
- 関連施策: `_archive/subagent-permission-model/`
