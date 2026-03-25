# 改善施策提案: sprint-template-design

## 背景・課題

現在の `dev-process-improvement` リポジトリでは、initiative セッションごとの作業は L1/L2 ロール分担で管理されているが、スプリント単位のライフサイクル（計画→実行→レビュー→知見蒸留）を統一したテンプレート構造で回す仕組みが存在しない。planner/generator/evaluator の3セッションが協調してスプリントを管理するための標準アーティファクトが必要。

## 目標

`templates/sprint_template/` 配下に5ファイルのテンプレートを作成し、planner・generator・evaluator の各セッションが明確な責任分離のもとでスプリントライフサイクルを回せる状態にする。

## スコープ
### やること
- `templates/sprint_template/` ディレクトリの作成
- `plan.md` / `todo.md` / `work_log.md` / `review.md` / `knowledge.md` の5ファイルを設計・作成
- 各ファイルの責任マトリクス（誰が作成・更新・読み取りするか）をコメントとして明記

### やらないこと
- 既存の `sessions/initiatives/_template/` の変更
- CLAUDE.md の L1/L2 定義の変更
- スプリント運用の自動化（GHA 連携等）
- スプリント実体の配置先フォルダ定義

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## プロジェクト紐づけ

| プロジェクト名 | パス |
|-------------|------|
| なし | - |

## 期待される効果

- planner・generator・evaluator がどのファイルをいつ・どのように更新すべきかが明確になる
- スプリントループ（計画→実行→レビュー→修正→再実行）が繰り返し回せる
- work_log の DEVIATION 通知によって計画と実態の乖離が早期に検出できる
- knowledge.md への蒸留と `refs/` へのエスカレーションで知見が資産として蓄積される

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| 既存の L1/L2 ロール定義と新ロール定義が混在して混乱する | 中 | テンプレートコメントに既存体系との対応を記載しない。独立した体系として明確に分離する |
| テンプレートが形骸化し実際に使われない | 低 | 最小限の構造に留め、使いやすさを優先する |

## 壁打ちの背景

設計計画書（inbox/sprint_template 設計計画書.txt）で壁打ち済みの意思決定を引き継ぐ。

**ロール責任分離の決定経緯:**
- planner / generator / evaluator の3ロールを設定
- generator は todo.md のステータス更新のみ可能。plan.md の変更権限は planner が専有
- evaluator は review.md を round 別セクションで追記。plan.md の成功条件を参照して採点
- knowledge.md は planner が work_log・review を読んで定期的に蒸留（evaluator ではなく planner が管理）
- planner/generator/evaluator は既存の L1/L2 体系とは独立したセッションとして扱う

**各ファイルのフォーマット決定経緯:**
- `todo.md`: テーブル形式。親タスク(T-XXX)は planner 管理・子タスク(T-XXX-Y)は generator 管理の2層構造
- `work_log.md`: タスク単位でセクション。DEVIATION は通常ログの流れに混在。小見出し4つ
- `review.md`: ラウンドをまたいで IMP 連番。総評はラウンドごと
- `knowledge.md`: スプリント固有の知見に絞る。完了後は `refs/` へエスカレーション

## 備考・設計パターン

- 本テンプレートは `templates/sprint_template/` に配置し、既存の `sessions/initiatives/_template/` とは独立した体系として管理する
- スプリント開始時は `templates/sprint_template/` をコピーして使用する（展開先は別途定義）
- 設計計画書に確定フォーマットが記載済みのため、ワーカーはこれをそのまま実体化する
- `knowledge.md` のエスカレーション先は `refs/<リポ名>/knowledge.md` を想定

---
**起票者**: L1
**起票日**: 2026-03-25
**ステータス**: 起票
**backlog元ファイル**: なし（壁打ちセッションから直接施策化）
