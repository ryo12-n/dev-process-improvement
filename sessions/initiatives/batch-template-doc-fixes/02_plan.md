# 実施計画: batch-template-doc-fixes

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | docs/workflow.md 拡充（BL-054 + BL-065 統合） | GHAワークフロー記述・リファレンススキル一覧が追加済み |
| 2 | バックログエントリ旧フォーマット統一（BL-077） | 対象エントリが現行テンプレート形式に変換済み |
| 3 | チェックリスト型スキルテンプレート作成（BL-045） | .claude/templates/ にテンプレートが存在 |
| 4 | Claude Code Action バージョン追跡手順（BL-060） | 手順文書が作成済み |
| 5 | refs メタ情報テンプレート標準化（BL-083） | refs/_knowledge_template.md にメタ情報セクションが追加済み |

## タスクグループ

### グループ A: docs/workflow.md 拡充（BL-054 + BL-065）
- docs/workflow.md に initiative GHA ワークフロー（wallbash/execute/close）記述を追加
- docs/workflow.md にリファレンス系スキル（非起動型: manager-common-policy, session-flow-policy, session-lifecycle-policy 等）一覧セクションを追加
- 対象ファイル: `docs/workflow.md`（1184行、可視化文書）
- 情報源: `.claude/skills/gha-wallbash/`, `.claude/skills/gha-execute/`, `.claude/skills/gha-close/` の各 SKILL.md

### グループ B: バックログエントリ旧フォーマット統一（BL-077）
- BL-036〜BL-047, BL-049 の13件を現行テンプレート（メタ情報テーブル形式）に変換
- 実施前に現存ファイルを確認し、既に削除されたものはスキップ
- format-conversion-checklist スキルを適用（同等性検証）
- 対象ファイル: `backlog/entries/` 内の13ファイル

### グループ C: チェックリスト型スキルテンプレート（BL-045）
- 既存チェックリスト型スキル（rule-change-checklist, format-conversion-checklist, repo-sync-checklist）の共通構成パターンを抽出
- `.claude/templates/checklist-skill-template.md` として標準テンプレートを作成
- 共通構成: frontmatter + 位置づけ説明 + チェックリスト本体 + 使い方 + 関連ファイル一覧

### グループ D: Claude Code Action バージョン追跡手順（BL-060）
- GHA ワークフローで使用する claude-code-action のバージョン追跡手順を文書化
- `docs/claude-code-action-version-tracking.md` として作成（運用ガイドカテゴリ）
- CLAUDE.md の docs/ ファイル分類テーブルに追加

### グループ E: refs メタ情報テンプレート標準化（BL-083）
- `refs/_knowledge_template.md` にメタ情報セクション（用途・有効期限・取得日・取得方法）を追加
- agency-agents-integration 施策で実践されたパターンを標準化
- CLAUDE.md 規定「参照物格納時は用途・有効期限のメタ情報を必ず記載すること」との整合確保

## 成功基準（全体）
1. 6件のバックログエントリすべてに対応する成果物が作成されている
2. docs/workflow.md の変更が既存セクションと整合している
3. バックログエントリの旧フォーマット13件が現行形式に変換されている（現存するもの）
4. 対応するバックログエントリファイルが git rm で削除されている

## リソース・前提条件
- SDK 環境（claude/l1-manager-fvWsq ブランチ）で実施
- 全対象ファイルが dev-process-improvement リポジトリ内で完結
- docs/workflow.md は可視化文書のため、スキル定義との整合性確認が必要

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| BL-077 対象ファイルの一部が削除済み | 中 | 低 | 現存確認して存在するもののみ変換 |
| docs/workflow.md の大幅変更による不整合 | 低 | 中 | 追加のみ行い既存セクションは変更しない |
| チェックリストテンプレートの設計判断 | 低 | 低 | 既存3スキルの共通パターン抽出に徹する |

---
**作成者**: L1
**作成日**: 2026-03-25
**最終更新**: 2026-03-25
