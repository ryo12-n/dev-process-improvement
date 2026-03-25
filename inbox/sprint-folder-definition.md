# スプリント実体の配置先フォルダ定義

## 背景
sprint-template-design 施策で `templates/sprint_template/` にテンプレートを作成したが、実際のスプリント運用時のコピー先フォルダは未定義。運用開始前に定義が必要。

## 提案
- `sessions/sprints/<sprint_name>/` のような配置先を定義する
- コピー手順（手動 / 自動）を決定する

## 発見元
sprint-template-design 施策 05_gate_review.md

---
**起票日**: 2026-03-25
