---
name: session-lifecycle-policy
description: 'セッションタイプ横断のライフサイクルパターン・ペアリング要件を定義するガイドライン'
user-invocable: false
---
# セッションライフサイクルポリシーガイドライン

> **このファイルの位置づけ**
> セッションタイプ間で共通するライフサイクルパターン・ペアリング要件を定義する。
> `.claude/skills/` 配下のスキル・エージェント定義が個々のルールの正の情報源であり、本ガイドラインはそれらの横断的な整合性を担保するための基準文書である。
> TG-008 チェックリストは `triage-manager/SKILL.md` に統合済み。

---

## 1. 標準ライフサイクルパターン

各セッションタイプが経るべきライフサイクルステージと、その必須要素を定義する。

### 1.1 ステージ定義と必須要素

| ステージ | 必須要素 | 説明 |
|---------|---------|------|
| **壁打ち** | 理解のサマリー（目的・スコープ・完了条件）、前提条件チェック、不明点の列挙 | 作業着手前にタスク理解と環境確認を行い、記録する |
| **計画** | 実施/評価計画の作成、タスク順序・依存関係の明記 | マネージャーが立案するか、ワーカー/評価者が自身の作業計画を記載する |
| **実施（作業履歴）** | タイムスタンプ付き作業ログ、タスクID・状態・作業内容の記録 | 作業の追跡可能性を担保する |
| **実施（課題起票）** | 課題の構造化記録（種別・内容・対応方針案）、起票先の明示 | 発見した課題を適切なバッファ（07_issues.md または CSV）に記録する |
| **実施（気づき記録）** | 「ルール化候補」と「参考情報」の分類テーブル | 作業中の知見をゲート判定時の横展開に活用できる形で記録する |
| **レポート** | 計画対比の実績、成果物一覧、課題参照 | マネージャーまたは評価者への報告書 |
| **評価** | 評価計画（基準・方法）、評価結果テーブル、達成度判定、推奨アクション | 成功基準に対する客観的な達成度評価 |
| **ゲート判定** | 通過/条件付き通過/差し戻しの3択判定、判定理由の明記 | 次フェーズへの進行可否を決定する |
| **知見集約ルーティング** | 横展開テーブル、ルーティング先（CSV/refs/backlog/inbox/なし）の明記 | 施策の知見を組織に還元する |

### 1.2 セッションタイプ別の適用マトリクス

全セッションタイプのロールを **マネージャー**・**ワーカー**・**評価ワーカー** の 3 アーキタイプに集約する。

| ステージ | マネージャー | ワーカー | 評価ワーカー |
|---------|:----------:|:------:|:----------:|
| 壁打ち | 必須 | 必須 | 必須 |
| 計画 | 必須（立案） | 必須（実施計画）^1 | 必須（評価計画）^1 |
| 実施（作業履歴） | N/A | 必須 | N/A |
| 実施（課題起票） | 必須^2 | 必須 | 必須 |
| 実施（気づき記録） | N/A | 必須 | 必須 |
| レポート | 必須^3 | 必須 | 必須 |
| 評価 | N/A | N/A | 必須 |
| ゲート判定 | 必須^4 | N/A | N/A |
| 知見集約ルーティング | 必須 | N/A | N/A |

**凡例**:
- **必須**: ロール定義に含まれていなければならない
- **N/A**: 該当ロールの責務外（他ロールが担当）

#### 例外テーブル

| 注記 | 対象ロール | 例外内容 |
|------|----------|---------|
| ^1 | 3-phase ワーカー/評価ワーカー（triage, meta, bm, auto, co, sc） | 計画はマネージャーが作成し受領する（N/A）。ただし壁打ちフェーズ内で作業/評価計画を記載するため、壁打ちは必須 |
| ^2 | L1-manager | 条件付き（ワーカー成果物の課題をゲート判定時に集約転記。直接起票は条件付き） |
| ^3 | L1-manager | N/A（ワーカー成果物を直接ゲート判定に使用）。sync-manager も同様 |
| ^3 | impl-manager | 必須（B+C 集約レポート） |
| ^4 | 3-phase マネージャー（triage, meta, bm, auto） | 条件付き（PR レビューでユーザー承認を得る形式） |
| ^4 | multi-phase マネージャー（co, sc） | 必須（3 回：各フェーズゲート） |
| ^4 | impl-manager | 必須（4 回：各フェーズゲート） |
| — | impl-worker (Ph4) | 計画は N/A（チェックポイント方式）。気づき記録は N/A（B+C 集約）。レポートは N/A（B+C 集約） |

### 1.3 記録先ファイルの対応

ロール別に記録先ファイルを定義する。

#### パターン A: イニシアティブ（l1-manager + l2-worker/evaluator）

| ステージ | マネージャー | ワーカー | 評価ワーカー |
|---------|------------|---------|------------|
| 壁打ち | 01_proposal.md, 00_wallbash_log.md | phase-\*/set-N/01_worker_plan.md | phase-\*/set-N/04_eval_plan.md |
| 計画 | 02_plan.md, 03_tasks.md | phase-\*/set-N/01_worker_plan.md（実施計画を記載） | phase-\*/set-N/04_eval_plan.md |
| 作業履歴 | — | phase-\*/set-N/02_worker_log.md | — |
| 課題起票 | 05_gate_review.md（集約転記） | phase-\*/set-N/07_issues.md → CSV | phase-\*/set-N/07_issues.md → CSV |
| 気づき記録 | — | phase-\*/set-N/03_worker_report.md | phase-\*/set-N/06_eval_report.md |
| レポート | — | phase-\*/set-N/03_worker_report.md | phase-\*/set-N/06_eval_report.md |
| 評価 | — | — | phase-\*/set-N/04_eval_plan.md → phase-\*/set-N/06_eval_report.md |
| ゲート判定 | 05_gate_review.md | — | — |
| 知見集約 | 05_gate_review.md 横展開テーブル | — | — |

#### パターン B: 3フェーズ標準（triage, meta, bm, auto, co, sc 共通）

| ステージ | マネージャー | ワーカー | 評価ワーカー |
|---------|------------|---------|------------|
| 壁打ち | 00_pre_investigation.md | 02_scan_plan.md | 05_eval_plan.md |
| 計画 | 01_plan.md | N/A（受領側） | N/A（受領側） |
| 作業履歴 | — | 03_work_log.md | — |
| 課題起票 | 03_report.md（集約転記） | 07_issues.md → マネージャーが CSV 転記 | 07_issues.md → マネージャーが CSV 転記 |
| 気づき記録 | — | 04_scan_report.md | 06_eval_report.md |
| レポート | 03_report.md | 04_scan_report.md | 06_eval_report.md |
| 評価 | — | — | 05_eval_plan.md → 06_eval_report.md |
| ゲート判定 | 04_gate_review.md + PR レビュー | — | — |
| 知見集約 | 03_report.md | — | — |

#### バリアント B': sync（パターン B との差分のみ）

| ステージ | 差分 |
|---------|------|
| 壁打ち（ワーカー） | 03_work_log.md（scan_plan なし） |
| 壁打ち（評価ワーカー） | 05_eval_plan.md |
| 計画（ワーカー） | N/A（受領側） |
| 計画（評価ワーカー） | 必須（05_eval_plan.md に記載） |
| レポート（ワーカー） | 04_sync_report.md（scan_report ではない） |
| レポート（マネージャー） | N/A |
| ゲート判定 | 08_gate_review.md + PR レビュー（04 ではなく 08） |
| 知見集約 | 08_gate_review.md 横展開テーブル（03_report ではない） |

> **impl**: 4 フェーズ特殊構造。`l1-impl-manager/SKILL.md` を参照

### 1.4 テンプレート構成仕様

各セッションタイプの `sessions/<type>/_template/` に含まれるべきファイルの正解定義。SC-009 チェックの基準となる。

#### 基本モデル: multi-phase manager パターン

```
_template/
├── [マネージャールートファイル]
├── phase-N-xxx/
│   ├── 01_gate.md                  ← phase ゲート
│   └── _template/                  ← worker set テンプレート
│       └── [ワーカー+評価ワーカーファイル]
```

マネージャーがルートレベルで計画・集約・ゲート判定を行い、各 phase 内で worker set をディスパッチする。

#### §1.4.1 マネージャールートファイル

| ファイル | 用途 | 適用パターン |
|---------|------|-----------|
| `00_pre_investigation.md` | 事前調査（壁打ち） | 3-phase, sync, multi-phase |
| `01_proposal.md` | 提案書（壁打ち） | initiative, impl |
| `00_wallbash_log.md` | 壁打ちログ | initiative |
| `01_plan.md` | 計画 | 全パターン（initiative 以外） |
| `02_plan.md` | 計画 | initiative |
| `02_dispatch_log.md` | ディスパッチ記録 | 3-phase, multi-phase |
| `03_tasks.md` | タスクリスト | initiative |
| `04_dispatch_log.md` | ディスパッチ記録 | initiative |
| `02_impl_design.md` | 実装設計 | impl |
| `03_report.md` | 集約レポート | 3-phase, multi-phase |
| `04_gate_review.md` | ゲートレビュー | 3-phase, multi-phase |
| `05_gate_review.md` | ゲートレビュー | initiative |
| `08_gate_review.md` | ゲートレビュー | sync |
| `08_gate_summary.md` | ゲートサマリー | impl |
| `06_cost_record.md` | コスト分析 | initiative |

#### §1.4.2 ワーカーセットテンプレート（共通 7 ファイル）

3-phase / multi-phase の `phase-N-xxx/_template/` 配下:

| ファイル | ロールオーナー | 用途 |
|---------|-------------|------|
| `01_tasks.md` | マネージャー(CREATE) / ワーカー(READ) | タスク割当 |
| `02_scan_plan.md` | ワーカー | スキャン計画 + 壁打ち |
| `03_work_log.md` | ワーカー | 作業履歴 |
| `04_scan_report.md` | ワーカー | スキャンレポート |
| `05_eval_plan.md` | 評価ワーカー | 評価計画 + 壁打ち |
| `06_eval_report.md` | 評価ワーカー | 評価レポート |
| `07_issues.md` | ワーカー / 評価ワーカー | 課題バッファ |

##### initiative 向けワーカーセットテンプレート（7 ファイル）

initiative の `phase-N-xxx/_template/` 配下:

| ファイル | ロールオーナー | 用途 |
|---------|-------------|------|
| `01_worker_plan.md` | ワーカー | タスク理解・不明点解消（壁打ち） |
| `02_worker_log.md` | ワーカー | 作業中の判断・メモ |
| `03_worker_report.md` | ワーカー | 振り返り・課題発見 |
| `04_eval_plan.md` | 評価ワーカー | 評価観点の整理（壁打ち） |
| `05_eval_log.md` | 評価ワーカー | 評価中の判断・メモ |
| `06_eval_report.md` | 評価ワーカー | 評価結果・改善点 |
| `07_issues.md` | ワーカー / 評価ワーカー | 課題バッファ |

#### §1.4.3 Initiative テンプレート（2-phase 構造）

`sessions/initiatives/_template/`:

```
_template/
├── 00_wallbash_log.md              ← マネージャー（壁打ちログ）
├── 01_proposal.md                  ← マネージャー（提案書）
├── 02_plan.md                      ← マネージャー（計画）
├── 03_tasks.md                     ← マネージャー（タスクリスト）
├── 04_dispatch_log.md              ← マネージャー（ディスパッチ記録）
├── 05_gate_review.md               ← マネージャー（ゲートレビュー）
├── 06_cost_record.md               ← マネージャー（コスト分析）
│
├── phase-1-planning/
│   └── _template/                  ← plan-worker/plan-evaluator set テンプレート
│       ├── 01_worker_plan.md       ← plan-worker: タスク理解・不明点解消
│       ├── 02_worker_log.md        ← plan-worker: 作業中の判断・メモ
│       ├── 03_worker_report.md     ← plan-worker: 振り返り・課題発見
│       ├── 04_eval_plan.md         ← plan-evaluator: 評価観点の整理
│       ├── 05_eval_log.md          ← plan-evaluator: 評価中の判断・メモ
│       ├── 06_eval_report.md       ← plan-evaluator: 評価結果・改善点
│       ├── 07_issues.md            ← 共有: 課題バッファ
│       └── 08_task_division.md     ← 成果物（ファイルレベルタスク分割）
│
└── phase-2-execution/
    └── _template/                  ← worker/evaluator set テンプレート
        ├── 01_worker_plan.md       ← worker: タスク理解・不明点解消
        ├── 02_worker_log.md        ← worker: 作業中の判断・メモ
        ├── 03_worker_report.md     ← worker: 振り返り・課題発見
        ├── 04_eval_plan.md         ← evaluator: 評価観点の整理
        ├── 05_eval_log.md          ← evaluator: 評価中の判断・メモ
        ├── 06_eval_report.md       ← evaluator: 評価結果・改善点
        └── 07_issues.md            ← 共有: 課題バッファ
```

> **構造上の特徴**: マネージャールートファイル + 2-phase ネスト構造。各 phase 内に `_template/` があり、ワーカーセット 7 ファイル（§1.4.2 initiative 向け）を格納する。並列ディスパッチ時は `_template/` を `set-N/` にコピーして使用する（W_template は不要）。

#### §1.4.4 3-Phase 標準テンプレート（triage, meta, bm, auto）

`sessions/<type>/_template/`:

| 階層 | ファイル | ロールオーナー |
|------|---------|-------------|
| ルート | `00_pre_investigation.md` | マネージャー |
| ルート | `01_plan.md` | マネージャー |
| ルート | `02_dispatch_log.md` | マネージャー |
| ルート | `03_report.md` | マネージャー |
| ルート | `04_gate_review.md` | マネージャー |
| `phase-1-xxx/_template/` | 共通 7 ファイル（§1.4.2） | ワーカー / 評価ワーカー |

> **構造上の特徴**: 事実上 single-phase。`phase-1-xxx/` パターンに統一済み。

#### §1.4.5 Multi-Phase テンプレート（co, sc）

`sessions/<type>/_template/`:

| 階層 | ファイル | ロールオーナー |
|------|---------|-------------|
| ルート | `00_pre_investigation.md` | マネージャー |
| ルート | `01_plan.md` | マネージャー |
| ルート | `02_dispatch_log.md` | マネージャー |
| ルート | `03_report.md` | マネージャー |
| ルート | `04_gate_review.md` | マネージャー |
| `phase-1-collection/` | `01_gate.md` | マネージャー |
| `phase-1-collection/_template/` | 共通 7 ファイル（§1.4.2） | ワーカー / 評価ワーカー |
| `phase-2-analysis/` | `01_gate.md` | マネージャー |
| `phase-2-analysis/_template/` | 共通 7 ファイル（§1.4.2） | ワーカー / 評価ワーカー |
| `phase-3-proposal/` | `01_gate.md` | マネージャー |
| `phase-3-proposal/_template/` | 共通 7 ファイル（§1.4.2） | ワーカー / 評価ワーカー |

> **基本形そのもの**。マネージャーが 3 phase を逐次オーケストレーションし、各 phase 内で worker set をディスパッチする。

#### §1.4.6 Sync テンプレート（9 ファイル、フラット構造）

`sessions/sync/_template/`:

| ファイル | ロールオーナー | 用途 |
|---------|-------------|------|
| `00_pre_investigation.md` | マネージャー | 事前調査 |
| `01_plan.md` | マネージャー | 計画 |
| `02_dispatch_log.md` | マネージャー | ディスパッチ記録 |
| `03_work_log.md` | ワーカー | 作業履歴 |
| `04_sync_report.md` | ワーカー | 同期レポート |
| `05_eval_plan.md` | 評価ワーカー | 評価計画 |
| `06_eval_report.md` | 評価ワーカー | 評価レポート |
| `07_issues.md` | ワーカー / 評価ワーカー | 課題バッファ |
| `08_gate_review.md` | マネージャー | ゲートレビュー |

> **構造上の特徴**: フラット構造。worker set ディスパッチなし（単一ワーカー + 単一評価ワーカー）。

#### §1.4.7 Impl テンプレート（4 フェーズ特殊構造）

`sessions/impl/_template/`:

| 階層 | ファイル | ロールオーナー |
|------|---------|-------------|
| ルート | `00_proposal.md` | マネージャー |
| ルート | `01_plan.md` | マネージャー |
| ルート | `02_impl_design.md` | マネージャー |
| ルート | `07_issues.md` | ワーカー / 評価ワーカー（共有） |
| ルート | `07_issues_W_template.md` | ワーカー（並列用） |
| ルート | `08_gate_summary.md` | マネージャー |
| `phase-1-investigation/` | `01_tasks, 02_work_log, 03_work_report, 04_eval_plan, 05_eval_report, 06_gate` | ワーカー / 評価ワーカー / マネージャー(gate) |
| `phase-2-design/` | 同上 | 同上 |
| `phase-3-impl-plan/` | 同上 + `07_file_task_division.md` | 同上 |
| `phase-4-impl/` | `01_tasks, 02_work_log_W_template, 03_work_report, 04_eval_plan, 05_eval_report, 06_gate` | 同上（並列用テンプレート） |

> **構造上の特徴**: phase 内にファイル直置き（`_template/` sub-dir なし）。各 phase で異なるワーカータイプ（investigation, design, impl-plan, impl）を使用。

---

## 2. 実施者/評価者ペアリング要件

### 2.1 ペアリング構造

| 実施者 | 評価者 | オーケストレーター |
|--------|--------|-----------------|
| L2-worker | L2-evaluator | L1-manager |
| l2-plan-worker | L1-manager（直接確認） | L1-manager |
| investigation-worker / design-worker / impl-plan-worker / impl-worker | impl-evaluator | l1-impl-manager |
| triage-worker | triage-evaluator | triage-manager |
| metacognition-worker | metacognition-evaluator | metacognition-manager |
| sync-worker | sync-evaluator | sync-manager |
| backlog-maintenance-worker | backlog-maintenance-evaluator | backlog-maintenance-manager |
| automation-worker | automation-evaluator | automation-manager |
| config-collection-worker / config-analysis-worker / config-proposal-worker | config-optimizer-evaluator | config-optimizer-manager |
| sc-collection-worker / sc-analysis-worker / sc-proposal-worker | sc-evaluator | session-consistency-manager |

### 2.2 ペアリングルール

1. **順序制約**: 実施者が完了してから評価者を起動すること（並列起動禁止）
2. **成果物チェーン**: 実施者の成果物が評価者の入力となる。評価者は実施者の成果物を直接編集しない
3. **課題のエスカレーション**: 評価者が発見した課題のうち、実施者の責務に属するもの（未転記課題など）はレポートに記載してオーケストレーターに委ねる
4. **独立コンテキスト**: 実施者と評価者は独立したサブエージェントとして起動される。相互の作業ログへのアクセスは読み取りのみ

### 2.3 ペアリングの対称性要件

実施者と評価者は以下の要素で対称的であること。

| 要素 | 実施者に必須 | 評価者に必須 |
|------|------------|------------|
| 壁打ちフェーズ | あり | あり |
| 作業/評価計画 | あり | あり |
| レポート | あり | あり |
| 知見記録セクション | あり | あり |
| 課題起票手段 | あり | あり |
| 停止ルール | あり | あり |

> **解消済み（2026-03-06）**: triage-evaluator に壁打ちフェーズ（05_eval_plan.md）と知見記録セクション（06_eval_report.md「評価中の知見」）が追加済み。triage-worker の知見記録セクションも構造化テーブル形式に改善済み。

---

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | ゲート判定基準・差し戻し手順のチェック基準（セクション D）の参照先 |
| `.claude/skills/l1-manager/SKILL.md` | ライフサイクルステージ・ペアリング要件の変更がマネージャー定義に影響する場合 |
| `.claude/skills/l1-manager/agents/l2-worker.md` | ライフサイクル適用マトリクスの変更がワーカー定義に影響する場合 |
| `.claude/skills/l1-manager/agents/l2-evaluator.md` | ライフサイクル適用マトリクスの変更が評価者定義に影響する場合 |
| `.claude/skills/triage-manager/SKILL.md` | ライフサイクル適用マトリクスの変更がマネージャー定義に影響する場合（TG-008 チェックリストは triage-manager 側に統合済み） |
| `.claude/skills/triage-manager/agents/triage-evaluator.md` | ペアリング対称性要件の変更が評価者定義に影響する場合 |
| `.claude/skills/metacognition-manager/SKILL.md` | ライフサイクル適用マトリクスの変更がメタ認知マネージャー定義に影響する場合 |
| `.claude/skills/metacognition-manager/agents/metacognition-worker.md` | ライフサイクル適用マトリクスの変更がメタ認知ワーカー定義に影響する場合 |
| `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md` | ペアリング対称性要件の変更がメタ認知評価者定義に影響する場合 |
| `.claude/skills/sync-manager/SKILL.md` | ライフサイクル適用マトリクスの変更が同期マネージャー定義に影響する場合 |
| `.claude/skills/sync-manager/agents/sync-worker.md` | ライフサイクル適用マトリクスの変更が同期ワーカー定義に影響する場合 |
| `.claude/skills/sync-manager/agents/sync-evaluator.md` | ペアリング対称性要件の変更が同期評価者定義に影響する場合 |
| `.claude/skills/backlog-maintenance-manager/SKILL.md` | ライフサイクル適用マトリクスの変更がバックログメンテナンスマネージャー定義に影響する場合 |
| `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md` | ライフサイクル適用マトリクスの変更がバックログメンテナンスワーカー定義に影響する場合 |
| `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md` | ペアリング対称性要件の変更がバックログメンテナンス評価者定義に影響する場合 |
| `.claude/skills/automation-manager/SKILL.md` | ライフサイクル適用マトリクスの変更がオートメーションマネージャー定義に影響する場合 |
| `.claude/skills/automation-manager/agents/automation-worker.md` | ライフサイクル適用マトリクスの変更がオートメーションワーカー定義に影響する場合 |
| `.claude/skills/automation-manager/agents/automation-evaluator.md` | ペアリング対称性要件の変更がオートメーション評価者定義に影響する場合 |
| `.claude/skills/l1-impl-manager/SKILL.md` | ライフサイクル適用マトリクスの変更が実装マネージャー定義に影響する場合 |
| `.claude/skills/l1-impl-manager/agents/investigation-worker.md` | ライフサイクル適用マトリクスの変更が調査ワーカー定義に影響する場合 |
| `.claude/skills/l1-impl-manager/agents/design-worker.md` | ライフサイクル適用マトリクスの変更が設計ワーカー定義に影響する場合 |
| `.claude/skills/l1-impl-manager/agents/impl-plan-worker.md` | ライフサイクル適用マトリクスの変更が実装計画ワーカー定義に影響する場合 |
| `.claude/skills/l1-impl-manager/agents/impl-worker.md` | ライフサイクル適用マトリクスの変更が実装ワーカー定義に影響する場合 |
| `.claude/skills/l1-impl-manager/agents/impl-evaluator.md` | ペアリング対称性要件の変更が実装評価者定義に影響する場合 |
| `.claude/skills/config-optimizer-manager/SKILL.md` | ライフサイクル適用マトリクスの変更がconfig最適化マネージャー定義に影響する場合 |
| `.claude/skills/config-optimizer-manager/agents/config-collection-worker.md` | ライフサイクル適用マトリクスの変更がconfig収集ワーカー定義に影響する場合 |
| `.claude/skills/config-optimizer-manager/agents/config-analysis-worker.md` | ライフサイクル適用マトリクスの変更がconfig分析ワーカー定義に影響する場合 |
| `.claude/skills/config-optimizer-manager/agents/config-proposal-worker.md` | ライフサイクル適用マトリクスの変更がconfig提案ワーカー定義に影響する場合 |
| `.claude/skills/config-optimizer-manager/agents/config-optimizer-evaluator.md` | ペアリング対称性要件の変更がconfig最適化評価者定義に影響する場合 |
| `.claude/skills/session-consistency-manager/SKILL.md` | ライフサイクル適用マトリクスの変更がセッション一貫性マネージャー定義に影響する場合。SC-009（§1.4 テンプレート構成仕様準拠）が §1.4 を参照 |
| `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md` | ライフサイクル適用マトリクスの変更がSC収集ワーカー定義に影響する場合 |
| `.claude/skills/session-consistency-manager/agents/sc-analysis-worker.md` | ライフサイクル適用マトリクスの変更がSC分析ワーカー定義に影響する場合 |
| `.claude/skills/session-consistency-manager/agents/sc-proposal-worker.md` | ライフサイクル適用マトリクスの変更がSC提案ワーカー定義に影響する場合 |
| `.claude/skills/session-consistency-manager/agents/sc-evaluator.md` | ペアリング対称性要件の変更がSC評価者定義に影響する場合 |
| `.claude/skills/session-flow-policy/SKILL.md` | ペアリング要件・ライフサイクル定義が新セッション作成ポリシーに影響する場合 |
| `docs/workflow.md` | 標準ポリシーの変更がワークフロー記述に影響する場合（人間向け可視化） |

---

**作成日**: 2026-03-05
**作成者**: L2（実施）
**関連施策**: トリアージ標準ポリシーガイドライン
**リネーム日**: 2026-03-17（triage-standard-policy → session-lifecycle-policy、§3 TG-008 チェックリストを triage-manager に移動）
