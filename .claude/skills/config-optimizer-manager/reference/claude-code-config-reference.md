# Claude Code Configuration Reference

> **Snapshot Date**: 2026-03-15
> **Source**: Claude Code official documentation (code.claude.com/docs/en/)
> **Freshness**: 初回収集。以降はセッション実行ごとに確認。

---

## 1. settings.json Schema

### Configuration Scopes

| Scope | Location | Who it affects | Shared with team? |
|-------|----------|---------------|-------------------|
| Managed | Server-managed settings, plist/registry, or system-level `managed-settings.json` | All users on the machine | Yes (deployed by IT) |
| User | `~/.claude/` directory | You, across all projects | No |
| Project | `.claude/` in repository | All collaborators on this repository | Yes (committed to git) |
| Local | `.claude/settings.local.json` | You, in this repository only | No (gitignored) |

**Precedence**: Managed > Local > Project > User（高い方が優先）

### Supported Fields

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| `$schema` | string | JSON Schema URL for editor validation/autocomplete | - |
| `permissions` | object | Tool access control (allow/deny/ask rules) | `{}` |
| `permissions.allow` | string[] | Auto-approved tool rules | `[]` |
| `permissions.deny` | string[] | Blocked tool rules | `[]` |
| `permissions.ask` | string[] | Rules requiring user confirmation | `[]` |
| `permissions.defaultMode` | string | Default permission mode (`"acceptEdits"`, `"default"`, `"plan"`, `"dontAsk"`, `"bypassPermissions"`) | `"default"` |
| `permissions.disableBypassPermissionsMode` | boolean | Prevent bypassing permissions (managed settings only) | `false` |
| `permissions.additionalDirectories` | string[] | Allow-listed additional directories for context | `[]` |
| `model` | string | Override default model | - |
| `hooks` | object | Lifecycle hook configurations (see §4) | `{}` |
| `env` | object | Environment variables passed to all tool executions | `{}` |
| `sandbox` | object | Bash command sandboxing configuration | `{}` |
| `sandbox.enabled` | boolean | Enable/disable sandboxing | `false` |
| `sandbox.allowUnsandboxedCommands` | boolean | Allow commands outside sandbox | - |
| `sandbox.network.allowedDomains` | string[] | Domains allowed for network access in sandbox | `[]` |
| `enableAllProjectMcpServers` | boolean | Auto-approve all MCP servers in project | `false` |
| `enabledMcpjsonServers` | string[] | Enabled MCP servers | `[]` |
| `disabledMcpjsonServers` | string[] | Disabled MCP servers | `[]` |
| `cleanupPeriodDays` | number | Conversation history retention period | - |
| `attribution` | object | Commit/PR attribution message settings (`commit`, `pr` fields) | - |
| `worktree` | object | git worktree configuration for `--worktree` | - |
| `claudeMdExcludes` | string[] | Glob patterns to exclude specific CLAUDE.md files | `[]` |
| `autoMemoryEnabled` | boolean | Enable/disable auto memory | `true` |
| `autoMemoryDirectory` | string | Custom auto memory storage location | - |
| `outputStyle` | string | Output style configuration | - |
| `skippedMarketplaces` | string[] | Skipped plugin marketplaces | `[]` |
| `skippedPlugins` | string[] | Skipped plugins | `[]` |
| `extraKnownMarketplaces` | object | Team marketplace configuration | `{}` |
| `enabledPlugins` | object | Plugin enablement settings | `{}` |
| `forceLoginMethod` | string | Force specific login method | - |
| `forceLoginOrgUUID` | string | Force specific org UUID for login | - |
| `disableAllHooks` | boolean | Disable all hooks globally | `false` |
| `allowManagedHooksOnly` | boolean | Only allow managed hooks (managed settings only) | `false` |

### Permission Rule Format

Rules follow the format `Tool` or `Tool(specifier)`:
- `Bash(npm test*)` — allow bash commands matching pattern
- `Read(./.env)` — control read access to specific files
- `Edit|Write` — control multiple tools
- `Skill(commit)` — exact skill match
- `Skill(deploy *)` — prefix match with arguments

Evaluation order: deny rules first, then ask, then allow. First matching rule wins.

**Known Issue**: As of v1.0.93, `deny` rules in settings.json were reported as non-functional. Use PreToolUse hooks with exit code 2 as reliable alternative.

---

## 2. Rules (.claude/rules/)

### Rule File Format

- ディレクトリ: `.claude/rules/` にマークダウンファイルを配置
- 再帰的発見: サブディレクトリ内の `.md` ファイルも自動発見される
- ファイル名: descriptive kebab-case（例: `testing.md`, `api-design.md`）。ファイル名はルール動作に影響しない
- ユーザーレベル: `~/.claude/rules/` に個人ルールを配置可能（プロジェクトルールが優先）
- シンボリックリンク: サポート済み。循環参照も検出される

### Path-Scoped Rules

YAML フロントマターで `paths` フィールドを指定すると、特定ファイルにスコープできる:

```yaml
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules
- All API endpoints must include input validation
```

**Glob パターン例:**

| Pattern | Matches |
|---------|---------|
| `**/*.ts` | 全ディレクトリの TypeScript ファイル |
| `src/**/*` | src/ 配下の全ファイル |
| `*.md` | プロジェクトルートの Markdown ファイル |
| `src/components/*.tsx` | 特定ディレクトリの React コンポーネント |
| `src/**/*.{ts,tsx}` | ブレース展開による複数拡張子マッチ |

### Loading Behavior

- `paths` フロントマターなし: 起動時に `.claude/CLAUDE.md` と同じ優先度で読み込まれる
- `paths` フロントマターあり: マッチするファイルを Claude が読んだ時に読み込まれる（遅延読み込み）
- CLAUDE.md の子ディレクトリファイルとは異なり、rules はグロブパターンで精密ターゲティング

### Best Practices

- `CLAUDE.md` は全体に適用するもの（ルーティングロジック、品質基準）に使用。簡潔に保つ
- `rules/` は特定領域に適用するもの（API パターン、テスト要件）に使用
- `@import` で詳細コンテンツを分離ファイルに参照可能
- 短い CLAUDE.md ほど遵守率が高い

---

## 3. Skills (.claude/skills/)

### SKILL.md Format

2つの部分で構成:
1. **YAML フロントマター** (`---` マーカー間): Claude がいつスキルを使うかを設定
2. **マークダウンコンテンツ**: スキル起動時に Claude が従う指示

### Frontmatter Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | スキルの表示名。省略時はディレクトリ名を使用。小文字・数字・ハイフンのみ（最大64文字） |
| `description` | Recommended | スキルの目的と使用タイミング。最大1024文字、XML タグ不可。省略時はマークダウンの最初の段落を使用 |
| `argument-hint` | No | オートコンプリート時に表示されるヒント（例: `[issue-number]`） |
| `disable-model-invocation` | No | `true` でClaude の自動起動を防止。手動 `/name` のみ。デフォルト: `false` |
| `user-invocable` | No | `false` で `/` メニューから非表示。デフォルト: `true` |
| `allowed-tools` | No | スキルアクティブ時に許可なしで使えるツール |
| `model` | No | スキルアクティブ時に使用するモデル |
| `context` | No | `fork` でフォークされたサブエージェントコンテキストで実行 |
| `agent` | No | `context: fork` 時のサブエージェントタイプ（`Explore`, `Plan`, `general-purpose`, またはカスタム） |
| `hooks` | No | スキルライフサイクルにスコープされたフック |

### Description Best Practices

- 単一行文字列を使用（YAML マルチライン指示子 `>-`, `|` は正しくパースされない）
- Claude はスキルを「使わなすぎる」傾向があるため、description は少し「積極的」に書く
- キーワードはユーザーが自然に言うであろう表現を含める

### String Substitutions

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | スキル起動時に渡された全引数 |
| `$ARGUMENTS[N]` / `$N` | N番目の引数（0ベースインデックス） |
| `${CLAUDE_SESSION_ID}` | 現在のセッションID |
| `${CLAUDE_SKILL_DIR}` | SKILL.md を含むディレクトリ |

### Dynamic Context Injection

`` !`command` `` 構文でシェルコマンドを前処理として実行し、出力をプロンプトに挿入:
```yaml
PR diff: !`gh pr diff`
```

### Context Budget

- スキル description はコンテキストに読み込まれ、フルコンテンツは起動時のみ読み込まれる（Progressive Disclosure）
- description の読み込みは約100トークン
- 予算: コンテキストウィンドウの **2%**（フォールバック: 16,000文字）
- `SLASH_COMMAND_TOOL_CHAR_BUDGET` 環境変数でオーバーライド可能
- `/context` で除外されたスキルの警告を確認可能

### Directory Structure

```
my-skill/
├── SKILL.md           # メイン指示（必須）
├── template.md        # テンプレート
├── examples/
│   └── sample.md      # 出力例
├── references/        # 詳細ドキュメント
└── scripts/
    └── helper.py      # 実行可能スクリプト
```

### Skill Locations

| Location | Path | Applies to |
|----------|------|-----------|
| Enterprise | Managed settings | All users in organization |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Where plugin is enabled |

優先順位: enterprise > personal > project

### Invocation Control

| Frontmatter | User can invoke | Claude can invoke | Context loading |
|-------------|----------------|-------------------|----------------|
| (default) | Yes | Yes | Description always, full on invoke |
| `disable-model-invocation: true` | Yes | No | Not in context |
| `user-invocable: false` | No | Yes | Description always, full on invoke |

### Agent Skills Open Standard

Claude Code skills は [Agent Skills](https://agentskills.io) オープン標準に準拠。Claude Code, Cursor, Gemini CLI 等で互換動作。

---

## 4. Hooks

### Hook Event Types (24 events)

#### Session Lifecycle
| Type | Trigger | Matcher Target |
|------|---------|---------------|
| SessionStart | セッション開始/再開 | `startup`, `resume`, `clear`, `compact` |
| SessionEnd | セッション終了 | `clear`, `logout`, `prompt_input_exit`, `other` |
| InstructionsLoaded | CLAUDE.md/rules 読み込み時 | - |

#### User Input
| Type | Trigger | Matcher Target |
|------|---------|---------------|
| UserPromptSubmit | プロンプト処理前 | マッチャー非対応（常に発火） |

#### Tool Execution
| Type | Trigger | Matcher Target |
|------|---------|---------------|
| PreToolUse | ツール実行前（ブロック可） | ツール名（`Bash`, `Edit\|Write`, `mcp__.*`） |
| PostToolUse | ツール成功後 | ツール名 |
| PostToolUseFailure | ツール失敗後 | ツール名 |
| PermissionRequest | 権限ダイアログ表示時 | - |

#### Agent Flow
| Type | Trigger | Matcher Target |
|------|---------|---------------|
| SubagentStart | サブエージェント起動 | エージェントタイプ |
| SubagentStop | サブエージェント完了 | エージェントタイプ |
| Stop | メインエージェント応答完了 | マッチャー非対応（常に発火） |
| TeammateIdle | チームメイトがアイドルへ | - |
| TaskCompleted | タスク完了マーク | - |

#### System Events
| Type | Trigger | Matcher Target |
|------|---------|---------------|
| Notification | 通知送信時 | `permission_prompt`, `idle_prompt`, `auth_success` |
| ConfigChange | 設定ファイル変更時 | `user_settings`, `project_settings`, `policy_settings` |
| PreCompact | コンテキスト圧縮前 | `manual`, `auto` |
| PostCompact | コンテキスト圧縮後 | `manual`, `auto` |
| WorktreeCreate | ワークツリー作成 | - |
| WorktreeRemove | ワークツリー削除 | - |

#### MCP Integration
| Type | Trigger | Matcher Target |
|------|---------|---------------|
| Elicitation | MCP サーバーがユーザー入力要求 | - |
| ElicitationResult | ユーザーが MCP リクエストに応答 | - |

### Three-Level Configuration Structure

```json
{
  "hooks": {
    "PreToolUse": [           // Level 1: Event name
      {
        "matcher": "Bash",    // Level 2: Matcher group (regex)
        "hooks": [            // Level 3: Hook handlers
          {
            "type": "command",
            "command": "/path/to/script.sh",
            "timeout": 600
          }
        ]
      }
    ]
  }
}
```

### Matcher Syntax

- 正規表現文字列（大文字小文字を区別）
- `"Bash"` — Bash ツールにマッチ
- `"Edit|Write"` — 複数ツールにマッチ
- `"Bash(npm test*)"` — 特定コマンド引数にマッチ
- `"mcp__memory__.*"` — MCP ツールにマッチ
- 省略 / `""` / `"*"` — 全てにマッチ
- ツール名は大文字小文字を区別（`"Bash"` は有効、`"bash"` は無効）

### Handler Types

#### 1. Command (`type: "command"`)
```json
{
  "type": "command",
  "command": "/path/to/script.sh",
  "async": false,
  "timeout": 600,
  "statusMessage": "Running validation..."
}
```

#### 2. HTTP (`type: "http"`)
```json
{
  "type": "http",
  "url": "http://localhost:8080/hooks/pre-tool-use",
  "headers": { "Authorization": "Bearer $MY_TOKEN" },
  "allowedEnvVars": ["MY_TOKEN"],
  "timeout": 30
}
```

#### 3. Prompt (`type: "prompt"`)
```json
{
  "type": "prompt",
  "prompt": "Evaluate if action is allowed: $ARGUMENTS",
  "model": "claude-opus-4-1",
  "timeout": 30
}
```

#### 4. Agent (`type: "agent"`)
```json
{
  "type": "agent",
  "prompt": "Verify tests pass: $ARGUMENTS",
  "model": "claude-opus-4-1",
  "timeout": 60
}
```

### Exit Codes (Command hooks)

| Code | Behavior | JSON Processing |
|------|----------|----------------|
| 0 | Success; stdout の JSON を解析 | Yes |
| 2 | Blocking error; stderr を Claude にフィードバック | No |
| Other | Non-blocking error; verbose モードで表示 | No |

### HTTP Status Codes

| Status | Behavior |
|--------|----------|
| 2xx (empty body) | Success, no output |
| 2xx (JSON body) | Success, parse JSON |
| 2xx (plain text) | Success, add as context |
| Non-2xx | Non-blocking error; continue |

### Decision Control

#### PreToolUse — hookSpecificOutput
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "Explanation",
    "updatedInput": { "command": "modified command" },
    "additionalContext": "Context for Claude"
  }
}
```

#### PostToolUse / Stop — Top-level decision
```json
{
  "decision": "block",
  "reason": "Explanation for Claude"
}
```

### Timeout Defaults

| Hook Type | Default | Override |
|-----------|---------|---------|
| Command | 600s | `timeout` field |
| HTTP | 30s | `timeout` field |
| Prompt | 30s | `timeout` field |
| Agent | 60s | `timeout` field |
| SessionEnd | 1.5s | `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` env var |

### Path Interpolation

- `$CLAUDE_PROJECT_DIR` — プロジェクトルート参照
- `${CLAUDE_PLUGIN_ROOT}` — プラグインルート参照

### SessionStart — 環境変数永続化

`CLAUDE_ENV_FILE` に書き込むことでセッション全体に環境変数を永続化:
```bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=production' >> "$CLAUDE_ENV_FILE"
fi
```

### Hook Deduplication

- Command hooks: コマンド文字列で重複排除
- HTTP hooks: URL で重複排除

---

## 5. CLAUDE.md

### File Locations and Scopes

| Scope | Location | Purpose | Shared with |
|-------|----------|---------|-------------|
| Managed policy | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`; Linux/WSL: `/etc/claude-code/CLAUDE.md`; Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions | All users |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared project instructions | Team via VCS |
| User | `~/.claude/CLAUDE.md` | Personal preferences | Just you |

### Import (@) Syntax

- `@path/to/import` 構文で追加ファイルをインポート
- 相対パスと絶対パスの両方をサポート
- 相対パスは CLAUDE.md を含むファイルからの相対パスで解決（作業ディレクトリではない）
- 再帰的インポート可能、最大深度 **5 ホップ**
- インポートされたファイルは起動時にインラインで展開される（遅延読み込みではない）

```text
See @README for project overview and @package.json for available commands.
@docs/git-workflow.md
@~/.claude/my-project-overrides.md
```

外部インポートの初回発見時に承認ダイアログが表示される。

### Size Guidelines

- 目標: **200行以下** per CLAUDE.md file
- 推奨: ルート CLAUDE.md は **50-100行** で `@import` で詳細セクションを分離
- 長いファイルはコンテキストを消費し、遵守率が低下する
- 150行超えたら分離を検討
- 各行に対して「これを削除したら Claude がミスするか？」と問い、Noなら削除

### Loading Order

1. 作業ディレクトリから上方向にディレクトリツリーを走査し、各ディレクトリの CLAUDE.md を確認
2. 作業ディレクトリ以上の CLAUDE.md は起動時に全文読み込み
3. 子ディレクトリの CLAUDE.md はオンデマンド読み込み（Claude がそのディレクトリのファイルを読んだ時）
4. `.claude/rules/` のファイルはメイン CLAUDE.md と共に自動読み込み（インポート不要）
5. Managed policy CLAUDE.md は除外不可

**`claudeMdExcludes`**: グロブパターンで特定の CLAUDE.md を除外可能（monorepo 向け）

### Compaction Behavior

CLAUDE.md は圧縮（`/compact`）を完全に生き残る。圧縮後、Claude はディスクから CLAUDE.md を再読み込みして再注入する。

### `--add-dir` との連携

`--add-dir` で追加したディレクトリの CLAUDE.md はデフォルトでは読み込まれない。`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` 環境変数で有効化。

### `/init` Command

`/init` で既存コードベースを分析し、CLAUDE.md を自動生成。既に存在する場合は上書きではなく改善提案。

---

## 6. Plugins

### Plugin System Overview

プラグインは skills, agents, hooks, MCP servers をバンドルした拡張パッケージ。9,000+ プラグインが利用可能（2026年2月時点）。

### Plugin Structure

```
my-plugin/
├── plugin.json          # マニフェスト
├── SKILL.md             # メインスキル
├── skills/              # 追加スキル
├── hooks/hooks.json     # フック定義
└── README.md
```

### Marketplace System

- **Official**: `claude-plugins-official`（Anthropic 管理、自動利用可能）
- **Third-party**: GitHub リポジトリ、Git URL、ローカルパス、リモート URL から追加

### Installation Commands

```shell
# マーケットプレース追加
/plugin marketplace add owner/repo
/plugin marketplace add https://gitlab.com/company/plugins.git
/plugin marketplace add ./local-marketplace

# プラグインインストール
/plugin install plugin-name@marketplace-name

# スコープ指定
claude plugin install formatter@your-org --scope project

# 管理
/plugin disable plugin-name@marketplace-name
/plugin enable plugin-name@marketplace-name
/plugin uninstall plugin-name@marketplace-name
```

### Installation Scopes

| Scope | Description |
|-------|------------|
| User | 全プロジェクトで利用（デフォルト） |
| Project | リポジトリの全コラボレーター（`.claude/settings.json` に追加） |
| Local | このリポジトリの自分のみ |
| Managed | 管理者がインストール（変更不可） |

### Plugin Manager

`/plugin` で4タブ UI を開く:
- **Discover**: 利用可能なプラグインをブラウズ
- **Installed**: インストール済みプラグインの管理
- **Marketplaces**: マーケットプレースの追加/削除/更新
- **Errors**: プラグイン読み込みエラーの確認

### Code Intelligence Plugins (LSP)

公式マーケットプレースの LSP プラグインで言語サーバー連携:
- TypeScript (`typescript-lsp`), Python (`pyright-lsp`), Rust (`rust-analyzer-lsp`), Go (`gopls-lsp`) 等11言語
- 自動診断: 編集後に型エラー、未インポート、構文エラーを自動レポート
- コードナビゲーション: 定義ジャンプ、参照検索、型情報ホバー

### Marketplace Configuration

`.claude-plugin/marketplace.json`:
```json
{
  "name": "marketplace-name",
  "owner": "org-name",
  "plugins": [
    {
      "source": "path/to/plugin",
      "version": "1.0.0",
      "description": "Plugin description",
      "author": "Author",
      "keywords": ["keyword"],
      "category": "category"
    }
  ]
}
```

### Team Marketplace Configuration

`.claude/settings.json` で `extraKnownMarketplaces` を設定:
```json
{
  "extraKnownMarketplaces": {
    "my-team-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    }
  }
}
```

### Auto-update

- 公式マーケットプレースはデフォルトで自動更新有効
- サードパーティはデフォルトで無効
- `DISABLE_AUTOUPDATER` で全自動更新を無効化
- `FORCE_AUTOUPDATE_PLUGINS=true` で Claude Code 更新を無効にしつつプラグイン更新を維持

### Requirements

- Claude Code version 1.0.33 以降が必要
- `/reload-plugins` でセッション中にプラグイン変更を適用

---

## 7. Additional Configuration

### settings.local.json

- 場所: `.claude/settings.local.json`（プロジェクト）、`~/.claude/settings.local.json`（ユーザー）
- `settings.json` をオーバーライド（個人設定用、gitignore 推奨）
- API キー等のセンシティブ値は OS keychain または `settings.local.json` に格納
- Local scope (priority 3) > Project scope (priority 4)

### Memory (Auto Memory)

- 保存場所: `~/.claude/projects/<project>/memory/`
- `<project>` は git リポジトリから派生（同リポジトリの全ワークツリーで共有）
- `MEMORY.md` がエントリーポイント（最初の **200行** が毎セッション読み込まれる）
- トピックファイル（`debugging.md`, `api-conventions.md` 等）はオンデマンド読み込み
- マシンローカル（クラウド環境間で共有されない）
- `autoMemoryEnabled: false` で無効化、`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` 環境変数でも可
- `autoMemoryDirectory` でカスタム保存先を設定可能（user/local settings のみ、project settings からは不可）
- `/memory` コマンドで閲覧・編集

### Sandbox

- `/sandbox` コマンドまたは `sandbox.enabled: true` で有効化
- 有効時: Bash コマンドをファイルシステム・ネットワークから分離
- `autoAllowBashIfSandboxed: true` でサンドボックス内の Bash コマンドを自動許可
- デフォルト動作: 書き込みは現在の作業ディレクトリとサブディレクトリに制限
- サンドボックスなしの場合、Bash コマンドは Claude の Read/Edit ツールを通らないため deny ルールをバイパス可能
- サンドボックス有効時、OS カーネルレベルで deny ルールを強制

### Environment Variables

`env` フィールドまたはシェルプロファイルで設定。主要な変数:

#### Model Configuration
| Variable | Description |
|----------|-------------|
| `ANTHROPIC_MODEL` | デフォルト会話モデル |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | Sonnet モデルエイリアス |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | Opus モデルエイリアス |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Haiku モデルエイリアス |

#### Performance & Limits
| Variable | Description |
|----------|-------------|
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | 最大出力トークン数（例: `"16384"`） |
| `BASH_DEFAULT_TIMEOUT_MS` | Bash コマンドタイムアウト |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET` | スキル description 予算オーバーライド |

#### Feature Flags
| Variable | Description |
|----------|-------------|
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | 自動更新・テレメトリ無効化 |
| `CLAUDE_CODE_DISABLE_ANALYTICS` | 分析無効化 |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | 自動メモリ無効化 |
| `DISABLE_AUTOUPDATER` | 全自動更新無効化 |
| `FORCE_AUTOUPDATE_PLUGINS` | プラグイン自動更新を強制有効化 |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | `--add-dir` ディレクトリの CLAUDE.md 読み込み有効化 |

#### Hook-Related
| Variable | Description |
|----------|-------------|
| `CLAUDE_ENV_FILE` | SessionStart フックでの環境変数永続化先 |
| `CLAUDE_PROJECT_DIR` | プロジェクトルートパス（フック内で使用） |
| `CLAUDE_PLUGIN_ROOT` | プラグインルートパス（フック内で使用） |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd フックのタイムアウト |

Claude Code は約70の環境変数を認識するが、頻繁に使用されるのは約20個。

---

## Changelog

### 2026-03-15
- 初回収集: 公式ドキュメント（code.claude.com/docs/en/）から全7セクション（§1〜§7）を収集
- Source: settings, hooks, memory, skills, discover-plugins 各ページ + WebSearch 補完
- 24 hook events（従来の4タイプから大幅増加を確認）
- 4 handler types（command, http, prompt, agent）
- Plugin system（9,000+ plugins、マーケットプレース体系）
- Auto memory system の詳細仕様を追加
