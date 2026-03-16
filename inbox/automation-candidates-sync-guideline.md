# automation-candidates 運用ガイドライン整備

## 種別
改善提案

## 背景
2026-03-16 の初回自動化メンテナンスで、automation-candidates のステータスと backlog のステータスが乖離していることが判明。AC-002 は BL-029 として backlog に起票済みだが、候補管理では「候補」のままだった（AC-012 も同様）。

## 提案内容
backlog に自動化候補を起票した際、automation-candidates の CSV/エントリを連動更新するプロセスを明文化する。具体的には:
- backlog 起票時に automation-candidates のステータスを「backlog起票済」に更新
- 関連backlog 列に BL-XXX を記入
- 最終評価日を更新

## 発見元
sessions/automation/20260316/（初回自動化メンテナンス）
