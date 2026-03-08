# 評価計画: ai-driven-dev-patterns の設計プロセス整備

## 壁打ちフェーズ [2026-03-08 00:00]

### 理解のサマリー
- 評価の目的: 01_plan.md の成功基準3項目に対し、L2-worker の成果物が基準を満たしているか客観的に評価する
- 評価スコープ: ai-driven-dev-patterns 側の成果物8ファイル + dev-process-improvement 側の作業レポート・課題メモ
- 完了条件: 06_eval_report.md に評価結果・知見・課題が記載されていること

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能
- [x] 評価に必要なツール・アクセス権限: 確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象

### ai-driven-dev-patterns 側（ブランチ: initiative/design-process-setup）
1. `docs/design-process-guide.md` — 設計プロセス全体像マップ
2. `CLAUDE.md` — 知見ルーティングセクション追加
3. `inbox/README.md` — 人間のアイデア保管場所として明確化
4. `backlog/README.md` — 起票元・ライフサイクル図・優先順位判断基準追加
5. `backlog/ルールファイル実体作成.md` — 施策候補
6. `backlog/openspecライフサイクル統合.md` — 施策候補
7. `backlog/セッション記録の整理と活用基盤.md` — 施策候補
8. `backlog/テスト実行基盤の整備.md` — 施策候補

### dev-process-improvement 側
9. `initiatives/design-process-setup/04_work_report.md` — 作業レポート
10. `initiatives/design-process-setup/07_issues.md` — 課題メモ

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| SC-1 | 設計プロセス全体像マップの存在と品質 | `docs/design-process-guide.md` を読み、全体フローの網羅性・Mermaid 図の正確性・ナビゲーション文書としての有用性を確認 | docs/ にファイルが存在し、エントリーポイント→セッション→成果物→知見ルーティングの全体フローが Mermaid 図で可視化されている |
| SC-2 | 気づきルーティングの仕組み実装 | inbox/README.md、backlog/README.md、CLAUDE.md の変更内容を読み、ルーティングフローが明確に定義されているか確認 | inbox/backlog の README が更新され、CLAUDE.md に知見ルーティングセクションが追加されている。起票者別のルーティング先が明示されている |
| SC-3 | backlog 施策候補の件数と品質 | backlog/ 配下のファイルを読み、_template.md のフォーマットに従っているか、課題・背景・期待効果が記載されているか確認 | 3 件以上の施策候補ファイルが存在し、各ファイルに課題・背景・期待効果が記載されている |
| SC-4 | 知見記録の品質 | 04_work_report.md の「作業中の知見」セクションを確認 | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある |
| SC-5 | 課題転記の完了 | 07_issues.md の全課題に転記判断が付いているか確認 | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている |

## 評価スケジュール
- SC-1 → SC-2 → SC-3 → SC-4 → SC-5 の順に評価

## 前提・制約
- ai-driven-dev-patterns 側は `initiative/design-process-setup` ブランチで作業されており、main にはまだマージされていない
- 評価対象の成果物は全て読み取り可能な状態

---
**作成者**: L2（評価）
**作成日**: 2026-03-08
