# スキャンレポート: Phase 1（情報収集）

## サマリ

Claude Code 公式ドキュメント（code.claude.com/docs/en/）から7つのCOターゲット全てについて情報収集を完了した。WebSearch 10クエリ + WebFetch 5ページの取得により、リファレンスの全7セクションを具体的な仕様情報で更新した。特筆すべき発見として、hooks が従来想定の4タイプから24イベントに大幅拡張されていること、plugin system が9,000+プラグインの規模に成長していることが確認された。

## CO ターゲット別結果

### CO-001: settings.json

- **カバレッジ**: 完全
- **収集内容**: 30+ フィールドのスキーマ（型・説明・デフォルト値）、4つの Configuration Scope と優先順位、Permission Rule Format（`Tool(specifier)` 記法）
- **情報源**: code.claude.com/docs/en/settings（WebFetch 全文取得）
- **主要発見**:
  - deny ルールの既知バグ（v1.0.93 時点で non-functional と報告）→ PreToolUse hook が代替手段
  - `claudeMdExcludes` フィールドの存在（monorepo 向け）
  - `autoMemoryEnabled`, `autoMemoryDirectory` フィールドの存在
  - plugin 関連フィールド（`extraKnownMarketplaces`, `enabledPlugins`, `skippedMarketplaces`）

### CO-002: .claude/rules/

- **カバレッジ**: 完全
- **収集内容**: ルールファイルフォーマット、path-scoped rules の YAML フロントマター記法、glob パターン例、読み込み動作、シンボリックリンクサポート
- **情報源**: code.claude.com/docs/en/memory（WebFetch 全文取得）
- **主要発見**:
  - rules は CLAUDE.md 子ディレクトリファイルとは異なる読み込み戦略（glob パターンによる精密ターゲティング）
  - ユーザーレベルルール（`~/.claude/rules/`）がプロジェクトルールより低い優先度で読み込まれる
  - ブレース展開（`*.{ts,tsx}`）をサポート

### CO-003: .claude/skills/

- **カバレッジ**: 完全
- **収集内容**: フロントマター全フィールド（10フィールド）、description 最適化ガイドライン、Context Budget（2% / 16,000文字 fallback）、Progressive Disclosure、String Substitutions、Dynamic Context Injection、Agent Skills オープン標準
- **情報源**: code.claude.com/docs/en/skills（WebFetch 全文取得）
- **主要発見**:
  - description は単一行文字列推奨（YAML マルチライン指示子は正しくパースされない）
  - `context: fork` はタスク付き指示にのみ有効（ガイドラインのみではサブエージェントが何もせずに返る）
  - `!`command`` による動的コンテキスト注入が可能
  - `/context` コマンドで除外されたスキルの警告を確認可能

### CO-004: .claude/hooks/

- **カバレッジ**: 完全
- **収集内容**: 24イベントタイプの完全仕様、4 handler types（command/http/prompt/agent）、3レベル設定構造、matcher regex 記法、exit codes、JSON input/output スキーマ、decision control、timeout defaults
- **情報源**: code.claude.com/docs/en/hooks（WebFetch 全文取得）
- **主要発見**:
  - 24イベントに拡張（SessionStart, SessionEnd, InstructionsLoaded, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, SubagentStart, SubagentStop, Stop, TeammateIdle, TaskCompleted, Notification, ConfigChange, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Elicitation, ElicitationResult 等）
  - 4 handler types: command（シェルコマンド）、http（POST リクエスト）、prompt（単一ターン LLM 評価）、agent（マルチターンエージェント検証）
  - PreToolUse の decision control が `hookSpecificOutput.permissionDecision` 方式に移行（旧 top-level decision は deprecated）
  - `$CLAUDE_PROJECT_DIR` と `${CLAUDE_PLUGIN_ROOT}` によるパス補間
  - `CLAUDE_ENV_FILE` による SessionStart フックでの環境変数永続化

### CO-005: CLAUDE.md

- **カバレッジ**: 完全
- **収集内容**: @import 構文（相対・絶対パス、最大深度5ホップ）、サイズガイドライン（200行以下、50-100行推奨）、読み込み順序（上方向走査 + 子ディレクトリはオンデマンド）、Managed policy CLAUDE.md、claudeMdExcludes
- **情報源**: code.claude.com/docs/en/memory（WebFetch 全文取得）
- **主要発見**:
  - CLAUDE.md は compaction を完全に生き残る（ディスクから再読み込み）
  - `--add-dir` ディレクトリの CLAUDE.md はデフォルトで読み込まれない（`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` で有効化）
  - `/init` コマンドで CLAUDE.md を自動生成可能
  - Managed policy CLAUDE.md は除外不可

### CO-006: プラグイン導入

- **カバレッジ**: 完全
- **収集内容**: プラグインシステム概要、構造（plugin.json, SKILL.md）、マーケットプレースシステム（official + third-party）、インストールコマンド、スコープ、Plugin Manager UI、LSP プラグイン、Team Marketplace 設定、Auto-update
- **情報源**: code.claude.com/docs/en/discover-plugins（WebFetch 全文取得）
- **主要発見**:
  - 9,000+ プラグインが利用可能（2026年2月時点）
  - 11言語の LSP プラグイン（自動診断 + コードナビゲーション）
  - `/reload-plugins` でセッション中にプラグイン変更を適用可能
  - `extraKnownMarketplaces` でチーム向けマーケットプレースを設定可能
  - `.claude-plugin/marketplace.json` がマーケットプレース設定ファイル

### CO-007: その他

- **カバレッジ**: 完全
- **収集内容**: settings.local.json（優先度・用途）、Auto Memory（保存場所・MEMORY.md 200行上限・トピックファイル）、Sandbox（enabled, autoAllowBashIfSandboxed, network 設定）、環境変数（約70変数、主要20変数を分類）
- **情報源**: code.claude.com/docs/en/settings + /memory（WebFetch）+ WebSearch 補完
- **主要発見**:
  - Auto Memory: git リポジトリ単位で共有、マシンローカル、`autoMemoryDirectory` でカスタム保存先設定可能（project settings からは不可）
  - Sandbox: 有効時はカーネルレベルで deny ルールを強制（Bash 経由のバイパスを防止）
  - `CLAUDE_CODE_MAX_OUTPUT_TOKENS` で出力トークン数を制御可能（高すぎると throttling エラー）
  - `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` で SessionEnd フックのタイムアウトを設定可能

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | deny ルールの非機能性 | `.claude/settings.json` の deny | v1.0.93 時点で deny が機能しないバグ報告あり。PreToolUse hook が代替。本プロジェクトの deny ルール設定を要検証 |
| 2 | hooks 24イベント対応 | `.claude/settings.json` の hooks | 現在 SessionStart のみ使用。PostToolUse, Stop, ConfigChange 等の活用余地あり |
| 3 | Context Budget 2% 制約 | `.claude/skills/` | スキル数増加時に description 予算を超過する可能性。`/context` で定期確認推奨 |
| 4 | SKILL.md description の単一行推奨 | `.claude/skills/*/SKILL.md` | YAML マルチライン指示子が正しくパースされないため、全スキルの description を要確認 |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | Agent Skills オープン標準 | Claude Code, Cursor, Gemini CLI 等で互換。将来のツール移行時のポータビリティ確保に有利 |
| 2 | Plugin LSP 統合 | 11言語の LSP プラグインで自動診断 + コードナビゲーション。開発効率向上の可能性 |
| 3 | Auto Memory の200行制限 | MEMORY.md の最初の200行のみセッション開始時に読み込まれる。トピックファイルはオンデマンド |

---
**作成者**: config-collection-worker
**作成日**: 2026-03-15
