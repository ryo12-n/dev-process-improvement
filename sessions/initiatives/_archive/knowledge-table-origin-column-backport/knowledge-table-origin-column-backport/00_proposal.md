# 改善施策提案: knowledge-table-origin-column-backport

## 背景・課題

triage プロセスの知見集約テーブルには「発見元 Set」列が存在し、各知見がどのワーカーセットから得られたかを追跡できる。

**前回施策（2026-03-16 完了・アーカイブ済み）** にて `04_work_report.md` および `06_eval_report.md` の知見テーブルに「発見元」列を追加した。しかしその際、以下のファイルは「別途検討」として明示的にスコープ外とした。

- `08_gate_review.md` の「横展開・次施策への引き継ぎ事項」内「必須把握事項」テーブル

現状、`08_gate_review.md` の「必須把握事項」テーブルは以下の構造であり「発見元」列が存在しない。

```
| # | 知見・注意事項 | 詳細 | ルーティング先 |
```

L1 が横展開テーブルに知見を集約する際に、各知見の発見者（ワーカーか評価者か）を記録できず、トレーサビリティが不完全な状態が継続している。

## 目標

`sessions/initiatives/_template/08_gate_review.md` の「必須把握事項」テーブルに「発見元」列を追加し、initiatives テンプレート全体で知見テーブルの構造を統一する。

## スコープ
### やること
- `sessions/initiatives/_template/08_gate_review.md` の「必須把握事項」テーブルに「発見元」列を追加
- docs/ 可視化文書（workflow.md 等）への影響確認

### やらないこと
- 既存の完了済み・アーカイブ済み施策の gate_review への遡及適用
- triage テンプレートの変更（発見元 Set 列は既に存在）
- `04_work_report.md`、`06_eval_report.md` の変更（前回施策で完了済み）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- `08_gate_review.md` の横展開テーブルでも知見の出自追跡が可能になる
- initiatives テンプレート全体（work_report / eval_report / gate_review）で「発見元」列の構造が統一される
- L1 がゲートレビュー時に各知見の発見者（Worker / Evaluator）を記録・参照できる

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| 既存の進行中施策の gate_review との不整合 | 低 | 遡及適用は行わず、新規施策から適用する |
| docs/ の可視化文書との整合性漏れ | 低 | タスクに整合性確認を含める |

## 壁打ちの背景

- BL-012 として起票済み。前回施策（`_archive/knowledge-table-origin-column-backport/`）の「別途検討」として残された課題の解消
- 前回施策の `00_proposal.md` に「`08_gate_review.md` の横展開テーブル構造の変更（別途検討）」と明記されている
- スコープは `_template/08_gate_review.md` の1ファイルに限定
- 「発見元」の値は initiatives 文脈ではタスク ID（T-001, T-E01 等）またはロール（L2-worker, L2-evaluator）を想定

## 備考・設計パターン

「発見元 Set」（triage）→「発見元」（initiatives）の対応関係:
- triage: 複数ワーカーセットが並列走査 → 発見元 Set = set-1, set-2 等
- initiatives: L2-worker（実施）と L2-evaluator（評価）が順次実施 → 発見元 = タスク ID（T-001, T-E01 等）またはロール

---
**起票者**: L1
**起票日**: 2026-03-18
**ステータス**: 起票 → 承認済 → 実施中 → 評価中 → 完了
**backlog元ファイル**: backlog/entries/知見集約テーブル発見元列のinitiatives逆移植.md
