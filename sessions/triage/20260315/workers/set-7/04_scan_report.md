# スキャンレポート: Set-7

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-010 | GHA/Skills 整合性チェック | 完了 |

## TG-010: GHA ↔ Skills 整合性チェック

### 走査結果サマリ
- マッピング数: 2件（triage-gha, l1-auto-execute-gha）
- ドリフト検出: CRITICAL 0件 / WARNING 0件 / INFO 1件
- 未マッピングワークフロー: 6件（うちマッピング追加推奨 3件）

### マッピング別結果

#### triage-gha

**概要**: トリアージセッションの GHA プロンプト ↔ スキル定義

| チェックポイント | Skill側 | GHA側 | ドリフト | 重大度 |
|----------------|---------|-------|---------|--------|
| task_ids (`TG-\d{3}`) | TG-001〜TG-010 | TG-001〜TG-010 | なし | - |
| workflow_steps | 8ステップ（作業フロー1〜8） | 9ステップ（ステップ1〜9） | GHA 側にステップ5「評価の実行」とステップ9「ディスパッチログの記録」が追加。single-agent-mode の期待差異に起因 | INFO |
| report_sections | 7セクション全て定義 | 7セクション全てカバー | なし | - |
| file_templates (`sessions/triage/_template/`) | 7箇所参照 | 2箇所参照 | Skill 側の関連ファイル一覧のメタ参照5件は実質差異なし | - |

#### l1-auto-execute-gha

**概要**: L1 自動施策化の GHA ワークフロー ↔ スキル定義

| チェックポイント | Skill側 | GHA側 | ドリフト | 重大度 |
|----------------|---------|-------|---------|--------|
| file_numbers (`\d{2}_\w+\.md`) | 00〜08 の9ファイル | 00〜08 の9ファイル | なし | - |
| workflow_steps | 6ステップ全て対応 | 6ステップ全て対応 | なし | - |
| file_templates (`sessions/initiatives/_template/`) | 2箇所参照 | 1箇所参照 | Skill 側の関連ファイル一覧のメタ参照1件は実質差異なし | - |

### inherent_differences 検証

#### triage-gha

| カテゴリ | 宣言 | 実態 | 判定 |
|---------|------|------|------|
| wall-beating-omission | GHA 版は壁打ちフェーズを省略 | GHA 側 line 10: 「壁打ちフェーズは実施しない」と明記 | 有効 |
| single-agent-mode | GHA 版はサブエージェント不使用 | GHA 側 line 11: 「サブエージェント（Task ツール）は使用できない」と明記 | 有効 |
| no-commit | GHA 版はコミット不要 | GHA 側 line 13: 「コミット・プッシュ・PR 作成は GHA ワークフローが行う」と明記 | 有効 |
| no-todo-registration | GHA 版はセッションライフサイクル todo 登録不要 | GHA 側 line 14: 「TaskCreate/TaskUpdate は使用しない」と明記 | 有効 |
| no-branch-cleanup | GHA 版はブランチ整理不要 | GHA 側 line 12: 「GHA が毎回クリーンな環境で実行するため」と明記 | 有効 |

#### l1-auto-execute-gha

| カテゴリ | 宣言 | 実態 | 判定 |
|---------|------|------|------|
| wall-beating-omission | 自動実行のため壁打ちフェーズを省略 | GHA 側 prompt: 「壁打ちフェーズは省略」と明記 | 有効 |
| single-agent-mode | 単一エージェントで全ロールを順次実行 | GHA 側 prompt: 「L2-worker として」「L2-evaluator として」と順次実行指示 | 有効 |
| scope-restriction | 対象リポジトリは dev-process-improvement のみ | GHA 側 制約セクション: 「対象リポジトリは dev-process-improvement のみ」と明記 | 有効 |

### 未マッピングワークフロー/プロンプト ギャップ報告

`.github/workflows/` には8ファイル（README.md 除く）、`.github/prompts/` には1ファイルが存在する。マッピング済みは2件のみ。

| # | ファイル | 用途 | 対応スキル定義 | マッピング追加推奨 | 理由 |
|---|---------|------|-------------|:----------------:|------|
| 1 | `daily-triage.yml` | デイリートリアージ（スケジュール/手動） | triage-manager（`.github/prompts/triage.md` 経由） | 不要 | triage.md プロンプトを呼び出すラッパー。triage-gha マッピングでプロンプト側がカバー済み |
| 2 | `initiative-wallbash.yml` | 施策の壁打ちフェーズ | l1-manager SKILL.md フェーズ0 | 推奨 | l1-manager の壁打ちフェーズに対応。GHA 版は部分的（壁打ちのみ）だが、proposal 作成まで実行 |
| 3 | `initiative-execute.yml` | 施策の実行フェーズ | l1-manager SKILL.md フェーズA〜B | 推奨 | l1-manager の計画→実行→評価→ゲート判定に対応。最も機能が豊富なワークフロー |
| 4 | `initiative-close.yml` | 施策のクローズ | l1-manager SKILL.md クローズ手順 | 推奨 | l1-manager のクローズチェックリスト・アーカイブ移動に対応 |
| 5 | `backlog-candidate-propose.yml` | バックログ候補の提案 | なし（GHA 固有） | 不要 | スキル定義との直接対応なし。backlog.csv を読んで Issue を作成するユーティリティ |
| 6 | `backlog-to-issue.yml` | バックログ→Issue 起票 | なし（GHA 固有） | 不要 | スキル定義との直接対応なし。バックログ ID を指定して Issue を作成するユーティリティ |
| 7 | `test-permissions.yml` | E2E テスト | なし（テスト用） | 不要 | 権限テスト用のユーティリティ。スキル定義との対応なし |

### ドリフト詳細（CRITICAL のみ）

CRITICAL ドリフトなし。

### INFO ドリフト詳細

| # | マッピング | チェックポイント | 内容 | 備考 |
|---|----------|----------------|------|------|
| 1 | triage-gha | workflow_steps | GHA 側にステップ5「評価の実行」とステップ9「ディスパッチログの記録」が追加。Skill 側のワーカー→評価者の2段階が GHA 側では単一エージェントで順次実行されるため、Skill 側にないステップが GHA 側に存在 | single-agent-mode の inherent_difference に起因。実質的なドリフトではない |

## 課題起票

- 起票件数: 0 件（`07_issues.md` に起票）

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | initiative ワークフロー3件（wallbash/execute/close）のマッピング追加検討 | `.github/gha-skills-mapping.yml` | l1-manager SKILL.md の異なるフェーズに対応する3つの GHA ワークフローが未マッピング。これらは backlog-auto-execute.yml（全フェーズ一括）とは異なり、フェーズ単位で分割されているため、個別のマッピングが適切。ただし、これらのワークフローは inline prompt を使用しており、チェックポイント定義の設計が必要 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | マニフェスト v1.0 のチェックポイント型は5種類（task_ids, workflow_steps, report_sections, file_templates, file_numbers）で、現在の2マッピングをカバーするには十分 | 今後 initiative ワークフローのマッピングを追加する場合、フェーズ単位の部分的対応をどう表現するかが設計課題になる（例: wallbash は l1-manager のフェーズ0 のみに対応） |
| 2 | daily-triage.yml はプロンプトファイル経由の間接参照で、ワークフロー自体にはプロンプト内容を含まない。triage-gha マッピングでプロンプト側をカバーしているため、ワークフローの重複マッピングは不要 | GHA ワークフローとプロンプトの分離パターン（daily-triage.yml → triage.md）と統合パターン（backlog-auto-execute.yml に inline prompt）の2種類が混在している |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
