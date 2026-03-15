# 評価計画: GHA Initiative ワークフロー

## 壁打ちフェーズ [2026-03-14]

### 理解のサマリー
- 評価の目的: L2-worker が作成したワークフロー3ファイル + gha-guideline 更新が、01_plan.md の成功基準を満たしているかを検証する
- 評価スコープ: `.github/workflows/initiative-{wallbash,execute,close}.yml` の構造・トリガー・権限設計・フロー整合性、および `.claude/skills/gha-guideline/SKILL.md` §5 の追記内容
- 完了条件: 成功基準5項目すべてについて達成度を判定し、06_eval_report.md に記録。評価中の知見セクションに最低1行記載

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全タスク T-001〜T-006 が完了と報告されている）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（5項目が具体的に記述されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（ファイル読み取りのみで評価可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.github/workflows/initiative-wallbash.yml` — 壁打ちフェーズワークフロー
- `.github/workflows/initiative-execute.yml` — 実行フェーズワークフロー
- `.github/workflows/initiative-close.yml` — クローズフェーズワークフロー
- `.claude/skills/gha-guideline/SKILL.md` — §5 権限マトリクス追記部分

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-001 | wallbash.yml のトリガー設計 | ワークフローの `on:` と `if:` を確認し、`issues:labeled` + `workflow_dispatch` の両トリガーが正しく動作するか検証 | `issues:labeled` で `initiative-start` ラベル付与時に発火、`workflow_dispatch` で issue_number 入力を受け付ける |
| E-002 | wallbash.yml の壁打ちサマリー投稿フロー | Claude ステップの出力 → Issue コメント投稿の流れを確認 | Claude の出力が `steps.claude.outputs.result` 経由で Issue コメントとして投稿される |
| E-003 | execute.yml のトリガー設計 | `issue_comment:created` の条件分岐を確認。`/approve`（wallbashing→execute）と `/reject`（gate-review→re-execute）の両パスが定義されているか | 2つのコマンドパス（approve + reject）が正しいラベル条件と組み合わされている |
| E-004 | execute.yml のフェーズ間状態引き継ぎ | PR ブランチの取得・チェックアウトロジックを確認 | Issue 番号から PR を検索し、ブランチをチェックアウトして Claude が作業を継続できる |
| E-005 | execute.yml の bot コメント排除 | `issue_comment` トリガーの安全対策を確認 | `github-actions[bot]` のコメントと PR コメントの両方が除外されている |
| E-006 | close.yml のアーカイブ・クローズフロー | ワークフロー全体の構造を確認。Issue クローズ + ラベル更新が Shell ステップで実行されるか | Claude がアーカイブ移動を実行 → Shell ステップで Issue クローズ + ラベル更新 |
| E-007 | 3ワークフローの権限設計 | GHA permissions + Claude Code ツール許可を確認し、3層権限モデルとの整合性を検証 | L1(GHA) ⊇ L3(プロンプト指示)、L2(Claude ツール) ⊇ L3、L2 ⊆ 最小権限 が成立 |
| E-008 | gha-guideline §5 の追記内容 | §5.1（ワークフロー一覧）、§5.2（権限マトリクス）、§5.3（設計判断の記録）に3ワークフローが追記されているか | 3ワークフローすべてのエントリが §5.1, §5.2, §5.3 に存在し、内容がワークフローファイルと一致 |
| E-009 | gha-guideline 関連ファイル一覧の更新 | 関連ファイル一覧に新規3ワークフローが追加されているか | 3ワークフローが関連ファイル一覧に含まれている |
| E-010 | メタルール横断検証（条件付き） | `.claude/skills/gha-guideline/SKILL.md` が変更対象のため、フロー記述整合性・workflow.md 同期・TG-008 基準を確認 | スキル定義の変更箇所がフロー記述と一致していること |

## 評価スケジュール
- E-001〜E-006: ワークフローファイルのレビュー（構造・ロジック確認）
- E-007: 3層権限モデル整合性チェック
- E-008〜E-009: gha-guideline 更新内容の確認
- E-010: メタルール横断検証

## 前提・制約
- E2E テスト（実際の GHA 実行）は施策スコープ外のため、構造レビューと論理検証のみで評価する
- ラベルの事前作成は実行時の前提条件であり、ワークフロー定義の評価対象外とする

---
**作成者**: L2（評価）
**作成日**: 2026-03-14
