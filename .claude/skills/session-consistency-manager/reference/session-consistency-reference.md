# Session Consistency Reference

> **Snapshot Date**: 2026-03-19
> **Source**: `.claude/skills/` 配下のセッション定義、`sessions/*/_template/` 配下のテンプレート
> **Freshness**: 初回収集 2026-03-17。2回目収集 2026-03-19（差分なし）。

---

## 1. SC-001: SKILL.md 構造準拠

### 準拠基準

session-flow-policy §2 の必須セクション:
- あなたの役割
- 作業フロー
- やること
- やらないこと

オーケストレーション関連の必須記載:
- ワーカーのディスパッチ手順
- 成果物の確認観点
- 結果の集約手順
- 担当ファイル

### マネージャー SKILL.md 一覧

| マネージャー | パス | 必須セクション | オーケストレーション | 備考 |
|-------------|------|--------------|-------------------|------|
| l1-manager | `.claude/skills/l1-manager/SKILL.md` | 4/4 (役割,フロー,やること,やらないこと) | 4/4 (ディスパッチ,確認,集約,担当ファイル) | 完全準拠 |
| triage-manager | `.claude/skills/triage-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| metacognition-manager | `.claude/skills/metacognition-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| sync-manager | `.claude/skills/sync-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| backlog-maintenance-manager | `.claude/skills/backlog-maintenance-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| automation-manager | `.claude/skills/automation-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| config-optimizer-manager | `.claude/skills/config-optimizer-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| session-consistency-manager | `.claude/skills/session-consistency-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| l1-impl-manager | `.claude/skills/l1-impl-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |

---

## 2. SC-002: エージェント定義構造準拠

### 準拠基準

session-flow-policy §3 の必須セクション:
- あなたの役割
- 作業フロー
- やること
- やらないこと
- 担当ファイル
- 停止ルール

### エージェント定義一覧

| エージェント | パス | 必須セクション（6項目） | 壁打ちフェーズ | YAML name ケバブケース | 備考 |
|-------------|------|---------------------|-------------|---------------------|------|
| l2-worker | `l1-manager/agents/l2-worker.md` | 6/6 | あり | OK (l2-worker) | 完全準拠 |
| l2-evaluator | `l1-manager/agents/l2-evaluator.md` | 6/6 | あり | OK (l2-evaluator) | 完全準拠 |
| l2-plan-worker | `l1-manager/agents/l2-plan-worker.md` | 6/6 | あり | OK (l2-plan-worker) | 完全準拠 |
| l2-plan-evaluator | `l1-manager/agents/l2-plan-evaluator.md` | 6/6 | あり | OK (l2-plan-evaluator) | 完全準拠 |
| triage-worker | `triage-manager/agents/triage-worker.md` | 6/6 | あり | OK (triage-worker) | 完全準拠 |
| triage-evaluator | `triage-manager/agents/triage-evaluator.md` | 6/6 | あり | OK (triage-evaluator) | 完全準拠 |
| metacognition-worker | `metacognition-manager/agents/metacognition-worker.md` | 6/6 | あり | OK (metacognition-worker) | 完全準拠 |
| metacognition-evaluator | `metacognition-manager/agents/metacognition-evaluator.md` | 6/6 | あり | OK (metacognition-evaluator) | 完全準拠 |
| sync-worker | `sync-manager/agents/sync-worker.md` | 6/6 | あり | OK (sync-worker) | 完全準拠 |
| sync-evaluator | `sync-manager/agents/sync-evaluator.md` | 6/6 | あり | OK (sync-evaluator) | 完全準拠 |
| backlog-maintenance-worker | `backlog-maintenance-manager/agents/backlog-maintenance-worker.md` | 6/6 | あり | OK (backlog-maintenance-worker) | 完全準拠 |
| backlog-maintenance-evaluator | `backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md` | 6/6 | あり | OK (backlog-maintenance-evaluator) | 完全準拠 |
| automation-worker | `automation-manager/agents/automation-worker.md` | 6/6 | あり | OK (automation-worker) | 完全準拠 |
| automation-evaluator | `automation-manager/agents/automation-evaluator.md` | 6/6 | あり | OK (automation-evaluator) | 完全準拠 |
| config-collection-worker | `config-optimizer-manager/agents/config-collection-worker.md` | 6/6 | あり | OK (config-collection-worker) | 完全準拠 |
| config-analysis-worker | `config-optimizer-manager/agents/config-analysis-worker.md` | 6/6 | あり | OK (config-analysis-worker) | 完全準拠 |
| config-proposal-worker | `config-optimizer-manager/agents/config-proposal-worker.md` | 6/6 | あり | OK (config-proposal-worker) | 完全準拠 |
| config-optimizer-evaluator | `config-optimizer-manager/agents/config-optimizer-evaluator.md` | 6/6 | あり | OK (config-optimizer-evaluator) | 完全準拠 |
| investigation-worker | `l1-impl-manager/agents/investigation-worker.md` | 6/6 | あり | OK (investigation-worker) | 完全準拠 |
| design-worker | `l1-impl-manager/agents/design-worker.md` | 6/6 | あり | OK (design-worker) | 完全準拠 |
| impl-plan-worker | `l1-impl-manager/agents/impl-plan-worker.md` | 6/6 | あり | OK (impl-plan-worker) | 完全準拠 |
| impl-worker | `l1-impl-manager/agents/impl-worker.md` | 6/6 | あり | OK (impl-worker) | 完全準拠 |
| impl-evaluator | `l1-impl-manager/agents/impl-evaluator.md` | 6/6 | あり | OK (impl-evaluator) | 完全準拠 |
| sc-collection-worker | `session-consistency-manager/agents/sc-collection-worker.md` | 6/6 | あり | OK (sc-collection-worker) | 完全準拠 |
| sc-analysis-worker | `session-consistency-manager/agents/sc-analysis-worker.md` | 6/6 | あり | OK (sc-analysis-worker) | 完全準拠 |
| sc-proposal-worker | `session-consistency-manager/agents/sc-proposal-worker.md` | 6/6 | あり | OK (sc-proposal-worker) | 完全準拠 |
| sc-evaluator | `session-consistency-manager/agents/sc-evaluator.md` | 6/6 | あり | OK (sc-evaluator) | 完全準拠 |

---

## 3. SC-003: Worker ↔ Evaluator 対称性

### 準拠基準

session-flow-policy §3.2 の対称性要件:
- 壁打ちフェーズ
- 作業/評価計画
- レポート
- 知見記録セクション
- 課題起票手段
- 停止ルール

### ペアリング対称性マトリクス

| マネージャー | Worker(s) | Evaluator | 壁打ち | 計画 | レポート | 知見記録 | 課題起票 | 停止ルール | 対称性テーブル |
|-------------|-----------|-----------|--------|------|---------|---------|---------|-----------|-------------|
| l1-manager | l2-worker | l2-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:なし |
| l1-manager | l2-plan-worker | l2-plan-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:あり |
| l1-impl-manager | investigation-worker, design-worker, impl-plan-worker, impl-worker | impl-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:あり |
| triage-manager | triage-worker | triage-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:なし |
| metacognition-manager | metacognition-worker | metacognition-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:なし |
| sync-manager | sync-worker | sync-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:あり |
| backlog-maintenance-manager | backlog-maintenance-worker | backlog-maintenance-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:あり |
| automation-manager | automation-worker | automation-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:あり |
| config-optimizer-manager | config-collection/analysis/proposal-worker | config-optimizer-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:あり |
| session-consistency-manager | sc-collection/analysis/proposal-worker | sc-evaluator | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | W:あり E:あり | E:あり |

---

## 4. SC-004: テンプレート ↔ エージェント担当ファイル整合

### セッションテンプレート一覧

| セッションタイプ | テンプレートパス | ファイル数 | ファイル一覧 |
|----------------|---------------|----------|------------|
| initiatives | `sessions/initiatives/_template/` | 13 | 00_proposal, 00a_wallbash_log, 01_plan, 02_tasks, 02a_task_division, 03_work_log, 03_work_log_W_template, 04_work_report, 05_eval_plan, 06_eval_report, 07_issues, 07_issues_W_template, 08_gate_review |
| impl | `sessions/impl/_template/` | 6+phase dirs | 00_proposal, 01_plan, 02_impl_design, 07_issues, 07_issues_W_template, 08_gate_summary + phase-1〜4 |
| triage | `sessions/triage/_template/` | 5+workers | 00_pre_investigation, 01_plan, 02_dispatch_log, 03_report, 04_gate_review + workers/ |
| metacognition | `sessions/metacognition/_template/` | 5+workers | 00_pre_investigation, 01_plan, 02_dispatch_log, 03_report, 04_gate_review + workers/ |
| sync | `sessions/sync/_template/` | 9 | 00_pre_investigation, 01_plan, 02_dispatch_log, 03_work_log, 04_sync_report, 05_eval_plan, 06_eval_report, 07_issues, 08_gate_review |
| backlog-maintenance | `sessions/backlog-maintenance/_template/` | 5+workers | 00_pre_investigation, 01_plan, 02_dispatch_log, 03_report, 04_gate_review + workers/ |
| automation | `sessions/automation/_template/` | 5+workers | 00_pre_investigation, 01_plan, 02_dispatch_log, 03_report, 04_gate_review + workers/ |
| config-optimization | `sessions/config-optimization/_template/` | 5+phase+workers | 00_pre_investigation, 01_plan, 02_dispatch_log, 03_report, 04_gate_review + phase-1〜3/ + workers/ |
| session-consistency | `sessions/session-consistency/_template/` | 5+phase+workers | 00_pre_investigation, 01_plan, 02_dispatch_log, 03_report, 04_gate_review + phase-1〜3/ + workers/ |

### テンプレート ↔ 担当ファイル突合結果

| セッションタイプ | テンプレートのみ | 担当ファイルのみ | 一致 | 備考 |
|----------------|---------------|----------------|------|------|
| initiatives (l2-worker) | 00a_wallbash_log, 02a_task_division, 03_work_log_W_template, 05_eval_plan, 06_eval_report, 07_issues_W_template, 08_gate_review | issues/entries/ | 02_tasks, 03_work_log, 03_work_log_W, 04_work_report, 07_issues, 07_issues_W | Worker は自分の担当ファイルのみ操作。テンプレートにはマネージャー・評価者のファイルも含む |
| initiatives (l2-evaluator) | 00_proposal, 00a_wallbash_log, 02a_task_division, 02_tasks(read), 03_work_log, 03_work_log_W_template, 07_issues_W_template, 08_gate_review | issues/entries/, refs/agency-agents/ | 01_plan(read), 04_work_report(read), 05_eval_plan, 06_eval_report, 07_issues | 正常。evaluator は work_report を読み取り、eval 成果物を作成 |
| triage (worker) | — | inbox/*.md, backlog/entries/ | 01_tasks, 02_scan_plan, 03_work_log, 04_scan_report, 07_issues | ワーカーセット内テンプレートは workers/_template/ で別管理 |
| sync (worker) | 00_pre_investigation, 02_dispatch_log, 05_eval_plan, 06_eval_report, 08_gate_review | — | 01_plan(read), 03_work_log, 04_sync_report, 07_issues | 正常。テンプレートにはマネージャー・評価者のファイルも含む |

---

## 5. SC-005: manager-common-policy 準拠

### 参照パターン一覧

| §セクション | 内容 | 参照すべきマネージャー | 備考 |
|------------|------|---------------------|------|
| §2 | ワーカーディスパッチパターン | 全マネージャー | |
| §3 | 成果物確認観点 | 全マネージャー | |
| §4 | ゲート判定基準 | 全マネージャー | |
| §5 | 知見集約手順 | 全マネージャー | |
| §6 | 課題集約手順 | 全マネージャー | |
| §7 | 差し戻し手順 | 全マネージャー | |
| §8 | セッションライフサイクル todo 登録 | 全マネージャー | |
| §10 | ドメインエージェント参照 | l1-manager, l1-impl-manager のみ | 任意適用 |

### マネージャー別参照状況

| マネージャー | §2 | §3 | §4 | §5 | §6 | §7 | §8 | §10 | 備考 |
|-------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|------|
| l1-manager | OK | OK | OK | OK | OK | OK | OK | OK | 全セクション参照済み |
| triage-manager | OK | OK | OK | OK | OK | OK | OK | — | §10 は任意（適用なし） |
| metacognition-manager | OK | OK | OK | OK | OK | OK | OK | — | §10 は任意（適用なし） |
| sync-manager | OK | OK | OK | OK | OK | OK | OK | — | §10 は任意（適用なし） |
| backlog-maintenance-manager | OK | OK | OK | OK | OK | OK | OK | — | §10 は任意（適用なし） |
| automation-manager | OK | OK | OK | OK | OK | OK | OK | — | §10 は任意（適用なし） |
| config-optimizer-manager | OK | OK | OK | OK | OK | OK | OK | — | §10 は任意（適用なし） |
| session-consistency-manager | OK | OK | OK | OK | OK | OK | OK | — | §1 も参照（適用対象テーブル確認） |
| l1-impl-manager | OK | OK | OK | OK | OK | OK | OK | OK | 全セクション参照済み |

---

## 6. SC-006: session-lifecycle-policy 適用マトリクス整合

### マトリクス列（セッションタイプ）一覧

| マトリクス上の列名 | 対応するセッション定義 | 存在確認 | 備考 |
|------------------|---------------------|---------|------|
| L1-manager | `.claude/skills/l1-manager/SKILL.md` | 存在 | |
| L2-plan-worker | `l1-manager/agents/l2-plan-worker.md` | 存在 | |
| L2-plan-evaluator | `l1-manager/agents/l2-plan-evaluator.md` | 存在 | |
| L2-worker | `l1-manager/agents/l2-worker.md` | 存在 | |
| L2-evaluator | `l1-manager/agents/l2-evaluator.md` | 存在 | |
| impl-manager | `.claude/skills/l1-impl-manager/SKILL.md` | 存在 | |
| impl-worker (Ph1-3) | `l1-impl-manager/agents/investigation-worker.md` 等 | 存在 | |
| impl-worker (Ph4) | `l1-impl-manager/agents/impl-worker.md` | 存在 | |
| impl-evaluator | `l1-impl-manager/agents/impl-evaluator.md` | 存在 | |
| triage-manager | `.claude/skills/triage-manager/SKILL.md` | 存在 | |
| triage-worker | `triage-manager/agents/triage-worker.md` | 存在 | |
| triage-evaluator | `triage-manager/agents/triage-evaluator.md` | 存在 | |
| meta-manager | `.claude/skills/metacognition-manager/SKILL.md` | 存在 | |
| meta-worker | `metacognition-manager/agents/metacognition-worker.md` | 存在 | |
| meta-evaluator | `metacognition-manager/agents/metacognition-evaluator.md` | 存在 | |
| sync-manager | `.claude/skills/sync-manager/SKILL.md` | 存在 | |
| sync-worker | `sync-manager/agents/sync-worker.md` | 存在 | |
| sync-evaluator | `sync-manager/agents/sync-evaluator.md` | 存在 | |
| bm-manager | `.claude/skills/backlog-maintenance-manager/SKILL.md` | 存在 | |
| bm-worker | `backlog-maintenance-manager/agents/backlog-maintenance-worker.md` | 存在 | |
| bm-evaluator | `backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md` | 存在 | |
| auto-manager | `.claude/skills/automation-manager/SKILL.md` | 存在 | |
| auto-worker | `automation-manager/agents/automation-worker.md` | 存在 | |
| auto-evaluator | `automation-manager/agents/automation-evaluator.md` | 存在 | |
| co-manager | `.claude/skills/config-optimizer-manager/SKILL.md` | 存在 | |
| co-worker | `config-optimizer-manager/agents/config-*-worker.md` | 存在 | 3ワーカー（collection, analysis, proposal） |
| co-evaluator | `config-optimizer-manager/agents/config-optimizer-evaluator.md` | 存在 | |
| sc-manager | `.claude/skills/session-consistency-manager/SKILL.md` | 存在 | |
| sc-worker | `session-consistency-manager/agents/sc-*-worker.md` | 存在 | 3ワーカー（collection, analysis, proposal） |
| sc-evaluator | `session-consistency-manager/agents/sc-evaluator.md` | 存在 | |

### §1.3 記録先ファイル対応

| セッション系統 | マトリクス記載 | 実態 | 整合 | 備考 |
|-------------|-------------|------|------|------|
| イニシアティブ系 | 03_work_log, 04_work_report, 05_eval_plan, 06_eval_report, 07_issues, 08_gate_review | テンプレート一致 | OK | |
| トリアージ系 | 02_scan_plan, 03_work_log, 04_scan_report, 05_eval_plan, 06_eval_report, 07_issues, 00_pre_investigation, 03_report, 04_gate_review | テンプレート一致 | OK | |
| メタ認知系 | 同トリアージ系 | テンプレート一致 | OK | |
| 同期系 | 03_work_log, 04_sync_report, 05_eval_plan, 06_eval_report, 07_issues, 00_pre_investigation, 08_gate_review | テンプレート一致 | OK | |
| バックログメンテナンス系 | 同トリアージ系 | テンプレート一致 | OK | |
| オートメーション系 | 同トリアージ系 | テンプレート一致 | OK | |
| セッション一貫性系 | 同トリアージ系 | テンプレート一致 | OK | |

---

## 7. SC-007: commit-message 規約カバレッジ

### セッション種別テーブル

| session-type | 登録済み | 対応するセッション定義 | 備考 |
|-------------|---------|---------------------|------|
| L1 | OK | l1-manager | |
| L2-worker | OK | l2-worker | |
| L2-evaluator | OK | l2-evaluator | |
| triage-mgr | OK | triage-manager | |
| triage-worker | OK | triage-worker | |
| triage-eval | OK | triage-evaluator | |
| meta-mgr | OK | metacognition-manager | |
| meta-worker | OK | metacognition-worker | |
| meta-eval | OK | metacognition-evaluator | |
| sync | OK | fork-sync (git同期) | |
| sync-mgr | OK | sync-manager | |
| sync-worker | OK | sync-worker | |
| sync-eval | OK | sync-evaluator | |
| bm-mgr | OK | backlog-maintenance-manager | |
| bm-worker | OK | backlog-maintenance-worker | |
| bm-eval | OK | backlog-maintenance-evaluator | |
| auto-mgr | OK | automation-manager | |
| auto-worker | OK | automation-worker | |
| auto-eval | OK | automation-evaluator | |
| impl-mgr | OK | l1-impl-manager | |
| impl-worker | OK | impl-worker | |
| impl-evaluator | OK | impl-evaluator | |
| co-mgr | OK | config-optimizer-manager | |
| co-worker | OK | config-collection/analysis/proposal-worker | |
| co-eval | OK | config-optimizer-evaluator | |
| sc-mgr | OK | session-consistency-manager | |
| sc-worker | OK | sc-collection/analysis/proposal-worker | |
| sc-eval | OK | sc-evaluator | |
| maintenance | OK | 保守作業 | |

### 未登録セッションタイプ

なし。全セッションタイプが登録済み。

> **備考**: l2-plan-worker は L2-worker に、l2-plan-evaluator は L2-evaluator にそれぞれ包含されている（commit-message.md 37-38行目の括弧内包含記述「l2-plan-worker を含む」「l2-plan-evaluator を含む」による）。

---

## 8. SC-008: 関連ファイル一覧の相互参照整合

### 参照マトリクス

全9マネージャー SKILL.md および全27エージェント定義に「関連ファイル一覧」セクションが存在する。

| 参照元カテゴリ | 件数 | 関連ファイル一覧あり | 備考 |
|-------------|------|------------------|------|
| マネージャー SKILL.md | 9 | 9/9 | 全件あり |
| エージェント定義 | 27 | 27/27 | 全件あり |
| ポリシー SKILL.md | 3 (session-flow, session-lifecycle, manager-common) | 3/3 | 全件あり |

### 主要な参照パターン

| 参照元 | 参照先 | 逆参照 | 参照先実在 | 備考 |
|--------|--------|--------|----------|------|
| l1-manager/SKILL.md | agents/l2-worker.md | あり | OK | 双方向参照 |
| l1-manager/SKILL.md | agents/l2-evaluator.md | あり | OK | 双方向参照 |
| l1-manager/SKILL.md | agents/l2-plan-worker.md | あり | OK | 双方向参照 |
| l1-manager/SKILL.md | agents/l2-plan-evaluator.md | あり | OK | 双方向参照 |
| l1-manager/SKILL.md | manager-common-policy/SKILL.md | あり | OK | 双方向参照 |
| l1-manager/SKILL.md | session-flow-policy/SKILL.md | なし | OK | 片方向参照（session-flow は多数の参照元を持つ） |
| l1-manager/SKILL.md | session-lifecycle-policy/SKILL.md | あり | OK | 双方向参照 |
| triage-manager/SKILL.md | agents/triage-worker.md | あり | OK | 双方向参照 |
| triage-manager/SKILL.md | agents/triage-evaluator.md | あり | OK | 双方向参照 |
| sync-manager/SKILL.md | agents/sync-worker.md | あり | OK | 双方向参照 |
| sync-manager/SKILL.md | agents/sync-evaluator.md | あり | OK | 双方向参照 |
| l2-plan-evaluator.md | `.claude/skills/triage-standard-policy/SKILL.md` | — | NG | 旧名称参照。正しくは session-lifecycle-policy |
| l2-plan-worker.md | `.claude/skills/triage-standard-policy/SKILL.md` | — | NG | 旧名称参照。正しくは session-lifecycle-policy |

### 壊れた参照

| 参照元 | 参照先（不在） | 備考 |
|--------|-------------|------|
| `l1-manager/agents/l2-plan-evaluator.md` (112行目, 198行目) | `.claude/skills/triage-standard-policy/SKILL.md` | 旧名称。2026-03-17 に session-lifecycle-policy にリネーム済み。参照先を更新すべき |
| `l1-manager/agents/l2-plan-worker.md` (195行目) | `.claude/skills/triage-standard-policy/SKILL.md` | 同上 |

---

## Changelog

| 日付 | 変更内容 |
|------|---------|
| 2026-03-17 | 初回収集。全8ターゲット（SC-001〜SC-008）の情報を記録。9マネージャー SKILL.md、27エージェント定義、9テンプレートディレクトリを走査。SC-008 で壊れた参照2件を検出（l2-plan-worker, l2-plan-evaluator の triage-standard-policy 参照）。SC-007 で未登録の可能性がある session-type 2件を検出（l2-plan-worker, l2-plan-evaluator）。 |
| 2026-03-19 | 2回目収集。全8ターゲットを再走査。前回スナップショットからの差分なし。壊れた参照2件（l2-plan-worker, l2-plan-evaluator）は依然として未修正。SC-008 の壊れた参照の行番号を詳細化（l2-plan-evaluator: 112行目, 198行目、l2-plan-worker: 195行目）。 |

---
**最終更新者**: sc-collection-worker
**最終更新日**: 2026-03-19
