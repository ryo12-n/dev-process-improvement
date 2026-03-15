# スキャン計画: Phase 1（情報収集）

## 壁打ちフェーズ [2026-03-15]

### 理解のサマリー
- タスクの目的: Claude Code 公式ドキュメントから最新の設定仕様を収集し、リファレンスファイルを更新する
- スコープ: CO-001〜CO-007（settings.json, rules/, skills/, hooks, CLAUDE.md, plugins, その他設定）
- 完了条件: リファレンスの全7セクションが具体的情報で更新され、Snapshot Date が 2026-03-15 に更新

### 前提条件チェック
- [x] 割り当てタスクの内容を理解: 理解済み
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み（リファレンスファイルはテンプレート状態）
- [x] 前フェーズの成果物（該当する場合）の確認: N/A（初回収集）

### 不明点・確認事項
- なし。WebSearch で公式ドキュメントを収集する方針で進める。

### 壁打ち結果 [2026-03-15 作業開始]
- 7つのCOターゲットは独立して収集可能。WebSearchを並列実行する。
- 公式ドキュメント（docs.anthropic.com）とGitHub（anthropics/claude-code）を主要ソースとする。
- 収集後、リファレンスファイルを一括更新し、scan_reportとwork_logを作成する。

---

## スキャン計画

### 走査対象

| # | 対象 | 走査方法 | 期待する出力 |
|---|------|---------|------------|
| 1 | CO-001: settings.json | WebSearch で公式ドキュメント検索 | フィールド一覧・型・デフォルト値 |
| 2 | CO-002: rules/ | WebSearch で公式ドキュメント検索 | ルールファイルフォーマット・パススコープ記法 |
| 3 | CO-003: skills/ | WebSearch で公式ドキュメント検索 | SKILL.md フロントマター・description 最適化 |
| 4 | CO-004: hooks | WebSearch で公式ドキュメント検索 | 全フックタイプの仕様・設定スキーマ |
| 5 | CO-005: CLAUDE.md | WebSearch で公式ドキュメント検索 | import構文・サイズガイドライン・読み込み順 |
| 6 | CO-006: plugins | WebSearch で公式ドキュメント検索 | プラグインシステム仕様 |
| 7 | CO-007: その他設定 | WebSearch で公式ドキュメント検索 | settings.local.json, memory, sandbox, 環境変数 |

### 走査順序・依存関係

- CO-001〜CO-007 は独立して収集可能。並列で WebSearch を実行する。
- CO-001（settings.json）と CO-004（hooks）は関連するため、settings.json 内の hooks フィールドは CO-004 で詳述する。
