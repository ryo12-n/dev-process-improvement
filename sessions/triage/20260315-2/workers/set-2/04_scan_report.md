# スキャンレポート: Set-2

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-002 | backlog | 完了 |
| TG-005 | backlog | 完了 |
| TG-006 | rules/workflow | 完了 |
| TG-010 | GHA/Skills | 完了 |
| TG-009 | backlog | スキップ（削除・統合候補なし） |

---

## TG-002: backlog 棚卸し

### 全体サマリ

| 項目 | 値 |
|------|-----|
| CSV 総件数 | 72行（BL-001〜BL-074、BL-032/BL-061 欠番） |
| entries/ ファイル数 | 72件（CSV と一致） |
| 完了済みエントリ | 2件（BL-002, BL-031） |
| 進行中エントリ | 1件（BL-020） |
| 候補エントリ | 69件 |
| 対象リポジトリ未記入 | 0件 |
| 施策ディレクトリ名記入済み | 3件（BL-002, BL-020, BL-031） |

### 完了済みエントリの処理状況

| BL-ID | ステータス | 施策ディレクトリ名 | initiatives/ 存在 | _archive/ 存在 | 判定 |
|-------|----------|------------------|:-:|:-:|------|
| BL-002 | 完了 | dev-workflow-detail-l1-ref-review | - | OK | 正常 |
| BL-031 | 完了 | automation-manager-session | - | OK | 正常 |

### 進行中エントリの処理状況

| BL-ID | ステータス | 施策ディレクトリ名 | initiatives/ 存在 | 判定 |
|-------|----------|------------------|:-:|------|
| BL-020 | 進行中 | sync-worker-target-commit | OK | 正常 |

### 新規 BL-066〜BL-074 品質チェック

| BL-ID | 優先度 | 対象リポ | BL-ID記載 | 課題・背景 | 期待効果 | 依存環境前提 | 関連エントリ | チェックリスト | 総合判定 |
|-------|:------:|:------:|:---------:|:---------:|:--------:|:----------:|:----------:|:----------:|:--------:|
| BL-066 | 中 | OK | OK | OK | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-067 | 高 | OK | OK | NG（「概要」で代替） | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-068 | 高 | OK | OK | NG（「概要」で代替） | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-069 | 中 | OK | OK | NG（「概要」で代替） | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-070 | 中 | OK | OK | NG（「概要」で代替） | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-071 | 高 | OK | OK | NG（「概要」で代替） | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-072 | 中 | OK | OK | NG（「概要」で代替） | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-073 | 低 | OK | OK | OK | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |
| BL-074 | 低 | OK | OK | OK | OK | NG（欠落） | NG（欠落） | NG（欠落） | 要修正 |

**品質所見**:
- BL-067〜BL-072（config-optimization 起票元）は「課題・背景」セクションの代わりに「概要」セクションを使用しており、テンプレートと乖離
- 全9件で「依存する環境前提」「関連エントリ」「起票時チェックリスト」セクションが欠落
- ただし内容面（BL-ID、対象リポジトリ、優先度、期待効果）は適切に記載されている

### 施策化済みチェック（CSV外の進行中 initiative）

以下の4件は `sessions/initiatives/` に進行中ディレクトリが存在するが、`backlog.csv` に対応するエントリがない。

| initiative ディレクトリ名 | backlog.csv | 状態 |
|------------------------|:-----------:|------|
| backlog-id-and-issue-template | 未登録 | 進行中 |
| external-repo-cleanup-on-demand | 未登録 | 進行中 |
| impl-worker-worklog-reliability | 未登録 | 進行中 |
| triage-phase-gate-and-gha-sync | 未登録 | 進行中 |

**備考**: これらは backlog を経由せずに直接施策化された可能性がある。CSV の追跡漏れとして記録する。

### 削除・クローズ候補

- なし（BL-002, BL-031 は完了ステータスで CSV 残存は正常運用）

---

## TG-005: backlog 関係性分析

### 走査結果サマリ

- 分析対象: 全72件（BL-001〜BL-074、BL-032/BL-061 欠番）
- 新規21件（BL-054〜BL-074）の関係性に注目
- 重複候補: 2組
- 依存関係: 6組
- 統合候補: 5グループ

### 重複候補

| # | エントリ A | エントリ B | 重複の根拠 | 推奨アクション |
|---|----------|----------|-----------|-------------|
| 1 | BL-008: 長文rulesのコンテキストコスト最適化 | BL-068: claude-md-import-shrink | BL-068 は BL-008 の部分的な実装手段。CLAUDE.md の行数削減はコンテキストコスト最適化の一部 | BL-068 を BL-008 の下位施策として統合検討 |
| 2 | BL-008: 長文rulesのコンテキストコスト最適化 | BL-070: path-scoped-rules-introduction | BL-070 は BL-008 の主要な実装手段。rules/ の path-scoped 化はコンテキストコスト最適化の核心 | BL-070 を BL-008 の下位施策として統合検討 |

### 依存関係

| # | 依存元 | 依存先 | 依存の内容 |
|---|--------|--------|-----------|
| 1 | BL-067: pretooluse-hook-security-guard | BL-071: sandbox-enable-settings-local | BL-067 は BL-071 との二重防御を前提として設計されている |
| 2 | BL-068: claude-md-import-shrink | BL-070: path-scoped-rules-introduction | BL-068 の rules/ 委譲は BL-070 の path-scoped rules 導入が前提 |
| 3 | BL-073: domain-agent-review-session | agency-agents-integration（施策） | BL-073 は agency-agents-integration 施策の完了が前提 |
| 4 | BL-074: domain-agent-expansion | agency-agents-integration（施策） | BL-074 も agency-agents-integration 施策の完了が前提 |
| 5 | BL-074: domain-agent-expansion | BL-073: domain-agent-review-session | BL-074 は BL-073 での活用実績レビュー後が望ましい |
| 6 | BL-069: gha-skills-disable-model-invocation | gha-initiative-skills-separation（施策） | GHA 専用スキルの分離が完了していることが前提 |

### 統合候補

| # | グループ名 | 含まれるエントリ | 統合の根拠 | 推奨 |
|---|----------|---------------|-----------|------|
| 1 | コンテキスト最適化統合 | BL-008 + BL-068 + BL-070 | CLAUDE.md 縮小・path-scoped rules・長文 rules 最適化は一つの施策として実施可能。BL-068 は BL-070 に依存しており、BL-070 は BL-008 の主要実装手段 | 統合推奨（BL-008 を親施策として BL-068/BL-070 を吸収） |
| 2 | セキュリティ二重防御 | BL-067 + BL-071 | PreToolUse hook と sandbox 有効化は「二重防御」として同時実施が効果的。両者とも deny ルール非機能の代替手段 | 統合推奨 |
| 3 | PreToolUse hook 基盤 | BL-029 + BL-067 | コミットメッセージバリデーションとセキュリティガードは共に PreToolUse hook をベースとし、hook 基盤の設計を共有できる | 統合検討（基盤部分のみ） |
| 4 | GHA 自動化拡張 | BL-055 + BL-057 | backlog-maintenance と metacognition の GHA 自動化は、既存の triage GHA 自動化と同様のパターンで実装可能 | 統合推奨 |
| 5 | ドメインエージェント展開 | BL-073 + BL-074 | レビューセッションと他マネージャー展開は、活用実績の蓄積とフィードバックのサイクルとして連続的に実施すべき | 統合推奨 |

---

## TG-006: ルール・workflow 整合性チェック

### 前回修正の反映確認

| チェック項目 | 結果 | 詳細 |
|------------|:----:|------|
| manager-common-policy §1 に automation-manager 記載 | OK | 7マネージャーとして記載済み |
| manager-common-policy §9 に config-optimizer-manager 記載 | OK | 関連ファイル一覧に記載済み |
| README セッション種別テーブルに automation-manager 記載 | OK | 記載済み |
| README セッション種別テーブルに config-optimizer-manager 記載 | OK | 記載済み |
| README AI向けスキル定義テーブルに automation-manager 記載 | OK | 記載済み |
| README AI向けスキル定義テーブルに config-optimizer-manager 記載 | OK | 記載済み |
| docs/workflow.md に GHA Initiative スキル4件のセクション | OK | 444行目以降に専用セクション記載済み |

### 参考資料（ドラフト）ステータスチェック

| ファイル | バナー有無 | 統合状況 | 実態との矛盾 | 備考 |
|---------|:---------:|---------|:----------:|------|
| docs/coordination-protocol-guideline.md | OK | 一部統合済み（セクション2.2 → commit-message.md） | なし | 統合先 `.claude/rules/commit-message.md` が存在確認済み |
| docs/git-worktree-guideline.md | OK | 一部統合済み | なし | l1-impl-manager 等に worktree 関連の記述あり |

### docs/ 分類テーブル網羅性

| ファイル | CLAUDE.md テーブル記載 | 備考 |
|---------|:-------------------:|------|
| docs/workflow.md | あり | 可視化文書 |
| docs/management-system-guide.md | あり | 運用ガイド |
| docs/subagent-permission-guide.md | あり | 運用ガイド |
| docs/implementation.md | あり | 運用ガイド |
| docs/coordination-protocol-guideline.md | あり | 参考資料（ドラフト） |
| docs/git-worktree-guideline.md | あり | 参考資料（ドラフト） |

全6ファイルが CLAUDE.md テーブルに記載済み。未記載ファイルなし。

### README と文書バナーの乖離

| 箇所 | README 記載 | 実際のバナー | 乖離 |
|------|-----------|-----------|:----:|
| docs/coordination-protocol-guideline.md | 「一部統合済み」 | 「一部統合済み」 | なし |
| docs/git-worktree-guideline.md | 「未着手」 | 「一部統合済み」 | **あり** |

**乖離詳細**: README 164行目では `git-worktree-guideline.md` を「参考資料（ドラフト）、未着手」と記載しているが、実際のドキュメントバナーでは「一部統合済み」と記載されている。`l1-impl-manager` 等のスキルに worktree 関連の記述が統合されており、バナー側が正しい。README の記載を「一部統合済み」に修正が必要。

---

## TG-010: GHA ↔ Skills 整合性チェック

### 走査結果サマリ

- マッピング数: 2件（triage-gha, l1-auto-execute-gha）
- ドリフト検出: CRITICAL 1件 / WARNING 1件 / INFO 0件

### マッピング別結果

#### triage-gha

| チェックポイント | Skill側 | GHA側 | ドリフト | 重大度 |
|----------------|---------|-------|---------|--------|
| task_ids | TG-001〜TG-010 | TG-001〜TG-010 | なし | - |
| workflow_steps | 8ステップ定義 | 8ステップ定義 | 表現差異あり（Skill は日本語セクション見出し、GHA は「ステップ N:」形式）だが内容一致 | - |
| report_sections | 知見集約・課題集約等 | 同構成 | なし | - |
| file_templates | 7参照 | 2参照 | GHA は最小限のテンプレート参照（inherent_differences の範囲） | - |

#### inherent_differences 検証（triage-gha）

| カテゴリ | 宣言 | 実態 | 判定 |
|---------|------|------|------|
| wall-beating-omission | 省略 | GHA に「壁打ちフェーズは実施しない」と明記 | 有効 |
| single-agent-mode | 単一エージェント | GHA に「サブエージェント（Task ツール）は使用できない」と明記 | 有効 |
| no-commit | コミット不要 | GHA に「コミット・プッシュ・PR 作成は GHA ワークフローが行う」と明記 | 有効 |
| no-todo-registration | todo 登録不要 | GHA に「TaskCreate/TaskUpdate は使用しない」と明記 | 有効 |
| no-branch-cleanup | ブランチ整理不要 | GHA に「ブランチ整理は不要」と明記 | 有効 |

**triage-gha 判定**: 整合（ドリフトなし）

#### l1-auto-execute-gha

| チェックポイント | Skill側 | GHA側 | ドリフト | 重大度 |
|----------------|---------|-------|---------|--------|
| gha_source.path | - | `.github/workflows/backlog-auto-execute.yml`（**ファイル不存在**） | ファイル参照が stale。実際は `initiative-execute.yml` | **CRITICAL** |
| file_numbers | 検証不可 | 検証不可 | gha_source が読めないため検証不可 | - |
| workflow_steps | 検証不可 | 検証不可 | 同上 | - |
| file_templates | 検証不可 | 検証不可 | 同上 | - |

**l1-auto-execute-gha 判定**: CRITICAL ドリフト（ソースファイル参照が陳腐化）

### initiative 系マッピング追加状況

前回トリアージで推奨された initiative ワークフロー3件（wallbash, execute, close）のマッピング追加は**未対応**。さらに gha-question も含めると計4件のマッピングが未定義。

| スキル | SKILL.md 存在 | ワークフロー存在 | マッピング定義 |
|--------|:----------:|:----------:|:----------:|
| gha-wallbash | OK | initiative-wallbash.yml: OK | **未定義** |
| gha-execute | OK | initiative-execute.yml: OK | **未定義** |
| gha-close | OK | initiative-close.yml: OK | **未定義** |
| gha-question | OK | initiative-question.yml: OK | **未定義** |

### ドリフト詳細（CRITICAL）

**l1-auto-execute-gha のファイル参照 stale**:
- gha-skills-mapping.yml 66行目: `path: .github/workflows/backlog-auto-execute.yml`
- 実際のファイル: `.github/workflows/initiative-execute.yml`
- 原因: gha-initiative-skills-separation 施策でワークフローが改名されたが、マッピングマニフェストが更新されなかった
- 推奨アクション: `gha-skills-mapping.yml` の `l1-auto-execute-gha` エントリのパスを `initiative-execute.yml` に更新。加えて、マッピング ID 自体も `initiative-execute-gha` 等に改名を検討

---

## TG-009: 情報欠損リスク評価

削除・統合候補なし：スキップ

---

## 課題起票

- 起票件数: 3件（`07_issues.md` に起票済み）
  1. BL-066〜BL-074 テンプレート準拠不足
  2. README と git-worktree-guideline.md バナーの統合状況乖離
  3. gha-skills-mapping.yml の l1-auto-execute-gha ファイル参照 stale + initiative 系4件マッピング未定義

## 走査中の知見

### ルール化候補（.claude/rules/ や skills/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | config-optimization 起票元のエントリがテンプレート非準拠の傾向 | backlog/_template.md, config-optimizer-manager | config-optimizer-manager の提案出力がテンプレートの「課題・背景」ではなく「概要」セクションを使用。起票時にテンプレート準拠を強制する仕組みが必要 |
| 2 | GHA スキル改名時のマッピングマニフェスト更新漏れパターン | .github/gha-skills-mapping.yml | ワークフローファイル改名時に gha-skills-mapping.yml の更新が漏れるパターンが検出された。関連ファイル一覧への gha-skills-mapping.yml の追加、またはルール変更チェックリストへの項目追加を検討 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | 4件の進行中 initiative が CSV 未登録 | backlog を経由せずに直接施策化された initiative が存在する。施策管理の網羅性の観点から、事後的にでも CSV 登録するか、または「CSV 登録不要な施策」の基準を明確にする必要がある |
| 2 | コンテキスト最適化系施策（BL-008/068/070）は親子関係での統合が効果的 | BL-008 が上位目標、BL-068/BL-070 が具体的な実装手段という階層関係にある。施策間の親子関係を backlog で表現する仕組みがあると管理しやすい |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
