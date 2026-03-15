# 課題メモ（ワーカーセット別バッファ）: Set-3

> **このファイルの役割**: ワーカーセット内で発見された課題・知見・リスクの一時メモ置き場。
> マネージャーが `03_report.md` 作成時に全ワーカーセットの課題を集約し、`プロセス改善_課題管理.csv` へ転記する。

## 転記ルール

- ワーカー・評価者は課題をこのファイルに起票する（CSV 直接起票はしない）
- マネージャーが集約時に CSV 転記の要否を判断する
- 施策スコープ外・他のセッションでも再発しうる課題 → **マネージャーが CSV に転記**
- 当セッション内だけで完結する軽微な修正メモ → 転記不要（クローズ扱い）
- 転記済みの項目には `[転記済 ISS-XXX]` を末尾に追記する

---

## 未転記メモ

### [2026-03-15] BL-031 施策化済み未反映（3重未連携）
- **種別**: 不具合
- **発見者**: ワーカー
- **内容**: BL-031（automation-managerセッション作成）は initiatives/automation-manager-session として施策化済みだが、以下の3点が未連携:
  1. backlog.csv のステータスが「候補」のまま（「進行中」に未更新）
  2. backlog.csv の施策ディレクトリ名列が空欄
  3. 00_proposal.md の backlog元ファイルが「なし」と記載（実際は automation-managerセッション作成.md が対応）
- **対応方針（案）**: backlog.csv のステータスを「進行中」に更新、施策ディレクトリ名列に `automation-manager-session` を記入、proposal の backlog元ファイルを修正。根本対策として l1-manager の施策化フローに CSV 更新チェック項目を追加
- **関連タスク**: TG-002
- **既知情報**: Phase 1 Set-2 (TG-004) で BL-031 が候補ステータスのまま残存を確認済み

### [2026-03-15] entries ファイルの対象リポジトリ未記入（14件）
- **種別**: 改善提案
- **発見者**: ワーカー
- **内容**: backlog/entries/ 内の14件のファイルで「対象リポジトリ」フィールドが未記入。いずれも 2026-03-09〜03-12 の起票分に集中（BL-035〜BL-048）。CSV 列には全件記入済みのため運用上の実害は限定的だが、entries ファイルが正の情報源として機能するためには記入が望ましい。対象:
  - BL-035: role-format-guideのagents対応更新.md
  - BL-036: agentsの公式ディレクトリ分け.md
  - BL-037: ai-driven-dev-patterns-builtin-skills-eval.md
  - BL-038: entries-pattern-inbox適用検討.md
  - BL-039: メタ認知セット分割粒度・スキャンモード.md
  - BL-040: スキャンレポート変更理由記載ルール.md
  - BL-041: rules-skills移動時の波及更新パターン.md
  - BL-042: session-flow-checklist-precision.md
  - BL-043: triage-standard-policy適用マトリクス列数リスク.md
  - BL-044: user-invocable-false-description-pattern.md
  - BL-045: チェックリスト型スキルの標準テンプレート化.md
  - BL-046: 条件付き固定タスク配置ルール整備.md
  - BL-047: 費用対効果評価フレームワークの標準化.md
  - BL-048: triage-metacognitionテンプレート共通化検討.md
- **対応方針（案）**: トリアージのアクション実施フェーズで一括記入（CSV の値を転記）。根本対策として backlog テンプレートの対象リポジトリフィールドを必須化、または起票時チェックを追加
- **関連タスク**: TG-002
