---
name: project-progress-sync
description: 'プロジェクトの進捗をセッション施策から反映し、知見を抽出・蓄積する'
user-invocable: true
---
# project-progress-sync — プロジェクト進捗反映 + 知見管理 Skill

## 概要

`projects/<name>/todo.md` に記載された施策の進捗状態を `sessions/initiatives/` から取得して更新し、完了施策のレポートから知見を抽出して `projects/<name>/knowledge.md` に蓄積する。

## 引数仕様

| 引数 | 必須 | 説明 | 例 |
|------|------|------|----|
| `<project-name>` | 必須 | プロジェクト名（`projects/<name>` の `<name>` 部分） | `my-api` |

**引数なし呼び出し時の動作**: 「プロジェクト名を教えてください（例: my-api）」とユーザーに質問する。

## 入力

| リソース | パス | 操作 |
|---------|------|------|
| TODO管理 | `projects/<name>/todo.md` | 読み書き |
| 知見管理 | `projects/<name>/knowledge.md` | 読み書き |
| 全体計画書 | `projects/<name>/plan.md` | 読み書き |
| 施策ディレクトリ | `sessions/initiatives/*/` | 読み取りのみ |
| アーカイブ | `sessions/initiatives/_archive/*/` | 読み取りのみ |

## 担当ファイル

| 操作 | パス |
|------|------|
| 読み書き | `projects/<name>/todo.md` |
| 読み書き | `projects/<name>/knowledge.md` |
| 読み書き | `projects/<name>/plan.md` |
| 読み取りのみ | `sessions/initiatives/*/` 配下全ファイル |
| 読み取りのみ | `sessions/initiatives/_archive/*/` 配下全ファイル |

## 処理フロー

### ステップ 1: todo.md の読み込み

`projects/<name>/todo.md` を読み込み、TODO一覧テーブルから施策名の一覧を取得する。

### ステップ 2: 施策状態の走査

`sessions/initiatives/` および `sessions/initiatives/_archive/` を走査し、todo.md に記載された各施策名と一致するディレクトリを確認する。

### ステップ 3: ステータス判定

各施策のステータスを以下の優先順位で判定する。

| 条件 | ステータス |
|------|-----------|
| `sessions/initiatives/_archive/<施策名>/` が存在する | `完了` |
| `05_gate_review.md` が存在し、判定結果が「通過」 | `完了` |
| `05_gate_review.md` が存在し、判定結果が「通過」以外 | `進行中`（評価完了） |
| `phase-2-execution/` ディレクトリが存在する | `進行中` |
| `01_proposal.md` のみ存在する（plan, tasks がない） | `未着手`（提案のみ） |
| 施策ディレクトリが存在しない | `未着手` |

### ステップ 4: todo.md のステータス更新

ステップ 3 の判定結果に基づき、`projects/<name>/todo.md` の TODO一覧テーブルのステータス列を更新する。最終更新日も更新する。

### ステップ 5: 知見抽出

**完了した施策**（ステータスが `完了` に変わった施策、または前回の同期以降に完了した施策）について、以下のファイルから知見を抽出する。

| ファイル | 抽出対象セクション |
|---------|-----------------|
| `phase-2-execution/set-N/03_worker_report.md` | 「作業中の知見」セクション（ルール化候補テーブル + 参考情報テーブル） |
| `phase-2-execution/set-N/06_eval_report.md` | 「評価中の知見」セクション（ルール化候補テーブル + 参考情報テーブル） |

複数の set が存在する場合は、全 set のレポートを走査する。

### ステップ 6: knowledge.md への追記

抽出した知見を `projects/<name>/knowledge.md` の「施策別知見ログ」テーブルに追記する。

マッピングルール:

| 抽出元の分類 | knowledge.md のカテゴリ |
|------------|----------------------|
| ルール化候補 | `ルール化候補` |
| 参考情報 | `参考情報` |

アクション列は初期値 `保留` を設定する。最終更新日も更新する。

知見テーブルの行に「なし — 理由: ○○」と記載されている場合は、その行は追記対象としない（知見なしと判断する）。

### ステップ 7: plan.md の更新判断

以下のいずれかの条件に該当する場合、`projects/<name>/plan.md` の施策一覧テーブルのステータスを更新し、必要に応じて方針・制約セクションに注記を追加する。

| 条件 | アクション |
|------|-----------|
| 施策がブロック状態（`07_issues.md` に未解決のブロッキング課題がある） | plan.md の施策ステータスを `ブロック` に更新し、ブロック理由を備考に記載 |
| 施策のスコープが大幅に変更された（`05_gate_review.md` の条件付き通過・差し戻し） | plan.md の方針・制約セクションに変更内容を注記 |
| 新たな依存関係が判明した | plan.md の方針・制約セクションに依存関係を追記 |

該当条件がない場合は plan.md を変更しない。

### ステップ 8: 結果報告

更新内容をユーザーに報告する。

```
## 進捗同期結果: <project-name>

### ステータス更新
| 施策名 | 旧ステータス | 新ステータス |
|--------|------------|------------|
| ... | ... | ... |

### 抽出した知見
- <施策名>: N件の知見を knowledge.md に追記

### plan.md の変更
- （変更がある場合のみ記載）
```

## エラーハンドリング

| エラー条件 | 対応 |
|-----------|------|
| `projects/<name>/` が存在しない | 「プロジェクト `<name>` が見つかりません。`/project-init <name>` で初期化してください」と報告して終了 |
| `projects/<name>/todo.md` が存在しない | 同上 |
| todo.md に施策名が記載されていない | 「todo.md に施策が登録されていません」と報告して終了 |
| 施策ディレクトリ内のファイルが想定構造と異なる | 該当施策のステータスを `不明` として報告し、手動確認を促す |

## 関連ファイル一覧

| ファイル | 関係 |
|---------|------|
| `.claude/skills/project-init/SKILL.md` | 前工程（プロジェクト初期化） |
| `projects/_initiative_template/knowledge.md` | knowledge.md のテンプレート |
| `projects/_initiative_template/todo.md` | todo.md のテンプレート |
| `projects/_initiative_template/plan.md` | plan.md のテンプレート |
| `docs/workflow.md` | 可視化文書（本スキル追加時に連動更新） |
