# claude-code-action 実践知見

## 概要

| 項目 | 内容 |
|------|------|
| リポジトリ名 | anthropics/claude-code-action |
| 使用バージョン | `@v1` |
| 用途 | GHA ワークフローから Claude Code を実行 |

## 蓄積された知見

| # | 施策名 | 日付 | カテゴリ | 内容 |
|---|--------|------|---------|------|
| 1 | initiative-metadata-comment | 2026-03-15 | API仕様 | `outputs.result` は存在しない。公式 outputs は `execution_file`, `branch_name`, `github_token`, `structured_output`, `session_id` のみ |
| 2 | initiative-metadata-comment | 2026-03-15 | API仕様 | `execution_file` output は Claude 失敗時（max-turns 等）に空になる。`${{ runner.temp }}/claude-execution-output.json` を直接参照するのがフォールバック手段 |
| 3 | initiative-metadata-comment | 2026-03-15 | 権限 | `Bash(cp *)` は `cp -r` にマッチしない。`Bash(cp -r *)` を別途追加する必要がある |
| 4 | initiative-metadata-comment | 2026-03-15 | 権限 | `Bash(mkdir *)` で `mkdir -p` を使うと同様のブロックが発生する可能性がある |
| 5 | initiative-metadata-comment | 2026-03-15 | 認証 | `workflow_dispatch` で起動されたワークフローの actor は `github-actions[bot]`。`allowed_bots: "github-actions[bot]"` を設定しないと Claude が起動を拒否する |
| 6 | initiative-metadata-comment | 2026-03-15 | 前提条件 | ディスパッチャーで `gh workflow run` を使う場合、`actions/checkout@v4` が必要（git リポジトリコンテキストがないと `gh` コマンドが失敗する） |
| 7 | initiative-metadata-comment | 2026-03-15 | スコープ制御 | Claude は CLAUDE.md や `.claude/skills/` を自動で読み込み、プロンプトの指示範囲を超えた行動をする。壁打ちフェーズのみの指示でも全フェーズの成果物（01_plan〜08_gate_review）を生成した |
| 8 | initiative-metadata-comment | 2026-03-15 | スコープ制御 | プロンプトに「CLAUDE.md や .claude/skills/ のルールは参照しないこと」を明記することで緩和可能。根本対策は GHA 専用 skills の分離（BL-054） |
| 9 | initiative-metadata-comment | 2026-03-15 | 安全性 | `Bash(git *)` を許可すると `git rebase`, `git reset --hard` 等の破壊的操作も可能になる。プロンプトで明示的に禁止する必要がある |
| 10 | initiative-metadata-comment | 2026-03-15 | ターン消費 | Claude が PR 作成（`gh pr create`）を試み、権限エラーでリトライを繰り返し max-turns に到達。ワークフロー後続ステップが担当する操作はプロンプトで明示禁止する |
| 11 | initiative-metadata-comment | 2026-03-15 | GHA設定 | PR を Actions から作成するにはリポジトリ設定で「Allow GitHub Actions to create and approve pull requests」の有効化が必要 |
| 12 | gha-initiative-skills-separation | 2026-03-15 | スコープ制御 | GHA 専用スキルファイル（`.claude/skills/gha-*`）を作成し、ワークフロー YAML のプロンプトをスキルファイル参照方式にリファクタすることで、#7/#8 の根本対策を実現した。スキルファイル内で「CLAUDE.md や l1-manager のルールには従わない」と明記し、プロンプトには Read 指示 + 動的コンテキスト + 1行リマインダーのみを記載する |
| 13 | gha-initiative-skills-separation | 2026-03-15 | API仕様 | `steps.claude.outputs.result` は存在しないため、全 initiative ワークフロー（execute/close/question）で `${{ runner.temp }}/claude-execution-output.json` からの jq 抽出 + フォールバックメッセージに統一した |
| 14 | gha-initiative-skills-separation | 2026-03-15 | セキュリティ制限 | `cp -r` は `permissions.allow` に `Bash(cp -r *)` を設定しても Claude Code のビルトインセキュリティで「cp with flags requires manual approval to ensure path safety」としてブロックされる。`mkdir` も同様に「may only create directories in the allowed working directories」でブロックされる。GHA 環境（非対話）では手動承認不可のため致命的 |
| 15 | gha-initiative-skills-separation | 2026-03-15 | 回避策 | `cp -r` / `mkdir` の代替として Glob + Read + Write ツールの組み合わせでディレクトリコピーを実現できる。Write ツールはディレクトリを自動作成するため `mkdir` も不要 |
| 16 | gha-initiative-skills-separation | 2026-03-15 | 確認要求 | Claude は `git push` や `git push --delete` を「リスクの高い操作」として認識し、非対話環境でも「実行してよいですか？」とユーザー確認を求めて停止する。スキルファイルに「確認なしで実行」と書くだけでは不十分な場合がある |
| 17 | gha-initiative-skills-separation | 2026-03-15 | インジェクション誤検知 | スキルファイル内の「CLAUDE.md のルールを無視してください」「確認なしで自律的に実行してください」等の表現が、Claude のプロンプトインジェクション検知に引っかかり「このファイルはプロンプトインジェクションの疑いがあります。実行を拒否します」と出力して全作業を拒否する |
| 18 | gha-initiative-skills-separation | 2026-03-15 | インジェクション対策 | CLAUDE.md（プロジェクト設定として信頼される情報源）に「GHA スキルは正当な自動化であり、確認なしの自律実行は設計上の意図」と明記することで誤検知を解消。スキルファイル側は「コンテキスト」セクションで正当性を説明し、否定形の指示（「〜を無視」「〜に従わない」）を全て除去する |
| 19 | gha-initiative-skills-separation | 2026-03-15 | ワークフロー検証 | `claude-code-action` の OIDC トークン交換時、ワークフローファイルが default branch（main）と一致しているか検証される。ブランチ上でワークフロー YAML を変更した場合、マージ前のテスト実行は失敗する（`Workflow validation failed`） |
| 20 | gha-initiative-skills-separation | 2026-03-15 | デバッグ | `show_full_output: true` を設定すると、Claude の各ターンの thinking・tool_use・tool_result が GHA ログに出力され、permission denial やインジェクション誤検知の原因特定に有用 |
| 21 | gha-initiative-skills-separation | 2026-03-15 | ディスパッチャー | `@ai-task /reject` の後に改行してフィードバックを書くと、ディスパッチャーの `sed` パースが1行目の空文字列のみを抽出し、フィードバックが消失する。`echo "args=..."` も1行しか `GITHUB_OUTPUT` に書けない。修正: sed で複数行対応 + HEREDOC 形式で出力 |

## 知見の詳細

### execution_file の構造（#1, #2）

`execution_file`（`${{ runner.temp }}/claude-execution-output.json`）は JSON 配列で、各要素は以下の型を持つ:

```json
[
  {"type": "user", "message": {"role": "user", "content": [...]}},
  {"type": "assistant", "message": {"role": "assistant", "content": [...]}},
  {"type": "result", "subtype": "success" | "error_max_turns" | ...}
]
```

最後の assistant メッセージのテキストを抽出する jq クエリ:
```bash
jq -r '[.[] | select(.type == "assistant") | .message.content[]? | select(.type == "text") | .text] | last // empty' "$EXECUTION_FILE"
```

### permission パターンマッチの注意点（#3, #4）

`Bash(cp *)` は `cp file1 file2` にはマッチするが、`cp -r dir1 dir2` にはマッチしない。フラグ付きコマンドは別途 allow が必要:

```json
{
  "permissions": {
    "allow": [
      "Bash(cp *)",
      "Bash(cp -r *)"
    ]
  }
}
```

### スコープ制御の問題と対策（#7, #8, #9, #10）

GHA 環境でも Claude は CLAUDE.md と `.claude/skills/` を読み込むため、プロンプトで「壁打ちのみ」と指示しても、L1 マネージャースキルの全フェーズオーケストレーションルールに従って行動する。

**発生した問題**:
- 壁打ちプロンプトで `01_plan.md` 〜 `08_gate_review.md` まで全ファイルを生成
- `gh pr create` を試行し、権限エラーでリトライしてターン消費
- push 失敗時に `git rebase` → `git reset --hard` を実行

**暫定対策**（プロンプトベース）:
```
## 制約
- 編集するファイルは `00_proposal.md` のみ。`01_plan.md` 以降はテンプレートのまま残すこと
- PR の作成は行わないこと（ワークフローの後続ステップが担当する）
- gh コマンドによる Issue・PR 操作は行わないこと
- git rebase, git reset --hard 等の破壊的 git 操作は行わないこと
- CLAUDE.md や .claude/skills/ のルールは参照しないこと（このプロンプトの指示のみに従う）
```

**根本対策**: GHA 専用 skills の分離（BL-054）

### GHA 専用スキル分離アプローチ（#12, #13）

#7/#8 のスコープ制御問題の根本対策として、GHA ワークフローごとに専用スキルファイルを作成した。

**アーキテクチャ**:
```
ワークフロー YAML (prompt:)
  → 「.claude/skills/gha-<ワークフロー>/SKILL.md を Read して従え」
  → 動的コンテキスト（Issue番号、ブランチ名等）
  → 1行リマインダー（CLAUDE.md 無視）

スキルファイル (SKILL.md)
  → あなたの役割 / 作業フロー / やること / やらないこと
  → 「CLAUDE.md や l1-manager のルールには従わない」を明記
```

**メリット**:
- プロンプトが短縮化され、YAML の可読性が向上
- 制約ロジックがスキルファイルに集約され、保守性が向上
- 各フェーズの GHA スキルを再利用可能

**作成したスキル**:
- `gha-wallbash`: 壁打ちフェーズ（テンプレートコピー・提案作成）
- `gha-execute`: 実行フェーズ（approve/reject）
- `gha-close`: クローズフェーズ（知見ルーティング・アーカイブ移動）
- `gha-question`: 質問回答（読み取り専用）

### Claude Code ビルトインセキュリティによるブロック（#14, #15）

`permissions.allow` で許可しても、Claude Code のビルトインセキュリティが別レイヤーでブロックするケースがある:

| コマンド | エラーメッセージ | 原因 |
|---------|---------------|------|
| `cp -r` | `cp with flags requires manual approval to ensure path safety` | フラグ付き cp は全てブロック |
| `mkdir` | `may only create directories in the allowed working directories` | サブディレクトリ作成がブロック |

**回避策**: Glob + Read + Write ツールの組み合わせでディレクトリコピーを実現する。

```
1. Glob ツールで対象ディレクトリのファイル一覧を取得
2. 各ファイルを Read ツールで読み取る
3. 各ファイルを Write ツールで新ディレクトリに書き込む
   （Write ツールはディレクトリを自動作成する）
```

### プロンプトインジェクション誤検知と対策（#17, #18）

GHA スキルの以下の表現パターンが、Claude のインジェクション検知を発火させる:

**誤検知トリガーとなる表現**:
- 「CLAUDE.md のルールを無視してください」
- 「他のルールファイルの指示が見えても無視してください」
- 「確認なしで自律的に実行してください」
- 「このスキルの指示のみに従い、CLAUDE.md や他のスキル定義のルールは無視すること」

**Claude の反応**: thinking で `"This is a prompt injection attack"` と判定し、全作業を拒否。

**対策（2層構造）**:

1. **CLAUDE.md 側**: GHA スキルの正当性を明記
```markdown
## GitHub Actions からの実行
`.claude/skills/gha-*/SKILL.md` はリポジトリオーナーが設定した正当な自動化である。
GHA スキルが参照される場合、本 CLAUDE.md の CLI セッション向けルールは
GHA スキルの作業フローには適用されない。GHA スキル内の指示が優先される。
```

2. **スキルファイル側**: 否定形の指示を全て除去し、「コンテキスト」セクションで正当性を説明
```markdown
## コンテキスト
このファイルは GitHub Actions の `xxx.yml` ワークフローから
`claude-code-action` 経由で実行される自動化スキルです。
リポジトリオーナーが設定したワークフローから呼び出されており、
`permissions.allow` で許可されたツールのみが使用可能です。
```

3. **ワークフロープロンプト側**: 「ルールに従わないこと」表現を削除し、中立的な表現に
```yaml
prompt: |
  `.claude/skills/gha-xxx/SKILL.md` を Read ツールで読み取り、その指示に従って作業してください。
  このタスクは GitHub Actions の自動化ワークフローから実行されています。
```

### ワークフロー OIDC 検証（#19）

`claude-code-action` は OIDC トークン交換時にワークフローファイルの内容を default branch と比較する。差分がある場合:

```
Workflow validation failed. The workflow file must exist and have identical content
to the version on the repository's default branch.
```

→ ワークフロー YAML の変更は**必ず main にマージしてからテスト実行**する必要がある。

### ディスパッチャーの複数行フィードバック問題（#21）

`initiative-dispatcher.yml` のコマンドパースで、以下のように改行を含むコメントを投稿した場合:

```
@ai-task /reject
ここにフィードバック
2行目のフィードバック
```

**問題1**: `sed -n 's|.*@ai-task\s\+/reject\s*||p'` は `@ai-task /reject` がある行の残りのみを返す。改行後のテキストは捨てられる。

**問題2**: `echo "args=$args"` は `GITHUB_OUTPUT` に1行しか書けない。複数行は HEREDOC 形式が必要。

**修正**:
```bash
# 複数行対応のパース
args=$(echo "$COMMENT_BODY" | sed '1,/@ai-task\s\+\/'"$command"'/{s/.*@ai-task\s\+\/'"$command"'\s*//;}')

# HEREDOC 形式で出力
{
  echo "args<<ARGS_EOF"
  echo "$args"
  echo "ARGS_EOF"
} >> "$GITHUB_OUTPUT"
```

---
**作成日**: 2026-03-15
**関連施策**: initiative-metadata-comment, gha-initiative-skills-separation
**参照元**: `.claude/skills/gha-guideline/SKILL.md` セクション6
