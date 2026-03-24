# 作業レポート: backlog-inventory-batch — Set-1

## サマリ

バックログエントリ棚卸しを完了。完了済み41件を `git rm` で削除し、残存78件に粒度ラベル（S:33/M:32/L:13）を付与した。S分類33件を6テーマにグルーピングし、バッチ施策名候補を付与した。M/Lエントリは個別施策として残す方針を明記した。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | 完了済み41件削除 | git rm 41件 | git rm 41件完了 | 差異なし。ファイルは既にワーキングツリーから削除済みでステージングのみ |
| T-002 | 粒度分類 | 78件にS/M/L付与 | S:33, M:32, L:13 | 差異なし |
| T-003 | テーマ別グルーピング | S分類をテーマ別整理 | 6テーマにグルーピング完了 | 差異なし |
| T-004 | 知見記録 | 知見セクション記載 | 記載完了 | 差異なし |
| T-005 | 課題転記確認 | 転記確認 | 転記対象なし | 差異なし |

## 成果物一覧
- `phase-2-execution/set-1/02_worker_log.md`: T-002 粒度分類結果一覧（78件）
- `phase-2-execution/set-1/03_worker_report.md`: テーマ別グルーピング・全件分類一覧
- `backlog/entries/`: 41件削除済み（git rm）

## S分類エントリのテーマ別グルーピング

### テーマ1: GHA関連
**バッチ施策名候補**: `batch-gha-minor-fixes`

| # | ファイル名 | 内容要約 |
|---|-----------|---------|
| 1 | gha-skills-disable-model-invocation.md | GHAスキル6件に disable-model-invocation 設定追加 |
| 2 | gha-skills-mapping-initiative-registration.md | gha-skills-mapping.yml に4件マッピング追加 |
| 3 | gha-workflow-responsibility-transfer-verification.md | 評価テンプレートに責務移動検証パターン追記 |
| 4 | gha-skill-usage-class-template.md | 用途クラス別テンプレート作成 |

### テーマ2: テンプレート・ドキュメント
**バッチ施策名候補**: `batch-template-doc-fixes`

| # | ファイル名 | 内容要約 |
|---|-----------|---------|
| 1 | docs-workflow-initiative-gha-update.md | docs/workflow.md にGHA記述追加 |
| 2 | workflow-md-reference-skills-section.md | docs/workflow.md にリファレンススキル一覧追加 |
| 3 | backlog-entries-format-unification.md | 旧フォーマット13件のテーブル形式統一 |
| 4 | チェックリスト型スキルの標準テンプレート化.md | チェックリスト型スキルのテンプレート作成 |
| 5 | claude-code-action-version-tracking.md | バージョン追従手順文書作成 |
| 6 | refs-meta-info-template.md | _knowledge_template.md にメタ情報セクション追加 |

### テーマ3: ルール・ポリシー
**バッチ施策名候補**: `batch-rule-policy-minor-additions`

| # | ファイル名 | 内容要約 |
|---|-----------|---------|
| 1 | denyリスト変更提案への副作用分析必須化.md | rule-change-checklistに1項目追加 |
| 2 | ゲート判定基準での課題重大度の明文化.md | manager-common-policy §4 に判定基準追加 |
| 3 | reference-doc-granularity-rule.md | リファレンス文書粒度基準のルール文書作成 |
| 4 | user-invocable-false-description-pattern.md | description設計パターンのガイド追記 |
| 5 | 条件付き固定タスク配置ルール整備.md | SKILL.md のサブヘッダ分類 |
| 6 | rules-skills移動時の波及更新パターン.md | SKILL.md に関連ファイル一覧セクションルール |
| 7 | agentsの管理方法のガイドライン追記.md | エージェント管理ガイドライン追加 |

### テーマ4: 参照修正・リネーム追従
**バッチ施策名候補**: `batch-reference-fix-and-rename`

| # | ファイル名 | 内容要約 |
|---|-----------|---------|
| 1 | SC-008壊れた参照修正.md | l2-plan-worker/evaluator の参照3箇所を修正 |
| 2 | SCチェックQuickWins一括是正.md | SC検出Quick Wins（SC-008に集約） |
| 3 | リネーム時全文検索チェック義務化ルール追加.md | リネーム時のgrep義務化ルール新規作成 |
| 4 | sync-worker同期先コミット漏れ防止.md | sync-worker.md に同期先コミットステップ追加 |

### テーマ5: ai-driven-dev-patterns関連
**バッチ施策名候補**: `batch-aidd-minor-fixes`

| # | ファイル名 | 内容要約 |
|---|-----------|---------|
| 1 | ai-driven-dev-patterns-design-vs-operation-gap.md | dev-workflow-detail.md §8 の記述更新 |
| 2 | ai-driven-dev-patterns_source-of-truth明示.md | CLAUDE.md/rules/にSource of Truth明記 |
| 3 | aidd-documentarian-rule-reference-fix.md | documentarian参照切れ修正 |
| 4 | role-format-guideのagents対応更新.md | SKILL.md のagents対応更新 |
| 5 | sessionsテンプレート間連携ガイド.md | sessions/_template/にデータフローガイド追記 |
| 6 | ルートリポのトリアージにTG-008走査観点追加.md | triage-worker.mdに走査観点追加 |

### テーマ6: その他
**バッチ施策名候補**: `batch-skill-session-tweaks`

| # | ファイル名 | 内容要約 |
|---|-----------|---------|
| 1 | backlog-maintenance-worker走査手順改善.md | BM-workerに集計手順追加 |
| 2 | entries-pattern-inbox適用検討.md | inbox/ のentries/パターン適用検討 |
| 3 | l1-pre-applied-template-task-design.md | L1タスク設計にガイダンス追加 |
| 4 | metacognition-managerの記述構造統一.md | SKILL.md のセクション構造統一 |
| 5 | session-flow-checklist-precision.md | session-flow-policy §5.1 にチェック項目追加 |
| 6 | triage-standard-policy適用マトリクス列数リスク.md | テーブル形式の再設計 |
| 7 | スキャンレポート変更理由記載ルール.md | metacognition-worker.md に記載ルール追加 |
| 8 | 別リポジトリ成果物の記法スタイル事前確認.md | l2-worker.md にチェック項目追加 |

## M/L エントリの扱い方針

**M分類（32件）**: 個別施策として backlog に残す。3-5ファイルの変更や軽い設計判断を伴うため、バッチ化すると品質低下のリスクがある。ただし、BM-005 で検出済みの統合候補（例: BL-055+BL-057「非施策セッション GHA 自動化」、BL-054+BL-065「docs/workflow.md 網羅性改善」、BL-030+BL-082「PostToolUse hook 品質チェック統合」）は、統合施策として実施することを推奨する。

**L分類（13件）**: 個別施策として backlog に残す。アーキテクチャ設計や6+ファイルの変更を伴い、十分な計画・設計フェーズが必要。

## 全78件 粒度分類一覧表

| # | ファイル名 | 粒度 | 対象リポ | テーマ |
|---|-----------|------|---------|--------|
| 1 | Building-trust-through-layers活用検討.md | L | aidd | - |
| 2 | L1マネージャー実作業禁止の構造的強制.md | M | dpi | - |
| 3 | L2知見発見と修正適用のギャップ改善.md | M | dpi | - |
| 4 | LLMローカル開発のセキュリティ強化.md | L | 横断 | - |
| 5 | PostToolUse-hookルール変更連動チェック.md | M | dpi | - |
| 6 | PreToolUse-hookコミットメッセージバリデーション.md | M | dpi | - |
| 7 | SC-008壊れた参照修正.md | S | dpi | 参照修正・リネーム追従 |
| 8 | SCチェックQuickWins一括是正.md | S | dpi | 参照修正・リネーム追従 |
| 9 | agentsの公式ディレクトリ分け.md | M | dpi | - |
| 10 | agentsの管理方法のガイドライン追記.md | S | dpi | ルール・ポリシー |
| 11 | ai-driven-dev-patterns-builtin-skills-eval.md | M | aidd | - |
| 12 | ai-driven-dev-patterns-design-vs-operation-gap.md | S | aidd | aidd関連 |
| 13 | ai-driven-dev-patterns-triage-standard-policy作成.md | M | aidd | - |
| 14 | ai-driven-dev-patterns_source-of-truth明示.md | S | aidd | aidd関連 |
| 15 | aidd-documentarian-rule-reference-fix.md | S | aidd | aidd関連 |
| 16 | aidd-test-infrastructure.md | M | aidd | - |
| 17 | backlog-entries-format-unification.md | S | dpi | テンプレート・ドキュメント |
| 18 | backlog-maintenance-worker走査手順改善.md | S | dpi | その他 |
| 19 | claude-code-action-version-tracking.md | S | dpi | テンプレート・ドキュメント |
| 20 | claude-md-import-shrink.md | M | dpi | - |
| 21 | denyリスト変更提案への副作用分析必須化.md | S | dpi | ルール・ポリシー |
| 22 | disallowedToolsフィールド活用検討.md | M | dpi | - |
| 23 | docs-workflow-initiative-gha-update.md | S | dpi | テンプレート・ドキュメント |
| 24 | domain-agent-expansion.md | L | dpi | - |
| 25 | domain-agent-review-session.md | M | dpi | - |
| 26 | entries-pattern-inbox適用検討.md | S | dpi | その他 |
| 27 | gha-auto-execute-skills-separation.md | M | dpi | - |
| 28 | gha-backlog-maintenance-automation.md | M | dpi | - |
| 29 | gha-guideline-other-workflows.md | M | dpi | - |
| 30 | gha-metacognition-automation.md | M | dpi | - |
| 31 | gha-skill-usage-class-template.md | S | dpi | GHA関連 |
| 32 | gha-skills-disable-model-invocation.md | S | dpi | GHA関連 |
| 33 | gha-skills-mapping-initiative-registration.md | S | dpi | GHA関連 |
| 34 | gha-workflow-responsibility-transfer-verification.md | S | dpi | GHA関連 |
| 35 | harness-engineering-periodic-check-dpi.md | L | dpi | - |
| 36 | l1-pre-applied-template-task-design.md | S | dpi | その他 |
| 37 | metacognition-managerの記述構造統一.md | S | dpi | その他 |
| 38 | path-scoped-rules-introduction.md | M | dpi | - |
| 39 | per-workerファイル自動生成.md | M | dpi | - |
| 40 | permission-prompt-optimization.md | M | dpi | - |
| 41 | plugin-high-applicability-trial.md | M | dpi | - |
| 42 | posttooluse-hook-quality-check-integration.md | M | dpi | - |
| 43 | posttooluse-hook-quality-check.md | M | dpi | - |
| 44 | pretooluse-hook-security-guard.md | M | dpi | - |
| 45 | reference-doc-granularity-rule.md | S | dpi | ルール・ポリシー |
| 46 | refs-meta-info-template.md | S | dpi | テンプレート・ドキュメント |
| 47 | refs-routing-template-unification.md | M | dpi | - |
| 48 | role-format-guideのagents対応更新.md | S | aidd | aidd関連 |
| 49 | rules-skills移動時の波及更新パターン.md | S | dpi | ルール・ポリシー |
| 50 | sandbox-enable-settings-local.md | M | dpi | - |
| 51 | session-flow-checklist-precision.md | S | dpi | その他 |
| 52 | sessionsテンプレート間連携ガイド.md | S | aidd | aidd関連 |
| 53 | sync-worker同期先コミット漏れ防止.md | S | dpi | 参照修正・リネーム追従 |
| 54 | triage-action-subagent-delegation.md | M | dpi | - |
| 55 | triage-metacognitionテンプレート共通化検討.md | M | dpi | - |
| 56 | triage-standard-policy適用マトリクス列数リスク.md | S | dpi | その他 |
| 57 | user-invocable-false-description-pattern.md | S | dpi | ルール・ポリシー |
| 58 | workflow-md-reference-skills-section.md | S | dpi | テンプレート・ドキュメント |
| 59 | ゲート判定基準での課題重大度の明文化.md | S | dpi | ルール・ポリシー |
| 60 | スキャンレポート変更理由記載ルール.md | S | dpi | その他 |
| 61 | チェックリスト型スキルの標準テンプレート化.md | S | dpi | テンプレート・ドキュメント |
| 62 | ディレクトリ構成最適化検討.md | L | aidd | - |
| 63 | マルチAIエージェント共通ルール適用.md | L | aidd | - |
| 64 | メタ認知セッションのai-driven-dev-patterns展開.md | M | aidd | - |
| 65 | メタ認知セット分割粒度・スキャンモード.md | M | dpi | - |
| 66 | リネーム時全文検索チェック義務化ルール追加.md | S | dpi | 参照修正・リネーム追従 |
| 67 | リンク整合性チェック標準化.md | M | dpi | - |
| 68 | ルートリポのトリアージにTG-008走査観点追加.md | S | aidd | aidd関連 |
| 69 | 全ロールファイルrole-format-guide準拠確認修正.md | M | aidd | - |
| 70 | 別リポジトリ成果物の記法スタイル事前確認.md | S | dpi | その他 |
| 71 | 北村さんの取り組みを取り込む.md | L | aidd | - |
| 72 | 同期対象リスト管理と差分ベース反映計画.md | M | dpi | - |
| 73 | 外部リポジトリアーキテクチャオーバービュー管理.md | M | dpi | - |
| 74 | 施策間の競合防止方針策定.md | L | 横断 | - |
| 75 | 条件付き固定タスク配置ルール整備.md | S | dpi | ルール・ポリシー |
| 76 | 社内施策_devkitのコマンドやガイドの使用クロードのskillやRuleとして用意しておく.md | M | 横断 | - |
| 77 | 長文rulesのコンテキストコスト最適化.md | M | 横断 | - |
| 78 | 高度な並列化と協調プロトコル統合.md | L | aidd | - |

## 発生した課題
- 転記対象の課題なし（07_issues.md 参照）

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | バックログエントリの粒度分類基準（S/M/L）は backlog テンプレートのメタ情報フィールドとして標準化すると、今後の棚卸し作業が効率化される | T-002 粒度分類作業 | backlog/_template.md | 現在のテンプレートには粒度フィールドがない。起票時に粒度見積もりを記載するフィールドを追加すれば、BM走査やトリアージでの判断が迅速になる |
| 2 | aidd 関連のS分類エントリ6件は CLI --add-dir 環境でのバッチ実行が必要だが、SDK環境からは実行不可（ISS-027制約）。バッチ施策の実行環境制約を計画段階で明記すべき | T-003 テーマ別グルーピング | l1-manager SKILL.md のバッチ施策ガイド | バッチ施策名候補に「実行環境: CLI推奨」の注記を付けるルールがあると、着手時の混乱を防げる |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | BM-005 で検出済みの統合候補（BL-055+BL-057, BL-054+BL-065, BL-030+BL-082）はS分類ではなくM分類だが、統合施策として実施すれば効率的。次回トリアージでの統合判断材料になる | T-003 テーマ別グルーピング | 統合候補エントリには「関連エントリ」セクションに統合推奨が既に記載されている |
| 2 | sync-worker同期先コミット漏れ防止.md のステータスが「initiative 開始済」だが backlog/entries/ に残存。施策化済みエントリの backlog からの除去タイミングが不明確 | T-002 全件読み取り | BM走査で検出されるべき不整合だが、本施策のスコープ外 |

## 所感・次フェーズへの申し送り
- S分類33件のうち、テーマ1（GHA関連）とテーマ4（参照修正・リネーム追従）は相互依存が少なく、バッチ施策として実行しやすい
- テーマ5（aidd関連）は CLI --add-dir 環境が必要なため、SDK 環境では実行不可。実行環境の制約を考慮して施策化する必要がある
- テーマ2（テンプレート・ドキュメント）の docs-workflow-initiative-gha-update.md と workflow-md-reference-skills-section.md は BM-005 統合候補（BL-054+BL-065）と重複するため、統合施策としてまとめるのが効率的

---
**作成者**: L2（実施）
**作成日**: 2026-03-24
