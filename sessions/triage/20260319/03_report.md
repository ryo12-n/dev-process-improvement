# トリアージ振り返りレポート: 2026-03-19

## サマリ

前回トリアージ（2026-03-18）から1日経過で inbox 15 件が新規蓄積（GHA 関連知見 6 件を含む）。backlog 候補 11 件、ルール反映 3 件に分類。アーカイブ待ち initiative 7 件、ゲートレビュー未記入 3 件の滞留を検出。GHA ↔ Skills 整合性は問題なし。高優先度課題 4 件が依然「起票」ステータスのまま未対応。

## Worker Set サマリ

| Set | 担当 TG タスク | 評価結果 | 備考 |
|-----|--------------|---------|------|
| set-1 | TG-001〜TG-007, TG-010（TG-008/009 スキップ） | 承認 | 軽微指摘 2 件（次回参考） |

## 走査結果

### inbox（TG-001）

| # | アイテム | 判断 | 理由 |
|---|---------|------|------|
| 1 | SC-007スキャン手順改善_括弧内包含記述の確認.md | ルール反映 | sc-collection-worker の SC-007 手順に括弧内包含検出を追加 |
| 2 | SCチェック後のアクション接続明確化.md | backlog 候補 | SC チェック結果→即時修正オプション追加。BL-101 と補完関係 |
| 3 | automation-20260318-count-definition.md | ルール反映 | automation-worker のカウント定義明確化。スキル定義への直接反映 |
| 4 | automation-20260318-integration-score.md | backlog 候補 | 統合施策のスコア算出方法定義。一定スコープあり |
| 5 | dispatcher-reject-retry-count-explicit.md | 保留 | 機能的問題なし、一貫性のみ。次回 GHA メンテナンス一括対応 |
| 6 | gha-claude-dir-write-restriction.md | backlog 候補 | GHA .claude/ 書き込み制約の文書化。ISS-068 と直結 |
| 7 | gha-constraint-check-in-proposal.md | backlog 候補 | 00_proposal テンプレートへの GHA 制約事前チェック追加 |
| 8 | gha-metadata-extraction-composite-action.md | backlog 候補 | メタデータ取得の composite action 共通化。コスト対効果要検討 |
| 9 | gha-task-division-step-name-reference.md | ルール反映 | l2-plan-worker にステップ名参照推奨ガイド追加 |
| 10 | gha-verdict-step-separation-pattern.md | backlog 候補 | gha-guideline へ verdict/dispatch ステップ分離パターン追加 |
| 11 | meta-rule-checklist-integration-proposal.md | backlog 候補 | l1-manager 固定タスクのメタルール/チェックリスト統合 |
| 12 | non-initiative-cost-tracking.md | backlog 候補 | 非 initiative セッションへのコスト追跡拡張 |
| 13 | success-criteria-grep-scope.md | backlog 候補 | 成功基準 grep スコープ制限ガイドライン |
| 14 | template-md-path-reference-check.md | backlog 候補 | rule-change-checklist にテンプレート .md パス追加 |
| 15 | template-new-file-update-pattern.md | backlog 候補 | テンプレート新設時の 5 ステップパターン固定タスク化 |

### backlog 突合（TG-002）

| BL-ID | 施策名 | ステータス | 施策化状況 | 備考 |
|-------|--------|----------|----------|------|
| BL-095 | PostToolUse hook 品質チェック統合 | 候補 | 未施策化 | |
| BL-096 | backlog エントリ記述粒度最低基準 | 候補 | 未施策化 | |
| BL-097 | BM-001 閾値段階化 | 候補 | 未施策化 | |
| BL-098 | BM レポート→backlog 実行トリガー | 候補 | 未施策化 | |
| BL-099 | .claude/templates/ 連動更新チェックリスト | 候補 | 未施策化 | inbox #15 と関連 |
| BL-100 | （欠番） | — | — | 採番ミス |
| BL-101 | SC フィードバックループ定義 | 候補 | 未施策化 | inbox #2 と補完関係 |
| BL-102 | SC インライン参照走査拡大 | 候補 | 未施策化 | |
| BL-103 | evaluator 対称性テーブル統一 | 候補 | 未施策化 | |
| BL-104 | SC-008 壊れた参照修正 | 未着手 | 施策ディレクトリ名定義済み | 高優先度 |
| BL-105 | SC-006 impl 系列追加 | 未着手 | 施策ディレクトリ名定義済み | |
| BL-106 | テンプレート構成仕様定義 | 候補 | 未施策化 | |

**検出事項**: BL-100 欠番、未採番エントリ 2 件（「SC チェック Quick Wins 一括是正」「リネーム時全文検索チェック義務化ルール追加」）、対象リポジトリ未記入 0 件。

### 課題管理 CSV（TG-003）

| ISS-ID | 優先度 | ステータス | 概要 | 対応状況 |
|--------|--------|----------|------|---------|
| ISS-059 | 高 | 起票 | GHA シェルインジェクションリスク | 未対応。セキュリティリスク |
| ISS-061 | 高 | 起票 | settings.json deny ルール非機能 | 未対応。BL-067+071 で予定 |
| ISS-064 | 高 | 起票 | テストスクリプトパス未設定 | 未対応。外部リポジトリ側 |
| ISS-068 | 高 | 起票 | GHA .claude/ 書き込み拒否 | 新規。inbox に回避手順あり |
| ISS-065 | 中 | 起票 | session-lifecycle-policy co-* 列欠落 | BL-105 で対応可能 |
| ISS-066 | 中 | 起票 | CSV/md ステータス不一致 | 自動生成信頼性問題 |
| ISS-067 | 低 | 起票 | BL ID 二重採番 | BL-084 で根本対応予定 |

### backlog 関係性分析（TG-005）

| アイテムA | アイテムB | 関係種別 | 詳細 | 提案 |
|----------|----------|---------|------|------|
| BL-104 | 未採番「SC Quick Wins」 | 重複候補 | BL-104 は Quick Wins の部分集合 | 未採番エントリを BL-104 に統合 or BL ID 採番 |
| BL-099 | inbox #15 (template-new-file) | 重複候補 | テンプレート連動更新の類似提案 | スコープ調整を検討 |
| BL-101 | inbox #2 (SCアクション接続) | 重複候補 | SC チェック結果アクションの補完関係 | inbox を BL-101 拡張提案として統合 |
| BL-095 | BL-030, BL-082 | 依存関係 | BL-095 は BL-030+082 の統合施策 | 施策化時に元エントリクローズ |
| BL-105 | ISS-065 | 依存関係 | 同根問題（lifecycle-policy 列欠落） | BL-105 で ISS-065 も併せて対応 |
| BL-101, 102, 104 + inbox #2 | — | 統合候補 | SC 改善グループ | 統合施策として実施すると効率的 |

### initiative 状態確認（TG-004）

#### アーカイブ待ち（ゲート通過済み）: 7 件

| 施策名 | 判定 |
|--------|------|
| backlog-to-issue-status-sync | アーカイブ可 |
| csv-conflict-prevention | アーカイブ可 |
| l1-manager-checklist-integration | アーカイブ可 |
| l1-manager-enhanced-planning | アーカイブ可 |
| session-cost-measurement | アーカイブ可 |
| session-lifecycle-policy-rename | アーカイブ可 |
| skill-plugin-overlap-check-rule | アーカイブ可 |

#### ゲートレビュー未記入（作業完了済み）: 3 件

| 施策名 | 状態 |
|--------|------|
| external-repo-cleanup-on-demand | ゲート判定実施でアーカイブ可能 |
| sync-worker-target-commit | ゲート判定実施でアーカイブ可能 |
| triage-phase-gate-and-gha-sync | ゲート判定実施でアーカイブ可能 |

#### 進行中: 2 件

| 施策名 | 状態 |
|--------|------|
| backlog-id-and-issue-template | 長期停滞（2026-03-14 作成、0/5 未着手） |
| impl-worker-worklog-reliability | 長期停滞（2026-03-14 作成、0/5 未着手） |

### ルール・workflow 整合性チェック（TG-006）

| 検出事項 | 重大度 | 対応 |
|---------|--------|------|
| README.md 219 行（150 行上限超過） | 中 | backlog 候補として起票検討 |
| docs/workflow.md 1067 行 | 低 | 可視化文書の性質上許容 |
| 参考資料ステータスバナー | — | 全件適正 |

### refs/ 孤立エントリ確認（TG-007）

| エントリ | 判定 | 備考 |
|---------|------|------|
| agency-agents/ | 要確認 | メタ情報確認が必要 |
| ai-driven-dev-patterns/ | 問題なし | CLAUDE.md で参照 |
| claude-code-action/ | 要確認 | メタ情報確認が必要 |
| test/ | 要確認 | 不要なら削除候補 |
| _knowledge_template.md | 問題なし | テンプレート |
| _work_log_template.md | 問題なし | テンプレート |

### GHA ↔ Skills 整合性チェック（TG-010）

| マッピングID | ドリフト | 重大度 | 備考 |
|------------|---------|--------|------|
| triage-gha | なし | — | 全チェックポイント一致 |
| l1-auto-execute-gha | あり（想定内） | INFO | single-agent-mode/wall-beating-omission に該当 |

## backlog 追加・変更案

### 追加候補

| 優先度 | 施策名 | 課題概要 | 元 inbox |
|--------|--------|---------|---------|
| 低 | SCチェック後アクション接続明確化 | SC 結果→即時修正の接続フロー定義 | #2 |
| 低 | automation 統合スコア算出定義 | AT-004 の優先度スコア算出方法 | #4 |
| 中 | GHA .claude/ 書き込み制約文書化 | ISS-068 対応。gha-guideline への追加 | #6 |
| 中 | 00_proposal GHA 制約事前チェック | 施策設計時の GHA 実行不可フラグ | #7 |
| 低 | GHA メタデータ抽出共通化 | composite action 化。コスト対効果要検討 | #8 |
| 低 | GHA verdict ステップ分離パターン | gha-guideline への追加 | #10 |
| 低 | メタルール/チェックリスト統合 | l1-manager 固定タスク再編 | #11 |
| 低 | 非 initiative コスト追跡 | triage/meta/sync 等へのコスト計測拡張 | #12 |
| 低 | 成功基準 grep スコープ制限 | grep 対象を施策スコープに限定 | #13 |
| 低 | テンプレート .md パス参照チェック | rule-change-checklist にテンプレート追加 | #14 |
| 低 | テンプレート新設 5 ステップパターン | 固定タスク化（BL-099 と調整） | #15 |

### 優先度変更候補

なし

### 削除・クローズ候補

なし（施策化済みの新規検出なし）

## 振り返り

### うまくいったこと
- 全フェーズ 1 セット逐次実行で効率的に完了（前回から1日のため適切な判断）
- GHA 整合性チェック（TG-010）でドリフトなしを確認

### 改善すべきこと
- 高優先度課題 4 件（ISS-059, 061, 064, 068）が複数回のトリアージで「起票」ステータスのまま
- ゲートレビュー未記入 3 施策の滞留

### プロセス改善の気づき
- TG-006 のスキル定義チェック対象範囲をタスク指示で明確化すべき（評価者指摘）
- TG-007 の refs/ 確認にメタ情報ファイル有無確認ステップを追加すべき（評価者知見）
- 課題管理のエスカレーション基準（N 回連続未対応でアラート）の検討余地あり

### 次回トリアージへの申し送り

- refs/ 孤立 3 件（agency-agents, claude-code-action, test）のユーザー確認結果を反映
- 保留 inbox 1 件（dispatcher-reject-retry-count-explicit.md）の再判定
- TG-006 スキル定義チェック対象範囲の明確化

**→ 申し送り事項がある場合**: `inbox/triage-handoff-20260319.md` を作成する

## 知見集約

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | TG-007 refs/ チェックにメタ情報確認ステップ追加 | set-1 評価者 | triage-worker エージェント定義 | inbox/ref_* ポインターだけでなく knowledge.md の有無と用途・有効期限メタ情報も確認 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | GHA 関連 inbox の集中傾向（15 件中 6 件） | set-1 ワーカー | gha-guideline スキルの拡充を中期的に検討すべき |
| 2 | SC 改善提案の蓄積（BL-101, 102, 104 + inbox 2 件） | set-1 ワーカー | 統合施策として優先度を上げることを推奨 |
| 3 | 高優先度課題の長期滞留パターン | set-1 評価者 | エスカレーション基準の検討余地あり |

## 課題集約

### ワーカーセット別課題件数

| Set | 課題件数 | CSV転記件数 | 備考 |
|-----|---------|-----------|------|
| set-1 | 3 件（ワーカー2 + 評価者1） | 0 件 | 既存 backlog/課題で管理可能 |

### CSV 転記判定

| # | 課題内容 | 転記判定 | 理由 |
|---|---------|---------|------|
| 1 | README.md 150 行超過 | 転記不要 | backlog 候補として管理が適切 |
| 2 | ゲートレビュー未記入 3 施策の滞留 | 転記不要 | L1 セッションでゲート判定実施を推奨 |
| 3 | refs/ メタ情報チェック不足 | 転記不要 | 知見集約のルール化候補として管理 |

## 課題起票

- 起票した課題（合計）：0 件（既存課題・backlog で管理可能なため新規 CSV 転記なし）

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-19
**レビュー依頼先**: ユーザー
**レビュー状態**: レビュー待ち
