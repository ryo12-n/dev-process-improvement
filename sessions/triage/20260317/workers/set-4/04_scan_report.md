# スキャンレポート: Set-4

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-010 | GHA ↔ Skills 整合性チェック | 完了 |

## TG-010: GHA ↔ Skills 整合性チェック

### 走査結果サマリ
- マッピング数: 2件
- ドリフト検出: CRITICAL 1件 / WARNING 3件 / INFO 4件

### マッピング別結果

#### triage-gha

| チェックポイント | Skill側 | GHA側 | ドリフト | 重大度 |
|----------------|---------|-------|---------|--------|
| task_ids | TG-001〜TG-010 (10件) | TG-001〜TG-010 (10件) | なし（完全一致） | - |
| workflow_steps | 8ステップ（セッションフォルダ作成〜アクション実施） | 9ステップ（ステップ1〜ステップ9）。「ディスパッチログの記録」が追加 | GHA 側に「ディスパッチログの記録」が追加されているが、Skill 側のディスパッチログ記録は `02_dispatch_log.md` として作業フロー内に含まれている。実質的な欠落ではない | INFO |
| report_sections | inbox, backlog 棚卸し, 課題管理 CSV, backlog 関係性分析, initiative 状態確認, 知見集約, 課題集約（全7セクション） | 同7セクションに対応する記述あり（ステップ2事前調査 + ステップ4走査 + ステップ6集約に分散） | なし（構造は異なるが内容は網羅） | - |
| file_templates | `sessions/triage/_template/` + 個別ファイル参照（00_pre_investigation.md, 01_plan.md, 03_report.md, 04_gate_review.md, workers/_template/07_issues.md） | `sessions/triage/_template/` + `sessions/triage/_template/workers/_template/`（上位ディレクトリのみ） | Skill 側は個別テンプレートファイルを明示的に参照、GHA 側はディレクトリレベルの参照のみ。実運用上の影響なし | INFO |

#### l1-auto-execute-gha

| チェックポイント | Skill側 | GHA側 | ドリフト | 重大度 |
|----------------|---------|-------|---------|--------|
| file_numbers | 00〜08 基本ファイル + 00a_wallbash_log.md, 02a_task_division.md, 03_work_log_W_template.md, 07_issues_W_template.md (計13種) | 00〜08 基本ファイル (9種) | Skill 側に追加4ファイル（00a_wallbash_log.md, 02a_task_division.md, 03_work_log_W_template.md, 07_issues_W_template.md）。ただし GHA execute は単一エージェントで壁打ちログ・計画ワーカー・並列ディスパッチを省略するため、これらは inherent_differences の範疇 | INFO |
| workflow_steps | _template コピー → proposal/plan/tasks 作成 → worker 実行 → evaluator 実行 → gate_review 作成 → backlog エントリ削除 | proposal 読み取り → plan/tasks 作成/補完 → worker 実行 → evaluator 実行 → gate_review 作成（5ステップ） | (1) 「_template コピー」欠落: GHA execute は wallbash フェーズで施策ディレクトリが作成済みのため不要 (2) 「backlog エントリ削除」欠落: GHA execute にはこのステップがない | WARNING |
| file_templates | `sessions/initiatives/_template/` + 個別テンプレート参照（03_work_log.md, 04_work_report.md, 05_eval_plan.md, 06_eval_report.md, 07_issues.md, 00a_wallbash_log.md, 03_work_log_W_template.md, 07_issues_W_template.md） | テンプレート参照なし | GHA execute はテンプレートコピーを行わないため参照なし。inherent_differences の範疇（施策ディレクトリは wallbash フェーズで作成済み） | INFO |

**マニフェスト自体のドリフト（CRITICAL）**:

| 項目 | マニフェスト記載 | 実態 | 重大度 |
|------|----------------|------|--------|
| `gha_source.path` | `.github/workflows/backlog-auto-execute.yml` | `.github/workflows/initiative-execute.yml`（ワークフロー）+ `.claude/skills/gha-execute/SKILL.md`（プロンプト本体） | CRITICAL |
| `gha_source.type` | `workflow-inline` | ワークフローのプロンプトは `gha-execute/SKILL.md` への Read 指示であり inline ではない | WARNING |
| `gha_source.prompt_location` | `jobs.execute.steps[2].with.prompt` | steps[2] は "Get issue title" ステップ。Claude Code 実行は steps[5]（"Run Claude Code" ステップ） | WARNING |

#### inherent_differences 検証

##### triage-gha (5件)

| mapping-id | カテゴリ | 宣言 | 実態 | 判定 |
|-----------|---------|------|------|------|
| triage-gha | wall-beating-omission | GHA 版は非対話のため壁打ちフェーズを省略 | GHA プロンプトに「壁打ちフェーズは省略し、直接走査を開始する」と明記。制約事項に「ユーザーへの確認待ち・壁打ちフェーズは実施しない」と記載 | 有効 |
| triage-gha | single-agent-mode | GHA 版はサブエージェント不使用、単一エージェントで逐次実行 | GHA プロンプトに「単一エージェント: サブエージェント（Task ツール）は使用できない」と明記 | 有効 |
| triage-gha | no-commit | GHA 版はコミット不要（GHA ワークフローが担当） | GHA プロンプトに「コミット不要: ファイルの作成・編集のみ行う。コミット・プッシュ・PR 作成は GHA ワークフローが行う」と明記 | 有効 |
| triage-gha | no-todo-registration | GHA 版はセッションライフサイクル todo 登録不要 | GHA プロンプトに「セッションライフサイクル todo 登録不要: TaskCreate/TaskUpdate は使用しない」と明記 | 有効 |
| triage-gha | no-branch-cleanup | GHA 版はブランチ整理不要（クリーン環境） | GHA プロンプトに「ブランチ整理不要: GHA が毎回クリーンな環境で実行するため」と明記 | 有効 |

##### l1-auto-execute-gha (3件)

| mapping-id | カテゴリ | 宣言 | 実態 | 判定 |
|-----------|---------|------|------|------|
| l1-auto-execute-gha | wall-beating-omission | 自動実行のため壁打ちフェーズを省略 | `gha-execute/SKILL.md` の approve フローに壁打ちフェーズの記述なし。ただし「既存の壁打ちドラフト」を読み取る記述はあり（これは wallbash フェーズの成果物読み取りであり、壁打ちフェーズの実施ではない） | 有効 |
| l1-auto-execute-gha | single-agent-mode | 単一エージェントで全ロールを順次実行 | `gha-execute/SKILL.md` に「L2-worker として」「L2-evaluator として」と記載。サブエージェント起動ではなく自身で順次実行する構造 | 有効 |
| l1-auto-execute-gha | scope-restriction | 対象リポジトリは dev-process-improvement のみ | `gha-execute/SKILL.md` に「対象リポジトリは dev-process-improvement のみ」と明記 | 有効 |

### ドリフト詳細（CRITICAL）

#### CRITICAL-001: マニフェスト `l1-auto-execute-gha` の `gha_source.path` 不正

**現状**: マニフェストの `gha_source.path` が `.github/workflows/backlog-auto-execute.yml` を指しているが、このファイルは存在しない。

**実態**:
- 実際のワークフロー: `.github/workflows/initiative-execute.yml`
- 実際のプロンプト本体: `.claude/skills/gha-execute/SKILL.md`（ワークフローの Claude Code ステップから Read で読み込まれる）

**影響**: TG-010 の自動チェックツールを将来作成した場合、このマッピングのチェックが実行不可能になる。現状は手動チェックのため実害は限定的だが、マニフェストの信頼性に影響する。

**推奨アクション**: マニフェストの `l1-auto-execute-gha` を以下のように修正する:
- `gha_source.path`: `.github/workflows/initiative-execute.yml` に修正
- `gha_source.type`: 実際の構造を反映する形に修正（`skill-reference` 等の新タイプ、または GHA ソースを `gha-execute/SKILL.md` に変更して `type: prompt` にする）
- `gha_source.prompt_location`: 削除するか `jobs.execute.steps[5].with.prompt` に修正（ただし実際は inline prompt ではなく skill 参照）

### ドリフト詳細（WARNING）

#### WARNING-001: `l1-auto-execute-gha` の workflow_steps 不一致

マニフェストの `workflow_steps.keys` に「_template コピー」と「backlog エントリ削除」が含まれているが、`gha-execute/SKILL.md` にはこれらのステップが存在しない。

- 「_template コピー」: GHA execute は wallbash フェーズで施策ディレクトリが作成済みであるため不要。inherent_differences に宣言すべき差異。
- 「backlog エントリ削除」: GHA execute フローには存在しない。initiative-dispatcher または他のワークフローが担当している可能性。inherent_differences に宣言すべき差異。

**推奨アクション**: 以下のいずれかで対応する:
1. マニフェストの `workflow_steps.keys` を実態に合わせて修正する（「_template コピー」「backlog エントリ削除」を削除）
2. `inherent_differences` に `template-copy-omission` と `backlog-deletion-omission` を追加する

#### WARNING-002: `l1-auto-execute-gha` の `gha_source.type` 不正

`type: workflow-inline` と宣言されているが、実際のプロンプトは外部スキルファイル（`.claude/skills/gha-execute/SKILL.md`）への Read 指示であり、inline prompt ではない。

#### WARNING-003: `l1-auto-execute-gha` の `prompt_location` 不正

`prompt_location: "jobs.execute.steps[2].with.prompt"` と宣言されているが、steps[2] は "Get issue title" ステップ。Claude Code の実行は steps[5]（"Run Claude Code" ステップ、0-indexed）。

## 課題起票

- 起票件数: 2 件（`07_issues.md` に起票済み）
- マニフェストの gha_source.path 不正（l1-auto-execute-gha）
- l1-auto-execute-gha: backlog エントリ削除ステップの欠落

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA ソースの参照構造パターンとして `skill-reference` タイプが必要 | `.github/gha-skills-mapping.yml` | `initiative-execute.yml` はプロンプト本体を `gha-execute/SKILL.md` に外部化している。マニフェストの `gha_source.type` に `workflow-inline` と `prompt` 以外のパターン（例: `skill-reference`）を追加するか、`skill_source` 側に GHA 専用スキルも含める設計が必要 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | triage-gha マッピングは高い整合性を維持している | 前回トリアージ（20260315-2）以降の変更が GHA プロンプト側にも適切に反映されている。TG-001〜TG-010 の全タスク ID、ワークフローステップ、レポートセクションが一致しており、inherent_differences も全件有効 |
| 2 | l1-auto-execute-gha マッピングはマニフェスト定義自体に課題がある | ワークフローファイル名の変更（backlog-auto-execute → initiative-execute）やプロンプトの外部化（inline → skill 参照）がマニフェストに反映されていない。GHA ワークフローの構造変更時にマニフェスト更新を連動させるプロセスが必要 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-17
