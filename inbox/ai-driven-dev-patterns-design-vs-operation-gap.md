# ai-driven-dev-patterns の設計構想と実運用の乖離調査

## 気づき

`dev-workflow-detail.md` §8（716-735行）には「L1 施策管理マネージャー → dev_manager → 各ロール」という3層アーキテクチャが記述されている。しかし ai-driven-dev-patterns の実運用モデルは `dev_manager` が最上位オーケストレーターとして自律稼働しており、外部 L1 からの指示チャネルは設計上存在しない。

この乖離は本施策（L1 参照精査）のスコープ外として「変更不要」と判断したが、§8 の記述が現在の実運用実態に対応しているかを検討する別施策が有益と考えられる。

## 提案

以下のいずれかを検討する施策として起票：

1. `dev-workflow-detail.md` §8 の記述を現在の運用実態に合わせて更新する
2. 設計構想と現状運用の乖離を明示するドキュメント（注記）を追加する
3. 両リポジトリの関係性を正確に記述した cross-repo アーキテクチャドキュメントを整備する

## 背景

- 施策: dev-workflow-detail-l1-ref-review（T-007 追加調査）
- ai-driven-dev-patterns の `.claude/` 調査で発見

---
**記録日**: 2026-03-15
**発生施策**: dev-workflow-detail-l1-ref-review
