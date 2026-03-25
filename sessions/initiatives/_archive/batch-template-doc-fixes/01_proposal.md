# 改善施策提案: batch-template-doc-fixes

## 背景・課題
backlog-inventory-batch 施策で棚卸し・分類した78件のバックログのうち、S分類のドキュメント・テンプレート整備に関する6件が未消化。個別施策にするにはオーバーヘッドが大きいため、バッチ施策として一括消化する。

対象エントリ:
- BL-054: docs/workflow.md に initiative GHA ワークフロー記述がない
- BL-065: docs/workflow.md にリファレンススキル一覧セクションがない
- BL-077: バックログエントリ13件が旧フォーマットのまま残存
- BL-045: チェックリスト型スキルの標準テンプレートが未整備
- BL-060: Claude Code Action バージョン追跡手順が未制度化
- BL-083: refs/_knowledge_template.md にメタ情報セクションがない

## 目標
6件のバックログエントリを完了し、ドキュメント・テンプレートの網羅性と一貫性を向上させる。

## スコープ
### やること
- BL-054: docs/workflow.md に initiative GHA ワークフロー（wallbash/execute/close）記述を追加
- BL-065: docs/workflow.md にリファレンス系スキル（非起動型）一覧セクションを追加
- BL-077: 旧フォーマットのバックログエントリ（BL-036〜BL-047, BL-049）を現行テンプレート形式に変換
- BL-045: チェックリスト型スキルの標準テンプレートを .claude/templates/ に作成
- BL-060: Claude Code Action バージョン追跡手順を docs/ またはルールに制度化
- BL-083: refs/_knowledge_template.md にメタ情報セクション（用途・有効期限・取得日・取得方法）を追加

### やらないこと
- M/L 分類のバックログエントリの消化
- 外部リポジトリ（ai-driven-dev-patterns）への変更
- 既存ルール・スキルのロジック変更（テンプレート・ドキュメントの追記のみ）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## プロジェクト紐づけ

| プロジェクト名 | パス |
|-------------|------|
| backlog-batch-execution | projects/backlog-batch-execution |

## 期待される効果
- バックログ6件の消化（S分類残 35→29件）
- docs/workflow.md の網羅性向上（GHA ワークフロー・リファレンススキル）
- バックログエントリのフォーマット統一（機械的集計・BM走査が容易に）
- テンプレート整備による将来の作成効率向上

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| BL-077 対象ファイルの一部が既に削除済み | 低 | 実施時に現存確認し、存在するもののみ変換 |
| docs/workflow.md の変更が他セクションと不整合 | 低 | 変更後に全体の整合性を確認 |

## 壁打ちの背景
- BL-054 + BL-065 は M統合候補（docs/workflow.md 網羅性改善）としても計上されていたが、ユーザー指示によりバッチに含める方針に決定。plan.md の M統合候補は完了扱いとする
- BL-077 の対象13件の現存確認は L2 実施時に行う方針

## 備考・設計パターン
- BL-077 はフォーマット変換のため、format-conversion-checklist スキルの適用対象
- BL-054 + BL-065 は同一ファイル対象のため統合タスクとして実施

---
**起票者**: L1
**起票日**: 2026-03-25
**ステータス**: 実施中
**backlog元ファイル**: docs-workflow-initiative-gha-update.md, workflow-md-reference-skills-section.md, backlog-entries-format-unification.md, チェックリスト型スキルの標準テンプレート化.md, claude-code-action-version-tracking.md, refs-meta-info-template.md
