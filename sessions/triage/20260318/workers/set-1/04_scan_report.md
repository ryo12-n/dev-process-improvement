# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox 9件分類 | 完了 |
| TG-007 | 気づきエントリ4件処理 | 完了 |
| TG-003 | CSV 概況確認 | 完了 |
| TG-004 | initiative 状態確認 | 完了 |
| TG-002 | backlog 突合確認 | 完了 |
| TG-006 | rules/workflow 整合性チェック | 完了 |
| TG-008 | session-consistency-manager 差分チェック | 完了 |
| TG-005 | backlog 関係性横断分析 | 完了 |
| TG-009 | 情報欠損リスク評価 | 完了 |
| TG-010 | GHA ↔ Skills 整合性差分チェック | 完了 |

---

## TG-001: inbox 9件の分類

| # | ファイル名 | 起票日 | 起票元 | 分類 |
|---|----------|--------|--------|------|
| 1 | backlog-entry-minimum-description.md | 2026-03-17 | BM 20260317 BM-005 | backlog候補 |
| 2 | bm-001-threshold-tiering.md | 2026-03-17 | BM 20260317 振り返り | backlog候補 |
| 3 | bm-report-to-backlog-trigger.md | 2026-03-17 | BM 20260317 振り返り | backlog候補 |
| 4 | claude-templates-update-checklist.md | 2026-03-17 | cost-effectiveness-eval-framework | backlog候補 |
| 5 | phase-worker-set-standardization.md | 2026-03-18 | SC 20260317 後のユーザー協議 | backlog候補 |
| 6 | SCチェック結果フィードバックループ定義.md | 2026-03-17 | SC 20260317 Phase 3 ワーカー知見 | backlog候補 |
| 7 | SC走査対象インライン参照拡大.md | 2026-03-17 | SC 20260317 IMP-008 | backlog候補 |
| 8 | commit-message規約l2-plan明確化.md | 2026-03-17 | SC 20260317 IMP-004/SC-007 | ルール反映候補 |
| 9 | evaluator対称性テーブル統一.md | 2026-03-17 | SC 20260317 IMP-003/SC-003 | backlog候補 |

**所見**:
- 9件全てが2026-03-17/18起票の新規エントリ
- SC（セッション一貫性チェック）初回実行からの派生が5件（#6〜#9 + #5はSC後の協議）
- BM（バックログメンテナンス）からの派生が3件（#1〜#3）
- 施策からの派生が1件（#4）
- #8（commit-message規約l2-plan明確化）は1ファイル2箇所のテキスト修正で完結するため、ルール反映として直接対応可能

---

## TG-007: 気づきエントリ4件の処理

| # | ファイル名 | 処理結果 | 理由 |
|---|----------|---------|------|
| 1 | commit-message規約l2-plan明確化.md | ルール反映候補 | commit-message.md の施策作業テーブルに l2-plan-worker/evaluator の包含関係を追記するのみ（軽微修正） |
| 2 | evaluator対称性テーブル統一.md | backlog候補 | 3ファイルへのテーブル追加。機械的だが複数ファイル変更のため施策管理推奨 |
| 3 | SCチェック結果フィードバックループ定義.md | backlog候補 | テンプレート・作業フローの構造変更。設計検討が必要 |
| 4 | SC走査対象インライン参照拡大.md | backlog候補 | エージェント定義変更。false positive リスクの検討が必要 |

**所見**:
- #1 はルール反映として直接修正可能（TG-001 の分類と同じ結論）
- #2〜#4 は backlog 経由での施策化が適切

---

## TG-003: CSV 概況確認

### ステータス分布

| ステータス | 件数 |
|-----------|------|
| クローズ | 30 |
| 起票 | 31 |
| 方針確定 | 1 |
| **合計** | **62** |

### 方針確定エントリ

| ID | タイトル | 備考 |
|----|---------|------|
| ISS-031 | inbox/backlog が ai-driven-dev-patterns と dev-process-improvement の両方に存在する二重構造 | 前回から変化なし |

### 最近の起票（2026-03-17以降）

| ID | タイトル | 起票日 |
|----|---------|--------|
| ISS-066 | backlog.csv / entries のステータス不一致4件 | 2026-03-17 |
| ISS-067 | BL-076/077 の二重採番 | 2026-03-17 |

**所見**:
- タスク指示では「起票36件」だが、実測は31件。マネージャーの事前調査時点からCSVが更新された可能性（5件がクローズに移動）
- ISS-066（CSV/エントリ不一致）とISS-067（BL ID二重採番）は backlog 運用の品質に関わる課題で、BL-084（ID衝突防止）の施策化が待たれる
- 対応方針案: 起票31件は現状維持。方針確定1件（ISS-031）は継続的に検討

---

## TG-004: initiative 状態確認

### 進行中施策（2件）

| 施策名 | 最終ファイル | 状態 | 備考 |
|--------|------------|------|------|
| backlog-id-and-issue-template | 02_tasks.md | タスク作成済み・ワーカー未着手 | TASK-001〜005 定義済み |
| impl-worker-worklog-reliability | 02_tasks.md | タスク作成済み・ワーカー未着手 | T-001〜005 定義済み |

### ゲート未完了施策（3件）

| 施策名 | 08_gate_review 状態 | 作業状態 | 推奨アクション |
|--------|-------------------|---------|--------------|
| sync-worker-target-commit | テンプレートのまま | 04_work_report が未記入 | 作業完了確認 → ゲート判定実施 |
| triage-phase-gate-and-gha-sync | テンプレートのまま | 04_work_report が未記入 | 作業完了確認 → ゲート判定実施 |
| external-repo-cleanup-on-demand | テンプレートのまま | 04_work_report 記入済み（作業完了） | ゲート判定のみ実施 |

### アーカイブ待ち施策（6件）

| 施策名 | ゲート判定結果 | 推奨アクション |
|--------|-------------|--------------|
| backlog-to-issue-status-sync | 全フェーズ PASS | _archive/ へ移動 |
| csv-conflict-prevention | 全フェーズ PASS | _archive/ へ移動 |
| l1-manager-enhanced-planning | 記録完了 | _archive/ へ移動 |
| session-cost-measurement | 記録完了 | _archive/ へ移動 |
| session-lifecycle-policy-rename | 記録完了 | _archive/ へ移動 |
| skill-plugin-overlap-check-rule | 全フェーズ PASS | _archive/ へ移動 |

**所見**:
- アーカイブ待ち6件は速やかに _archive/ へ移動すべき（initiatives/ の見通し改善）
- ゲート未完了3件のうち external-repo-cleanup-on-demand は作業完了済みなのでゲート判定のみ
- sync-worker-target-commit と triage-phase-gate-and-gha-sync は作業レポートも未記入のため、作業状態の確認が必要

---

## TG-002: backlog 施策化済み8件の突合確認

### 施策化済みエントリ突合

| BL-ID | ステータス(CSV) | 施策ディレクトリ | 施策所在 | 整合性 |
|-------|---------------|----------------|---------|--------|
| BL-002 | 完了 | dev-workflow-detail-l1-ref-review | _archive/ | OK |
| BL-004 | 完了 | harness-engineering-brushup | _archive/ | OK |
| BL-010 | 完了 | backlog-template-legend-enhancement | _archive/ | OK |
| BL-012 | 完了 | knowledge-table-origin-column-backport | _archive/ | OK |
| BL-020 | 進行中 | sync-worker-target-commit | initiatives/ | OK |
| BL-031 | 完了 | automation-manager-session | _archive/ | OK |
| BL-064 | 完了 | skill-plugin-overlap-check-rule | initiatives/ | 要確認: アーカイブ未移動 |
| BL-072 | 完了 | session-artifacts-structure-refactor | _archive/ | OK |

### 対象リポジトリ未記入チェック
- **全件記入済み**。空欄なし

### 削除・クローズ候補
- 完了済み7件（BL-002/004/010/012/031/064/072）は backlog エントリとしての役割を終えている
- ただし ISS-066 で CSV とエントリ間のステータス不一致が報告されている（BL-004, BL-010, BL-012, BL-072 の CSV ステータスが「候補」のまま）
- 削除よりも先に ISS-066 の解消（CSV 自動生成の整合性修正）が必要

---

## TG-006: rules/workflow 整合性チェック

### session-consistency-manager 変更の docs/workflow.md 反映確認

| チェック項目 | 結果 | 詳細 |
|------------|------|------|
| SKILL.md パス変更 → workflow.md 連動 | OK | コミット77cb07dで同時更新。Phase ディレクトリパス一致 |
| agents パス変更 → workflow.md 連動 | OK | workflow.md のSCセクション内パスが全て更新済み |
| テンプレート再配置 → workflow.md 記述 | OK | テンプレート構造の記述は変更不要（詳細レベルでは記載なし） |

### README 整合性チェック

| チェック項目 | 結果 | 詳細 |
|------------|------|------|
| ディレクトリ構成ツリー | OK | session-consistency-manager 記載あり（L47-48） |
| セッション種別テーブル | OK | L111 に記載あり |
| スキルディレクトリテーブル | OK | L195 に記載あり |
| 行数 | 注意 | 219行（推奨150行超過だが、構造的に分割済みで問題なし） |

### 参考資料ステータスチェック

| ファイル | ステータスバナー | 統合状態 | CLAUDE.md テーブル整合 |
|---------|---------------|---------|---------------------|
| coordination-protocol-guideline.md | あり | 一部統合済み | OK |
| git-worktree-guideline.md | あり | 一部統合済み | OK |

**所見**:
- session-consistency-manager の変更に伴う docs/workflow.md の連動更新は適切に実施済み
- 乖離なし

---

## TG-008: session-consistency-manager 関連変更の差分チェック

### 対象コミット

| コミット | 内容 | 影響範囲 |
|---------|------|---------|
| 6199b56 | SCチェック初回実行（sessions/ 成果物追加） | スキル定義への影響なし |
| 77cb07d | ワーカーセットを Phase ディレクトリ配下に再配置 | SKILL.md + agents 4件 + workflow.md + テンプレート |

### 77cb07d の変更詳細

| 変更対象 | 変更内容 | 整合性 |
|---------|---------|--------|
| SKILL.md | パス参照15箇所を phase-N-xxx/workers/set-1/ に更新 | OK |
| sc-collection-worker.md | 担当ファイルテーブル6箇所更新 | OK |
| sc-analysis-worker.md | 担当ファイルテーブル7箇所 + Phase 1参照1箇所更新 | OK |
| sc-proposal-worker.md | 担当ファイルテーブル7箇所 + Phase 2参照1箇所更新 | OK |
| sc-evaluator.md | フェーズマッピングテーブル3行 + パラメータ説明2箇所更新 | OK |
| docs/workflow.md | SCフローセクション12行更新 | OK |
| テンプレート | phase-1: リネーム、phase-2/3: 新規作成（各7ファイル） | OK |
| inbox | phase-worker-set-standardization.md 新規追加 | OK（TG-001で分類済み） |

**所見**:
- パス参照の一括更新は整合性がとれている。漏れなし
- ロジック変更はなく、ディレクトリ構造の再編のみ

---

## TG-005: backlog 関係性横断分析

### 重複・類似候補グループ

| グループ | エントリ | 関係性 | 統合推奨度 |
|---------|---------|--------|-----------|
| Hook基盤 | BL-029, BL-030, BL-067, BL-082 | PreToolUse/PostToolUse hook の4施策。基盤整備として統合可能 | 中（個別実装も可だが基盤が共通） |
| セキュリティ二重防御 | BL-067, BL-071 | hook + sandbox の二重防御設計。実装順序の依存あり | 低（設計上の意図的分離） |
| コンテキストコスト削減 | BL-008, BL-068, BL-070 | 長文rules最適化 + CLAUDE.md縮小 + path-scoped rules。BL-070がBL-068の前提 | 中（実装順序: BL-070 → BL-068 → BL-008） |
| GHA自動化拡大 | BL-055, BL-057 | BM自動化 + メタ認知自動化。同パターンで並行可能 | 低（独立実装で問題なし） |
| sync改善 | BL-050, BL-051 | 外部リポ管理 + 同期対象リスト。補完関係 | 中（BL-051がBL-050を含む可能性） |

### 依存関係

| 先行 | 後続 | 依存の種類 |
|------|------|-----------|
| BL-070 | BL-068 | path-scoped rules 導入が import 縮小の前提 |
| BL-067 | BL-071 | hook 実装が sandbox 有効化の前提（二重防御設計） |
| BL-084 | ISS-066/067 | BL ID衝突防止 → 既存二重採番の解消 |

---

## TG-009: 情報欠損リスク評価

### 削除・クローズ候補の評価

| BL-ID | 施策アーカイブ | 情報欠損リスク | 備考 |
|-------|-------------|-------------|------|
| BL-002 | _archive/dev-workflow-detail-l1-ref-review | 低 | 施策詳細はアーカイブに保存済み |
| BL-004 | _archive/harness-engineering-brushup | 低 | 同上 |
| BL-010 | _archive/backlog-template-legend-enhancement | 低 | 同上 |
| BL-012 | _archive/knowledge-table-origin-column-backport | 低 | 同上 |
| BL-031 | _archive/automation-manager-session | 低 | 同上 |
| BL-064 | initiatives/skill-plugin-overlap-check-rule（アーカイブ待ち） | 低 | アーカイブ移動後に削除可 |
| BL-072 | _archive/session-artifacts-structure-refactor | 低 | 同上 |

**所見**:
- 全7件とも施策アーカイブに詳細が残存しており、backlog エントリ削除による情報欠損リスクは低い
- ただし ISS-066（CSV/エントリ不一致）の解消を先に行うべき。generate-csvs.py が .md のステータスを正しくCSVに反映できるか確認が必要

---

## TG-010: GHA ↔ Skills 整合性差分チェック

### gha-skills-mapping.yml マッピング状況

| マッピングID | GHA ソース | スキルソース | 状態 |
|------------|-----------|------------|------|
| triage-gha | .github/prompts/triage.md | triage-manager/ | 登録済み |
| l1-auto-execute-gha | gha-execute/SKILL.md | l1-manager/ | 登録済み |

### GHA スキルのマッピング網羅性

| GHA スキル | マッピング有無 | 重大度 |
|-----------|-------------|--------|
| gha-close | なし | 中（BL-080 で起票済み） |
| gha-execute | あり | - |
| gha-guideline | なし | 低（補助的スキル） |
| gha-question | なし | 中（BL-080 で起票済み） |
| gha-test | なし | 低（テスト用） |
| gha-wallbash | なし | 中（BL-080 で起票済み） |

### session-consistency-manager 変更の GHA 影響

- session-consistency-manager は GHA ワークフローなし（CLI専用セッション）
- 77cb07d の変更は GHA に影響なし
- マッピング追加不要

**所見**:
- BL-080（gha-wallbash/close/question のマッピング追加）の対応が必要（既知）
- session-consistency-manager の変更による GHA 側のドリフトなし

---

## 課題起票

- 起票件数: 0 件（`07_issues.md` に起票）

既知の課題（ISS-066, ISS-067, BL-080）でカバーされており、新規課題の起票は不要。

---

## 判断・気づき

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|------------------|------|
| 1 | commit-message.md に l2-plan-worker/evaluator の包含関係を追記 | .claude/rules/commit-message.md | inbox「commit-message規約l2-plan明確化.md」の内容。L2-worker に「(l2-plan-worker を含む)」、L2-evaluator に「(l2-plan-evaluator を含む)」を追記するのみ |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | アーカイブ待ち6件の滞留 | initiatives/ に完了済み施策が6件残存。定期的なアーカイブ移動の仕組み（またはトリアージアクションへの組み込み）を検討 |
| 2 | CSV 起票件数の事前調査との差異 | マネージャー事前調査では36件、実測31件。事前調査〜ワーカー実行間のCSV更新で差異が発生。軽微だが認識しておく |
| 3 | SC 初回実行からの inbox 大量派生 | SCチェック1回で inbox 5件が派生。定期実行時の inbox 流入量に注意 |
| 4 | hook系施策4件の基盤共通性 | BL-029/030/067/082 は PreToolUse/PostToolUse hook の基盤を共有。統合施策化で効率化可能 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-18
