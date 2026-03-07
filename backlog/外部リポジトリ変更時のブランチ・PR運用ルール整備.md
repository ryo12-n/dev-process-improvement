# 外部リポジトリ変更時のブランチ・PR運用ルール整備

## メタ情報

| 項目 | 内容 |
|------|------|
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-07 |

## 課題・背景

ai-research-notebook-setup 施策において、外部リポジトリ（ai-research-notebook）への変更を main ブランチに直接コミットし、push も漏れるという問題が発生した。dev-process-improvement 側ではブランチ作成・PR運用が確立されているが、外部リポジトリへの変更時にはそのルールが適用されていなかった。

現状のルール（L1-manager スキル、L2-worker エージェント定義）は dev-process-improvement リポジトリ内の作業を前提としており、外部リポジトリへの変更手順が定義されていない。

## 期待効果

- 外部リポジトリへの変更もブランチ・PRベースで管理され、レビュー可能になる
- push 漏れが防止される
- 変更の追跡性が向上する

## 補足・参考情報

- 発生施策: `initiatives/_archive/ai-research-notebook-setup/`
- 影響範囲: L1-manager スキル、L2-worker エージェント定義、場合によっては commit-message ルール
- 今回の知見: inbox/別リポジトリ成果物の記法スタイル事前確認.md も関連
