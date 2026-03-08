# 作業レポート: roles/ → .claude/agents/ 移行

## サマリ

ai-driven-dev-patterns リポジトリの `roles/` ディレクトリを廃止し、Claude Code ネイティブの `.claude/agents/` + `.claude/skills/` + `.claude/rules/` 構成への移行を完了した。8つの専門ロールをエージェント形式に変換し、共通ルールを3つのルールファイルに分離し、dev_manager を dispatcher スキルに統合し、約40ファイルの参照パスを更新した。全タスク（T-001〜T-008）完了。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | common.md の共通ルール分離 + commit-message.md 統合 | 3ルールファイル作成 | 3ファイル作成 + commit-message.md 統合 | 計画通り |
| T-002 | 8つの専門ロールを .claude/agents/ に変換 | 8ファイル作成 | 8ファイル作成 | ファイル名を `_` → `-` ケバブケースに変換 |
| T-003 | dev_manager を dispatcher に統合 | SKILL.md 更新 | SKILL.md を2パート構成に再構成 | 計画通り |
| T-004 | 参照パス更新 | 約40ファイル | 約40ファイル | 計画通り。docs/design/ は歴史的記録として保持 |
| T-005 | roles/ 削除 | git rm -r | 10ファイル削除 | 計画通り |
| T-006 | 知見記録 | 本レポートに記録 | 下記「作業中の知見」に記載 | 計画通り |
| T-007 | 連動更新チェックリスト | 全項目確認 | 全項目確認済み（03_work_log.md に記録） | 計画通り |
| T-008 | 課題転記確認 | 07_issues.md 確認 | 起票なし（施策横断課題の発見なし） | 転記不要 |

## 成果物一覧

### ai-driven-dev-patterns 側（ブランチ: initiative/roles-agents-migration）

**新規作成**:
- `.claude/rules/agent-common-workflow.md` — エージェント共通作業フロー（common.md セクション3, 6, 7 + エラー対応）
- `.claude/rules/agent-restrictions.md` — エージェント共通禁止事項（common.md セクション4）
- `.claude/rules/worktree-rules.md` — worktree 環境での共通ルール（common.md セクション8）
- `.claude/agents/feature-builder.md` — 機能実装担当エージェント
- `.claude/agents/test-writer.md` — テスト整備担当エージェント
- `.claude/agents/reviewer.md` — レビュー担当エージェント（tools: Read, Grep, Glob, Bash のみ）
- `.claude/agents/bug-fixer.md` — バグ修正担当エージェント
- `.claude/agents/refactorer.md` — リファクタリング担当エージェント
- `.claude/agents/optimizer.md` — 最適化担当エージェント
- `.claude/agents/documentarian.md` — ドキュメント整備担当エージェント
- `.claude/agents/openspec-specialist.md` — OpenSpec ライフサイクル管理担当エージェント

**更新**:
- `.claude/rules/commit-message.md` — コミット規約を自己完結型に統合
- `.claude/skills/dispatcher/SKILL.md` — dev_manager のオーケストレーションロジックを統合
- 約30ファイルの参照パス更新（CLAUDE.md, README.md, docs/, .claude/skills/, sessions/, triage/, backlog/, inbox/）

**削除**:
- `roles/` ディレクトリ全体（10ファイル）

### dev-process-improvement 側

- `sessions/initiatives/roles-agents-migration/03_work_log.md` — 作業履歴
- `sessions/initiatives/roles-agents-migration/04_work_report.md` — 本レポート

## 発生した課題

なし（07_issues.md への起票なし）

## 作業中の知見

### ルール化候補（.claude/rules/ や .claude/agents/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | エージェント名のケバブケース規則の明文化 | `.claude/skills/role-format-guide/SKILL.md` | Claude Code agents は YAML の `name` フィールドが小文字・ハイフンのみを許容する。ファイル名もケバブケースに統一すべき（`feature_builder` → `feature-builder`）。role-format-guide にこの命名規則を明記することで、新規エージェント作成時の迷いを防止できる |
| 2 | ルール分離時のテーマ別分割パターン | `.claude/rules/` | common.md のような大規模な共通ルールを `.claude/rules/` に移行する際、「作業フロー」「禁止事項」「環境固有ルール」のテーマ別に分割するとメンテナンス性が高い。1ファイル1テーマの原則をルール化候補として検討 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | roles/ → agents/ の一括移行は中間状態のリスクが高いため一括実施が正解だった | 参照箇所が約40ファイル・136箇所あり、段階的移行だと二重管理が発生する。一括移行で整合性を担保できた。同規模の構造変更では一括移行を選択すべき |
| 2 | docs/design/ 配下の歴史的設計書は更新不要とする判断が適切 | 設計書は「設計時点の記録」として価値があり、現在の構成に追従させると設計の意図が不明瞭になる。将来の参照時に混乱を避けるため、歴史的記録は「当時の記述をそのまま残す」方針が有効 |

## 所感・次フェーズへの申し送り

- 移行は計画通り完了。`grep -r 'roles/' --include='*.md'` で docs/design/ 以外にヒットなしを確認済み
- reviewer のツール制限（Read, Grep, Glob, Bash のみ）が仕組みレベルで強制されるようになった点は品質面で改善
- triage テンプレートの `.claude/rules/*.md ↔ roles/*.md` 整合性チェック項目は `.claude/rules/*.md ↔ .claude/agents/*.md` に更新済み
- 次フェーズ（L2-evaluator）での検証ポイント: (1) agents 形式の YAML バリデーション (2) dispatcher 統合の機能網羅性 (3) 参照パスの残存チェック

---
**作成者**: L2（実施）
**作成日**: 2026-03-08
