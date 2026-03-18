# commit-message 規約で l2-plan-worker/evaluator の session-type を明確化

## 起票情報

| 項目 | 内容 |
|------|------|
| 起票元 | session-consistency チェック 2026-03-17（IMP-004, SC-007） |
| 起票日 | 2026-03-17 |

## 内容

commit-message.md の施策作業テーブルに L2-worker/L2-evaluator は登録されているが、l2-plan-worker/l2-plan-evaluator の扱いが明示されていない。

推奨対応: L2-worker の用途欄に「（l2-plan-worker を含む）」、L2-evaluator の用途欄に「（l2-plan-evaluator を含む）」と追記する。独立した session-type にする必然性は低い。

## 判断ポイント

- 包含関係の追記（1ファイル2箇所のテキスト修正）で十分か
- 独立した session-type として登録する必要があるか
