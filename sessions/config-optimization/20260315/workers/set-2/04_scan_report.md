# スキャンレポート: Phase 2（現状分析）

## サマリ

7つの CO ターゲット全てについて現状分析を完了した。`.claude/settings.json` は 30+ フィールド中3フィールドのみ使用（利用率 ~10%）、deny ルール 14件は v1.0.93 既知バグにより非機能の可能性が高い。`.claude/rules/` は5ファイル・計292行で path-scoped rules 未使用。`.claude/skills/` は24スキルでコンテキスト予算上の懸念は低いが、description 品質にばらつきがある。hooks は 24 イベント中 1 イベント（SessionStart）のみ使用。CLAUDE.md は192行で公式推奨（50-100行）の約2-4倍、import(@) 未使用。プラグインは未導入。settings.local.json・sandbox ともに未使用。

## CO ターゲット別結果

### CO-001: settings.json

#### Current State

使用中フィールド: 3/30+
- `$schema`: 設定済み（`https://json.schemastore.org/claude-code-settings.json`）
- `hooks.SessionStart`: 1件（startup matcher、command 型）
- `permissions.allow`: 18件のルール
- `permissions.deny`: 14件のルール

#### Best Practices（リファレンス §1）

- 30+ フィールドが利用可能（permissions, model, hooks, env, sandbox, MCP, plugin, attribution, worktree, cleanupPeriodDays, autoMemory, outputStyle 等）
- deny ルールは v1.0.93 時点で非機能と報告されている。PreToolUse hook（exit code 2）が推奨代替手段
- sandbox 有効時にカーネルレベルで deny を強制可能

#### Gaps & Inefficiencies

| # | ギャップ | エビデンス | 重要度 |
|---|---------|-----------|--------|
| 1 | **deny ルール14件が非機能の可能性** | リファレンス §1: "As of v1.0.93, deny rules in settings.json were reported as non-functional"。現在の deny に `Read(./.env*)`, `Read(./secrets/**)`, `Read(**/*.pem)`, `Read(**/*.key)` 等のセキュリティ関連ルールが含まれるが、実効性なし | 高 |
| 2 | **sandbox 未設定** | `sandbox.enabled` 未設定。sandbox 有効時は OS カーネルレベルで deny を強制し、Bash 経由のバイパスも防止できる | 高 |
| 3 | **env フィールド未使用** | 環境変数を settings.json で一元管理できるが未使用。`CLAUDE_CODE_MAX_OUTPUT_TOKENS` や `SLASH_COMMAND_TOOL_CHAR_BUDGET` 等の活用余地あり | 低 |
| 4 | **attribution 未設定** | コミット・PR の帰属表示設定が未設定 | 低 |

#### Unused Features

- `model`: モデルオーバーライド
- `env`: 環境変数の一元管理
- `sandbox`: Bash コマンドのサンドボックス化
- `enableAllProjectMcpServers` / `enabledMcpjsonServers`: MCP サーバー管理
- `cleanupPeriodDays`: 会話履歴の保持期間
- `attribution`: コミット/PR 帰属設定
- `worktree`: git worktree 設定
- `claudeMdExcludes`: 特定 CLAUDE.md の除外
- `outputStyle`: 出力スタイル設定
- plugin 関連フィールド群（`skippedMarketplaces`, `skippedPlugins`, `extraKnownMarketplaces`, `enabledPlugins`）

---

### CO-002: .claude/rules/

#### Current State

5ファイル、計292行:

| # | ファイル | 行数 | path-scoped | 内容 |
|---|---------|------|-------------|------|
| 1 | `commit-message.md` | 139 | なし | コミットメッセージ規約（形式・セッション種別・例・禁止事項） |
| 2 | `session-start-branch-cleanup.md` | 88 | なし | ブランチ整理ルール（設計仕様リファレンス。実行ロジックは hook に移行済み） |
| 3 | `gha-workflow-security.md` | 27 | なし | GHA ワークフローセキュリティチェックリスト |
| 4 | `pr-url-output.md` | 19 | なし | PR URL 出力規約 |
| 5 | `rebase-conflict-handling.md` | 19 | なし | rebase コンフリクト時の対応フロー |

全ルールファイルの合計トークン消費: 292行 x ~5トークン/行 = ~1,460トークン（毎セッション読み込み）

#### Best Practices（リファレンス §2）

- path-scoped rules: YAML フロントマターの `paths` フィールドで特定ファイルにスコープ可能（遅延読み込み）
- `paths` なし: 起動時に全文読み込み（現在の全5ファイルがこれに該当）
- CLAUDE.md は全体適用、rules/ は特定領域適用が推奨パターン

#### Gaps & Inefficiencies

| # | ギャップ | エビデンス | 重要度 |
|---|---------|-----------|--------|
| 1 | **path-scoped rules 未使用** | 5ファイル全てが `paths` フロントマターなしで、全セッションで起動時に全文読み込みされる。GHA 関連ルール（`gha-workflow-security.md`）は `.github/workflows/` 編集時のみ必要だが常時読み込まれている | 中 |
| 2 | **commit-message.md の肥大化** | 139行はルールファイルとして大きい。セッション種別の対応テーブルが67行を占め、非施策作業の種別が増えるたびに肥大化する構造 | 中 |
| 3 | **session-start-branch-cleanup.md の役割重複** | 88行の設計仕様リファレンスとして維持されているが、実行ロジックは hook に移行済み。rules/ に置くことで毎セッション読み込まれるコストが発生 | 低 |
| 4 | **CLAUDE.md との責務分離が不完全** | CLAUDE.md に「禁止事項」「コマンド」等のルール的な内容が残っている。rules/ に委譲すればコンテキストの最適化が可能 | 中 |

#### Unused Features

- path-scoped rules（YAML `paths` フロントマター）
- サブディレクトリ構成（`rules/` 内のサブディレクトリも自動発見される）
- シンボリックリンクによるルール共有

---

### CO-003: .claude/skills/

#### Current State

24スキル（user-invocable: true が 11件、false が 13件）:

**user-invocable: true（11件）**: automation-manager, backlog-maintenance-manager, config-optimizer-manager, fork-sync, l1-impl-manager, l1-manager, metacognition-manager, repo-sync-checklist, sync-manager, triage-manager, gha-test

**user-invocable: false（13件）**: builtin-skills-reference, external-repo-cleanup, format-conversion-checklist, gha-close, gha-execute, gha-guideline, gha-question, gha-wallbash, manager-common-policy, plugin-reference, rule-change-checklist, session-flow-policy, triage-standard-policy

**disable-model-invocation の使用**: 0件（全スキルがデフォルト `false`）

#### Description 品質分析

全24スキルの description が単一行文字列であり、YAML マルチライン指示子は使用されていない（ベストプラクティス準拠）。

description 内容の詳細:

| 分類 | スキル数 | 例 |
|------|---------|-----|
| 具体的で良好 | 18 | `l1-manager`: "L1マネージャーとして施策の提案・計画・タスク分解・ゲートレビューを管理する" |
| やや長い（100文字超） | 4 | `format-conversion-checklist`: 156文字、`manager-common-policy`: 94文字 |
| 抽象的 | 2 | `gha-test`: "GHA 壁打ち相当の動作検証用テストスキル"（何のテストか不明確） |

#### Context Budget 推定

- 24スキル × description ~100トークン = ~2,400トークン（常時読み込み）
- コンテキスト予算: 2%（フォールバック 16,000文字）
- 現在の description 合計は予算内に収まっていると推定される
- `user-invocable: false` のスキルも description は常時読み込みされる（Claude が自動起動判断に使うため）
- ただし `disable-model-invocation: true` の場合は description がコンテキストに読み込まれない

#### Gaps & Inefficiencies

| # | ギャップ | エビデンス | 重要度 |
|---|---------|-----------|--------|
| 1 | **disable-model-invocation 未活用** | 13件の `user-invocable: false` スキルのうち、GHA 専用スキル（gha-close, gha-execute, gha-wallbash, gha-question, gha-test）は Claude の自動起動対象外にすべきだが、`disable-model-invocation: true` が設定されていない。これらの description がコンテキスト予算を消費している | 中 |
| 2 | **参照専用スキルの自動起動コスト** | `builtin-skills-reference`, `plugin-reference`, `gha-guideline` 等の参照専用スキルは `user-invocable: false` だが、Claude が自動起動を判断するために description を毎回評価する。`disable-model-invocation: true` にすれば description の読み込み自体を省略できる | 低 |
| 3 | **スキルサイズの偏り** | 最大468行（l1-impl-manager）から最小40行（gha-question）まで11倍以上の差。起動時のコンテキスト消費に大きな差がある | 低 |
| 4 | **Dynamic Context Injection 未活用** | `!`command`` 構文による動的コンテキスト注入が一切使用されていない。スキル内で現在のブランチ状態やファイル一覧を注入する活用余地がある | 低 |

#### Unused Features

- `disable-model-invocation: true`（GHA スキル・参照専用スキルに適用可能）
- Dynamic Context Injection（`!`command`` 構文）
- `model` フロントマター（スキルごとのモデル指定）
- `hooks` フロントマター（スキルライフサイクルにスコープされたフック）
- `argument-hint` フロントマター

---

### CO-004: .claude/hooks/

#### Current State

使用中イベント: 1/24（SessionStart のみ）

設定内容:
```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "startup",
      "hooks": [{
        "type": "command",
        "command": ".claude/hooks/session-start-branch-cleanup.sh"
      }]
    }]
  }
}
```

使用中の handler type: command（1/4）
未使用の handler type: http, prompt, agent

#### Best Practices（リファレンス §4）

24イベントが利用可能:
- Session Lifecycle: SessionStart, SessionEnd, InstructionsLoaded
- User Input: UserPromptSubmit
- Tool Execution: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Agent Flow: SubagentStart, SubagentStop, Stop, TeammateIdle, TaskCompleted
- System Events: Notification, ConfigChange, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove
- MCP Integration: Elicitation, ElicitationResult

#### Gaps & Inefficiencies

| # | ギャップ | エビデンス | 重要度 |
|---|---------|-----------|--------|
| 1 | **PreToolUse hook 未使用（deny ルール代替として必須）** | deny ルール非機能性（ISS-TEMP-001）の代替として PreToolUse hook（exit code 2）が公式推奨されているが未実装。現在の deny ルール14件のセキュリティガードが実質無効 | 高 |
| 2 | **PostToolUse hook 未使用** | ファイル編集後の自動検証（例: CLAUDE.md の行数チェック、rules/ の path-scoped フロントマター検証）に活用可能だが未使用 | 中 |
| 3 | **Stop hook 未使用** | メインエージェント応答完了時のサマリー自動生成やチェックリスト検証に活用可能だが未使用 | 低 |
| 4 | **SessionEnd hook 未使用** | セッション終了時の自動クリーンアップ（一時ファイル削除等）に活用可能だが未使用 | 低 |
| 5 | **prompt/agent handler type 未活用** | LLM ベースの検証（prompt type）やマルチターンエージェント検証（agent type）が利用可能だが、command type のみ使用中 | 低 |

#### Unused Features（活用余地の高い順）

| イベント | 活用シナリオ | 優先度 |
|---------|------------|--------|
| PreToolUse | deny ルールの代替ガード（`.env*`, `secrets/**`, `*.pem`, `*.key` へのアクセスブロック） | 高 |
| PostToolUse | ファイル編集後の自動検証（CLAUDE.md 行数、コミットメッセージ規約チェック） | 中 |
| Stop | 応答完了時のチェックリスト検証 | 低 |
| SessionEnd | セッション終了時のクリーンアップ | 低 |
| SubagentStart/Stop | サブエージェントの起動・終了ログ記録 | 低 |
| ConfigChange | 設定ファイル変更時の整合性チェック | 低 |
| PreCompact/PostCompact | コンテキスト圧縮前後のカスタム処理 | 低 |

---

### CO-005: CLAUDE.md

#### Current State

- 行数: 192行（公式推奨 50-100行の約2-4倍）
- import(@) 使用: なし
- セクション構成:

| セクション | 行範囲 | 行数 | 内容 |
|-----------|--------|------|------|
| 概要 | 1-5 | 5 | プロジェクト概要 |
| セッション構成 | 7-14 | 8 | L1/L2 ロール定義 |
| GitHub Actions からの実行 | 16-22 | 7 | GHA 実行ポリシー |
| ファイル命名規則 | 24-28 | 5 | 命名規則 |
| 施策管理の必須化 | 30-37 | 8 | 施策管理ルール |
| 禁止事項 | 39-45 | 7 | 禁止操作リスト |
| コマンド | 47-51 | 5 | 操作コマンド |
| ディレクトリ構成と用途 | 53-79 | 27 | ディレクトリ説明（テーブル + 使い分けガイド） |
| ドキュメント階層方針 | 81-86 | 6 | 3層構造方針 |
| ドキュメント整合性ルール | 88-129 | 42 | docs/ 文書分類（3カテゴリ定義 + ファイル分類テーブル + 管理ルール） |
| セッション終了時の気づき記録 | 131-153 | 23 | inbox 記録ルール |
| 文書分類ポリシー | 155-168 | 14 | Claude/人間向け配置先 |
| 環境分離ポリシー | 170-186 | 17 | リポジトリ別実行環境 |
| リポジトリ間の関係 | 188-192 | 5 | 依存関係 |

#### Best Practices（リファレンス §5）

- 目標: 200行以下 per file
- 推奨: ルート CLAUDE.md は 50-100行で `@import` で詳細を分離
- 短い CLAUDE.md ほど遵守率が高い
- 150行超えたら分離を検討
- 各行に「削除したら Claude がミスするか？」を問う

#### Gaps & Inefficiencies

| # | ギャップ | エビデンス | 重要度 |
|---|---------|-----------|--------|
| 1 | **192行で公式推奨の約2-4倍** | 公式推奨 50-100行に対して192行。150行超過の分離検討基準も超過。遵守率低下リスク | 高 |
| 2 | **import(@) 未使用** | 詳細セクションを分離ファイルに切り出す機能が利用可能だが一切未使用 | 高 |
| 3 | **ドキュメント整合性ルール（42行）が肥大化** | docs/ 文書分類のカテゴリ定義・ファイル分類テーブル・管理ルールが42行。これは CLAUDE.md ではなく rules/ に委譲可能 | 中 |
| 4 | **セッション終了時の気づき記録（23行）** | 特定タイミングのみ必要な詳細手順が常時読み込まれている。rules/ または import 先に分離可能 | 中 |
| 5 | **禁止事項セクションの rules/ との重複可能性** | CLAUDE.md の禁止事項と rules/ の各ルールファイル内の禁止事項が同じコンテキストで読み込まれ、冗長性がある | 低 |
| 6 | **ディレクトリ構成と用途（27行）の詳細度** | inbox/refs/issues の使い分けガイドは初回理解には有用だが、毎セッション読み込みには詳細すぎる | 低 |

#### rules/ 委譲候補

| セクション | 行数 | 委譲先 | 理由 |
|-----------|------|--------|------|
| ドキュメント整合性ルール | 42 | `.claude/rules/doc-integrity.md` | ルール的な内容であり、docs/ 編集時のみ必要。path-scoped で `docs/**` にスコープ可能 |
| セッション終了時の気づき記録 | 23 | `.claude/rules/session-end-notes.md` | セッション終了時のみ必要。常時読み込みは不要 |
| 環境分離ポリシー | 17 | `@import` で分離 | 施策起票時のみ参照。常時読み込みは過剰 |

#### import(@) 分離候補

| 分離対象 | 推定行数 | 分離先 | 効果 |
|---------|---------|--------|------|
| ドキュメント整合性ルール | 42 | rules/ に委譲（上記） | CLAUDE.md から42行削減 |
| セッション終了時の気づき記録 | 23 | `docs/session-end-notes-detail.md` を @import | CLAUDE.md から23行削減 |
| ディレクトリ構成詳細（使い分けガイド部分） | ~15 | `docs/directory-guide.md` を @import | CLAUDE.md から15行削減 |

上記を全て実施した場合: 192 - 42 - 23 - 15 = **112行**（推奨範囲の上限に近づく）

#### Unused Features

- import(@) 構文
- 子ディレクトリ CLAUDE.md（`sessions/CLAUDE.md` 等でサブコンテキストを定義可能）
- `claudeMdExcludes`（不要な CLAUDE.md の除外）

---

### CO-006: プラグイン導入

#### Current State

- 導入済みプラグイン: **0件**
- settings.json にプラグイン関連設定: なし（`enabledPlugins`, `extraKnownMarketplaces` 等未設定）
- `.claude/skills/plugin-reference/SKILL.md` に評価リファレンスが存在（2026-03-13 評価）

#### Best Practices（リファレンス §6）

- 9,000+ プラグインが利用可能
- 公式マーケットプレイスから4件が「適用可能性: 高」と評価済み:
  1. `commit-commands`: git 操作標準化
  2. `claude-md-management`: CLAUDE.md 品質維持
  3. `skill-creator`: スキル作成・改善・評価
  4. `claude-code-setup`: 設定最適化提案

#### Gaps & Inefficiencies

| # | ギャップ | エビデンス | 重要度 |
|---|---------|-----------|--------|
| 1 | **評価済み高優先度プラグイン4件が未導入** | plugin-reference で「適用可能性: 高」と評価された4件（commit-commands, claude-md-management, skill-creator, claude-code-setup）が未導入 | 中 |
| 2 | **hookify プラグイン未導入** | deny ルール非機能性の代替として PreToolUse hook の作成を支援する hookify が未導入。手動でのフック作成が必要 | 低 |

#### Unused Features

- 公式マーケットプレイスプラグイン全般
- `extraKnownMarketplaces`（チームマーケットプレース設定）
- `/plugin` UI

---

### CO-007: その他

#### Current State

| 項目 | 状態 |
|------|------|
| settings.local.json | 不存在（`.claude/settings.local.json` が存在しない） |
| Auto Memory | デフォルト有効（`autoMemoryEnabled` 未設定 = `true`）。`autoMemoryDirectory` 未設定 |
| Sandbox | 未設定（`sandbox.enabled` 未設定 = `false`） |
| 環境変数（env フィールド） | 未設定 |
| worktree 設定 | 未設定 |

#### Best Practices（リファレンス §7）

- settings.local.json: 個人設定の分離（API キー、ローカルオーバーライド）に使用
- Auto Memory: `~/.claude/projects/<project>/memory/` に自動保存。MEMORY.md の先頭200行が毎セッション読み込み
- Sandbox: `sandbox.enabled: true` で Bash コマンドの分離。deny ルールをカーネルレベルで強制
- 環境変数: `SLASH_COMMAND_TOOL_CHAR_BUDGET` でスキル予算制御、`CLAUDE_CODE_MAX_OUTPUT_TOKENS` で出力トークン制御

#### Gaps & Inefficiencies

| # | ギャップ | エビデンス | 重要度 |
|---|---------|-----------|--------|
| 1 | **sandbox 未有効化** | deny ルール非機能性（ISS-TEMP-001）と合わせて、sandbox 有効化によるカーネルレベルの deny 強制が代替手段の一つだが未設定 | 高 |
| 2 | **settings.local.json 未使用** | 個人設定（env オーバーライド等）の分離先がない | 低 |
| 3 | **Auto Memory の状態不明** | デフォルト有効だが、実際の Memory 内容・品質は未確認（ローカル環境依存のため本分析スコープ外） | 低 |

#### Unused Features

- settings.local.json（個人設定分離）
- sandbox（Bash コマンドのサンドボックス化）
- env フィールド（環境変数の一元管理）
- worktree 設定（git worktree の自動化）
- `SLASH_COMMAND_TOOL_CHAR_BUDGET` 環境変数
- `CLAUDE_CODE_MAX_OUTPUT_TOKENS` 環境変数

---

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | deny ルールの二重防御が欠如 | `.claude/settings.json` の deny + hooks | settings.json の deny が非機能でも、PreToolUse hook と sandbox の組み合わせでセキュリティガードを実現できる。現在はどちらも未実装で単一障害点 |
| 2 | GHA 専用スキルに disable-model-invocation 未設定 | `.claude/skills/gha-*/SKILL.md` | GHA 環境でのみ使用されるスキル5件が CLI セッションでもコンテキスト予算を消費している |
| 3 | commit-message.md の肥大化パターン | `.claude/rules/commit-message.md` | 139行のうちセッション種別テーブルが67行。新規セッション種別追加ごとに増大する構造的問題 |
| 4 | CLAUDE.md の分離で ~80行削減が可能 | `CLAUDE.md` | ドキュメント整合性ルール（42行）+ セッション終了時の気づき記録（23行）+ ディレクトリ詳細（15行）を rules/ と import に分離可能 |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | skills の Progressive Disclosure がコンテキスト最適化に効いている | 24スキルの全文は起動時のみ読み込みされ、description のみが常時読み込み。最大468行のスキルも起動されなければコスト0 |
| 2 | path-scoped rules は遅延読み込みでコンテキスト節約に直結 | 現在の5ルールファイル（292行）が全て起動時読み込み。path-scoped にすれば必要時のみ読み込まれる |
| 3 | SessionStart hook の実装品質は高い | JSON 出力、全パス exit 0 保証、エラーハンドリングが適切。他の hook 追加時のテンプレートとして活用可能 |

---
**作成者**: config-analysis-worker
**作成日**: 2026-03-15
