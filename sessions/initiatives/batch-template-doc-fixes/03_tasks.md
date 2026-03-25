# タスクリスト: batch-template-doc-fixes

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 全タスクがドキュメント・テンプレート整備のため特定ドメイン知識不要 | Worker |
| なし | - | 同上 | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-009 | 逐次実施 |
| L2-evaluator | 全タスクの評価 | worker 完了後 |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-009 | Wave 1（逐次） |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | 1ワーカーで全タスク実行 |

> **方式**: 逐次（1ワーカーずつ） / 並列（Wave 方式、`.claude/rules/parallel-dev.md` 参照）

## タスク一覧

### Wave 1: 実施タスク（T-001〜T-006）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | **docs/workflow.md 拡充（BL-054 + BL-065 統合）**: (1) BL-054: docs/workflow.md の「GHA Initiative スキル」セクション（L482付近）を確認し、wallbash/execute/close の記述が不足していれば補完する。既に充足していれば「既に解決済み」として作業ログに記録しスキップ。(2) BL-065: 「リファレンス系スキル一覧」セクションを新設し、全 `user-invocable: false` スキル（ポリシー系・チェックリスト系・リファレンス系・ユーティリティ系・GHA専用）を一覧化する | (1) BL-054 について既存セクションの確認結果が作業ログに記録されている (2) 「リファレンス系スキル一覧」セクションが追加され、全非起動型スキルが網羅されている (3) 既存セクションとの整合性が保たれている | 🔴 | ⬜ |
| T-002 | **バックログエントリ旧フォーマット統一（BL-077）**: `backlog/entries/` 内の BL-036〜BL-046, BL-049 の12件（BL-047 欠番）を現行テンプレート形式に変換する。不足フィールド（`依存する環境前提`）・セクション（`起票時チェックリスト`、`関連エントリ`）を補完する。`.claude/skills/format-conversion-checklist/SKILL.md` を参照して同等性検証を実施し、検証記録を作業ログに記載する | (1) 現存する全対象ファイルが現行テンプレート形式に変換されている (2) format-conversion-checklist に従い同等性検証が完了し、検証記録が作業ログにある (3) BL-047 欠番の旨が作業ログに記録されている | 🔴 | ⬜ |
| T-003 | **チェックリスト型スキルテンプレート作成（BL-045）**: 既存3スキル（rule-change-checklist, format-conversion-checklist, repo-sync-checklist）の共通構成パターンを抽出し、`.claude/templates/checklist-skill-template.md` を作成する | (1) `.claude/templates/checklist-skill-template.md` が作成されている (2) 共通構成パターン（frontmatter + 位置づけ説明 + チェックリスト本体 + 使い方 + 関連ファイル一覧）がテンプレート化されている (3) プレースホルダーが含まれている | 🟡 | ⬜ |
| T-004 | **Claude Code Action バージョン追跡手順作成（BL-060）**: (1) `docs/claude-code-action-version-tracking.md` を運用ガイドとして作成する。バージョン確認方法・更新手順・影響範囲の確認観点を記載する (2) `CLAUDE.md` の docs/ ファイル分類テーブルに行を追加する | (1) `docs/claude-code-action-version-tracking.md` が作成されている (2) CLAUDE.md の docs/ ファイル分類テーブルに当該ファイルが運用ガイドとして追加されている (3) `.github/workflows/` 内の現在のバージョン指定が確認・記載されている | 🟡 | ⬜ |
| T-005 | **refs メタ情報テンプレート標準化（BL-083）**: `refs/_knowledge_template.md` にメタ情報セクション（用途・有効期限・取得日・取得方法）を追加する。`refs/agency-agents/knowledge.md` の実践済みパターンを参考にする | (1) `refs/_knowledge_template.md` にメタ情報セクションが追加されている (2) 4フィールド（用途・有効期限・取得日・取得方法）がテンプレートに含まれている (3) CLAUDE.md 規定との整合が確保されている | 🟡 | ⬜ |
| T-006 | **バックログエントリ削除・CSV ステータス更新**: (1) 6件のバックログエントリファイル（BL-054/065/077/045/060/083）を `git rm` で削除する (2) `backlog/backlog.csv` の該当6行のステータスを「完了」に更新し、施策ディレクトリ名に `batch-template-doc-fixes` を記入する | (1) 6件のファイルが `git rm` で削除されている (2) backlog.csv の該当行が更新されている | 🔴 | ⬜ |

### 固定タスク: 知見記録・課題転記（T-007〜T-009）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-007 | **知見記録（実施ワーカー）**: 作業中に発見した知見を `phase-2-execution/set-1/03_worker_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-008 | **課題転記（実施ワーカー）**: `phase-2-execution/set-1/07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` に作成する。転記時は `issues/_template.md` をコピーして作成する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |
| T-009 | **プロジェクト紐づけ更新（実施ワーカー）**: 施策クローズ時に以下を更新する: (1) `projects/backlog-batch-execution/todo.md` の #3 のステータスを `完了` に更新 (2) 施策レポートから知見を抽出し `projects/backlog-batch-execution/work_log.md` に追記（knowledge.md がないため work_log に記録） (3) `projects/backlog-batch-execution/plan.md` の施策一覧テーブル #3 のステータスを更新 | (1) todo.md のステータスが更新済み (2) work_log.md に知見が追記済み (3) plan.md のステータスが更新済み。適用対象環境: SDK | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-25
