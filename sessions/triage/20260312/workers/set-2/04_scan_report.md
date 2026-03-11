# スキャンレポート: Set-2

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-002 | backlog CSV-ファイル突合 | 完了 |
| TG-003 | CSV 起票25件棚卸し | 完了 |
| TG-004 | external-repo-cleanup-on-demand 状態確認 | 完了 |
| TG-005 | backlog 36件関係性分析 | 完了 |
| TG-009 | 情報欠損リスク評価 | 完了 |

---

## TG-002: backlog CSV とファイル実体の突合

### CSV 構造確認

| 項目 | 結果 |
|------|------|
| ヘッダー列数 | 8列（施策名, 優先度, ステータス, 対象リポジトリ, 起票日, 簡易説明, ファイル名, 施策ディレクトリ名） |
| データ行数 | 36行 |
| 末尾空行（行38） | あり → 削除候補 |
| 列数不整合行 | なし（全行8列） |

### CSV vs entries/ ファイル突合

| 種別 | ファイル名 | 状態 | 推奨アクション |
|------|----------|------|-------------|
| entries/ にあるが CSV にない | permission-prompt-optimization.md | CSV 未登録 | CSV に行追加、または不要なら entries/ から削除 |
| entries/ にあるが CSV にない | role-format-guideのagents対応更新.md | CSV 未登録 | CSV に行追加、または不要なら entries/ から削除 |
| entries/ にあるが CSV にない | 施策間の競合防止方針策定.md | CSV 未登録 | CSV に行追加、または不要なら entries/ から削除 |
| CSV にあるが entries/ にない | backlogメンテナンスセッション作成.md | 施策化済み（backlog-maintenance-session, アーカイブ完了） | CSV 行削除 |
| CSV にあるが entries/ にない | フォーマット変換の内容同等性基準.md | 施策化済み（format-conversion-equivalence, アーカイブ完了） | CSV 行削除 |

### 施策化済みチェック

施策ディレクトリ名列は全36行が空欄。backlog-archive-matching 施策で列を追加したが、既存行への値設定は未実施。

以下のエントリは CSV にファイル名が残っているが、対応する施策がアーカイブ済み:

| Row | 施策名 | CSV ステータス | アーカイブ施策ディレクトリ | 推奨 |
|-----|--------|--------------|----------------------|------|
| 14 | AI補助自動化ツール検討 | 完了 | ai-automation-tool-review | CSV 行削除 + entries/ ファイル削除 |
| 32 | backlogメンテナンスセッション作成 | 候補 | backlog-maintenance-session | CSV 行削除（entries/ ファイルは既に削除済み） |
| 31 | フォーマット変換の内容同等性基準 | 候補 | format-conversion-equivalence | CSV 行削除（entries/ ファイルは既に削除済み） |

### 対象リポジトリ未記入チェック

未記入なし。全36行に値が設定済み。

### ステータス「完了」残存確認

| Row | 施策名 | entries/ ファイル | 推奨 |
|-----|--------|-----------------|------|
| 14 | AI補助自動化ツール検討 | 残存 | CSV 行削除 + entries/ ファイル削除 |

---

## TG-003: CSV ステータス「起票」棚卸し

### 起票ステータス一覧（25件）

| ISS-ID | タイトル | 優先度 | 関連施策 | 施策状態 | 対応方針案 |
|--------|--------|--------|---------|---------|----------|
| ISS-006 | ロール定義と OpenSpec 開発ライフサイクルの統合が未定義 | 中 | role-agent-prompts | アーカイブ済 | openspec 連携が進展するまで保留。長期残存 |
| ISS-013 | Claude Code Agent Teams 機能がworktreeガイドラインで言及されていない | 低 | git-worktree-standardization | アーカイブ済 | ガイドライン次回改訂時に対応。保留 |
| ISS-016 | m6o-es-product-api の .claude/rules/ 向けルールファイル整備 | 中 | m6o-es-product-apiドキュメント整理 | アーカイブ済 | 別施策として backlog 起票待ち。保留 |
| ISS-019 | claude-directory-guide.md の skills/ 移動検討 | 低 | claude-directory-structure-rules | アーカイブ済 | 長文rulesのコンテキストコスト最適化（Row 9）で統合対応可能 |
| ISS-020 | config.yaml の tasks ルールのカテゴリ分けが CLI ツールに適合しない | 低 | openspec-code-trial | アーカイブ済 | openspec 改善時に対応。保留 |
| ISS-021 | spec 作成時にエッジケース・境界条件のシナリオが漏れやすい | 低 | openspec-code-trial | アーカイブ済 | openspec 改善時に対応。保留 |
| ISS-022 | spec 作成フェーズが openspec サイクルのボトルネック | 中 | openspec-code-trial | アーカイブ済 | openspec 改善時に対応。保留 |
| ISS-027 | Claude Code Web は1セッション=1リポジトリの制約がある | 高 | dev-process-improvementリポジトリ分離 | アーカイブ済 | 環境制約として記録。Claude Code 側の対応待ち |
| ISS-032 | CSV ステータスの同期漏れパターン | 低 | workflow-doc-consistency-fix | アーカイブ済 | ISS-055 と統合して対応を検討 |
| ISS-033 | 成功基準と CSV 対応方針案のスコープ整合 | 低 | workflow-doc-consistency-fix | アーカイブ済 | ルール改善時に対応。保留 |
| ISS-038 | CSV列追加時に全既存行の列数整合性を検証すべき | 低 | 課題管理とinbox管理の方法見直し | アーカイブ済 | 知見として記録済み。次回 CSV 変更時に適用 |
| ISS-039 | L1クローズ手順で gate_review の Write と git mv の実行順序に注意が必要 | 低 | 課題管理とinbox管理の方法見直し | アーカイブ済 | l1-manager 注意事項追加で対応可能。保留 |
| ISS-042 | パス移動施策の grep 検証で走査対象ディレクトリが網羅されていない | 中 | partial-repo-sync | アーカイブ済 | ISS-054 と統合（rule-change-checklist 走査対象拡充） |
| ISS-043 | commit-message.md の2系統共存による運用混乱リスク | 低 | sync/20260308 | セッション完了 | 経過観察中。保留 |
| ISS-044 | ai-driven-dev-patterns の連動更新が未実施 | 中 | sync/20260308 | セッション完了 | 次回同期セッションのスコープに含める |
| ISS-045 | Claude Agent SDK 環境では settings.json の allow/deny リストが機能しない | 中 | subagent-permission-model | アーカイブ済 | 知見として記録。運用ガイドに明記済み |
| ISS-046 | エージェント定義の tools フィールドによるツール制限が SDK 環境で機能しない | 低 | subagent-permission-model | アーカイブ済 | 知見として記録。意図の文書化として維持 |
| ISS-047 | deferred tools が tools フィールドの制限を迂回する | 中 | cli-permission-verification | アーカイブ済 | disallowedTools 活用検討（Row 28）で対応 |
| ISS-048 | deny リスト設計時の Read/Write/Edit 網羅性チェック不足 | 低 | cli-permission-verification | アーカイブ済 | ISS-050 と重複。統合してクローズ検討 |
| ISS-049 | deny リストは CLI 環境で唯一の強制的制限 | 中 | cli-permission-verification | アーカイブ済 | 知見として記録済み |
| ISS-050 | deny リスト設計時は Read/Write/Edit の3ツール網羅的考慮が必要 | 中 | cli-permission-verification | アーカイブ済 | ISS-048 と重複。統合してクローズ検討 |
| ISS-052 | gate_review ルーティング宣言の未実行率22% | 中 | メタ認知20260311 | セッション完了 | l1-manager クローズ手順でルーティング実行確認強化。施策化候補 |
| ISS-053 | 知見型 CSV ルーティングが構造的に転記漏れしやすい | 中 | メタ認知20260311 | セッション完了 | ISS-ID 事前割当 or クローズ時突合。施策化候補 |
| ISS-054 | rule-change-checklist の grep 走査対象に docs/ が未含有 | 中 | メタ認知20260311 | セッション完了 | ISS-042 と統合。rule-change-checklist 改善施策として対応 |
| ISS-055 | CSV ステータス更新漏れの検出・防止メカニズムが未整備 | 中 | メタ認知20260311 | セッション完了 | ISS-032 と統合。CSV 管理改善施策として対応 |

### ISS-052〜055 対応方針検討

| ISS-ID | 対応方針案 | 備考 |
|--------|----------|------|
| ISS-052 | l1-manager クローズ手順の「ルーティング実行確認」を自己申告から実在確認に変更する施策を検討 | 未実行率22%は無視できない |
| ISS-053 | クローズ手順に「知見型ルーティングの ISS-ID 事前割当」ステップ追加。ISS-052 と同一施策で対応可能 | ISS-052 と統合推奨 |
| ISS-054 | rule-change-checklist SKILL.md の走査対象リストに docs/ を明示追加。ISS-042 と統合して単一施策で対応 | 小規模だが再発パターンのため施策化推奨 |
| ISS-055 | rule-change-checklist に CSV ステータス更新チェック項目追加。ISS-032 と統合 | ISS-054 と同じ rule-change-checklist 改善施策に含める |

### ISS-041 状態確認

| 項目 | 結果 |
|------|------|
| CSV ステータス | タスク化済 |
| タスク化先 | backlog-archive-matching T-005 |
| T-005 ステータス | 完了（l1-manager クローズチェックリストにステップ5追加） |
| 施策ゲート判定 | 通過（全8成功基準達成） |
| 施策状態 | アーカイブ済み |
| 推奨 | ISS-041 を「クローズ」に更新。対応完了 |

---

## TG-004: external-repo-cleanup-on-demand 進行状態確認

| 項目 | 状態 |
|------|------|
| 施策ディレクトリ | sessions/initiatives/external-repo-cleanup-on-demand/ |
| 00_proposal.md ステータス | 実施中 |
| 02_tasks.md | 全6タスク（T-001〜T-006）完了 |
| 04_work_report.md | 作成済み |
| 06_eval_report.md | テンプレート状態（未実施） |
| 08_gate_review.md | テンプレート状態（未実施） |
| 進行状態 | **実施フェーズ完了 → 評価フェーズ待ち** |

備考: L2-worker の全タスクは完了しているが、L2-evaluator による評価と L1 によるゲート判定が未実施。次回 L1 セッションで評価者ディスパッチ→ゲート判定を実施する必要がある。

---

## TG-005: backlog 36件の関係性分析

### カテゴリ分類

| カテゴリ | 件数 | 主要アイテム |
|---------|------|------------|
| hook/自動化系 | 4 | SessionStart-hook, PreToolUse-hook, PostToolUse-hook, automation-manager |
| triage/メタ認知系 | 3 | ai-driven-dev-patterns-triage-standard-policy, メタ認知セッションの横展開, backlogメンテナンスセッション |
| ai-driven-dev-patterns 系 | 10 | sessionsテンプレート間連携, ハーネスエンジニアリング, マルチAI, 全ロール準拠確認, 北村さん取込, 並列化, Building-trust, ディレクトリ構成, TG-008横展開, source-of-truth明示 |
| ルール/ポリシー系 | 3 | 長文rules最適化, l1-manager-checklist-reference, denyリスト副作用分析 |
| ドキュメント/テンプレート系 | 3 | backlogテンプレート凡例強化, agentsガイドライン, フォーマット変換基準 |
| セキュリティ/設定系 | 1 | LLMローカル開発セキュリティ強化 |
| その他 | 12 | dev-workflow-detail L1参照精査, リンク整合性, 知見集約逆移植, AI補助自動化, 記法スタイル, sync-worker漏れ防止, devkit, L2知見ギャップ, disallowedTools, metacognition構造統一, ゲート判定重大度, Claude Code標準plugin |

### 重複候補

| # | アイテムA | アイテムB | 重複の内容 | 推奨 |
|---|----------|----------|----------|------|
| 1 | ISS-048（deny Read/Write/Edit 網羅性） | ISS-050（同） | 同一知見の異なる文脈での重複記載 | ISS-050 に統合し ISS-048 クローズ |
| 2 | ISS-032（CSV ステータス同期漏れ） | ISS-055（CSV ステータス更新漏れ防止） | 同じ問題（CSV ステータス管理の不備）の異なる側面 | 同一施策で対応 |
| 3 | ISS-042（grep 走査対象未網羅） | ISS-054（rule-change-checklist docs/ 未含有） | rule-change-checklist の走査対象網羅性 | ISS-054 に統合 |
| 4 | AI補助自動化ツール検討（Row 14） | automation-managerセッション作成（Row 36） | AI 自動化の調査と制度化。前者は完了済み調査、後者は制度化 | Row 14 は削除（完了済み） |
| 5 | backlogメンテナンスセッション作成（Row 32） | - | 施策化済みでアーカイブ完了 | CSV 行削除 |

### 依存関係

| # | 先行アイテム | 後続アイテム | 依存内容 |
|---|------------|------------|---------|
| 1 | ai-driven-dev-patterns-triage-standard-policy作成（Row 21） | ルートリポのトリアージにTG-008走査観点追加（Row 17） | standard-policy 作成が先、TG-008 横展開が後 |
| 2 | Claude Code標準plugin・skills情報整理（Row 37） | disallowedToolsフィールド活用検討（Row 28） | 標準 plugin 調査結果が disallowedTools 検討の前提 |
| 3 | 長文rulesのコンテキストコスト最適化（Row 9） | ISS-019（claude-directory-guide.md skills/ 移動） | 同じ問題の上位施策 |
| 4 | SessionStart-hook（Row 33） | automation-manager（Row 36） | 個別 hook 実績が自動化マネージャー設計の入力 |
| 5 | PreToolUse-hook（Row 34） | automation-manager（Row 36） | 同上 |
| 6 | PostToolUse-hook（Row 35） | automation-manager（Row 36） | 同上 |
| 7 | ai-driven-dev-patterns_source-of-truth明示（Row 20） | sync セッション全般 | source-of-truth が明示されると同期判断が容易に |

### 統合候補

| # | 統合対象 | 統合後の施策名案 | 理由 |
|---|---------|---------------|------|
| 1 | Hook 系3施策（Rows 33-35）+ automation-manager（Row 36） | Claude Code hooks 統合自動化 | 同一技術基盤（hooks API）を使う4施策。automation-manager を上位施策として個別 hook を統合管理 |
| 2 | ISS-042 + ISS-054 + ISS-055 + ISS-032 | rule-change-checklist 走査・連動更新強化 | rule-change-checklist の改善という共通テーマ。走査対象拡充 + CSV ステータス管理を統合 |
| 3 | metacognition-managerの記述構造統一（Row 29）+ ゲート判定基準での課題重大度の明文化（Row 30） | manager 系スキル構造改善 | 両方 manager 系スキルの記述構造・判定基準の改善 |
| 4 | ISS-052 + ISS-053 | ゲート判定ルーティング実行確認強化 | 両方ゲート判定時のルーティング品質改善 |

---

## TG-009: 情報欠損リスク評価

### 走査結果サマリ
- 評価対象ファイル数: 4件（削除候補: 4件 / 統合候補: 0件）
- リスク「高」: 0件 / リスク「中」: 0件 / リスク「低」: 4件

### リスク評価テーブル

| ファイル名 | 種別 | 含有知見数 | 参照リンク数 | 消失リスク | 推奨アクション |
|-----------|------|----------|------------|----------|-------------|
| backlog/entries/AI補助自動化ツール検討.md | 削除 | 0（施策完了済み。知見は ai-automation-tool-review アーカイブに保存） | 0 | 低 | そのまま削除 |
| backlog.csv Row 14（AI補助自動化ツール検討） | 削除 | 0 | 0 | 低 | そのまま削除 |
| backlog.csv Row 31（フォーマット変換の内容同等性基準） | 削除 | 0（施策完了済み） | 0 | 低 | そのまま削除 |
| backlog.csv Row 32（backlogメンテナンスセッション作成） | 削除 | 0（施策完了済み） | 0 | 低 | そのまま削除 |

全削除候補は施策としてアーカイブ済みであり、知見はアーカイブの gate_review や work_report に保存されている。情報欠損リスクはない。

---

## 削除・クローズ候補まとめ

### backlog 削除候補

| 対象 | 種別 | 理由 |
|------|------|------|
| backlog.csv Row 14（AI補助自動化ツール検討） | CSV 行削除 | ステータス「完了」、施策アーカイブ済み |
| backlog.csv Row 31（フォーマット変換の内容同等性基準） | CSV 行削除 | 施策化済み（format-conversion-equivalence）、アーカイブ完了、entries/ ファイル既削除 |
| backlog.csv Row 32（backlogメンテナンスセッション作成） | CSV 行削除 | 施策化済み（backlog-maintenance-session）、アーカイブ完了、entries/ ファイル既削除 |
| backlog/entries/AI補助自動化ツール検討.md | ファイル削除 | ステータス「完了」、施策アーカイブ済み |
| backlog.csv 行38 | 空行削除 | データなしの末尾空行 |

### CSV 未登録エントリ（要判断）

| ファイル | 推奨 |
|---------|------|
| backlog/entries/permission-prompt-optimization.md | CSV に行追加して正式登録 |
| backlog/entries/role-format-guideのagents対応更新.md | CSV に行追加して正式登録 |
| backlog/entries/施策間の競合防止方針策定.md | CSV に行追加して正式登録 |

### ISS クローズ候補

| ISS-ID | 理由 |
|--------|------|
| ISS-041 | backlog-archive-matching 施策で対応完了、ゲート通過済み |
| ISS-048 | ISS-050 と重複。ISS-050 に統合 |

---

## 課題起票

- 起票件数: 2件（`07_issues.md` に起票済み）

---

## 走査中の知見

### ルール化候補（.claude/rules/ や skills/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 施策化済みエントリの CSV 残存が依然として発生 | l1-manager/SKILL.md | backlog-archive-matching で対策済みだが、対策前の既存エントリ3件（Row 14, 31, 32）が残存。施策ディレクトリ名列も全行空欄のまま。既存データのクリーンアップが必要 |
| 2 | CSV 未登録の entries/ ファイルが3件存在 | backlog 管理フロー | entries/ へのファイル追加と CSV 行追加が分離しており片方だけ実行されるケース。backlog テンプレートの手順に CSV 同時更新を必須化すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | hook/自動化系4施策は技術基盤が共通（Claude Code hooks API）のため統合管理が効率的 | TG-005 関係性分析で hook 系アイテムが独立して起票されているが、API 調査・設計は共通作業 |
| 2 | 「起票」ステータスの長期残存（25件中12件が関連施策アーカイブ済み）が蓄積傾向 | TG-003 棚卸しで、関連施策完了後も ISS が「起票」のまま残存するパターンが多数。定期的な棚卸し or 施策クローズ時の連動クローズが有効 |
| 3 | external-repo-cleanup-on-demand は実施完了・評価待ちの状態が継続 | TG-004 で確認。L1 セッションでの評価者ディスパッチが必要 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-12
