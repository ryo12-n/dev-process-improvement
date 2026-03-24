# バックログエントリ削除時の CSV 再生成義務化ルール追加

## 気づき

`backlog/entries/*.md` を削除した場合、`scripts/generate-csvs.py` を実行しないと `backlog/backlog.csv` に削除済みエントリが残存する。現状はワーカーの判断で実行しているが、明文化されたルールがない。

## 提案

以下のいずれかの形でルール化する:
- `.claude/rules/` に backlog 操作時のチェックルールを追加
- 既存のバックログ関連スキルにステップとして追記

## 発見元

`batch-reference-fix-and-rename` 施策の T-003（バックログエントリ4件削除）で、L2-worker が手動で `generate-csvs.py` を実行して整合性を確保した。

---
**記録日**: 2026-03-24
**発見元施策**: batch-reference-fix-and-rename
