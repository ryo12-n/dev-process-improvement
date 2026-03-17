# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 + TG-007 | inbox 17件の分類（気づきエントリ処理を統合） | 完了 |

## TG-001 + TG-007: inbox 17件の分類

### 分類結果サマリ

| 分類 | 件数 | 内訳 |
|------|------|------|
| backlog候補 | 10 | 新規施策化が必要なもの |
| 即時反映 | 4 | 軽微なルール修正・テーブル更新で対応可能なもの |
| 対応不要 | 3 | 既存 backlog で対応済み、または情報として記録済みのもの |
| 却下 | 0 | - |

### 分類詳細

| # | ファイル名 | 分類 | 対象リポジトリ | 理由・備考 |
|---|-----------|------|--------------|-----------|
| 1 | l1-direct-execution-bypasses-l2-flow.md | 対応不要 | dev-process-improvement | BL-053「L1マネージャー実作業禁止の構造的強制」が既に起票済み。本件は新たな発生事例（session-lifecycle-policy-rename 施策）の報告であり、BL-053 の補足・参考情報として追記するのが適切。別施策化は不要 |
| 2 | backlog-id-collision-prevention.md | backlog候補 | dev-process-improvement | 並列セッション環境での BL-076/077 二重採番の実例あり。ID 採番の排他制御・重複検知の仕組み構築が必要。重大度: 高 |
| 3 | subagent-commit-reliability.md | backlog候補 | dev-process-improvement | L2 サブエージェントのコミット・プッシュ失敗が常態化。L1 の補完作業がオーバーヘッドになっている。根本原因調査と改善策が必要。重大度: 高 |
| 4 | aidd-cross-session-knowledge-aggregation.md | backlog候補 | ai-driven-dev-patterns | ai-driven-dev-patterns にクロスセッション知識集約の仕組み（refs/ or knowledge/）を導入する施策候補。dev-process-improvement の知見モデルの横展開 |
| 5 | aidd-tool-policy-centralization.md | backlog候補 | ai-driven-dev-patterns | ai-driven-dev-patterns のツールポリシー集中管理。reviewer の tools/本文矛盾など具体的不整合あり |
| 6 | gha-multirepository-access-via-clone.md | backlog候補 | dev-process-improvement | GHA 環境での git clone によるマルチリポジトリアクセスのパターンをドキュメント化・テンプレート化する施策候補。ISS-027 への知見追記も含む |
| 7 | automation-candidates-sync-guideline.md | backlog候補 | dev-process-improvement | automation-candidates と backlog のステータス連動更新プロセスの明文化。初回自動化メンテナンスで乖離が判明 |
| 8 | session-definition-meta-template.md | backlog候補 | dev-process-improvement | 3フェーズ構成セッション定義のメタテンプレート（ジェネレータ）導入。session-consistency-manager で有効性が実証済み |
| 9 | skill-file-table-completeness-check.md | backlog候補 | dev-process-improvement | スキルファイル修正時の担当ファイルテーブル網羅性チェックを L1 タスク作成ガイドまたはテンプレートに追加する施策 |
| 10 | template-refactor-cross-reference-check.md | backlog候補 | dev-process-improvement | テンプレートリファクタ時のテンプレート内相互参照チェック（grep 対象拡張）をメタルール横断検証タスクに追加する施策 |
| 11 | refs-read-step-placement-pattern.md | backlog候補 | dev-process-improvement | refs 読み込みステップの標準配置パターン（マネージャー: タスク作成前、ワーカー: 壁打ち前）を rules/ に記載する施策候補 |
| 12 | triage-policy-section-consistency-check.md | 即時反映 | dev-process-improvement | session-flow-policy §5.1 チェックリストに §1.2/§1.3 列数一致確認を追加。修正範囲が明確で軽微 |
| 13 | triage-standard-policy-checklist-gap.md | 即時反映 | dev-process-improvement | session-flow-policy §5.1 チェックリストに triage-standard-policy §2.1/§1.2 連動更新を追加。修正範囲が明確で軽微 |
| 14 | l1-impl-common-policy-missing.md | 即時反映 | dev-process-improvement | manager-common-policy §1 テーブルに l1-impl-manager 行を追加、description「7つ」→「8つ」修正。修正範囲が明確で軽微 |
| 15 | table-footnote-consistency-check.md | 即時反映 | dev-process-improvement | テーブルセルと備考テキストの整合性確認をドキュメントタスク完了条件に含める。既存テンプレートへの1行追加レベル |
| 16 | knowledge-md-table-scalability.md | 対応不要 | dev-process-improvement | refs/agency-agents/knowledge.md のテーブル肥大化は現時点で8列。実際に可読性問題が顕在化した段階で対応すれば十分。現時点では予防的観測にとどまる |
| 17 | policy-subsection-numbering-rule.md | 対応不要 | dev-process-improvement | ポリシー文書のサブセクション番号付けルール。発生頻度が低く（§10.5 挿入時の1件）、個別対応で十分。ルール化のコスト対効果が合わない |

## 課題起票

- 起票件数: 0 件

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 即時反映4件のうち3件が session-flow-policy / manager-common-policy のチェックリスト・テーブル更新漏れ | `.claude/skills/session-flow-policy/`, `manager-common-policy` | 新セッションタイプ追加時の連動更新チェックリストの網羅性が課題。チェックリスト自体を自動検証する仕組みがあると再発防止になる |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | inbox 17件中10件が backlog 候補 — 施策実行中の知見発見が活発 | harness-engineering-brushup, l1-manager-enhanced-planning, session-consistency-manager 等の施策から多数の気づきが生まれている。プロセス改善サイクルが機能している証拠 |
| 2 | ai-driven-dev-patterns 向け施策が2件（#4, #5）。ローカル CLI 環境での実施が推奨される | 環境分離ポリシーに従い、backlog 起票時に対象リポジトリを明記すること |
| 3 | BL-053（L1実作業禁止）に新事例が追加された（#1）。施策化の優先度を上げる判断材料になる | session-lifecycle-policy-rename でも再発。ルール記載だけでは防止できないことが2例で実証された |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-17
