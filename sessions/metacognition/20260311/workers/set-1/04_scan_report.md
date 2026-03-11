# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| MC-001 | `_archive/*/04_work_report.md`, `06_eval_report.md` の知見セクション | 完了 |
| MC-004 | `_archive/*/02_tasks.md` + `04_work_report.md` | 完了 |

## MC-001: 施策横断の知見パターン抽出

### 走査概要

- 走査対象: 全64施策の `04_work_report.md`（62件存在）および `06_eval_report.md`（61件存在）
- 知見セクション保有施策: 04_work_report.md 約45件、06_eval_report.md 約42件
- 初期施策（旧フォーマット）や一部施策では知見セクションが未構造化

### 反復パターン一覧

| # | パターン | 出現施策数 | 該当施策（代表例） | 重要度 | アクション候補 |
|---|---------|----------|-----------------|--------|-------------|
| 1 | 連動更新漏れ・更新箇所の網羅性不足 | 20+ | backlog-relationship-analysis, partial-repo-sync, management-structure-review, refine-triage-template, backlog-maintenance-session, workflow-doc-consistency-fix, triage-process-brushup, add-triage-risk-assessment 等 | 高 | ルール強化（下記詳細参照） |
| 2 | チェックリスト駆動パターンの有効性 | 22+ | metacognitive-improvement-enforcement, backlog-maintenance-session, repo-sync-verification-checklist, role-format-guide準拠確認チェックリスト, format-conversion-equivalence, sync-checklist-skill, ルール変更連動更新標準化 等 | 高 | 成功パターンとして横展開 |
| 3 | 関連ファイル一覧セクションの有効性 | 15+ | add-triage-risk-assessment, sync-checklist-skill, ルール変更連動更新標準化, triage-process-brushup, manager-common-policy, repo-sync-verification-checklist 等 | 高 | 新規スキル作成テンプレートへの組み込み |
| 4 | grep/パス参照検証の必要性 | 12+ | partial-repo-sync, management-structure-review, claude-directory最適化, refine-triage-template, roles-agents-migration, readme-consistency-check 等 | 高 | rule-change-checklist の走査対象拡充 |
| 5 | ペアリング対称性要件の維持 | 11+ | refine-triage-template, metacognitive-improvement-enforcement, repo-sync-verification-checklist, backlog-maintenance-session, トリアージ標準ポリシーガイドライン, 課題管理とinbox管理の方法見直し 等 | 中 | 既存ポリシーで対応済み。session-flow-policy §3 に明記 |
| 6 | CSV操作・ステータス更新漏れ | 10+ | workflow-doc-consistency-fix, backlog-archive-matching, 課題管理とinbox管理の方法見直し, backlog-readme-improvement, management-structure-review 等 | 中 | CSV操作のガイドライン強化 |
| 7 | セクション番号・参照の脆弱性 | 10+ | マネージャーロール整備, triage-todo-management, backlog-archive-matching, manager-common-policy, meta-rule-cross-validation-scope 等 | 中 | アンカー名方式への移行を検討 |
| 8 | SDK/CLI 環境差による挙動の違い | 4 | cli-permission-verification, subagent-permission-model, 個人PCローカル環境構築, ai-automation-tool-review | 低 | 改善提案に環境前提の明記を義務化（ISS-027 関連で対応済み） |

### パターン詳細

#### パターン1: 連動更新漏れ・更新箇所の網羅性不足（20施策+, 重要度: 高）

最も高頻度で出現するパターン。ルール・スキル・テンプレート・docs を変更した際に、関連ファイルの更新が漏れる問題。

**具体的な出現形態**:
- スキル定義変更時に workflow.md の更新漏れ
- テンプレートリネーム時に旧番号参照の残存（refine-triage-template）
- パス移動時に docs/ 配下のガイド文書の参照漏れ（management-structure-review, partial-repo-sync）
- 新セッションタイプ追加時に5箇所以上の連動更新が必要（backlog-maintenance-session, repo-sync-verification-checklist）
- ルール変更時にテンプレートとの連動更新漏れ（backlog-relationship-analysis）
- CSV のステータス更新漏れ（workflow-doc-consistency-fix）

**既存の対策と効果**:
- rule-change-checklist（ルール変更連動更新標準化で導入）: 効果あり
- 関連ファイル一覧セクション（ルール変更連動更新標準化で導入）: 効果あり
- session-flow-policy §5.1 チェックリスト: 新セッションタイプ追加時に有効

**残存課題**:
- rule-change-checklist の走査対象に `docs/` が明示されていない
- session-flow-policy §5.1 のチェックリストに triage-standard-policy の全更新箇所が列挙されていない
- CSV ステータス更新は手動依存で、チェックリストに含まれていない

#### パターン2: チェックリスト駆動パターンの有効性（22施策+, 重要度: 高）

課題ではなく成功パターン。チェックリストを用いた作業が高い品質を実現している。

**確認された有効パターン**:
- rule-change-checklist: ルール変更時の連動更新漏れを防止
- session-flow-policy §5.1: 新セッションタイプ追加時の連動更新先をカバー
- format-conversion-checklist: フォーマット変換の等価性検証
- TG-008: ルール定義のポリシーチェック（メタルール）

**横展開の推奨**:
- 新規チェックリスト作成時に「L1/L2-worker/L2-evaluator の3者向けガイド」を含める標準化（format-conversion-equivalence で提起）
- チェックリスト型スキルの自己記述パターンの標準化

#### パターン3: 関連ファイル一覧セクションの有効性（15施策+, 重要度: 高）

連動更新漏れ防止の対策として導入された「関連ファイル一覧」セクションが広く有効に機能している。

**確認された効果**:
- 変更施策で「関連ファイル一覧」を参照して連動更新を実施 → 漏れ防止に寄与
- ポリシー系ファイル（5-9件）とエージェント定義（3-5件）でエントリ数に差がある
- docs/workflow.md は全スキル/エージェント定義に共通して記載

**残存課題**:
- 全スキル/エージェント定義に一覧があるわけではない
- 新規スキル作成テンプレートに「関連ファイル一覧」セクションが含まれていない可能性

#### パターン4: grep/パス参照検証の必要性（12施策+, 重要度: 高）

ファイル移動・リネーム・パス変更を伴う施策で、旧パス参照の残存が繰り返し検出されている。

**具体的な出現形態**:
- `backlog/` を走査対象に含めていなかった（partial-repo-sync）
- `docs/management-system-guide.md` に旧パス参照が残存（management-structure-review）
- rules/ → skills/ 移行時の本文内自己参照の更新漏れ（claude-directory最適化）
- triage-manager SKILL.md に実在しないファイルパス参照（readme-consistency-check）

**改善候補**:
- rule-change-checklist に「ルートレベルの全ディレクトリを走査対象に含めたか」の項目追加
- 「docs/ 配下のガイド文書」を明示的な grep 走査対象に含める

#### パターン5: ペアリング対称性要件の維持（11施策+, 重要度: 中）

worker と evaluator のエージェント定義に同じ構造要素を持たせる要件。

**具体例**:
- triage-evaluator に壁打ちフェーズ・知見記録セクションが欠落していた（トリアージ標準ポリシーガイドラインで検出）
- l2-worker.md と l2-evaluator.md の CSV 転記セクションの対称性維持（課題管理とinbox管理の方法見直し）
- sync-evaluator.md に対称性確認テーブルを含めるパターン（repo-sync-verification-checklist）

**対応状況**: session-flow-policy §3 にペアリング対称性要件が定義済み。主に新セッションタイプ追加時に注意が必要。

#### パターン6: CSV操作・ステータス更新漏れ（10施策+, 重要度: 中）

CSV ファイルの操作と整合性維持に関する課題。

**具体的な出現形態**:
- ISS のステータスが「起票」のまま放置（workflow-doc-consistency-fix）
- CSV 列追加時の全行列数整合性の未検証（課題管理とinbox管理の方法見直し）
- backlog CSV の優先度表記不統一（backlogを俯瞰できる一覧資料作成）
- sed での CSV 操作による引用符破損リスク（課題管理とinbox管理の方法見直し）

**改善候補**:
- CSV 操作は Python csv モジュールを推奨するルール化
- ルール修正で ISS が解消された場合のステータス更新チェックリスト

#### パターン7: セクション番号・参照の脆弱性（10施策+, 重要度: 中）

ファイル内のセクション番号（§N）を参照する設計が、セクション挿入時に脆弱になる問題。

**具体例**:
- dev_manager.md のセクション繰り下げ時の相互参照確認（マネージャーロール整備）
- manager-common-policy への§追加時の影響確認パターン（triage-todo-management）
- 条件付き固定タスクの配置順序にルールがない（meta-rule-cross-validation-scope）

**改善候補**:
- アンカー名方式への移行検討（繰り下げ耐性の向上）
- セクション内のサブヘッダ分類（全施策共通 / 条件付き）

#### パターン8: SDK/CLI 環境差による挙動の違い（4施策, 重要度: 低）

**具体例**:
- deny リストが SDK 環境で非機能（cli-permission-verification）
- tools フィールドが SDK 環境で制限として機能しない（subagent-permission-model）
- `--add-dir` の CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD 設定要件（個人PCローカル環境構築）

**対応状況**: ISS-027 関連、backlog に環境前提明記の施策あり。CLAUDE.md の環境分離ポリシーで対応済み。

## MC-004: プロセス効率分析

### 走査概要

- 走査対象: 全64施策の `02_tasks.md` と `04_work_report.md` のタスク実績テーブル
- 全件自動突合を実施（サンプリングではなく全数分析が可能だったため全数で実施）

### 計画対実績サマリ

| 分類 | 件数 | 割合 |
|------|------|------|
| 両方存在（突合可能） | 60 | 94% |
| 完全一致（差異0） | 37 | 62% |
| 実績増（タスク追加） | 10 | 17% |
| 実績減（タスク統合・スキップ） | 13 | 22% |
| レポートなし（未完了施策） | 2 | 3% |
| タスクファイルなし（初期施策） | 2 | 3% |

### 乖離パターン分類

| 乖離パターン | 件数 | 代表例 | 改善候補 |
|------------|------|--------|---------|
| タイプA: 追加作業の発生 | 10 | coordination-protocol (+5), git-worktree-standardization (+4), role-agent-prompts (+4) | タスク設計時に「検証タスク」「知見記録タスク」の追加を標準化 |
| タイプB: タスク統合・先行タスクで完了済み | 6 | ai-driven-dev-patternsの改善サイクル整備 (-3), roles-agents-migration (-5) | タスク間依存関係の事前分析を計画フェーズで実施 |
| タイプC: 不要タスクのスキップ | 4 | OpenSpec活用専門ロール設定 (-2), boris-claude-rules-adoption (-2) | 計画時に「条件付き実行」タスクを明示 |
| タイプD: スコープ削減 | 3 | session-branch-cleanup-flow (-3), design-process-setup (-3) | L1 の計画精度向上（スコープの適正化） |

### 乖離施策の詳細

#### 実績増（タスク追加）の詳細

| 施策名 | 計画 | 実績 | 差 | 追加理由 |
|--------|------|------|---|---------|
| coordination-protocol | 2 | 7 | +5 | 初期の粗い計画（2タスク）を L2 が7タスクに分解して実施 |
| git-worktree-standardization | 2 | 6 | +4 | 同上。計画が概要レベルだった |
| role-agent-prompts | 1 | 5 | +4 | 同上 |
| コード開発ワークフロー設計の探索 | 1 | 5 | +4 | 探索型施策で計画が概要レベル |
| manager-common-policy | 12 | 13 | +1 | grep 検証タスクの追加 |
| claude-directory最適化 | 10 | 11 | +1 | 本文内参照更新タスクの追加 |
| cli-permission-verification | 9 | 10 | +1 | 追加検証タスク |
| dev-setup-knowledge | 4 | 5 | +1 | 追加検証タスク |
| m6o-es-product-apiドキュメント移動実施 | 6 | 7 | +1 | grep 検証タスクの追加 |
| 課題管理とinbox管理の方法見直し | 9 | 10 | +1 | CSV 操作タスクの追加 |

#### 実績減（タスク統合・スキップ）の詳細

| 施策名 | 計画 | 実績 | 差 | 減少理由 |
|--------|------|------|---|---------|
| roles-agents-migration | 13 | 8 | -5 | 複数タスクが統合され、レポートでは8タスクとして報告 |
| ai-driven-dev-patternsの改善サイクル整備 | 14 | 11 | -3 | 前セッションで作成済みタスクの確認のみ、先行タスクで後続が完了 |
| backlogを俯瞰できる一覧資料作成 | 10 | 7 | -3 | レポートのタスクテーブルに含まれていないタスクあり |
| design-process-setup | 9 | 6 | -3 | スコープ調整による削減 |
| session-branch-cleanup-flow | 9 | 6 | -3 | L2 が6タスクに集約して実施 |
| ルール変更連動更新標準化 | 13 | 10 | -3 | タスク統合による削減 |

### 傾向分析

1. **計画精度は概ね高い**: 62%が完全一致。プロセスの成熟を示す
2. **初期施策の計画粒度が粗い**: +4以上の乖離は初期施策に集中。計画が1-2タスクの概要レベルで、L2 が実施時に分解するパターン
3. **大規模施策（10タスク+）は乖離しやすい**: タスク数13のうち5件が乖離（38%）、タスク数5以下の施策は乖離率が低い
4. **追加タスクの多くは「grep検証」「知見記録」**: プロセス改善の結果として追加された定型タスクが乖離の主因
5. **タスク統合は健全な最適化**: 先行タスクで後続が完了するケースは、実施者の効率的な判断によるもの

### 改善候補

| # | 改善候補 | 期待効果 | 優先度 |
|---|---------|---------|--------|
| 1 | L1 の計画時にタスク粒度の最低ラインを設定（1タスク = 1成果物の原則） | 初期施策の計画精度向上 | 中 |
| 2 | 02_tasks.md テンプレートに「検証タスク」「知見記録タスク」を定型化 | 追加タスクの事前計画化 | 中 |
| 3 | タスク間依存関係の明示（02_tasks.md に依存列を追加） | タスク統合の事前検出 | 低 |

## 課題起票

- 起票件数: 2 件（`07_issues.md` に起票済み）

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | rule-change-checklist の grep 走査対象に `docs/` を明示追加すべき | `.claude/skills/rule-change-checklist/SKILL.md` | 12施策+で docs/ 配下の参照漏れが発生。走査対象ディレクトリの網羅性を高めるため、`docs/` を明示的な走査対象に含めるルール追加を推奨 |
| 2 | CSV 操作時に Python csv モジュールの使用を推奨するルール | `.claude/rules/` | 10施策+で CSV の列追加・更新漏れ・引用符破損のリスクが報告されている。sed/手動編集ではなく Python csv モジュールを標準とするルールが有効 |
| 3 | チェックリスト型スキルに L1/L2-worker/L2-evaluator の3者向けガイドを含める標準化 | `.claude/skills/` 全般 | format-conversion-equivalence で提起。rule-change-checklist には L2-evaluator 向けガイドがない。新規チェックリスト作成時の標準パターンとして整理可能 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | 連動更新漏れ（パターン1）と関連ファイル一覧（パターン3）は表裏一体 | 関連ファイル一覧の導入後に連動更新漏れの報告が減少傾向にある。対策が機能していることを示す。ただし全スキルに一覧があるわけではなく、網羅性に改善余地あり |
| 2 | 計画対実績の乖離率は62%一致（MC-004）であり、プロセスの成熟度は高い | 乖離の主因は「プロセス改善による定型タスクの追加/省略」であり、計画の質的問題ではない。大規模施策のみ計画精度に改善余地がある |
| 3 | 初回メタ認知セッションのため、ベースラインとして記録 | 次回メタ認知セッションでは今回の数値と比較し、改善傾向を追跡可能 |

---
**作成者**: メタ認知ワーカー
**作成日**: 2026-03-11
