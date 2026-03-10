# 作業レポート: AI補助自動化ツール検討

## サマリ

`.claude/skills/`（10スキル）、`.claude/rules/`（3ルール）、`.claude/skills/*/agents/`（8エージェント）、`.claude/settings.json`、`CLAUDE.md` を走査し、手動で繰り返される定型作業を **14件** 抽出した。Claude Code hooks（18種のライフサイクルイベント、4種のハンドラー型）/ MCP tools / シェルスクリプト / skills 拡張の4手段で自動化可能性を調査し、費用対効果の高い上位3件についてロードマップを策定した。

---

## T-001: 定型作業一覧

以下の14件の定型作業を抽出した。

| # | 定型作業 | 発生源 | 説明 |
|---|---------|--------|------|
| R-001 | セッション開始時のブランチ整理 | `.claude/rules/session-start-branch-cleanup.md` | 7ステップの手順（ブランチ確認→未プッシュ確認→プッシュ→PR確認/作成→main切替→外部リポ整理→通常フローへ）。L1/triage/meta/sync の全マネージャーセッション開始時に毎回実行 |
| R-002 | コミットメッセージ規約の遵守 | `.claude/rules/commit-message.md` | `[session-type] category: summary` 形式の厳守。session-type と category の対応表に基づく。毎コミット時に確認が必要 |
| R-003 | PR URL 出力形式の統一 | `.claude/rules/pr-url-output.md` | プレーンテキスト形式での出力（バッククォート・リンク記法の禁止） |
| R-004 | テンプレートコピーと施策ディレクトリ作成 | `.claude/skills/l1-manager/SKILL.md` | `_template/` をコピーして `sessions/initiatives/<施策名>/` を作成 |
| R-005 | 壁打ちフェーズの実施 | 全エージェント定義 | 理解サマリー・前提条件チェック・不明点列挙を定型フォーマットで記録 |
| R-006 | 作業履歴のタイムスタンプ付き記録 | 全 worker エージェント | `03_work_log.md` にタスクID・状態・作業内容・成果物・課題を記録 |
| R-007 | 知見記録（ルール化候補・参考情報） | 全 worker/evaluator エージェント | レポートに「ルール化候補」「参考情報」テーブルを最低1行記載 |
| R-008 | 課題起票・CSV転記 | 全 worker/evaluator エージェント | `07_issues.md` → `プロセス改善_課題管理.csv` → `issues/entries/ISS-XXX.md` の3段階転記 |
| R-009 | ゲート判定の実施 | `.claude/skills/l1-manager/SKILL.md` | 3択判定（通過/条件付き通過/差し戻し）＋判定理由＋知見ルーティング |
| R-010 | 施策クローズ・アーカイブ移動 | `.claude/skills/l1-manager/SKILL.md` | `sessions/initiatives/<施策名>/` → `_archive/` への移動、PR作成 |
| R-011 | トリアージ走査（inbox/backlog/CSV） | `.claude/skills/triage-manager/SKILL.md` | inbox/backlog/CSV の状態確認、ボリューム見積もり、セット分割 |
| R-012 | ルール変更時の連動更新チェック | `.claude/skills/rule-change-checklist/SKILL.md` | 7項目のチェック（関連ファイル確認、workflow.md更新、TG-008基準、パス走査等） |
| R-013 | マネージャー共通ポリシーの遵守 | `.claude/skills/manager-common-policy/SKILL.md` | サブエージェント起動パターン・知見ルーティング・品質チェックの共通手順 |
| R-014 | 外部リポジトリの整理（セッション開始時） | `.claude/rules/session-start-branch-cleanup.md` ステップ6 | アクティブ施策の `00_proposal.md` を走査し、外部リポのブランチ整理を実施 |

---

## T-002: 自動化手段の調査

### Claude Code hooks の仕様概要（公式ドキュメント確認結果）

**ライフサイクルイベント（18種）**:

| イベント | 発火タイミング | matcher 対象 |
|---------|-------------|-------------|
| SessionStart | セッション開始/再開時 | startup, resume, clear, compact |
| UserPromptSubmit | プロンプト送信時 | matcher なし |
| PreToolUse | ツール呼び出し前（ブロック可能） | ツール名 (Bash, Edit, Write 等) |
| PermissionRequest | 権限ダイアログ表示時 | ツール名 |
| PostToolUse | ツール呼び出し成功後 | ツール名 |
| PostToolUseFailure | ツール呼び出し失敗後 | ツール名 |
| Notification | 通知発生時 | 通知タイプ |
| SubagentStart | サブエージェント起動時 | エージェントタイプ |
| SubagentStop | サブエージェント完了時 | エージェントタイプ |
| Stop | Claude の応答完了時 | matcher なし |
| TeammateIdle | チームメイトのアイドル時 | matcher なし |
| TaskCompleted | タスク完了マーク時 | matcher なし |
| InstructionsLoaded | CLAUDE.md / rules ファイルのロード時 | matcher なし |
| ConfigChange | 設定ファイル変更時 | 設定ソース |
| WorktreeCreate | worktree 作成時 | matcher なし |
| WorktreeRemove | worktree 削除時 | matcher なし |
| PreCompact | コンテキスト圧縮前 | manual, auto |
| SessionEnd | セッション終了時 | 終了理由 |

**ハンドラー型（4種）**:

| 型 | 説明 | 用途 |
|---|------|------|
| command | シェルコマンドを実行。stdin で JSON 入力、stdout で JSON 出力 | スクリプトベースの自動化 |
| http | HTTP POST で外部サーバーにイベント送信 | 外部サービス連携 |
| prompt | Claude モデルに単一ターン評価を依頼（yes/no 判定） | セマンティックなチェック |
| agent | サブエージェントを起動し、Read/Grep/Glob で条件検証 | 複雑な検証ロジック |

**設定場所**: `.claude/settings.json`（プロジェクトスコープ、コミット可能）

**主要な機能**:
- `async: true` でバックグラウンド実行可能
- matcher は正規表現（例: `Edit|Write` で両方にマッチ）
- PreToolUse で `permissionDecision: "deny"` を返すとツール実行をブロック可能
- PostToolUse で `addToConversation` フィールドで Claude に情報を伝達可能

### 各定型作業の自動化手段

| # | 定型作業 | 推奨自動化手段 | 実現可能性 | 備考 |
|---|---------|-------------|-----------|------|
| R-001 | ブランチ整理 | **SessionStart hook** (command) | 高 | 7ステップをシェルスクリプト化。matcher: `startup|resume` で新規・再開時に自動実行 |
| R-002 | コミットメッセージ規約 | **PreToolUse hook** (command, matcher: Bash) | 高 | git commit を含む Bash コマンドを検知し、メッセージ形式を正規表現バリデーション。不適合なら deny |
| R-003 | PR URL 出力形式 | **Stop hook** (prompt) | 中 | prompt ハンドラーで「PR URL がプレーンテキストか」をセマンティックチェック |
| R-004 | テンプレートコピー | **シェルスクリプト** | 中 | `cp -r` の1コマンド化。施策名の入力が必要なため完全自動化は困難 |
| R-005 | 壁打ちフェーズ | **skills 拡張** | 低 | 対話的プロセスのため自動化不向き。テンプレート化で効率化は可能 |
| R-006 | 作業履歴記録 | **PostToolUse hook** (command) | 中 | タイムスタンプ自動付与は可能だが、内容の記述は手動が必要 |
| R-007 | 知見記録チェック | **Stop hook** (agent) | 中 | セッション終了時に agent ハンドラーで知見テーブルの記載有無をチェック |
| R-008 | 課題起票・CSV転記 | **シェルスクリプト** | 中 | ISS-XXX の採番と CSV 追記をスクリプト化。テンプレート生成も自動化可能 |
| R-009 | ゲート判定 | **skills 拡張** | 低 | 判断を伴うため自動化不向き。チェックリストの自動生成は可能 |
| R-010 | 施策クローズ | **シェルスクリプト** | 高 | git mv + CSV更新 + git add/commit + gh pr create をスクリプト化可能 |
| R-011 | トリアージ走査 | **シェルスクリプト** | 中 | inbox/backlog のファイル数カウント・CSV 状態サマリーをスクリプト化可能 |
| R-012 | ルール変更連動チェック | **PostToolUse hook** (command, matcher: `Edit|Write`) | 中 | `.claude/skills/` や `.claude/rules/` へのファイル変更を検知し、関連ファイル一覧を走査して通知 |
| R-013 | マネージャー共通ポリシー | **skills 拡張** | 低 | 対話的プロセスのため自動化不向き |
| R-014 | 外部リポ整理 | **SessionStart hook** (command) | 高 | R-001 のスクリプトに統合して実装可能 |

---

## T-003: 費用対効果評価表

### 評価基準
- **頻度**: 毎セッション=3 / 毎施策=2 / 不定期=1
- **手動コスト**: 高=3（5分以上/複数ステップ/ミスしやすい）/ 中=2（2-5分）/ 低=1（1分未満）
- **実装難易度**: 高=3（セマンティック判断・複雑ロジック）/ 中=2（中程度のスクリプト）/ 低=1（単純なコマンド/設定変更）
- **優先度スコア** = (頻度 x 手動コスト) / 実装難易度（高いほど優先）

| # | 定型作業 | 頻度 | 手動コスト | 実装難易度 | 自動化手段 | 優先度スコア | 順位 |
|---|---------|------|-----------|-----------|-----------|------------|------|
| R-001 | ブランチ整理 | 3 | 3 | 1 | SessionStart hook | **9.0** | **1** |
| R-014 | 外部リポ整理 | 3 | 2 | 1 | SessionStart hook (R-001統合) | **6.0** | **2** |
| R-002 | コミットメッセージ規約 | 3 | 2 | 1 | PreToolUse hook | **6.0** | **2** |
| R-010 | 施策クローズ | 2 | 3 | 1 | シェルスクリプト | **6.0** | **2** |
| R-008 | 課題起票・CSV転記 | 2 | 2 | 1 | シェルスクリプト | **4.0** | 5 |
| R-012 | ルール変更連動チェック | 2 | 3 | 2 | PostToolUse hook | **3.0** | 6 |
| R-004 | テンプレートコピー | 2 | 1 | 1 | シェルスクリプト | **2.0** | 7 |
| R-007 | 知見記録チェック | 2 | 1 | 1 | Stop hook | **2.0** | 7 |
| R-011 | トリアージ走査 | 1 | 2 | 1 | シェルスクリプト | **2.0** | 7 |
| R-006 | 作業履歴記録 | 3 | 1 | 2 | PostToolUse hook | **1.5** | 10 |
| R-003 | PR URL 出力形式 | 3 | 1 | 2 | Stop hook (prompt) | **1.5** | 10 |
| R-009 | ゲート判定 | 2 | 2 | 3 | skills 拡張 | **1.3** | 12 |
| R-013 | マネージャー共通ポリシー | 3 | 1 | 3 | skills 拡張 | **1.0** | 13 |
| R-005 | 壁打ちフェーズ | 3 | 1 | 3 | skills 拡張 | **1.0** | 13 |

> R-014 は R-001 のスクリプトに統合して実装するため、独立ロードマップ項目としない。実質の上位3件は **R-001（ブランチ整理）、R-002（コミットメッセージ規約）、R-012（ルール変更連動チェック）**。

---

## T-004: 優先度付きロードマップ

### Phase 1: 即時実施可能・高効果（上位3件）

#### 順位1: セッション開始時ブランチ整理の自動化（R-001 + R-014、スコア 9.0 + 6.0）

**手段**: SessionStart hook + command ハンドラー + シェルスクリプト

**実装方針**:
1. `.claude/hooks/session-start-branch-cleanup.sh` を作成
2. `.claude/settings.json` の `hooks.SessionStart` に登録
3. スクリプト処理内容:
   - `git branch --show-current` で現在ブランチを確認
   - main 以外: 未プッシュコミット確認 → push → PR確認/作成 → main 切替
   - main: `git pull` のみ
   - 外部リポジトリ走査: `sessions/initiatives/` 配下の `00_proposal.md` を grep して外部リポパスを抽出し、同じフローを `git -C <path>` で実行
4. 結果を JSON で stdout に出力

**設定例**:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/session-start-branch-cleanup.sh"
          }
        ]
      }
    ]
  }
}
```

**注意点**:
- SessionStart の matcher で `startup|resume` を指定し、`clear` / `compact` では実行しない設定を推奨
- `gh pr create` 失敗時はエラー報告のみとし、セッションをブロックしない
- 既存の `.claude/rules/session-start-branch-cleanup.md` はルールの方針定義として残し、実行ロジックはスクリプトに移行

**対象環境**: CLI / SDK 共通

---

#### 順位2: コミットメッセージ規約の自動バリデーション（R-002、スコア 6.0）

**手段**: PreToolUse hook + command ハンドラー（matcher: `Bash`）

**実装方針**:
1. `.claude/hooks/check-commit-message.sh` を作成
2. `.claude/settings.json` の `hooks.PreToolUse` に登録（matcher: `Bash`）
3. スクリプト処理内容:
   - stdin から JSON を読み取り、`tool_input.command` を抽出
   - `git commit` コマンドかどうかを判定（それ以外は即 exit 0）
   - `-m` オプションの値を抽出
   - 正規表現 `^\[(L1|L2-worker|L2-evaluator|triage-mgr|triage-worker|triage-eval|meta-mgr|meta-worker|meta-eval|sync|sync-mgr|sync-worker|sync-eval|maintenance)\] .+: .+` でバリデーション
   - 不適合: `permissionDecision: "deny"` + 理由を返す
   - 適合: exit 0

**設定例**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/check-commit-message.sh"
          }
        ]
      }
    ]
  }
}
```

**注意点**:
- HEREDOC 形式のコミットメッセージ（`git commit -m "$(cat <<'EOF' ...)"` ）への対応が必要
- `git commit` 以外の Bash コマンドでは即 exit 0 を返しパフォーマンス影響を最小化
- session-type の許容値リストは将来の拡張に備え、設定ファイルから読み込む方式も検討

**対象環境**: CLI / SDK 共通

---

#### 順位3: ルール変更連動更新チェックの自動化（R-012、スコア 3.0）

**手段**: PostToolUse hook + command ハンドラー（matcher: `Edit|Write`）

**実装方針**:
1. `.claude/hooks/check-rule-change.sh` を作成
2. `.claude/settings.json` の `hooks.PostToolUse` に登録（matcher: `Edit|Write`）
3. スクリプト処理内容:
   - stdin から JSON を読み取り、`tool_input.file_path` を抽出
   - パスが `.claude/skills/` または `.claude/rules/` 配下かどうかを判定（それ以外は即 exit 0）
   - 該当する場合: 変更ファイル内の「関連ファイル一覧」セクションを grep で検出
   - 関連ファイル一覧がある場合: リストアップされたファイルパスを抽出し、`addToConversation` で Claude に通知（「以下の連動更新を確認してください: ...」）
   - `docs/workflow.md` の更新リマインダーも併せて通知

**設定例**:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/check-rule-change.sh"
          }
        ]
      }
    ]
  }
}
```

**注意点**:
- PostToolUse はブロックではなく通知型（`addToConversation` で情報提供）
- `.claude/skills/` や `.claude/rules/` 以外のファイル変更では即 exit 0 で処理をスキップし、パフォーマンス影響を最小化
- `docs/workflow.md` の自動更新はセマンティックな作業が必要なためリマインダー通知にとどめる

**対象環境**: CLI / SDK 共通

---

### Phase 2（中期・順位1-3の知見を活用）

| # | 定型作業 | 手段 | 備考 |
|---|---------|------|------|
| R-010 | 施策クローズ・アーカイブ移動 | シェルスクリプト | git mv + PR 作成をスクリプト化 |
| R-008 | 課題起票・CSV転記 | シェルスクリプト | ISS-XXX 採番の自動化 |
| R-007 | 知見記録チェック | Stop hook (agent) | レポートの知見テーブルが空なら警告 |

### Phase 3（長期・検討段階）

| # | 定型作業 | 手段 | 備考 |
|---|---------|------|------|
| R-005 | 壁打ちフェーズ | skills 拡張 | テンプレート自動展開の検討 |
| R-009 | ゲート判定 | skills 拡張 | チェックリスト自動生成の検討 |

---

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | 定型作業の洗い出し | 10件以上 | 14件 | 計画超過（4件多い）。skills 10ファイル、agents 8ファイル、rules 3ファイルを走査 |
| T-002 | 自動化手段の調査 | 全候補に手段を記載 | 14件全てに記載 | 公式ドキュメントで hooks 仕様（18イベント、4ハンドラー型）を確認 |
| T-003 | 費用対効果の評価表 | 4軸評価+スコア算出 | 14件全てに算出 | 計画通り |
| T-004 | ロードマップ策定 | 上位3件の提案 | 3件 + Phase 2/3 | 計画通り |
| T-005 | レポート・知見記録 | レポート+知見1行以上 | 完了 | 計画通り |

## 成果物一覧
- 定型作業一覧（14件）
- 自動化手段調査結果（14件、hooks 仕様の詳細調査含む）
- 費用対効果評価表（14件、優先度スコア付き）
- 優先度付きロードマップ（Phase 1: 3件、Phase 2: 3件、Phase 3: 2件）

## 発生した課題
なし

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | SessionStart hook でブランチ整理を自動化すれば、`.claude/rules/session-start-branch-cleanup.md` のルール定義を hooks 設定に移行でき、手順書と実行ロジックの二重管理を解消できる | `.claude/rules/session-start-branch-cleanup.md` | ルールファイルは「方針」のみ残し、手順の実行はスクリプトに委譲する設計が望ましい |
| 2 | PreToolUse hooks の deny 機能でコミットメッセージの形式バリデーションを guaranteed execution にできる | `.claude/rules/commit-message.md` | 現在はルール記載のみで遵守を依存しているが、hooks で形式チェックを強制できる |
| 3 | PostToolUse hooks で `.claude/skills/` 変更時の連動更新リマインダーを自動通知できる | `.claude/skills/rule-change-checklist/SKILL.md` | Edit/Write 完了後に対象パスをチェックし、「関連ファイル一覧」セクションの走査結果を addToConversation で通知 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | Claude Code hooks は 2026年2月時点で18種のライフサイクルイベントと4種のハンドラー型（command, http, prompt, agent）をサポート | 公式ドキュメント https://code.claude.com/docs/en/hooks で確認。prompt ハンドラーはセマンティックチェック、agent ハンドラーは複雑な検証に有用 |
| 2 | 優先度スコアの上位は「毎セッション実施 x 手動コスト高 x 実装容易」の組み合わせに集中する。ブランチ整理（スコア9.0）が突出して高い | 費用対効果分析の傾向。今後の自動化施策の優先順位付けにも同じ評価軸が使える |

## 所感・次フェーズへの申し送り
- ブランチ整理の自動化（SessionStart hook）は最も費用対効果が高く、即時着手を推奨する
- コミットメッセージバリデーション（PreToolUse hook）は実装が容易で効果も高い
- 3件とも hooks ベースで実装可能であり、別々の施策として backlog に起票することを推奨
- hooks は `.claude/settings.json` への追記で済むため、既存のスキル・エージェント構成に影響を与えずに段階的に導入可能

---
**作成者**: L2（実施）
**作成日**: 2026-03-10
