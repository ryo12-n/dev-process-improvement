# 作業履歴: backlog-inventory-batch — Set-1

## 作業ログ

### [2026-03-24] タスクID: T-001
**状態**: 完了
**作業内容**:
- `backlog/entries/` 配下の完了済み41件を `git rm` で削除
- 41件すべてが `git status` で staged deletion 確認済み
- 残存ファイル数: 78件（`ls backlog/entries/*.md | wc -l` = 78）
**成果物**: 41件の git rm 実行済み
**課題・気づき**: ファイルは既にワーキングツリーから削除されており、`git rm` でステージングのみ必要だった

### [2026-03-24] タスクID: T-002
**状態**: 完了
**作業内容**:
- 残存78件の全エントリを読み取り、粒度ラベル（S/M/L）を付与
- 分類基準: S=1-2ファイル変更・設計判断不要、M=3-5ファイル変更・軽い設計判断、L=6+ファイル変更・アーキテクチャ設計。迷ったらM

**分類結果一覧**:

| # | ファイル名 | 粒度 | 対象リポ | 根拠 |
|---|-----------|------|---------|------|
| 1 | Building-trust-through-layers活用検討.md | L | aidd | 設計原則の検討・適用、アーキテクチャ設計 |
| 2 | L1マネージャー実作業禁止の構造的強制.md | M | dpi | SKILL.md修正+Hook実装+ルール追加で3-5ファイル |
| 3 | L2知見発見と修正適用のギャップ改善.md | M | dpi | ワークフロー変更+ルール追加で3-5ファイル |
| 4 | LLMローカル開発のセキュリティ強化.md | L | 横断 | 複数リポ横断のセキュリティ設定 |
| 5 | PostToolUse-hookルール変更連動チェック.md | M | dpi | Hook実装+設定+テストで3-5ファイル |
| 6 | PreToolUse-hookコミットメッセージバリデーション.md | M | dpi | Hook実装+設定+テストで3-5ファイル |
| 7 | SC-008壊れた参照修正.md | S | dpi | 3箇所の文字列置換のみ、2ファイル |
| 8 | SCチェックQuickWins一括是正.md | S | dpi | 分解済み→SC-008に集約、実質2ファイル修正 |
| 9 | agentsの公式ディレクトリ分け.md | M | dpi | スキル移植+ガイド追加+エージェント作成 |
| 10 | agentsの管理方法のガイドライン追記.md | S | dpi | session-flow-policyまたはdocs/に1-2ファイル追記 |
| 11 | ai-driven-dev-patterns-builtin-skills-eval.md | M | aidd | 評価実施+レポート作成+適用判断 |
| 12 | ai-driven-dev-patterns-design-vs-operation-gap.md | S | aidd | 1ファイル（dev-workflow-detail.md）の記述更新 |
| 13 | ai-driven-dev-patterns-triage-standard-policy作成.md | M | aidd | ポリシーファイル新規作成+triage-worker参照更新 |
| 14 | ai-driven-dev-patterns_source-of-truth明示.md | S | aidd | CLAUDE.mdまたはrules/に1行追記+agents対応更新 |
| 15 | aidd-documentarian-rule-reference-fix.md | S | aidd | 参照先修正または2ルールファイル新規作成 |
| 16 | aidd-test-infrastructure.md | M | aidd | feature-builder+test-writer+CIスクリプト設定 |
| 17 | backlog-entries-format-unification.md | S | dpi | 13件のフォーマット変換、機械的作業 |
| 18 | backlog-maintenance-worker走査手順改善.md | S | dpi | 1ファイル（backlog-maintenance-worker.md）の手順追加 |
| 19 | claude-code-action-version-tracking.md | S | dpi | 手順文書1-2ファイルの作成 |
| 20 | claude-md-import-shrink.md | M | dpi | CLAUDE.md分割+rules/委譲+import設定で3-5ファイル |
| 21 | denyリスト変更提案への副作用分析必須化.md | S | dpi | rule-change-checklist等に1項目追加 |
| 22 | disallowedToolsフィールド活用検討.md | M | dpi | 仕様調査+エージェント定義更新+ガイド更新 |
| 23 | docs-workflow-initiative-gha-update.md | S | dpi | docs/workflow.md 1ファイルにセクション追加 |
| 24 | domain-agent-expansion.md | L | dpi | 7マネージャーへの統合、各ファイル修正 |
| 25 | domain-agent-review-session.md | M | dpi | knowledge.md更新+レビュー手順策定 |
| 26 | entries-pattern-inbox適用検討.md | S | dpi | inbox/のディレクトリ構造変更のみ |
| 27 | gha-auto-execute-skills-separation.md | M | dpi | スキルファイル新規+YAML修正+execution_file修正 |
| 28 | gha-backlog-maintenance-automation.md | M | dpi | YAMLワークフロー+スキル+設定で3-5ファイル |
| 29 | gha-guideline-other-workflows.md | M | dpi | 複数ワークフローのレビュー・修正 |
| 30 | gha-metacognition-automation.md | M | dpi | YAMLワークフロー+スキル+設定で3-5ファイル |
| 31 | gha-skill-usage-class-template.md | S | dpi | テンプレート文書1-2ファイルの作成 |
| 32 | gha-skills-disable-model-invocation.md | S | dpi | 6ファイルに1行追加だが設計判断不要、機械的 |
| 33 | gha-skills-mapping-initiative-registration.md | S | dpi | gha-skills-mapping.yml 1ファイルに4エントリ追加 |
| 34 | gha-workflow-responsibility-transfer-verification.md | S | dpi | 評価テンプレート1ファイルにパターン追記 |
| 35 | harness-engineering-periodic-check-dpi.md | L | dpi | 5観点での全面評価、多数ファイル読み取り+レポート |
| 36 | l1-pre-applied-template-task-design.md | S | dpi | SKILL.mdにガイダンス1セクション追加 |
| 37 | metacognition-managerの記述構造統一.md | S | dpi | SKILL.md 1ファイルのセクション構造変更 |
| 38 | path-scoped-rules-introduction.md | M | dpi | rules/ 5ファイルの分離+フロントマター追加 |
| 39 | per-workerファイル自動生成.md | M | dpi | スクリプト作成+ルール更新+テスト |
| 40 | permission-prompt-optimization.md | M | dpi | ルール追加+エージェント定義更新+settings.json |
| 41 | plugin-high-applicability-trial.md | M | dpi | 4プラグイン導入検証+レポート |
| 42 | posttooluse-hook-quality-check-integration.md | M | dpi | Hook実装+設定+複数チェック統合 |
| 43 | posttooluse-hook-quality-check.md | M | dpi | Hook実装+設定（BL-095と統合候補） |
| 44 | pretooluse-hook-security-guard.md | M | dpi | Hook実装+段階的導入+設定 |
| 45 | reference-doc-granularity-rule.md | S | dpi | ルール文書1ファイルの作成 |
| 46 | refs-meta-info-template.md | S | dpi | _knowledge_template.md 1ファイルの更新 |
| 47 | refs-routing-template-unification.md | M | dpi | 複数テンプレートのルーティング先統一 |
| 48 | role-format-guideのagents対応更新.md | S | aidd | SKILL.md 1ファイルの更新 |
| 49 | rules-skills移動時の波及更新パターン.md | S | dpi | SKILL.mdに関連ファイル一覧セクション追加ルール |
| 50 | sandbox-enable-settings-local.md | M | dpi | sandbox設定+settings.local.json+段階的導入 |
| 51 | session-flow-checklist-precision.md | S | dpi | session-flow-policy §5.1 に数項目追加 |
| 52 | sessionsテンプレート間連携ガイド.md | S | aidd | sessions/_template/にデータフローガイド追記 |
| 53 | sync-worker同期先コミット漏れ防止.md | S | dpi | 2-3ファイルだが各数行の修正、設計判断不要 |
| 54 | triage-action-subagent-delegation.md | M | dpi | エージェント定義新規/拡張+テンプレート修正 |
| 55 | triage-metacognitionテンプレート共通化検討.md | M | dpi | テンプレート統合+共通化設計 |
| 56 | triage-standard-policy適用マトリクス列数リスク.md | S | dpi | テーブル形式の再設計（1ファイル内） |
| 57 | user-invocable-false-description-pattern.md | S | dpi | ルール文書またはガイドに1パターン追記 |
| 58 | workflow-md-reference-skills-section.md | S | dpi | docs/workflow.md 1ファイルにセクション追加 |
| 59 | ゲート判定基準での課題重大度の明文化.md | S | dpi | manager-common-policy §4 に数行追加 |
| 60 | スキャンレポート変更理由記載ルール.md | S | dpi | metacognition-worker.md 1ファイルに1項目追加 |
| 61 | チェックリスト型スキルの標準テンプレート化.md | S | dpi | テンプレート1ファイルの作成 |
| 62 | ディレクトリ構成最適化検討.md | L | aidd | リポジトリ全体の構成見直し |
| 63 | マルチAIエージェント共通ルール適用.md | L | aidd | 複数AI間のルール共通化、アーキテクチャ設計 |
| 64 | メタ認知セッションのai-driven-dev-patterns展開.md | M | aidd | スキル定義移植+調整 |
| 65 | メタ認知セット分割粒度・スキャンモード.md | M | dpi | マネージャースキル修正+フルスキャン/差分スキャン機能 |
| 66 | リネーム時全文検索チェック義務化ルール追加.md | S | dpi | .claude/rules/ に1ファイル新規作成 |
| 67 | リンク整合性チェック標準化.md | M | dpi | スクリプト作成+チェックリスト+タスクテンプレート統合 |
| 68 | ルートリポのトリアージにTG-008走査観点追加.md | S | aidd | triage-worker.md 1ファイルに走査観点追加 |
| 69 | 全ロールファイルrole-format-guide準拠確認修正.md | M | aidd | agents/配下の複数ファイルの修正 |
| 70 | 別リポジトリ成果物の記法スタイル事前確認.md | S | dpi | l2-worker.md に1チェック項目追加 |
| 71 | 北村さんの取り組みを取り込む.md | L | aidd | 調査・評価・複数施策への分解 |
| 72 | 同期対象リスト管理と差分ベース反映計画.md | M | dpi | リスト文書+sync-manager修正+手順変更 |
| 73 | 外部リポジトリアーキテクチャオーバービュー管理.md | M | dpi | refs/にオーバービュー文書作成+sync手順統合 |
| 74 | 施策間の競合防止方針策定.md | L | 横断 | プロセス設計+競合検出の仕組み構築 |
| 75 | 条件付き固定タスク配置ルール整備.md | S | dpi | SKILL.md 1ファイルのセクション分割 |
| 76 | 社内施策_devkitのコマンドやガイドの使用クロードのskillやRuleとして用意しておく.md | M | 横断 | スキル/ルール作成+社内環境調査 |
| 77 | 長文rulesのコンテキストコスト最適化.md | M | 横断 | 複数rules/のskills化+設定変更 |
| 78 | 高度な並列化と協調プロトコル統合.md | L | aidd | 並列化パターン拡張+協調プロトコル統合+Agent Teams |

**集計**:
- S: 33件
- M: 32件
- L: 13件

**成果物**: 上記分類結果一覧
**課題・気づき**:
- 統合候補（BM-005で検出済み）のエントリが複数あり、テーマ別グルーピング時に考慮が必要
- `gha-skills-disable-model-invocation.md` は6ファイル変更だが、各1行追加の機械的作業のためSに分類
- `sync-worker同期先コミット漏れ防止.md` はinitiative開始済みだが残存している
