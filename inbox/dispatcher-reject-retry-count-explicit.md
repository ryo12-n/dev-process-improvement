# dispatcher.yml reject ルートへの retry_count 明示追加

## 提案
initiative-dispatcher.yml の reject ルートに `-f retry_count="0"` を明示的に追加する。approve ルートには既に追加済みだが、reject ルートは `default: 0` に依存している。一貫性の向上が目的。

## 背景
gha-pipeline-autorun 施策の L2-evaluator が改善提案として指摘。機能的問題はなし。

---
**起票日**: 2026-03-19
