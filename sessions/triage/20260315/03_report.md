# トリアージ振り返りレポート: 2026-03-15

## サマリ

前回トリアージ（20260312）から3日経過。inbox 23件の分類、backlog 53件の突合・関係性分析、CSV 27件の棚卸し、initiative 10件の状態確認、ルール/workflow 整合性チェック、セッション構造ポリシーチェック、GHA ↔ Skills 整合性チェックを6セット（5フェーズ）で実施した。主要な発見: (1) inbox から backlog 候補12件・ルール反映8件を抽出、(2) manager-common-policy の適用対象不整合（7マネージャー中2件欠落）を検出・修正、(3) README に起動型スキル4件の未記載を検出・修正、(4) backlog 関係性分析で重複3組・依存8組・統合候補6グループを特定、(5) GHA マッピングにドリフトなし（CRITICAL 0/WARNING 0）。全 TG タスク完了（TG-009 はスキップ）。

## Worker Set サマリ

| Set | 担当 TG タスク | 評価結果 | 備考 |
|-----|--------------|---------|------|
| set-1 | TG-001 | 条件付き承認 | inbox 23件分類。軽微修正2点（件数不一致・二重分類）→集約時修正 |
| set-2 | TG-003, TG-004, TG-007 | 承認 | CSV 27件棚卸し・initiative 10件確認・README 整合性 |
| set-3 | TG-002 | 承認 | backlog 53件突合。施策化済み3件・不整合2件・未記入14件検出 |
| set-4 | TG-006, TG-008 | 承認（補完あり） | manager-common-policy 不整合検出。評価者が §9 補完 |
| set-5 | TG-005 | 承認 | backlog 関係性分析。重複3組・依存8組・統合6グループ |
| set-6 | TG-009 | スキップ | 削除候補が CSV メタデータ修正のみのため不要 |
| set-7 | TG-010 | 条件付き承認 | GHA 整合性。サマリ件数修正（6→7）→集約時修正 |

## 走査結果

### inbox（TG-001）

全23件を分類。評価者指摘の修正を反映: backlog候補は12件（サマリ修正）、#4 は「対応不要」に一本化（二重分類解消）。

| # | ファイル名 | 分類 | 備考 |
|---|-----------|------|------|
| 1 | automation-manager-common-policy-addition.md | ルール反映 | manager-common-policy §1 へ追加 |
| 2 | automation-session-flow-policy-addition.md | ルール反映 | session-flow-policy §5 へ追加 |
| 3 | claude-code-action-version-tracking.md | backlog候補 | 優先度: 低 |
| 4 | conditional-checklist-pattern.md | 対応不要 | BL-045 検討時に参照可能 |
| 5 | docs-workflow-initiative-gha-update.md | backlog候補 | 優先度: 中 |
| 6 | gha-backlog-maintenance-automation.md | backlog候補 | 優先度: 中 |
| 7 | gha-guideline-other-workflows.md | backlog候補 | 優先度: 中 |
| 8 | gha-metacognition-automation.md | backlog候補 | 優先度: 中 |
| 9 | gha-prompt-shell-expansion-caveat.md | ルール反映 | gha-guideline SKILL.md へ注意事項追記 |
| 10 | gha-session-prompt-conversion-pattern.md | backlog候補 | 優先度: 低 |
| 11 | gha-workflow-security-checklist.md | ルール反映 | .claude/rules/ 新規 |
| 12 | git-rebase-conflict-handling-guideline.md | ルール反映 | .claude/rules/ 新規 |
| 13 | l1-pre-applied-template-task-design.md | backlog候補 | 優先度: 低 |
| 14 | l1-skill-file-enumeration-check.md | ルール反映 | l1-manager タスク作成ガイドへ追記 |
| 15 | plugin-high-applicability-trial.md | backlog候補 | 優先度: 中（BL-032 後続） |
| 16 | reference-doc-granularity-rule.md | backlog候補 | 優先度: 低 |
| 17 | refs-metadata-requirement.md | ルール反映 | CLAUDE.md refs/ セクションへ追記 |
| 18 | refs-routing-template-unification.md | backlog候補 | 優先度: 中 |
| 19 | session-flow-policy-checklist-improvement.md | 重複（BL-042 吸収） | BL-042 のスコープに含まれる |
| 20 | skill-plugin-overlap-check-rule.md | backlog候補 | 優先度: 低 |
| 21 | sync-checklist-source-term-grep.md | ルール反映 | repo-sync-checklist へ追記 |
| 22 | workflow-md-reference-skills-section.md | backlog候補 | 優先度: 低 |
| 23 | 実装ワーカーの作業ログclaude-context-detailed-doc.md | 対応不要 | 外部リポジトリ文書。削除 |

**分類サマリ**: backlog候補 12件 / ルール反映 8件 / 対応不要 2件 / 重複（BL吸収）1件

### backlog 棚卸し（TG-002）

53件を突合。施策化済み3件、ステータス不整合2件、対象リポジトリ未記入14件を検出。

| BL-ID | 施策名 | 状態 | アクション |
|-------|--------|------|----------|
| BL-020 | sync-worker同期先コミット漏れ防止 | 施策化済み（アクティブ） | 変更なし（整合） |
| BL-031 | automation-managerセッション作成 | 施策化済み（ゲート通過） | CSV ステータス「完了」更新 + 施策ディレクトリ名記入 → CSV行削除 |
| BL-032 | Claude Code標準plugin・skills情報整理 | 施策化済み（ゲート通過） | CSV行削除 + 施策を _archive/ に移動 |

**対象リポジトリ未記入（entries ファイル）**: 14件（BL-035〜BL-048）。CSV列は全件記入済み。アクション実施フェーズで一括記入。

### 課題管理 CSV（TG-003）

27件を棚卸し。対応方針分類:

| 分類 | 件数 | ISS-ID |
|------|------|--------|
| 保留継続（前提条件未充足） | 4 | ISS-006, ISS-020, ISS-021, ISS-022 |
| 知見として維持 | 9 | ISS-013, ISS-027, ISS-033, ISS-038, ISS-039, ISS-043, ISS-045, ISS-046, ISS-049 |
| 施策化候補 | 5 | ISS-016, ISS-042+054, ISS-052+053 |
| 軽微修正（maintenance） | 3 | ISS-056, ISS-057, ISS-058 |
| 連動更新待ち | 1 | ISS-044 |
| 統合検討 | 2 | ISS-032+055 |
| rule-change-checklist 改善 | 2 | ISS-047, ISS-050 |
| 経過観察 | 1 | ISS-019 |

### backlog 関係性分析（TG-005）

51件（BL-031/032 除外）を分析。

**重複候補（3組）**:

| # | エントリA | エントリB | 推奨 |
|---|----------|----------|------|
| R-1 | BL-025 (agents管理ガイドライン) | BL-036 (agents公式ディレクトリ分け) | 統合 → G-1 |
| R-2 | BL-041 (波及更新パターン) | BL-030 (PostToolUse Hook) | 統合 → G-2/G-6 |
| R-3 | BL-016 (L1チェックリスト参照) | BL-022 (deny副作用分析) | 個別実施可（同時推奨） |

**統合候補（6グループ）**:

| # | グループ名 | エントリ | 推奨施策名 |
|---|----------|---------|-----------|
| G-1 | エージェント管理体系化 | BL-025, BL-035, BL-036 | agent-management-standardization |
| G-2 | ルール変更連動更新強化 | BL-016, BL-030, BL-041 | rule-change-cascade-prevention |
| G-3 | 同期セッション効率化 | BL-050, BL-051 | sync-session-efficiency |
| G-4 | ADP 横展開パッケージ | BL-015, BL-019, BL-021 | adp-process-infrastructure |
| G-5 | セッション構造標準化 | BL-027, BL-042, BL-048 | session-structure-standardization |
| G-6 | Hook 自動化基盤 | BL-029, BL-030 | hook-automation-foundation |

**マネージャー判断**: BL-030 は G-2 と G-6 に重複 → G-6 先行、G-2 は BL-016+BL-041 で実施。BL-037 は G-4 に統合せず独立維持（builtin-skills-eval は ADP 横展開だが対象が特定的すぎるため）。

**依存関係（8組）**: D-1〜D-8。D-4/D-8（BL-033/029→BL-053）は「必須前提」ではなく「先行推奨」レベル（評価者指摘）。

**優先実施推奨順序**: BL-024 → BL-011 → G-6 → G-2 → G-1 → G-3 → G-5 → G-4

### initiative 状態確認（TG-004）

| 施策名 | 状態 | アクション |
|--------|------|----------|
| automation-manager-session | ゲート通過・クローズ済み | **アーカイブ移動** |
| claude-code-plugin-skills-survey | ゲート通過・クローズ済み | **アーカイブ移動** |
| impl-worktree-parallel | ゲート通過・クローズ済み | **アーカイブ移動** |
| phase-gate-standardization | ゲート通過・クローズ済み | **アーカイブ移動** |
| sessionstart-hook-branch-cleanup | ゲート通過・クローズ済み | **アーカイブ移動** |
| sync-worker-target-commit | 計画済み・未着手 | 継続（BL-020 進行中） |
| triage-phase-gate-and-gha-sync | 計画済み・未着手 | 継続 |
| backlog-id-and-issue-template | 計画済み・未着手 | 継続 |
| impl-worker-worklog-reliability | 計画済み・未着手 | 継続 |
| external-repo-cleanup-on-demand | 作業完了・評価待ち | 継続（L1 が evaluator ディスパッチ要） |

### ルール/workflow 整合性（TG-006）

**重大度「高」の乖離**: manager-common-policy の適用対象不整合

| 問題 | 現状 | 修正内容 |
|------|------|---------|
| manager-common-policy §1 | 6マネージャー（automation 欠落） | 7マネージャーに更新、automation-manager 追加 |
| manager-common-policy §9 | 5マネージャー（automation/config-optimizer 欠落） | 7マネージャー分の関連ファイルを追加 |
| docs/workflow.md L623/L639 | 6マネージャー（config-optimizer 欠落） | 7マネージャーに更新、config-optimizer-manager 追加 |

**参考資料（ドラフト）**: 2件（coordination-protocol-guideline, git-worktree-guideline）のバナー・統合状況は正常。
**refs/**: 孤立エントリなし。
**docs/ 分類テーブル**: 6件全て網羅。

### セッション構造ポリシーチェック（TG-008）

14ファイルを A/B/C/D の4観点でチェック。

| 対象 | ファイル数 | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール |
|------|:--------:|:-:|:-:|:-:|:-:|
| config-optimizer-manager | 5 | OK | OK | OK | OK |
| automation-manager | 3 | OK | OK | OK | OK |
| l1-impl-manager | 6 | OK | OK | OK | OK |

不適合1件: manager-common-policy §1 適用対象不整合（TG-006 と同一、上記で修正対応）

### README 整合性（TG-007）

起動型スキル10件中4件が README.md の3セクションに未記載:
- l1-impl-manager
- automation-manager
- config-optimizer-manager
- repo-sync-checklist

ドキュメントマップ（セクション4）は網羅されている。→ アクション実施フェーズで修正。

### GHA ↔ Skills 整合性チェック（TG-010）

マッピング2件のドリフトチェック結果:

| マッピングID | CRITICAL | WARNING | INFO |
|------------|:-------:|:------:|:---:|
| triage-gha | 0 | 0 | 1 |
| l1-auto-execute-gha | 0 | 0 | 0 |

INFO 1件: triage-gha workflow_steps の差異（single-agent-mode の inherent_difference に起因。実質的ドリフトなし）。

inherent_differences 検証: 8件全て有効。

**未マッピングワークフロー**: 7件（サマリ修正: 6→7）

| ファイル | マッピング推奨 | 理由 |
|---------|:-----------:|------|
| daily-triage.yml | 不要 | triage.md 経由でカバー済み |
| initiative-wallbash.yml | **推奨** | l1-manager フェーズ0 対応 |
| initiative-execute.yml | **推奨** | l1-manager フェーズA〜B 対応 |
| initiative-close.yml | **推奨** | l1-manager クローズ手順対応 |
| backlog-candidate-propose.yml | 不要 | GHA 固有ユーティリティ |
| backlog-to-issue.yml | 不要 | GHA 固有ユーティリティ |
| test-permissions.yml | 不要 | テスト用 |

## backlog 追加・変更案

### 追加候補（12件）

inbox backlog候補からの新規追加:

| 優先度 | BL-ID | 施策名 | 課題概要 | 対象リポジトリ |
|--------|-------|--------|---------|-------------|
| 中 | BL-054 | docs-workflow-initiative-gha-update | docs/workflow.md への initiative GHA 記述追加 | dev-process-improvement |
| 中 | BL-055 | gha-backlog-maintenance-automation | GHA バックログメンテナンス自動化 | dev-process-improvement |
| 中 | BL-056 | gha-guideline-other-workflows | 他ワークフローへの権限3層モデル適用 | dev-process-improvement |
| 中 | BL-057 | gha-metacognition-automation | GHA メタ認知セッション自動化 | dev-process-improvement |
| 中 | BL-058 | plugin-high-applicability-trial | 高適用性4プラグインの導入検証 | dev-process-improvement |
| 中 | BL-059 | refs-routing-template-unification | 全セッションテンプレートのルーティング先統一 | dev-process-improvement |
| 低 | BL-060 | claude-code-action-version-tracking | Claude Code Action バージョン追従手順の制度化 | dev-process-improvement |
| 低 | BL-061 | gha-session-prompt-conversion-pattern | GHA セッションプロンプト変換パターンガイド | dev-process-improvement |
| 低 | BL-062 | l1-pre-applied-template-task-design | L1 タスク設計の改善（事前適用テンプレート） | dev-process-improvement |
| 低 | BL-063 | reference-doc-granularity-rule | リファレンス文書の粒度基準ルール化 | dev-process-improvement |
| 低 | BL-064 | skill-plugin-overlap-check-rule | スキル/プラグイン機能重複の定期チェック制度化 | dev-process-improvement |
| 低 | BL-065 | workflow-md-reference-skills-section | docs/workflow.md にリファレンススキル一覧セクション追加 | dev-process-improvement |

### 優先度変更候補

なし。

### 削除・クローズ候補

| BL-ID | 施策名 | 理由 |
|-------|--------|------|
| BL-031 | automation-managerセッション作成 | 施策化済み（ゲート通過・クローズ済み）。CSV行削除 |
| BL-032 | Claude Code標準plugin・skills情報整理 | 施策化済み（ゲート通過・クローズ済み）。CSV行削除 |

## 振り返り

### うまくいったこと
- Phase 内並列ディスパッチにより Phase 1 の2セット・Phase 2a の2セットを効率的に処理
- Phase 2b と Phase 3 を並列化（TG-010 は独立）し、全体リードタイムを短縮
- TG-006 と TG-008 を同一セット（set-4）に割り当てたことで、manager-common-policy の交差的不整合を横断的に検出

### 改善すべきこと
- ワーカーのスキャンレポートでサマリ件数と詳細テーブル行数の不一致が複数セットで発生（set-1: backlog候補件数、set-7: 未マッピング件数）。セルフチェック手順の追加が有効
- backlog entries の対象リポジトリ未記入が特定期間（03-09〜03-12）に集中。起票時のテンプレートバリデーション強化が必要

### プロセス改善の気づき
- GHA 自動化関連の inbox が8件集中。包括的な GHA 自動化計画の策定が有効かもしれない
- 知見型 CSV 課題は「起票」のまま滞留しやすい。自動クローズ基準（運用ガイド記載済みならクローズ等）の検討余地あり
- TG-005 の51件横断分析はワーカー負荷が高い。backlog 増加時にはカテゴリ単位のセット分割を検討

### 次回トリアージへの申し送り
- external-repo-cleanup-on-demand が評価待ち中間状態。L1 セッションで evaluator ディスパッチ要
- initiative 4件（sync-worker-target-commit, triage-phase-gate-and-gha-sync, backlog-id-and-issue-template, impl-worker-worklog-reliability）が計画済み・未着手で停滞。着手判断または優先度見直しを検討
- initiative-wallbash/execute/close の GHA マッピング追加を検討（TG-010 推奨3件）

**→ 申し送り事項あり**: `inbox/triage-handoff-20260315.md` を作成する

## 知見集約

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 Set | 対象ファイル・領域 | 詳細 |
|---|------|----------|-----------------|------|
| 1 | スキャンレポートのサマリ件数と詳細テーブル行数の整合性チェック | set-1 eval | triage-worker / triage-evaluator | 走査中の修正でサマリが更新されないパターン。セルフチェック手順の追加を検討 |
| 2 | 新セッションタイプ追加時の連動更新チェックリスト拡充 | set-4 scan/eval | session-flow-policy §5.1 | manager-common-policy §1/§9 の適用対象テーブル更新を追加。§1 と §9 の対応関係検証も含める |
| 3 | 施策化時の backlog.csv 更新チェックリスト | set-3 scan/eval | l1-manager SKILL.md | CSV ステータス更新・施策ディレクトリ名記入・proposal backlog元ファイル記入の3点を必須化 |
| 4 | entries ファイルの対象リポジトリ記入漏れ防止 | set-3 scan | backlog テンプレート | テンプレートバリデーションまたは起票時チェックの追加 |
| 5 | 関係性分析の依存テーブルに「依存強度」列追加 | set-5 eval | triage-standard-policy / TG-005 | 「必須前提」と「先行推奨」の区別で優先順序判断の精度向上 |
| 6 | カテゴリ再分類時の変更理由記録を work_log に義務化 | set-5 eval | triage-worker | scan_plan と scan_report 間のカテゴリ差異の透明性確保 |
| 7 | ルール反映系のトリアージ直接反映は効率的 | set-1 scan | トリアージフロー | 8件がルール反映分類。施策化すると管理オーバーヘッドが大きい |
| 8 | scan_report の自己修正は元データ（テーブルヘッダー等）も合わせて更新すべき | set-2 eval | triage-worker | 中間テーブルの見出しが残存すると混乱を招く |
| 9 | initiative ワークフロー3件のマッピング追加検討 | set-7 scan | gha-skills-mapping.yml | wallbash/execute/close は l1-manager の各フェーズに対応 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 Set | 背景・文脈 |
|---|------|----------|-----------|
| 1 | GHA 自動化関連 inbox が8件集中 | set-1 scan | 施策完了に伴う横展開提案の一斉流入。包括的 GHA 自動化計画が有効かも |
| 2 | 知見型 CSV 課題は滞留しやすい | set-2 scan | 自動クローズ基準の検討余地あり |
| 3 | config-optimizer-manager は新セッション作成時のリファレンス実装として優秀 | set-4 scan | 3フェーズ構成で対称性が完全に担保。ペアリング確認テーブルも完備 |
| 4 | ADP 横展開系5件が backlog の約10%を占める | set-5 scan | 包括的な ADP 整備計画の策定価値あり。CLI 環境推奨の制約あり |
| 5 | 51件横断分析はワーカー負荷が高い | set-5 eval | backlog 増加時のセット分割を検討 |
| 6 | TG-010 評価のコンテキスト負荷が高い | set-7 eval | マッピング数増加時の評価スケーラビリティが課題 |
| 7 | BL-040 が指摘する課題が set-5 で実際に発生 | set-5 eval | カテゴリ再編の変更理由未記録。BL-040 の優先度見直し根拠 |

## 課題集約

### ワーカーセット別課題件数

| Set | 課題件数 | CSV転記件数 | 備考 |
|-----|---------|-----------|------|
| set-1 | 2 | 0 | inbox 混入（当セッション対応）、レポート品質（当セッション対応） |
| set-2 | 2 | 0 | README 未記載（当セッション修正）、BL-031 残存（当セッション修正） |
| set-3 | 2 | 0 | BL-031 3重未連携（当セッション修正）、entries 未記入（当セッション修正） |
| set-4 | 2 | 1 | manager-common-policy 不整合（当セッション修正 + CSV転記） |
| set-5 | 3 | 0 | BL-030 重複割り当て（レポート記載）、BL-037 未割り当て（レポート記載）、相互参照未標準化（BL-010 スコープ） |
| set-7 | 0 | 0 | 課題なし |

### CSV転記済み課題

| ISS-ID | タイトル | 発見元 Set | 優先度 |
|--------|---------|----------|--------|
| ISS-059 | 新セッションタイプ追加時の manager-common-policy §1/§9 連動更新漏れ | set-4 | 中 |

## 課題起票

- 起票した課題（合計）：1 件（プロセス改善_課題管理.csv に転記済み）
- 残り10件は当セッション内で対応完了または レポート記載で対応

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-15
**レビュー依頼先**: ユーザー
**レビュー状態**: レビュー待ち
