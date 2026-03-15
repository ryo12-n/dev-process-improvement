# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox 23件の分類 | 完了 |

## TG-001: inbox 23件の分類

### 分類サマリ

| 分類 | 件数 |
|------|------|
| backlog候補 | 11件 |
| ルール反映 | 8件 |
| 対応不要 | 2件 |
| 重複（既存BL吸収） | 2件 |
| 却下 | 0件 |

### 分類結果一覧

| # | ファイル名 | 分類 | 重複BL | 判断根拠 |
|---|-----------|------|--------|---------|
| 1 | automation-manager-common-policy-addition.md | ルール反映 | BL-031関連だが別件 | manager-common-policy §1 への1行追加。施策不要で直接反映可能 |
| 2 | automation-session-flow-policy-addition.md | ルール反映 | BL-042関連だが別件 | session-flow-policy §5 への1行追加。施策不要で直接反映可能 |
| 3 | claude-code-action-version-tracking.md | backlog候補 | なし | バージョン追従手順の制度化。定期チェックの仕組み化が必要で施策規模 |
| 4 | conditional-checklist-pattern.md | 対応不要 | BL-045で参照可能 | 設計パターンの知見記録。独立施策の必要なく、BL-045検討時に自然に参照される |
| 5 | docs-workflow-initiative-gha-update.md | backlog候補 | なし | docs/workflow.md への記述追加。複数セクションの追記が必要で施策規模 |
| 6 | gha-backlog-maintenance-automation.md | backlog候補 | なし | GHA 自動化の横展開（バックログメンテナンス）。新ワークフロー作成が必要 |
| 7 | gha-guideline-other-workflows.md | backlog候補 | なし | 他ワークフローへの権限3層モデル適用。複数ファイルのレビュー・修正が必要 |
| 8 | gha-metacognition-automation.md | backlog候補 | なし | GHA 自動化の横展開（メタ認知）。新ワークフロー作成が必要 |
| 9 | gha-prompt-shell-expansion-caveat.md | ルール反映 | なし | gha-guideline SKILL.md への注意事項追記。限定的な追記で直接反映可能 |
| 10 | gha-session-prompt-conversion-pattern.md | backlog候補 | なし | 変換パターンのガイドライン化。refs/ へのナレッジ蓄積または gha-guideline への統合 |
| 11 | gha-workflow-security-checklist.md | ルール反映 | なし | GHA セキュリティチェックリストの .claude/rules/ への追加。ISS-058 関連で具体的 |
| 12 | git-rebase-conflict-handling-guideline.md | ルール反映 | なし | rebase コンフリクト対応フローの .claude/rules/ への追加。具体的な手順が記載済み |
| 13 | l1-pre-applied-template-task-design.md | backlog候補 | なし | L1 タスク設計の改善。l1-manager スキルへの反映が必要で検討規模 |
| 14 | l1-skill-file-enumeration-check.md | ルール反映 | なし | L1 タスク作成ガイドへの検索ステップ追加。具体的で限定的な追記 |
| 15 | plugin-high-applicability-trial.md | backlog候補 | BL-032の後続 | 4プラグインの導入検証。BL-032完了の後続施策として新規起票が適切 |
| 16 | reference-doc-granularity-rule.md | backlog候補 | なし | リファレンス文書の粒度基準ルール化。L2-worker テンプレートへの組み込み |
| 17 | refs-metadata-requirement.md | ルール反映 | なし | refs/ 参照物のメタ情報必須化。CLAUDE.md の refs/ 説明への追記で対応可能 |
| 18 | refs-routing-template-unification.md | backlog候補 | なし | 全セッションテンプレートのルーティング先統一。複数テンプレートの更新が必要で施策規模 |
| 19 | session-flow-policy-checklist-improvement.md | 重複（既存BL吸収） | BL-042 | BL-042（session-flow-checklist精度向上）の具体的な1項目。BL-042 に吸収推奨 |
| 20 | skill-plugin-overlap-check-rule.md | backlog候補 | なし | スキル/プラグイン機能重複の定期チェック制度化 |
| 21 | sync-checklist-source-term-grep.md | ルール反映 | なし | repo-sync-checklist へのソース固有用語チェックステップ追加。具体的な追記 |
| 22 | workflow-md-reference-skills-section.md | backlog候補 | なし | docs/workflow.md にリファレンススキル一覧セクション追加 |
| 23 | 実装ワーカーの作業ログclaude-context-detailed-doc.md | 対応不要 | なし | 外部リポジトリ（newproduct-registry）のツール詳細文書。本リポジトリの施策・ルール対象外。refs/ 格納が適切だった可能性あり |

### backlog候補の詳細（11件）

| # | ファイル名 | 提案する施策名 | 優先度案 | 対象リポジトリ |
|---|-----------|-------------|---------|-------------|
| 3 | claude-code-action-version-tracking.md | claude-code-action-version-tracking | 低 | dev-process-improvement |
| 5 | docs-workflow-initiative-gha-update.md | docs-workflow-initiative-gha-update | 中 | dev-process-improvement |
| 6 | gha-backlog-maintenance-automation.md | gha-backlog-maintenance-automation | 中 | dev-process-improvement |
| 7 | gha-guideline-other-workflows.md | gha-guideline-other-workflows | 中 | dev-process-improvement |
| 8 | gha-metacognition-automation.md | gha-metacognition-automation | 中 | dev-process-improvement |
| 10 | gha-session-prompt-conversion-pattern.md | gha-session-prompt-conversion-pattern | 低 | dev-process-improvement |
| 13 | l1-pre-applied-template-task-design.md | l1-pre-applied-template-task-design | 低 | dev-process-improvement |
| 15 | plugin-high-applicability-trial.md | plugin-high-applicability-trial | 中 | dev-process-improvement |
| 16 | reference-doc-granularity-rule.md | reference-doc-granularity-rule | 低 | dev-process-improvement |
| 18 | refs-routing-template-unification.md | refs-routing-template-unification | 中 | dev-process-improvement |
| 20 | skill-plugin-overlap-check-rule.md | skill-plugin-overlap-check-rule | 低 | dev-process-improvement |
| 22 | workflow-md-reference-skills-section.md | workflow-md-reference-skills-section | 低 | dev-process-improvement |

### ルール反映の詳細（8件）

| # | ファイル名 | 反映先 | 反映内容 |
|---|-----------|--------|---------|
| 1 | automation-manager-common-policy-addition.md | .claude/skills/manager-common-policy/SKILL.md §1 | automation-manager 行追加 |
| 2 | automation-session-flow-policy-addition.md | .claude/skills/session-flow-policy/SKILL.md §5 | automation-manager 行追加 |
| 9 | gha-prompt-shell-expansion-caveat.md | .claude/skills/gha-guideline/SKILL.md | prompt: フィールドのシェル展開不可、issue_comment の PR コメント発火の注意事項追記 |
| 11 | gha-workflow-security-checklist.md | .claude/rules/ (新規) | GHA ワークフロー作成時のセキュリティチェックリスト |
| 12 | git-rebase-conflict-handling-guideline.md | .claude/rules/ (新規) | rebase コンフリクト時の対応フロー（4ステップ） |
| 14 | l1-skill-file-enumeration-check.md | .claude/skills/l1-manager/ タスク作成ガイド | 対象スキルファイル列挙時の grep 網羅検索ステップ |
| 17 | refs-metadata-requirement.md | CLAUDE.md の refs/ セクション | 参照物格納時のメタ情報（用途・有効期限）記載の必須化 |
| 21 | sync-checklist-source-term-grep.md | repo-sync-checklist | ソース固有用語リスト定義と grep チェックステップ追加 |

### 重複（既存BL吸収）の詳細（2件）

| # | ファイル名 | 吸収先BL | 理由 |
|---|-----------|---------|------|
| 4 | conditional-checklist-pattern.md | BL-045 | BL-045（チェックリスト型スキル標準テンプレート化）検討時に参照される設計パターン知見。独立施策不要 |
| 19 | session-flow-policy-checklist-improvement.md | BL-042 | BL-042（session-flow-checklist精度向上）のスコープに含まれる具体的1項目（manager-common-policy §1 追加） |

### 対応不要の詳細（2件）

| # | ファイル名 | 理由 |
|---|-----------|------|
| 4 | conditional-checklist-pattern.md | 設計知見の記録。BL-045 の検討時に参照可能であり、独立した施策・ルール化の必要なし |
| 23 | 実装ワーカーの作業ログclaude-context-detailed-doc.md | 外部リポジトリ（newproduct-registry）の実装詳細文書。本リポジトリの改善施策・ルールの対象外 |

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票済み）
- inbox に外部リポジトリの詳細文書が混入（#23）：inbox と refs の使い分けルール周知の課題

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | ゲートレビューからの知見ルーティングが大量に発生する場合、ルール反映系（小規模変更）は施策化せずトリアージアクションで直接反映する運用が効率的 | トリアージフロー | 8件がルール反映分類。これらを個別施策化すると管理オーバーヘッドが大きい |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | GHA 自動化関連の inbox が集中（#3,5,6,7,8,9,10,11 の8件） | gha-triage-automation、gha-initiative-workflow、backlog-auto-initiative-gha、gha-claude-code-guidelines の各施策完了に伴う横展開提案が一斉に流入。GHA 自動化を包括的に計画する施策が有効かもしれない |
| 2 | #23 は inbox ではなく refs/ に格納されるべきだった | CLAUDE.md に「参照物 → refs/ に本体、inbox/ にポインターメモ」とあるが、実体文書が直接 inbox に置かれている。ルーティング元（L2-worker）での判断ミスか、ルール周知不足の可能性 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
