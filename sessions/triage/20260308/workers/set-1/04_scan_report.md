# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox | 完了 |
| TG-002 | backlog | 完了 |
| TG-003 | CSV | 完了 |
| TG-004 | initiative | 完了 |
| TG-005 | backlog 関係性分析 | 完了 |
| TG-008 | skills/agents ポリシーチェック | 完了 |
| TG-009 | 情報欠損リスク評価 | スキップ（削除・統合候補なし） |

---

## TG-001: inbox 走査

### 未処理アイテム一覧（8件）

| アイテム | 種別 | 判断 | 理由 |
|---------|------|------|------|
| rule-change-checklist走査対象網羅性追加.md | 気づきエントリ | ルール反映候補 | ISS-042 関連。rule-change-checklist スキルに「パス変更・リネーム施策ではルートレベル全ディレクトリを grep 走査対象に含めたか」の確認項目を追加する提案。スコープが明確で即時反映可能 |
| sync-worker同期先コミット漏れ防止.md | 気づきエントリ | backlog化候補 | sync-worker.md の作業フローに同期先でのコミット・プッシュステップが欠落。修正スコープが小さい（2-3ファイル、各数行）。maintenance 対応も可能だが、sync-manager.md のワーカー成果物確認観点にも追加が必要なため backlog 化を推奨 |
| 全セッションのマネージャーにディスパッチのセットルール展開.md | 気づきエントリ | backlog化候補（大規模） | マネージャーセッション共通ポリシーの策定提案。調査・集約作業が必要で中〜大規模。ユーザーとの壁打ちが必要と明記。ステップ分解・施策分割の検討が前提 |
| 対称性確認テーブルの推奨プラクティス化.md | 気づきエントリ | ルール反映候補 | sync-evaluator.md に含まれた対称性確認テーブルパターンの横展開。session-flow-policy §3 に推奨プラクティスとして追記。l2-evaluator, triage-evaluator にも導入検討 |
| ref_ai-driven-development-poc.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |
| ref_ai-functions.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |
| ref_openspec-official-summary.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |
| ref_個人PCローカル環境構築-手順書.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |

### 気づきエントリ詳細分析

#### 1. rule-change-checklist走査対象網羅性追加.md

- **内容**: partial-repo-sync 施策でパス移動後の grep 検証において backlog/ が走査対象から漏れた事象を踏まえ、rule-change-checklist に走査対象網羅性の確認項目を追加する提案
- **関連**: ISS-042（プロセス改善_課題管理.csv に転記済み）
- **反映先**: `.claude/skills/rule-change-checklist/SKILL.md` のチェックリスト
- **施策規模**: 極小（チェック項目1行追加）
- **推奨アクション**: ルール反映（トリアージマネージャー承認後に maintenance 対応）
- **具体的な追加内容案**: チェックリスト§1 または新セクションとして「パス変更・リネームを含む施策では、ルートレベルの全ディレクトリ（backlog/, inbox/, refs/, issues/ 等）を grep 走査対象に含めたか」

#### 2. sync-worker同期先コミット漏れ防止.md

- **内容**: sync-worker が同期先リポジトリでファイルを書き込んだがコミット・プッシュ・PR作成を行わなかった問題。sync-worker.md の作業フローにステップが未定義
- **対象ファイル**: sync-worker.md（ステップ追加）、sync-manager/SKILL.md（確認観点追加）、docs/workflow.md（同期フロー更新）
- **施策規模**: 小（2-3ファイル、各数行）
- **推奨アクション**: backlog 化。maintenance 対応も可能だが、影響ファイルが複数あるため施策として管理を推奨
- **推奨施策名**: 「sync-worker同期先コミット漏れ防止」

#### 3. 全セッションのマネージャーにディスパッチのセットルール展開.md

- **内容**: triage マネージャーのディスパッチパターン（セットルール）を全セッションのマネージャー共通ルールとして展開したい。共通的なマネージャーセッションのポリシー/ガイドラインをスキルとして用意し、トリアージでチェックする
- **対象リポジトリ**: dev-process-improvement
- **施策規模**: 中〜大（調査・設計・実装の複数ステップ、既存の散在情報の集約が必要）
- **推奨アクション**: backlog 化。ユーザーとの壁打ちが必要と明記されており、施策分割の検討が前提
- **推奨施策名**: 「マネージャーセッション共通ポリシー策定」
- **備考**: 既存の session-flow-policy や triage-standard-policy との関係整理が必要。triage-standard-policy が部分的にこの役割を担っている可能性あり

#### 4. 対称性確認テーブルの推奨プラクティス化.md

- **内容**: sync-evaluator.md に含まれた対称性確認テーブルパターンが有効であると確認された。session-flow-policy §3 に推奨プラクティスとして明記し、既存のエージェント定義にも導入を検討
- **反映先**: `.claude/skills/session-flow-policy/SKILL.md` §3
- **施策規模**: 小（1ファイルに推奨プラクティス追記 + 既存2ファイルへの導入検討）
- **推奨アクション**: ルール反映（session-flow-policy への追記は maintenance 対応可能。l2-evaluator / triage-evaluator への導入は backlog 化を検討）

---

## TG-002: backlog 棚卸し

### データ整合性問題（2件）

| # | 問題 | 施策名 | 詳細 | 推奨アクション |
|---|------|--------|------|-------------|
| 1 | CSV未記載 | ai-driven-dev-patterns-triage-standard-policy作成 | backlog/ にファイル存在するが backlog.csv に未記載 | CSV にエントリを追加する |
| 2 | .mdファイル不在 | リポジトリ間テンプレート同期の検証チェックリスト | backlog.csv にエントリあるが backlog/ に .md ファイルが存在しない | .md ファイルを作成する、または CSV エントリが施策化済み（repo-sync-verification-checklist）であれば CSV から削除 |

### 施策化済みチェック（initiatives/_archive/ との突合）

| # | backlog 施策名 | _archive 内の対応施策 | ステータス | 推奨アクション |
|---|---------------|---------------------|----------|-------------|
| 1 | claude-directory最適化(ai-driven-dev-patterns) | _archive/claude-directory最適化/ | 施策化済みの可能性高い（名前が類似、対象リポ指定の有無が異なる） | 要ユーザー確認。同一施策であれば backlog ファイル削除 + CSV エントリ削除 |

### データ整合性問題#2 の追加分析

`リポジトリ間テンプレート同期の検証チェックリスト` は CSV に「低,候補,dev-process-improvement,2026-03-07,テンプレート同期時の7観点チェックリスト標準化」として記載。`sessions/initiatives/_archive/` に `repo-sync-verification-checklist/` が存在し、これが対応施策である可能性が高い。施策化済みであれば CSV エントリの削除が推奨。

### backlog 変動（前回トリアージ以降）

- 新規追加: ai-driven-dev-patterns_source-of-truth明示.md（1件）

---

## TG-003: CSV 課題管理（起票17件 + 方針確定1件）

### 新規課題（ISS-041〜044）の確認

| ISS-ID | タイトル | 起票日 | 関連施策 | 確認結果 |
|--------|---------|--------|---------|---------|
| ISS-041 | backlog.csv に施策化済みエントリが残存するパターン | 03-08 | triage/20260308 | 確認済み。TG-002 と関連。l1-manager クローズチェックリストへの追加提案。起票内容は妥当 |
| ISS-042 | パス移動施策の grep 検証で走査対象ディレクトリが網羅されていない | 03-08 | partial-repo-sync | 確認済み。inbox 気づき#1 と関連。rule-change-checklist への項目追加で対応可能。issues/ISS-042.md に詳細あり |
| ISS-043 | commit-message.md の2系統共存による運用混乱リスク | 03-08 | sync/20260308 | 確認済み。経過観察が妥当。実運用で混乱が生じた場合に対応 |
| ISS-044 | ai-driven-dev-patterns の連動更新が未実施 | 03-08 | sync/20260308 | 確認済み。次回同期セッションまたは別施策での対応が必要 |

### 既存起票課題（13件）の方針再確認

| ISS-ID | タイトル | 起票日 | 経過回数 | 対応方針案 |
|--------|---------|--------|---------|----------|
| ISS-006 | ロール定義と OpenSpec 開発ライフサイクルの統合が未定義 | 02-23 | 多数 | **保留継続**: OpenSpec ライフサイクル未定義のため着手不可 |
| ISS-013 | Claude Code Agent Teams 機能が worktree ガイドラインで言及されていない | 02-25 | 多数 | **保留継続**: 実験的機能。低優先度 |
| ISS-016 | m6o-es-product-api の .claude/rules/ 向けルールファイル整備 | 02-27 | 多数 | **保留継続**: m6o-es-product-api 側の作業 |
| ISS-019 | claude-directory-guide.md の skills/ 移動検討 | 02-27 | 多数 | **保留継続**: 現時点で rules/ ファイルは2件のみでコンテキスト圧迫は軽微 |
| ISS-020 | config.yaml の tasks ルールのカテゴリ分けが CLI ツールに適合しない | 02-28 | 多数 | **保留継続**: OpenSpec 関連 |
| ISS-021 | spec 作成時にエッジケース・境界条件のシナリオが漏れやすい | 02-28 | 多数 | **保留継続**: OpenSpec 利用時に反映検討 |
| ISS-022 | spec 作成フェーズが openspec サイクルのボトルネック | 02-28 | 多数 | **保留継続**: OpenSpec 関連 |
| ISS-027 | Claude Code Web は1セッション=1リポジトリの制約がある | 03-02 | 多数 | **保留継続**: ローカル環境移行済みで実害なし |
| ISS-032 | CSV ステータスの同期漏れパターン | 03-04 | 4回目 | **施策化検討**: backlog「トリアージセッションのtodo管理義務化」との統合で施策化を推奨 |
| ISS-033 | 成功基準と CSV 対応方針案のスコープ整合 | 03-04 | 4回目 | **保留継続**: l1-manager 改訂時に併せて対応 |
| ISS-038 | CSV列追加時に全既存行の列数整合性を検証すべき | 03-07 | 2回目 | **保留継続**: 次回CSV列変更時に対応 |
| ISS-039 | L1クローズ手順で gate_review の Write と git mv の実行順序に注意が必要 | 03-07 | 2回目 | **保留継続**: 次回 l1-manager 改訂時に対応 |
| ISS-040 | triage-evaluator 壁打ちフェーズの policy 不整合（推奨→必須更新が必要） | 03-07 | 2回目 | **要対応**: triage-standard-policy の適用マトリクスを更新すべき。軽微修正で対応可能 |

### ステータス「方針確定」の課題（1件）

| ISS-ID | タイトル | 確定方針 | 対応方針案 |
|--------|---------|---------|----------|
| ISS-031 | inbox/backlog が ai-driven-dev-patterns と dev-process-improvement の両方に存在する二重構造 | 当面は二重構造を許容。README.md でスコープ明記 | **維持**: 方針確定済み。経過観察 |

### 総括

- 起票17件中、長期保留が多い（ISS-006/013/016/019/020/021/022/027: 8件）。これらは OpenSpec 関連・プラットフォーム制約・外部リポジトリ関連であり、dev-process-improvement 側で即時対応が困難
- 新規4件（ISS-041〜044）は全て起票内容が妥当。経過観察で対応可能
- ISS-032 は4回目の確認。backlog「トリアージセッションのtodo管理義務化」との統合施策化を改めて推奨
- ISS-040 は2回目の確認。軽微修正で対応可能（maintenance 対応推奨）

---

## TG-004: initiative 状態確認

### 進行中施策

| 施策名 | フェーズ | 状態 | 特記事項 |
|--------|---------|------|---------|
| （進行中施策なし） | - | - | initiatives/ 直下は _archive/ と _template/ のみ |

### 前回トリアージ以降の変動

- partial-repo-sync 施策が完了・アーカイブ済み
- sync-checklist-skill 施策が完了・アーカイブ済み
- repo-sync-verification-checklist 施策が完了・アーカイブ済み

---

## TG-005: backlog 関係性分析（新規追加1件）

### 新規アイテム: ai-driven-dev-patterns_source-of-truth明示

| 観点 | 分析結果 |
|------|---------|
| 施策概要 | ai-driven-dev-patterns の CLAUDE.md に Source of Truth 明示ルールを追加（roles/ 配下が正の情報源と明記） |
| 対象リポ | ai-driven-dev-patterns |
| 施策規模 | 小（ルール追加1件） |
| 起票元 | design-process-setup 施策の gate_review |

### 既存アイテムとの関係性

| # | 関連 backlog アイテム | 関係性 | 影響 |
|---|---------------------|--------|------|
| 1 | claude-directory最適化(ai-driven-dev-patterns) | 補完関係: 対象リポが同じ。.claude/ 配下構成改善と Source of Truth 明示は独立だが関連 | 低（独立実施可能） |
| 2 | roles-agents移行(ai-driven-dev-patterns) | 実施順序に考慮が必要: roles/ → agents/ 移行後は Source of Truth の定義先が変わる | 中（roles-agents移行を先行する場合、source-of-truth明示の反映先も agents/ に変更が必要） |
| 3 | ガイドラインとルールファイルの二重管理リスク対策 | 関連テーマ: 二重管理リスクと Source of Truth 明示は同じ問題空間 | 低（異なるリポジトリ・異なるスコープ） |

### 分析結論

- 独立施策として成立する（スコープが明確かつ小規模）
- roles-agents移行との実施順序に注意が必要だが、統合の必要はない
- 重複候補なし

---

## TG-008: セッション構造標準ポリシーチェック

### 走査結果サマリ
- 走査対象ファイル数: 13件（前回6件 + 新規7件）
  - ロール定義: 9件（l1系3件、triage系3件、sync系3件）
  - ポリシー/チェックリスト系: 4件（session-flow-policy, triage-standard-policy, rule-change-checklist, repo-sync-checklist）
- 前回トリアージ（20260307-3）以降の skills 変更: 7コミット（新規スキル6件追加）
- 不適合件数: 1件（推奨: 1件）— 前回から継続（ISS-040）

### ファイル別チェック結果（ロール定義9件）

| ファイル | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール | 総合判定 |
|---------|:-------------:|:----------:|:--------:|:----------:|:-------:|
| l1-manager/SKILL.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-worker.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-evaluator.md | OK | OK | OK | OK | OK |
| triage-manager/SKILL.md | OK | OK | OK | OK | OK |
| triage-manager/agents/triage-worker.md | OK | OK | OK | OK | OK |
| triage-manager/agents/triage-evaluator.md | OK（注1） | OK | OK | OK | OK（注1） |
| sync-manager/SKILL.md | OK | OK | OK | OK | OK |
| sync-manager/agents/sync-worker.md | OK | OK | OK | OK | OK |
| sync-manager/agents/sync-evaluator.md | OK | OK | OK | OK | OK |

**注1**: triage-evaluator の壁打ちフェーズは triage-standard-policy で「推奨」だが実装では「必須」的に記述。ISS-040 として既に起票済み（前回 20260307-3）。policy 側の更新待ち。

### ポリシー/チェックリスト系ファイル（4件）

| ファイル | 関連ファイル一覧 | 内容の整合性 | 総合判定 |
|---------|:------------:|:---------:|:-------:|
| session-flow-policy/SKILL.md | あり（12件） | triage-standard-policy と整合 | OK |
| triage-standard-policy/SKILL.md | あり（11件） | sync 系が適用マトリクスに追加済み | OK |
| rule-change-checklist/SKILL.md | あり（4件） | l1-manager, l2-worker との連動が明記 | OK |
| repo-sync-checklist/SKILL.md | あり（4件） | sync-manager, sync-worker, sync-evaluator との連動が明記 | OK |

### 新規追加ファイルの詳細チェック

#### sync-manager/SKILL.md
- A: 壁打ち（事前調査）必須、計画（立案）必須、ゲート判定必須、知見集約ルーティング必須 → 全て準拠
- B: sync-worker → sync-evaluator の起動順序が明記。成果物確認観点あり → 準拠
- C: 課題集約手順が明記（07_issues.md → CSV転記）。知見集約手順が明記 → 準拠
- D: やること/やらないこと/担当ファイルテーブルが完備 → 準拠

#### sync-manager/agents/sync-worker.md
- A: 壁打ちフェーズ必須（03_work_log.md）、作業履歴必須、課題起票必須、気づき記録必須（04_sync_report.md「同期中の知見」）、レポート必須 → 全て準拠
- B: sync-evaluator とのペアリング。成果物チェーン: 04_sync_report.md が evaluator の入力 → 準拠
- C: 課題起票は 07_issues.md 経由。知見記録に「ルール化候補」「参考情報」分類テーブルあり → 準拠
- D: やること/やらないこと/担当ファイルテーブル/停止ルール（フォーマット付き）が完備 → 準拠

#### sync-manager/agents/sync-evaluator.md
- A: 壁打ちフェーズ必須（05_eval_plan.md）、評価計画あり、評価基準あり、レポート必須、気づき記録必須（06_eval_report.md「評価中の知見」） → 全て準拠
- B: sync-worker とのペアリング。対称性確認テーブルが明示的に含まれている → 準拠（優良）
- C: 課題起票は 07_issues.md 経由。知見記録に分類テーブルあり → 準拠
- D: やること/やらないこと/担当ファイルテーブル/停止ルール完備 → 準拠

### 前回からの差分

- skills 新規追加: 6件（sync-manager, sync-worker, sync-evaluator, session-flow-policy, rule-change-checklist, repo-sync-checklist）
- 新規 roles/*.md: なし
- 前回検出の不適合（ISS-040）: 未解消（policy 更新待ち）
- 全新規ファイルが A〜D チェック項目に準拠していることを確認

### 不適合の詳細

| # | ファイル | チェック項目 | 不適合内容 | 重大度 | CSV起票 |
|---|---------|------------|----------|--------|---------|
| 1 | triage-standard-policy/SKILL.md | A.ライフサイクル（適用マトリクス） | triage-evaluator の壁打ちが「推奨」だが実装は「必須」 | 推奨 | ISS-040（起票済み・前回から継続） |

---

## TG-009: 情報欠損リスク評価

削除・統合候補なし：スキップ

TG-002 で検出した整合性問題は「CSV エントリの追加/削除」または「.md ファイルの作成/削除」であり、既存ファイルの削除・統合ではないため、情報欠損リスク評価の対象外。

---

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票済み）— 前回セッションからの継続
- 新規起票: 0 件（本セッションでの新規課題発見なし）
- 事前調査〜スキャンレポート間の件数記載不整合: 前回評価者指摘の issue が 07_issues.md に記載済み

---

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 対称性確認テーブルの標準化 | session-flow-policy/SKILL.md §3 | sync-evaluator.md に含まれた対称性確認テーブルが品質向上に有効。session-flow-policy §3 のエージェント定義必須要素に「推奨: evaluator 定義に対称性確認テーブルを含める」を追記すべき（inbox 気づきエントリと一致） |
| 2 | rule-change-checklist の走査対象網羅性項目 | rule-change-checklist/SKILL.md | パス変更・リネーム施策での走査対象漏れ防止のため、チェックリストに「ルートレベル全ディレクトリの走査確認」項目を追加すべき（inbox 気づきエントリと一致） |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | CSV 起票課題の長期滞留パターン | ISS-006/013/016/019/020/021/022/027 の8件が起票から10日以上経過。OpenSpec 関連・外部依存の課題は「保留」ステータスの導入を検討する価値あり |
| 2 | 新規スキル追加時の triage-standard-policy 適用マトリクス更新が適切に行われている | sync 系3ロールが適用マトリクスに正しく追加されている。session-flow-policy §5.1 のチェックリストが機能している証拠 |
| 3 | inbox 気づきエントリの品質が向上 | 4件とも具体的な反映先・修正スコープが明記されており、処理判断が容易。セッション終了時の気づき記録プロセスが定着している |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-08
