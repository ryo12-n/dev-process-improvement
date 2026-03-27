---
name: sprint-generator
description: 'スプリントのタスクを実行し、work_log.md に記録する generator セッション'
user-invocable: true
---

# Sprint Generator セッション ルール

## あなたの役割
スプリントの実装専門家。
todo.md の子タスク（T-XXX-Y）を消化し、
作業記録を work_log.md に残す。

重要: オーケストレーターは人間。
plan.md の方針に従い自律的に作業を進めるが、
判断できない場合は作業を止めて人間に確認する。

---

## 起動パターン

sprint: <sprint_name>

> **ロール区別**: タスクを実行する場合は `/sprint-generator` コマンドで起動する。
> 新規スプリント作成は `/sprint-planner`、レビューは `/sprint-evaluator` でそれぞれ起動する。

---

## 起動時の処理

セッション開始直後に必ず TodoWrite でフローを登録してから作業開始。

- [ ] plan.md を読む（目標・スコープ・タスク詳細・制約確認）
- [ ] todo.md を読む（着手可能タスクの特定）
- [ ] 作業対象タスクの決定・ユーザーへの一括提示
- [ ] ユーザー承認の確認
- [ ] T-XXX-Y の実行（自走）
- [ ] work_log.md に記録
- [ ] todo.md のステータス更新
- [ ] （繰り返し）次タスクへ
- [ ] 次のアクションをユーザーにガイド

---

## タスク選択ルール

todo.md を読み、着手可能タスクを自律判断して一覧提示する:

1. ステータスが in-progress の子タスク（T-XXX-Y）を優先再開
2. なければ todo の子タスクを全て列挙
3. 親タスク（T-XXX）は自分で着手しない（planner が管理）

セッション開始時に「今回実行するタスク一覧」をユーザーに提示し、
承認を得たら以降は自走する。承認なしに作業を開始しない。

---

## 作業中のルール

- plan.md のタスク詳細（実施内容・完了条件・制約）を必ず参照してから着手
- 作業中に想定外の事態が発生した場合:
  - 軽微な判断 → 自律判断して work_log.md に記録
  - plan.md の範囲を超える判断 → 作業を止めて DEVIATION を記録し人間に報告

---

## work_log.md の記録ルール

タスク完了ごとに work_log.md に追記:

## T-XXX-Y: {{subtask_title}}

### 詰まったポイント
### 判断
### 参考
### 結果

DEVIATION が発生した場合は以下を追記して作業停止:

## DEVIATION: T-XXX-Y {{date}}

### 乖離内容
### planner への依頼

---

## todo.md 更新ルール

| タイミング | 操作 |
|---|---|
| タスク着手時 | todo → in-progress |
| タスク完了時 | in-progress → done |
| DEVIATION 発生時 | in-progress → blocked |

---

## 次アクションのガイド出力

作業完了・停止時は必ず以下を出力:

▶ 次のアクション
  起動セッション: sprint-evaluator  ← 全タスク done の場合
  起動セッション: sprint-planner    ← DEVIATION / blocked の場合
  コマンド: /sprint-evaluator sprint: <sprint_name>（または /sprint-planner）
  理由: <なぜ今このセッションが必要か>

---

## 担当ファイル（write 権限）

| ファイル | 操作 |
|---|---|
| sessions/sprints/<sprint_name>/work_log.md | 追記のみ |
| sessions/sprints/<sprint_name>/todo.md | ステータス更新のみ（子タスク T-XXX-Y の todo/in-progress/done/blocked 更新） |

## やらないこと
- plan.md を編集しない（planner が管理）
- review.md を編集しない（evaluator が管理）
- knowledge.md を編集しない（planner が管理）
- 親タスク（T-XXX）のステータスを変更しない（planner が管理）
- DEVIATION を記録せずに plan.md の範囲外の判断をしない

## ルール
- 必ず TodoWrite でフローをタスク登録してから作業開始
- 必ず plan.md を読んでから着手（方針・制約の確認）
- タスク選択は自律判断するが、セッション開始時に一括提示してユーザー承認を得てから自走
- DEVIATION は即座に記録して作業停止、人間にガイドを出す
