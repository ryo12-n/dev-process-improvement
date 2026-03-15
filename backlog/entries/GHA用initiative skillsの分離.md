# GHA 用 initiative skills の分離

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-054 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | <!-- 施策化時に L1 が記入する --> |
| **起票日** | 2026-03-15 |

## 課題・背景

GHA ワークフロー（initiative-wallbash 等）で `claude-code-action` を使用する際、Claude が CLAUDE.md や `.claude/skills/l1-manager/SKILL.md` を読み込み、CLI 対話セッション向けの全フェーズオーケストレーションルールに従って行動してしまう。

テスト実行では、壁打ちフェーズのみのプロンプトにもかかわらず:
- `01_plan.md`, `02_tasks.md` を作成（フェーズ A の成果物）
- `03_work_log.md` 〜 `08_gate_review.md` を Write で自前生成
- `gh pr create` を実行（ワークフロー後続ステップの責務）
- `git rebase`, `git reset --hard` を実行（危険なリカバリ）

現在はプロンプト内の制約文で対処しているが、skills 層での棲み分けが本質的な解決策。

## 期待効果

- **CLI 用と GHA 用の責務分離**: CLI skills は対話的オーケストレーション、GHA skills は単一フェーズの自律実行に特化
- **プロンプト肥大化の防止**: ワークフローの YAML に長大な制約を書く代わりに、skills ファイルを参照する設計
- **再利用性**: 各フェーズの GHA skill を共通化し、wallbash / execute / close / question で参照可能
- **安全性向上**: GHA 環境では不要なツール（gh コマンド等）の制約を skills レベルで管理

## 補足・参考情報

- 検討すべき棲み分け構造:
  - 既存 `skills/l1-manager/`: CLI 対話セッション用（全フェーズオーケストレーション）
  - 新規 `skills/gha-wallbash/` 等: GHA ワークフロー用（単一フェーズ実行、制約付き）
- `claude-code-action` の `settings` で deny リストが使えるかも調査対象
- 関連 inbox: `inbox/gha-execution-file-fix-rollout.md`（execution_file 修正の横展開）
- 関連ワークフロー: `initiative-wallbash.yml`, `initiative-execute.yml`, `initiative-close.yml`, `initiative-question.yml`
- **実践知見**: `refs/claude-code-action/knowledge.md` に claude-code-action のハマりポイント・制約・対策を蓄積済み。施策化時に参照すること
