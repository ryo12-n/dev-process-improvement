# 評価計画: gha-workflow-ux-improvements

## 壁打ちフェーズ [2026-03-19 23:10]

### 理解のサマリー
- 評価の目的: L2 計画ワーカーが作成した `02a_task_division.md` の品質を評価し、タスク分割・Conflict Check Matrix・Wave 割当の正確性を検証する
- 評価スコープ: `02a_task_division.md`（5タスク・2 Wave・12ファイルの Conflict Check Matrix）+ `04_work_report.md`（計画レポート）
- 完了条件: 本ファイル（05_eval_plan.md）に評価計画 + `06_eval_report.md` に評価結果（「評価中の知見」セクション含む）

### 前提条件チェック
- [x] 評価対象（02a_task_division.md, 04_work_report.md）の完成度: 十分
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能
- [x] 評価に必要なツール・アクセス権限: 確認済み
- [x] 参照ドメインエージェント: 指定なし → 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 参照ドメインエージェント

| エージェント名 | 参照パス | 評価への活用方針 |
|-------------|---------|---------------|
| なし | - | - |

## 評価対象
- `02a_task_division.md`: 5タスク（T-001〜T-005）のファイルレベルタスク分割、Conflict Check Matrix（12ファイル x 5タスク）、Wave Assignment（2 Wave）
- `04_work_report.md`: 計画ワーカーの作業レポート

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | タスク粒度 | 各タスクの変更対象ファイル数・変更量を確認し、1ワーカーで完結可能か判定 | 全タスクが単一ワーカーで完結可能なサイズ |
| 2 | CREATE/MODIFY/READ アノテーション | 実際のワークフロー YML・スキル MD を読み取り、02a の記載と照合 | 全ファイルのアクセス種別が実態と一致 |
| 3 | コンフリクトマトリクス | マトリクスの全セルを検証し、MODIFY 競合の見落としがないか確認 | 同一ファイルへの複数 MODIFY が正しく検出されていること |
| 4 | 依存関係 | Prerequisite tasks の設定が変更ファイルの READ/MODIFY 関係と一致するか確認 | 循環依存なし、READ 依存の先行タスクが正しく設定 |
| 5 | Wave 割当 | 同一 Wave 内のタスクが並列実行可能か（MODIFY 競合なし）を確認 | Wave 内にファイル書き込み競合なし |
| 6 | ドメインエージェント推奨 | 施策の性質（GHA YML 変更のみ）に対して「なし」が妥当か確認 | 推奨が施策内容に適合 |
| 7 | 完了条件（Acceptance criteria） | 各タスクの完了条件が 01_plan.md の成功基準を網羅しているか確認 | 5つの成功基準すべてがいずれかのタスクの完了条件に対応 |
| 8 | メタルール横断検証 | `.claude/skills/gha-close/SKILL.md` と `.claude/skills/gha-wallbash/SKILL.md` の変更が計画されているため、関連スキル定義のフロー記述・workflow.md・TG-008 との整合性を確認 | 変更後のスキル記載がワークフロー実態と整合 |

## 評価スケジュール
- 壁打ちフェーズ: 完了
- 評価計画作成: 本ファイル
- 評価実施: 壁打ち完了後、即時実施
- 評価レポート: `06_eval_report.md` に記載

## 前提・制約
- GHA ワークフロー YML のみの変更（コード実装なし）のため、テスト実行の観点は評価対象外
- タスク粒度は「変更箇所が適切に分離されているか」の観点で評価する（L1 からの施策固有注意事項）

---
**作成者**: L2（評価・計画フェーズ）
**作成日**: 2026-03-19

---

## 壁打ちフェーズ（実施評価）[2026-03-19 23:50]

### 理解のサマリー
- 評価の目的: L2 実施ワーカーの作業成果（T-001〜T-009）を `01_plan.md` の成功基準5項目に対して評価する
- 評価スコープ: ワークフロー YML 5件 + GHA スキル 2件 + README 1件の変更内容を直接検証
- 完了条件: 本ファイルに評価計画 + `06_eval_report.md` に評価結果（「評価中の知見」セクション含む）

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全9タスク完了、成果物一覧・知見・メタルール横断検証を含む）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（5項目が具体的に定義されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read, Grep で YML/スキルファイルを直接検証可能）
- [x] 参照ドメインエージェント: 指定なし → 該当なし

### 不明点・確認事項
確認事項なし：評価開始

## 参照ドメインエージェント

| エージェント名 | 参照パス | 評価への活用方針 |
|-------------|---------|---------------|
| なし | - | - |

## 評価対象（実施フェーズ）
- `04_work_report.md`: 実施ワーカーの作業レポート（T-001〜T-009 全件完了）
- 変更ファイル群: `.github/workflows/` 配下5件、`.claude/skills/gha-wallbash/SKILL.md`、`.claude/skills/gha-close/SKILL.md`、`.github/workflows/README.md`

## 評価項目（実施フェーズ）

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E1 | `@ai-task` 完全撤廃 | `.github/` と `.claude/skills/` 配下を grep で `@ai-task` 検索 | 該当箇所 0件 |
| E2 | dispatcher コマンドパース | `initiative-dispatcher.yml` を Read し、`@ai` トリガー条件・grep パターン・エラーメッセージを確認 | 全5コマンドが `@ai /command` 形式でパース可能 |
| E3 | feedback 伝播（dispatcher → 下流） | dispatcher の `/start` と `/approve`(gate-review) で `-f feedback="$ARGS"` が渡されているか確認 | 2箇所で feedback パラメータが下流に渡されている |
| E4 | feedback 伝播（下流 → Claude prompt） | wallbash.yml の prompt に feedback 参照あり（init/continue 共通）、close.yml の prompt に feedback 参照あり | init モードでも feedback が Claude に届く |
| E5 | フェンスドコードブロック化 | wallbash.yml, execute.yml, backlog-to-issue.yml のコメント投稿でコマンドが ` ``` ` で囲まれているか確認 | 3ファイルのコメント投稿で `--body-file` パターン + フェンスドコードブロック |
| E6 | backlog-to-issue cron 間隔 | `backlog-to-issue.yml` の `on.schedule.cron` を確認 | `0 */3 * * *`（3時間間隔） |
| E7 | README 実態一致 | README のワークフロー一覧と `ls .github/workflows/*.yml` を比較 | 存在しないワークフローの記載なし + 存在するワークフロー全記載（test 系除く） |
| E8 | GHA スキルファイル更新 | `gha-wallbash/SKILL.md` に init feedback 記述、`gha-close/SKILL.md` に feedback 活用記述 | 各ファイルに該当記述あり |
| E9 | メタルール横断検証 | `.claude/skills/` 変更のため、フロー記述整合・workflow.md 同期・TG-008 連動を確認 | 変更後のスキル記載がワークフロー実態と整合 |

## 評価スケジュール
- 壁打ちフェーズ: 完了
- 評価計画作成: 本セクション
- 評価実施: 壁打ち完了後、即時実施
- 評価レポート: `06_eval_report.md` に追記

---
**作成者**: L2（評価・実施フェーズ）
**作成日**: 2026-03-19
