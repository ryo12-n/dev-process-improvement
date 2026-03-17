# スキャンレポート: Phase 2（現状分析）

## サマリ

全8ターゲット（SC-001〜SC-008）の現状分析を完了した。SC-001（SKILL.md 構造）・SC-002（エージェント定義構造）・SC-004（テンプレート整合）・SC-005（manager-common-policy 準拠）は完全準拠で不整合なし。SC-003 では対称性テーブル欠落3件（推奨レベル）、SC-006 では §1.3 記録先テーブルに config最適化系・実装系の2系統が欠落（中）、SC-007 では l2-plan-worker/evaluator の commit-message 登録不備（低）、SC-008 では壊れた参照3箇所（l2-plan-worker 1箇所、l2-plan-evaluator 2箇所）を検出した。全体の不整合件数は10件（重大度: 中5件、低5件）。

## SC ターゲット別結果

---

### SC-001: SKILL.md 構造準拠

#### Current State（現状）
- 対象マネージャー SKILL.md: 9件
- Phase 1 で全9件が必須セクション4/4、オーケストレーション4/4 を完備と確認済み

#### Requirements（準拠要件）
- session-flow-policy §2.2: 必須セクション（あなたの役割・作業フロー・やること・やらないこと）
- session-flow-policy §2.3: オーケストレーション関連の必須記載（ディスパッチ手順・成果物確認観点・結果集約手順・担当ファイル）

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 全9件完全準拠（Phase 1 リファレンス §1 参照） |

#### Recommendations（推奨対応）
- 対応不要。定期的な一貫性チェックで維持する。

---

### SC-002: エージェント定義構造準拠

#### Current State（現状）
- 対象エージェント定義: 27件
- Phase 1 で全27件が必須セクション6/6、壁打ちフェーズあり、YAML name ケバブケース準拠と確認済み

#### Requirements（準拠要件）
- session-flow-policy §3.1: 必須セクション6項目（あなたの役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）
- session-flow-policy §3.4: YAML フロントマター name フィールドのケバブケース命名

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 全27件完全準拠（Phase 1 リファレンス §2 参照） |

#### Recommendations（推奨対応）
- 対応不要。

---

### SC-003: Worker ↔ Evaluator 対称性

#### Current State（現状）
- ペアリング数: 10組（l1-manager: 2、l1-impl-manager: 1、その他7マネージャー: 各1）
- 対称性要件6項目: 全10組で充足
- 対称性確認テーブル: 10組中7組が備えている。3組（l2-evaluator, triage-evaluator, metacognition-evaluator）に欠落

#### Requirements（準拠要件）
- session-flow-policy §3.2: ペアリング対称性要件6項目（壁打ち・計画・レポート・知見記録・課題起票・停止ルール）— 必須
- session-flow-policy §3.3: 対称性確認テーブル — 推奨プラクティス（必須ではない）

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| 1 | l2-evaluator に対称性確認テーブルが欠落 | 低（推奨） | `l1-manager/agents/l2-evaluator.md` — テーブルなし。ペアの l2-plan-evaluator にはテーブルあり |
| 2 | triage-evaluator に対称性確認テーブルが欠落 | 低（推奨） | `triage-manager/agents/triage-evaluator.md` — テーブルなし。sync-evaluator（参考実装）にはテーブルあり |
| 3 | metacognition-evaluator に対称性確認テーブルが欠落 | 低（推奨） | `metacognition-manager/agents/metacognition-evaluator.md` — テーブルなし |

#### Recommendations（推奨対応）
- 3件の evaluator に対称性確認テーブルを追加する。sync-evaluator の実装を参考にする。
- なお、対称性要件6項目自体は全ペアで充足しているため、実質的なリスクはない。テーブルの追加は早期不整合検出のための予防的措置。

---

### SC-004: テンプレート ↔ エージェント担当ファイル整合

#### Current State（現状）
- テンプレートディレクトリ: 9種（initiatives, impl, triage, metacognition, sync, backlog-maintenance, automation, config-optimization, session-consistency）
- 設計上の構造: テンプレートはマネージャー・全エージェント分のファイルを含み、各エージェントの担当ファイルテーブルは自分の操作対象のみを記載する

#### Requirements（準拠要件）
- 各エージェントの「担当ファイル」テーブルに記載されたファイルが、対応するテンプレートディレクトリに存在すること
- テンプレートに存在するファイルのうち、いずれかのエージェントの担当ファイルに含まれていること（マネージャー担当分を除く）

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | Phase 1 の突合結果で、全セッションタイプにおいてテンプレートとエージェント担当ファイルの関係が設計上正常であることを確認。Worker は自分の担当ファイルのみ操作し、テンプレートにはマネージャー・評価者のファイルも含むという構造が全セッションタイプで一貫している |

#### Recommendations（推奨対応）
- 対応不要。

---

### SC-005: manager-common-policy 準拠

#### Current State（現状）
- 対象マネージャー: 9件
- 全9件が §2〜§8 を参照済み
- §10（ドメインエージェント参照）は l1-manager と l1-impl-manager のみが適用（任意）

#### Requirements（準拠要件）
- manager-common-policy §2〜§8: 全マネージャーに適用
- manager-common-policy §10: 任意適用（ドメインエージェント参照）

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| — | なし | — | 全9件が §2〜§8 を参照済み（Phase 1 リファレンス §5 参照）。§10 は任意適用で l1-manager, l1-impl-manager のみ参照しており、他マネージャーの不参照は設計意図通り |

#### Recommendations（推奨対応）
- 対応不要。

---

### SC-006: session-lifecycle-policy 適用マトリクス整合

#### Current State（現状）
- §1.2 マトリクス: 30列（セッションタイプ）×9行（ステージ）で定義済み
- §1.3 記録先テーブル: 7系統（イニシアティブ系・トリアージ系・メタ認知系・同期系・バックログメンテナンス系・オートメーション系・セッション一貫性系）を定義
- §1.2 マトリクスには co-manager / co-worker / co-evaluator（config最適化系）と impl-manager / impl-worker / impl-evaluator（実装系）の列が存在
- §1.3 テーブルにはこれら2系統の行が存在しない

#### Requirements（準拠要件）
- §1.2 マトリクスの全列に対応するセッション定義（SKILL.md / agents/*.md）が存在すること — 充足
- §1.3 記録先テーブルが §1.2 マトリクスの全セッション系統をカバーしていること — 未充足
- §1.3 のファイル名がテンプレートの実態と一致していること — 検証可能な範囲では一致
- session-flow-policy §5.1 チェックリスト: 「§1.2 と §1.3 の列が一致していること」 — 未充足

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| 1 | §1.3 記録先テーブルに「config最適化系」が欠落 | 中 | §1.2 マトリクスに co-manager / co-worker / co-evaluator の列が存在するが、§1.3 テーブルに config最適化系の行がない。テンプレート `sessions/config-optimization/_template/` は実在し、ファイル構成は他の Phase 型系統（session-consistency 等）と同一 |
| 2 | §1.3 記録先テーブルに「実装系」が欠落 | 中 | §1.2 マトリクスに impl-manager / impl-worker (Ph1-3) / impl-worker (Ph4) / impl-evaluator の列が存在するが、§1.3 テーブルに実装系の行がない。テンプレート `sessions/impl/_template/` は実在し、Phase 型の独自構成（phase-1〜4）を持つ |

#### Recommendations（推奨対応）
- §1.3 テーブルに「config最適化系」と「実装系」の列を追加する。各ステージの記録先ファイルは、テンプレートディレクトリの実態に基づいて記載する。

---

### SC-007: commit-message 規約カバレッジ

#### Current State（現状）
- commit-message.md のセッション種別テーブル: 29種の session-type が登録
- 施策作業テーブル: L1, L2-worker, L2-evaluator の3種
- 非施策作業テーブル: 26種（triage-mgr〜maintenance）
- l2-plan-worker / l2-plan-evaluator は明示的に登録されていない

#### Requirements（準拠要件）
- 全セッション定義に対応する session-type が commit-message.md に登録されていること
- 各 session-type の分類（施策作業 / 非施策作業）が正しいこと

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| 1 | l2-plan-worker の session-type が明示的に登録されていない | 低 | commit-message.md の施策作業テーブルには L1, L2-worker, L2-evaluator のみ登録。l2-plan-worker は l1-manager の Phase 2 で使用される（`l1-manager/SKILL.md` 行29, 110）。session-type の明示的な割当がなく、L2-worker に包含されるのか独立すべきかが不明 |
| 2 | l2-plan-evaluator の session-type が明示的に登録されていない | 低 | 同上。l2-plan-evaluator は l1-manager の Phase 3 で使用される（`l1-manager/SKILL.md` 行31, 115）。L2-evaluator に包含されるのか独立すべきかが不明 |

#### Recommendations（推奨対応）
- 方法1（推奨）: L2-worker の用途欄に「l2-plan-worker を含む」、L2-evaluator の用途欄に「l2-plan-evaluator を含む」と追記する。理由: 施策作業という分類は同一であり、独立した session-type にする必然性が低い
- 方法2: 新たに L2-plan-worker / L2-plan-evaluator を独立した session-type として登録する

---

### SC-008: 関連ファイル一覧の相互参照整合

#### Current State（現状）
- 全9マネージャー SKILL.md に「関連ファイル一覧」セクション: 9/9
- 全27エージェント定義に「関連ファイル一覧」セクション: 27/27
- 全3ポリシー SKILL.md に「関連ファイル一覧」セクション: 3/3
- マネージャー ↔ エージェント間の双方向参照: 正常

#### Requirements（準拠要件）
- 「関連ファイル一覧」に記載された参照先が実在すること
- マネージャーとエージェント間の双方向参照が維持されていること
- リネーム・移動時に参照先が更新されていること
- 本文中のインライン参照も含めて実在すること

#### Gaps & Inconsistencies（不整合）

| # | Gap | Severity | Evidence |
|---|-----|----------|----------|
| 1 | l2-plan-worker.md の関連ファイル一覧に壊れた参照 | 中 | `l1-manager/agents/l2-plan-worker.md` 行195: `.claude/skills/triage-standard-policy/SKILL.md` を参照。正しくは `.claude/skills/session-lifecycle-policy/SKILL.md`。2026-03-17 に triage-standard-policy → session-lifecycle-policy にリネーム済みだが、参照が未更新 |
| 2 | l2-plan-evaluator.md の関連ファイル一覧に壊れた参照 | 中 | `l1-manager/agents/l2-plan-evaluator.md` 行198: `.claude/skills/triage-standard-policy/SKILL.md` を参照。同上 |
| 3 | l2-plan-evaluator.md のメタルール横断検証チェックリストに壊れた参照（Phase 1 未検出） | 中 | `l1-manager/agents/l2-plan-evaluator.md` 行112: `triage-standard-policy/SKILL.md` をインライン参照。関連ファイル一覧セクション外の本文中参照であり、Phase 1 の走査では検出されていなかった |

#### Recommendations（推奨対応）
- 3箇所すべての `triage-standard-policy` 参照を `session-lifecycle-policy` に更新する。

---

## 不整合サマリ

| SC | ターゲット | 不整合件数 | 最大重大度 |
|----|----------|----------|----------|
| SC-001 | SKILL.md 構造準拠 | 0 | — |
| SC-002 | エージェント定義構造準拠 | 0 | — |
| SC-003 | Worker ↔ Evaluator 対称性 | 3 | 低（推奨プラクティス） |
| SC-004 | テンプレート ↔ 担当ファイル整合 | 0 | — |
| SC-005 | manager-common-policy 準拠 | 0 | — |
| SC-006 | session-lifecycle-policy マトリクス整合 | 2 | 中 |
| SC-007 | commit-message 規約カバレッジ | 2 | 低 |
| SC-008 | 関連ファイル一覧の相互参照整合 | 3 | 中 |
| **合計** | | **10** | **中: 5件、低: 5件** |

## 課題起票

- 起票件数: 3件（`07_issues.md` に起票済み）

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | リネーム時の全文検索チェック義務化 | `.claude/rules/` | triage-standard-policy → session-lifecycle-policy のリネーム時に l2-plan-worker/evaluator の3箇所が更新漏れ。リネーム時は `Grep` で旧名称の全文検索を行い、残存参照がないことを確認するルールを追加すべき |
| 2 | §1.3 テーブルの系統追加チェック | session-lifecycle-policy | 新セッションタイプ追加時のチェックリスト（session-flow-policy §5.1）に「§1.2 と §1.3 の列が一致していること」が含まれているが、config最適化系・実装系で漏れが発生。チェックリスト実行の徹底が必要 |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | Phase 1 で検出されなかった追加の壊れた参照 | l2-plan-evaluator.md のメタルール横断検証チェックリスト内（行112）に `triage-standard-policy/SKILL.md` のインライン参照が残存。Phase 1 の走査は「関連ファイル一覧」セクションを対象としていたため、本文中のインライン参照は検出対象外だった可能性がある。今後の SC チェックでは、関連ファイル一覧セクションだけでなく本文中のインライン参照も走査対象とすべき |
| 2 | 対称性確認テーブルの欠落パターン | 欠落している3件（l2-evaluator, triage-evaluator, metacognition-evaluator）は、いずれも初期に作成されたエージェント定義。後発の evaluator（sync, backlog-maintenance, automation, config-optimizer, sc, l2-plan, impl）にはテーブルが存在する。時系列的に、§3.3 推奨プラクティスが追加された後に作成されたものにはテーブルがあり、以前のものには遡及追加されていないと推測される |

---
**作成者**: sc-analysis-worker
**作成日**: 2026-03-17
