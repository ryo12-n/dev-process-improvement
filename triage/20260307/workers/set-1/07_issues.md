# 課題メモ（ワーカーセット別バッファ）: Set-1

> **このファイルの役割**: ワーカーセット内で発見された課題・知見・リスクの一時メモ置き場。
> マネージャーが `03_report.md` 作成時に全ワーカーセットの課題を集約し、`プロセス改善_課題管理.csv` へ転記する。

## 転記ルール

- ワーカー・評価者は課題をこのファイルに起票する（CSV 直接起票はしない）
- マネージャーが集約時に CSV 転記の要否を判断する
- 施策スコープ外・他のセッションでも再発しうる課題 → **マネージャーが CSV に転記**
- 当セッション内だけで完結する軽微な修正メモ → 転記不要（クローズ扱い）
- 転記済みの項目には `[転記済 ISS-XXX]` を末尾に追記する

---

## 未転記メモ

### [2026-03-07] workflow.md のトリアージ課題起票フロー乖離
- **種別**: 改善提案
- **発見者**: ワーカー
- **内容**: workflow.md の「課題起票の考え方」セクション（126行目付近）に「トリアージは CSVに直接起票します」と記載されているが、実装（triage-worker.md, triage-evaluator.md, triage-manager.md）では 07_issues.md 経由でマネージャーが集約・CSV転記する設計に変更済み。workflow.md の記述が古い設計のまま残存
- **対応方針（案）**: workflow.md の該当セクションを 07_issues.md 経由フローに書き換える。maintenance コミットで即時対応可能
- **関連タスク**: TG-007
- **対応**: セッション内修正済み（workflow.md + triage-standard-policy SKILL.md を同時修正）

### [2026-03-07] triage-standard-policy SKILL.md の壁打ち記録先テーブル不整合
- **種別**: 改善提案
- **発見者**: ワーカー
- **内容**: triage-standard-policy SKILL.md セクション1.3「記録先ファイルの対応」テーブルで、トリアージ系の壁打ち記録先が「02_work_log.md」と記載されているが、triage-worker.md の実装では「02_scan_plan.md」に記録する設計。基準文書と実装の不整合
- **対応方針（案）**: triage-standard-policy SKILL.md のテーブルを「02_scan_plan.md / 05_eval_plan.md」に修正。軽微修正でセッション内対応可能
- **関連タスク**: TG-008
- **対応**: セッション内修正済み（triage-standard-policy SKILL.md 記録先テーブルを修正）

### [2026-03-07] triage-standard-policy SKILL.md の課題起票欄「CSV（直接起票）」が実装と乖離
- **種別**: 改善提案
- **発見者**: 評価者
- **内容**: triage-standard-policy SKILL.md セクション1.3「記録先ファイルの対応」テーブルの課題起票行（59行目）で、トリアージ系の課題起票先が「CSV（直接起票）」と記載されている。しかし、triage-worker.md および triage-evaluator.md の実装では 07_issues.md に起票し、マネージャーが集約・CSV転記する設計に変更済み。ワーカーが起票済みの「workflow.md のトリアージ課題起票フロー乖離」と同根の問題であり、修正時は workflow.md と triage-standard-policy SKILL.md の両方を同時に更新すべき
- **対応方針（案）**: triage-standard-policy SKILL.md 59行目の「CSV（直接起票）」を「07_issues.md（中間バッファ）-> マネージャーが CSV 転記」に修正。ワーカー起票の workflow.md 修正と同時に maintenance コミットで対応可能
- **関連タスク**: TG-007, TG-008（評価時の追加発見）
- **対応**: セッション内修正済み（triage-standard-policy SKILL.md + workflow.md を同時修正）
