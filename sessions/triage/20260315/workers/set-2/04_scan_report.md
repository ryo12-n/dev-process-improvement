# スキャンレポート: Set-2

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-003 | CSV ステータス「起票」棚卸し | 完了 |
| TG-004 | initiative 状態確認 | 完了 |
| TG-007 | README 整合性チェック | 完了 |

---

## TG-003: CSV 起票アイテム棚卸し

### 概要
- ステータス「起票」: 27件（タスク指示は24件だが、ISS-056〜058 の3件が追加されているため27件）
- ステータス「方針確定」: 1件（ISS-031）

### 起票アイテム一覧（経過日数・分類）

#### 長期起票（14日超）: 7件 --- 対応方針検討が必要

| ISS-ID | 起票日 | 経過日数 | 優先度 | タイトル | 関連施策 | 対応方針の検討 |
|--------|--------|---------|--------|---------|---------|-------------|
| ISS-006 | 2026-02-23 | 20日 | 中 | ロール定義と OpenSpec 開発ライフサイクルの統合が未定義 | role-agent-prompts (archived) | 保留継続が妥当。openspec ライフサイクル自体が未定義のため前提条件未充足。クローズまたは低優先度への降格を検討 |
| ISS-013 | 2026-02-25 | 18日 | 低 | Agent Teams 機能が worktree ガイドラインで未言及 | git-worktree-standardization (archived) | 知見として維持。worktree ガイドラインが参考資料（ドラフト）のため、次回改訂時に反映する方針で問題なし |
| ISS-016 | 2026-02-27 | 16日 | 中 | m6o-es-product-api の .claude/rules/ 向けルールファイル整備 | m6o-es-product-apiドキュメント整理 (archived) | 外部リポジトリ作業のため CLI 環境でのみ実施可能。backlog 化 or 保留 |
| ISS-019 | 2026-02-27 | 16日 | 低 | claude-directory-guide.md の skills/ 移動検討 | claude-directory-structure-rules (archived) | 低優先度。現時点で claude-directory-guide.md は存在しない可能性あり。実態確認の上でクローズ検討 |
| ISS-020 | 2026-02-28 | 15日 | 低 | config.yaml の tasks ルールのカテゴリ分けが CLI ツールに適合しない | openspec-code-trial (archived) | openspec 固有の知見。保留継続 |
| ISS-021 | 2026-02-28 | 15日 | 低 | spec 作成時にエッジケース・境界条件のシナリオが漏れやすい | openspec-code-trial (archived) | openspec 固有の知見。保留継続 |
| ISS-022 | 2026-02-28 | 15日 | 中 | spec 作成フェーズが openspec サイクルのボトルネック | openspec-code-trial (archived) | openspec 固有の知見。保留継続 |

#### 中期起票（7〜14日）: 12件

| ISS-ID | 起票日 | 経過日数 | 優先度 | タイトル | 関連施策 | 状態 |
|--------|--------|---------|--------|---------|---------|------|
| ISS-027 | 2026-03-02 | 13日 | 高 | Claude Code Web は1セッション=1リポジトリの制約 | dev-process-improvementリポジトリ分離 | 環境制約の事実記録。SDK マルチリポ対応待ち |
| ISS-032 | 2026-03-04 | 11日 | 低 | CSV ステータスの同期漏れパターン | workflow-doc-consistency-fix (archived) | ISS-055 と重複する可能性あり。統合検討 |
| ISS-033 | 2026-03-04 | 11日 | 低 | 成功基準と CSV 対応方針案のスコープ整合 | workflow-doc-consistency-fix (archived) | 知見として維持 |
| ISS-038 | 2026-03-07 | 8日 | 低 | CSV列追加時の列数整合性検証 | 課題管理とinbox管理の方法見直し (archived) | 知見として維持 |
| ISS-039 | 2026-03-07 | 8日 | 低 | L1クローズ手順の Write/git mv 実行順序 | 課題管理とinbox管理の方法見直し (archived) | 知見として維持 |
| ISS-042 | 2026-03-08 | 7日 | 中 | grep 走査対象ディレクトリの網羅性 | partial-repo-sync (archived) | ISS-054 と関連。rule-change-checklist 改善で対応可能 |
| ISS-043 | 2026-03-08 | 7日 | 低 | commit-message.md の2系統共存リスク | sync/20260308 | 経過観察中 |
| ISS-044 | 2026-03-08 | 7日 | 中 | ai-driven-dev-patterns の連動更新未実施 | sync/20260308 | 次回同期セッションで対応 |
| ISS-045 | 2026-03-08 | 7日 | 中 | SDK 環境で settings.json allow/deny が機能しない | subagent-permission-model (archived) | 知見。運用ガイド記載済み |
| ISS-046 | 2026-03-08 | 7日 | 低 | エージェント定義 tools フィールドが SDK で機能しない | subagent-permission-model (archived) | 知見。運用ガイド記載済み |
| ISS-047 | 2026-03-08 | 7日 | 中 | deferred tools が tools フィールドの制限を迂回 | cli-permission-verification (archived) | 知見。ガイド記載済み |
| ISS-049 | 2026-03-08 | 7日 | 中 | deny リストは CLI 環境で唯一の強制的制限 | cli-permission-verification (archived) | 知見。運用継続 |

#### 直近起票（7日未満）: 8件

| ISS-ID | 起票日 | 経過日数 | 優先度 | タイトル | 関連施策 | 状態 |
|--------|--------|---------|--------|---------|---------|------|
| ISS-050 | 2026-03-08 | 7日 | 中 | deny リスト設計時の Read/Write/Edit 3ツール網羅 | cli-permission-verification (archived) | rule-change-checklist 改善で対応可能 |
| ISS-052 | 2026-03-11 | 4日 | 中 | gate_review ルーティング宣言の未実行率22% | メタ認知20260311 | l1-manager クローズ手順強化が必要。施策化候補 |
| ISS-053 | 2026-03-11 | 4日 | 中 | 知見型 CSV ルーティングが構造的に転記漏れしやすい | メタ認知20260311 | ISS-052 と同時対応可能 |
| ISS-054 | 2026-03-11 | 4日 | 中 | rule-change-checklist の grep 走査対象に docs/ 未含有 | メタ認知20260311 | ISS-042 と統合して rule-change-checklist 改善施策として対応可能 |
| ISS-055 | 2026-03-11 | 4日 | 中 | CSV ステータス更新漏れの検出・防止メカニズム未整備 | メタ認知20260311 | ISS-032 と関連。トリアージ TG 走査項目への追加 or rule-change-checklist 改善 |
| ISS-056 | 2026-03-12 | 3日 | 低 | manager-common-policy §1 に l1-impl-manager 未追加 | l1-impl-manager-session (archived) | 軽微修正。maintenance コミットで対応可能 |
| ISS-057 | 2026-03-12 | 3日 | 低 | triage-standard-policy §3.2 カテゴリラベル「E」重複 | l1-impl-manager-session (archived) | 軽微修正。maintenance コミットで対応可能 |
| ISS-058 | 2026-03-13 | 2日 | 低 | GHA run ブロックで ${{ }} 式の直接展開 | backlog-auto-initiative-gha (archived) | 低リスク。次回 GHA 修正時に対応 |

### ISS-031（方針確定）の確認

| ISS-ID | 起票日 | ステータス | タイトル | 確定方針 | 確認結果 |
|--------|--------|----------|---------|---------|---------|
| ISS-031 | 2026-03-04 | 方針確定 | inbox/backlog の二重構造 | 当面は二重構造を許容。README でスコープを明記 | 方針通り運用中。変更不要 |

### 対応方針の分類サマリ

| 分類 | 件数 | ISS-ID |
|------|------|--------|
| 保留継続（前提条件未充足） | 4件 | ISS-006, ISS-020, ISS-021, ISS-022 |
| 知見として維持（対応不要） | 9件 | ISS-013, ISS-027, ISS-033, ISS-038, ISS-039, ISS-043, ISS-045, ISS-046, ISS-049 |
| 施策化候補（施策として対応） | 5件 | ISS-016, ISS-042+ISS-054, ISS-052+ISS-053 |
| 軽微修正（maintenance対応可能） | 3件 | ISS-056, ISS-057, ISS-058 |
| 連動更新待ち | 1件 | ISS-044 |
| ISS-032+ISS-055 統合検討 | 2件 | ISS-032, ISS-055 |
| rule-change-checklist 改善で対応 | 2件 | ISS-047, ISS-050 |
| 経過観察・保留 | 1件 | ISS-019 |

---

## TG-004: initiative 状態確認

### 全10件の状態サマリ

| # | initiative名 | 状態 | ゲート通過 | アーカイブ可否 | 備考 |
|---|-------------|------|----------|-------------|------|
| 1 | automation-manager-session | ゲート通過・クローズ済み | 2026-03-13 | 可 | 横展開チェックリスト全完了 |
| 2 | claude-code-plugin-skills-survey | ゲート通過・クローズ済み | 2026-03-13 | 可 | 横展開チェックリスト全完了 |
| 3 | impl-worktree-parallel | ゲート通過・クローズ済み | 2026-03-13 | 可 | 横展開チェックリスト全完了 |
| 4 | phase-gate-standardization | ゲート通過・クローズ済み | 2026-03-15 | 可 | 横展開チェックリスト全完了 |
| 5 | sessionstart-hook-branch-cleanup | ゲート通過・クローズ済み | 2026-03-13 | 可 | 横展開チェックリスト全完了 |
| 6 | sync-worker-target-commit | 計画済み・未着手 | 未 | 不可 | 全タスク未着手。BL-020 進行中 |
| 7 | triage-phase-gate-and-gha-sync | 計画済み・未着手 | 未 | 不可 | 全タスク未着手 |
| 8 | backlog-id-and-issue-template | 計画済み・未着手 | 未 | 不可 | 08_gate_review.md 不存在 |
| 9 | impl-worker-worklog-reliability | 計画済み・未着手 | 未 | 不可 | 08_gate_review.md 不存在 |
| 10 | external-repo-cleanup-on-demand | 作業完了・評価待ち | 未 | 不可 | work_report 完成、eval_report テンプレート状態 |

### アーカイブ候補5件: クローズチェックリスト確認

| チェック項目 | automation-manager-session | claude-code-plugin-skills-survey | impl-worktree-parallel | phase-gate-standardization | sessionstart-hook-branch-cleanup |
|------------|:---:|:---:|:---:|:---:|:---:|
| ゲート通過判定 | OK | OK | OK | OK | OK |
| 横展開チェックリスト完了 | OK | OK | OK | OK | OK |
| 必須把握事項記載 | OK (2件) | OK (3件) | OK (3件) | OK (3件) | OK (3件) |
| 次施策候補記載 | OK (1件) | OK (2件) | OK (1件) | OK (1件) | OK (1件) |
| ルーティング実行確認 | OK | OK | OK | OK | OK |
| CSV転記確認 | OK (課題なし) | OK (課題なし) | OK (課題なし) | OK | OK (課題なし) |
| backlog.csv エントリ確認 | 要確認 (BL-031) | 要確認 (BL-032) | N/A | N/A | N/A |

### backlog.csv 整合性の問題

| BL-ID | 施策名 | backlog.csv ステータス | 施策ディレクトリ | 問題 |
|-------|--------|---------------------|----------------|------|
| BL-031 | automation-managerセッション作成 | 候補 | automation-manager-session | ステータスが「候補」のまま。「完了」に更新済みだが、施策化済みエントリとして削除が必要 |
| BL-032 | Claude Code標準plugin・skills情報整理 | 完了 | claude-code-plugin-skills-survey | ステータスは「完了」だがエントリが残存。施策化済みエントリとして削除が必要 |

### 進行中施策の詳細

#### sync-worker-target-commit
- **状態**: L1計画完了、ワーカー未ディスパッチ
- **タスク**: T-001〜T-005 全て未着手
- **backlog**: BL-020 ステータス「進行中」
- **所見**: 施策ディレクトリは作成済みだが作業が全く進行していない

#### triage-phase-gate-and-gha-sync
- **状態**: L1計画完了、ワーカー未ディスパッチ
- **タスク**: T-001〜T-008 全て未着手
- **backlog**: backlog.csv にエントリなし（施策化時に削除済みと推定）
- **所見**: 施策ディレクトリは作成済みだが作業が全く進行していない

### 状態不明施策の詳細

#### backlog-id-and-issue-template
- **状態**: L1計画完了、ワーカー未ディスパッチ
- **ファイル**: 00_proposal.md, 01_plan.md, 02_tasks.md のみ（最小構成）
- **タスク**: TASK-001〜TASK-005 全て未着手
- **backlog**: backlog.csv にエントリなし
- **所見**: 08_gate_review.md が不存在だが、まだワーカーディスパッチ前のため正常

#### impl-worker-worklog-reliability
- **状態**: L1計画完了、ワーカー未ディスパッチ
- **ファイル**: 00_proposal.md, 01_plan.md, 02_tasks.md のみ（最小構成）
- **タスク**: T-001〜T-005 全て未着手
- **backlog**: backlog.csv にエントリなし
- **所見**: 08_gate_review.md が不存在だが、まだワーカーディスパッチ前のため正常

#### external-repo-cleanup-on-demand
- **状態**: L2-worker 作業完了、L2-evaluator 未ディスパッチ
- **ファイル**: 全8ファイル存在。04_work_report.md に実績あり（T-001〜T-006全完了）。06_eval_report.md はテンプレート状態
- **08_gate_review.md**: テンプレート状態（ゲート判定未実施）
- **所見**: 評価者のディスパッチが止まっている中間状態。L1 が評価者をディスパッチすればクローズ可能

---

## TG-007: README 4セクション整合性チェック

### .claude/skills/ 全スキルディレクトリ一覧（19件）

#### 起動型スキル（user-invocable: true）: 11件

| # | スキルディレクトリ | README 記載 | 備考 |
|---|------------------|:-----------:|------|
| 1 | l1-manager | あり | ディレクトリ構成図・セッション種別・スキルテーブル全てに記載 |
| 2 | triage-manager | あり | 同上 |
| 3 | sync-manager | あり | 同上 |
| 4 | metacognition-manager | あり | 同上 |
| 5 | backlog-maintenance-manager | あり | 同上 |
| 6 | fork-sync | あり | 同上 |
| 7 | l1-impl-manager | なし | コード実装専用マネージャー。起動型だが未記載 |
| 8 | automation-manager | なし | 自動化マネージャー。起動型だが未記載 |
| 9 | config-optimizer-manager | なし | config最適化マネージャー。起動型だが未記載 |
| 10 | repo-sync-checklist | なし | リポジトリ間同期チェックリスト。user-invocable: true だが未記載 |
| 11 | session-flow-policy | なし | セッションフロー作成ポリシー。user-invocable: false と思われたが SKILL.md では false。再確認→ false であった。起動型は10件に修正 |

修正: session-flow-policy は user-invocable: false。起動型は **10件**。

#### 非起動型スキル（user-invocable: false）: 9件

| # | スキルディレクトリ | README 記載 | 備考 |
|---|------------------|:-----------:|------|
| 1 | manager-common-policy | なし | マネージャー共通ポリシー |
| 2 | triage-standard-policy | なし | トリアージ標準ポリシー |
| 3 | session-flow-policy | なし | セッションフロー作成ポリシー |
| 4 | rule-change-checklist | なし | ルール変更連動更新チェックリスト |
| 5 | format-conversion-checklist | なし | フォーマット変換同等性チェックリスト |
| 6 | external-repo-cleanup | なし | 外部リポジトリブランチ整理（オンデマンド） |
| 7 | builtin-skills-reference | なし | ビルトインスキル評価リファレンス |
| 8 | plugin-reference | なし | プラグイン評価リファレンス |
| 9 | gha-guideline | なし | GHA運用ガイドライン |

### セクション別整合性チェック結果

#### (1) ディレクトリ構成図

| チェック項目 | 結果 | 詳細 |
|------------|:----:|------|
| 記載スキル数 | 6/19 | l1-manager, triage-manager, sync-manager, metacognition-manager, backlog-maintenance-manager, fork-sync のみ |
| 未記載の起動型スキル | 4件 | l1-impl-manager, automation-manager, config-optimizer-manager, repo-sync-checklist |
| 未記載の非起動型スキル | 9件 | 全て未記載 |
| 方針の明示 | 部分的 | 「起動型のみ記載」とコメントあり。ただし起動型4件が漏れている |

#### (2) セッション種別テーブル

| チェック項目 | 結果 | 詳細 |
|------------|:----:|------|
| 記載セッション数 | 6/10 | イニシアティブ, トリアージ, 同期, メタ認知, バックログメンテナンス, fork同期 |
| 未記載の起動型セッション | 4件 | l1-impl-manager, automation-manager, config-optimizer-manager, repo-sync-checklist |

未記載の起動型セッション詳細:

| スキル | セッション種別 | 目的 |
|--------|------------|------|
| l1-impl-manager | 実装マネージャー | 外部リポジトリへのコード実装の4フェーズオーケストレーション |
| automation-manager | 自動化マネージャー | 自動化候補の探索・再評価・進捗追跡 |
| config-optimizer-manager | config最適化マネージャー | .claude/ 配下の設定ファイル分析・最適化提案 |
| repo-sync-checklist | 同期チェックリスト | リポジトリ間同期作業時のチェックリスト |

#### (3) AI向けスキル定義テーブル

| チェック項目 | 結果 | 詳細 |
|------------|:----:|------|
| 記載スキル数 | 6/19 | l1-manager, triage-manager, sync-manager, metacognition-manager, backlog-maintenance-manager, fork-sync |
| テーブル記載方針 | 起動型マネージャー+fork-sync | 非起動型は記載対象外と推定 |
| 起動型の欠落 | 4件 | l1-impl-manager, automation-manager, config-optimizer-manager, repo-sync-checklist |

#### (4) ドキュメントマップ

| チェック項目 | 結果 | 詳細 |
|------------|:----:|------|
| docs/ ファイル数 | 6/6 | workflow.md, implementation.md, management-system-guide.md, subagent-permission-guide.md, coordination-protocol-guideline.md, git-worktree-guideline.md 全て記載 |
| 整合性 | OK | 実際の docs/ ディレクトリの内容と一致 |

### 総合判定

README.md のセクション1〜3で起動型スキル4件（l1-impl-manager, automation-manager, config-optimizer-manager, repo-sync-checklist）が未記載。セクション4（ドキュメントマップ）は網羅されている。

---

## 課題起票

- 起票件数: 1件（`07_issues.md` に起票済み）
- README起動型スキル未記載（4件）の整合性課題

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 施策ゲート通過後のアーカイブ移動が遅延するパターン | l1-manager クローズ手順 | 5件のアーカイブ候補が sessions/initiatives/ に滞留。ゲート通過からアーカイブまでの期間上限をルール化する余地あり |
| 2 | backlog.csv の施策化済みエントリ残存（BL-031） | l1-manager クローズ手順 | ISS-041 で対応済みのはずだが BL-031 が「候補」ステータスのまま残存。チェックリストの実効性に課題 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | CSV 起票27件中、「知見」種別の課題は対応不要なものが多い | ISS-013, ISS-038, ISS-039, ISS-045, ISS-046, ISS-047, ISS-049 等。知見型課題はクローズ基準が曖昧で「起票」のまま滞留しやすい。知見型課題の自動クローズ基準（例: 運用ガイド記載済みならクローズ）を検討する余地あり |
| 2 | external-repo-cleanup-on-demand が評価待ち中間状態で放置 | L2-worker 完了後に L2-evaluator がディスパッチされていない。L1 のセッション中断が原因と推定。再開時の検知メカニズムが不足 |
| 3 | 起票アイテムの件数がタスク指示（24件）と実態（27件）で不一致 | 事前調査時点から走査実施までに新規起票があった可能性。または事前調査の集計誤差 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
