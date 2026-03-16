---
name: triage-standard-policy
description: 'トリアージ走査（TG-008）・ペアリング検証・ライフサイクル準拠チェック時に参照するガイドライン'
user-invocable: false
---
# トリアージ標準ポリシーガイドライン

> **このファイルの位置づけ**
> セッションタイプ間で共通するライフサイクルパターン・ペアリング要件・準拠チェック基準を定義する。
> `.claude/skills/` 配下のスキル・エージェント定義が個々のルールの正の情報源であり、本ガイドラインはそれらの横断的な整合性を担保するための基準文書である。

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

| ステージ | L1-manager | L2-worker | L2-evaluator | impl-manager | impl-worker (Ph1-3) | impl-worker (Ph4) | impl-evaluator | triage-manager | triage-worker | triage-evaluator | meta-manager | meta-worker | meta-evaluator | sync-manager | sync-worker | sync-evaluator | bm-manager | bm-worker | bm-evaluator | auto-manager | auto-worker | auto-evaluator | co-manager | co-worker | co-evaluator |
|---------|:----------:|:---------:|:------------:|:------------:|:-------------------:|:-----------------:|:--------------:|:--------------:|:-------------:|:----------------:|:------------:|:-----------:|:--------------:|:------------:|:-----------:|:--------------:|:----------:|:---------:|:------------:|:------------:|:-----------:|:--------------:|:----------:|:---------:|:------------:|
| 壁打ち | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須（事前調査） | 必須 | 必須 | 必須（事前調査） | 必須 | 推奨 | 必須（事前調査） | 必須 | 必須 | 必須（事前調査） | 必須 | 必須 | 必須（事前調査） | 必須 | 必須 | 必須（事前調査） | 必須 | 必須 |
| 計画 | 必須（立案） | 必須（実施計画） | 必須（評価計画） | 必須（4フェーズ立案） | 必須（実施計画） | N/A（チェックポイント） | 必須（評価計画） | 必須（立案） | N/A（受領側） | N/A（受領側） | 必須（立案） | N/A（受領側） | N/A（受領側） | 必須（立案） | N/A（受領側） | 必須（評価計画） | 必須（立案） | N/A（受領側） | N/A（受領側） | 必須（立案） | N/A（受領側） | N/A（受領側） | 必須（立案） | N/A（受領側） | N/A（受領側） |
| 実施（作業履歴） | N/A | 必須 | N/A | N/A | 必須 | 必須（チェックポイント） | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A |
| 実施（課題起票） | 条件付き | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 推奨 | 必須 | 必須 | 推奨 | 必須 | 必須 | 必須 | 必須 | 必須 | 推奨 | 必須 | 必須 | 推奨 | 必須 | 必須 | 推奨 |
| 実施（気づき記録） | N/A | 必須 | 必須 | N/A | 必須 | N/A（B+C集約） | 必須 | N/A | 必須 | 推奨 | N/A | 必須 | 推奨 | N/A | 必須 | 必須 | N/A | 必須 | 推奨 | N/A | 必須 | 推奨 | N/A | 必須 | 推奨 |
| レポート | N/A | 必須 | 必須 | 必須（B+C集約） | 必須 | N/A（B+C集約） | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | N/A | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 | 必須 |
| 評価 | N/A | N/A | 必須 | N/A | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 |
| ゲート判定 | 必須 | N/A | N/A | 必須（4回） | N/A | N/A | N/A | 条件付き | N/A | N/A | 条件付き | N/A | N/A | 必須 | N/A | N/A | 条件付き | N/A | N/A | 条件付き | N/A | N/A | 必須（3回） | N/A | N/A |
| 知見集約ルーティング | 必須 | N/A | N/A | 必須 | N/A | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A | 必須 | N/A | N/A |

**凡例**:
- **必須**: ロール定義に含まれていなければならない
- **推奨**: 含まれていることが望ましい（欠落している場合はトリアージで課題として起票）
- **条件付き**: 特定条件下でのみ実施（条件はロール定義に明記されていること）
- **N/A**: 該当ロールの責務外（他ロールが担当）

### 1.3 記録先ファイルの対応

| ステージ | イニシアティブ系 | トリアージ系 | メタ認知系 | 同期系 | バックログメンテナンス系 | オートメーション系 |
|---------|----------------|-------------|-----------|--------|---------------------|------------------|
| 壁打ち | 03_work_log.md / 05_eval_plan.md | 02_scan_plan.md / 05_eval_plan.md / 00_pre_investigation.md | 02_scan_plan.md / 05_eval_plan.md / 00_pre_investigation.md | 03_work_log.md / 05_eval_plan.md / 00_pre_investigation.md | 02_scan_plan.md / 05_eval_plan.md / 00_pre_investigation.md | 02_scan_plan.md / 05_eval_plan.md / 00_pre_investigation.md |
| 計画 | 01_plan.md / 03_work_log.md / 05_eval_plan.md | 01_plan.md | 01_plan.md | 01_plan.md / 05_eval_plan.md | 01_plan.md | 01_plan.md |
| 作業履歴 | 03_work_log.md | 03_work_log.md | 03_work_log.md | 03_work_log.md | 03_work_log.md | 03_work_log.md |
| 課題起票 | 07_issues.md（中間バッファ）→ CSV | 07_issues.md（中間バッファ）→ マネージャーが CSV 転記 | 07_issues.md（中間バッファ）→ マネージャーが CSV 転記 | 07_issues.md（中間バッファ）→ マネージャーが CSV 転記 | 07_issues.md（中間バッファ）→ マネージャーが CSV 転記 | 07_issues.md（中間バッファ）→ マネージャーが CSV 転記 |
| 気づき記録 | 04_work_report.md / 06_eval_report.md | 04_scan_report.md | 04_scan_report.md | 04_sync_report.md / 06_eval_report.md | 04_scan_report.md / 06_eval_report.md | 04_scan_report.md / 06_eval_report.md |
| レポート | 04_work_report.md / 06_eval_report.md | 04_scan_report.md / 06_eval_report.md / 03_report.md | 04_scan_report.md / 06_eval_report.md / 03_report.md | 04_sync_report.md / 06_eval_report.md | 04_scan_report.md / 06_eval_report.md / 03_report.md | 04_scan_report.md / 06_eval_report.md / 03_report.md |
| 評価 | 05_eval_plan.md → 06_eval_report.md | 05_eval_plan.md → 06_eval_report.md | 05_eval_plan.md → 06_eval_report.md | 05_eval_plan.md → 06_eval_report.md | 05_eval_plan.md → 06_eval_report.md | 05_eval_plan.md → 06_eval_report.md |
| ゲート判定 | 08_gate_review.md | 04_gate_review.md + PR レビュー（ユーザー承認） | 04_gate_review.md + PR レビュー（ユーザー承認） | 08_gate_review.md + PR レビュー（ユーザー承認） | 04_gate_review.md + PR レビュー（ユーザー承認） | 04_gate_review.md + PR レビュー（ユーザー承認） |
| 知見集約 | 08_gate_review.md 横展開テーブル | 03_report.md | 03_report.md | 08_gate_review.md 横展開テーブル | 03_report.md | 03_report.md |

---

## 2. 実施者/評価者ペアリング要件

### 2.1 ペアリング構造

| 実施者 | 評価者 | オーケストレーター |
|--------|--------|-----------------|
| L2-worker | L2-evaluator | L1-manager |
| investigation-worker / design-worker / impl-plan-worker / impl-worker | impl-evaluator | l1-impl-manager |
| triage-worker | triage-evaluator | triage-manager |
| metacognition-worker | metacognition-evaluator | metacognition-manager |
| sync-worker | sync-evaluator | sync-manager |
| backlog-maintenance-worker | backlog-maintenance-evaluator | backlog-maintenance-manager |
| automation-worker | automation-evaluator | automation-manager |
| config-collection-worker / config-analysis-worker / config-proposal-worker | config-optimizer-evaluator | config-optimizer-manager |

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

## 3. トリアージ走査用チェックリスト（TG-008）

トリアージセッションで、ロール定義（`.claude/skills/` 配下のスキル・エージェント定義）やセッションルールがガイドラインに準拠しているかを確認するためのチェックリスト。

### 3.1 走査対象

- `.claude/skills/l1-manager/SKILL.md`
- `.claude/skills/l1-manager/agents/l2-worker.md`
- `.claude/skills/l1-manager/agents/l2-evaluator.md`
- `.claude/skills/triage-manager/SKILL.md`
- `.claude/skills/triage-manager/agents/triage-worker.md`
- `.claude/skills/triage-manager/agents/triage-evaluator.md`
- `.claude/skills/metacognition-manager/SKILL.md`
- `.claude/skills/metacognition-manager/agents/metacognition-worker.md`
- `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md`
- `.claude/skills/sync-manager/SKILL.md`
- `.claude/skills/sync-manager/agents/sync-worker.md`
- `.claude/skills/sync-manager/agents/sync-evaluator.md`
- `.claude/skills/backlog-maintenance-manager/SKILL.md`
- `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md`
- `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md`
- `.claude/skills/automation-manager/SKILL.md`
- `.claude/skills/automation-manager/agents/automation-worker.md`
- `.claude/skills/automation-manager/agents/automation-evaluator.md`
- `.claude/skills/l1-impl-manager/SKILL.md`
- `.claude/skills/l1-impl-manager/agents/investigation-worker.md`
- `.claude/skills/l1-impl-manager/agents/design-worker.md`
- `.claude/skills/l1-impl-manager/agents/impl-plan-worker.md`
- `.claude/skills/l1-impl-manager/agents/impl-worker.md`
- `.claude/skills/l1-impl-manager/agents/impl-evaluator.md`
- `.claude/skills/config-optimizer-manager/SKILL.md`
- `.claude/skills/config-optimizer-manager/agents/config-collection-worker.md`
- `.claude/skills/config-optimizer-manager/agents/config-analysis-worker.md`
- `.claude/skills/config-optimizer-manager/agents/config-proposal-worker.md`
- `.claude/skills/config-optimizer-manager/agents/config-optimizer-evaluator.md`
- 新規作成または変更されたロール定義ファイル（`roles/*.md` を含む）

### 3.2 チェック項目

#### A. ライフサイクル完備チェック

- [ ] セクション1.2の適用マトリクスで「必須」となっているステージが、ロール定義に含まれているか
- [ ] 壁打ちフェーズの定義があるか（記録先ファイル・フォーマットが明記されているか）
- [ ] 計画ステージが適切に定義されているか（マネージャー系は立案、ワーカー系は実施/評価計画）
- [ ] レポートの構成が明記されているか
- [ ] 「推奨」ステージの欠落がないか（欠落している場合は課題として起票）

#### B. ペアリング整合性チェック

- [ ] 実施者と対応する評価者の両方のロール定義が存在するか
- [ ] 実施者の成果物が評価者の入力として参照されているか（担当ファイルテーブルで確認）
- [ ] ペアリングの対称性要件（セクション2.3）が満たされているか
- [ ] オーケストレーターのルール定義に、実施者→評価者の起動順序が明記されているか

#### C. 課題起票・ルーティングチェック

- [ ] 課題起票の方法（中間バッファ経由 or CSV直接起票）がロール定義に明記されているか
- [ ] 知見記録セクション（「ルール化候補」「参考情報」の分類テーブル）が定義されているか
- [ ] 知見集約のルーティング先が明記されているか（マネージャー系のみ）

#### D. マネージャー共通ポリシー準拠チェック

- [ ] ゲート判定基準の定義があるか（直接記載または `manager-common-policy` §4 参照）
- [ ] 差し戻し手順の定義があるか（直接記載または `manager-common-policy` §7 参照）

#### E. 停止ルール・スコープチェック

- [ ] 「やること」「やらないこと」セクションが存在し、スコープが明確か
- [ ] 停止ルールが定義されているか
- [ ] 停止時の起票/報告フォーマットが明記されているか
- [ ] 担当ファイルテーブルがあり、各ファイルの操作権限（読み取り/編集/追記）が明記されているか

#### E. メタルール横断整合性チェック

- [ ] テンプレートファイルのパス参照がスキル・エージェント定義内のフロー記述と一致しているか
- [ ] `.claude/skills/` 配下の変更が `docs/workflow.md` の対応セクションに反映されているか
- [ ] `.claude/rules/` 配下のルール変更が本チェックリスト（TG-008）の基準に反映されているか

### 3.3 不適合時のアクション

| 不適合の種類 | アクション |
|-------------|----------|
| 「必須」ステージの欠落 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 高、CSV は自動生成） |
| 「推奨」ステージの欠落 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 中、CSV は自動生成） |
| ペアリング不整合 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 高、CSV は自動生成） |
| フォーマット不備（停止ルール・担当ファイル等の欠落） | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 低、CSV は自動生成） |
| 軽微な記述ズレ（表現の不統一等） | トリアージセッション内で修正 |
| テンプレート・ルールとメタルールの不整合 | `issues/entries/ISS-XXX.md` を作成して起票（優先度: 中、CSV は自動生成）。軽微なパス参照ズレはセッション内で修正 |

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
| `.claude/skills/triage-manager/SKILL.md` | TG-008 チェック基準の変更がマネージャーのルールに影響する場合 |
| `.claude/skills/triage-manager/agents/triage-worker.md` | TG-008 走査手順・チェック項目の変更がワーカーの走査手順に影響する場合 |
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
| `.claude/skills/session-flow-policy/SKILL.md` | ペアリング要件・ライフサイクル定義が新セッション作成ポリシーに影響する場合 |
| `docs/workflow.md` | 標準ポリシーの変更がワークフロー記述に影響する場合（人間向け可視化） |

---

**作成日**: 2026-03-05
**作成者**: L2（実施）
**関連施策**: トリアージ標準ポリシーガイドライン
