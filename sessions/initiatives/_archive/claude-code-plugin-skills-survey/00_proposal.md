# 改善施策提案: Claude Code 標準 plugin 情報整理

## 背景・課題

Claude Code は 2026年3月時点で公式マーケットプレイス（`claude-plugins-official`）に50〜60個規模の公式プラグインを提供している。しかし本リポジトリ（dev-process-improvement）では、これらのプラグインの調査・評価が行われておらず、活用の機会を逃している可能性がある。

既存の `.claude/skills/builtin-skills-reference/SKILL.md` でビルトイン skills（/simplify, /batch, /debug, /loop, /claude-api）の評価は完了しているが、plugins エコシステムは未調査。

## 目標

1. Claude Code 公式プラグインのうち、dev-process-improvement プロジェクトに適用可能なものを特定する
2. 有用と判断されたプラグインの導入可否・設定方法を整理し、リファレンス文書として `.claude/skills/` に配置する
3. 即時導入可能なプラグインがあれば、導入手順を明確にする

## スコープ
### やること
- Claude Code 公式プラグイン一覧の調査（公式マーケットプレイス / GitHub `anthropics/claude-code` の `plugins/` ディレクトリ）
- 各プラグインの dev-process-improvement プロジェクトへの適用可能性評価
- 評価結果のリファレンス文書作成（`.claude/skills/plugin-reference/SKILL.md`）
- 導入推奨プラグインがある場合、具体的な設定手順の文書化

### やらないこと
- ビルトイン skills の再評価（`builtin-skills-reference` で評価済み）
- ai-driven-dev-patterns リポジトリへのプラグイン導入検討（別施策 `ai-driven-dev-patterns-builtin-skills-eval` のスコープ）
- コミュニティ製（非公式）プラグインの調査
- プラグインの実際のインストール・有効化（評価結果を踏まえた導入は別施策とする）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- プラグインエコシステムの全体像把握により、今後のプロセス改善の選択肢が広がる
- 適用可能なプラグインが見つかった場合、開発プロセスの効率化に直結する
- リファレンス文書により、将来のプラグイン評価・導入判断が効率化される

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| プラグインの情報がWeb調査に依存し、正確性が限定的 | 中 | 公式ドキュメント・GitHubリポジトリを優先情報源とする |
| 評価時点のプラグイン情報が陳腐化する | 低 | 評価日・対象バージョンを明記し、再評価タイミングを記載する |
| 適用可能なプラグインが少ない可能性 | 低 | Markdown/プロセス管理主体のプロジェクト特性を踏まえ、「適用場面なし」も有効な成果とする |

## 壁打ちの背景

壁打ちで以下を確認・決定した:

1. **スコープを plugin に限定**: ビルトイン skills は `builtin-skills-reference` で評価済みのため除外。本施策は plugin エコシステム（公式マーケットプレイス経由のプラグイン）に焦点を当てる
2. **既存リファレンスとの棲み分け**: `builtin-skills-reference` はそのまま維持し、新たに `plugin-reference` を別 skill として作成する
3. **ユーザーからの情報提供**: 公式プラグインの具体例（commit-commands, code-review, claude-code-setup, hookify, claude-md-management, typescript-lsp 等）やカテゴリ（開発フロー・レビュー系、設定・自動化系、LSP系）の情報を得ており、調査の出発点として活用する

## 備考・設計パターン

本施策は調査・評価型であり、成果物は主にリファレンス文書。`builtin-skills-reference` と同じパターン（SKILL.md に評価サマリーと詳細評価を記載）を踏襲する。

**バージョン依存の前提**: 2026年3月時点の Claude Code 公式プラグイン一覧に基づく。プラグインの追加・変更は随時行われるため、評価日を明記する。

---
**起票者**: L1
**起票日**: 2026-03-13
**ステータス**: 実施中
**backlog元ファイル**: Claude Code標準plugin・skills情報整理.md
