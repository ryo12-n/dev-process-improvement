# 評価計画: impl-worktree-parallel

## 壁打ちフェーズ [2026-03-12 23:50]

### 理解のサマリー
- 評価の目的: L2-worker の全成果物（9ファイルの変更・作成）が 01_plan.md の成功基準8項目を満たしているか、ファイル間の整合性・3層検証チェックリストの完全性・フェールセーフの有効性を評価する
- 評価スコープ: impl-manager 配下のスキル・エージェント定義（SKILL.md, impl-worker.md, impl-evaluator.md）、テンプレート（07_issues_W_template.md, 36_file_task_division.md, 42_impl_work_report.md）、ドキュメント（docs/git-worktree-guideline.md, docs/workflow.md）、CLAUDE.md の修正
- 完了条件: 評価計画・評価レポート・課題起票が完了し、マネージャーへの推奨が明記されている

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全12タスク完了、知見セクション記載あり、メタルール横断検証結果あり）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（8項目が具体的に記載）
- [x] 評価に必要なツール・アクセス権限: 確認済み（全評価対象ファイルの読み取りが可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象

L2-worker が変更・作成した全9ファイル:
1. `.claude/skills/l1-impl-manager/SKILL.md` — 並列ディスパッチ機構の変更
2. `.claude/skills/l1-impl-manager/agents/impl-worker.md` — worktree 対応
3. `.claude/skills/l1-impl-manager/agents/impl-evaluator.md` — Phase 4 評価基準追加
4. `sessions/impl/_template/07_issues_W_template.md` — per-worker 課題バッファテンプレート
5. `sessions/impl/_template/36_file_task_division.md` — Worktree Configuration 追加
6. `sessions/impl/_template/42_impl_work_report.md` — Merge Results / Consolidated Issues 追加
7. `docs/git-worktree-guideline.md` — ステータス更新 + impl-manager セクション追加
8. `docs/workflow.md` — worktree 記述追加
9. `CLAUDE.md` — docs/ 分類テーブル修正

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-01 | impl-worker.md の worktree 対応完全性 | impl-worker.md の6項目（作業フロー・課題起票先・外部リポ手順・担当ファイル・チェックポイント・完了チェックリスト）を確認 | 全6項目が反映済み。`initiative/` 参照がゼロ |
| E-02 | SKILL.md の並列ディスパッチ機構完全性 | 事前準備・マージ手順・3層検証チェックリスト・ディスパッチパラメータ・B+C集約手順・コンフリクト解消を確認 | 全5項目が反映済み。事前・事後チェックリストに回復手順が明記 |
| E-03 | 07_issues_W_template.md の適切性 | テンプレートに Worker 情報・課題メモセクション・起票フォーマットが含まれるか確認 | ファイルが存在し、必要セクションが揃っている |
| E-04 | テンプレートの worktree セクション追加 | 36_file_task_division.md と 42_impl_work_report.md の追加セクションを確認 | 36 に Worktree Configuration + Per-Worker Mapping、42 に Merge Results + Consolidated Issues |
| E-05 | impl-evaluator.md Phase 4 評価基準 | Phase 4 評価基準に worktree 関連4項目が追加されているか確認 | per-worker マージ・マージ後テスト・範囲外変更・課題統合の4項目が存在 |
| E-06 | ブランチ参照の統一 | impl-manager 配下の全ファイルで `initiative/` → `impl/` の変更を grep で確認 | `initiative/` 参照がゼロ |
| E-07 | docs の整合性 | workflow.md と git-worktree-guideline.md が SKILL.md の実態と一致するか確認 | Phase 4 フロー・B+C集約・ブランチ参照が SKILL.md と整合 |
| E-08 | メタルール横断検証 | フロー記述・workflow.md 同期・TG-008 基準連動の3領域を検証 | 3領域すべて合格（または修正済み） |
| E-09 | ファイル間の整合性（重点） | SKILL.md とエージェント定義間のファイル名・パス・パラメータの相互参照を検証 | 相互参照が矛盾なく一致 |
| E-10 | 3層検証チェックリストの完全性（重点） | 事前・ワーカー・事後の各チェック項目が漏れなくカバーされ、回復手順が明記されているか | 全項目に検証コマンドと回復手順がある |
| E-11 | 知見セクションの記載 | 04_work_report.md の知見セクションに最低1行ずつ記載があるか | ルール化候補・参考情報の各テーブルに1行以上 |
| E-12 | 課題転記 | 07_issues.md の未転記課題がないか確認 | 全課題に「転記済」or「転記不要」が付いている |

## 評価スケジュール
- E-01〜E-06: 成功基準の直接検証（個別ファイル確認）
- E-07〜E-08: ドキュメント整合性検証
- E-09〜E-10: 重点評価（ファイル間整合性・チェックリスト完全性）
- E-11〜E-12: 付帯確認

## 前提・制約
- 評価は成果物ファイルの読み取りのみで実施（変更は行わない）
- TG-008 基準への変更必要性はワーカーの判断を検証する

---
**作成者**: L2（評価）
**作成日**: 2026-03-12
