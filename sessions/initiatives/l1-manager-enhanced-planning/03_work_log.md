# 作業履歴: l1-manager-enhanced-planning

## 壁打ちフェーズ [2026-03-17 10:00]

### 理解のサマリー
- タスクの目的: L1マネージャーに計画ワーカー（l2-plan-worker）を導入し、フェーズ構造を Phase A/B/C/D から Phase 1〜6 に再構築する。これにより、タスク分割の質向上と並列ディスパッチの基盤を整備する
- スコープ: 施策フェーズ1（計画ワーカー導入 + フェーズ再構築の基盤）。T-001〜T-008 + T-F01〜T-F03
- 完了条件: 全タスク完了、03_work_log.md に作業履歴、04_work_report.md にサマリー・成果物・知見、07_issues.md に課題記録、コミット・プッシュ済み

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（01_plan.md, 02_tasks.md 作成済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read, Write, Edit, Bash）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
  - impl-plan-worker.md: 存在確認済み（参考パターン）
  - l2-worker.md, l2-evaluator.md: 存在確認済み（対称性確認用）
  - l1-manager SKILL.md: 存在確認済み（変更対象）
  - session-flow-policy SKILL.md: 存在確認済み（§3 エージェント必須要素）
  - _template/ ディレクトリ: 存在確認済み

### 不明点・確認事項
確認事項なし：実施開始

### タスク実施計画

1. **新規ファイル作成（T-001〜T-003）**: 依存関係なし、並列可能
   - T-001: l2-plan-worker.md — impl-plan-worker パターン応用、l2-worker 対称性考慮
   - T-002: l2-plan-evaluator.md — l2-evaluator 対称性考慮
   - T-003: 02a_task_division.md テンプレート — impl-plan-worker のフォーマットを l1 向けに調整

2. **既存ファイル変更（T-004〜T-008）**: T-004 が基盤、T-005〜T-008 は T-004 の Phase 構造に依存
   - T-004: l1-manager SKILL.md — Phase A/B/C/D → Phase 1〜6
   - T-005: 02_tasks.md テンプレート — Worker Set Assignment 追加
   - T-006: 08_gate_review.md テンプレート — Phase チェック更新
   - T-007: manager-common-policy — §2, §10 更新
   - T-008: docs/workflow.md — イニシアティブフロー更新

3. **固定タスク（T-F01〜T-F03）**: 作業完了後
   - T-F01: 知見セクション記録
   - T-F02: CSV 転記確認
   - T-F03: メタルール横断検証

---

### [2026-03-17 10:05] タスクID: T-001
**状態**: 完了
**作業内容**:
- `.claude/skills/l1-manager/agents/l2-plan-worker.md` を作成
- impl-plan-worker パターンを応用し、l1-manager 向けに調整
- 必須6セクション（役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）を備えた
- 02a_task_division.md のフォーマット定義を内蔵（T-XXX形式、ドメインエージェント推奨欄含む）
**成果物**: `.claude/skills/l1-manager/agents/l2-plan-worker.md`

### [2026-03-17 10:15] タスクID: T-002
**状態**: 完了
**作業内容**:
- `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` を作成
- l2-evaluator との対称性を確認し、対称性確認テーブルを含めた
- 重点評価項目（タスク粒度・アノテーション・コンフリクトマトリクス・依存関係・Wave割当・ドメインエージェント推奨・完了条件）を定義
**成果物**: `.claude/skills/l1-manager/agents/l2-plan-evaluator.md`

### [2026-03-17 10:25] タスクID: T-003
**状態**: 完了
**作業内容**:
- `sessions/initiatives/_template/02a_task_division.md` を作成
- タスク割当・Conflict Check Matrix・Wave Assignment・Domain Agent Recommendations・Summary セクションを定義
**成果物**: `sessions/initiatives/_template/02a_task_division.md`

### [2026-03-17 10:35] タスクID: T-004
**状態**: 完了
**作業内容**:
- l1-manager SKILL.md のフェーズ構造を Phase A/B/C/D → Phase 1〜6 に変更
- セッションライフサイクル todo を14ステップに更新（パターン1）
- Phase 2（計画ワーカーディスパッチ）、Phase 3（計画評価・タスク作成）フローを追加
- L2 壁打ちフェーズ応答フローに plan-worker/evaluator を追加
- 関連ファイル一覧に plan-worker/evaluator を追加
**成果物**: `.claude/skills/l1-manager/SKILL.md`（変更）

### [2026-03-17 10:45] タスクID: T-005
**状態**: 完了
**作業内容**:
- `sessions/initiatives/_template/02_tasks.md` を拡張
- Worker Set Assignment テーブル追加（Set / Worker / Evaluator / 担当タスク / Wave）
- Set Dispatch Order セクション追加（順序 / Set / 前提条件 / 備考）
- ドメインエージェント欄を Worker/Evaluator に分離（「対象」列追加）
**成果物**: `sessions/initiatives/_template/02_tasks.md`（変更）

### [2026-03-17 10:55] タスクID: T-006
**状態**: 完了
**作業内容**:
- `sessions/initiatives/_template/08_gate_review.md` を更新
- Phase A→B/B→C/C→D → Phase 1→2/2→3/3→4/4→5/5→6 の5段階チェック構造に変更
- Phase 1→2: Plan-Worker ディスパッチ前チェック3項目
- Phase 2→3: Plan-Evaluator ディスパッチ前チェック4項目
- Phase 3→4: Worker ディスパッチ前チェック5項目
- Phase 4→5: Evaluator ディスパッチ前チェック8項目
- Phase 5→6: 最終ゲート判定前チェック5項目
**成果物**: `sessions/initiatives/_template/08_gate_review.md`（変更）

### [2026-03-17 11:05] タスクID: T-007
**状態**: 完了
**作業内容**:
- manager-common-policy SKILL.md の §2 に §2.3（計画ワーカーディスパッチパターン）を追加
- §10.3 を更新し、L2-evaluator へのドメインエージェント参照を追加。Worker/Evaluator で異なるエージェント指定が可能であることを明記
**成果物**: `.claude/skills/manager-common-policy/SKILL.md`（変更）

### [2026-03-17 11:15] タスクID: T-008
**状態**: 完了
**作業内容**:
- docs/workflow.md のイニシアティブフローを Phase 1〜6 構造に更新
- 計画ワーカーフェーズ（Phase 2: l2-plan-worker、Phase 3: l2-plan-evaluator + タスク作成）を可視化
- フェーズゲートチェックテーブルを3段階→5段階に更新
- L2サブエージェント起動セクションに計画ワーカー起動順序を追加
- session-flow-policy SKILL.md のセッションタイプ一覧にplan-worker/evaluator を追加
**成果物**: `docs/workflow.md`, `.claude/skills/session-flow-policy/SKILL.md`（変更）

### [2026-03-17 11:25] タスクID: T-F03
**状態**: 完了
**作業内容**:
- メタルール横断検証を実施
- フロー記述: l1-manager SKILL.md 内の旧 Phase A/B/C/D 参照が全て Phase 1〜6 に更新されていることを grep で確認（合格）
- workflow.md 同期: docs/workflow.md のイニシアティブフローが Phase 1〜6 構造と整合していることを確認（合格）
- TG-008 基準連動: triage-standard-policy SKILL.md の走査対象リストに l2-plan-worker.md, l2-plan-evaluator.md を追加（修正済）
**成果物**: triage-standard-policy SKILL.md（走査対象追加）

### [2026-03-17 11:30] タスクID: T-F01, T-F02
**状態**: 完了
**作業内容**:
- T-F01: 04_work_report.md に知見セクション（ルール化候補・参考情報）を記録
- T-F02: 07_issues.md を確認。施策横断課題なし、転記対象なし
**成果物**: `04_work_report.md`, `07_issues.md`

---

## 施策フェーズ2: 並列ワーカーディスパッチ

## 壁打ちフェーズ [2026-03-17 14:00]

### 理解のサマリー
- タスクの目的: l1-manager の Phase 4（実施ワーカーディスパッチ）に並列実行の仕組みを導入する。現在は Worker が1つずつ順次ディスパッチされているが、独立タスクセットについては並列ディスパッチできるようにする
- スコープ: parallel-dev.md（新規ルール）、SKILL.md（Phase 4 並列ディスパッチ追加）、l2-worker.md（per-worker ファイル対応）、テンプレート群（per-worker ファイル追加）、manager-common-policy（§2 並列ディスパッチ詳細化）、session-flow-policy（並列ディスパッチ条件の更新）
- 完了条件: 02a_task_division.md に施策フェーズ2 のタスク分割が追記され、04_work_report.md に計画レポートが追記されている

### 前提条件チェック
- [x] 施策計画（01_plan.md）の内容を理解: 理解済み — 施策フェーズ2 の成功基準は「独立タスクセットが同時実行される」
- [x] 提案書（00_proposal.md）の確認: 確認済み — 並列ディスパッチでファイル衝突リスクが高いため、コンフリクトマトリクスによる事前検証 + L1承認ゲートが対策として挙げられている
- [x] 変更対象ファイル群の特定: 特定済み — 下記調査結果参照

### 変更対象ファイル調査結果

**新規作成**:
- `.claude/rules/parallel-dev.md` — 並列開発ルール（§2.2 で参照されているが未作成）

**変更対象**:
1. `.claude/skills/l1-manager/SKILL.md` — Phase 4 に並列ディスパッチ機構を追加。impl-manager のハイブリッド方式を l1-manager 向けに簡略化（外部リポ worktree は不要、per-worker ファイル分離のみ）
2. `.claude/skills/l1-manager/agents/l2-worker.md` — per-worker ファイル（03_work_log_W<N>.md, 07_issues_W<N>.md）への対応追加。isolation: worktree は dev-process-improvement が文書中心のため不要（git-worktree-guideline §4 の判断に準拠）
3. `sessions/initiatives/_template/02_tasks.md` — Set Dispatch Order に並列ディスパッチの Wave 情報を追加
4. `sessions/initiatives/_template/03_work_log.md` — per-worker テンプレート追加の参照
5. `.claude/skills/manager-common-policy/SKILL.md` — §2.2 の並列ディスパッチ条件を詳細化。per-worker ファイル分離パターンを追加
6. `.claude/skills/session-flow-policy/SKILL.md` — §4.2 並列ディスパッチ条件の更新

**参照のみ（Read-only）**:
- `.claude/skills/l1-impl-manager/SKILL.md` — 並列ディスパッチ機構の参考パターン
- `docs/git-worktree-guideline.md` — worktree 判断基準の参照
- `00_proposal.md`, `01_plan.md` — 背景・計画の参照

### 設計判断

1. **worktree vs per-worker ファイル分離**: dev-process-improvement は文書中心リポジトリであり、l1-manager の L2-worker は主に `.claude/skills/` や `sessions/initiatives/` 配下のファイルを編集する。impl-manager のような外部リポジトリのコード変更はないため、worktree による物理隔離は不要。per-worker ファイル分離（03_work_log_W<N>.md, 07_issues_W<N>.md）で競合を回避する方式が適切。ただし、**将来の worktree 活用のフック**として parallel-dev.md に escalation パスを記載する

2. **並列ディスパッチの単位**: Wave 方式（02a_task_division.md の Wave Assignment を利用）。同一 Wave 内のタスクは担当ファイルが分離されていることがコンフリクトマトリクスで検証済みであるため、並列実行が安全

3. **成果物統合**: Wave 完了後に L1 マネージャーが per-worker ファイルを統合する。07_issues_W<N>.md → 07_issues.md への統合、03_work_log_W<N>.md の確認

### 不明点・確認事項
確認事項なし：計画開始

### 分析計画

1. parallel-dev.md の設計（新規ルールファイル）
2. l1-manager SKILL.md の Phase 4 変更箇所の特定
3. l2-worker.md の per-worker ファイル対応箇所の特定
4. テンプレート群の変更箇所の特定
5. manager-common-policy §2 の変更箇所の特定
6. session-flow-policy §4 の変更箇所の特定
7. タスク分割・コンフリクトマトリクス・Wave 割当の作成

---

### [2026-03-17 14:10] 計画項目: 変更対象の詳細分析
**状態**: 完了
**作業内容**:
- impl-manager SKILL.md の並列ディスパッチ機構を参考パターンとして精読
- git-worktree-guideline.md §4 の判断基準を確認（dev-process-improvement は文書中心リポジトリのため worktree 不要、per-worker ファイル分離で十分）
- 各変更対象ファイルの具体的な変更箇所を特定:
  1. **parallel-dev.md（新規）**: ルールファイル。並列ディスパッチの前提条件・per-worker ファイルパターン・Wave 方式・成果物統合手順を定義
  2. **SKILL.md**: Phase 4 セクションに並列ディスパッチ機構（事前準備・Wave ディスパッチ・事後処理）を追加。L2 への指示に per-worker ファイル情報を含める
  3. **l2-worker.md**: 担当ファイルテーブルに per-worker ファイル（03_work_log_W<N>.md, 07_issues_W<N>.md）を追加。壁打ちフェーズに Worker ID の確認を追加
  4. **02_tasks.md テンプレート**: Set Dispatch Order に Wave/並列情報を反映
  5. **03_work_log.md テンプレート**: per-worker 版テンプレートの参照注記を追加
  6. **manager-common-policy**: §2.2 に per-worker ファイル分離パターンの詳細を追加
  7. **session-flow-policy**: §4.2 に per-worker ファイル前提条件を追加
**判断・気づき**:
- impl-manager は外部リポの worktree + per-worker ファイルのハイブリッド方式だが、l1-manager は per-worker ファイル分離のみで十分
- parallel-dev.md はルールファイル（.claude/rules/）に配置する。§2.2 が既にこのパスを参照している
- テンプレート群は per-worker テンプレート（03_work_log_W_template.md, 07_issues_W_template.md）の新規作成が必要

### [2026-03-17 14:20] 計画項目: タスク分割・コンフリクトマトリクス・Wave 割当の作成
**状態**: 完了
**作業内容**:
- 7タスクに分割（T2-001〜T2-007）
- コンフリクトマトリクスを作成し、競合なしを確認
- Wave 割当: Wave 1（T2-001 新規作成群、並列可）、Wave 2（T2-002〜T2-005 既存ファイル変更群、T2-001 に依存）、Wave 3（T2-006〜T2-007 固定タスク）
**判断・気づき**:
- T2-001（parallel-dev.md）は他全タスクの Read-only 依存先であるため、必ず Wave 1 で先行
- 既存ファイル変更群は SKILL.md と l2-worker.md が相互参照関係にあるが MODIFY 競合はないため同一 Wave で可
- per-worker テンプレート（03_work_log_W_template.md, 07_issues_W_template.md）は T2-004 に含める

---

## 施策フェーズ2: 実施ワーカー作業

## 壁打ちフェーズ [2026-03-17 11:59]

### 理解のサマリー
- タスクの目的: 施策フェーズ2 の T2-001〜T2-007 を実行し、並列ワーカーディスパッチの仕組み（parallel-dev.md ルール、SKILL.md Phase 4 並列ディスパッチ、l2-worker.md per-worker 対応、テンプレート群、ポリシー更新、workflow.md 可視化）を完成させる
- スコープ: Wave 1（T2-001）→ Wave 2（T2-002〜T2-005, T2-007 逐次実行）→ Wave 3（T2-006 固定タスク）
- 完了条件: 全タスク完了、03_work_log.md に作業履歴、04_work_report.md に施策フェーズ2 レポート、07_issues.md に課題記録、コミット・プッシュ済み

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（施策フェーズ1 ゲート通過、02a_task_division.md 施策フェーズ2 セクション作成済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read, Write, Edit, Bash）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
  - l1-impl-manager SKILL.md: 存在確認済み（並列ディスパッチ機構の参考パターン）
  - l1-manager SKILL.md: 存在確認済み（変更対象）
  - l2-worker.md: 存在確認済み（変更対象）
  - manager-common-policy SKILL.md: 存在確認済み（変更対象）
  - session-flow-policy SKILL.md: 存在確認済み（変更対象）
  - docs/workflow.md: 存在確認済み（変更対象）
  - _template/ ディレクトリ: 存在確認済み
  - ブランチ: claude/l1-manager-WG7FF チェックアウト済み

### 不明点・確認事項
確認事項なし：実施開始

### タスク実施計画

1. **Wave 1: T2-001** — parallel-dev.md 新規作成（impl-manager の並列ディスパッチ機構を参考に l1-manager 向けに簡略化）
2. **Wave 2（逐次実行）**:
   - T2-002: l1-manager SKILL.md Phase 4 並列ディスパッチ機構追加
   - T2-003: l2-worker.md per-worker ファイル対応
   - T2-004: テンプレート群更新（per-worker テンプレート新規作成 + 02_tasks.md/03_work_log.md 更新）
   - T2-005: manager-common-policy §2.2 + session-flow-policy §4.2 更新
   - T2-007: docs/workflow.md 並列ディスパッチ可視化
3. **Wave 3: T2-006** — 知見セクション記録 + メタルール横断検証

---

### [2026-03-17 12:00] タスクID: T2-001
**状態**: 完了
**作業内容**:
- `.claude/rules/parallel-dev.md` を新規作成
- §1: 前提条件（Conflict Check Matrix 検証済み・Wave 割当定義済み・per-worker ファイル作成済み）
- §2: per-worker ファイル分離パターン（03_work_log_W<N>.md, 07_issues_W<N>.md）
- §3: Wave 方式の運用ルール（Wave 内は並列、Wave 間は逐次、事前検証チェックリスト）
- §4: 成果物統合手順（課題ファイル統合・作業ログ確認・タスクステータス更新）
- §5: worktree 方式への escalation パス（将来の拡張用フック）
**成果物**: `.claude/rules/parallel-dev.md`

### [2026-03-17 12:10] タスクID: T2-002
**状態**: 完了
**作業内容**:
- l1-manager SKILL.md の Phase 4 に逐次/並列の分岐を追加
- 「Phase 4 並列ディスパッチ手順」セクションを新設（事前準備・Wave ディスパッチ・完了後処理）
- セッションライフサイクル todo パターン1 のステップ10に並列ディスパッチステップを反映
- 関連ファイル一覧に parallel-dev.md を追加
**成果物**: `.claude/skills/l1-manager/SKILL.md`（変更）

### [2026-03-17 12:20] タスクID: T2-003
**状態**: 完了
**作業内容**:
- l2-worker.md の担当ファイルテーブルに per-worker ファイル追加
- 壁打ちフェーズに Worker ID 確認・per-worker ファイル存在確認を追加
- 作業フローに順次/並列の判別条件を明記（Worker ID 指定あり → per-worker ファイル使用）
- 「やること」セクションに per-worker ファイルへの記録を追加
- 関連ファイル一覧に per-worker テンプレート・parallel-dev.md を追加
**成果物**: `.claude/skills/l1-manager/agents/l2-worker.md`（変更）

### [2026-03-17 12:30] タスクID: T2-004
**状態**: 完了
**作業内容**:
- `sessions/initiatives/_template/03_work_log_W_template.md` を新規作成（Worker 情報・壁打ち・作業ログセクション）
- `sessions/initiatives/_template/07_issues_W_template.md` を新規作成（Worker 情報・課題起票セクション）
- 02_tasks.md テンプレートと 03_work_log.md テンプレートは plan-worker により更新済みのため追加変更なし
**成果物**: `_template/03_work_log_W_template.md`, `_template/07_issues_W_template.md`

### [2026-03-17 12:35] タスクID: T2-005
**状態**: 完了（変更なし）
**作業内容**:
- manager-common-policy §2.2 を確認 → plan-worker が per-worker ファイル分離パターン・parallel-dev.md 参照・Wave 完了後処理を追加済み
- session-flow-policy §4.2 を確認 → plan-worker が per-worker ファイル作成の前提条件を追加済み
- 両ファイルとも完了条件を満たしているため、追加変更は不要
**課題・気づき**: plan-worker が関連ファイルを先行更新するパターンが有効（知見として記録済み）

### [2026-03-17 12:40] タスクID: T2-007
**状態**: 完了（変更なし）
**作業内容**:
- docs/workflow.md の Phase 4 セクションを確認 → plan-worker が並列/逐次の判断フロー・Wave 方式・per-worker 分離・統合手順を可視化済み
- 完了条件を満たしているため、追加変更は不要

### [2026-03-17 12:50] タスクID: T2-006
**状態**: 完了
**作業内容**:
- メタルール横断検証を3領域で実施（全合格）
  - フロー記述: parallel-dev.md を参照する全ファイルのフロー記述が実態と一致
  - workflow.md 同期: Phase 4 セクションの並列ディスパッチ可視化が変更内容と整合
  - TG-008 基準連動: parallel-dev.md は `.claude/rules/` 配下であり TG-008 走査対象外。一般チェックでカバー
- 04_work_report.md に施策フェーズ2 実施レポートを作成（知見セクション・メタルール検証結果・転記判断を含む）
- 07_issues.md を確認: 施策フェーズ2 で新規施策横断課題なし。転記対象なし
**成果物**: `04_work_report.md`（施策フェーズ2 実施レポート追記）

---

## 施策フェーズ3: ドメインエージェント深層統合（計画）

## 壁打ちフェーズ [2026-03-17 16:00]

### 理解のサマリー
- タスクの目的: Evaluator にドメインエージェント参照フローを追加し、有効性フィードバックループ（06_eval_report.md → knowledge.md）を構築する。Worker に既に導入済みのドメインエージェント参照パターンを Evaluator に対称的に拡張する
- スコープ: l2-evaluator.md（参照フロー追加）、SKILL.md（evaluator ディスパッチ手順更新）、manager-common-policy §10（§10.5 新設）、05_eval_plan.md テンプレート（参照セクション追加）、06_eval_report.md テンプレート（フィードバックセクション追加）、knowledge.md（Evaluator 向け推奨マッピング追加）、docs/workflow.md（深層統合の可視化）
- 完了条件: 02a_task_division.md に施策フェーズ3 のタスク分割が追記され、03_work_log.md に壁打ちフェーズと作業履歴が記録され、04_work_report.md に計画レポートが記載されている

### 前提条件チェック
- [x] 施策計画（01_plan.md）の内容を理解: 理解済み — 施策フェーズ3 の成功基準は「Evaluator にドメインエージェントが注入され、有効性フィードバックが機能する」
- [x] 提案書（00_proposal.md）の確認: 確認済み — ドメインエージェントがノイズになるリスクに対し、有効性フィードバックで追跡し不要なら除外可能とする対策
- [x] 変更対象ファイル群の特定: 特定済み — 下記調査結果参照

### 変更対象ファイル調査結果

**変更対象**:
1. `.claude/skills/l1-manager/agents/l2-evaluator.md` — 作業フロー step 1 にドメインエージェント参照を追加。l2-worker.md の既存パターン（step 1 で `refs/agency-agents/` を Read）を踏襲
2. `.claude/skills/l1-manager/SKILL.md` — Phase 5 L2-evaluator ディスパッチ手順にドメインエージェント参照の伝達を明記
3. `.claude/skills/manager-common-policy/SKILL.md` — §10.5 を新設し、Evaluator 向けドメインエージェント参照の具体的手順とフィードバック責務を定義
4. `sessions/initiatives/_template/05_eval_plan.md` — ドメインエージェント参照セクションを追加
5. `sessions/initiatives/_template/06_eval_report.md` — ドメインエージェント有効性フィードバックセクションを追加
6. `refs/agency-agents/knowledge.md` — Evaluator 向け推奨マッピングとフィードバック受領構造を追加
7. `docs/workflow.md` — Phase 5 セクションにドメインエージェント参照行追加、フィードバックループの可視化

**参照のみ（Read-only）**:
- `.claude/skills/l1-manager/agents/l2-worker.md` — 既存ドメインエージェント参照パターンの確認（対称性を保つための参照）
- `00_proposal.md`, `01_plan.md` — 背景・計画の参照

### 設計判断

1. **Worker/Evaluator の対称性**: l2-worker.md の step 1 で `02_tasks.md` の「参照ドメインエージェント」Evaluator 向けエージェントを Read するパターンを、l2-evaluator.md にも同じ構造で追加する。ただし Evaluator は「評価に活かす」点が Worker の「作業に活かす」と異なるため、活用方法の記述は Evaluator 固有にする

2. **フィードバックループの設計**: 06_eval_report.md に「ドメインエージェント有効性フィードバック」セクションを新設し、有効だった観点・不要だった観点・推奨更新事項を記録する。L1 がゲート判定時にこの内容を確認し、knowledge.md への反映を判断する

3. **knowledge.md の拡張方針**: 既存の「施策タイプ別推奨マッピング」テーブルに Evaluator 向け推奨列を追加する方式を採用（別建てテーブルではなく、同一テーブルに Worker/Evaluator 両方を含める）。加えて「蓄積された知見」テーブルにフィードバック起源の知見を追加できる構造にする

4. **§10.5 の位置づけ**: §10.3 は Worker/Evaluator 共通の「渡し方」を定義しているが、Evaluator 固有の「活用方法」（評価計画への反映・評価基準への活用・フィードバック責務）は §10.5 として分離する

### 不明点・確認事項
確認事項なし：計画開始

### 分析計画

1. l2-evaluator.md の変更箇所の特定（l2-worker.md の対称パターン分析）
2. SKILL.md の Phase 5 evaluator ディスパッチ変更箇所の特定
3. manager-common-policy §10 の拡張箇所の特定
4. テンプレート群（05_eval_plan.md, 06_eval_report.md）の変更箇所の特定
5. knowledge.md の拡張方針の決定
6. docs/workflow.md の変更箇所の特定
7. タスク分割・コンフリクトマトリクス・Wave 割当の作成

---

### [2026-03-17 16:10] 計画項目: 変更対象の詳細分析
**状態**: 完了
**作業内容**:
- l2-worker.md の既存ドメインエージェント参照パターンを精読（step 1: `02_tasks.md` の「参照ドメインエージェント」セクションを確認 → エージェント `.md` ファイルを Read → 専門知識として参照）
- l2-evaluator.md の現状を精読 — ドメインエージェント参照が一切なし。作業フローは step 1 が `01_plan.md` と `04_work_report.md` の読み取りから開始
- manager-common-policy §10 を精読 — §10.3 で既に「Worker 向けと Evaluator 向けでそれぞれ異なるドメインエージェントを指定できる」と記載されているが、Evaluator 側の具体的手順は未定義
- l1-manager SKILL.md の evaluator ディスパッチ箇所を確認 — Phase 5 セクションの起動時に渡す観点にドメインエージェント情報が含まれていない
- knowledge.md の推奨マッピングを確認 — 全て Worker 向けの推奨のみ。Evaluator 向け推奨列は存在しない
- 05_eval_plan.md テンプレートを確認 — ドメインエージェント参照セクションなし
- 06_eval_report.md テンプレートを確認 — フィードバックセクションなし
- docs/workflow.md の Phase 5 セクションを確認 — Worker 側（Phase 4）には「参照ドメインエージェントがある場合」の記載があるが、Evaluator 側（Phase 5）にはない
**判断・気づき**:
- 全7箇所の変更で新規ファイル作成なし。全て既存ファイルの拡張で完結する
- コンフリクトマトリクス上、全タスクのファイル書き込み先が完全に分離されているため、Wave 1 で5タスク並列が可能
- T3-007（docs/workflow.md）は T3-001 と T3-003 の成果物を参照するため Wave 2 に配置

### [2026-03-17 16:20] 計画項目: タスク分割・コンフリクトマトリクス・Wave 割当の作成
**状態**: 完了
**作業内容**:
- 7タスクに分割（T3-001〜T3-007）
- コンフリクトマトリクスを作成し、競合なしを確認
- Wave 割当: Wave 1（T3-001〜T3-005、並列実行可）、Wave 2（T3-006〜T3-007、Wave 1 完了後）
- 02a_task_division.md に施策フェーズ3 セクションを追記
**判断・気づき**:
- 施策フェーズ2 と異なり新規ファイル作成がないため、タスク構成がシンプル
- Wave 1 の5タスクは全て異なるファイルを MODIFY するため、最大5並列が可能
- フィードバックループの構築は T3-003（policy 定義）、T3-004（テンプレート）、T3-005（knowledge.md 構造）の3タスクにまたがるが、各タスクの担当ファイルが分離されているため並列で問題なし
