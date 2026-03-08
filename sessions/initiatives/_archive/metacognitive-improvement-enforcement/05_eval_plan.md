# 評価計画: メタ認知による改善の強制

## 壁打ちフェーズ [2026-03-08]

### 理解のサマリー
- 評価の目的: L2-worker が作成したメタ認知セッションタイプの全成果物（スキル定義・エージェント定義・テンプレート・連動更新）が session-flow-policy / triage-standard-policy の基準を満たしているかを評価する
- 評価スコープ: 新規作成ファイル（SKILL.md, agents/2ファイル, テンプレート12ファイル）+ 更新ファイル（commit-message.md, workflow.md, CLAUDE.md, session-flow-policy, triage-standard-policy）
- 完了条件: 06_eval_report.md に全チェック項目の評価結果が記載され、知見セクションに最低1行の記載があり、07_issues.md の課題が転記済みまたは転記不要の判断済み

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（T-001〜T-008 全て完了済み）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（session-flow-policy セクション5.1 / triage-standard-policy セクション1.2, 2.3 の基準が明確）
- [x] 評価に必要なツール・アクセス権限: 確認済み（全ファイルを読み取り済み）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象

1. `.claude/skills/metacognition-manager/SKILL.md` — マネージャースキル定義
2. `.claude/skills/metacognition-manager/agents/metacognition-worker.md` — ワーカーエージェント定義
3. `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md` — 評価者エージェント定義
4. `sessions/metacognition/_template/` — マネージャー用5ファイル + ワーカー用7ファイル
5. `.claude/rules/commit-message.md` — meta-mgr/meta-worker/meta-eval 追加
6. `docs/workflow.md` — メタ認知セッションフローセクション追加
7. `CLAUDE.md` — ディレクトリ構成テーブルに metacognition/ 追加
8. `.claude/skills/session-flow-policy/SKILL.md` — セクション5テーブルに追加
9. `.claude/skills/triage-standard-policy/SKILL.md` — 適用マトリクス等に追加

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | session-flow-policy セクション5.1 チェックリスト | SKILL.md + agents/ の内容を5.1の6項目と突合 | 6項目全てにチェックが付く |
| 2 | triage-standard-policy ペアリング対称性（セクション2.3） | worker / evaluator の定義を6要素で突合 | 6要素全てが両者に存在する |
| 3 | triage-standard-policy ライフサイクル完備（セクション1.2） | 適用マトリクスの「必須」ステージがロール定義に含まれるか確認 | 全「必須」ステージが定義に含まれている |
| 4 | テンプレート構造の triage との対称性 | metacognition/_template/ と triage/_template/ のファイル構成を比較 | ファイル数・構造が一致する |
| 5 | 連動更新の整合性 | CLAUDE.md / session-flow-policy / triage-standard-policy / commit-message.md / workflow.md の記載を相互突合 | 全ファイルでメタ認知セッションタイプが認識されている |
| 6 | SKILL.md 必須セクション | session-flow-policy セクション2のチェック | あなたの役割・作業フロー・やること・やらないこと・担当ファイルが含まれている |
| 7 | エージェント定義必須セクション | session-flow-policy セクション3のチェック | あなたの役割・作業フロー・やること・やらないこと・担当ファイル・停止ルールが含まれている |

## 評価スケジュール
- 壁打ち → 評価計画 → 全項目評価 → レポート作成 → 課題起票（必要時）

## 前提・制約
- triage セッションの既存定義をリファレンスとして参照する
- 評価基準は session-flow-policy / triage-standard-policy に定義された基準を使用する

---
**作成者**: L2（評価）
**作成日**: 2026-03-08
