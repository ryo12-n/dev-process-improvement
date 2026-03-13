# タスクリスト: Claude Code 標準 plugin 情報整理

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | Claude Code 公式プラグイン一覧の調査 | 公式ドキュメント・GitHub・技術記事から主要プラグインのリストが作成されていること。カテゴリ分類（開発フロー系、設定・自動化系、LSP系、その他）が完了していること | 🔴 | ⬜ |
| T-002 | 各プラグインの dev-process-improvement 適用可能性評価 | 各プラグインに「高・中・低・対象外」の適用可能性が付与されていること。評価根拠（プロジェクト特性との適合性）が記載されていること | 🔴 | ⬜ |
| T-003 | リファレンス文書の作成 | `.claude/skills/plugin-reference/SKILL.md` が作成されていること。builtin-skills-reference と同等の記述構造（評価サマリー、各プラグイン詳細評価、総合方針）を持つこと。frontmatter（name, description, user-invocable: false）が設定されていること | 🔴 | ⬜ |
| T-004 | 知見の記録（固定タスク） | 04_work_report.md の「ルール化候補」「参考情報」テーブルにそれぞれ1行以上記載されていること | 🟡 | ⬜ |
| T-005 | 課題の CSV 転記（固定タスク） | 07_issues.md に起票した課題を issues/ の CSV に転記していること（課題がない場合は「該当なし」と記載） | 🟡 | ⬜ |

### 補足: T-001 の調査出発点

壁打ちでユーザーから以下のプラグイン情報が提供されている。これを出発点として調査を開始する:

**開発フロー・レビュー系**: commit-commands, code-review, pr-review-toolkit, feature-dev, frontend-design
**設定・自動化系**: claude-code-setup, hookify, claude-md-management, plugin-dev, skill-creator, example-plugin
**LSP系**: typescript-lsp, その他言語向け LSP プラグイン

**参考URL**:
- 公式ドキュメント: https://code.claude.com/docs/en/discover-plugins
- GitHub: https://github.com/anthropics/claude-code/tree/main/plugins
- Zenn（全59個解説）: https://zenn.dev/chmod644/articles/claude-code-plugins-all-59

### 補足: T-003 の成果物配置

- 新規ディレクトリ `.claude/skills/plugin-reference/` を作成
- `SKILL.md` に frontmatter + 評価内容を記載
- `builtin-skills-reference/SKILL.md` のフォーマットを踏襲

### 補足: 適用対象環境

本施策の成果物は dev-process-improvement リポジトリ内で完結する（CLI / SDK いずれでも参照可能）。

---
**作成者**: L1
**最終更新**: 2026-03-13
