# 評価レポート: GHA Initiative ワークフロー

## 評価サマリ

L2-worker の成果物（ワークフロー3ファイル + gha-guideline §5 更新）は、01_plan.md の成功基準5項目のうち4項目を達成し、1項目を一部達成と判定した。ワークフローの構造・トリガー設計・権限設計・ラベルフローは適切に実装されている。主な指摘事項は wallbash.yml における Issue 本文のプロンプト注入方法（`$(cat /tmp/issue_body.txt)` が GHA の `prompt:` 入力フィールドではシェル展開されない問題）であり、実運用時に壁打ちの入力情報が欠落するリスクがある。

## 評価結果

| # | 評価項目 | 判定基準 | 結果 | 判定 |
|---|---------|---------|------|------|
| E-001 | wallbash.yml のトリガー設計 | `issues:labeled` + `workflow_dispatch` の両トリガーが定義されている | `on:` に `issues: types: [labeled]` と `workflow_dispatch: inputs: issue_number` が定義されている。ジョブ条件で `initiative-start` ラベルまたは `workflow_dispatch` をチェック | ✅ |
| E-002 | wallbash.yml の壁打ちサマリー投稿フロー | Claude の出力が Issue コメントとして投稿される | `steps.claude.outputs.result` を `gh issue comment` で投稿する Shell ステップが存在。ただし `prompt:` 内の `$(cat /tmp/issue_body.txt)` は GHA の入力フィールドではシェル展開されず、Claude にリテラル文字列として渡される。Claude が `Bash(cat *)` 権限で `/tmp/issue_body.txt` を読めるため完全に機能しないわけではないが、プロンプト内にインラインで Issue 本文が展開される意図であれば不具合 | ⚠️ |
| E-003 | execute.yml のトリガー設計 | `/approve`（wallbashing→execute）と `/reject`（gate-review→re-execute）の両パスが定義されている | `issue_comment:created` トリガーで、`initiative:wallbashing` + `/approve` と `initiative:gate-review` + `/reject` の2パスが if 条件に正しく定義されている | ✅ |
| E-004 | execute.yml のフェーズ間状態引き継ぎ | Issue 番号から PR を検索し、ブランチをチェックアウトして作業継続できる | `gh pr list --search` で Issue 番号を検索し、`body` に `#<Issue番号>` を含む PR を特定。ブランチをフェッチ・チェックアウトするステップが実装されている | ✅ |
| E-005 | execute.yml の bot コメント排除 | `github-actions[bot]` と PR コメントが除外されている | if 条件に `github.event.issue.pull_request == null` と `github.event.comment.user.login != 'github-actions[bot]'` の両方が含まれている | ✅ |
| E-006 | close.yml のアーカイブ・クローズフロー | Claude がアーカイブ移動 → Shell ステップで Issue クローズ + ラベル更新 | プロンプトに `git mv` によるアーカイブ移動指示あり。Shell ステップで `gh issue close` と `--add-label "initiative:completed"` が実行される | ✅ |
| E-007 | 3ワークフローの権限設計 | L1 ⊇ L3、L2 ⊇ L3、L2 ⊆ 最小権限が成立 | 3ワークフローとも GHA permissions は `contents:write, pull-requests:write, issues:write, id-token:write`。Claude ツール許可に `Bash(gh *)` を含まず、gh 操作は Shell ステップで実行（最小権限の原則に準拠）。`Bash(cat *)` は wallbash のみで必要だが3ファイルとも含まれている（execute/close では不要だが低リスク） | ✅ |
| E-008 | gha-guideline §5 の追記内容 | 3ワークフローのエントリが §5.1〜§5.3 に存在 | §5.1 に3ワークフローの方式・トリガー・用途が記載。§5.2 に権限マトリクス（GHA permissions、Claude ツール許可、git/gh 操作の実行者）が記載。§5.3 に設計判断の根拠が記載。すべてワークフローファイルの実装と一致 | ✅ |
| E-009 | gha-guideline 関連ファイル一覧の更新 | 3ワークフローが関連ファイル一覧に含まれている | `initiative-wallbash.yml`、`initiative-execute.yml`、`initiative-close.yml` の3ファイルが関連ファイル一覧に追加されている | ✅ |
| E-010 | メタルール横断検証 | スキル定義の変更箇所がフロー記述・workflow.md と整合 | gha-guideline SKILL.md の §5 追記は既存セクションへの行追加のみで、スキルのフロー定義（§1〜§4）に変更なし。ただし `docs/workflow.md` の「自動施策化フロー（GitHub Actions）」セクションに initiative ワークフロー群の記載がない。gha-guideline 関連ファイル一覧に `docs/workflow.md` の更新必要性が記載されているが、02_tasks.md のスコープには含まれていない | ⚠️ |

## 計画の成功基準に対する達成度

| 成功基準 | 達成度 | 根拠 |
|---------|--------|------|
| 1. `initiative-wallbash.yml` が `issues:labeled` と `workflow_dispatch` でトリガーされ、壁打ちサマリーを Issue コメントに投稿する | 一部達成 | トリガー設計とコメント投稿フローは正しい。ただし `$(cat /tmp/issue_body.txt)` の展開問題により、Claude が Issue 本文をプロンプト内で直接参照できない可能性がある（Claude が自発的にファイルを読む場合は機能するが、意図した動作と異なる） |
| 2. `initiative-execute.yml` が `/approve` コメントで起動し、計画・実行・評価・ゲート判定を自律実行する | 達成 | `/approve` と `/reject` の両パスが正しく条件分岐され、プロンプトに計画〜ゲート判定の全手順が含まれている |
| 3. `initiative-close.yml` が `/approve` コメントでアーカイブ・Issue クローズを行う | 達成 | `initiative:gate-review` + `/approve` で起動し、アーカイブ移動→Issue クローズ→ラベル更新のフローが実装されている |
| 4. フェーズ間の状態引き継ぎが PR ブランチ経由で機能する | 達成 | execute.yml と close.yml で Issue 番号から PR ブランチを検索・チェックアウトする共通パターンが実装されている |
| 5. `gha-guideline` に新ワークフローの権限マトリクスが追記されている | 達成 | §5.1, §5.2, §5.3 に3ワークフローのエントリが追加され、関連ファイル一覧も更新されている |

## 発見された課題・改善提案

### 課題1: wallbash.yml の `$(cat /tmp/issue_body.txt)` がプロンプト内で展開されない

- **深刻度**: 中
- **内容**: `anthropics/claude-code-action@v1` の `prompt:` 入力は GHA の式評価 (`${{ }}`) のみが展開される。`$(cat /tmp/issue_body.txt)` はシェルコマンド置換であり、この文脈では展開されずリテラル文字列として Claude に渡される。Claude は `Bash(cat *)` 権限を持つため自発的にファイルを読める可能性はあるが、プロンプト設計の意図としては Issue 本文がインラインで注入されることを期待している
- **推奨対策**:
  - 案A: Issue 本文を `${{ }}` 式で直接注入する（`${{ github.event.issue.body }}` または `steps.info.outputs.body`）
  - 案B: `GITHUB_OUTPUT` にマルチライン出力として書き込み、`${{ steps.info.outputs.body }}` で参照する
  - 案C: `Bash(cat *)` 権限を活かし、プロンプト内でファイルパスを明示して Claude に読み取りを指示する形に変更する

### 課題2: docs/workflow.md に initiative ワークフロー群の記載がない

- **深刻度**: 低
- **内容**: `docs/workflow.md` の「自動施策化フロー（GitHub Actions）」セクションには既存の `backlog-auto-execute.yml` のみが記載されている。新規 initiative ワークフロー3つの追記がない。gha-guideline SKILL.md の関連ファイル一覧でも `docs/workflow.md` の更新が必要と記載されている
- **備考**: 02_tasks.md のスコープには含まれていないため、ワーカーのタスク漏れではなく計画時のスコープ定義の問題。次施策または別タスクとして対応可能

### 課題3: execute/close.yml の `Bash(cat *)` 権限が不要

- **深刻度**: 低
- **内容**: `Bash(cat *)` は wallbash.yml で `/tmp/issue_body.txt` の読み取り用に必要だが、execute.yml と close.yml では使用されない。最小権限の原則に基づけば除外すべき。ただし、Claude が内部的にファイル内容確認に `cat` を使う可能性があり、`Read` ツールで代替可能であるため実害は小さい
- **推奨対策**: execute.yml と close.yml の permissions から `Bash(cat *)` を除外する

#### 実施ワーカー未転記課題
- **件数**: 0件
- **課題一覧**: 07_issues.md に1件の知見メモがあるが「転記不要 — 当施策内で対応済み」と判断済み
- **対応依頼**: なし

## 評価中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA Action の `prompt:` 入力フィールドではシェルコマンド置換 `$(...)` は展開されない | gha-guideline に追記候補 | `prompt:` フィールドは GHA 式 (`${{ }}`) のみが評価される。シェル展開が必要な場合は事前の Shell ステップで変数化し `${{ steps.*.outputs.* }}` で参照するか、Claude に `Bash` ツールでファイル読み取りを指示する。このパターンを gha-guideline のチェックリスト（§4 または新セクション）に追加することで、同種の問題を予防できる |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | initiative ワークフロー群のラベルフローは状態遷移として一貫しており、`execute.yml` が `/approve` と `/reject` の両パスを処理する設計は再利用性が高い | `initiative-start` → `initiative:wallbashing` → `initiative:executing` → `initiative:gate-review` → `initiative:completed` の状態遷移がラベルで可視化される。reject 時のループバックも execute.yml 内で完結しており、ワークフロー数を最小限に抑えている |
| 2 | PR 検索の `body contains #<Issue番号>` パターンは、PR 本文にリンクを書く規約と組み合わせることで Issue-PR 紐づけを実現しているが、同一 Issue 番号を含む無関係な PR があると誤マッチする可能性がある | 現時点では initiative ワークフローが PR を作成する唯一の経路であるため問題は小さいが、将来的にリポジトリ内の PR 数が増えた場合はブランチ名規約（`initiative/<施策名>`）との組み合わせで検索精度を上げることを検討すべき |

## 次フェーズへの推奨

**条件付きで進めるべき**

課題1（`$(cat /tmp/issue_body.txt)` の展開問題）は壁打ちフェーズの入力品質に影響するため、ゲート判定前に修正することを推奨する。ただし、Claude が `Bash(cat *)` 権限で自発的にファイルを読む可能性があり、完全に機能しないわけではないため、修正を次施策に回してゲート通過とすることもL1の判断として許容される。

課題2（docs/workflow.md 未更新）と課題3（execute/close の `Bash(cat *)` 権限）は低リスクであり、ゲート通過の阻害要因にはならない。

---
**作成者**: L2（評価）
**作成日**: 2026-03-14
