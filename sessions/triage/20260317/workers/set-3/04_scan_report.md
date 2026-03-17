# スキャンレポート: Set-3

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-002 | backlog | 完了 |
| TG-005 | backlog | 完了 |
| TG-006 | rules/workflow | 完了 |
| TG-008 | skills/agents | 完了 |

---

## TG-002: backlog 施策化済みチェック・完了/進行中エントリの突合・対象リポジトリ未記入チェック

### 施策化済みチェック結果

CSV の「施策ディレクトリ名」列に記入があるエントリ: 4件（BL-002, BL-020, BL-031, BL-064）

CSV に施策ディレクトリ名が記入されていないが、initiatives/ または _archive/ に対応する施策が存在するエントリ: 4件

| BL-ID | 施策名 | 対応 initiative | 場所 | 推奨アクション |
|-------|--------|----------------|------|--------------|
| BL-004 | ハーネスエンジニアリング観点でのブラッシュアップ | harness-engineering-brushup | _archive/ | CSV の施策ディレクトリ名列を更新、ステータスを「完了」に変更 |
| BL-010 | backlogテンプレート凡例強化 | backlog-template-legend-enhancement | _archive/ | CSV の施策ディレクトリ名列を更新、ステータスを「完了」に変更 |
| BL-012 | 知見集約テーブル発見元列のinitiatives逆移植 | knowledge-table-origin-column-backport | _archive/ | CSV の施策ディレクトリ名列を更新、ステータスを「完了」に変更 |
| BL-072 | 非施策セッション成果物の構造・プレフィックス見直し | session-artifacts-structure-refactor | initiatives/（活動中） | CSV の施策ディレクトリ名列を更新、ステータスを「進行中」に変更 |

### 完了/進行中エントリの突合

| BL-ID | CSV ステータス | initiative 場所 | 整合性 | 推奨アクション |
|-------|--------------|----------------|--------|--------------|
| BL-002 | 完了 | _archive/dev-workflow-detail-l1-ref-review | OK | なし |
| BL-020 | 進行中 | initiatives/sync-worker-target-commit | OK | なし |
| BL-031 | 完了 | _archive/automation-manager-session | OK | なし |
| BL-064 | 完了 | initiatives/skill-plugin-overlap-check-rule（未アーカイブ） | 不整合 | 施策はゲート判定通過済み（08_gate_review.md あり）だが _archive/ に移動されていない。アーカイブ処理を実施すべき |

### 削除・クローズ候補リスト

| BL-ID | 施策名 | 理由 | 推奨アクション |
|-------|--------|------|--------------|
| BL-004 | ハーネスエンジニアリング観点でのブラッシュアップ | 施策化済み・完了（_archive/harness-engineering-brushup） | ステータスを「完了」に更新 |
| BL-010 | backlogテンプレート凡例強化 | 施策化済み・完了（_archive/backlog-template-legend-enhancement） | ステータスを「完了」に更新 |
| BL-012 | 知見集約テーブル発見元列のinitiatives逆移植 | 施策化済み・完了（_archive/knowledge-table-origin-column-backport） | ステータスを「完了」に更新 |
| BL-072 | 非施策セッション成果物の構造・プレフィックス見直し | 施策化済み・進行中（initiatives/session-artifacts-structure-refactor） | ステータスを「進行中」に更新 |

### 重複採番の検出

| BL-ID | エントリ1 | エントリ2 | 推奨アクション |
|-------|----------|----------|--------------|
| BL-076 | ai-driven-dev-patterns の設計構想と実運用の乖離調査 | ai-driven-dev-patterns テストインフラ整備 | 後者に新ID（BL-084）を採番し直す |
| BL-077 | ai-driven-dev-patterns documentarian 参照切れルール修正 | backlog エントリ旧フォーマット統一 | 後者に新ID（BL-085）を採番し直す |

### 対象リポジトリ未記入チェック

未記入エントリ: **0件**（全エントリに対象リポジトリが記入済み）

前回トリアージ（20260315-2）時点で約31件の未記入が報告されていたが、その後のメンテナンスで全件対応済みと判断される。

---

## TG-005: backlog アイテム間の関係性横断分析

### 関係性分析テーブル

#### クラスター1: Hook 系自動化（4件）

| BL-ID | 施策名 | 関係性 | 推奨 |
|-------|--------|--------|------|
| BL-029 | PreToolUse hook コミットメッセージバリデーション | 依存なし（独立実装可） | 独立実施 |
| BL-030 | PostToolUse hook ルール変更連動チェック | BL-082 と類似（PostToolUse hook） | BL-082 と統合検討 |
| BL-067 | PreToolUse hook センシティブファイルアクセスガード | BL-071（sandbox）と二重防御の関係 | BL-071 と連携実施 |
| BL-082 | PostToolUse hook CLAUDE.md 行数・rules/ フロントマター自動検証 | BL-030 と類似（PostToolUse hook） | BL-030 と統合検討 |

**統合候補**: BL-030 + BL-082 → PostToolUse hook の統合施策として一本化（スコープが重なる）

#### クラスター2: GHA 自動化拡張（8件）

| BL-ID | 施策名 | 関係性 | 推奨 |
|-------|--------|--------|------|
| BL-055 | GHA バックログメンテナンスセッション自動化 | BL-057 と同パターン（セッション GHA 化） | 独立実施（参考パターン共有） |
| BL-057 | GHA メタ認知セッション自動化 | BL-055 と同パターン | 独立実施 |
| BL-056 | 他ワークフローへの権限3層モデル適用 | GHA 全体に横断的 | GHA 系施策の前提として先行実施推奨 |
| BL-069 | GHA スキル6件に disable-model-invocation 設定 | 独立（設定変更のみ） | 独立実施（小規模） |
| BL-078 | backlog-auto-execute.yml への GHA スキル分離パターン適用 | BL-079 と関連 | 独立実施 |
| BL-079 | GHA スキル「やらないこと」の用途クラス別テンプレート化 | BL-078 と関連 | 独立実施 |
| BL-080 | gha-skills-mapping.yml に initiative ワークフロー4件のマッピング追加 | TG-010 の前提 | 優先実施推奨 |
| BL-081 | GHA ワークフロー間の責務移動時の対検証パターン | 独立 | 独立実施 |

#### クラスター3: コンテキスト最適化（3件）

| BL-ID | 施策名 | 関係性 | 推奨 |
|-------|--------|--------|------|
| BL-008 | 長文 rules のコンテキストコスト最適化 | BL-068, BL-070 と同テーマ | BL-070 が技術基盤、BL-068 が適用 |
| BL-068 | CLAUDE.md の import(@) + rules/ 委譲 | BL-070 に依存（path-scoped rules が前提） | BL-070 完了後に実施 |
| BL-070 | path-scoped rules 導入と commit-message.md 分離 | BL-068 の前提条件 | 先行実施推奨 |

**依存関係**: BL-070 → BL-068 → BL-008（段階的に実施）

#### クラスター4: docs/workflow.md 更新（2件）

| BL-ID | 施策名 | 関係性 | 推奨 |
|-------|--------|--------|------|
| BL-054 | docs/workflow.md への initiative GHA 記述追加 | BL-065 と同一ファイル対象 | 統合実施（同一ファイルの更新を一度に） |
| BL-065 | docs/workflow.md にリファレンススキル一覧セクション追加 | BL-054 と同一ファイル対象 | 統合実施 |

**統合候補**: BL-054 + BL-065 → docs/workflow.md 更新の統合施策

#### クラスター5: ai-driven-dev-patterns 品質改善（3件、重複ID含む）

| BL-ID | 施策名 | 関係性 | 推奨 |
|-------|--------|--------|------|
| BL-076(1) | ai-driven-dev-patterns の設計構想と実運用の乖離調査 | 独立 | 独立実施 |
| BL-076(2) | ai-driven-dev-patterns テストインフラ整備 | BL-077(1)と関連（品質基盤） | 独立実施 |
| BL-077(1) | ai-driven-dev-patterns documentarian 参照切れルール修正 | 小規模・独立 | 独立実施 |

#### クラスター6: セッション構造統一（3件）

| BL-ID | 施策名 | 関係性 | 推奨 |
|-------|--------|--------|------|
| BL-027 | metacognition-manager の記述構造統一 | BL-048 と関連 | 独立実施 |
| BL-048 | triage/metacognition テンプレート共通化検討 | BL-027 完了後が効率的 | BL-027 後に実施 |
| BL-072 | 非施策セッション成果物の構造・プレフィックス見直し | 施策化済み（進行中） | 進行中施策として継続 |

#### クラスター7: セキュリティ二重防御（2件）

| BL-ID | 施策名 | 関係性 | 推奨 |
|-------|--------|--------|------|
| BL-067 | PreToolUse hook センシティブファイルアクセスガード | BL-071 と二重防御を構成 | 同時または連続実施 |
| BL-071 | sandbox 有効化 + settings.local.json 導入 | BL-067 と二重防御を構成 | 同時または連続実施 |

### 関係性サマリ

| 関係タイプ | 組み合わせ | 推奨 |
|-----------|-----------|------|
| **統合候補** | BL-030 + BL-082 | PostToolUse hook 統合施策 |
| **統合候補** | BL-054 + BL-065 | docs/workflow.md 更新統合 |
| **依存関係** | BL-070 → BL-068 → BL-008 | path-scoped rules → import → コンテキスト最適化 |
| **依存関係** | BL-027 → BL-048 | 記述構造統一 → テンプレート共通化 |
| **連携推奨** | BL-067 + BL-071 | セキュリティ二重防御 |

---

## TG-006: ルール・workflow 整合性チェック

### .claude/skills/ と docs/workflow.md の整合性

| チェック項目 | 結果 | 詳細 |
|------------|------|------|
| l1-manager フロー（Phase 1-6） | OK | workflow.md に plan-worker/plan-evaluator の新フェーズが反映済み |
| triage-manager フロー | OK | 整合 |
| session-consistency-manager フロー | OK | workflow.md に新規セクション追加済み |
| metacognition-manager フロー | OK | 整合 |
| sync-manager フロー | OK | 整合 |
| backlog-maintenance-manager フロー | OK | 整合 |
| automation-manager フロー | OK | 整合 |
| config-optimizer-manager フロー | OK | 整合 |
| l1-impl-manager フロー | OK | 整合 |

### .claude/rules/ と README.md の整合性

| チェック項目 | 結果 | 詳細 |
|------------|------|------|
| rules/ ファイル一覧 | **NG** | `parallel-dev.md` が README のディレクトリ構成から欠落 |

**不整合の詳細**: README.md の `.claude/rules/` セクション（13-18行目）には5ファイルが列挙されているが、実際には6ファイルが存在する。`parallel-dev.md`（並列ディスパッチルール）が記載されていない。

### .claude/skills/ と README.md の整合性

| チェック項目 | 結果 | 詳細 |
|------------|------|------|
| 起動型スキル一覧 | **NG** | `session-consistency-manager` が README のディレクトリ構成・セッション種別テーブル・AI向けスキルテーブルから欠落 |

**不整合の詳細**: `session-consistency-manager` は `user-invocable: true` の起動型スキルだが、README.md の以下3箇所に記載がない:
1. ディレクトリ構成ツリー（8-48行目）
2. セッション種別と起動方法テーブル（95-106行目）
3. AI向けスキル・エージェント定義テーブル（178-189行目）

### 参考資料（ドラフト）ステータスチェック

| ファイル | バナー有無 | 統合状況 | 実態との矛盾 | 備考 |
|---------|:---------:|---------|:----------:|------|
| docs/coordination-protocol-guideline.md | OK | 一部統合済み（セクション2.2 → `.claude/rules/commit-message.md`） | なし | commit-message.md に統合済みの記載と実態が一致 |
| docs/git-worktree-guideline.md | OK | 一部統合済み | なし | バナーの記載と実態が一致 |

### docs/ 分類テーブル網羅性

| ファイル | CLAUDE.md テーブル記載 | 備考 |
|---------|:-------------------:|------|
| docs/workflow.md | あり | 可視化文書 |
| docs/management-system-guide.md | あり | 運用ガイド |
| docs/subagent-permission-guide.md | あり | 運用ガイド |
| docs/implementation.md | あり | 運用ガイド |
| docs/coordination-protocol-guideline.md | あり | 参考資料（ドラフト） |
| docs/git-worktree-guideline.md | あり | 参考資料（ドラフト） |

全6ファイルが CLAUDE.md の分類テーブルに記載済み。未記載ファイルなし。

---

## TG-008: セッション構造標準ポリシーチェック

### 走査結果サマリ
- 走査対象ファイル数: 11件（前回 20260315-2 以降に変更されたスキル/エージェント定義）
- 不適合件数: 0件（必須: 0件 / 推奨: 0件 / 軽微: 0件）

### 走査対象（差分）

前回トリアージ（20260315-2、コミット 7f211ee）以降にマージされた施策で変更されたファイル:

| 施策 | 変更ファイル |
|------|-----------|
| l1-manager-enhanced-planning | l1-manager/SKILL.md, agents/l2-plan-worker.md(新規), agents/l2-plan-evaluator.md(新規), agents/l2-worker.md, agents/l2-evaluator.md |
| session-lifecycle-policy-rename | session-lifecycle-policy/SKILL.md(リネーム), triage-manager/SKILL.md, triage-manager/agents/triage-worker.md, triage-manager/agents/triage-evaluator.md |
| session-consistency-manager | session-consistency-manager/SKILL.md(新規), agents/sc-collection-worker.md(新規), agents/sc-analysis-worker.md(新規), agents/sc-proposal-worker.md(新規), agents/sc-evaluator.md(新規) |
| impl-manager-refs-knowledge-read | l1-impl-manager/SKILL.md |

### ファイル別チェック結果

| ファイル | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール | 総合判定 |
|---------|:-------------:|:----------:|:--------:|:----------:|:-------:|
| l1-manager/SKILL.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-plan-worker.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-plan-evaluator.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-worker.md | OK | N/A | OK | OK | OK |
| l1-manager/agents/l2-evaluator.md | OK | N/A | OK | OK | OK |
| session-lifecycle-policy/SKILL.md | OK | OK | N/A | N/A | OK |
| triage-manager/SKILL.md | OK | OK | OK | OK | OK |
| triage-manager/agents/triage-worker.md | OK | N/A | OK | OK | OK |
| triage-manager/agents/triage-evaluator.md | OK | N/A | OK | OK | OK |
| session-consistency-manager/SKILL.md | OK | OK | OK | OK | OK |
| session-consistency-manager/agents/sc-collection-worker.md | OK | OK | OK | OK | OK |
| session-consistency-manager/agents/sc-analysis-worker.md | OK | OK | OK | OK | OK |
| session-consistency-manager/agents/sc-proposal-worker.md | OK | OK | OK | OK | OK |
| session-consistency-manager/agents/sc-evaluator.md | OK | OK | OK | OK | OK |
| l1-impl-manager/SKILL.md | OK | OK | OK | OK | OK |

### チェック詳細

**A. ライフサイクル完備チェック**:
- l2-plan-worker: 壁打ちフェーズ（03_work_log.md に記録）、実施計画、レポート（04_work_report.md）、知見記録 → 全て完備
- l2-plan-evaluator: 壁打ちフェーズ（05_eval_plan.md に記録）、評価計画、レポート（06_eval_report.md）、知見記録 → 全て完備
- session-consistency-manager 全エージェント: 壁打ち、計画、レポート、知見記録、課題起票 → 全て完備
- session-lifecycle-policy: 適用マトリクスに sc-manager/sc-worker/sc-evaluator が追加済み

**B. ペアリング整合性チェック**:
- l2-plan-worker ↔ l2-plan-evaluator: ペア定義あり、成果物チェーン確認（02a_task_division.md → 評価者が読み取り）、起動順序明記あり
- sc-collection-worker/sc-analysis-worker/sc-proposal-worker ↔ sc-evaluator: ペア定義あり、成果物チェーン確認、起動順序明記あり（「ワーカー完了後、sc-evaluator をサブエージェントとして起動する」）
- session-lifecycle-policy §2.1 ペアリング構造テーブルに新ペアが反映済み

**C. 課題起票・ルーティングチェック**:
- 全新規エージェント: 07_issues.md 経由の課題起票方法が明記
- 知見記録: 「ルール化候補」「参考情報」の分類テーブルが定義済み

**D. 停止ルール・スコープチェック**:
- 全新規エージェント: 「やること」「やらないこと」「停止ルール」「担当ファイルテーブル」が完備

### 不適合の詳細

不適合なし。

---

## 課題起票

- 起票件数: 0 件（`07_issues.md` に起票）

検出された不整合はいずれも TG-002/TG-006 のスコープ内でアクション推奨として記録済み。課題として独立起票が必要な重大度の不適合はなし。

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | なし — 理由: 今回の走査範囲では新規ルール化が必要なパターンは検出されなかった | - | - |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | BL-076/077 の重複採番は backlog-id-and-issue-template 施策で導入された採番規則が適用されていない可能性を示唆 | CSV への手動追記時に ID 重複チェックが行われていない |
| 2 | BL-064（skill-plugin-overlap-check-rule）が完了済みだが _archive/ に未移動。initiative-close-procedure の実行漏れの可能性 | ゲート判定通過済み施策のアーカイブ処理がフローとして確実に実行されていない |
| 3 | README.md に session-consistency-manager が反映されていない。施策作成時の README 更新がフローに組み込まれていない可能性 | 新規起動型スキル追加時に README 更新が漏れるパターン |
| 4 | 対象リポジトリ未記入が0件に改善。前回（約31件未記入）からの大幅改善 | バックログメンテナンスの効果が確認された |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-17
