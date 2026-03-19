# スキャンレポート: Phase 1（情報収集）

## サマリ

前回スナップショット（2026-03-17）から2日後の定期収集。全8ターゲット（SC-001〜SC-008）について情報収集を実施した結果、前回からの差分は検出されなかった。9マネージャー SKILL.md、27エージェント定義、9テンプレートディレクトリの構成に変更なし。前回検出済みの壊れた参照2件（l2-plan-worker, l2-plan-evaluator の triage-standard-policy 参照）は依然として未修正。

## SC ターゲット別結果

### SC-001: SKILL.md 構造準拠

**走査対象**: 9件のマネージャー SKILL.md

| マネージャー | パス | 必須セクション（4項目） | オーケストレーション（4項目） | 備考 |
|-------------|------|---------------------|--------------------------|------|
| l1-manager | `.claude/skills/l1-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| triage-manager | `.claude/skills/triage-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| metacognition-manager | `.claude/skills/metacognition-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| sync-manager | `.claude/skills/sync-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| backlog-maintenance-manager | `.claude/skills/backlog-maintenance-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| automation-manager | `.claude/skills/automation-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| config-optimizer-manager | `.claude/skills/config-optimizer-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| session-consistency-manager | `.claude/skills/session-consistency-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |
| l1-impl-manager | `.claude/skills/l1-impl-manager/SKILL.md` | 4/4 | 4/4 | 完全準拠 |

**差分**: 前回スナップショットから変更なし

### SC-002: エージェント定義構造準拠

**走査対象**: 27件のエージェント定義

全27件について以下を確認:
- 必須6セクション（あなたの役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）: 全件あり
- 壁打ちフェーズ: 全件あり
- YAML name フィールドのケバブケース: 全件 OK

**差分**: 前回スナップショットから変更なし

### SC-003: Worker ↔ Evaluator 対称性

**走査対象**: 10ペアリング

全ペアについて対称性要件6項目（壁打ち・計画・レポート・知見記録・課題起票・停止ルール）を確認。

| マネージャー | Worker(s) | Evaluator | 対称性6項目 | 対称性テーブル | 備考 |
|-------------|-----------|-----------|-----------|-------------|------|
| l1-manager | l2-worker | l2-evaluator | 全て対称 | E:なし | |
| l1-manager | l2-plan-worker | l2-plan-evaluator | 全て対称 | E:あり | |
| l1-impl-manager | investigation/design/impl-plan/impl-worker | impl-evaluator | 全て対称 | E:あり | |
| triage-manager | triage-worker | triage-evaluator | 全て対称 | E:なし | |
| metacognition-manager | metacognition-worker | metacognition-evaluator | 全て対称 | E:なし | |
| sync-manager | sync-worker | sync-evaluator | 全て対称 | E:あり | |
| backlog-maintenance-manager | bm-worker | bm-evaluator | 全て対称 | E:あり | |
| automation-manager | automation-worker | automation-evaluator | 全て対称 | E:あり | |
| config-optimizer-manager | config-collection/analysis/proposal-worker | config-optimizer-evaluator | 全て対称 | E:あり | |
| session-consistency-manager | sc-collection/analysis/proposal-worker | sc-evaluator | 全て対称 | E:あり | |

**差分**: 前回スナップショットから変更なし

### SC-004: テンプレート ↔ エージェント担当ファイル整合

**走査対象**: 9種のテンプレートディレクトリ

| セッションタイプ | テンプレートパス | ファイル数 |
|----------------|---------------|----------|
| initiatives | `sessions/initiatives/_template/` | 13 |
| impl | `sessions/impl/_template/` | 6+phase dirs (33 total) |
| triage | `sessions/triage/_template/` | 5+workers (12 total) |
| metacognition | `sessions/metacognition/_template/` | 5+workers (12 total) |
| sync | `sessions/sync/_template/` | 9 |
| backlog-maintenance | `sessions/backlog-maintenance/_template/` | 5+workers (12 total) |
| automation | `sessions/automation/_template/` | 5+workers (12 total) |
| config-optimization | `sessions/config-optimization/_template/` | 5+phase (29 total) |
| session-consistency | `sessions/session-consistency/_template/` | 5+phase (29 total) |

**差分**: 前回スナップショットから変更なし

### SC-005: manager-common-policy 準拠

**走査対象**: 9マネージャー × §2〜§8 参照パターン

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

**差分**: 前回スナップショットから変更なし

### SC-006: session-lifecycle-policy 適用マトリクス整合

**走査対象**: session-lifecycle-policy §1.2 の適用マトリクス

マトリクスに記載された全30セッションタイプ列と、`.claude/skills/` 配下の実在セッション定義の突合を実施。

- マトリクス上の全列に対応するセッション定義が存在する: OK
- 実在するセッション定義のうちマトリクスに未記載のものはない: OK
- §1.3 記録先ファイル対応テーブルの内容がテンプレートと一致: OK

**差分**: 前回スナップショットから変更なし

### SC-007: commit-message 規約カバレッジ

**走査対象**: `.claude/rules/commit-message.md` のセッション種別テーブル

登録済みセッション種別: 29種（maintenance 含む）

未登録セッション定義: なし（全セッションタイプが登録済み）

> **補足**: l2-plan-worker は L2-worker に、l2-plan-evaluator は L2-evaluator にそれぞれ包含されている（commit-message.md 37-38行目の括弧内包含記述による）。Phase 1 評価で誤検出が指摘され修正済み。

**差分**: 前回スナップショットから変更なし

### SC-008: 関連ファイル一覧の相互参照整合

**走査対象**: 全9マネージャー SKILL.md + 全27エージェント定義 + 3ポリシー SKILL.md

- 関連ファイル一覧セクション: 全39件にあり
- 主要な参照パターン（マネージャー↔エージェント双方向参照）: 正常

**壊れた参照（前回から継続）**:

| 参照元 | 参照先（不在） | 備考 |
|--------|-------------|------|
| `l1-manager/agents/l2-plan-evaluator.md` (112行目) | TG-008 基準チェックで `triage-standard-policy/SKILL.md` を参照 | 旧名称。session-lifecycle-policy にリネーム済み |
| `l1-manager/agents/l2-plan-evaluator.md` (198行目) | 関連ファイル一覧で `triage-standard-policy/SKILL.md` を参照 | 同上 |
| `l1-manager/agents/l2-plan-worker.md` (195行目) | 関連ファイル一覧で `triage-standard-policy/SKILL.md` を参照 | 同上 |

**差分**: 前回スナップショットから変更なし。壊れた参照3箇所（2ファイル）が未修正

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 壊れた参照の修正が2回のスキャンにわたり未対応 | l2-plan-worker.md, l2-plan-evaluator.md | 前回（2026-03-17）に検出された triage-standard-policy への壊れた参照が依然として残存。SC チェックで検出された不整合の修正フローが明確でない可能性がある |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | 全8ターゲットで前回から差分なし | 前回スナップショットから2日しか経過していないため、変更がないのは想定通り。スキャン間隔が短い場合の効率化（差分検出のみのライトスキャンモード等）は将来検討の余地あり |

---
**作成者**: sc-collection-worker
**作成日**: 2026-03-19
