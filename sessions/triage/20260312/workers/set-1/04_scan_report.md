# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox 全24件の分類 | 完了 |
| TG-INT | ルール・整合性チェック4項目 | 完了 |
| TG-009 | 情報欠損リスク評価 | 完了 |

---

## TG-001: inbox 分類

### 分類結果サマリ

| 分類 | 件数 |
|------|------|
| backlog候補 | 10 |
| ルール反映 | 0 |
| 対応不要（継続保持） | 4 |
| 対応不要（削除候補: backlog/CSV 重複） | 5 |
| 対応不要（削除候補: ISS 転記済みのため不要） | 4 |
| 却下 | 1 |
| **合計** | **24** |

### inbox 分類詳細

| # | ファイル名 | 分類 | 判断理由 | backlog重複 | ISS関連 |
|---|-----------|------|---------|:-----------:|:-------:|
| 1 | agentsの公式ディレクトリ分け.md | backlog候補 | claude-directory-guide の移植・agents チェック専門化の提案。具体的な作業内容あり | なし | - |
| 2 | ai-driven-dev-patterns-builtin-skills-eval.md | backlog候補 | builtin-skills-evaluation の横展開提案。コード主体リポでの評価は有益 | なし | - |
| 3 | entries-pattern-inbox適用検討.md | backlog候補 | inbox/ への entries/ パターン適用検討。現時点では不急だが施策候補として蓄積 | なし | - |
| 4 | meta_csv-status-update-mechanism.md | 対応不要（削除候補） | ISS-055 として CSV 転記済み。inbox に残す意味なし | - | ISS-055 |
| 5 | meta_knowledge-routing-iss-id.md | 対応不要（削除候補） | ISS-053 として CSV 転記済み。inbox に残す意味なし | - | ISS-053 |
| 6 | meta_routing-execution-verification.md | 対応不要（削除候補） | ISS-052 として CSV 転記済み。inbox に残す意味なし | - | ISS-052 |
| 7 | meta_rule-change-checklist-docs-scope.md | 対応不要（削除候補） | ISS-054 として CSV 転記済み。inbox に残す意味なし | - | ISS-054 |
| 8 | meta_scan-mode-and-set-granularity.md | backlog候補 | メタ認知のセット分割粒度とフル/差分スキャン選択。独立した改善提案で ISS 非該当 | なし | - |
| 9 | meta_scan-report-change-reason.md | backlog候補 | scan_report 内の走査対象変更理由記載ルール。独立した改善提案で ISS 非該当 | なし | - |
| 10 | ref_ai-driven-development-poc.md | 対応不要（継続保持） | refs/ ポインターメモ。参照のみ保持方針 | - | - |
| 11 | ref_ai-functions.md | 対応不要（継続保持） | refs/ ポインターメモ。参照のみ保持方針 | - | - |
| 12 | ref_openspec-official-summary.md | 対応不要（継続保持） | refs/ ポインターメモ。参照のみ保持方針 | - | - |
| 13 | ref_個人PCローカル環境構築-手順書.md | 対応不要（継続保持） | refs/ ポインターメモ。参照のみ保持方針 | - | - |
| 14 | rules-skills移動時の波及更新パターン.md | backlog候補 | 全スキルへの「関連ファイル一覧」セクション義務化の提案。具体的で施策化可能 | なし | - |
| 15 | session-flow-checklist-precision.md | backlog候補 | session-flow-policy §5.1 チェックリスト精度向上。triage-standard-policy 更新箇所の追加提案 | なし | - |
| 16 | sync-worker同期先コミット漏れ防止.md | 対応不要（削除候補） | backlog/entries/ に同名ファイルが既存。backlog.csv にも登録済み（中優先度、候補ステータス）。inbox 側は重複 | あり | - |
| 17 | triage-metacognition テンプレート共通化検討.md | backlog候補 | テンプレート共通化提案。次セッションタイプ追加時に再検討推奨 | なし | - |
| 18 | triage-standard-policy-table-width.md | backlog候補 | 適用マトリクス列数増加リスク。#24（適用マトリクス列数増加リスク.md）と同一テーマ | あり（統合候補） | - |
| 19 | user-invocable-false-description-pattern.md | backlog候補 | user-invocable: false スキルの description 設計パターン。事例蓄積後にルール化検討 | なし | - |
| 20 | チェックリスト型スキルの標準テンプレート化.md | backlog候補 | チェックリスト型スキルのテンプレート化提案。施策化 or session-flow-policy 統合 | なし | - |
| 21 | 条件付き固定タスク適用条件パスパターン重複.md | 却下 | パスパターンの一元定義は2箇所のみで管理コスト低。現時点では過剰設計 | - | - |
| 22 | 条件付き固定タスク配置ルール整備.md | backlog候補 | 条件付きタスクの視覚的区別。軽微だがサブヘッダ分類の提案は実用的 | なし | - |
| 23 | 費用対効果評価フレームワークの標準化.md | backlog候補 | 費用対効果フレームワークのテンプレート化。汎用性あり | なし | - |
| 24 | 適用マトリクス列数増加リスク.md | 対応不要（削除候補） | #18（triage-standard-policy-table-width.md）と同一テーマ。統合して1件にすべき | 統合候補 | - |

### 重複・統合候補

| # | ファイル1 | ファイル2 | 関係 | 推奨アクション |
|---|----------|----------|------|-------------|
| 1 | inbox/sync-worker同期先コミット漏れ防止.md | backlog/entries/sync-worker同期先コミット漏れ防止.md | 完全重複（backlog化済み） | inbox 側を削除 |
| 2 | inbox/triage-standard-policy-table-width.md | inbox/適用マトリクス列数増加リスク.md | 同一テーマ（異なる施策から起票） | 統合して1件のbacklog候補に |

---

## TG-INT: ルール・整合性チェック

### (1) .claude/skills/ vs docs/workflow.md 整合性

| # | チェック項目 | 結果 | 備考 |
|---|------------|:----:|------|
| 1 | l1-manager フロー | OK | workflow.md に正確に反映 |
| 2 | triage-manager フロー | OK | TG タスク一覧・走査手順が一致 |
| 3 | metacognition-manager フロー | OK | MC タスク一覧が一致 |
| 4 | sync-manager フロー | OK | ファイルオーナーシップテーブルが一致 |
| 5 | backlog-maintenance-manager フロー | OK | BM タスク一覧が一致 |
| 6 | builtin-skills-reference（新規追加、非起動型） | OK | workflow.md に「ビルトイン Skills 評価リファレンス」セクションとして反映済み |
| 7 | manager-common-policy | OK | workflow.md に「マネージャーセッション共通ポリシー」セクションとして反映済み |
| 8 | format-conversion-checklist | OK | workflow.md に「フォーマット変換時の同等性検証」セクションとして反映済み |
| 9 | rule-change-checklist | OK | workflow.md に「ルール変更時の連動更新」セクションとして反映済み |
| 10 | session-flow-policy / triage-standard-policy | OK | workflow.md のポリシー3層構造で参照 |

**総合判定**: 乖離なし。workflow.md は skills 定義と整合している。

### (2) README.md 4セクション整合性

| # | セクション | 結果 | 不整合の内容 |
|---|-----------|:----:|------------|
| 1 | ディレクトリ構成図 | NG | backlog-maintenance-manager が .claude/skills/ ツリーに未記載。sessions/backlog-maintenance/ が sessions/ ツリーに未記載。docs/ 配下に management-system-guide.md, subagent-permission-guide.md が未記載。non-user-invocable スキル（builtin-skills-reference, external-repo-cleanup, format-conversion-checklist, manager-common-policy, repo-sync-checklist, rule-change-checklist, session-flow-policy, triage-standard-policy）が未記載だが、README では「起動型のみ記載」と明記されているため、これらは問題なし。ただし fork-sync（user-invocable: true）も未記載 |
| 2 | セッション種別テーブル | NG | backlog-maintenance-manager が未記載（4種のみ、5種あるべき） |
| 3 | AI向けスキル定義テーブル | NG | backlog-maintenance-manager が未記載（4行のみ、5行あるべき） |
| 4 | ドキュメントマップ | NG | 人間向けドキュメントテーブルに docs/management-system-guide.md, docs/subagent-permission-guide.md, docs/coordination-protocol-guideline.md, docs/git-worktree-guideline.md が未記載 |

**総合判定**: README.md に backlog-maintenance-manager 施策の連動更新が漏れている。docs/ ファイルの一部もドキュメントマップに反映されていない。

### (3) 参考資料（ドラフト）ステータスチェック

| ファイル | バナー有無 | 統合状況 | 実態との矛盾 | 備考 |
|---------|:---------:|---------|:----------:|------|
| docs/coordination-protocol-guideline.md | OK | 一部統合済み（セクション2.2 → .claude/rules/commit-message.md） | なし | commit-message.md は実在 |
| docs/git-worktree-guideline.md | OK | 未着手 | なし | .claude/skills/ に worktree 関連なし |

#### docs/ 分類テーブル網羅性

| ファイル | CLAUDE.md テーブル記載 | 備考 |
|---------|:-------------------:|------|
| docs/workflow.md | あり | 可視化文書 |
| docs/management-system-guide.md | あり | 運用ガイド |
| docs/subagent-permission-guide.md | あり | 運用ガイド |
| docs/implementation.md | あり | 運用ガイド |
| docs/coordination-protocol-guideline.md | あり | 参考資料（ドラフト） |
| docs/git-worktree-guideline.md | あり | 参考資料（ドラフト） |

**総合判定**: 参考資料ステータスに問題なし。CLAUDE.md テーブルの網羅性も問題なし。

### (4) refs/ 孤立エントリ確認

| refs/ エントリ | 対応する inbox/ref_*.md | 状態 |
|---------------|----------------------|------|
| refs/ai-driven-development-poc/ | inbox/ref_ai-driven-development-poc.md | OK |
| refs/ai-functions/ | inbox/ref_ai-functions.md | OK |
| refs/openspec-official-summary.md | inbox/ref_openspec-official-summary.md | OK |
| refs/個人PCローカル環境構築-手順書.md | inbox/ref_個人PCローカル環境構築-手順書.md | OK |

**総合判定**: 孤立エントリなし。

---

## TG-009: 情報欠損リスク評価

### 走査結果サマリ
- 評価対象ファイル数: 6件（削除候補: 5件 / 統合候補: 1件）
- リスク「高」: 0件 / リスク「中」: 0件 / リスク「低」: 6件

### リスク評価テーブル

| ファイル名 | 種別 | 含有知見数 | 参照リンク数 | 消失リスク | 推奨アクション |
|-----------|------|----------|------------|----------|-------------|
| inbox/sync-worker同期先コミット漏れ防止.md | 削除 | 0（backlog に全情報あり） | 0 | 低 | そのまま削除 |
| inbox/meta_csv-status-update-mechanism.md | 削除 | 0（ISS-055 に転記済み） | 1（ISS-055） | 低 | そのまま削除 |
| inbox/meta_knowledge-routing-iss-id.md | 削除 | 0（ISS-053 に転記済み） | 1（ISS-053） | 低 | そのまま削除 |
| inbox/meta_routing-execution-verification.md | 削除 | 0（ISS-052 に転記済み） | 1（ISS-052） | 低 | そのまま削除 |
| inbox/meta_rule-change-checklist-docs-scope.md | 削除 | 0（ISS-054 に転記済み） | 1（ISS-054） | 低 | そのまま削除 |
| inbox/適用マトリクス列数増加リスク.md | 統合 | 1（triage-standard-policy-table-width.md と同一テーマ） | 0 | 低 | 統合（情報は triage-standard-policy-table-width.md に包含） |

---

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票済み）
- README.md の backlog-maintenance-manager 連動更新漏れ（07_issues.md に起票済み）

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | README.md の連動更新が session-flow-policy や rule-change-checklist の走査対象に含まれていない | README.md / session-flow-policy | 新セッションタイプ追加時に README の4セクション更新が漏れる構造的な問題。session-flow-policy §5.1 のチェックリストまたは rule-change-checklist に README.md を追加すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | meta_* inbox エントリは ISS 転記済みかどうかで扱いが二分される | ISS 転記済み4件は削除可能、未転記2件は独立した backlog 候補。メタ認知セッションの気づき出力が inbox と ISS の両方に転記される場合、inbox 側は削除タイミングを明確にすべき |
| 2 | inbox/ref_* は4件とも「参照のみ保持」方針で安定している | 前回トリアージからの変化なし。将来的に施策化されるまで inbox に残し続ける形になるが、inbox の件数増加には注意 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-12
