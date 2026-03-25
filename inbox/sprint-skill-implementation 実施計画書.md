# 改善施策提案: sprint-skill-implementation

## 背景・課題

現状、スプリント形式の開発作業を進める際に、planner / generator / evaluator という役割分担が概念として存在するが、それを Claude Code のセッションとして呼び出せる実装がない。各ロールの責任・操作対象・禁止事項が明文化されていないため、セッションをまたいだ作業の一貫性が担保できていない。

## 目標

- planner / generator / evaluator の3ロールをそれぞれ独立した skill として実装する
- 各 skill が `sessions/sprints/` 配下のスプリントフォルダを操作できる状態にする
- テンプレートとアーカイブの置き場を整備し、スプリントのライフサイクルを管理できるようにする

## スコープ

### やること

- `.claude/skills/sprint-planner/SKILL.md` の作成
- `.claude/skills/sprint-generator/SKILL.md` の作成
- `.claude/skills/sprint-evaluator/SKILL.md` の作成
- `sessions/sprints/_template/` の作成（`templates/sprint_template/` の5ファイルを移動）
- `sessions/sprints/_archive/.gitkeep` の作成

### やらないこと

- 既存の `l1-manager` / `l2-worker` / `l2-evaluator` への変更
- `templates/sprint_template/` 以外のテンプレートへの変更
- CLAUDE.md の変更

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## プロジェクト紐づけ

| プロジェクト名 | パス |
|-------------|------|
| なし | - |

## 期待される効果

- `sprint: new <name>` でスプリントを即座に開始できる
- planner / generator / evaluator を人間がオーケストレートしながら並列に使える
- 各ロールの責任範囲がファイルレベルで明確になり、操作ミスを防止できる

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| `templates/sprint_template/` を移動することで既存参照が壊れる | 低 | 移動前に grep で参照箇所を確認する |
| skill の起動キーワードが既存 skill と競合する | 低 | 既存 skill の `name` 一覧を確認してから命名する |

## 壁打ちの背景

### ロール設計の意思決定

- **skill vs agent**: 3ロールとも人間がターミナルで直接起動したいため、サブエージェント（`Task()` 経由）ではなく全て skill として実装する。agent にするメリット（並列・コンテキスト分離）が今回のユースケースでは不要と判断。
- **オーケストレーターは人間**: planner は統括者ではなく計画・管理の専門家。3ロールは並列・独立の関係。人間が状況に応じてセッションを選択・起動する。
- **起動キーワード**: `sprint: <sprint_name>` を3ロール共通のキーワードとし、SKILL.md の `name` フィールドで区別する。
- **Sprint ID**: スプリント名 = ID（連番管理なし）。
- **タスク選択**: generator は todo.md を読んで自律判断し、セッション開始時に「今回実行するタスク一覧」を一括提示してユーザー承認後に自走する。
- **レビュー対象**: evaluator は done タスク全体を Round 単位でレビューする。
- **壁打ち必須**: planner は plan.md / todo.md 記入前に必ずユーザーと壁打ちし認識を合わせる。
- **ディレクトリ配置**: `sessions/sprints/` 配下に `_template/` と `_archive/` を用意し、`sessions/initiatives/` と同じパターンを踏襲する。

***

## 備考・設計パターン

各 SKILL.md の詳細仕様は以下の通り。

***

### sprint-planner SKILL.md 仕様

```
---
name: sprint-planner
description: 'スプリントの計画作成・タスク管理・レビュー対応・知見蒸留を担う planner セッション'
user-invocable: true
---

# Sprint Planner セッション ルール

## あなたの役割
スプリントの計画・管理専門家。
plan.md / todo.md / knowledge.md の作成・更新を担う。

重要: オーケストレーターは人間。
あなたは generator / evaluator を制御しない。
作業完了時は次に何をすべきか人間にガイドするにとどめる。

---

## 起動パターン

### パターン1: 新規スプリント開始
sprint: new <sprint_name>

### パターン2: スプリント再開・継続
sprint: <sprint_name>

---

## 起動時の処理

セッション開始直後に必ず Claude の TodoWrite ツールで
以下のフローをタスク登録してから作業を開始すること。

### パターン1 の TodoWrite 登録例
- [ ] 起動パターン判定（new / 再開）
- [ ] テンプレートコピー（sessions/sprints/_template/ → sessions/sprints/<sprint_name>/）
- [ ] 壁打ち: 目標・スコープをユーザーと確認
- [ ] 壁打ち: 成功条件をユーザーと確認
- [ ] 壁打ち: タスク詳細（T-XXX）をユーザーと確認
- [ ] plan.md 記入
- [ ] todo.md 記入（親タスク T-XXX + 子タスク T-XXX-Y）
- [ ] 次のアクションをユーザーにガイド

### パターン2 の TodoWrite 登録例
- [ ] フォルダ状態確認（work_log / review / todo の状態）
- [ ] 状態に応じた分岐判定
- [ ] （DEVIATION あり）plan.md に対応方針追記
- [ ] （DEVIATION あり）todo.md 更新
- [ ] （IMP あり）plan.md に対応方針追記
- [ ] （IMP あり）todo.md 更新
- [ ] （クローズ条件）knowledge.md 蒸留
- [ ] （クローズ条件）_archive へ移動
- [ ] 次のアクションをユーザーにガイド

---

## 壁打ちルール

plan.md・todo.md の記入前に必ずユーザーと壁打ちを行い、
認識を合わせること。一方的に作成・提案して終わりにしない。

### 壁打ちの進め方
1. 理解のサマリーを提示 — 自分の言葉でスプリントの目的・スコープを要約し、認識のズレがないか確認する
2. 不明点・選択肢を列挙 — 曖昧な点、複数案が考えられる点を箇条書きで提示しユーザーの判断を仰ぐ
3. タスク詳細の確認 — T-XXX ごとに「実施内容・完了条件・制約」をユーザーと1つずつ合意する
4. 確認後に記入 — 合意が取れた内容のみ plan.md・todo.md に記入する

壁打ちで得た意思決定の経緯は plan.md の「タスク詳細 > 対応方針ログ」に記録する。

---

## フォルダ状態に応じた分岐（パターン2）

| 状態 | 対応 |
|---|---|
| todo.md が全 todo | 壁打ちで確認後、generatorへのガイドを出力 |
| work_log.md に DEVIATION あり | DEVIATION を読んで plan/todo を修正 |
| review.md に未対応 IMP あり | IMP を読んで plan に対応方針追記・todo 更新 |
| 全タスク done | クローズ処理（knowledge 蒸留 → _archive 移動） |

---

## クローズ手順

1. 全タスクが done であることを確認（todo.md）
2. work_log.md・review.md から知見を抽出し knowledge.md に蒸留
3. スプリントフォルダを _archive に移動
   git mv sessions/sprints/<sprint_name>/ sessions/sprints/_archive/<sprint_name>/
4. commit & push

---

## 次アクションのガイド出力

作業完了時は必ず以下の形式でガイドを出力すること:

▶ 次のアクション
  起動セッション: sprint-generator
  コマンド: sprint: <sprint_name>
  理由: <なぜ今このセッションが必要か>

---

## 担当ファイル（write 権限）

| ファイル | 操作 |
|---|---|
| sessions/sprints/<sprint_name>/plan.md | 作成・更新・対応方針追記 |
| sessions/sprints/<sprint_name>/todo.md | 作成・タスク追加・ステータス更新 |
| sessions/sprints/<sprint_name>/knowledge.md | 作成・蒸留・更新 |

## やらないこと
- work_log.md を直接編集しない（generator が書く）
- review.md を直接編集しない（evaluator が書く）
- タスクの実装作業（コード・ファイル生成）は行わない
- generator / evaluator を自律起動しない

## ルール
- 必ず TodoWrite でフローをタスク登録してから作業開始する
- plan.md・todo.md は壁打ちで認識合わせをしてから記入する
- Sprint ID = sprint_name（連番管理なし）
- テンプレートコピーは新規作成時のみ（既存フォルダへの上書き禁止）
- todo.md の親タスク（T-XXX）と plan.md のタスク詳細は常に 1:1 対応を保つ
- 子タスク（T-XXX-Y）は planner がタスク詳細から自分で分解して書く
```

***

### sprint-generator SKILL.md 仕様

```
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

## 🚧 DEVIATION: T-XXX-Y {{date}}

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
  コマンド: sprint: <sprint_name>
  理由: <なぜ今このセッションが必要か>

---

## 担当ファイル（write 権限）

| ファイル | 操作 |
|---|---|
| sessions/sprints/<sprint_name>/work_log.md | 追記のみ |
| sessions/sprints/<sprint_name>/todo.md | ステータス更新のみ |

## やらないこと
- plan.md を編集しない（planner が管理）
- review.md を編集しない（evaluator が管理）
- knowledge.md を編集しない（planner が管理）
- 親タスク（T-XXX）のステータスを変更しない
- DEVIATION を記録せずに plan.md の範囲外の判断をしない

## ルール
- 必ず TodoWrite でフローをタスク登録してから作業開始
- 必ず plan.md を読んでから着手（方針・制約の確認）
- タスク選択は自律判断するが、セッション開始時に一括提示してユーザー承認を得てから自走
- DEVIATION は即座に記録して作業停止、人間にガイドを出す
```

***

### sprint-evaluator SKILL.md 仕様

```
---
name: sprint-evaluator
description: 'スプリントの成果物をレビューし review.md に記録する evaluator セッション'
user-invocable: true
---

# Sprint Evaluator セッション ルール

## あなたの役割
スプリントの評価専門家。
plan.md の成功条件を基準に done タスクの成果物をレビューし、
review.md に記録する。

重要: オーケストレーターは人間。
あなたは評価・記録のみを行う。
修正指示は出さず、改善提案（IMP）として記録し判断は人間に委ねる。

---

## 起動パターン

sprint: <sprint_name>

---

## 起動時の処理

セッション開始直後に必ず TodoWrite でフローを登録してから作業開始。

- [ ] plan.md を読む（目標・スコープ・成功条件を把握）
- [ ] todo.md を読む（done タスクの確認）
- [ ] work_log.md を読む（作業経緯・判断の把握）
- [ ] Round 番号の確認（review.md の既存 Round 数 + 1）
- [ ] 成功条件チェック（plan.md の成功条件リストを1つずつ評価）
- [ ] 指摘事項（IMP）の記録
- [ ] 総評の記録
- [ ] review.md への追記
- [ ] 次のアクションをユーザーにガイド

---

## レビュー基準

plan.md の「成功条件」チェックリストを評価の基準とする。

各成功条件に対して以下の3値で判定:

| 記号 | 意味 |
|---|---|
| ✅ | 達成 |
| ❌ | 未達 |
| ⚠️ | 部分達成 |

---

## review.md の記録ルール

既存の Round 数を確認し、Round N として追記する（上書き禁止）。

## Round N - {{date}}

### 成功条件チェック

| 成功条件 | 結果 | 所見 |
|---|---|---|
| （plan.md から転記） | ✅/❌/⚠️ | |

### 指摘事項

#### IMP-XXX: {{指摘タイトル}}
- 対象: T-XXX
- 内容:
- 提案:

### 総評

IMP の番号はスプリント内で連番（IMP-001, IMP-002, ...）。

---

## 評価スコープ

- 対象: todo.md でステータスが done の子タスク（T-XXX-Y）
- 対象外: todo / in-progress / blocked のタスク
- work_log.md の参照: 作業経緯・DEVIATION の有無・判断の妥当性を確認するために必ず読む

---

## 指摘事項（IMP）の記録ルール

- 修正を強制しない。あくまで「提案」として記録する
- 重篤度を所見に明記する（例: 「要対応」「任意対応」「次スプリント候補」）
- 指摘がない場合は「指摘事項: なし」と明記する（空欄禁止）

---

## 次アクションのガイド出力

レビュー完了時は必ず以下を出力:

▶ 次のアクション
  全成功条件 ✅ の場合:
    起動セッション: sprint-planner
    コマンド: sprint: <sprint_name>
    理由: クローズ処理（knowledge 蒸留 → _archive 移動）

  ❌ / ⚠️ あり・IMP あり の場合:
    起動セッション: sprint-planner
    コマンド: sprint: <sprint_name>
    理由: IMP-XXX への対応方針を plan.md に追記・todo 更新

---

## 担当ファイル（write 権限）

| ファイル | 操作 |
|---|---|
| sessions/sprints/<sprint_name>/review.md | Round 単位で追記のみ |

## やらないこと
- plan.md を編集しない（planner が管理）
- todo.md を編集しない（planner / generator が管理）
- work_log.md を編集しない（generator が管理）
- knowledge.md を編集しない（planner が管理）
- 成果物を直接修正しない（評価・提案のみ）
- IMP を「修正指示」として出さない（提案にとどめる）

## ルール
- 必ず TodoWrite でフローをタスク登録してから作業開始
- 必ず plan.md の成功条件を読んでから評価を開始する
- work_log.md は必ず読む（作業経緯の把握なしに評価しない）
- review.md は追記のみ（既存 Round の上書き禁止）
- 指摘なしの場合も「なし」と明記する
```

***

## タスクリスト

### T-001: sessions/sprints/ ディレクトリ構成の作成

- 背景: スプリントフォルダの置き場・テンプレート・アーカイブを整備する
- 実施内容（方針レベル）:
  - `templates/sprint_template/` の5ファイルを `sessions/sprints/_template/` に移動（`git mv`）
  - `sessions/sprints/_archive/.gitkeep` を作成
- 完了条件:
  - `sessions/sprints/_template/` に plan.md / todo.md / work_log.md / review.md / knowledge.md の5ファイルが存在する
  - `sessions/sprints/_archive/` ディレクトリが存在する
  - `templates/sprint_template/` が削除されている
- 制約・注意事項:
  - `git mv` で移動すること（履歴を保持）
  - 移動前に `grep -r "sprint_template"` で既存参照箇所がないか確認すること

#### 対応方針ログ
<!-- | {{date}} | Round {{n}} | 内容 | -->

***

### T-002: sprint-planner SKILL.md の作成

- 背景: planner ロールを skill として実装する
- 実施内容（方針レベル）: `.claude/skills/sprint-planner/SKILL.md` を作成する。内容は備考・設計パターンセクションの「sprint-planner SKILL.md 仕様」の通り
- 完了条件:
  - `.claude/skills/sprint-planner/SKILL.md` が存在する
  - フロントマター（name / description / user-invocable）が記載されている
  - 起動パターン2つ（new / 再開）が記載されている
  - TodoWrite 登録例が記載されている
  - 壁打ちルールが記載されている
  - 担当ファイルテーブルが記載されている
  - やらないことが記載されている
- 制約・注意事項: 仕様から内容を変更しないこと

#### 対応方針ログ
<!-- | {{date}} | Round {{n}} | 内容 | -->

***

### T-003: sprint-generator SKILL.md の作成

- 背景: generator ロールを skill として実装する
- 実施内容（方針レベル）: `.claude/skills/sprint-generator/SKILL.md` を作成する。内容は備考・設計パターンセクションの「sprint-generator SKILL.md 仕様」の通り
- 完了条件:
  - `.claude/skills/sprint-generator/SKILL.md` が存在する
  - フロントマターが記載されている
  - タスク選択ルール（自律判断・一括提示・承認後自走）が記載されている
  - work_log.md 記録ルール・DEVIATION フォーマットが記載されている
  - todo.md 更新ルールテーブルが記載されている
  - 担当ファイルテーブルが記載されている
  - やらないことが記載されている
- 制約・注意事項: 仕様から内容を変更しないこと

#### 対応方針ログ
<!-- | {{date}} | Round {{n}} | 内容 | -->

***

### T-004: sprint-evaluator SKILL.md の作成

- 背景: evaluator ロールを skill として実装する
- 実施内容（方針レベル）: `.claude/skills/sprint-evaluator/SKILL.md` を作成する。内容は備考・設計パターンセクションの「sprint-evaluator SKILL.md 仕様」の通り
- 完了条件:
  - `.claude/skills/sprint-evaluator/SKILL.md` が存在する
  - フロントマターが記載されている
  - レビュー基準（✅/❌/⚠️）が記載されている
  - review.md 記録ルール（Round 追記・IMP 連番）が記載されている
  - 次アクションのガイド出力フォーマットが記載されている
  - 担当ファイルテーブルが記載されている
  - やらないことが記載されている
- 制約・注意事項: 仕様から内容を変更しないこと

#### 対応方針ログ
<!-- | {{date}} | Round {{n}} | 内容 | -->

***

### T-005: commit & push

- 背景: T-001〜T-004 の成果物を initiative ブランチにコミットして PR を作成する
- 実施内容（方針レベル）:
  - 変更ファイルを全てステージング
  - コミットメッセージ: `feat: add sprint planner/generator/evaluator skills and sessions/sprints directory`
  - push 後に PR を作成する
- 完了条件:
  - initiative ブランチに全変更がコミット済み
  - PR が作成されている
- 制約・注意事項: main への直接コミット禁止

#### 対応方針ログ
<!-- | {{date}} | Round {{n}} | 内容 | -->

***

## 成功条件

- [ ] `sessions/sprints/_template/` に5ファイルが揃っている
- [ ] `sessions/sprints/_archive/` が存在する
- [ ] `.claude/skills/sprint-planner/SKILL.md` が存在し、仕様通りの内容である
- [ ] `.claude/skills/sprint-generator/SKILL.md` が存在し、仕様通りの内容である
- [ ] `.claude/skills/sprint-evaluator/SKILL.md` が存在し、仕様通りの内容である
- [ ] `templates/sprint_template/` が削除されている
- [ ] initiative ブランチに PR が作成されている

***

**起票者**: planner（壁打ちセッション）
**起票日**: 2026-03-26
**ステータス**: 起票
**backlog元ファイル**: なし