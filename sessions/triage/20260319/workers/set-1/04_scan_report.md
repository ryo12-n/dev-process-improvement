# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox 15 件分類 | 完了 |
| TG-002 | backlog BL-095〜BL-106 突合 | 完了 |
| TG-003 | 課題管理 CSV 確認 | 完了 |
| TG-004 | initiative 状態確認 | 完了 |
| TG-005 | backlog 関係性分析 | 完了 |
| TG-006 | ルール・workflow 整合性 | 完了 |
| TG-007 | refs/ 孤立エントリ確認 | 完了 |
| TG-008 | セッション構造チェック | スキップ（SC セッション実施済み） |
| TG-009 | 情報欠損リスク評価 | スキップ（大規模削除なし） |
| TG-010 | GHA ↔ Skills ドリフト検出 | 完了 |

---

## TG-001: inbox 走査・分類

### 分類結果サマリ

| 分類 | 件数 | 内訳 |
|------|------|------|
| backlog 候補 | 11 | 下記テーブル参照 |
| ルール反映 | 3 | 下記テーブル参照 |
| 却下 | 0 | — |
| 保留 | 1 | dispatcher-reject-retry-count-explicit.md |

### 詳細分類テーブル

| # | ファイル名 | 分類 | 理由 |
|---|----------|------|------|
| 1 | SC-007スキャン手順改善_括弧内包含記述の確認.md | ルール反映 | sc-collection-worker の SC-007 手順に括弧内包含記述チェックを追加する具体的提案。スキル定義への直接反映が適切 |
| 2 | SCチェック後のアクション接続明確化.md | backlog 候補 | session-consistency-manager SKILL.md の作業フローへの変更提案。BL-101（SC フィードバックループ）と関連するが、スコープが異なる（検出後アクションの即時実行オプション追加）|
| 3 | automation-20260318-count-definition.md | ルール反映 | automation-worker のカウント定義明確化。スキャン計画テンプレートまたはワーカー指示への追記で対応可能 |
| 4 | automation-20260318-integration-score.md | backlog 候補 | 統合施策のスコア算出方法定義。automation-candidates 運用ガイドへの追加が必要で、一定のスコープがある |
| 5 | dispatcher-reject-retry-count-explicit.md | 保留 | initiative-dispatcher.yml の reject ルートに retry_count=0 を明示追加。機能的問題なし、一貫性のみ。次回 GHA メンテナンス時に一括対応が効率的 |
| 6 | gha-claude-dir-write-restriction.md | backlog 候補 | GHA 環境での `.claude/` 書き込み制限と git plumbing 回避手順のドキュメント化。ISS-068 と直結。gha-guideline への追加が必要 |
| 7 | gha-constraint-check-in-proposal.md | backlog 候補 | 施策設計段階での GHA 実行不可チェック。00_proposal.md テンプレートへの変更を含む |
| 8 | gha-metadata-extraction-composite-action.md | backlog 候補 | メタデータ取得の composite action 共通化。現時点2箇所のみでコスト対効果要検討 |
| 9 | gha-task-division-step-name-reference.md | ルール反映 | l2-plan-worker の 02a_task_division.md フォーマットにガイド追加。スキル定義への直接反映が適切 |
| 10 | gha-verdict-step-separation-pattern.md | backlog 候補 | GHA verdict 抽出とディスパッチのステップ分離パターン。gha-guideline への追加候補 |
| 11 | meta-rule-checklist-integration-proposal.md | backlog 候補 | メタルール横断検証と rule-change-checklist の統合提案。l1-manager SKILL.md の条件付きタスク再編 |
| 12 | non-initiative-cost-tracking.md | backlog 候補 | 非 initiative セッションへのコスト計測拡張。dispatch-log-and-cost-tracking の次段階 |
| 13 | success-criteria-grep-scope.md | backlog 候補 | 成功基準 grep のスコープ明示ガイドライン追加 |
| 14 | template-md-path-reference-check.md | backlog 候補 | rule-change-checklist にテンプレート .md パスを追加。BL-092（テンプレート相互参照）と関連 |
| 15 | template-new-file-update-pattern.md | backlog 候補 | テンプレート新設時の 5 ステップ連動更新パターンの固定タスク化。BL-099 と関連 |

---

## TG-002: backlog 突合チェック

### BL-095〜BL-106 施策化状況

| BL-ID | 施策名 | CSV ステータス | initiatives/ 存在 | _archive/ 存在 | 判定 |
|-------|--------|-------------|-----------------|---------------|------|
| BL-095 | PostToolUse hook 品質チェック統合 | 候補 | なし | なし | 未施策化 |
| BL-096 | backlog エントリ記述粒度最低基準 | 候補 | なし | なし | 未施策化 |
| BL-097 | BM-001 閾値段階化 | 候補 | なし | なし | 未施策化 |
| BL-098 | BM レポート→backlog 実行トリガー | 候補 | なし | なし | 未施策化 |
| BL-099 | .claude/templates/ 連動更新チェックリスト | 候補 | なし | なし | 未施策化 |
| BL-100 | （欠番） | — | — | — | 欠番 |
| BL-101 | SC フィードバックループ定義 | 候補 | なし | なし | 未施策化 |
| BL-102 | SC インライン参照走査拡大 | 候補 | なし | なし | 未施策化 |
| BL-103 | evaluator 対称性テーブル統一 | 候補 | なし | なし | 未施策化 |
| BL-104 | SC-008 壊れた参照修正 | 未着手 | なし | なし | 施策ディレクトリ名定義済み(sc-008-broken-ref-fix)、未開始 |
| BL-105 | SC-006 impl 系列追加 | 未着手 | なし | なし | 施策ディレクトリ名定義済み(sc-006-impl-column-add)、未開始 |
| BL-106 | テンプレート構成仕様定義 | 候補 | なし | なし | 未施策化 |

### 検出事項

| # | 検出内容 | 重大度 |
|---|---------|--------|
| 1 | BL-100 が欠番（CSV に存在しない） | 低（採番ミスまたは削除済み） |
| 2 | BL ID 未採番エントリ 2 件が CSV に存在（「SC チェック Quick Wins 一括是正」「リネーム時全文検索チェック義務化ルール追加」） | 中（BL-104 と内容重複の可能性） |
| 3 | 全エントリの対象リポジトリが記入済み（未記入なし） | — |

---

## TG-003: 課題管理 CSV 確認

### 高優先度課題の対応状況

| ISS-ID | 優先度 | 種別 | ステータス | 概要 | 対応状況 |
|--------|--------|------|----------|------|---------|
| ISS-059 | 高 | リスク | 起票 | GHA ユーザー入力 JSON シェルインジェクション | 未対応。initiative-dispatcher 施策はアーカイブ済み。別途対応が必要 |
| ISS-061 | 高 | リスク | 起票 | settings.json deny ルール非機能 | 未対応。BL-067 + BL-071 で二重防御予定だが未施策化 |
| ISS-064 | 高 | 改善提案 | 起票 | テストスクリプトパス未設定（ai-driven-dev-patterns） | 未対応。外部リポジトリ側の問題 |
| ISS-068 | 高 | 技術的制約 | 起票 | GHA `.claude/` 書き込み拒否 | 新規（2026-03-19）。inbox に回避手順あり |

### 新規課題（ISS-065〜068）の確認

| ISS-ID | 優先度 | 種別 | 概要 | 関連 BL |
|--------|--------|------|------|---------|
| ISS-065 | 中 | 不具合 | session-lifecycle-policy §1.3 co-* 列欠落 | BL-105 と関連（impl 系も欠落） |
| ISS-066 | 中 | 不具合 | CSV/md ステータス不一致 4 件 | csv-conflict-prevention 施策の事後問題 |
| ISS-067 | 低 | 不具合 | BL ID 二重採番 | BL-084 で根本対応予定 |
| ISS-068 | 高 | 技術的制約 | GHA `.claude/` 書き込み拒否 | inbox gha-claude-dir-write-restriction.md |

---

## TG-004: initiative 状態確認

### アーカイブ待ち 7 件

| # | 施策名 | 全タスク完了 | ゲート通過 | アーカイブ可否 |
|---|--------|-----------|----------|-------------|
| 1 | backlog-to-issue-status-sync | 完了 | 済み | 可 |
| 2 | csv-conflict-prevention | 完了 | 済み | 可 |
| 3 | l1-manager-checklist-integration | 完了 | 済み | 可 |
| 4 | l1-manager-enhanced-planning | 完了 | 済み | 可 |
| 5 | session-cost-measurement | 完了 | 済み | 可 |
| 6 | session-lifecycle-policy-rename | 完了 | 済み | 可 |
| 7 | skill-plugin-overlap-check-rule | 完了 | 済み | 可 |

**判定**: 7 件すべてアーカイブ可能。

### 進行中 5 件

| # | 施策名 | 現在フェーズ | タスク進捗 | ゲートレビュー | 備考 |
|---|--------|-----------|----------|-------------|------|
| 1 | backlog-id-and-issue-template | 計画 | 0/5 未着手 | なし | 長期停滞（2026-03-14 作成） |
| 2 | external-repo-cleanup-on-demand | 完了待ち | 6/6 完了 | テンプレートのまま（未記入） | ゲート判定実施でアーカイブ可能 |
| 3 | impl-worker-worklog-reliability | 計画 | 0/5 未着手 | なし | 長期停滞（2026-03-14 作成） |
| 4 | sync-worker-target-commit | 完了待ち | 0/5（旧形式） | テンプレートのまま（未記入） | ゲート判定実施でアーカイブ可能 |
| 5 | triage-phase-gate-and-gha-sync | 完了待ち | 0/8（旧形式） | テンプレートのまま（未記入） | ゲート判定実施でアーカイブ可能 |

**注意**: 3 施策（external-repo-cleanup-on-demand, sync-worker-target-commit, triage-phase-gate-and-gha-sync）は作業・評価が完了しているが 08_gate_review.md が未記入。ゲート判定を実施すればアーカイブに移行可能。

---

## TG-005: backlog 関係性分析

### 重複候補

| # | エントリ A | エントリ B | 重複の性質 | 推奨アクション |
|---|----------|----------|----------|-------------|
| 1 | BL-104（SC-008 壊れた参照修正） | 未採番「SC チェック Quick Wins 一括是正」 | BL-104 は Quick Wins の修正箇所 #1 を含む。Quick Wins は BL-104 の上位集合 | 未採番エントリを BL-104 に統合するか、未採番エントリに BL ID を採番して BL-104 を部分タスクとして管理 |
| 2 | BL-099（templates/ 連動更新チェックリスト） | inbox template-new-file-update-pattern.md | テンプレート新設時の連動更新。BL-099 は .claude/templates/ 限定、inbox は initiative テンプレート全般 | inbox を backlog 候補として起票後、BL-099 とのスコープ調整を検討 |
| 3 | BL-101（SC フィードバックループ） | inbox SCチェック後のアクション接続明確化.md | SC チェック結果のアクション接続。BL-101 は「フィードバックループ定義」、inbox は「即時修正オプション追加」 | 補完関係。inbox を BL-101 の拡張提案として統合可能 |

### 依存関係

| # | 依存元 | 依存先 | 依存の内容 |
|---|--------|--------|----------|
| 1 | BL-095（PostToolUse hook 統合） | BL-030, BL-082 | BL-095 は BL-030 + BL-082 の統合施策。施策化時に元エントリのクローズが必要 |
| 2 | BL-105（impl 系列追加） | ISS-065 | ISS-065（co-* 列欠落）と同根の問題。BL-105 施策で ISS-065 も併せて対応可能 |

### 統合候補グループ

| グループ | エントリ | 統合理由 |
|---------|---------|---------|
| SC 改善グループ | BL-101, BL-102, BL-104, inbox SCチェック後のアクション接続明確化.md | すべて session-consistency-manager の改善提案。統合施策として実施すると効率的 |

---

## TG-006: ルール・workflow 整合性チェック

### 参考資料ステータスチェック

| ファイル | カテゴリ | バナー有無 | 判定 |
|---------|---------|----------|------|
| docs/coordination-protocol-guideline.md | 参考資料（ドラフト） | あり（一部統合済み） | 適正 |
| docs/git-worktree-guideline.md | 参考資料（ドラフト） | あり（一部統合済み） | 適正 |
| docs/management-system-guide.md | 運用ガイド | なし | 適正（バナー不要） |
| docs/subagent-permission-guide.md | 運用ガイド | なし | 適正（バナー不要） |
| docs/implementation.md | 運用ガイド | なし | 適正（バナー不要） |

### README 整合性チェック

| チェック項目 | 結果 | 備考 |
|------------|------|------|
| README.md 行数 | 219 行 | **超過**: 150 行上限に対し 69 行超過 |

### スキル定義の関連ファイル一覧チェック

| スキル | 関連ファイル件数 | サンプル確認結果 |
|--------|-------------|-------------|
| l1-manager/SKILL.md | 15 件 | 主要ファイル（agents/、_template/、docs/workflow.md、rules/）を網羅。09_cost_record.md, 02b_dispatch_log.md の追加が近日中に反映されている |

### 検出した乖離

| # | 乖離内容 | 重大度 |
|---|---------|--------|
| 1 | README.md が 219 行で 150 行上限超過（CLAUDE.md ドキュメント階層方針） | 中 |
| 2 | docs/workflow.md が 1067 行で肥大化 | 低（可視化文書の性質上、一定の長さは許容される） |

---

## TG-007: refs/ 孤立エントリ確認

### refs/ エントリ一覧

| # | エントリ | 種別 | inbox/ref_* ポインター | メタ情報（用途・有効期限） | 判定 |
|---|---------|------|---------------------|---------------------|------|
| 1 | agency-agents/ | ディレクトリ | なし | 要確認 | 孤立の可能性あり |
| 2 | ai-driven-dev-patterns/ | ディレクトリ | なし | 常時参照（CLAUDE.md に記載） | 問題なし |
| 3 | claude-code-action/ | ディレクトリ | なし | 要確認 | 孤立の可能性あり |
| 4 | test/ | ディレクトリ | なし | 要確認 | 実験用途の可能性。不要なら削除候補 |
| 5 | _knowledge_template.md | ファイル | なし | テンプレート | 問題なし |
| 6 | _work_log_template.md | ファイル | なし | テンプレート | 問題なし |

### 所見
- 6 エントリ中、inbox/ref_* ポインターは 0 件
- ai-driven-dev-patterns/ は CLAUDE.md のリポジトリ間関係で参照されており問題なし
- _knowledge_template.md と _work_log_template.md はテンプレートファイルであり問題なし
- agency-agents/, claude-code-action/, test/ はメタ情報（用途・有効期限）の確認が必要（CLAUDE.md「参照物格納時は用途・有効期限のメタ情報を必ず記載すること」に該当）

---

## TG-010: GHA ↔ Skills ドリフト検出

### triage-gha マッピング

| チェックポイント | GHA prompt | SKILL.md | ドリフト | 重大度 |
|--------------|-----------|---------|--------|--------|
| TG タスク ID | TG-001〜TG-010 | TG-001〜TG-010 | なし | — |
| 作業フローステップ | 8 ステップ定義 | 8 ステップ定義 | なし | — |
| レポート構造セクション | 確認対象 | 確認対象 | なし | — |
| テンプレートファイル参照 | sessions/triage/_template/ | sessions/triage/_template/ | なし | — |

**判定**: ドリフトなし

### l1-auto-execute-gha マッピング

| チェックポイント | gha-execute SKILL.md | l1-manager SKILL.md | ドリフト | 重大度 |
|--------------|---------------------|---------------------|--------|--------|
| 番号付きファイル | 00〜08（9 ファイル） | 00〜09 + 02b, 00a（12 ファイル） | あり | expected |
| ワークフローステップ | template→proposal/plan/tasks→worker→evaluator→gate_review | 同等 + 壁打ち + ディスパッチログ | あり | expected |
| テンプレート参照 | sessions/initiatives/_template/ | sessions/initiatives/_template/ | なし | — |

**差異の詳細**:
- 09_cost_record.md: gha-execute 未参照 → GHA 環境ではコスト記録不要（single-agent-mode）
- 02b_dispatch_log.md: gha-execute 未参照 → GHA 環境ではディスパッチログ不要（single-agent-mode）
- 00a_wallbash_log.md: gha-execute は壁打ちフェーズ省略（wall-beating-omission）

**判定**: 検出された差異はすべて inherent_differences（想定内の差異）に該当。重大なドリフトなし。

---

## 課題起票

- 起票件数: 2 件（`07_issues.md` に起票）
- README.md 150 行超過（07_issues.md に起票済み）
- ゲートレビュー未記入施策 3 件の滞留（07_issues.md に起票済み）

## 判断・気づき

- **GHA 関連 inbox の集中**: 15 件中 6 件が GHA 関連。gha-pipeline-autorun 施策や initiative-dispatcher 施策から派生した知見が多い。gha-guideline スキルの拡充が中期的に必要
- **SC 改善提案の蓄積**: BL-101, BL-102, BL-104 と inbox 2 件が SC セッション改善に集中。統合施策として優先度を上げることを推奨
- **アーカイブ待ち 7 件の速やかな処理**: 7 件がアーカイブ可能状態。initiatives/ ディレクトリの見通しを改善するため、早期アーカイブを推奨
- **ゲートレビュー未記入 3 件**: external-repo-cleanup-on-demand, sync-worker-target-commit, triage-phase-gate-and-gha-sync は作業完了済みだがゲートレビューがテンプレートのまま。ゲート判定実施でさらに 3 件のアーカイブが可能
- **BL-100 欠番**: 採番ミスの可能性。ISS-067（BL ID 二重採番）と合わせ、BL-084（並列セッション BL ID 衝突防止）の優先度検討材料
- **高優先度課題 4 件が全て「起票」ステータス**: ISS-059, 061, 064, 068 の対応が進んでいない。特に ISS-059（シェルインジェクション）はセキュリティリスクとして早期対応が望ましい

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-19
