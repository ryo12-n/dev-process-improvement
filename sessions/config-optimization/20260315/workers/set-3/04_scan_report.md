# スキャンレポート: Phase 3（最適化提案）

## サマリ

Phase 2 で特定された22件のギャップに対し、7件の最適化提案（OPT-001〜OPT-007）を作成した。Impact x Effort マトリクスにより Quick Wins 3件（OPT-003, OPT-007, OPT-002）、Strategic 2件（OPT-001, OPT-005）、Easy Adds 1件（OPT-004）、Nice-to-Have 1件（OPT-006）に分類した。最優先は OPT-003（GHA スキル disable-model-invocation）と OPT-007（sandbox 有効化）で、いずれも設定変更のみで即時効果が得られる。セキュリティ面では OPT-001（PreToolUse hook）+ OPT-007（sandbox）の二重防御を戦略的に実装すべきである。

---

## OPT-001: PreToolUse hook によるセンシティブファイルアクセスガード

- **CO ターゲット**: CO-001（settings.json）、CO-004（hooks/）
- **Current State**: deny ルール14件が v1.0.93 既知バグにより非機能。PreToolUse hook 未実装。センシティブファイル（`.env*`, `secrets/**`, `*.pem`, `*.key`）へのアクセスガードが実質無効
- **Proposed Change**: PreToolUse hook（exit code 2 でブロック）を実装し、deny ルールの代替ガードとする

  **実装例: `.claude/hooks/pretooluse-deny-guard.sh`**
  ```bash
  #!/usr/bin/env bash
  # PreToolUse hook: deny ルール代替ガード
  # exit 0 = 許可、exit 2 = ブロック（stderr を Claude にフィードバック）
  set -euo pipefail

  TOOL_NAME="${CLAUDE_TOOL_NAME:-}"
  TOOL_INPUT="${CLAUDE_TOOL_INPUT:-}"

  # ブロック対象パターン（settings.json の deny ルールと同等）
  DENY_PATTERNS=(
    '\.env'
    'secrets/'
    '\.pem$'
    '\.key$'
  )

  # Read/Edit/Write ツールのファイルパスをチェック
  if [[ "$TOOL_NAME" =~ ^(Read|Edit|Write)$ ]]; then
    for pattern in "${DENY_PATTERNS[@]}"; do
      if echo "$TOOL_INPUT" | grep -qE "$pattern"; then
        echo "BLOCKED: Access to sensitive file matching '$pattern' is denied by security policy." >&2
        exit 2
      fi
    done
  fi

  # Bash ツールのコマンドをチェック（cat .env*, cat secrets/* 等）
  if [[ "$TOOL_NAME" == "Bash" ]]; then
    for pattern in "${DENY_PATTERNS[@]}"; do
      if echo "$TOOL_INPUT" | grep -qE "$pattern"; then
        echo "BLOCKED: Bash command accessing sensitive file matching '$pattern' is denied by security policy." >&2
        exit 2
      fi
    done
  fi

  exit 0
  ```

  **settings.json への追加:**
  ```json
  {
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Read|Edit|Write",
          "hooks": [{
            "type": "command",
            "command": ".claude/hooks/pretooluse-deny-guard.sh",
            "timeout": 5
          }]
        },
        {
          "matcher": "Bash",
          "hooks": [{
            "type": "command",
            "command": ".claude/hooks/pretooluse-deny-guard.sh",
            "timeout": 5
          }]
        }
      ]
    }
  }
  ```

  **代替案（JSON 出力による構造化ブロック）:**
  ```bash
  # より高度な実装: JSON hookSpecificOutput で deny 理由を返す
  cat <<EOF
  {
    "hookSpecificOutput": {
      "hookEventName": "PreToolUse",
      "permissionDecision": "deny",
      "permissionDecisionReason": "Access to sensitive file denied by security policy"
    }
  }
  EOF
  exit 0
  ```

- **Expected Benefit**: deny ルール14件相当のセキュリティガードを PreToolUse hook で実現。settings.json の deny が修正されるまでの代替手段として機能する。sandbox（OPT-007）と併用で二重防御
- **Impact**: 高（セキュリティガード不在の解消。ISS-TEMP-003 の直接対策）
- **Effort**: 中（シェルスクリプト作成 + テスト。既存の SessionStart hook をテンプレートとして活用可能だが、パターンマッチングの精度検証が必要）
- **Risk**: パターンマッチングが誤検知（false positive）する可能性。緩和策: 正当なファイルアクセスがブロックされた場合に備え、`permissions.allow` との協調ロジックを設計する。段階的導入（まず Read のみ、次に Edit/Write、最後に Bash）を推奨
- **Backlog Entry Draft**:
  - タイトル: PreToolUse hook によるセンシティブファイルアクセスガード実装
  - 説明: deny ルール非機能（v1.0.93 既知バグ）の代替として PreToolUse hook を実装する。`.env*`, `secrets/**`, `*.pem`, `*.key` への Read/Edit/Write/Bash アクセスを exit code 2 でブロック。sandbox（別施策）との二重防御を構成する

---

## OPT-002: path-scoped rules 導入 + commit-message.md 分離

- **CO ターゲット**: CO-002（.claude/rules/）
- **Current State**: 5ファイル・計292行が全て `paths` フロントマターなしで起動時に全文読み込み。commit-message.md が139行と肥大化（セッション種別テーブル67行）。GHA セキュリティルールが `.github/workflows/` 編集時以外も常時読み込み
- **Proposed Change**:

  **(A) path-scoped rules の導入（3ファイル）:**

  **gha-workflow-security.md に paths 追加:**
  ```yaml
  ---
  paths:
    - ".github/workflows/**"
    - ".github/actions/**"
  ---

  # GHA ワークフローセキュリティチェックリスト
  ...（既存内容変更なし）
  ```

  **rebase-conflict-handling.md に paths 追加:**
  ```yaml
  ---
  paths:
    - "**"
  ---
  ```
  注: rebase は任意のファイルで発生するため、このルールは実質的に現状維持。ただし session-start-branch-cleanup.md の方が path-scoped の恩恵が大きい。

  **session-start-branch-cleanup.md を rules/ から docs/ へ移動:**
  実行ロジックは hook に移行済みであり、設計仕様リファレンスとしての役割のみ。rules/ に置くことで毎セッション88行が読み込まれるコストが不要。`docs/design/session-start-branch-cleanup.md` に移動し、rules/ からは削除する。

  **(B) commit-message.md の分離:**

  **現状 139行の構成:**
  - 形式定義: ~20行（必須。毎セッション参照）
  - セッション種別テーブル: ~67行（参照頻度低。新種別追加で肥大化する構造）
  - 例: ~35行（参照頻度低）
  - 禁止事項: ~10行（必須。毎セッション参照）

  **分離案:**
  - `.claude/rules/commit-message.md`（~35行）: 形式定義 + 禁止事項 + セッション種別テーブルへの @import
  - `.claude/rules/commit-message-sessions.md` に path-scoped で分離:
    ```yaml
    ---
    paths:
      - "sessions/**"
    ---
    # コミットメッセージ: セッション種別テーブル
    ...（67行のテーブル + 35行の例）
    ```
  - sessions/ 配下のファイル編集時のみ詳細テーブルが読み込まれる

  **期待削減量:**
  - path-scoped 化: gha-workflow-security.md 27行 + session-start-branch-cleanup.md 88行 = 115行が遅延読み込みに
  - commit-message.md 分離: 常時読み込み 139行 → 35行（104行削減）
  - 合計: 起動時の rules/ 読み込みが 292行 → ~73行（~75%削減）

- **Expected Benefit**: 起動時のコンテキスト消費を ~75% 削減（292行 → ~73行）。commit-message.md の構造的肥大化問題を解消し、新セッション種別追加時も分離ファイル側のみ更新
- **Impact**: 中（コンテキスト最適化。トークン節約は ~1,100トークン/セッション）
- **Effort**: 低（YAML フロントマター追加 + ファイル分割のみ。既存ルールの内容変更なし）
- **Risk**: path-scoped ルールがマッチしないケースで rules が適用されないリスク。緩和策: commit-message の形式定義・禁止事項は paths なし（常時読み込み）で維持する。分離後に各セッション種別でコミットメッセージが正しく生成されることをテスト
- **Backlog Entry Draft**:
  - タイトル: path-scoped rules 導入と commit-message.md 分離
  - 説明: rules/ の5ファイル（292行）に path-scoped rules を導入し、起動時読み込みを ~73行に削減する。commit-message.md（139行）はコア部分（35行）と sessions/ スコープの詳細テーブルに分離。session-start-branch-cleanup.md（88行）は docs/design/ に移動

---

## OPT-003: GHA スキル6件への disable-model-invocation 設定

- **CO ターゲット**: CO-003（.claude/skills/）
- **Current State**: GHA 専用スキル6件（gha-close, gha-execute, gha-guideline, gha-question, gha-test, gha-wallbash）が `disable-model-invocation` 未設定。全て `user-invocable: false` だが description が毎セッションのコンテキスト予算に読み込まれている。CLI セッションでは不要（GHA ワークフローからのみ使用）

  **補足**: Phase 2 では5件と報告されていたが、`gha-guideline`（GHA 運用ガイドライン参照スキル）も `user-invocable: false` の GHA 関連スキルであり、CLI セッションでの自動起動は不要。合計6件が対象

- **Proposed Change**: 6件全てに `disable-model-invocation: true` を追加

  **変更例（gha-close/SKILL.md）:**
  ```yaml
  ---
  name: gha-close
  description: 'GHA initiative-close ワークフロー専用スキル。クローズフェーズ（知見ルーティング・アーカイブ移動）を実行する。'
  user-invocable: false
  disable-model-invocation: true
  ---
  ```

  **対象スキル一覧:**

  | # | スキル | 現状 | 変更後 |
  |---|--------|------|--------|
  | 1 | `gha-close` | `user-invocable: false` のみ | + `disable-model-invocation: true` |
  | 2 | `gha-execute` | `user-invocable: false` のみ | + `disable-model-invocation: true` |
  | 3 | `gha-guideline` | `user-invocable: false` のみ | + `disable-model-invocation: true` |
  | 4 | `gha-question` | `user-invocable: false` のみ | + `disable-model-invocation: true` |
  | 5 | `gha-test` | `user-invocable: false` のみ | + `disable-model-invocation: true` |
  | 6 | `gha-wallbash` | `user-invocable: false` のみ | + `disable-model-invocation: true` |

  **GHA ワークフローへの影響**: なし。GHA ワークフローは `claude-code-action` のスキル指定で明示的に起動するため、`disable-model-invocation: true` は Claude の自動起動のみを防止し、明示的起動には影響しない

- **Expected Benefit**: CLI セッションで6件分の description トークン（~600トークン）がコンテキスト予算から除外される。Claude が GHA 専用スキルを誤って自動起動するリスクも排除
- **Impact**: 中（コンテキスト最適化 + 誤起動防止）
- **Effort**: 低（YAML フロントマターに1行追加 x 6ファイル。内容変更なし）
- **Risk**: 極低。GHA ワークフローからの明示的起動は `disable-model-invocation` の影響を受けない。万一問題が発生しても1行削除で即時復元可能
- **Backlog Entry Draft**:
  - タイトル: GHA スキル6件に disable-model-invocation を設定
  - 説明: GHA 専用スキル6件（gha-close, gha-execute, gha-guideline, gha-question, gha-test, gha-wallbash）に `disable-model-invocation: true` を追加し、CLI セッションでのコンテキスト消費と誤起動を防止する

---

## OPT-004: PostToolUse hook による自動検証の導入

- **CO ターゲット**: CO-004（.claude/hooks/）
- **Current State**: 24 hook イベント中 SessionStart のみ使用。PostToolUse 未使用。ファイル編集後の品質チェックが手動依存
- **Proposed Change**: PostToolUse hook で Edit/Write 後の自動検証を実装

  **ユースケース 1: CLAUDE.md 行数チェック**
  ```bash
  #!/usr/bin/env bash
  # PostToolUse hook: CLAUDE.md 行数警告
  set -euo pipefail

  TOOL_INPUT="${CLAUDE_TOOL_INPUT:-}"

  # CLAUDE.md への編集のみチェック
  if echo "$TOOL_INPUT" | grep -q "CLAUDE.md"; then
    LINE_COUNT=$(wc -l < "$CLAUDE_PROJECT_DIR/CLAUDE.md" 2>/dev/null || echo "0")
    if [ "$LINE_COUNT" -gt 150 ]; then
      cat <<EOF
  {
    "decision": "block",
    "reason": "WARNING: CLAUDE.md is now ${LINE_COUNT} lines (recommended: 50-100, max: 150). Consider splitting content using @import or delegating to .claude/rules/."
  }
  EOF
    fi
  fi

  exit 0
  ```

  **ユースケース 2: rules/ ファイルの path-scoped フロントマター検証（OPT-002 導入後）**
  ```bash
  #!/usr/bin/env bash
  # PostToolUse hook: rules/ 新規ファイルの path-scoped 確認
  set -euo pipefail

  TOOL_INPUT="${CLAUDE_TOOL_INPUT:-}"

  if echo "$TOOL_INPUT" | grep -q ".claude/rules/"; then
    FILE_PATH=$(echo "$TOOL_INPUT" | grep -oE '\.claude/rules/[^ "]+')
    if [ -f "$CLAUDE_PROJECT_DIR/$FILE_PATH" ]; then
      if ! head -3 "$CLAUDE_PROJECT_DIR/$FILE_PATH" | grep -q "^---"; then
        echo '{"decision":"block","reason":"INFO: New rules/ file without YAML frontmatter. Consider adding paths: for path-scoped loading to optimize context budget."}'
      fi
    fi
  fi

  exit 0
  ```

  **settings.json への追加:**
  ```json
  {
    "hooks": {
      "PostToolUse": [
        {
          "matcher": "Edit|Write",
          "hooks": [{
            "type": "command",
            "command": ".claude/hooks/posttooluse-quality-check.sh",
            "timeout": 5
          }]
        }
      ]
    }
  }
  ```

- **Expected Benefit**: CLAUDE.md の肥大化を自動検知し、コンテキスト最適化の維持を支援。rules/ ファイル作成時に path-scoped の設定漏れを警告
- **Impact**: 低（品質維持の補助。直接的な問題解決ではなく予防的措置）
- **Effort**: 低（シェルスクリプト作成。既存 hook テンプレート活用可能）
- **Risk**: PostToolUse hook の誤検知（CLAUDE.md 以外のファイルパスに "CLAUDE.md" が含まれる場合等）。緩和策: ファイルパスの完全一致チェックに改善。また `decision: "block"` は再試行を促すだけで作業を破壊しないため低リスク
- **Backlog Entry Draft**:
  - タイトル: PostToolUse hook による CLAUDE.md 行数チェック・rules/ フロントマター検証
  - 説明: Edit/Write 後に CLAUDE.md の行数（150行超過で警告）と rules/ ファイルの path-scoped フロントマター有無を自動検証する PostToolUse hook を導入する

---

## OPT-005: CLAUDE.md の import(@) 活用 + rules/ 委譲による 112行以下への縮小

- **CO ターゲット**: CO-005（CLAUDE.md）
- **Current State**: 192行（公式推奨50-100行の約2-4倍）。import(@) 未使用。ドキュメント整合性ルール（42行）、セッション終了時の気づき記録（23行）等のルール的内容が CLAUDE.md に混在
- **Proposed Change**: 3段階で分離し、192行 → 112行以下を目指す

  **Step 1: rules/ への委譲（-42行）**

  `ドキュメント整合性ルール` セクション（L87-L129、42行）を `.claude/rules/doc-integrity.md` に移動:
  ```yaml
  ---
  paths:
    - "docs/**"
    - ".claude/skills/**"
    - ".claude/rules/**"
  ---

  # ドキュメント整合性ルール

  `.claude/skills/` 配下のスキル・エージェント定義が正の情報源（Source of Truth）。
  `docs/workflow.md` はその人間向け可視化。

  **ルールファイルを変更した場合は、必ず `docs/workflow.md` も合わせて更新すること。**

  ## docs/ 文書分類
  ...（既存内容をそのまま移動）
  ```

  CLAUDE.md には1行のリファレンスのみ残す:
  ```markdown
  ## ドキュメント整合性ルール
  → `.claude/rules/doc-integrity.md` 参照（docs/ 編集時に自動読み込み）
  ```

  **Step 2: @import による分離（-23行）**

  `セッション終了時の気づき記録` セクション（L130-L153、23行）を分離ファイルに切り出し:

  分離先: `docs/session-end-notes-detail.md`
  ```markdown
  # セッション終了時の気づき記録（詳細）

  協働スタイルや設計に関する気づきが生まれたセッションの終了時に、以下の手順で記録する。
  ...（既存内容をそのまま移動）
  ```

  CLAUDE.md に @import を記載:
  ```markdown
  ## セッション終了時の気づき記録
  セッション終了時に気づきを inbox/ に記録する。
  @docs/session-end-notes-detail.md
  ```

  **Step 3: ディレクトリ構成詳細の圧縮（-15行）**

  `inbox と refs の使い分け`（L66-L69）+ `inbox と issues の使い分け`（L71-L79）の合計15行を分離:

  分離先: `docs/directory-usage-guide.md`

  CLAUDE.md に @import を記載:
  ```markdown
  ### 使い分けガイド
  @docs/directory-usage-guide.md
  ```

  **分離後の CLAUDE.md 構成（推定112行）:**

  | セクション | 行数 | 変更 |
  |-----------|------|------|
  | 概要 | 5 | 変更なし |
  | セッション構成 | 8 | 変更なし |
  | GitHub Actions からの実行 | 7 | 変更なし |
  | ファイル命名規則 | 5 | 変更なし |
  | 施策管理の必須化 | 8 | 変更なし |
  | 禁止事項 | 7 | 変更なし |
  | コマンド | 5 | 変更なし |
  | ディレクトリ構成と用途 | 12 | テーブルのみ残し、使い分けガイドを @import（-15） |
  | ドキュメント階層方針 | 6 | 変更なし |
  | ドキュメント整合性ルール | 2 | rules/ 委譲（-40）、リファレンス1行のみ |
  | セッション終了時の気づき記録 | 3 | @import に置き換え（-20） |
  | 文書分類ポリシー | 14 | 変更なし |
  | 環境分離ポリシー | 17 | 変更なし |
  | リポジトリ間の関係 | 5 | 変更なし |
  | 区切り線・空行 | ~8 | 変更なし |
  | **合計** | **~112** | **-80行** |

  **注意**: @import はインポート先を起動時にインラインで展開するため、コンテキスト消費量は変わらない。ただし CLAUDE.md ファイル自体の可読性・保守性が向上し、遵守率向上が期待できる。rules/ への委譲（Step 1）は path-scoped にすることで遅延読み込みとなり、実際のコンテキスト削減効果がある

- **Expected Benefit**: CLAUDE.md を 192行 → ~112行に縮小。公式推奨範囲の上限（100行）に近づき遵守率向上。rules/ 委譲分（42行）は path-scoped で遅延読み込みとなりコンテキスト節約
- **Impact**: 高（遵守率向上 + コンテキスト最適化。ISS-TEMP-004 の直接対策）
- **Effort**: 中（3ファイル作成 + CLAUDE.md 編集 + path-scoped YAML 設定。内容の変更なし、構造変更のみだがテストが必要）
- **Risk**: @import の再帰深度制限（5ホップ）に注意。緩和策: 1階層の import のみ使用し、深い階層は避ける。分離後に各セクションの読み込みを確認（`/context` コマンドで検証可能）
- **Backlog Entry Draft**:
  - タイトル: CLAUDE.md の import(@) + rules/ 委譲による 112行以下への縮小
  - 説明: CLAUDE.md（192行）からドキュメント整合性ルール（42行）を path-scoped rules に委譲、セッション終了時の気づき記録（23行）とディレクトリ使い分けガイド（15行）を @import で分離し、~112行に縮小する

---

## OPT-006: 高優先度プラグイン4件の段階的導入

- **CO ターゲット**: CO-006（プラグイン導入）
- **Current State**: 導入済みプラグイン 0件。plugin-reference スキルにて4件が「適用可能性: 高」と評価済み
- **Proposed Change**: 4件のプラグインを段階的に導入

  **導入順序（依存関係・リスクを考慮）:**

  | 順序 | プラグイン | 理由 | 導入コマンド |
  |------|----------|------|------------|
  | 1 | `claude-code-setup` | 設定最適化提案。本施策（config 最適化）との相乗効果が最も高い | `/plugin install claude-code-setup` |
  | 2 | `claude-md-management` | CLAUDE.md 品質維持。OPT-005 実施後の行数管理を自動化 | `/plugin install claude-md-management` |
  | 3 | `commit-commands` | git 操作標準化。既存の commit-message.md ルールとの整合性確認が必要 | `/plugin install commit-commands` |
  | 4 | `skill-creator` | スキル作成・改善・評価。既存24スキルの品質改善に活用 | `/plugin install skill-creator` |

  **導入スコープ**: Project（`.claude/settings.json` に追加、チーム共有）

  **settings.json への追加例:**
  ```json
  {
    "enabledPlugins": {
      "claude-code-setup@claude-plugins-official": true,
      "claude-md-management@claude-plugins-official": true,
      "commit-commands@claude-plugins-official": true,
      "skill-creator@claude-plugins-official": true
    }
  }
  ```

- **Expected Benefit**: 設定最適化・CLAUDE.md 品質維持・git 操作標準化・スキル品質改善を自動化。特に claude-code-setup は本施策の提案を自動で実装する際に有用
- **Impact**: 中（長期的な品質維持・自動化効果。ただし即時的な問題解決ではない）
- **Effort**: 中（各プラグインの動作検証 + 既存ルールとの整合性確認が必要。commit-commands は commit-message.md との競合可能性あり）
- **Risk**: プラグインが既存ルール（commit-message.md 等）と競合する可能性。緩和策: 1件ずつ導入しテスト。競合が発生した場合は `skippedPlugins` で即時無効化。commit-commands は commit-message.md との動作差分を事前検証
- **Backlog Entry Draft**:
  - タイトル: 高優先度プラグイン4件の段階的導入
  - 説明: plugin-reference で「適用可能性: 高」と評価済みの4件（claude-code-setup, claude-md-management, commit-commands, skill-creator）を段階的に導入する。1件ずつ導入・検証し、既存ルールとの整合性を確認する

---

## OPT-007: sandbox 有効化 + settings.local.json 導入

- **CO ターゲット**: CO-007（その他）、CO-001（settings.json）
- **Current State**: sandbox 未有効化。Bash コマンドがファイルシステム・ネットワークに無制限アクセス可能。settings.local.json 未使用。deny ルール非機能のため Bash 経由のセンシティブファイルアクセスも防止不可
- **Proposed Change**:

  **(A) sandbox 有効化:**

  **settings.json への追加:**
  ```json
  {
    "sandbox": {
      "enabled": true,
      "network": {
        "allowedDomains": [
          "github.com",
          "api.github.com"
        ]
      }
    }
  }
  ```

  **効果:**
  - Bash コマンドのファイルシステムアクセスが作業ディレクトリ + サブディレクトリに制限
  - OS カーネルレベルで deny ルールを強制（settings.json の deny 非機能を補完）
  - ネットワークアクセスを github.com のみに制限（gh コマンドの動作を保証）

  **(B) settings.local.json 導入:**

  **`.claude/settings.local.json`（.gitignore 推奨）:**
  ```json
  {
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "env": {
      "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "16384",
      "SLASH_COMMAND_TOOL_CHAR_BUDGET": "20000"
    }
  }
  ```

  **`.gitignore` への追加:**
  ```
  .claude/settings.local.json
  ```

  **(C) permissions.ask の導入（評価者補足対応）:**

  Phase 2 評価者から `permissions.ask` 未使用が指摘されている。高リスク操作（`rm -rf` 等）を deny ではなく ask に設定することで、正当な使用時にユーザー確認を求めるフローが可能:

  ```json
  {
    "permissions": {
      "ask": [
        "Bash(rm -rf *)"
      ]
    }
  }
  ```

  注: deny ルール非機能が修正された場合、`Bash(rm -rf *)` は deny に戻すことを推奨

- **Expected Benefit**: OPT-001（PreToolUse hook）と合わせて二重防御を実現。sandbox はカーネルレベルのガードであり、hook の誤検知やバイパスを補完する。settings.local.json は個人設定の分離先として機能
- **Impact**: 高（セキュリティの根本的改善。sandbox は deny ルール非機能の最も確実な代替手段）
- **Effort**: 低（settings.json に数行追加のみ。ただし sandbox 有効化後の既存 Bash コマンドの動作検証が必要）
- **Risk**: sandbox がビルドツールや外部コマンドの実行を制限する可能性。緩和策: `sandbox.network.allowedDomains` に必要なドメインを追加。問題発生時は `sandbox.enabled: false` で即時無効化可能。段階的に導入（まず sandbox のみ、次に network 制限）を推奨
- **Backlog Entry Draft**:
  - タイトル: sandbox 有効化 + settings.local.json 導入
  - 説明: sandbox を有効化しカーネルレベルのファイルシステム・ネットワーク制限を導入する。PreToolUse hook（別施策）と合わせて二重防御を構成。settings.local.json を個人設定分離先として導入する

---

## Impact x Effort マトリクス

```
              │  低 Effort     │  中 Effort     │  高 Effort
─────────────┼────────────────┼────────────────┼──────────────
高 Impact    │ Quick Wins     │ Strategic      │
             │ OPT-003 (GHA)  │ OPT-001 (hook) │
             │ OPT-007 (sbox) │ OPT-005 (MD)   │
─────────────┼────────────────┼────────────────┼──────────────
中 Impact    │ Quick Wins     │ Nice-to-Have   │
             │ OPT-002 (rules)│ OPT-006 (plug) │
─────────────┼────────────────┼────────────────┼──────────────
低 Impact    │ Easy Adds      │                │
             │ OPT-004 (post) │                │
─────────────┴────────────────┴────────────────┴──────────────
```

### 分類サマリ

| 分類 | 提案 | 推奨実施順序 |
|------|------|------------|
| **Quick Wins**（高Impact/低Effort） | OPT-003（GHA disable-model-invocation）、OPT-007（sandbox 有効化）、OPT-002（path-scoped rules） | 第1弾: 即時実施 |
| **Strategic**（高Impact/中Effort） | OPT-001（PreToolUse hook）、OPT-005（CLAUDE.md 縮小） | 第2弾: Quick Wins 後に実施 |
| **Easy Adds**（低Impact/低Effort） | OPT-004（PostToolUse hook） | 第3弾: OPT-001/005 と並行可 |
| **Nice-to-Have**（中Impact/中Effort） | OPT-006（プラグイン導入） | 第4弾: 他施策完了後に段階的導入 |

### 推奨実施ロードマップ

**第1弾（即時実施可能 — Quick Wins）:**
1. OPT-003: GHA スキル6件に `disable-model-invocation: true` を追加（作業時間: ~15分）
2. OPT-007: sandbox 有効化（作業時間: ~30分、動作検証含む）
3. OPT-002: path-scoped rules 導入 + commit-message.md 分離（作業時間: ~1時間）

**第2弾（計画的実施 — Strategic）:**
4. OPT-001: PreToolUse hook 実装（作業時間: ~2時間、テスト含む）
5. OPT-005: CLAUDE.md 縮小（作業時間: ~1.5時間、分離 + 検証）

**第3弾（補助的実施 — Easy Adds）:**
6. OPT-004: PostToolUse hook（作業時間: ~1時間）

**第4弾（段階的導入 — Nice-to-Have）:**
7. OPT-006: プラグイン4件の段階的導入（作業時間: ~2時間、検証含む）

---

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA スキル数は6件（Phase 2 では5件と報告） | `.claude/skills/gha-*/SKILL.md` | gha-guideline も `user-invocable: false` の GHA 関連スキルであり、`disable-model-invocation: true` の対象に含めるべき。Phase 2 の ISS-TEMP-005 を6件に修正 |
| 2 | @import はインライン展開のためコンテキスト削減にならない | CLAUDE.md | @import は可読性・保守性の向上には効果的だが、コンテキスト消費量は変わらない。実際のコンテキスト削減には rules/ への委譲（path-scoped）が必要 |
| 3 | sandbox + PreToolUse hook の二重防御が設計上の最適解 | `.claude/settings.json` + `.claude/hooks/` | sandbox はカーネルレベル（バイパス不可）、hook はアプリケーションレベル（柔軟だがバイパスリスク）。両方を組み合わせることで深層防御を実現 |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | PreToolUse hook は JSON 出力（hookSpecificOutput）と exit code 2 の2パターンがある | JSON パターンは deny 理由を構造化できるが実装が複雑。exit code 2 パターンはシンプルだが stderr 出力のみ。本提案では exit code 2 を推奨（シンプルさ優先） |
| 2 | PostToolUse hook の `decision: "block"` は再試行を促すだけで作業を破壊しない | block は「ブロッキングエラー」ではなく「再検討を促す」動作。Claude は代替アプローチを試みる。品質ゲートとして安全に使用可能 |
| 3 | permissions.ask は deny 非機能時の中間的な代替策 | deny が機能しない場合、ask を使えばユーザー確認を求めるフローが可能。ただし SDK 環境（インタラクティブユーザー不在）では機能しない点に注意 |

---
**作成者**: config-proposal-worker
**作成日**: 2026-03-15
