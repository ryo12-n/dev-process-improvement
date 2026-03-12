# 改善施策提案: impl-worktree-parallel

## 背景・課題

impl-manager の Phase 4 では複数の impl-worker を Wave 方式で並列実行する。現状は `36_file_task_division.md` の静的な Conflict Check Matrix で事前にファイル競合を検出しているが、以下の課題がある:

1. **実行時の動的な競合防止がない**: Conflict Check Matrix は静的な事前計画であり、実行時にワーカーがスコープ外のファイルを変更しても即座に検知できない
2. **`07_issues.md` の同時書き込みリスク**: 並列ワーカーが共有ファイルに同時追記する可能性がある
3. **作業忘れの検知手段がない**: ワーカーがチェックポイント記録や課題起票を忘れた場合のフェールセーフがない

## 目標

1. 外部リポジトリのコードファイルを Git worktree で物理的に分離し、並列ワーカー間のファイル競合を構造的に不可能にする
2. セッション管理ファイル（issues）をワーカー別に分離し、同時書き込みを排除する
3. 3層の検証チェックリスト（事前・ワーカー自身・事後）でフェールセーフを実現する

## スコープ
### やること
- impl-manager SKILL.md に worktree 管理（事前準備・マージ・クリーンアップ）手順を追加
- impl-worker.md に worktree 対応・per-worker issues・完了チェックリストを追加
- impl-evaluator.md に Phase 4 worktree 関連評価基準を追加
- per-worker 課題バッファテンプレート（`07_issues_W_template.md`）を新規作成
- テンプレート（`36_file_task_division.md`, `42_impl_work_report.md`）に worktree セクションを追加
- ブランチ命名を `initiative/` → `impl/` に変更（impl-manager 配下全ファイル）
- ドキュメント連動更新（`docs/git-worktree-guideline.md`, `docs/workflow.md`）

### やらないこと
- 通常の L1/L2 セッション（initiatives）への適用
- Phase 1〜3 の並列化
- Agent ツールの `isolation: worktree` の利用（外部リポの手動 worktree で対応）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- Phase 4 並列ワーカー間のコードファイル競合がゼロになる（構造的保証）
- `07_issues.md` の同時書き込み競合がゼロになる
- 作業忘れを事後検証チェックリストで100%検知・回復可能にする

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| worktree 管理の手順が複雑化し、マネージャーの負荷が増える | 中 | チェックリストで手順を定型化・自動補完 |
| マージ時のコンフリクト発生 | 中 | Conflict Check Matrix による事前防止 + コンフリクト解消手順を明文化 |
| ブランチ命名変更の既存施策への影響 | 低 | impl-manager 固有のみ。通常 L1 は `initiative/` を維持 |

## 壁打ちの背景

### 設計方針の選択

3つの案（A: ロックファイル、B: Git worktree、C: ハイブリッド）を検討し、**案C（ハイブリッド）**を選択した。

- **外部リポ（コードファイル）**: Git worktree で物理分離。ロックファイルではレースコンディションのリスクがあり、worktree による構造的保証が優れる
- **dev-process-improvement（セッションファイル）**: ワーカー別ファイル分離で対応。worktree 不要（既に `41_impl_work_log_W<N>.md` は分離済み、`07_issues.md` を `07_issues_W<N>.md` に分離するだけで十分）

### worktree の適用先

Agent ツールの `isolation: worktree` は dev-process-improvement の worktree を作成するが、実際の競合リスクは外部リポのコードファイル側にある。そのため、外部リポに手動で per-worker worktree を作成する方式を採用した。

### ブランチ命名規則

impl-manager のブランチを `initiative/` から `impl/` に変更し、通常の L1 initiatives と区別する。

### フェールセーフの設計思想

「ワーカーが忘れても大丈夫」を原則とし、3層構造を採用:
1. 事前検証（マネージャー）: ディスパッチ前に環境が整っていることを保証
2. ワーカーセルフチェック: 完了時に自己検証（忘れても問題ない）
3. 事後検証（マネージャー）: Wave 完了後に全項目を検証し、不足分を回復

---
**起票者**: L1
**起票日**: 2026-03-12
**ステータス**: 起票
**backlog元ファイル**: なし（壁打ちからの新規提案）
