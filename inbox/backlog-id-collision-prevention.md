# backlog ID 採番の衝突防止

## 気づき

csv-conflict-prevention 施策の main マージ時に、BL-076 と BL-077 が異なる施策に二重採番されていることが判明した。

| ID | ブランチ A | ブランチ B |
|-----|-----------|-----------|
| BL-076 | ai-driven-dev-patterns の設計構想と実運用の乖離調査 | ai-driven-dev-patterns テストインフラ整備 |
| BL-077 | backlog エントリ旧フォーマット統一 | ai-driven-dev-patterns documentarian 参照切れルール修正 |

## 原因

別々のセッション（ブランチ）が同時期に backlog エントリを起票した際、既存の最大 ID を基に採番するため、同じ ID が振られてしまった。CSV の自動生成（generate-csvs.py）はファイルからの集約であり、ID の一意性は保証しない。

## 検討すべきこと

- ID 採番の排他制御（ロックファイル、main の最新 ID を fetch して採番、等）
- 重複検知の仕組み（generate-csvs.py での警告出力、CI チェック等）
- 並列セッション環境（SDK）での発生頻度が高い可能性

## 発見元

csv-conflict-prevention 施策の origin/main マージ時（2026-03-16）
