# スキャンレポート: Set-2

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-003 | CSV（起票34件+方針確定1件） | 完了 |
| TG-004 | initiative（進行中9施策） | 完了 |

---

## TG-003: ステータス「起票」34件+「方針確定」1件の対応方針検討

### サマリ

| 分類 | 件数 |
|------|------|
| 起票 | 34件 |
| 方針確定 | 1件 |
| **合計** | **35件** |

### 対応方針の分布

| 推奨アクション | 件数 | 該当ISS |
|-------------|------|---------|
| クローズ推奨 | 4件 | ISS-006, ISS-019, ISS-031, ISS-043 |
| 施策化推奨 | 6件 | ISS-027, ISS-054, ISS-058, ISS-059, ISS-061, ISS-064 |
| 統合対応推奨（既存施策/チェックリストへの追加） | 10件 | ISS-032, ISS-038, ISS-039, ISS-042, ISS-050, ISS-052, ISS-053, ISS-055, ISS-060, ISS-065 |
| 経過観察（知見として維持） | 15件 | ISS-013, ISS-016, ISS-020, ISS-021, ISS-022, ISS-033, ISS-044, ISS-045, ISS-046, ISS-047, ISS-049, ISS-056, ISS-057, ISS-062, ISS-063 |

### グループ別詳細

#### G1: 外部リポジトリ関連（6件）

| ISS | タイトル | 現ステータス | 優先度 | 推奨アクション | 理由 |
|-----|---------|------------|--------|-------------|------|
| ISS-006 | ロール定義とOpenSpecライフサイクルの統合が未定義 | 起票 | 中 | クローズ推奨 | openspec-process-integration は完了済み。現在のプロセスでは OpenSpec を積極利用しておらず、ロール定義も ai-driven-dev-patterns に移行済み。前提が大幅に変化し課題の有効性が低下 |
| ISS-016 | m6o-es-product-api の .claude/rules/ 向けルールファイル整備 | 起票 | 中 | 経過観察 | 対象リポジトリ固有の課題。必要時に着手すればよい |
| ISS-043 | commit-message.md の2系統共存による運用混乱リスク | 起票 | 低 | クローズ推奨 | 起票から2週間経過し混乱報告なし。使い分けガイドが機能していると推定。経過観察期間満了 |
| ISS-044 | ai-driven-dev-patterns の連動更新が未実施 | 起票 | 中 | 経過観察 | 次回 sync セッションのスコープに含めるのが適切。単独施策化は過剰 |
| ISS-063 | ai-driven-dev-patterns: documentarian の参照切れルールファイル | 起票 | 中 | 経過観察 | ai-driven-dev-patterns 側の課題。harness-engineering-brushup 施策の後続として対応可能 |
| ISS-064 | ai-driven-dev-patterns: テストスクリプトパス未設定 | 起票 | 高 | 施策化推奨 | TDD フローが機能しない状態。ai-driven-dev-patterns 側での対応が必要だが、高優先度のため施策化して追跡すべき |

#### G2: プロセス改善・チェックリスト強化（10件）

| ISS | タイトル | 現ステータス | 優先度 | 推奨アクション | 理由 |
|-----|---------|------------|--------|-------------|------|
| ISS-032 | CSV ステータスの同期漏れパターン | 起票 | 低 | 統合対応 | ISS-055 と同根。rule-change-checklist への CSV ステータス更新項目追加で対応可能 |
| ISS-033 | 成功基準と CSV 対応方針案のスコープ整合 | 起票 | 低 | 経過観察 | 知見として有用だが、施策化するほどの影響度ではない。L1 の計画作成時の注意事項として記録を維持 |
| ISS-038 | CSV列追加時に全既存行の列数整合性を検証すべき | 起票 | 低 | 統合対応 | csv-conflict-prevention で CSV 自動生成に移行済み。generate-csvs.py のバリデーション強化として統合可能 |
| ISS-039 | L1クローズ手順でgate_reviewのWriteとgit mvの実行順序に注意が必要 | 起票 | 低 | 統合対応 | l1-manager.md のクローズ手順に注意書き1行追加で対応可能。maintenance コミットで実施推奨 |
| ISS-042 | パス移動施策の grep 検証で走査対象ディレクトリが網羅されていない | 起票 | 中 | 統合対応 | ISS-054 と同根。rule-change-checklist への走査対象網羅性チェック追加で対応 |
| ISS-052 | gate_review ルーティング宣言の未実行率22% | 起票 | 中 | 統合対応 | l1-manager クローズ手順でルーティング実行確認の強化。既存チェックリストへの項目追加で対応可能 |
| ISS-053 | 知見型CSVルーティングが構造的に転記漏れしやすい | 起票 | 中 | 統合対応 | ISS-052 と関連。ルーティング宣言時の ISS-ID 事前割当ルール追加で対応 |
| ISS-054 | rule-change-checklist の grep 走査対象に docs/ が未含有 | 起票 | 中 | 施策化推奨 | rule-change-checklist SKILL.md の走査対象リストに docs/ を追加。ISS-042, ISS-055 と統合して「rule-change-checklist 強化施策」として施策化推奨 |
| ISS-055 | CSV ステータス更新漏れの検出・防止メカニズムが未整備 | 起票 | 中 | 統合対応 | ISS-032, ISS-054 と統合。rule-change-checklist に CSV ステータス更新の項目追加で対応 |
| ISS-060 | 新セッションタイプ追加時の manager-common-policy §1/§9 連動更新漏れ | 起票 | 中 | 統合対応 | session-flow-policy §5.1 チェックリストへの項目追加で対応。ISS-054 と同じ rule-change-checklist 強化施策に含めることも可能 |

#### G3: 設定・セキュリティ（9件）

| ISS | タイトル | 現ステータス | 優先度 | 推奨アクション | 理由 |
|-----|---------|------------|--------|-------------|------|
| ISS-045 | Agent SDK 環境では settings.json の allow/deny リストが機能しない | 起票 | 中 | 経過観察 | SDK 環境の制約として記録済み。docs/subagent-permission-guide.md に反映済み。ツール側の改善待ち |
| ISS-046 | エージェント定義の tools フィールドによるツール制限が SDK 環境で機能しない | 起票 | 低 | 経過観察 | ISS-045 と同根の SDK 制約。意図の文書化として維持する方針が確定済み |
| ISS-047 | deferred tools が tools フィールドの制限を迂回する | 起票 | 中 | 経過観察 | CLI 環境の制約。disallowedTools の活用検討は知見として維持 |
| ISS-049 | deny リストは CLI 環境で唯一の強制的制限 | 起票 | 中 | 経過観察 | 知見として有用。deny リスト設計重視の運用方針を支持する根拠として維持 |
| ISS-050 | deny リスト設計時は Read/Write/Edit の3ツール網羅的考慮が必要 | 起票 | 中 | 統合対応 | rule-change-checklist に deny リスト変更時の対称性チェック項目追加で対応。ISS-054 統合施策に含める |
| ISS-058 | GHA ワークフローの run ブロックで ${{ }} 式を直接展開すべきでない | 起票 | 低 | 施策化推奨 | .claude/rules/gha-workflow-security.md として既にルール化済み。残件は backlog-auto-execute.yml の修正のみ。maintenance コミットまたは小施策で対応 |
| ISS-059 | GHA ワークフローのユーザー入力JSON構築にシェルインジェクションリスク | 起票 | 高 | 施策化推奨 | セキュリティリスクが具体的（eval + 未エスケープ変数）。initiative-dispatcher.yml の修正が必要。優先度「高」を維持し早期施策化推奨 |
| ISS-061 | settings.json deny ルールの非機能性（v1.0.93 既知バグ） | 起票 | 高 | 施策化推奨 | セキュリティガードが単一障害点。BL-071（sandbox有効化）+ BL-067（PreToolUse hook）で二重防御構築が必要。backlog に対応施策あり |
| ISS-062 | PreToolUse hook Bash パターンマッチングのバイパスリスク | 起票 | 中 | 経過観察 | ISS-061 の sandbox 導入により補完される。sandbox 施策の進捗に応じて再評価 |

#### G4: ドキュメント・ポリシー（2件）

| ISS | タイトル | 現ステータス | 優先度 | 推奨アクション | 理由 |
|-----|---------|------------|--------|-------------|------|
| ISS-057 | session-lifecycle-policy §3.2 のカテゴリラベル「E」が重複 | 起票 | 低 | 経過観察 | 軽微な記述ズレ。maintenance コミットで対応可能だが、現時点で実害報告なし |
| ISS-065 | session-lifecycle-policy §1.3 に config最適化系の列が欠落 | 起票 | 中 | 統合対応 | session-flow-policy §5.1 チェックリストに §1.2/§1.3 の系統一致確認を追加で再発防止。ISS-060 と同様の連動更新漏れパターン |

#### G5: ツール・仕様（4件）

| ISS | タイトル | 現ステータス | 優先度 | 推奨アクション | 理由 |
|-----|---------|------------|--------|-------------|------|
| ISS-019 | claude-directory-guide.md の skills/ 移動検討 | 起票 | 低 | クローズ推奨 | claude-directory-guide.md は docs/ に移動済みで rules/ からは除外されている。skills/ 移動のメリットが薄く、現状構成で十分 |
| ISS-020 | config.yaml の tasks ルールのカテゴリ分けが CLI ツールに適合しない | 起票 | 低 | 経過観察 | openspec 固有の課題。現在 openspec を積極利用しておらず優先度低 |
| ISS-021 | spec 作成時にエッジケース・境界条件のシナリオが漏れやすい | 起票 | 低 | 経過観察 | openspec 利用再開時に検討。現時点では知見として維持 |
| ISS-022 | spec 作成フェーズが openspec サイクルのボトルネック | 起票 | 中 | 経過観察 | openspec 利用再開時に検討。現時点では知見として維持 |

#### G6: 環境制約（2件）

| ISS | タイトル | 現ステータス | 優先度 | 推奨アクション | 理由 |
|-----|---------|------------|--------|-------------|------|
| ISS-013 | Claude Code Agent Teams 機能がworktreeガイドラインで言及されていない | 起票 | 低 | 経過観察 | Agent Teams は実験的機能。ガイドライン改訂時に対応すれば十分 |
| ISS-027 | Claude Code Web は1セッション=1リポジトリの制約がある | 起票 | 高 | 経過観察 | 環境分離ポリシー（CLAUDE.md）で対策済み。ツール側改善待ち。ステータスは「起票」のまま維持（制約は解消されていない） |

#### G7: 方針確定（1件）

| ISS | タイトル | 現ステータス | 優先度 | 推奨アクション | 理由 |
|-----|---------|------------|--------|-------------|------|
| ISS-031 | inbox/backlog が両リポジトリに存在する二重構造 | 方針確定 | 低 | クローズ推奨 | 方針確定済み（二重構造を許容、README で明記）。3回以上のトリアージで問題報告なし。経過観察期間満了としてクローズ可能 |

### 横断分析: 統合対応が可能なパターン

以下の ISS は共通の根本原因（rule-change-checklist の不十分さ）を持ち、統合施策で一括対応可能:

**統合施策案: rule-change-checklist 強化**
- ISS-032: CSV ステータス更新項目の追加
- ISS-042: パス移動時の走査対象ディレクトリ網羅性チェック
- ISS-050: deny リスト変更時の Read/Write/Edit 対称性チェック
- ISS-054: grep 走査対象に docs/ を追加
- ISS-055: CSV ステータス更新の検出・防止メカニズム

**統合施策案: session-flow-policy §5.1 チェックリスト強化**
- ISS-060: manager-common-policy §1/§9 への連動更新
- ISS-065: session-lifecycle-policy §1.2/§1.3 の系統一致確認

**統合施策案: l1-manager クローズ手順強化**
- ISS-039: gate_review の Write と git mv の実行順序注意
- ISS-052: ルーティング宣言の実行確認強化
- ISS-053: 知見型 CSV ルーティングの ISS-ID 事前割当

---

## TG-004: 進行中9施策の状態確認

### アーカイブ待ち7施策の状態

| 施策名 | ゲート通過 | 判定日 | 横展開チェックリスト | アーカイブ可否 | 備考 |
|--------|:---------:|--------|:------------------:|:----------:|------|
| csv-conflict-prevention | 通過 | 2026-03-16 | 完了 | 可 | SC-1〜SC-7 全達成。PreToolUse hook パターンを導入 |
| external-repo-cleanup-on-demand | **未実施** | - | - | **要確認** | 08_gate_review.md がテンプレート状態。成果物（04〜06）は存在するがゲートレビュー未記入 |
| l1-manager-enhanced-planning | 通過 | 2026-03-17 | 完了 | 可 | 3フェーズ全て通過。計画ワーカー・並列ディスパッチ・ドメインエージェント統合を導入 |
| session-lifecycle-policy-rename | 通過 | 2026-03-17 | 完了 | 可 | 単一フェーズ完了。58ファイル変更、旧名残存なし |
| skill-plugin-overlap-check-rule | 通過 | 2026-03-16 | 完了 | 可 | CO-008 追加。全5成功基準達成 |
| sync-worker-target-commit | **未実施** | - | - | **要確認** | 08_gate_review.md がテンプレート状態。成果物（04〜06）は存在するがゲートレビュー未記入 |
| triage-phase-gate-and-gha-sync | **未実施** | - | - | **要確認** | 08_gate_review.md がテンプレート状態。成果物（04〜06）は存在するがゲートレビュー未記入 |

#### アーカイブ可能（4件）
- csv-conflict-prevention
- l1-manager-enhanced-planning
- session-lifecycle-policy-rename
- skill-plugin-overlap-check-rule

#### ゲートレビュー未実施（3件）— 要確認
- external-repo-cleanup-on-demand
- sync-worker-target-commit
- triage-phase-gate-and-gha-sync

これら3施策は成果物ファイル（04_work_report.md, 05_eval_plan.md, 06_eval_report.md）が存在するため作業自体は完了している可能性が高いが、08_gate_review.md がテンプレート状態のまま残されている。L1 によるゲートレビュー実施が必要。

### 進行中2施策の状態

| 施策名 | フェーズ | タスク進捗 | 作成日 | 備考 |
|--------|--------|-----------|--------|------|
| backlog-id-and-issue-template | 実施 | 0/5（全て未着手） | 2026-03-14 | backlog.csv にID列追加・ワークフロー変更等 |
| impl-worker-worklog-reliability | 実施 | 0/5（全て未着手） | 2026-03-14 | impl-worker 作業ログテンプレート新規作成等 |

両施策とも2026-03-14に計画まで作成済みだが、3日間タスク未着手の状態。ブロック原因は記録されていない。

---

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票済み）
- アーカイブ待ち3施策のゲートレビュー未実施（external-repo-cleanup-on-demand, sync-worker-target-commit, triage-phase-gate-and-gha-sync）

## 走査中の知見

### ルール化候補（.claude/rules/ や skills/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | rule-change-checklist 走査対象の不十分さが複数 ISS の共通根本原因 | `.claude/skills/rule-change-checklist/SKILL.md` | ISS-032, ISS-042, ISS-050, ISS-054, ISS-055 が同一パターン。走査対象リストの拡充（docs/, backlog/ 追加）と対称性チェック（Read/Write/Edit）追加で5件を一括対応可能 |
| 2 | ゲートレビュー未実施のまま「アーカイブ待ち」と分類されるパターン | `l1-manager SKILL.md` クローズ手順 | 08_gate_review.md がテンプレート状態でも成果物が存在するケースがある。トリアージの事前調査時にゲートレビューの記入状態まで確認する走査ステップを追加すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | openspec 関連の ISS（006, 020, 021, 022）は現在のワークフローでの優先度が低下 | openspec を積極利用しなくなったことで、これらの課題の実質的影響度が低下。次回 openspec 活用再開時に再評価が必要 |
| 2 | セキュリティ系 ISS（059, 061, 062）は backlog の対応施策（BL-067, BL-071）と連動 | ISS 単独での施策化よりも、backlog 施策の進行と合わせて対応するのが効率的 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-17
