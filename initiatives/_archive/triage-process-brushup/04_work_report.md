# 作業レポート: triage-process-brushup

## サマリ

ai-driven-dev-patterns のトリアージプロセスを dev-process-improvement 側と同等の品質・網羅性にブラッシュアップした。フェーズ1〜3 の全16タスク（T-001〜T-016）を完了し、テンプレートファイル構造の整備（リナンバリング+新規3ファイル+既存2ファイル更新）、マネージャーテンプレートの拡充（TG-008/TG-009追加、知見集約・課題集約セクション追加、ゲート判定テンプレート新設）、スキル定義3ファイルの全面更新、backlog起票を実施した。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | ワーカーテンプレートのリナンバリング | git mv で3ファイルリネーム | git mv で3ファイルリネーム完了 | 差異なし |
| T-002 | 02_scan_plan.md 新規作成 | dev-process-improvement 参照で作成 | 作成完了 | 差異なし |
| T-003 | 05_eval_plan.md 新規作成 | dev-process-improvement 参照で作成 | 作成完了 | 差異なし |
| T-004 | 07_issues.md 新規作成 | dev-process-improvement 参照で作成 | 作成完了。用語適応済み |差異なし |
| T-005 | 04_scan_report.md 知見セクション追加 | テーブル2つ追加 | テーブル2つ追加+課題起票フロー変更 | 課題起票フローの変更も同時実施 |
| T-006 | 06_eval_report.md 知見セクション追加 | テーブル2つ追加 | テーブル2つ追加 | 差異なし |
| T-007 | 00_pre_investigation.md 拡充 | 気づき確認+ルール整合性詳細化 | 2セクション追加 | 差異なし |
| T-008 | 01_plan.md 拡充 | TG-008/TG-009 追加 | 走査タスク一覧+スコープチェックリスト追加 | 差異なし |
| T-009 | 03_report.md 拡充 | 知見集約・課題集約・TG結果追加 | 全セクション追加+課題フロー変更 | 差異なし |
| T-010 | 04_gate_review.md 新規作成 | dev-process-improvement 参照で作成 | 作成完了 | 差異なし |
| T-011 | triage-worker.md 更新 | 全7項目の更新 | 全面更新（関連ファイル一覧含む） | 差異なし |
| T-012 | triage-evaluator.md 更新 | 全7項目の更新 | 全面更新（関連ファイル一覧含む） | 差異なし |
| T-013 | triage-manager.md 更新 | 全8項目の更新 | 全面更新（関連ファイル一覧含む） | 差異なし |
| T-014 | backlog起票 | backlog ファイル作成 | 作成完了 | 差異なし |
| T-015 | 知見記録 | work_report に知見記載 | 本セクションに記載 | 差異なし |
| T-016 | 課題CSV転記 | 07_issues.md 確認・転記 | 転記対象課題なし | 差異なし |

## 成果物一覧

### ai-driven-dev-patterns リポジトリ（ブランチ: initiative/triage-process-brushup）
- `triage/_template/workers/_template/02_scan_plan.md`（新規）
- `triage/_template/workers/_template/03_work_log.md`（リネーム: 旧 02_work_log.md）
- `triage/_template/workers/_template/04_scan_report.md`（リネーム+更新: 旧 03_scan_report.md）
- `triage/_template/workers/_template/05_eval_plan.md`（新規）
- `triage/_template/workers/_template/06_eval_report.md`（リネーム+更新: 旧 04_eval_report.md）
- `triage/_template/workers/_template/07_issues.md`（新規）
- `triage/_template/00_pre_investigation.md`（更新）
- `triage/_template/01_plan.md`（更新）
- `triage/_template/03_report.md`（更新）
- `triage/_template/04_gate_review.md`（新規）
- `.claude/skills/triage/triage-worker.md`（全面更新）
- `.claude/skills/triage/triage-evaluator.md`（全面更新）
- `.claude/skills/triage/triage-manager.md`（全面更新）

### dev-process-improvement リポジトリ
- `backlog/ai-driven-dev-patterns-triage-standard-policy作成.md`（新規: T-014）

## 発生した課題
なし（07_issues.md に起票された課題なし）

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | リナンバリング時は全参照箇所の一括更新が必須 | テンプレート+スキル定義 | ファイル番号変更はスキル定義3ファイル全てのファイル参照に波及する。grep で旧番号の残存チェックを実施し、漏れがないことを確認する工程を標準化すべき |
| 2 | 課題起票フロー変更は「やること」「やらないこと」の両方で更新が必要 | スキル定義 | CSV直接起票→07_issues.md経由への変更時、「やること」に新フローを追加するだけでなく「やらないこと」に旧フローの禁止を明記する必要がある。片方だけの更新は矛盾を生む |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | 2リポジトリ間のテンプレート同期は参照元の構造をそのまま移植するのではなく用語適応が必要 | ai-driven-dev-patterns では initiatives→sessions、プロセス改善_課題管理.csv→課題管理.csv、L1/L2→triage-manager/worker/evaluator の用語変換が必要だった。将来的にリポジトリ間のテンプレート同期を自動化する場合は、用語マッピングテーブルの管理が重要になる |

## 所感・次フェーズへの申し送り
- 全タスクが計画通りに完了した
- 検証（grep による旧番号残存チェック、CSV直接起票残存チェック）で問題なしを確認済み
- T-014 で起票した backlog（triage-standard-policy 作成）は、TG-008 の運用実績を見てから着手するのが望ましい

---
**作成者**: L2（実施）
**作成日**: 2026-03-07
