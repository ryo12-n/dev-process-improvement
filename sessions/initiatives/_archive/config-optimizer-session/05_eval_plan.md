# 評価計画: config-optimizer-session

## 壁打ちフェーズ [2026-03-14]

### 理解のサマリー
- 評価の目的: config-optimizer-manager セッション（SKILL.md、4エージェント定義、セッションテンプレート、リファレンス初期ファイル、既存ファイル連動更新）の全12タスク成果物が、01_plan.md の成功基準6項目を満たしているかを検証する
- 評価スコープ: Phase 1（T-001〜T-007: スキル・エージェント・テンプレート作成）+ Phase 2（T-008〜T-012: 既存ファイル連動更新）の全成果物。加えて `.claude/skills/`, `.claude/rules/` 配下の変更があるためメタルール横断検証チェックリストも実施する
- 完了条件: 成功基準6項目の達成度判定 + メタルール横断検証 + 「評価中の知見」両テーブルに最低1行の記載

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全12タスクの実績・成果物一覧・知見が記載済み）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（6項目すべて具体的な判定基準を持つ）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read, Grep, Glob で全成果物にアクセス可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象

1. `.claude/skills/config-optimizer-manager/SKILL.md` — マネージャーセッション定義
2. `.claude/skills/config-optimizer-manager/agents/config-collection-worker.md` — Phase 1 ワーカー
3. `.claude/skills/config-optimizer-manager/agents/config-analysis-worker.md` — Phase 2 ワーカー
4. `.claude/skills/config-optimizer-manager/agents/config-proposal-worker.md` — Phase 3 ワーカー
5. `.claude/skills/config-optimizer-manager/agents/config-optimizer-evaluator.md` — 全フェーズ共通評価者
6. `.claude/skills/config-optimizer-manager/reference/claude-code-config-reference.md` — リファレンススケルトン
7. `sessions/config-optimization/_template/` — セッションテンプレート
8. `.claude/rules/commit-message.md` — co-mgr/co-worker/co-eval 追加
9. `.claude/skills/manager-common-policy/SKILL.md` — 適用対象テーブル追加
10. `.claude/skills/session-flow-policy/SKILL.md` — §5 セッションタイプテーブル追加
11. `.claude/skills/triage-standard-policy/SKILL.md` — ペアリング構造・走査対象追加
12. `docs/workflow.md` — config最適化セッションフロー記述追加

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | session-flow-policy §5.1 チェックリスト全項目 | §5.1 の6項目を1つずつ照合 | 6項目すべて充足 |
| 2 | SKILL.md 必須セクション | SKILL.md の見出し構造を §2.2 と照合 | 「あなたの役割」「作業フロー」「やること」「やらないこと」の4セクションが存在 |
| 3 | agents/ 構成（worker × 3 + evaluator × 1） | ファイル一覧と各定義の §3.1 必須セクション照合 | 4ファイルが存在し、各ファイルに §3.1 の6セクションが含まれる |
| 4 | ペアリング対称性要件 | evaluator 定義内の対称性テーブルを §3.2 と照合 | 6要素（壁打ち・計画・レポート・知見・課題・停止ルール）が worker 3種 + evaluator すべてで「あり」 |
| 5 | コミットメッセージ規約更新 | commit-message.md に co-mgr/co-worker/co-eval の行が存在するか | 3行が追加済み |
| 6 | workflow.md 新フロー記述 | docs/workflow.md に config最適化セッションフローが追加されているか | 3フェーズ構成・CO ターゲット・ワーカー/評価者のディスパッチが記述されている |
| M-1 | メタルール: フロー記述の整合性 | 変更ファイルを参照するスキル・エージェント定義のフロー記述が実態と一致するか | 不整合なし |
| M-2 | メタルール: workflow.md の同期 | docs/workflow.md が変更後のルール・スキル定義と整合するか | 不整合なし |
| M-3 | メタルール: TG-008 基準の連動性 | triage-standard-policy のチェック基準が変更内容を反映しているか | 走査対象・ペアリング構造に追加済み |

## 評価スケジュール
- 成功基準6項目の評価を実施
- メタルール横断検証チェックリスト3項目を実施
- 07_issues.md の実施ワーカー未転記確認

## 前提・制約
- L1 が直接作成した成果物のため、L2-worker の作業は「存在確認・レビュー」に特化している
- リファレンスファイルはスケルトン状態（意図通り）

---
**作成者**: L2（評価）
**作成日**: 2026-03-14
