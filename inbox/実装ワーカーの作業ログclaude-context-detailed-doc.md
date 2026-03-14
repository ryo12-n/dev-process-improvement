# Claude Context Manager 詳細ドキュメント

> **対象ディレクトリ**: `tools/claude-context/`
> **リポジトリ**: `newproduct-registry` (develop ブランチ)
> **作成日**: 2026-03-14

---

## 1. 概要

Claude Context Manager は、**Claude Code でのPR作業コンテキストをブランチ単位で自動管理**するツールです。

### 1.1 解決する課題

| 課題 | 解決方法 |
|---|---|
| Claude Code のセッション終了で会話が失われる | 変更のたびにコンテキストファイルへ自動追記 |
| ブランチ切替時にコンテキストが混ざる | ブランチごとに独立したコンテキストファイルを管理 |
| 作業中断・再開時に状況説明が必要 | セッション開始時に前回のコンテキストを CLAUDE.md に自動復元 |

### 1.2 全体フロー

```
Claude Code で Edit/Write 操作
  ↓ PostToolUse Hook 発火
  ↓
context-saver.py（Claude Haiku API で変更差分を1行要約）
  ↓
~/.claude/contexts/<project-hash>/<branch>.md に自動追記
  ↓
CLAUDE.md に反映 → 次回セッション開始時に自動読み込み

ブランチ切替時（git checkout）
  ↓ post-checkout フック
  ↓
旧ブランチのコンテキスト保存 → 新ブランチのコンテキスト復元
```

### 1.3 ファイル構成

```
tools/claude-context/
├── README.md                  # プロジェクトの説明（使い方・セットアップ）
├── install.sh                 # セットアップスクリプト
├── scripts/
│   ├── context-saver.py       # 自動要約スクリプト（Hook から呼ばれるコアロジック）
│   └── claude-context.sh      # コンテキスト管理 CLI
├── commands/
│   └── save-context.md        # /project:save-context スラッシュコマンド定義
└── templates/
    └── context-template.md    # 新ブランチ用テンプレート

~/.claude/（インストール後に生成）
├── scripts/
│   ├── context-saver.py
│   └── claude-context.sh
├── commands/
│   └── save-context.md
├── templates/
│   └── context-template.md
├── contexts/
│   └── <project-hash>/
│       ├── <branch-name>.md   # ブランチごとのコンテキスト
│       └── .last_save         # デバウンス用タイムスタンプ
└── settings.json              # Claude Code Hook 設定
```

---

## 2. `install.sh` — セットアップスクリプト

### 2.1 概要

リポジトリルートで `bash tools/claude-context/install.sh` を実行すると、4段階のセットアップを行います。

### 2.2 処理フロー詳細

#### ステップ 0: 初期化

```bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"       # install.sh 自身のディレクトリ
CLAUDE_DIR="$HOME/.claude"                          # ~/.claude
PROJECT_ROOT="$(git rev-parse --show-toplevel ...)" # git リポジトリルートを取得
```

- `set -euo pipefail`: エラー時即座に停止、未定義変数使用禁止、パイプ中のエラー検出
- git リポジトリ外で実行するとエラー終了

#### ステップ 1: スクリプト類のコピー

```bash
mkdir -p "$CLAUDE_DIR/scripts" "$CLAUDE_DIR/templates" "$CLAUDE_DIR/commands" "$CLAUDE_DIR/contexts"
cp scripts/context-saver.py   → ~/.claude/scripts/context-saver.py
cp scripts/claude-context.sh  → ~/.claude/scripts/claude-context.sh  (実行権限付与)
cp templates/context-template.md → ~/.claude/templates/context-template.md
cp commands/save-context.md    → ~/.claude/commands/save-context.md
```

`~/.claude/` 配下に必要なディレクトリを作成し、ツール内のファイルをコピーします。

#### ステップ 2: `settings.json` に Hook 設定を追加

Claude Code の Hook 機能を使い、特定イベント時に `context-saver.py` を自動実行する設定を追加します。

**3つの場合分け:**

| 条件 | 処理 |
|---|---|
| `settings.json` が存在しない | 新規作成（Hook 設定を含む JSON を書き出し） |
| `settings.json` に `"hooks"` キーが未存在 | Python で既存 JSON を読み込み、`hooks` キーをマージして書き戻し |
| `settings.json` に `"hooks"` キーが既に存在 | スキップ（手動確認を促すメッセージ表示） |

**設定される Hook:**

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python \"$HOME/.claude/scripts/context-saver.py\""
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python \"$HOME/.claude/scripts/context-saver.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python \"$HOME/.claude/scripts/context-saver.py\""
          }
        ]
      }
    ]
  }
}
```

- **SessionStart**: セッション開始時（matcher 空 = 全マッチ）
- **PostToolUse**: Edit / Write / MultiEdit ツール使用後
- **Stop**: セッション終了時

いずれも同じ `context-saver.py` を呼び出しますが、スクリプト内でイベント種別に応じた処理を分岐します。

#### ステップ 3: git post-checkout フックのインストール

```bash
"$CLAUDE_DIR/scripts/claude-context.sh" install
```

`claude-context.sh` の `install` コマンドを呼び出し、`.git/hooks/post-checkout` にフックスクリプトを設置します（詳細は後述の `claude-context.sh` セクションを参照）。

#### ステップ 4: `.gitignore` の更新

```bash
for pattern in "CLAUDE.md" "CLAUDE_BASE.md"; do
    # .gitignore に未登録であれば追記
done
```

`CLAUDE.md` と `CLAUDE_BASE.md` をコミット対象外にするため `.gitignore` に追加します（既に含まれていればスキップ）。

---

## 3. `scripts/context-saver.py` — 自動要約エンジン（コアロジック）

### 3.1 概要

Claude Code の Hook から呼び出される Python スクリプトです。標準入力から Hook のイベント情報（JSON）を受け取り、Claude Haiku API で変更を要約してコンテキストファイルに追記します。

### 3.2 依存関係

- Python 3.8+
- `anthropic` パッケージ（Claude API クライアント）
- `httpx`（プロキシ対応の HTTP クライアント、`anthropic` の依存）

### 3.3 設定定数

```python
CLAUDE_DIR = Path.home() / ".claude"
CONTEXTS_DIR = CLAUDE_DIR / "contexts"
TEMPLATES_DIR = CLAUDE_DIR / "templates"
DEBOUNCE_FILE = CLAUDE_DIR / "contexts" / ".last_save"
DEBOUNCE_SECONDS = 30
DEFAULT_MODEL = "claude-haiku-4-5-20251001"
```

### 3.4 ヘルパー関数

#### `get_api_key()`
環境変数 `ANTHROPIC_API_KEY` を返す。未設定なら空文字。

#### `get_model()`
環境変数 `CLAUDE_CONTEXT_MODEL` を返す。未設定なら `claude-haiku-4-5-20251001`。

#### `get_proxy()`
プロキシ URL を以下の優先順で返す:
1. `HTTPS_PROXY`
2. `HTTP_PROXY`
3. `CLAUDE_CONTEXT_PROXY`
4. 空文字（プロキシなし）

#### `get_git_info()`
```python
def get_git_info():
    branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip()
    root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip()
    return branch, root
```
現在のブランチ名とプロジェクトルートパスを取得。git リポジトリ外の場合は `(None, None)` を返す。

#### `get_project_hash(project_root)`
```python
def get_project_hash(project_root):
    return hashlib.md5(project_root.encode()).hexdigest()[:12]
```
プロジェクトルートパスの MD5 ハッシュ先頭12文字を返す。これによりプロジェクトごとにコンテキストディレクトリを分離。

#### `get_project_name(project_root)`
パスの末尾ディレクトリ名を返す（例: `/home/user/myproject` → `myproject`）。

#### `get_context_path(project_hash, branch)`
```python
def get_context_path(project_hash, branch):
    safe_branch = branch.replace("/", "__")  # feature/xxx → feature__xxx
    project_dir = CONTEXTS_DIR / project_hash
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir / f"{safe_branch}.md"
```
ブランチ名の `/` を `__` に置換し、`~/.claude/contexts/<hash>/<branch>.md` のパスを返す。

#### `should_debounce(file_path)`
```python
def should_debounce(file_path):
    # .last_save ファイルから前回保存の情報を読み取り
    # 同一ファイルへの保存が30秒以内であれば True を返す
```
同じファイルに対する連続編集で API を無駄に呼ばないためのデバウンス判定。`.last_save` ファイルに `{"file_path": "...", "timestamp": 1234567890}` 形式で記録。

#### `update_debounce(file_path)`
デバウンス情報を `.last_save` ファイルに書き込む。

#### `call_claude_api(prompt, api_key, model)`
```python
def call_claude_api(prompt, api_key, model):
    import anthropic
    import httpx

    proxy_url = get_proxy()
    http_client = httpx.Client(proxy=proxy_url) if proxy_url else None

    client = anthropic.Anthropic(api_key=api_key, http_client=http_client)
    response = client.messages.create(
        model=model,
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text
```
Claude API（Haiku）に要約リクエストを送信。プロキシ設定がある場合は `httpx.Client` 経由で接続。`max_tokens=300` で短い応答に制限。

### 3.5 プロンプト構築: `build_summary_prompt()`

イベント種別に応じて2パターンのプロンプトを生成:

**パターン1: Stop / SessionEnd イベント**
```
Project: {project_name}, Branch: {branch}
The user's Claude Code session has just ended or paused.
Current context:
{existing_context}

Based on the context above, write a brief 1-2 line summary of the current state
that would help someone resuming this work. Focus on what was being worked on and
any next steps. If the context already captures this well, respond with just: NO_UPDATE
```

**パターン2: PostToolUse イベント（Edit/Write/MultiEdit）**

ツール種別で変更内容の記述を分岐:
- **Edit**: `Edited {file_path}: Before: {old_string[:200]} After: {new_string[:200]}`
- **Write**: `Created/wrote {file_path}: Content preview: {content[:300]}`
- **その他**: `Used {tool_name} on {file_path}`

```
Project: {project_name}, Branch: {branch}
Change: {change_desc}
Current context:
{existing_context}

Write a brief 1-line log entry summarizing this change for a developer resuming work later.
Format: `- [YYYY-MM-DD HH:MM] <summary>`.
If this change is trivial or already captured in the context, respond with just: NO_UPDATE
```

`NO_UPDATE` レスポンスにより、重複・自明な変更の記録を抑制。

### 3.6 テンプレート初期化: `create_initial_context()`

```python
def create_initial_context(branch, project_name):
    template_path = TEMPLATES_DIR / "context-template.md"
    if template_path.exists():
        template = template_path.read_text(encoding="utf-8")
    else:
        template = "（ハードコードされたデフォルトテンプレート）"
    return template
        .replace("{{BRANCH_NAME}}", branch)
        .replace("{{PROJECT_NAME}}", project_name)
        .replace("{{DATE}}", time.strftime("%Y-%m-%d"))
```

テンプレートファイルが存在すればそれを使用し、なければコード内のデフォルトテンプレートを使用。プレースホルダー3つを実際の値に置換。

### 3.7 CLAUDE.md 同期: `_sync_claude_md()`

```python
def _sync_claude_md(claude_md_path, branch_context, project_root):
    # 1. CLAUDE_BASE.md があればその内容を先頭に配置
    base_path = Path(project_root) / "CLAUDE_BASE.md"
    base_content = base_path.read_text() + "\n\n---\n\n"  # あれば

    # 2. セパレータ "<!-- BRANCH_CONTEXT_START -->" を使って分離
    separator = "<!-- BRANCH_CONTEXT_START -->"

    # 3. 既存 CLAUDE.md にセパレータがあればその部分だけ置換
    #    なければ末尾に追加
    # 4. ファイルに書き出し
```

**CLAUDE.md の構造:**
```
[CLAUDE_BASE.md の内容（あれば）]

---

<!-- BRANCH_CONTEXT_START -->
[ブランチ固有のコンテキスト]
```

`CLAUDE_BASE.md` はプロジェクト共通の指示（全ブランチ共通）を書く場所。セパレータ以降がブランチ切替時に差し替わる部分。

### 3.8 メイン処理: `main()`

```python
def main():
    # 1. 標準入力から Hook イベント JSON を読み取り
    hook_input = json.loads(sys.stdin.read())

    # 2. API キーチェック（未設定なら何もせず終了）
    api_key = get_api_key()
    if not api_key:
        sys.exit(0)

    # 3. イベント情報を取得
    event_name = hook_input.get("hook_event_name", "")  # "SessionStart" / "PostToolUse" / "Stop"
    tool_name = hook_input.get("tool_name", "")          # "Edit" / "Write" / "MultiEdit"
    tool_input = hook_input.get("tool_input", {})        # {"file_path": ..., "old_string": ..., ...}

    # 4. git 情報取得
    branch, project_root = get_git_info()

    # 5. プロジェクトハッシュ・名前を算出
    project_hash = get_project_hash(project_root)
    project_name = get_project_name(project_root)

    # === イベント別分岐 ===

    # 6a. SessionStart: コンテキスト読み込み → CLAUDE.md に反映（API 呼び出しなし）
    if event_name == "SessionStart":
        context_path = get_context_path(project_hash, branch)
        if context_path.exists():
            context = context_path.read_text()
        else:
            context = create_initial_context(branch, project_name)
            context_path.write_text(context)
        _sync_claude_md(claude_md_path, context, project_root)
        sys.exit(0)

    # 6b. PostToolUse: デバウンスチェック
    if event_name == "PostToolUse":
        file_path = tool_input.get("file_path", "")
        if should_debounce(file_path):
            sys.exit(0)  # 30秒以内の同一ファイル編集はスキップ
        update_debounce(file_path)

    # 7. 既存コンテキスト読み込み（なければテンプレートから初期化）
    context_path = get_context_path(project_hash, branch)
    existing_context = context_path.read_text() if context_path.exists() else create_initial_context(...)

    # 8. Claude Haiku API で要約生成
    prompt = build_summary_prompt(event_name, tool_name, tool_input, existing_context, ...)
    summary = call_claude_api(prompt, api_key, model)

    # 9. "NO_UPDATE" なら何もしない
    if "NO_UPDATE" in summary:
        sys.exit(0)

    # 10. コンテキストファイルの「## 進捗ログ」セクションに要約を追記
    marker = "## 進捗ログ"
    if marker in existing_context:
        # marker を起点に分割し、次の "## " セクション見出しの直前に追記
        # 進捗ログセクションの末尾に summary を挿入
    else:
        # marker がなければファイル末尾に追記

    # 11. コンテキストファイルに書き戻し
    context_path.write_text(updated)

    # 12. CLAUDE.md に同期
    _sync_claude_md(claude_md_path, updated, project_root)
```

#### 進捗ログへの追記ロジック詳細

```python
marker = "## 進捗ログ"
if marker in existing_context:
    parts = existing_context.split(marker, 1)  # marker の前後に分割
    rest = parts[1]                             # marker 以降の内容
    next_section_idx = rest.find("\n## ")       # 次のセクション見出しの位置

    if next_section_idx != -1:
        # 進捗ログと次のセクションの間に要約を挿入
        log_section = rest[:next_section_idx]
        after_section = rest[next_section_idx:]
        updated = parts[0] + marker + log_section.rstrip() + "\n" + summary.strip() + "\n" + after_section
    else:
        # 進捗ログがファイル末尾のセクションの場合、末尾に追記
        updated = parts[0] + marker + rest.rstrip() + "\n" + summary.strip() + "\n"
else:
    # marker なし → ファイル末尾に追記
    updated = existing_context.rstrip() + "\n\n" + summary.strip() + "\n"
```

この処理により、テンプレートのセクション構造（目的 → スコープ → 進捗ログ → 決定事項 → メモ）を壊さずに進捗ログだけが成長していく。

---

## 4. `scripts/claude-context.sh` — CLI ツール

### 4.1 概要

ブランチコンテキストの手動管理とgit hookインストールを行うシェルスクリプト。

### 4.2 ヘルパー関数

| 関数 | 処理 |
|---|---|
| `get_branch()` | `git rev-parse --abbrev-ref HEAD` で現在のブランチ名を取得 |
| `get_project_root()` | `git rev-parse --show-toplevel` でプロジェクトルートを取得 |
| `get_project_hash()` | パスの `md5sum` 先頭12文字を算出（Python 版と同一ロジック） |
| `get_project_name()` | `basename` でディレクトリ名を取得 |
| `safe_branch_name()` | `/` を `__` に置換（`sed 's\|/\|__\|g'`） |
| `get_context_path()` | `$CONTEXTS_DIR/$project_hash/$safe_branch.md` のパスを返す |
| `ensure_dirs()` | コンテキストディレクトリを `mkdir -p` |
| `create_from_template()` | テンプレートファイルから `sed` でプレースホルダーを置換して出力 |

### 4.3 `sync_claude_md()` — CLAUDE.md 同期

```bash
sync_claude_md() {
    local project_root="$1"
    local context_content="$2"
    local claude_md="$project_root/CLAUDE.md"
    local base_md="$project_root/CLAUDE_BASE.md"
    local separator="<!-- BRANCH_CONTEXT_START -->"

    # 1. CLAUDE_BASE.md があればその内容を先頭に
    # 2. 既存 CLAUDE.md にセパレータがあれば、セパレータ以降を新しいコンテキストで置換
    # 3. セパレータがなければ既存内容の末尾に追加
    # 4. CLAUDE.md に書き出し
}
```

Python 版 `_sync_claude_md()` と同一ロジックのシェル実装。

### 4.4 コマンド詳細

#### `save` — コンテキスト保存

```bash
cmd_save() {
    # --branch オプション対応（post-checkout hook から旧ブランチ名を明示的に渡すため）
    if [ "${1:-}" = "--branch" ] && [ -n "${2:-}" ]; then
        branch="$2"
    else
        branch=$(get_branch)
    fi

    # CLAUDE.md からセパレータ以降を抽出してコンテキストファイルに保存
    if grep -q "$separator" "$claude_md"; then
        sed -n "/$separator/,\$p" "$claude_md" | tail -n +2 > "$context_path"
    else
        cp "$claude_md" "$context_path"
    fi
}
```

- `--branch` オプション: post-checkout フックから呼ばれる際、既にブランチが切り替わった後なので旧ブランチ名を引数で受け取る
- CLAUDE.md のセパレータ `<!-- BRANCH_CONTEXT_START -->` 以降のみをコンテキストとして保存
- セパレータがなければ CLAUDE.md 全体をコピー

#### `load` — コンテキスト読み込み

```bash
cmd_load() {
    # 保存済みコンテキストがあれば読み込み
    if [ -f "$context_path" ]; then
        context_content=$(cat "$context_path")
    else
        # なければテンプレートから新規作成して保存
        context_content=$(create_from_template "$branch" "$project_name")
        echo "$context_content" > "$context_path"
    fi

    # CLAUDE.md に同期
    sync_claude_md "$project_root" "$context_content"
}
```

#### `switch <branch>` — ブランチ切替

```bash
cmd_switch() {
    cmd_save            # 現在ブランチのコンテキストを保存
    git checkout "$1"   # ブランチ切替
    cmd_load            # 新ブランチのコンテキストを読み込み
}
```

save → checkout → load を一括実行するショートカット。

#### `list` — コンテキスト一覧

```bash
cmd_list() {
    # ~/.claude/contexts/<project-hash>/*.md を列挙
    for f in "$project_dir"/*.md; do
        name=$(basename "$f" .md | sed 's|__|/|g')  # __ を / に戻して表示
        mod_time=$(date -r "$f" "+%Y-%m-%d %H:%M")
        marker=""
        if [ "$name" = "$current_branch" ]; then
            marker=" (current)"
        fi
        echo "  $name  [$mod_time]$marker"
    done
}
```

保存済みコンテキストをブランチ名・最終更新日時とともに表示。現在ブランチには `(current)` マーカーを付与。

#### `status` — 状態表示

```bash
cmd_status() {
    echo "Project:  $(get_project_name)"
    echo "Branch:   $branch"
    echo "Context:  $context_path"
    echo "Status:   Saved (last updated: $mod_time)"  # or "No context saved"
    echo "CLAUDE.md: exists"                            # or "not found"
}
```

#### `install` — post-checkout フックのインストール

```bash
cmd_install() {
    local hook_file="$project_root/.git/hooks/post-checkout"

    # 既存フックがある場合:
    #   - "claude-context.sh" が含まれていれば何もしない（重複防止）
    #   - 含まれていなければ末尾に追記

    # 既存フックがない場合:
    #   - 新規作成して実行権限を付与
}
```

**インストールされる post-checkout フックの内容:**

```bash
#!/bin/bash
PREV_HEAD=$1       # チェックアウト前の HEAD コミット
NEW_HEAD=$2        # チェックアウト後の HEAD コミット
BRANCH_FLAG=$3     # 1=ブランチ切替、0=ファイルチェックアウト

if [ "$BRANCH_FLAG" = "1" ]; then
    # 旧ブランチ名を PREV_HEAD から逆引き
    OLD_BRANCH=$(git name-rev --name-only --refs='refs/heads/*' "$PREV_HEAD" | sed 's|^refs/heads/||')

    if [ -n "$OLD_BRANCH" ] && [ "$OLD_BRANCH" != "undefined" ]; then
        # 旧ブランチのコンテキストを保存
        claude-context.sh save --branch "$OLD_BRANCH"
    fi

    # 新ブランチのコンテキストを読み込み
    claude-context.sh load
fi
```

- `BRANCH_FLAG=1` のときのみ動作（ファイル単位のチェックアウトでは動作しない）
- `git name-rev` で PREV_HEAD からブランチ名を逆引きし、旧ブランチのコンテキストを保存
- その後、新ブランチのコンテキストを CLAUDE.md に読み込み

---

## 5. `commands/save-context.md` — スラッシュコマンド定義

### 5.1 概要

Claude Code 内で `/project:save-context` と入力すると実行されるコマンドのプロンプト定義。

### 5.2 内容

```markdown
現在の作業状況を要約し、プロジェクトルートの CLAUDE.md の以下のセクションを更新してください：

- **進捗ログ**: 完了したタスク、未完了のタスク、現在の状態を箇条書きで追記
- **決定事項**: 採用したアプローチや設計判断を記録
- **メモ**: 次回再開時に知っておくべき情報（ブロッカー、TODO、注意点）

以下は含めないでください：
- 権限承認のやり取り
- ファイルの単純な閲覧操作

既存の内容は上書きせず、追記・更新する形で行ってください。
```

### 5.3 使用場面

自動保存（`context-saver.py`）では拾いきれない以下の情報を手動で記録する:
- 設計判断の背景・理由
- 特定のアプローチを選んだ理由
- ブロッカーや次回作業のTODO
- 注意事項やメモ

---

## 6. `templates/context-template.md` — コンテキストテンプレート

### 6.1 内容

```markdown
# PR Context: {{BRANCH_NAME}}
Project: {{PROJECT_NAME}}
Created: {{DATE}}

## 目的
（このPRで何を達成するか）

## スコープ
（変更対象のファイル・機能）

## 進捗ログ
<!-- context-saver.py が自動追記 -->

## 決定事項

## メモ
```

### 6.2 プレースホルダー

| プレースホルダー | 置換内容 |
|---|---|
| `{{BRANCH_NAME}}` | 現在のブランチ名（例: `feature/add-login`） |
| `{{PROJECT_NAME}}` | プロジェクト名（ディレクトリ名） |
| `{{DATE}}` | 作成日（`YYYY-MM-DD` 形式） |

### 6.3 セクションの役割

| セクション | 記入者 | 説明 |
|---|---|---|
| 目的 | 手動 or スラッシュコマンド | PRの目標 |
| スコープ | 手動 or スラッシュコマンド | 変更対象の範囲 |
| 進捗ログ | `context-saver.py` が自動追記 | 変更の1行要約が時系列で蓄積 |
| 決定事項 | スラッシュコマンド | 設計判断の記録 |
| メモ | スラッシュコマンド | 次回作業への申し送り |

### 6.4 カスタマイズ

`~/.claude/templates/context-template.md` を直接編集することで、テンプレートをカスタマイズ可能。

---

## 7. 環境変数一覧

| 変数名 | 必須 | デフォルト | 説明 |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | はい | — | Anthropic API キー。未設定時は自動保存が全スキップ |
| `CLAUDE_CONTEXT_MODEL` | いいえ | `claude-haiku-4-5-20251001` | 要約に使用するモデル |
| `CLAUDE_CONTEXT_PROXY` | いいえ | — | プロキシ URL（`HTTPS_PROXY` / `HTTP_PROXY` が優先） |
| `HTTPS_PROXY` | いいえ | — | HTTPS プロキシ（最優先） |
| `HTTP_PROXY` | いいえ | — | HTTP プロキシ |

---

## 8. コスト・パフォーマンス

| 項目 | 詳細 |
|---|---|
| 使用モデル | `claude-haiku-4-5-20251001`（最安） |
| 1回あたりトークン | 入力 ~500、出力 ~50 |
| デバウンス | 同一ファイル30秒以内の連続編集はスキップ |
| NO_UPDATE 判定 | 重複・自明な変更は API レスポンスで記録スキップ |
| API キー未設定時 | サイレントスキップ（通常の Claude Code 利用に影響なし） |
| エラーハンドリング | API 呼び出し失敗時もサイレントスキップ（`sys.exit(0)`） |

---

## 9. データフロー図（総合）

```
┌─────────────────────────────────────────────────────────┐
│                    Claude Code Session                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [SessionStart]                                          │
│       │                                                  │
│       ▼                                                  │
│  context-saver.py (stdin: hook JSON)                     │
│       │                                                  │
│       ├─ contexts/<hash>/<branch>.md 存在?               │
│       │   YES → 読み込み                                 │
│       │   NO  → テンプレートから初期化                    │
│       │                                                  │
│       ▼                                                  │
│  CLAUDE.md に同期（CLAUDE_BASE.md + ブランチコンテキスト）│
│                                                          │
│  [PostToolUse: Edit/Write/MultiEdit]                     │
│       │                                                  │
│       ▼                                                  │
│  context-saver.py (stdin: hook JSON)                     │
│       │                                                  │
│       ├─ デバウンスチェック（同一ファイル30秒以内→スキップ）│
│       │                                                  │
│       ▼                                                  │
│  Claude Haiku API で変更を1行要約                         │
│       │                                                  │
│       ├─ "NO_UPDATE" → スキップ                          │
│       │                                                  │
│       ▼                                                  │
│  「## 進捗ログ」セクションに要約を追記                    │
│       │                                                  │
│       ▼                                                  │
│  CLAUDE.md に同期                                         │
│                                                          │
│  [Stop]                                                  │
│       │                                                  │
│       ▼                                                  │
│  context-saver.py → Haiku API で状態要約 → 追記 → 同期   │
│                                                          │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [git checkout (ブランチ切替)]                            │
│       │                                                  │
│       ▼                                                  │
│  post-checkout hook                                      │
│       │                                                  │
│       ├─ claude-context.sh save --branch <旧ブランチ>    │
│       │   → CLAUDE.md から旧ブランチのコンテキストを抽出  │
│       │   → contexts/<hash>/<旧ブランチ>.md に保存        │
│       │                                                  │
│       ▼                                                  │
│  claude-context.sh load                                  │
│       │                                                  │
│       ├─ contexts/<hash>/<新ブランチ>.md 存在?            │
│       │   YES → 読み込み                                 │
│       │   NO  → テンプレートから新規作成                  │
│       │                                                  │
│       ▼                                                  │
│  CLAUDE.md に同期（新ブランチのコンテキスト）             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```
