# ワーカータスク指示: Set-2

## 割り当て BM タスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| BM-003 | backlog/entries/ の背景・前提条件 | 各エントリの前提条件が現在の環境と整合しているか確認する。特に roles→agents 移行、manager-common-policy 整備、session-flow-policy 新設、hooks 機能の利用可能化等の環境変化による影響を重点チェック | 全エントリの前提条件が現状と照合され、変化のあるエントリが一覧化されている |
| BM-004 | backlog/entries/ の優先度 | 各エントリの優先度（高/中/低）が現状の課題状況・環境変化に照らして妥当か確認する。特に ISS-052（ルーティング未実行率22%）、ISS-054（rule-change-checklist走査対象不足）等の課題管理CSVの未対応課題との関連を考慮 | 全エントリの優先度妥当性がレビューされ、変更候補が一覧化されている |

## 走査時の注意事項

- BM-003: 以下の主要な環境変化を前提チェックの観点として使用すること
  - roles/ → .claude/agents/ への移行完了
  - manager-common-policy の整備（§1-§8）
  - session-flow-policy の新設
  - hooks 機能（SessionStart/PreToolUse/PostToolUse）の利用可能化
  - backlog-maintenance-session の新設
  - l1-impl-manager-session の新設
- BM-004: 優先度変更の提案には必ず変更理由を記載すること

---
**作成者**: バックログメンテナンスマネージャー
**作成日**: 2026-03-12
