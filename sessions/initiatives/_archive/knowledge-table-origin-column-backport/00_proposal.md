# 改善施策提案: knowledge-table-origin-column-backport

## 背景・課題

triage プロセスの知見集約テーブル（`sessions/triage/_template/03_report.md`）には「発見元 Set」列が存在し、各知見がどのワーカーセットから得られたかを追跡できる。
しかし initiatives テンプレートの知見テーブル（`04_work_report.md` および `06_eval_report.md`）にはこの列が存在しない。

その結果、L1 が `08_gate_review.md` の横展開テーブルに知見を集約する際に、各知見の発見元タスクを遡れず、知見の信頼性評価やトレーサビリティが不十分になっている。

## 目標

initiatives テンプレートの知見テーブルに「発見元」列を追加し、triage との一貫性を確保する。

## スコープ
### やること
- `sessions/initiatives/_template/04_work_report.md` の知見テーブルに「発見元」列を追加
- `sessions/initiatives/_template/06_eval_report.md` の知見テーブルに「発見元」列を追加
- 上記変更の整合性確認（docs/ への影響チェック）

### やらないこと
- 既存の進行中・完了済み施策の work_report / eval_report への遡及適用
- `08_gate_review.md` の横展開テーブル構造の変更（別途検討）
- triage テンプレートの変更（発見元 Set 列は既に存在）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- 知見の出自追跡が可能になり、L1 がゲートレビュー時に根拠を参照できる
- triage と initiatives 間で知見テーブルの構造が一致し、運用の一貫性が向上
- 知見の信頼性評価・レビュー判断の質が向上する

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| 既存の進行中施策のテンプレートとの不整合 | 低 | 遡及適用は行わず、新規施策から適用する |
| docs/ の可視化文書との整合性漏れ | 低 | タスクに整合性確認を含める |

## 壁打ちの背景

- BL-012 として起票済み。inbox 原文からの施策化
- triage の「発見元 Set」列を initiatives に逆移植する単純なテンプレート変更
- スコープは `_template/` の2ファイルに限定し、影響範囲を最小化する
- 「発見元」の値は initiatives 文脈ではタスク ID（T-001 等）を想定

## 備考・設計パターン

「発見元 Set」（triage）→「発見元」（initiatives）の対応関係:
- triage: 複数ワーカーセットが並列走査 → 発見元 Set = set-1, set-2 等
- initiatives: L2-worker（実施）と L2-evaluator（評価）が順次実施 → 発見元 = タスク ID（T-001, T-E01 等）

---
**起票者**: L1
**起票日**: 2026-03-16
**ステータス**: 起票 → 承認済 → 実施中 → 評価中 → 完了
**backlog元ファイル**: backlog/entries/知見集約テーブル発見元列のinitiatives逆移植.md
