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

---
**作成日**: 2026-03-15
**関連施策**: initiative-metadata-comment
**参照元**: `.claude/skills/gha-guideline/SKILL.md` セクション6
