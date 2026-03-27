# 改善施策提案: sprint-skill-implementation

## 背景・課題

スプリント形式の開発作業を進める際に、planner / generator / evaluator という役割分担が概念として存在するが、Claude Code のセッションとして呼び出せる実装がない。各ロールの責任・操作対象・禁止事項が明文化されていないため、セッションをまたいだ作業の一貫性が担保できていない。

`templates/sprint_template/` にテンプレート5ファイルは作成済みだが、実際のスプリント運用時のコピー先フォルダ（`sessions/sprints/`）が未定義。また、テンプレート内の変数名に不統一がある（`{{repository_name}}` vs `{{repo}}`）。

## 目標

- planner / generator / evaluator の3ロールをそれぞれ独立した skill として実装する
- `sessions/sprints/` 配下にテンプレート・アーカイブの置き場を整備し、スプリントのライフサイクルを管理できるようにする
- テンプレート内の変数名を統一する

## スコープ
### やること
- `.claude/skills/sprint-planner/SKILL.md` の作成
- `.claude/skills/sprint-generator/SKILL.md` の作成
- `.claude/skills/sprint-evaluator/SKILL.md` の作成
- `templates/sprint_template/` の5ファイルを `sessions/sprints/_template/` に `git mv` で移動
- `sessions/sprints/_archive/.gitkeep` の作成
- `sessions/sprints/_template/knowledge.md` 内の変数名統一（`{{repo}}` → `{{repository_name}}`）
- SKILL.md 仕様の改善（起動キーワード明確化、親タスク管理者の明記）
- コミットメッセージ規約への sprint 系 session-type 追加を inbox に起票

### やらないこと
- 既存の `l1-manager` / `l2-worker` / `l2-evaluator` への変更
- `templates/sprint_template/` 以外のテンプレートへの変更
- CLAUDE.md の変更
- コミットメッセージ規約（`.claude/rules/commit-message.md`）の直接変更

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## プロジェクト紐づけ

| プロジェクト名 | パス |
|-------------|------|
| なし | - |

## 期待される効果

- `sprint-planner` / `sprint-generator` / `sprint-evaluator` を人間がオーケストレートしながら並列に使える
- 各ロールの責任範囲がファイルレベルで明確になり、操作ミスを防止できる
- `sessions/sprints/` 配下でスプリントのライフサイクル（作成→運用→アーカイブ）が完結する

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| `templates/sprint_template/` を移動することで既存参照が壊れる | 低 | 移動前に grep で参照箇所を確認する |
| skill の起動キーワードが既存 skill と競合する | 低 | 既存 skill の name 一覧を確認してから命名する |

## 壁打ちの背景

### ロール設計の意思決定
- **skill vs agent**: 3ロールとも人間がターミナルで直接起動するため、全て skill として実装。agent のメリット（並列・コンテキスト分離）が今回のユースケースでは不要と判断
- **オーケストレーターは人間**: planner は統括者ではなく計画・管理の専門家。3ロールは並列・独立の関係
- **Sprint ID**: sprint_name = ID（連番管理なし）
- **タスク選択**: generator は todo.md を読んで自律判断し、セッション開始時に一括提示してユーザー承認後に自走する
- **レビュー対象**: evaluator は done タスク全体を Round 単位でレビューする
- **壁打ち必須**: planner は plan.md / todo.md 記入前に必ずユーザーと壁打ちし認識を合わせる

### SKILL.md 仕様の評価結果
- **指摘A（settings.json 登録）**: 対応不要。`.claude/skills/` ディレクトリから自動検出される
- **指摘B（起動キーワード競合）**: 3ロール全て `sprint:` で始まるため区別が曖昧。SKILL.md 内で起動パターンを明確化する（タスクとして対応）
- **指摘C（親タスク管理）**: planner が親タスクのステータス管理を担う旨を sprint-planner の「フォルダ状態に応じた分岐」に明記する（タスクとして対応）
- **指摘D（コミットメッセージ規約）**: スコープ外。inbox に起票して別施策で対応

## 備考・設計パターン

各 SKILL.md の詳細仕様は `inbox/sprint-skill-implementation 実施計画書.md` の「備考・設計パターン」セクションに記載されている。L2-worker はこの仕様を基に SKILL.md を作成し、指摘B・C の改善を反映する。

---
**起票者**: L1
**起票日**: 2026-03-26
**ステータス**: 実施中
**backlog元ファイル**: なし
