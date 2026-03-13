---
name: plugin-reference
description: Claude Code 公式プラグインの評価結果・適用可能性の参照。プラグイン導入判断や活用方針の検討時に参照する
user-invocable: false
---

# Claude Code 公式プラグイン評価リファレンス

## 概要

Claude Code 公式マーケットプレイス（`claude-plugins-official`）に登録されているプラグインの、dev-process-improvement プロジェクトにおける適用可能性を評価した結果をまとめたリファレンス。プラグイン導入判断や、新規プラグイン評価時の参考として参照する。

**評価日**: 2026-03-13
**評価対象**: claude-plugins-official マーケットプレイス登録プラグイン（内部 29 個 + 外部 47 個 = 計 76 個）
**補足対象**: anthropics/claude-code デモマーケットプレイス（13 個、公式マーケットプレイスと重複あり）
**プロジェクト特性**: Markdown 文書・プロセスルール管理が主体。コード実装は含まない

## カテゴリ分類

公式プラグインを以下の 6 カテゴリに分類した。

| カテゴリ | プラグイン数 | 概要 |
|---------|------------|------|
| コードインテリジェンス（LSP）系 | 12 | 言語サーバー連携による型チェック・定義ジャンプ等 |
| 開発フロー・レビュー系 | 10 | Git ワークフロー、PR レビュー、機能開発支援 |
| 設定・自動化・プラグイン開発系 | 7 | Claude Code 環境設定、フック作成、スキル・プラグイン開発 |
| 出力スタイル系 | 2 | Claude の応答スタイルカスタマイズ |
| 外部サービス連携（MCP）系 | 43 | GitHub/GitLab、プロジェクト管理、インフラ、決済等 |
| その他（特殊用途） | 2 | 自律開発ループ、セキュリティフック等 |

## 適用可能性サマリー

dev-process-improvement プロジェクト（Markdown 文書・プロセスルール管理主体、コード実装なし）への適用可能性を 4 段階で評価した。

### 適用可能性: 高

| プラグイン | カテゴリ | 提供元 | 推奨利用場面 |
|-----------|---------|--------|------------|
| commit-commands | 開発フロー系 | Anthropic | L1/L2 セッションでの git commit/push/PR 作成の標準化 |
| claude-md-management | 設定・自動化系 | Anthropic | CLAUDE.md の品質維持・改善提案 |
| claude-code-setup | 設定・自動化系 | Anthropic | リポジトリ分析に基づく Claude Code 設定の最適化提案 |
| skill-creator | 設定・自動化系 | Anthropic | `.claude/skills/` 配下のスキル作成・改善・評価 |

### 適用可能性: 中

| プラグイン | カテゴリ | 提供元 | 推奨利用場面 |
|-----------|---------|--------|------------|
| hookify | 設定・自動化系 | Anthropic | 禁止操作の自動検知フック作成（施策外ファイル変更防止等） |
| plugin-dev | 設定・自動化系 | Anthropic | 独自プラグイン開発時の参考・ガイド |
| pr-review-toolkit | 開発フロー系 | Anthropic | PR レビューの品質向上（文書変更のレビュー観点追加） |
| github | 外部連携系 | External | GitHub Issues/PR の操作を Claude Code 内で完結 |
| explanatory-output-style | 出力スタイル系 | Anthropic | 設計判断の教育的説明の付加（オンボーディング用途） |

### 適用可能性: 低

| プラグイン | カテゴリ | 提供元 | 備考 |
|-----------|---------|--------|------|
| code-review | 開発フロー系 | Anthropic | コードレビュー主体、Markdown 変更には過剰 |
| code-simplifier | 開発フロー系 | Anthropic | コード簡素化が目的、文書には不向き |
| feature-dev | 開発フロー系 | Anthropic | 7 フェーズの機能開発ワークフロー、コード前提 |
| security-guidance | その他 | Anthropic | セキュリティパターン監視、コード編集前提 |
| ralph-loop | その他 | Anthropic | 自律開発ループ、長時間セッション前提 |
| learning-output-style | 出力スタイル系 | Anthropic | コード貢献を要求する学習モード、文書作業と不適合 |
| agent-sdk-dev | 開発フロー系 | Anthropic | Agent SDK 開発支援、本プロジェクトでは不使用 |
| frontend-design | 開発フロー系 | Anthropic | フロントエンド UI 作成、適用場面なし |
| playground | 開発フロー系 | Anthropic | インタラクティブ HTML 生成、適用場面なし |

### 適用可能性: 対象外

| プラグイン群 | 理由 |
|-------------|------|
| LSP プラグイン全 12 種（typescript-lsp, pyright-lsp, gopls-lsp, rust-analyzer-lsp, clangd-lsp, php-lsp, swift-lsp, kotlin-lsp, csharp-lsp, jdtls-lsp, lua-lsp, ruby-lsp） | コード実装を含まないため言語サーバー不要 |
| 外部サービス連携プラグイン大半（supabase, firebase, vercel, stripe, laravel-boost, playwright, figma, sentry, slack, atlassian, asana, linear, notion, gitlab 等 40 種以上） | 本プロジェクトで使用しないサービス |

## 各プラグイン詳細評価（適用可能性: 高）

### commit-commands

**機能概要**: Git のコミット・プッシュ・PR 作成をコマンド化するプラグイン。`/commit-commands:commit` でステージング・コミットメッセージ生成・コミットを一括実行。

**プロジェクトでの適用可能性**: **高**

本プロジェクトの L1/L2 セッションでは頻繁に git 操作を行う。コミットメッセージ規約（`.claude/rules/commit-message.md`）との整合性を確保しつつ、操作を標準化できる。

**具体的な利用シーン**:
- L2 ワーカーの作業完了時のコミット・プッシュフロー
- PR 作成の自動化（セッション終了時のブランチ整理フローとの統合）

**制約事項**:
- コミットメッセージのフォーマットが本プロジェクトの規約（`[session-type] category: summary`）と一致するかは要検証
- カスタマイズ可能かどうかでプラグインの実用性が変わる

### claude-md-management

**機能概要**: CLAUDE.md ファイルの保守・改善ツール。CLAUDE.md の品質分析・改善提案・構造最適化を行う。

**プロジェクトでの適用可能性**: **高**

本プロジェクトの CLAUDE.md はプロジェクトルール全体を定義する中核文書であり、継続的な品質維持が重要。肥大化検知やルール整合性チェックに活用できる。

**具体的な利用シーン**:
- CLAUDE.md の定期メンテナンス（150 行制限の監視等）
- 新規ルール追加時の整合性確認
- ドキュメント階層方針に基づく分離提案

**制約事項**:
- 本プロジェクト固有のドキュメント階層方針（README → docs/ → docs/design/）との整合性は手動確認が必要

### claude-code-setup

**機能概要**: コードベースを分析し、Claude Code の最適な自動化設定（skills, hooks, MCP サーバー等）を推奨する。

**プロジェクトでの適用可能性**: **高**

本プロジェクトは `.claude/skills/` 配下に多数のカスタムスキルを持つ。リポジトリ構造の変化に応じた設定最適化の提案を受けられる。

**具体的な利用シーン**:
- 新しいワークフロー追加時の設定レビュー
- 既存スキル構成の最適化提案
- settings.json の改善提案

**制約事項**:
- 汎用的な推奨が多い可能性あり（プロセス管理特化リポジトリは一般的でない）

### skill-creator

**機能概要**: スキルのゼロからの作成、既存スキルの改善、評価（eval）、性能ベンチマークを支援。トリガー説明文の最適化機能も含む。

**プロジェクトでの適用可能性**: **高**

本プロジェクトは `.claude/skills/` 配下のスキル管理が中核業務。新規スキル作成や既存スキルの description 最適化に直接活用できる。

**具体的な利用シーン**:
- 新規スキル作成時のベストプラクティス適用
- 既存スキルの description（自動トリガー条件）の最適化
- スキル性能の定量評価

**制約事項**:
- 評価機能がコード系スキルを前提としている場合、文書管理系スキルの評価に適さない可能性

## 各プラグイン詳細評価（適用可能性: 中）

### hookify

**機能概要**: 会話分析に基づき、望ましくない動作を防止するカスタムフックを作成する。

**プロジェクトでの適用可能性**: **中**

L2 セッションによる禁止操作（L1 管轄ファイルの変更等）の自動検知フックとして活用可能。ただし、本プロジェクトの禁止事項は CLAUDE.md のルールで既に定義されており、フック化の必要性は限定的。

**具体的な利用シーン**:
- 施策フォルダ外ファイルへの無断変更防止フック
- L2 が plan/gate_review を変更しようとした場合の警告フック

**制約事項**:
- ルールベースの制御（CLAUDE.md）とフックベースの制御の二重管理になるリスク
- フックの保守コストと効果のバランスを考慮する必要あり

### plugin-dev

**機能概要**: Claude Code プラグイン開発の包括的ツールキット。フック・MCP 統合・コマンド・エージェント・ベストプラクティスをカバーする 7 種の専門スキル。

**プロジェクトでの適用可能性**: **中**

本プロジェクトがプラグイン開発を行う場合に有用。現時点ではプラグイン開発の予定はないが、hookify や skill-creator の活用が進んだ場合にプラグインとしてパッケージ化する可能性がある。

**具体的な利用シーン**:
- 本プロジェクトのスキル群をプラグインとしてパッケージ化する場合
- カスタムフックの高度な開発

**制約事項**:
- 現時点ではプラグイン開発の直接的ニーズがない

### pr-review-toolkit

**機能概要**: PR レビューに特化したエージェント群。コメント品質、テスト、エラーハンドリング、型設計、コード品質、コード簡素化の観点でレビュー。

**プロジェクトでの適用可能性**: **中**

本プロジェクトの PR は主に Markdown 文書の変更だが、コメント品質やレビュー漏れの検出には活用可能性がある。コード品質やテスト系のエージェントは対象外。

**具体的な利用シーン**:
- Markdown 文書変更の PR で、記述の一貫性・用語統一をチェック
- ゲートレビュー前の PR 品質確認

**制約事項**:
- コードレビュー前提の設計のため、Markdown 文書へのレビュー品質は未検証
- 6 つのエージェントのうち活用可能なのは一部に限られる

### github（外部プラグイン）

**機能概要**: GitHub 公式 MCP サーバー。Issues、PR、リポジトリ管理を Claude Code 内で操作。

**プロジェクトでの適用可能性**: **中**

本プロジェクトは GitHub で管理されており、Issues/PR 操作を Claude Code セッション内で完結できる利点がある。ただし `gh` CLI で多くの操作は既に可能。

**具体的な利用シーン**:
- Issues の一括操作（ラベル付け、マイルストーン設定等）
- PR のステータス確認・コメント追加

**制約事項**:
- `gh` CLI との機能重複が大きい
- MCP サーバーの追加設定が必要

### explanatory-output-style

**機能概要**: 実装選択やコードベースパターンに関する教育的説明を Claude の応答に付加する。

**プロジェクトでの適用可能性**: **中**

新規メンバーのオンボーディングや、ルール・スキル設計の意図説明に活用可能。日常的な作業では冗長になる可能性。

**具体的な利用シーン**:
- 新規メンバーがプロジェクト構造を理解する際の補助
- 複雑なスキル設計の意図を説明する場合

**制約事項**:
- 常時有効にすると応答が冗長化し、作業効率が低下する可能性
- 必要なときのみ有効化する運用が望ましい

## 公式プラグイン全一覧

### 内部プラグイン（Anthropic 開発・29 個）

| # | プラグイン名 | カテゴリ | 適用可能性 | 概要 |
|---|------------|---------|-----------|------|
| 1 | typescript-lsp | LSP | 対象外 | TypeScript/JavaScript 言語サーバー |
| 2 | pyright-lsp | LSP | 対象外 | Python 言語サーバー（Pyright） |
| 3 | gopls-lsp | LSP | 対象外 | Go 言語サーバー |
| 4 | rust-analyzer-lsp | LSP | 対象外 | Rust 言語サーバー |
| 5 | clangd-lsp | LSP | 対象外 | C/C++ 言語サーバー |
| 6 | php-lsp | LSP | 対象外 | PHP 言語サーバー（Intelephense） |
| 7 | swift-lsp | LSP | 対象外 | Swift 言語サーバー（SourceKit-LSP） |
| 8 | kotlin-lsp | LSP | 対象外 | Kotlin 言語サーバー |
| 9 | csharp-lsp | LSP | 対象外 | C# 言語サーバー |
| 10 | jdtls-lsp | LSP | 対象外 | Java 言語サーバー（Eclipse JDT.LS） |
| 11 | lua-lsp | LSP | 対象外 | Lua 言語サーバー |
| 12 | ruby-lsp | LSP | 対象外 | Ruby 言語サーバー |
| 13 | commit-commands | 開発フロー系 | 高 | Git コミット・プッシュ・PR 作成の自動化 |
| 14 | pr-review-toolkit | 開発フロー系 | 中 | PR レビュー特化エージェント群 |
| 15 | code-review | 開発フロー系 | 低 | 5 並列エージェントによる自動コードレビュー |
| 16 | code-simplifier | 開発フロー系 | 低 | コードの簡素化・リファクタリング |
| 17 | feature-dev | 開発フロー系 | 低 | 7 フェーズ機能開発ワークフロー |
| 18 | frontend-design | 開発フロー系 | 低 | プロダクション品質の UI 作成 |
| 19 | playground | 開発フロー系 | 低 | インタラクティブ HTML プレイグラウンド生成 |
| 20 | agent-sdk-dev | 開発フロー系 | 低 | Claude Agent SDK 開発支援 |
| 21 | claude-code-setup | 設定・自動化系 | 高 | コードベース分析による設定最適化提案 |
| 22 | claude-md-management | 設定・自動化系 | 高 | CLAUDE.md の保守・改善ツール |
| 23 | skill-creator | 設定・自動化系 | 高 | スキル作成・改善・評価ツール |
| 24 | hookify | 設定・自動化系 | 中 | カスタムフック作成ツール |
| 25 | plugin-dev | 設定・自動化系 | 中 | プラグイン開発ツールキット |
| 26 | explanatory-output-style | 出力スタイル系 | 中 | 教育的説明付き応答スタイル |
| 27 | learning-output-style | 出力スタイル系 | 低 | インタラクティブ学習モード |
| 28 | security-guidance | その他 | 低 | セキュリティパターン監視フック |
| 29 | ralph-loop | その他 | 低 | 自律的反復開発ループ |

### 外部プラグイン（サードパーティ・47 個）

| # | プラグイン名 | カテゴリ | 適用可能性 | 概要 |
|---|------------|---------|-----------|------|
| 1 | github | ソース管理 | 中 | GitHub 公式 MCP サーバー |
| 2 | gitlab | ソース管理 | 対象外 | GitLab 連携 |
| 3 | greptile | コード検索 | 対象外 | AI コードベース検索 |
| 4 | serena | コード解析 | 対象外 | セマンティックコード解析 MCP |
| 5 | sourcegraph | コード検索 | 対象外 | コード検索・理解 |
| 6 | playwright | テスト | 対象外 | ブラウザ自動化・E2E テスト |
| 7 | atlassian | プロジェクト管理 | 対象外 | Jira/Confluence 連携 |
| 8 | asana | プロジェクト管理 | 対象外 | Asana 連携 |
| 9 | linear | プロジェクト管理 | 対象外 | Linear 連携 |
| 10 | notion | プロジェクト管理 | 対象外 | Notion 連携 |
| 11 | figma | デザイン | 対象外 | Figma 連携 |
| 12 | supabase | インフラ | 対象外 | Supabase DB/Auth 連携 |
| 13 | firebase | インフラ | 対象外 | Google Firebase 連携 |
| 14 | vercel | インフラ | 対象外 | Vercel デプロイ連携 |
| 15 | railway | インフラ | 対象外 | Railway デプロイ連携 |
| 16 | stripe | 決済 | 対象外 | Stripe 開発連携 |
| 17 | sentry | 監視 | 対象外 | Sentry エラー監視連携 |
| 18 | slack | コミュニケーション | 対象外 | Slack 連携 |
| 19 | laravel-boost | フレームワーク | 対象外 | Laravel 開発ツールキット |
| 20 | context7 | ドキュメント | 対象外 | 最新ドキュメント参照 MCP |
| 21 | pinecone | データベース | 対象外 | Pinecone ベクトル DB 連携 |
| 22 | huggingface-skills | ML | 対象外 | HuggingFace モデル・データセット操作 |
| 23 | circleback | コンテキスト | 対象外 | 会話コンテキスト連携 |
| 24 | superpowers | 開発支援 | 対象外 | ブレインストーミング・サブエージェント開発 |
| 25 | posthog | 分析 | 対象外 | PostHog アナリティクス連携 |
| 26 | coderabbit | レビュー | 対象外 | CodeRabbit コードレビュー連携 |
| 27 | sonatype-guide | セキュリティ | 対象外 | ソフトウェアサプライチェーンインテリジェンス |
| 28 | firecrawl | Web | 対象外 | Web スクレイピング・クローリング |
| 29 | qodo-skills | 開発支援 | 対象外 | 再利用可能 AI エージェントスキルライブラリ |
| 30 | semgrep | セキュリティ | 対象外 | セキュリティ脆弱性検出 |
| 31 | pagerduty | 監視 | 対象外 | PagerDuty リスクスコアリング |
| 32 | postman | API | 対象外 | API ライフサイクル管理 |
| 33 | chrome-devtools-mcp | デバッグ | 対象外 | Chrome DevTools 連携 |
| 34 | planetscale | データベース | 対象外 | PlanetScale DB 連携 |
| 35 | rc | 決済 | 対象外 | RevenueCat 設定管理 |
| 36 | adspirer-ads-agent | 広告 | 対象外 | クロスプラットフォーム広告管理 |
| 37 | amazon-location-service | AWS | 対象外 | AWS 位置情報サービス |
| 38 | aws-serverless | AWS | 対象外 | AWS サーバーレスアプリケーション |
| 39 | migration-to-aws | AWS | 対象外 | AWS 移行評価 |
| 40 | deploy-on-aws | AWS | 対象外 | AWS デプロイ支援 |
| 41 | zapier | 自動化 | 対象外 | 8,000+ アプリ連携自動化 |
| 42 | sanity-plugin | CMS | 対象外 | Sanity コンテンツプラットフォーム連携 |
| 43 | data | データエンジニアリング | 対象外 | Apache Airflow/Astronomer 連携 |
| 44 | legalzoom | リーガル | 対象外 | 法務ガイダンス |
| 45 | mintlify | ドキュメント | 対象外 | ドキュメントサイト生成 |
| 46 | sumup | 決済 | 対象外 | SumUp 決済連携 |
| 47 | wix | Web | 対象外 | Wix サイト・アプリ管理 |

## 総合方針

### 積極活用を推奨するプラグイン

| プラグイン | 推奨理由 | 導入優先度 |
|-----------|---------|-----------|
| claude-md-management | CLAUDE.md の品質維持は本プロジェクトの中核。定期メンテナンスに直結 | 高 |
| skill-creator | スキル管理が中核業務。作成・改善・評価の全工程で活用可能 | 高 |
| commit-commands | git 操作の標準化。コミットメッセージ規約との統合を検証した上で導入 | 高（要検証） |
| claude-code-setup | リポジトリ設定の最適化提案。初回実行で効果を検証可能 | 中 |

### 状況に応じて活用するプラグイン

- **hookify**: 禁止操作の自動検知が繰り返し問題になる場合に導入を検討
- **pr-review-toolkit**: PR レビューの品質向上が必要な場合に導入を検討
- **plugin-dev**: スキル群のプラグインパッケージ化を行う場合に活用
- **github**: `gh` CLI では不十分な GitHub 操作ニーズが発生した場合に導入
- **explanatory-output-style**: オンボーディング目的で一時的に有効化

### 活用しないプラグイン

- **LSP プラグイン全 12 種**: コード実装を含まないため不要
- **外部サービス連携プラグイン大半**: 本プロジェクトで使用しないサービス
- **コードレビュー系（code-review, code-simplifier）**: コード前提の設計、文書には不適合
- **機能開発系（feature-dev, frontend-design, playground）**: コード開発ワークフロー、適用場面なし
- **agent-sdk-dev**: Agent SDK 開発を行わないため不要
- **ralph-loop**: 長時間自律開発ループ、本プロジェクトの単発セッション型と不適合
- **learning-output-style**: コード貢献を要求するモード、文書作業と不適合
- **security-guidance**: コード編集時のセキュリティパターン監視、適用場面なし

### 再評価の推奨タイミング

- 公式マーケットプレイスへの新規プラグイン追加時（現在も拡大中）
- プロジェクトの性質が変わった場合（コード実装を含む施策が増えた等）
- 既存プラグインの機能アップデート時
- 「適用可能性: 高」プラグインの導入後、実際の効果に基づく再評価
