# トリアージ振り返りレポート: 2026-03-12

## サマリ

前回トリアージ（20260309）から3日。inbox 24件の分類（backlog候補10件、削除5件、却下1件）、backlog 36件の突合・関係性分析、CSV起票25件の棚卸しを2セットで実施。施策化済みbacklogエントリ3件の残存、CSV未登録entries 3件、README連動更新漏れを検出。hook系4施策の統合管理やrule-change-checklist関連ISS統合など構造的な改善提案も得られた。

## Worker Set サマリ

| Set | 担当 TG タスク | 評価結果 | 備考 |
|-----|--------------|---------|------|
| set-1 | TG-001, TG-INT, TG-009 | 承認 | inbox 24件分類 + 整合性チェック4項目 + 情報欠損リスク評価6件 |
| set-2 | TG-002, TG-003, TG-004, TG-005, TG-009 | 承認 | backlog突合 + CSV棚卸し25件 + initiative状態 + 関係性分析 + 情報欠損リスク評価4件 |

## 走査結果

### inbox（TG-001）

| アイテム | 判断 | 理由 |
|---------|------|------|
| agentsの公式ディレクトリ分け.md | backlog候補 | agents チェック専門化の提案。具体的作業内容あり |
| ai-driven-dev-patterns-builtin-skills-eval.md | backlog候補 | builtin-skills-evaluation の ADP 横展開提案 |
| entries-pattern-inbox適用検討.md | backlog候補 | inbox/ への entries/ パターン適用検討 |
| meta_scan-mode-and-set-granularity.md | backlog候補 | メタ認知のセット分割粒度・フル/差分スキャン選択 |
| meta_scan-report-change-reason.md | backlog候補 | scan_report の走査対象変更理由記載ルール |
| rules-skills移動時の波及更新パターン.md | backlog候補 | 全スキルへの「関連ファイル一覧」義務化提案 |
| session-flow-checklist-precision.md | backlog候補 | session-flow-policy §5.1 精度向上提案 |
| triage-standard-policy-table-width.md + 適用マトリクス列数増加リスク.md | backlog候補（統合） | 同一テーマを統合。適用マトリクス列数リスク |
| user-invocable-false-description-pattern.md | backlog候補 | user-invocable: false スキルの description 設計パターン |
| チェックリスト型スキルの標準テンプレート化.md | backlog候補 | チェックリスト型スキルのテンプレート化 |
| 条件付き固定タスク配置ルール整備.md | backlog候補 | 条件付きタスクの視覚的区別・サブヘッダ分類 |
| 費用対効果評価フレームワークの標準化.md | backlog候補 | 費用対効果フレームワークのテンプレート化 |
| triage-metacognition テンプレート共通化検討.md | backlog候補 | テンプレート共通化提案 |
| meta_csv-status-update-mechanism.md | 削除（ISS-055 転記済み） | CSV に転記済み |
| meta_knowledge-routing-iss-id.md | 削除（ISS-053 転記済み） | CSV に転記済み |
| meta_routing-execution-verification.md | 削除（ISS-052 転記済み） | CSV に転記済み |
| meta_rule-change-checklist-docs-scope.md | 削除（ISS-054 転記済み） | CSV に転記済み |
| sync-worker同期先コミット漏れ防止.md | 削除（backlog 重複） | backlog/entries/ に同名ファイル既存 |
| 適用マトリクス列数増加リスク.md | 削除（統合） | triage-standard-policy-table-width.md に統合 |
| 条件付き固定タスク適用条件パスパターン重複.md | 却下 | 2箇所のみで過剰設計 |
| ref_ai-driven-development-poc.md | 継続保持 | refs/ ポインターメモ |
| ref_ai-functions.md | 継続保持 | refs/ ポインターメモ |
| ref_openspec-official-summary.md | 継続保持 | refs/ ポインターメモ |
| ref_個人PCローカル環境構築-手順書.md | 継続保持 | refs/ ポインターメモ |

### backlog 棚卸し（TG-002）

#### CSV-ファイル突合結果

| 種別 | 対象 | 推奨 |
|------|------|------|
| entries にあるが CSV にない | permission-prompt-optimization.md | CSV に行追加 |
| entries にあるが CSV にない | role-format-guideのagents対応更新.md | CSV に行追加 |
| entries にあるが CSV にない | 施策間の競合防止方針策定.md | CSV に行追加 |
| CSV にあるが entries にない | backlogメンテナンスセッション作成.md | CSV 行削除（施策化済み） |
| CSV にあるが entries にない | フォーマット変換の内容同等性基準.md | CSV 行削除（施策化済み） |

#### 施策化済みエントリ（CSV残存）

| Row | 施策名 | CSV ステータス | 対応施策 | 推奨 |
|-----|--------|--------------|---------|------|
| 14 | AI補助自動化ツール検討 | 完了 | ai-automation-tool-review（アーカイブ済） | CSV行削除 + entries/ ファイル削除 |
| 31 | フォーマット変換の内容同等性基準 | 候補 | format-conversion-equivalence（アーカイブ済） | CSV行削除 |
| 32 | backlogメンテナンスセッション作成 | 候補 | backlog-maintenance-session（アーカイブ済） | CSV行削除 |

#### その他

- 対象リポジトリ未記入: なし（全行記入済み）
- 施策ディレクトリ名列: 全36行が空欄（backlog-archive-matching で列追加済みだが既存データ未設定）
- CSV 末尾行38: 空行 → 削除

### 課題管理 CSV 棚卸し（TG-003）

**起票ステータス 25件の棚卸し結果**:

| 分類 | 件数 | 内容 |
|------|------|------|
| 保留（環境・外部要因待ち） | 5 | ISS-006, 013, 020, 021, 027 |
| 保留（関連施策検討時に対応） | 7 | ISS-016, 019, 022, 033, 038, 039, 043 |
| 知見として記録済み | 4 | ISS-045, 046, 049, 050 |
| 施策化候補 | 4 | ISS-044, 052, 053, 054+055 |
| クローズ推奨 | 2 | ISS-041（対応完了）, ISS-048（ISS-050と重複） |
| 統合推奨 | 3 | ISS-032→055, ISS-042→054, ISS-048→050 |

### backlog 関係性分析（TG-005）

#### 重複候補

| # | アイテムA | アイテムB | 推奨 |
|---|----------|----------|------|
| 1 | ISS-048 | ISS-050 | ISS-050 に統合し ISS-048 クローズ |
| 2 | ISS-032 | ISS-055 | 同一施策で対応 |
| 3 | ISS-042 | ISS-054 | ISS-054 に統合 |
| 4 | AI補助自動化ツール検討（Row 14） | automation-manager（Row 36） | Row 14 削除（完了済み） |

#### 依存関係

| # | 先行 | 後続 | 依存内容 |
|---|------|------|---------|
| 1 | ai-driven-dev-patterns-triage-standard-policy作成 | ルートリポのトリアージにTG-008走査観点追加 | standard-policy 作成が先 |
| 2 | Claude Code標準plugin・skills情報整理 | disallowedToolsフィールド活用検討 | 標準 plugin 調査結果が前提 |
| 3 | 長文rulesのコンテキストコスト最適化 | ISS-019（skills/ 移動） | 上位施策 |
| 4-6 | Hook系3施策（Rows 33-35） | automation-manager（Row 36） | 個別 hook 実績が入力 |
| 7 | source-of-truth明示 | sync セッション全般 | 同期判断基準 |

#### 統合候補

| # | 統合対象 | 統合後の施策名案 |
|---|---------|---------------|
| 1 | Hook系3施策 + automation-manager | Claude Code hooks 統合自動化 |
| 2 | ISS-042+054+055+032 | rule-change-checklist 走査・連動更新強化 |
| 3 | metacognition構造統一 + ゲート判定重大度 | manager 系スキル構造改善 |
| 4 | ISS-052+053 | ゲート判定ルーティング実行確認強化 |

### initiative 状態確認（TG-004）

| 施策名 | フェーズ | 状態 | 特記事項 |
|--------|---------|------|---------|
| external-repo-cleanup-on-demand | 実施完了→評価待ち | ブロック | L2-worker 全タスク完了済み。L2-evaluator 未ディスパッチ。次回 L1 セッションで対応必要 |

### 整合性チェック（TG-INT）

| チェック項目 | 結果 | 備考 |
|------------|:----:|------|
| skills vs workflow.md | OK | 全スキル整合 |
| README.md 4セクション | **NG** | backlog-maintenance-manager 未記載 + fork-sync 未記載 + docs/ 4ファイル未記載 |
| 参考資料ステータス | OK | 2件とも整合 |
| refs/ 孤立エントリ | OK | 孤立なし |

## backlog 追加・変更案

### 追加候補（inbox backlog候補 10件 + CSV未登録3件）

| # | 優先度 | 施策名 | 元ファイル | 対象リポジトリ |
|---|--------|--------|----------|-------------|
| 1 | 低 | agentsの公式ディレクトリ分け | inbox | dev-process-improvement |
| 2 | 低 | ai-driven-dev-patterns-builtin-skills-eval | inbox | ai-driven-dev-patterns |
| 3 | 低 | entries-pattern-inbox適用検討 | inbox | dev-process-improvement |
| 4 | 低 | メタ認知セット分割粒度・スキャンモード | inbox (meta_scan-mode-and-set-granularity) | dev-process-improvement |
| 5 | 低 | スキャンレポート変更理由記載ルール | inbox (meta_scan-report-change-reason) | dev-process-improvement |
| 6 | 低 | rules-skills移動時の波及更新パターン | inbox | dev-process-improvement |
| 7 | 低 | session-flow-checklist精度向上 | inbox | dev-process-improvement |
| 8 | 低 | triage-standard-policy適用マトリクス列数リスク | inbox (統合) | dev-process-improvement |
| 9 | 低 | user-invocable-false-description-pattern | inbox | dev-process-improvement |
| 10 | 低 | チェックリスト型スキル標準テンプレート化 | inbox | dev-process-improvement |
| 11 | 低 | 条件付き固定タスク配置ルール整備 | inbox | dev-process-improvement |
| 12 | 低 | 費用対効果評価フレームワーク標準化 | inbox | dev-process-improvement |
| 13 | 低 | triage-metacognitionテンプレート共通化 | inbox | dev-process-improvement |
| 14 | 低 | permission-prompt-optimization | entries（CSV未登録） | dev-process-improvement |
| 15 | 低 | role-format-guideのagents対応更新 | entries（CSV未登録） | dev-process-improvement |
| 16 | 中 | 施策間の競合防止方針策定 | entries（CSV未登録） | dev-process-improvement |

### 削除・クローズ候補

| 対象 | 種別 | 理由 |
|------|------|------|
| backlog.csv Row 14（AI補助自動化ツール検討） | CSV行削除 + entries削除 | ステータス「完了」、施策アーカイブ済み |
| backlog.csv Row 31（フォーマット変換の内容同等性基準） | CSV行削除 | 施策化済み、entries既削除 |
| backlog.csv Row 32（backlogメンテナンスセッション作成） | CSV行削除 | 施策化済み、entries既削除 |
| backlog.csv 行38 | 空行削除 | データなし |
| inbox: meta_csv-status-update-mechanism.md | 削除 | ISS-055 転記済み |
| inbox: meta_knowledge-routing-iss-id.md | 削除 | ISS-053 転記済み |
| inbox: meta_routing-execution-verification.md | 削除 | ISS-052 転記済み |
| inbox: meta_rule-change-checklist-docs-scope.md | 削除 | ISS-054 転記済み |
| inbox: sync-worker同期先コミット漏れ防止.md | 削除 | backlog に重複 |
| inbox: 適用マトリクス列数増加リスク.md | 削除 | triage-standard-policy-table-width に統合 |
| inbox: 条件付き固定タスク適用条件パスパターン重複.md | 削除 | 却下（過剰設計） |
| ISS-041 | クローズ | backlog-archive-matching T-005 完了 |
| ISS-048 | クローズ | ISS-050 と重複 |

### CRITICAL修正（セッション内実施）

| 対象 | 内容 |
|------|------|
| README.md | backlog-maintenance-manager + fork-sync + docs/ 4ファイルを追記 |

## 振り返り

### うまくいったこと
- 2セット分割でbacklog/CSV/inboxの相互参照を効率的に処理
- TG-009 全10件がリスク「低」で削除・統合を安全に実施可能

### 改善すべきこと
- マネージャーのCSV起票件数見積もり（24件→実際25件）に軽微な誤差

### プロセス改善の気づき
- README.md の連動更新が session-flow-policy / rule-change-checklist に含まれておらず、新セッション追加時に漏れる構造的問題
- CSV未登録 entries/ ファイルの検出パターンが繰り返し発生（backlog追加時のCSV同時更新必須化を検討）

### 次回トリアージへの申し送り
- external-repo-cleanup-on-demand: 次回 L1 セッションで評価者ディスパッチ→ゲート判定を実施
- 施策ディレクトリ名列の既存データクリーンアップ検討

## 知見集約

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 Set | 対象ファイル・領域 | 詳細 |
|---|------|----------|-----------------|------|
| 1 | README.md の連動更新が session-flow-policy のチェックリストに含まれていない | Set-1 (worker+eval) | session-flow-policy / rule-change-checklist | 新セッションタイプ追加時に README 4セクション更新が漏れる構造的問題 |
| 2 | 施策化済みエントリの CSV 残存が依然として発生 | Set-2 (worker) | l1-manager/SKILL.md | backlog-archive-matching 対策前の既存エントリ3件が残存 |
| 3 | CSV 未登録の entries/ ファイルが発生するパターン | Set-2 (worker) | backlog 管理フロー | entries/ 追加と CSV 行追加の同時実行必須化を検討 |
| 4 | トリアージマネージャーのタスク指示書と実データの件数差異 | Set-2 (eval) | triage-manager/SKILL.md | ワーカーは実データに基づいて走査すべき（現行の対応は正しい） |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 Set | 背景・文脈 |
|---|------|----------|-----------|
| 1 | meta_* inbox エントリは ISS 転記済みかどうかで扱いが二分される | Set-1 | 転記済み4件は削除、未転記2件は独立 backlog 候補 |
| 2 | inbox/ref_* は4件とも安定保持 | Set-1 | 施策化まで inbox に残り続ける形 |
| 3 | hook/自動化系4施策は統合管理が効率的 | Set-2 | Claude Code hooks API が共通技術基盤 |
| 4 | 「起票」ステータス長期残存25件中12件が関連施策アーカイブ済み | Set-2 | 施策クローズ時の ISS 連動クローズが有効 |
| 5 | Set-2 のセット分割判断（backlog/CSV/initiative 同一セット）が適切に機能 | Set-2 (eval) | タスク間の相互参照が効率的 |

## 課題集約

### ワーカーセット別課題件数

| Set | 課題件数 | CSV転記件数 | 備考 |
|-----|---------|-----------|------|
| set-1 | 1 | 0 | README 連動更新漏れ → セッション内修正で対応 |
| set-2 | 2 | 0 | CSV未登録3件 + 施策ディレクトリ名列空欄 → セッション内アクションで対応 |

### CSV転記判断

3件の課題はいずれもセッション内のアクション実施で解消可能。CSV転記不要。
- Set-1 課題（README連動更新漏れ）: CRITICAL修正として README.md を更新
- Set-2 課題1（CSV未登録3件）: backlog追加アクションで CSV に行追加
- Set-2 課題2（施策ディレクトリ名列空欄）: 知見として記録。次回施策化時から自然に埋まる運用とし、遡及的記入は今回スキップ

## 課題起票

- 起票した課題（合計）：0 件（全てセッション内アクションで対応）

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-12
**レビュー依頼先**: ユーザー
**レビュー状態**: レビュー待ち
