# スキャンレポート: Set-3

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-002 | backlog 53件の施策化済みチェック・突合 | 完了 |

## TG-002: backlog 施策化済みチェック・突合

### 走査結果サマリ

- backlog.csv エントリ数: 53件
- backlog/entries/ ファイル数: 52件（BL-032 のファイルは削除済み）
- initiatives アクティブ: 10件 / アーカイブ: 74件
- 施策化済み検出: 3件（BL-020, BL-031, BL-032）
- 削除・クローズ候補: 2件（BL-031, BL-032）
- 対象リポジトリ未記入（entries ファイル内）: 14件
- 対象リポジトリ未記入（CSV列）: 0件

### 全53件の突合結果

| BL-ID | 施策名 | CSV ステータス | 施策化状況 | 照合方法 | 施策ディレクトリ | 備考 |
|-------|--------|:----------:|----------|---------|---------------|------|
| BL-001 | LLMローカル開発のセキュリティ強化 | 候補 | 未施策化 | - | - | |
| BL-002 | dev-workflow-detail L1参照精査 | 候補 | 未施策化 | - | - | |
| BL-003 | sessionsテンプレート間連携ガイド | 候補 | 未施策化 | - | - | |
| BL-004 | ハーネスエンジニアリング観点でのブラッシュアップ | 候補 | 未施策化 | - | - | |
| BL-005 | マルチAIエージェント共通ルール適用 | 候補 | 未施策化 | - | - | |
| BL-006 | 全ロールファイルrole-format-guide準拠確認修正 | 候補 | 未施策化 | - | - | |
| BL-007 | 北村さんの取り組みを取り込む | 候補 | 未施策化 | - | - | |
| BL-008 | 長文rulesのコンテキストコスト最適化 | 候補 | 未施策化 | - | - | |
| BL-009 | 高度な並列化と協調プロトコル統合 | 候補 | 未施策化 | - | - | |
| BL-010 | backlogテンプレート凡例強化 | 候補 | 未施策化 | - | - | |
| BL-011 | リンク整合性チェック標準化 | 候補 | 未施策化 | - | - | |
| BL-012 | 知見集約テーブル発見元列のinitiatives逆移植 | 候補 | 未施策化 | - | - | |
| BL-013 | Building-trust-through-layers活用検討 | 候補 | 未施策化 | - | - | |
| BL-014 | ディレクトリ構成最適化検討 | 候補 | 未施策化 | - | - | |
| BL-015 | ルートリポのトリアージにTG-008走査観点追加 | 候補 | 未施策化 | - | - | |
| BL-016 | l1-manager-checklist-reference | 候補 | 未施策化 | - | - | |
| BL-017 | 別リポジトリ成果物の記法スタイル事前確認 | 候補 | 未施策化 | - | - | |
| BL-018 | ai-driven-dev-patterns_source-of-truth明示 | 候補 | 未施策化 | - | - | |
| BL-019 | ai-driven-dev-patterns-triage-standard-policy作成 | 候補 | 未施策化 | - | - | |
| BL-020 | sync-worker同期先コミット漏れ防止 | 進行中 | **施策化済み（アクティブ）** | 直接照合 | sync-worker-target-commit | CSV施策ディレクトリ名記入済み。整合 |
| BL-021 | メタ認知セッションのai-driven-dev-patterns展開 | 候補 | 未施策化 | - | - | |
| BL-022 | denyリスト変更提案への副作用分析必須化 | 候補 | 未施策化 | - | - | |
| BL-023 | 社内施策_devkitスペシャリストロール作成 | 候補 | 未施策化 | - | - | |
| BL-024 | L2知見発見と修正適用のギャップ改善 | 候補 | 未施策化 | - | - | |
| BL-025 | agentsの管理方法のガイドライン追記 | 候補 | 未施策化 | - | - | |
| BL-026 | disallowedToolsフィールド活用検討 | 候補 | 未施策化 | - | - | |
| BL-027 | metacognition-managerの記述構造統一 | 候補 | 未施策化 | - | - | |
| BL-028 | ゲート判定基準での課題重大度の明文化 | 候補 | 未施策化 | - | - | |
| BL-029 | PreToolUse-hookコミットメッセージバリデーション | 候補 | 未施策化 | - | - | |
| BL-030 | PostToolUse-hookルール変更連動チェック | 候補 | 未施策化 | - | - | |
| BL-031 | automation-managerセッション作成 | 候補 | **施策化済み（アクティブ）** | 手動照合 | automation-manager-session | **不整合**: ステータスが「候補」のまま。施策ディレクトリ名列も空欄。proposal の backlog元ファイルも「なし」 |
| BL-032 | Claude Code標準plugin・skills情報整理 | 完了 | **施策化済み（アクティブ・ゲート通過）** | 直接照合 | claude-code-plugin-skills-survey | **不整合**: CSV行が残存。entries ファイルは削除済み。施策はゲート通過・クローズ済みだが _archive/ に未移動 |
| BL-033 | 施策間の競合防止方針策定 | 候補 | 未施策化 | - | - | |
| BL-034 | permission-prompt-optimization | 候補 | 未施策化 | - | - | |
| BL-035 | role-format-guideのagents対応更新 | 候補 | 未施策化 | - | - | |
| BL-036 | agentsの公式ディレクトリ分け | 候補 | 未施策化 | - | - | |
| BL-037 | ai-driven-dev-patterns-builtin-skills-eval | 候補 | 未施策化 | - | - | |
| BL-038 | entries-pattern-inbox適用検討 | 候補 | 未施策化 | - | - | |
| BL-039 | メタ認知セット分割粒度・スキャンモード | 候補 | 未施策化 | - | - | |
| BL-040 | スキャンレポート変更理由記載ルール | 候補 | 未施策化 | - | - | |
| BL-041 | rules-skills移動時の波及更新パターン | 候補 | 未施策化 | - | - | |
| BL-042 | session-flow-checklist精度向上 | 候補 | 未施策化 | - | - | |
| BL-043 | triage-standard-policy適用マトリクス列数リスク | 候補 | 未施策化 | - | - | |
| BL-044 | user-invocable-false-description-pattern | 候補 | 未施策化 | - | - | |
| BL-045 | チェックリスト型スキル標準テンプレート化 | 候補 | 未施策化 | - | - | |
| BL-046 | 条件付き固定タスク配置ルール整備 | 候補 | 未施策化 | - | - | |
| BL-047 | 費用対効果評価フレームワーク標準化 | 候補 | 未施策化 | - | - | |
| BL-048 | triage-metacognitionテンプレート共通化 | 候補 | 未施策化 | - | - | |
| BL-049 | トリアージアクション実施のサブエージェント委託 | 候補 | 未施策化 | - | - | |
| BL-050 | 外部リポジトリアーキテクチャオーバービュー管理 | 候補 | 未施策化 | - | - | |
| BL-051 | 同期対象リスト管理と差分ベース反映計画 | 候補 | 未施策化 | - | - | |
| BL-052 | backlog-maintenance-worker走査手順改善 | 候補 | 未施策化 | - | - | |
| BL-053 | L1マネージャー実作業禁止の構造的強制 | 候補 | 未施策化 | - | - | |

### 削除・クローズ候補リスト

| BL-ID | 施策名 | 推奨アクション | 理由 |
|-------|--------|-------------|------|
| BL-031 | automation-managerセッション作成 | CSVステータスを「進行中」に更新 + 施策ディレクトリ名列に `automation-manager-session` を記入 | 施策化済みだがCSVが「候補」のまま。施策ディレクトリ名列も空欄。proposal の backlog元ファイルも「なし」で突合リンクが未確立 |
| BL-032 | Claude Code標準plugin・skills情報整理 | CSV行を削除 + 施策を _archive/ に移動 | 施策完了（ゲート通過済み）。entries ファイルは既に削除済みだがCSV行が残存。施策ディレクトリも _archive/ に未移動 |

### 対象リポジトリ未記入リスト

CSV 列は全53件記入済み。以下は **backlog/entries/ ファイル内** の「対象リポジトリ」フィールドが未記入のエントリ。

| BL-ID | 施策名 | ファイル名 | CSV記載の対象リポジトリ |
|-------|--------|----------|:-------------------:|
| BL-032 | Claude Code標準plugin・skills情報整理 | (ファイルなし) | dev-process-improvement |
| BL-035 | role-format-guideのagents対応更新 | role-format-guideのagents対応更新.md | dev-process-improvement |
| BL-036 | agentsの公式ディレクトリ分け | agentsの公式ディレクトリ分け.md | dev-process-improvement |
| BL-037 | ai-driven-dev-patterns-builtin-skills-eval | ai-driven-dev-patterns-builtin-skills-eval.md | ai-driven-dev-patterns |
| BL-038 | entries-pattern-inbox適用検討 | entries-pattern-inbox適用検討.md | dev-process-improvement |
| BL-039 | メタ認知セット分割粒度・スキャンモード | メタ認知セット分割粒度・スキャンモード.md | dev-process-improvement |
| BL-040 | スキャンレポート変更理由記載ルール | スキャンレポート変更理由記載ルール.md | dev-process-improvement |
| BL-041 | rules-skills移動時の波及更新パターン | rules-skills移動時の波及更新パターン.md | dev-process-improvement |
| BL-042 | session-flow-checklist精度向上 | session-flow-checklist-precision.md | dev-process-improvement |
| BL-043 | triage-standard-policy適用マトリクス列数リスク | triage-standard-policy適用マトリクス列数リスク.md | dev-process-improvement |
| BL-044 | user-invocable-false-description-pattern | user-invocable-false-description-pattern.md | dev-process-improvement |
| BL-045 | チェックリスト型スキル標準テンプレート化 | チェックリスト型スキルの標準テンプレート化.md | dev-process-improvement |
| BL-046 | 条件付き固定タスク配置ルール整備 | 条件付き固定タスク配置ルール整備.md | dev-process-improvement |
| BL-047 | 費用対効果評価フレームワーク標準化 | 費用対効果評価フレームワークの標準化.md | dev-process-improvement |
| BL-048 | triage-metacognitionテンプレート共通化 | triage-metacognitionテンプレート共通化検討.md | dev-process-improvement |

**計15件**（BL-032 はファイルなしのため実質14件のファイルが対象リポジトリ未記入）

### ステータス不整合

| BL-ID | CSV ステータス | 実態 | 不整合の内容 |
|-------|:----------:|------|------------|
| BL-031 | 候補 | 施策化済み（initiatives/automation-manager-session にアクティブ施策あり） | ステータスが「候補」→「進行中」に更新されていない。施策ディレクトリ名列も空欄 |
| BL-032 | 完了 | 施策完了・ゲート通過済み | CSV行が残存（削除されていない）。施策ディレクトリが _archive/ に未移動。entries ファイルは削除済み |

### entries ファイル ↔ CSV 整合性

| 確認項目 | 結果 |
|---------|------|
| CSV にあるが entries にないファイル | 1件: BL-032（Claude Code標準plugin・skills情報整理.md） |
| entries にあるが CSV にない orphan ファイル | 0件 |

## 課題起票

- 起票件数: 2件（`07_issues.md` に起票済み）
- BL-031 の施策化済み未反映（ステータス・施策ディレクトリ名・proposal backlog元ファイルの3重未連携）
- entries ファイル内の対象リポジトリ未記入パターン（BL-035〜BL-048、2026-03-09〜03-12 起票分に集中）

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 施策化時の backlog.csv 更新チェックリスト不足 | l1-manager SKILL.md | L1 が施策化する際に backlog.csv のステータス更新・施策ディレクトリ名記入を必須化するチェック項目が必要。BL-031 のような「施策化したが CSV 未更新」パターンの再発防止 |
| 2 | entries ファイルの対象リポジトリ記入漏れ防止 | backlog テンプレート | BL-035〜BL-048 の14件で対象リポジトリが未記入。起票時のテンプレートバリデーションまたはトリアージ時の自動チェックが有効 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | BL-032 の施策ディレクトリが _archive/ に未移動 | 施策はゲート通過・クローズ済みだが sessions/initiatives/ にアクティブとして残存。initiative-close-procedure の _archive 移動ステップが実行されていない可能性 |
| 2 | 突合精度の構造的限界 | 施策ディレクトリ名列が空欄の場合、ファイル名→ディレクトリ名の照合は日本語→英語の変換があるため自動突合が困難。施策ディレクトリ名列の記入徹底が最も効果的な改善策 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
