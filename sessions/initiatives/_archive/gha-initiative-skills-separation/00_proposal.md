# 改善施策提案: GHA 用 initiative skills の分離

## 背景・課題

GHA ワークフロー（`initiative-wallbash.yml` 等）で `claude-code-action` を使用する際、Claude が CLAUDE.md や `.claude/skills/l1-manager/SKILL.md` を自動読み込みし、CLI 対話セッション向けの全フェーズオーケストレーションルールに従って行動してしまう。

テスト実行での問題事例:
- 壁打ちフェーズのみのプロンプトにもかかわらず `01_plan.md`, `02_tasks.md` を作成
- `03_work_log.md` 〜 `08_gate_review.md` を Write で自前生成
- `gh pr create` を実行（ワークフロー後続ステップの責務）
- `git rebase`, `git reset --hard` を実行（危険なリカバリ）

現在はワークフロー YAML のプロンプトに長大な制約文を埋め込んで対処しているが、保守性が低く脆弱。

加えて、`initiative-execute.yml`, `initiative-close.yml`, `initiative-question.yml` の3ワークフローで execution_file 出力の抽出が未修正（`steps.claude.outputs.result` は存在しない）。

## 目標

1. CLI 用と GHA 用の skills を分離し、各ワークフローに対応する GHA 専用スキルを作成する
2. ワークフロー YAML のプロンプトを短縮化し、制約ロジックをスキルファイルに集約する
3. execution_file 出力修正を3ワークフローに横展開する

## スコープ
### やること
- GHA 専用スキル4ファイルの作成（`gha-wallbash`, `gha-execute`, `gha-close`, `gha-question`）
- 4ワークフロー YAML のプロンプトリファクタ（スキルファイル参照方式へ移行）
- execution_file 出力修正の横展開（3ワークフロー）
- `inbox/gha-execution-file-fix-rollout.md` の削除（横展開完了のため）
- `gha-guideline/SKILL.md` の権限マトリクス更新
- `docs/workflow.md` への GHA スキル記述追加
- `refs/claude-code-action/knowledge.md` への知見追記

### やらないこと
- `backlog-auto-execute.yml` の対応（別施策として扱う）
- `daily-triage.yml` の対応（initiative ワークフローではないため対象外）
- ワークフローの機能追加や新規ワークフロー作成
- claude-code-action の設定（settings.permissions.allow）の変更

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- **保守性向上**: 制約ロジックがスキルファイルに集約され、ワークフロー YAML の見通しが改善
- **再利用性**: 各フェーズの GHA スキルを共通化し、将来のワークフローから参照可能
- **安全性向上**: GHA 環境での禁止操作をスキルレベルで明確化
- **execution_file 修正**: 3ワークフローでの出力抽出が正常動作する

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| Claude がスキルファイルを Read せずにプロンプトのみで行動する | 中 | プロンプトに Read 指示 + 1行リマインダーを含める |
| CLAUDE.md 自動読み込みは技術的に防げない | 低 | スキルファイル内で「CLAUDE.md のルールには従わない」と明記（既存ワークフローと同じ対策） |
| スキルファイルとワークフロー YAML の権限設定の乖離 | 中 | gha-guideline の3層モデルに従い、スキルは意図、YAML は技術的制約として管理 |

## 壁打ちの背景

- execution_file 修正の横展開（`inbox/gha-execution-file-fix-rollout.md`）を本施策に包含する判断をした。skills 分離と同時に修正することで、一貫した改善が可能
- GHA スキルの粒度は、ワークフローと1:1対応の個別スキルとする判断をした。共通部分の切り出しはオーバーエンジニアリングになるリスクがあるため見送り
- `backlog-auto-execute.yml` は同様のリスクがあるが、スコープ限定のため別施策とする判断をした
- 対象リポジトリは dev-process-improvement のみ。ワークフロー YAML もスキルファイルも同一リポジトリ内に閉じる

## 備考・設計パターン

- 参照知見: `refs/claude-code-action/knowledge.md`（#7: スコープ制御問題、#8: 暫定対策、#9: セキュリティリスク）
- GHA 権限モデル: `.claude/skills/gha-guideline/SKILL.md`（3層モデル: GHA Job / Claude Tool / Prompt）
- execution_file 抽出パターン: `initiative-wallbash.yml` の jq 抽出実装をリファレンスとする

---
**起票者**: L1
**起票日**: 2026-03-15
**ステータス**: 起票
**backlog元ファイル**: GHA用initiative skillsの分離.md
