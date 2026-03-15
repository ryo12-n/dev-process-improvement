# 外部リポジトリ知見: agency-agents

## メタ情報

| 項目 | 内容 |
|------|------|
| 用途 | dev-process-improvement の L1 マネージャーが施策ディスパッチ時にドメインエージェントを選定し、L2-worker に専門知識として参照させるためのカタログ |
| 有効期限 | 2026-06-15（取得日から3ヶ月。定期レビューセッションで更新を検討） |
| 取得日 | 2026-03-15 |
| 取得方法 | `git clone https://github.com/msitarzewski/agency-agents.git` → `.git/` 削除 → `refs/agency-agents/` に配置 |

## リポジトリ概要

| 項目 | 内容 |
|------|------|
| リポジトリ名 | msitarzewski/agency-agents |
| 主要技術スタック | Markdown（エージェント定義）、Bash（scripts/）|
| ディレクトリ構成 | 13 エージェント部門ディレクトリ + examples / integrations / strategy / scripts |

## エージェントカタログ

### 部門一覧

| # | 部門 | エージェント数 | 代表的エージェント | 推奨マッチング条件 |
|---|------|-------------|----------------|-----------------|
| 1 | academic | 5 | academic-historian, academic-psychologist, academic-narratologist | リサーチ重視の調査・分析タスク、学術的観点での知見整理 |
| 2 | design | 8 | design-ux-architect, design-ui-designer, design-ux-researcher | UI/UX 設計、ブランドガイドライン、ユーザビリティ改善 |
| 3 | engineering | 23 | engineering-software-architect, engineering-code-reviewer, engineering-devops-automator, engineering-security-engineer, engineering-technical-writer | コード実装、アーキテクチャ設計、DevOps、セキュリティ、技術文書 |
| 4 | game-development | 5 | game-designer, level-designer, narrative-designer, technical-artist | ゲーム開発関連（通常の施策では該当少） |
| 5 | marketing | 27 | marketing-content-creator, marketing-seo-specialist, marketing-growth-hacker | マーケティング戦略、コンテンツ作成、SEO（通常の施策では該当少） |
| 6 | paid-media | 7 | paid-media-ppc-strategist, paid-media-tracking-specialist | 広告運用（通常の施策では該当少） |
| 7 | product | 5 | product-manager, product-feedback-synthesizer, product-sprint-prioritizer | プロダクト管理、フィードバック分析、優先順位付け |
| 8 | project-management | 6 | project-management-project-shepherd, project-manager-senior, project-management-experiment-tracker | プロジェクト管理、ワークフロー最適化、実験追跡 |
| 9 | sales | 8 | sales-engineer, sales-account-strategist, sales-pipeline-analyst | 営業プロセス（通常の施策では該当少） |
| 10 | spatial-computing | 6 | visionos-spatial-engineer, xr-interface-architect | XR/空間コンピューティング（通常の施策では該当少） |
| 11 | specialized | 27 | specialized-workflow-architect, specialized-mcp-builder, specialized-document-generator, compliance-auditor, agents-orchestrator | ワークフロー設計、MCP 構築、ドキュメント生成、コンプライアンス |
| 12 | support | 6 | support-support-responder, support-analytics-reporter, support-legal-compliance-checker | サポート対応、分析レポート、法的コンプライアンス |
| 13 | testing | 8 | testing-accessibility-auditor, testing-api-tester, testing-workflow-optimizer, testing-performance-benchmarker | テスト戦略、品質保証、ワークフロー最適化 |

### 非エージェント部門

| ディレクトリ | 内容 | 参照用途 |
|-------------|------|---------|
| examples | ワークフロー例（startup-mvp, landing-page, book-chapter 等） | エージェント連携パターンの参考 |
| integrations | ツール統合設定（claude-code, cursor, aider 等） | ツール統合時の参考 |
| strategy | 戦略フレームワーク（nexus-strategy, playbooks, runbooks） | オーケストレーション設計の参考 |
| scripts | ユーティリティスクリプト（convert, install, lint） | リポジトリメンテナンス用 |

### エージェント総数

**141 エージェント**（13部門合計、非エージェント部門を除く）

## 施策タイプ別推奨マッピング

dev-process-improvement の施策パターンに基づき、各タイプで参照すべきドメインエージェントを推奨する。

| # | 施策タイプ | 推奨エージェント | 参照パス | 参照理由 |
|---|-----------|----------------|---------|---------|
| 1 | ルール変更（skills/rules 変更） | specialized-workflow-architect | `specialized/specialized-workflow-architect.md` | ワークフロー設計の専門知識。ルール間整合性・影響範囲の分析に活用 |
| 2 | GHA 構築・自動化 | engineering-devops-automator | `engineering/engineering-devops-automator.md` | CI/CD パイプライン・自動化の専門知識。GHA ワークフロー設計に活用 |
| 3 | テンプレート改善 | specialized-document-generator | `specialized/specialized-document-generator.md` | ドキュメント構造設計の専門知識。テンプレートの構造最適化に活用 |
| 4 | セキュリティ施策 | engineering-security-engineer | `engineering/engineering-security-engineer.md` | セキュリティ設計の専門知識。権限モデル・脅威分析に活用 |
| 5 | 評価・品質保証系 | testing-workflow-optimizer | `testing/testing-workflow-optimizer.md` | テストワークフロー最適化の専門知識。評価計画・基準設計に活用 |
| 6 | 自動化候補評価 | automation-governance-architect | `specialized/automation-governance-architect.md` | 自動化ガバナンスの専門知識。費用対効果・リスク評価に活用 |
| 7 | コードレビュー・実装系 | engineering-code-reviewer, engineering-software-architect | `engineering/engineering-code-reviewer.md`, `engineering/engineering-software-architect.md` | コード品質・アーキテクチャの専門知識。実装タスクの品質向上に活用 |
| 8 | プロセス改善・ワークフロー最適化 | project-management-project-shepherd, testing-workflow-optimizer | `project-management/project-management-project-shepherd.md`, `testing/testing-workflow-optimizer.md` | プロジェクト管理・ワークフロー最適化の専門知識。プロセス設計に活用 |

## 蓄積された知見

| # | 施策名 | 日付 | 知見カテゴリ | 内容 | 元ログ |
|---|--------|------|------------|------|--------|
| 1 | agency-agents-integration | 2026-03-15 | アーキテクチャ | 13部門141エージェント。計画時の12部門想定より1部門多い（spatial-computing）。非エージェント部門（examples, integrations, strategy, scripts）も参考資料として有用 | — |
| 2 | agency-agents-integration | 2026-03-15 | 運用 | エージェント定義は Markdown 形式で、system prompt として直接利用可能な構造。ただし本施策では「役割を引き受ける」のではなく「専門知識として参照する」制約を設ける | — |

---
**テンプレート作成日**: 2026-03-14
**用途**: `refs/agency-agents/knowledge.md` — L1 マネージャーのドメインエージェント選定カタログ
