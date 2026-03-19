# スキャンレポート: Phase 2（現状分析）

## サマリ

Phase 1 収集データとリファレンスを基準に、SC-001〜SC-008 の全8ターゲットの現状分析を実施した。不整合は合計7件（中4件、低3件）を検出した。前回（20260317）検出の不整合10件のうち、SC-006 §1.3 の config最適化系・セッション一貫性系の追加（IMP-002 の一部）と SC-007 の包含記述確認は対応済みだが、残りは未修正。重点分析の SC-008（壊れた参照3箇所）と SC-003（対称性テーブル欠如3件）は前回から状態変化なし。前回アクション候補6件中、backlog 起票2件は「候補」のまま未着手、inbox 起票候補4件は未起票。

## 前回（20260317）SC セッション知見フォローアップ

### アクション候補の対応状況

| # | 前回アクション | 対応状況 | エビデンス |
|---|-------------|---------|----------|
| 1 | backlog 起票: SC チェック Quick Wins 一括是正（IMP-001, IMP-002, IMP-005） | 起票済み・未着手 | `backlog/entries/SCチェックQuickWins一括是正.md`（ステータス: 候補） |
| 2 | backlog 起票: リネーム時全文検索チェック義務化ルール追加（IMP-007） | 起票済み・未着手 | `backlog/entries/リネーム時全文検索チェック義務化ルール追加.md`（ステータス: 候補） |
| 3 | inbox 起票: evaluator 対称性テーブル統一（IMP-003） | 未起票 | inbox/ に該当ファイルなし |
| 4 | inbox 起票: commit-message 規約で l2-plan 明確化（IMP-004） | 未起票 | inbox/ に該当ファイルなし |
| 5 | inbox 起票: SC走査対象のインライン参照拡大（IMP-008） | 未起票 | inbox/ に該当ファイルなし |
| 6 | inbox 起票: SC チェック結果のフィードバックループ定義 | 未起票 | inbox/ に該当ファイルなし |

### 不整合修正の対応状況

| # | 前回検出不整合 | 修正状況 | エビデンス |
|---|-------------|---------|----------|
| 1 | SC-008: 壊れた参照3箇所（l2-plan-worker/evaluator の triage-standard-policy 参照） | 未修正 | `Grep triage-standard-policy` で3箇所の残存を確認（l2-plan-evaluator.md 112行目・198行目、l2-plan-worker.md 195行目） |
| 2 | SC-006: §1.3 テーブルに config最適化系・セッション一貫性系の欠落 | 修正済み | session-lifecycle-policy §1.3 に config最適化系・セッション一貫性系の列が存在 |
| 3 | SC-006: §1.3 テーブルに実装系の欠落 | 未修正 | session-lifecycle-policy §1.3 に実装系の列がない（8列: イニシアティブ系〜config最適化系） |
| 4 | SC-003: l2-evaluator 対称性テーブル欠如 | 未修正 | l2-evaluator.md に「対称性確認テーブル」セクションなし |
| 5 | SC-003: triage-evaluator 対称性テーブル欠如 | 未修正 | triage-evaluator.md に「対称性確認テーブル」セクションなし |
| 6 | SC-003: metacognition-evaluator 対称性テーブル欠如 | 未修正 | metacognition-evaluator.md に「対称性確認テーブル」セクションなし |
| 7 | SC-007: l2-plan-worker/evaluator の包含記述の曖昧さ | 前回判定通り問題なし | commit-message.md 37-38行目の括弧内包含記述で対応済み |
| 8 | 横断: テンプレート SC-006 セクション見出しの旧名称 | 未修正 | 3テンプレートファイルの25行目に `triage-standard-policy` 残存 |

## SC ターゲット別結果

### SC-001: SKILL.md 構造準拠

#### Current State（現状）
- 対象: 9件のマネージャー SKILL.md
- session-flow-policy §2 の必須セクション: 全9件 4/4 準拠
- オーケストレーション関連の必須記載: 全9件 4/4 準拠

#### Requirements（準拠要件）
- §2.2 必須セクション: あなたの役割、作業フロー、やること、やらないこと
- §2.3 オーケストレーション: ディスパッチ手順、確認観点、集約手順、担当ファイル

#### Gaps & Inconsistencies（不整合）
| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 全9件完全準拠 |

**判定**: 不整合なし

---

### SC-002: エージェント定義構造準拠

#### Current State（現状）
- 対象: 27件のエージェント定義
- session-flow-policy §3 の必須セクション: 全27件 6/6 準拠
- 壁打ちフェーズ: 全27件あり
- YAML name ケバブケース: 全27件 OK

#### Requirements（準拠要件）
- §3.1 必須セクション: あなたの役割、作業フロー、やること、やらないこと、担当ファイル、停止ルール
- §3.4 命名規約: YAML name フィールドはケバブケース

#### Gaps & Inconsistencies（不整合）
| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 全27件完全準拠 |

**判定**: 不整合なし

---

### SC-003: Worker <-> Evaluator 対称性

#### Current State（現状）
- 対象: 10ペアリング
- 対称性6要件（壁打ち・計画・レポート・知見記録・課題起票・停止ルール）: 全10ペア対称
- 対称性確認テーブル: 7/10 ペアの evaluator にあり、3件なし

#### Requirements（準拠要件）
- session-flow-policy §3.2: 対称性要件6項目（必須）
- session-flow-policy §3.3: 対称性確認テーブル（推奨）

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| 1 | l2-evaluator に対称性確認テーブルなし | 低（推奨） | `.claude/skills/l1-manager/agents/l2-evaluator.md` -- 「対称性確認テーブル」セクションが存在しない。ペアの l2-plan-evaluator.md には89-98行目に存在 |
| 2 | triage-evaluator に対称性確認テーブルなし | 低（推奨） | `.claude/skills/triage-manager/agents/triage-evaluator.md` -- 「対称性確認テーブル」セクションが存在しない |
| 3 | metacognition-evaluator に対称性確認テーブルなし | 低（推奨） | `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md` -- 「対称性確認テーブル」セクションが存在しない |

#### 重点分析: 欠如パターンの分析

**時系列パターン**: 欠如している3件（l2-evaluator, triage-evaluator, metacognition-evaluator）はすべて初期に作成されたエージェント定義。session-flow-policy §3.3 の推奨プラクティスが追加された後に作成された evaluator（sync-evaluator, backlog-maintenance-evaluator, automation-evaluator, config-optimizer-evaluator, impl-evaluator, sc-evaluator）にはすべて対称性テーブルが存在する。

**意図的 vs 遡及漏れの判定**: §3.3 追加後の遡及適用がされていない状態であり、「遡及漏れ」と判定する。根拠:
1. §3.3 の参考実装として sync-evaluator.md が明記されている（session-flow-policy 104行目）
2. 後発の全 evaluator が §3.3 に準拠していることから、推奨が事実上の標準パターンとなっている
3. l2-evaluator のペアである l2-plan-evaluator には対称性テーブルが存在する一方、l2-evaluator には存在しない非対称が同一マネージャー配下で発生

**実害**: 対称性要件6項目自体は全ペアで満たされているため、動作に影響はない。ただし、今後のエージェント定義変更時に対称性の自己検証手段が欠如する保守リスクがある。

---

### SC-004: テンプレート <-> エージェント担当ファイル整合

#### Current State（現状）
- 対象: 9種のテンプレートディレクトリ
- テンプレートにはマネージャー・ワーカー・評価者の全ファイルが含まれるため、各エージェントの担当ファイルはテンプレートのサブセット

#### Requirements（準拠要件）
- 各エージェントの「担当ファイル」テーブルに記載されたファイルがテンプレートに存在すること
- テンプレートに存在するファイルのうち、いずれのエージェントの担当にもなっていないファイルがないこと

#### Gaps & Inconsistencies（不整合）
| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 設計上正常（テンプレートは全ロール分を包含） |

**判定**: 不整合なし

---

### SC-005: manager-common-policy 準拠

#### Current State（現状）
- 対象: 9マネージャー x §2〜§8（必須）+ §10（任意）
- 全9マネージャーが §2〜§8 の全セクションを参照済み
- §10 は l1-manager と l1-impl-manager のみが参照（設計通り）

#### Requirements（準拠要件）
- §2（ワーカーディスパッチパターン）〜 §8（セッションライフサイクル todo 登録）: 全マネージャー必須
- §10（ドメインエージェント参照）: l1-manager, l1-impl-manager のみ任意適用

#### Gaps & Inconsistencies（不整合）
| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 全9件 §2〜§8 参照済み |

**判定**: 不整合なし

---

### SC-006: session-lifecycle-policy 適用マトリクス整合

#### Current State（現状）
- §1.2 適用マトリクス: 30セッションタイプ列、全列に対応するセッション定義が存在
- §1.3 記録先ファイル対応テーブル: 8系統（イニシアティブ系、トリアージ系、メタ認知系、同期系、バックログメンテナンス系、オートメーション系、セッション一貫性系、config最適化系）

#### Requirements（準拠要件）
- §1.2 の全列が実在するセッション定義と対応すること
- §1.3 が §1.2 の全セッション系統をカバーすること

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| 1 | §1.3 に実装系（impl）の列が欠落 | 中 | session-lifecycle-policy §1.3（55-65行目）に8系統が記載されているが、§1.2 マトリクスに存在する impl-manager / impl-worker / impl-evaluator に対応する「実装系」列がない |

**分析**: 前回（20260317）SC セッションで IMP-002 として「§1.3 テーブルに config最適化系と実装系の2系統が欠落」と指摘。config最適化系・セッション一貫性系は追加されたが、実装系は依然として欠落している。実装系はテンプレート構成が他系統と異なり（`sessions/impl/_template/` に Phase 別ディレクトリあり）、記録先ファイル名も独自のパターンを持つ。

---

### SC-007: commit-message 規約カバレッジ

#### Current State（現状）
- 登録済みセッション種別: 29種（maintenance 含む）
- 全セッションタイプが登録済み
- l2-plan-worker は L2-worker に、l2-plan-evaluator は L2-evaluator にそれぞれ包含（commit-message.md 37-38行目の括弧内記述「l2-plan-worker を含む」「l2-plan-evaluator を含む」）

#### Requirements（準拠要件）
- 全セッションタイプに対応する session-type が登録されていること

#### Gaps & Inconsistencies（不整合）
| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 全セッションタイプが登録済み。包含記述も明確 |

**判定**: 不整合なし

---

### SC-008: 関連ファイル一覧の相互参照整合

#### Current State（現状）
- 全9マネージャー SKILL.md + 全27エージェント定義 + 3ポリシー SKILL.md に「関連ファイル一覧」セクションあり
- マネージャー <-> エージェント間の双方向参照: 正常
- 壊れた参照: 3箇所（2ファイル）

#### Requirements（準拠要件）
- 関連ファイル一覧の参照先がすべて実在すること
- 主要な参照パターン（マネージャー <-> エージェント）で双方向参照が成立すること

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| 1 | l2-plan-evaluator.md 112行目: `triage-standard-policy/SKILL.md` への壊れた参照 | 中 | メタルール横断検証チェックリスト内の「TG-008 基準の連動性」チェック項目で旧名称を参照。正しくは `session-lifecycle-policy/SKILL.md` |
| 2 | l2-plan-evaluator.md 198行目: `triage-standard-policy/SKILL.md` への壊れた参照 | 中 | 関連ファイル一覧テーブル内で旧名称を参照。正しくは `session-lifecycle-policy/SKILL.md` |
| 3 | l2-plan-worker.md 195行目: `triage-standard-policy/SKILL.md` への壊れた参照 | 中 | 関連ファイル一覧テーブル内で旧名称を参照。正しくは `session-lifecycle-policy/SKILL.md` |

#### 重点分析: 壊れた参照の影響分析

**影響分析（参照箇所別）**:

1. **l2-plan-evaluator.md 112行目**（メタルール横断検証チェックリスト内）
   - 記述: `- [ ] TG-008 基準の連動性: triage-standard-policy/SKILL.md のチェック基準が変更内容を反映`
   - 影響: l2-plan-evaluator がルール・テンプレート変更を含む施策を評価する際、チェック対象として存在しないファイルパスを参照する。Read 時にファイル未検出エラーとなり、TG-008 基準の連動性チェックが実行不能になる
   - 比較: 同一チェックリストを持つ l2-evaluator.md では84行目で正しく `session-lifecycle-policy/SKILL.md` を参照済み

2. **l2-plan-evaluator.md 198行目**（関連ファイル一覧テーブル内）
   - 記述: `.claude/skills/triage-standard-policy/SKILL.md` を連動更新対象として参照
   - 影響: 連動更新の判断基準として参照されるが、ファイルが存在しないため連動更新のトリガーが機能しない。ただし関連ファイル一覧は参考用の静的ドキュメントであり、自動処理ではないため影響は限定的

3. **l2-plan-worker.md 195行目**（関連ファイル一覧テーブル内）
   - 記述: l2-plan-evaluator.md 198行目と同様
   - 影響: 同上

**対称ファイルの修正状況比較**:

| ファイル | TG-008 チェック内参照 | 関連ファイル一覧内参照 | 状態 |
|---------|-------------------|--------------------|------|
| l2-evaluator.md | `session-lifecycle-policy` (84行目) | `session-lifecycle-policy` (170行目) | 修正済み |
| l2-plan-evaluator.md | `triage-standard-policy` (112行目) | `triage-standard-policy` (198行目) | **未修正** |
| l2-worker.md | N/A（チェックリストなし） | N/A（triage-standard-policy 参照なし） | 該当なし |
| l2-plan-worker.md | N/A（チェックリストなし） | `triage-standard-policy` (195行目) | **未修正** |

**横断的な旧名称残存箇所（SC-008 関連ファイル一覧外）**:

テンプレートの SC-006 セクション見出しにも旧名称が残存している（前回 IMP-005 で指摘済み・未修正）:
- `sessions/session-consistency/_template/phase-1-collection/_template/04_scan_report.md` 25行目
- `sessions/session-consistency/_template/phase-2-analysis/_template/04_scan_report.md` 25行目
- `sessions/session-consistency/_template/phase-3-proposal/_template/04_scan_report.md` 25行目

---

## 不整合サマリ

| SC ターゲット | 不整合件数 | 最大重大度 | 前回比 | 備考 |
|-------------|----------|----------|-------|------|
| SC-001 | 0 | -- | 変化なし | 全9件完全準拠 |
| SC-002 | 0 | -- | 変化なし | 全27件完全準拠 |
| SC-003 | 3 | 低（推奨） | 変化なし | 対称性テーブル欠如（l2-eval, triage-eval, meta-eval） |
| SC-004 | 0 | -- | 変化なし | 設計上正常 |
| SC-005 | 0 | -- | 変化なし | 全9件 §2〜§8 参照済み |
| SC-006 | 1 | 中 | 改善（2->1） | §1.3 に実装系が欠落（config最適化系・SC系は追加済み） |
| SC-007 | 0 | -- | 改善（2->0） | 前回の包含記述確認で問題なしと判定 |
| SC-008 | 3 | 中 | 変化なし | 壊れた参照3箇所（triage-standard-policy -> session-lifecycle-policy） |
| **合計** | **7** | **中** | **改善（10->7）** | **中: 4件、低: 3件** |

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | SC チェック指摘の修正フロー未整備 | 横断 | 前回（20260317）SC セッションで検出された不整合10件のうち、自然修正（他施策での修正）は config最適化系追加のみ。backlog 起票済み2件は「候補」のまま未着手。inbox 起票候補4件は未起票。SC チェック -> backlog 起票 -> 施策化 -> 修正のフィードバックループが機能していない可能性がある |
| 2 | テンプレート経由の旧名称伝播が継続中 | sessions/session-consistency/_template/ | IMP-005 で指摘されたテンプレートの旧名称（triage-standard-policy）が未修正のまま。本 Phase 2 の `04_scan_report.md` テンプレートにも旧名称が伝播していた（25行目）。テンプレートコピーのたびに旧名称が拡散する構造的問題 |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | l2-evaluator は TG-008 参照を修正済みだが l2-plan-evaluator は未修正 | 同一マネージャー（l1-manager）配下の2つの evaluator で修正状態が非対称。l2-evaluator のリネーム対応時に l2-plan-evaluator の対応が漏れた可能性。リネーム時全文検索チェック義務化（IMP-007）の必要性を裏付けるエビデンス |
| 2 | SC-006 §1.3 の部分修正パターン | 前回「config最適化系と実装系の2系統が欠落」と指摘。config最適化系・セッション一貫性系は追加されたが実装系は漏れた。複数項目の一括修正で一部が漏れるパターン |

---
**作成者**: sc-analysis-worker
**作成日**: 2026-03-19
