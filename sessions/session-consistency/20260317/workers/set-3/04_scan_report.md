# 改善提案レポート: Phase 3

## サマリ

Phase 2 で検出された不整合10件（SC-003: 3件、SC-006: 2件、SC-007: 2件、SC-008: 3件）に対する改善提案6件と、横断的な改善提案2件の計8件を作成した。Impact x Effort 評価の結果、Quick Wins 3件（IMP-001, IMP-002, IMP-005）、Easy Adds 2件（IMP-003, IMP-006）、Strategic 2件（IMP-007, IMP-008）、Nice-to-Have 0件に分類された。IMP-004 は設計判断を含むため Strategic に近い Easy Add として分類した。最優先の Quick Wins 3件は合計6ファイルの機械的修正で完了でき、即座に着手可能。

## Summary Matrix

| # | Proposal | SC Target | Impact | Effort | Priority |
|---|----------|-----------|--------|--------|----------|
| IMP-001 | 壊れた参照の修正（triage-standard-policy → session-lifecycle-policy） | SC-008 | 高 | 低 | Quick Win |
| IMP-002 | §1.3 記録先テーブルに config最適化系・実装系を追加 | SC-006 | 中 | 低 | Quick Win |
| IMP-003 | evaluator 3件に対称性確認テーブルを追加 | SC-003 | 低 | 低 | Easy Add |
| IMP-004 | l2-plan-worker/evaluator の commit-message 登録を明確化 | SC-007 | 低 | 低 | Easy Add |
| IMP-005 | session-consistency テンプレート内の旧名称を更新 | 横断 | 中 | 低 | Quick Win |
| IMP-006 | session-consistency リファレンスの旧名称を更新 | 横断 | 低 | 低 | Easy Add |
| IMP-007 | リネーム時の全文検索チェック義務化ルールを追加 | 横断 | 高 | 中 | Strategic |
| IMP-008 | SC チェックの走査対象を本文中インライン参照にも拡大 | 横断 | 中 | 中 | Strategic |

---

## Quick Wins（高〜中 Impact / 低 Effort）

### IMP-001: 壊れた参照の修正（triage-standard-policy → session-lifecycle-policy）

- **SC ターゲット**: SC-008
- **Current State**: l2-plan-worker.md（行195）、l2-plan-evaluator.md（行198, 行112）の計3箇所で `.claude/skills/triage-standard-policy/SKILL.md` を参照しているが、2026-03-17 に `session-lifecycle-policy` にリネーム済みのため壊れた参照となっている
- **Proposed Change**: 3箇所すべての `triage-standard-policy` を `session-lifecycle-policy` に置換する
  - `.claude/skills/l1-manager/agents/l2-plan-worker.md` 行195
  - `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` 行198（関連ファイル一覧）
  - `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` 行112（メタルール横断検証チェックリスト）
- **Expected Benefit**: 壊れた参照を解消し、l2-plan-worker/evaluator が正しいポリシーファイルを参照できるようになる。参照先不在による作業エラーのリスクを排除
- **Impact**: 高（壊れた参照は動作不良リスクに直結。l2-plan-evaluator のチェックリストが不正確なポリシーファイルを指しているため、評価の品質に影響し得る）
- **Effort**: 低（2ファイル3箇所の文字列置換。機械的作業）
- **Risk**: 低。置換対象が明確であり、誤置換のリスクは極めて小さい。緩和策: 置換後に Grep で旧名称の残存がないことを確認する
- **Backlog Entry Draft**: 「l2-plan-worker/evaluator の壊れた参照を修正」— l2-plan-worker.md と l2-plan-evaluator.md の計3箇所で triage-standard-policy への参照が残存しており、session-lifecycle-policy に更新する。SC-008 で検出された不整合の是正。

### IMP-002: §1.3 記録先テーブルに config最適化系・実装系を追加

- **SC ターゲット**: SC-006
- **Current State**: session-lifecycle-policy の §1.2 マトリクスには co-manager/co-worker/co-evaluator（config最適化系）と impl-manager/impl-worker/impl-evaluator（実装系）の列が存在するが、§1.3 記録先テーブルにはこれら2系統の行が欠落している
- **Proposed Change**: `.claude/skills/session-lifecycle-policy/SKILL.md` の §1.3 記録先テーブルに以下の2行を追加する
  - 「config最適化系」: テンプレート `sessions/config-optimization/_template/` の実態に基づいてステージ別のファイル名を記載
  - 「実装系」: テンプレート `sessions/impl/_template/` の実態に基づいてステージ別のファイル名を記載（Phase 型の独自構成に注意）
- **Expected Benefit**: §1.2 マトリクスと §1.3 テーブルの列が一致し、session-flow-policy §5.1 チェックリストの要件を充足する。新規セッションタイプ追加時のリファレンスとして機能する
- **Impact**: 中（一貫性・保守性に影響。§1.3 テーブルが不完全だと、新しいワーカーが記録先ファイルを特定できないリスクがある）
- **Effort**: 低（1ファイルへの2行追加。テンプレートディレクトリの実態を確認して転記する機械的作業）
- **Risk**: 低。テンプレートの実態と突合するため正確性は高い。緩和策: 追加後に §1.2 の列数と §1.3 の行数が一致することを確認する
- **Backlog Entry Draft**: 「session-lifecycle-policy §1.3 に config最適化系・実装系の記録先を追加」— §1.2 マトリクスに存在する config最適化系と実装系の記録先ファイルが §1.3 テーブルに欠落している。テンプレートの実態に基づいて2行を追加し、マトリクス間の整合性を確保する。

### IMP-005: session-consistency テンプレート内の旧名称を更新

- **SC ターゲット**: 横断（SC-008 関連）
- **Current State**: `sessions/session-consistency/_template/` 配下の `04_scan_report.md` テンプレート（行25）に `SC-006: triage-standard-policy 適用マトリクス整合` という旧名称が残存している。また、本 Phase 3 の `04_scan_report.md` 初期状態にも同じ旧名称が含まれていた
- **Proposed Change**: テンプレートファイル `sessions/session-consistency/_template/workers/_template/04_scan_report.md` の SC-006 セクション見出しを `session-lifecycle-policy 適用マトリクス整合` に更新する
- **Expected Benefit**: 今後の session-consistency セッションでテンプレートからコピーされるファイルに旧名称が含まれなくなる。ワーカーが誤った名称でファイルを探すリスクを排除
- **Impact**: 中（テンプレートは繰り返し使用されるため、旧名称の伝播を防止する効果が高い）
- **Effort**: 低（1ファイル1箇所の文字列修正）
- **Risk**: 極めて低。見出しテキストの修正のみで、構造的な変更はない
- **Backlog Entry Draft**: 「session-consistency テンプレートの旧名称（triage-standard-policy）を更新」— SC-006 セクション見出しに旧名称 triage-standard-policy が残存しており、session-lifecycle-policy に更新する。テンプレート経由での旧名称伝播を防止する。

---

## Strategic Improvements（高〜中 Impact / 中 Effort）

### IMP-007: リネーム時の全文検索チェック義務化ルールを追加

- **SC ターゲット**: 横断
- **Current State**: triage-standard-policy → session-lifecycle-policy のリネーム時に、l2-plan-worker/evaluator の3箇所で参照更新が漏れた。現在、リネーム時の全文検索を義務付けるルールは存在しない
- **Proposed Change**: `.claude/rules/` に「リネーム・移動時の参照更新チェックルール」を新規作成する。内容:
  - リネーム・移動前に旧名称で `Grep` 全文検索を実行すること
  - 検出された全箇所を新名称に更新すること
  - 更新後に旧名称で再度 `Grep` を実行し、残存参照がないことを確認すること
  - 対象範囲: `.claude/skills/`、`docs/`、`sessions/*/_template/`、`.claude/rules/`
- **Expected Benefit**: リネーム時の参照更新漏れを構造的に防止できる。SC-008 で検出されたような壊れた参照の再発を防ぐ
- **Impact**: 高（予防的措置として高い効果。リネームは低頻度だが、漏れた場合の影響範囲が広い）
- **Effort**: 中（ルールファイルの新規作成 + 既存のリネーム手順との統合が必要。ルール自体は短いが、適用範囲の検討と既存ルールとの重複確認が必要）
- **Risk**: 低。新規ルール追加のため既存機能への影響はない。緩和策: 初回適用時に実効性を確認し、過度に煩雑であれば簡略化する
- **Backlog Entry Draft**: 「リネーム・移動時の全文検索チェック義務化ルールを追加」— triage-standard-policy → session-lifecycle-policy のリネーム時に参照更新漏れが3箇所発生した。`.claude/rules/` にリネーム時の Grep チェックを義務付けるルールを追加し、壊れた参照の再発を構造的に防止する。

### IMP-008: SC チェックの走査対象を本文中インライン参照にも拡大

- **SC ターゲット**: 横断（SC-008 強化）
- **Current State**: Phase 1 の SC-008 走査は「関連ファイル一覧」セクションを主な対象としていたため、l2-plan-evaluator.md 行112 の本文中インライン参照（メタルール横断検証チェックリスト内）が検出されなかった。Phase 2 の深堀り分析で初めて発見された
- **Proposed Change**: session-consistency-reference.md の SC-008 セクションに走査対象の定義を追加する:
  - 「関連ファイル一覧」セクションの参照パス（既存）
  - 本文中のインライン参照パス（`.claude/skills/` や `sessions/` で始まるパス文字列）
  - sc-collection-worker のエージェント定義の作業フローに「本文中インライン参照も走査対象とする」旨を追記する
- **Expected Benefit**: 今後の SC チェックで関連ファイル一覧外の壊れた参照も検出できるようになる。検出率の向上
- **Impact**: 中（予防的措置。本文中参照は関連ファイル一覧ほど多くないが、見落とされやすい）
- **Effort**: 中（リファレンスファイルの更新 + エージェント定義の作業フロー修正。走査ロジックの変更範囲を検討する必要がある）
- **Risk**: 低。走査対象の拡大であり、既存の走査結果には影響しない。緩和策: false positive が多い場合はパス文字列のパターンを絞り込む
- **Backlog Entry Draft**: 「SC-008 の走査対象を本文中インライン参照に拡大」— Phase 1 の SC-008 走査で関連ファイル一覧セクション外のインライン参照が検出漏れとなった。sc-collection-worker の走査対象定義を拡大し、本文中のパス参照も検出できるようにする。

---

## Easy Adds（低 Impact / 低 Effort）

### IMP-003: evaluator 3件に対称性確認テーブルを追加

- **SC ターゲット**: SC-003
- **Current State**: l2-evaluator、triage-evaluator、metacognition-evaluator の3件に対称性確認テーブルが欠落している。対称性要件6項目自体は全ペアで充足しており、実質的なリスクはない。テーブルの有無は推奨プラクティス（session-flow-policy §3.3）であり必須ではない
- **Proposed Change**: 以下の3ファイルに対称性確認テーブルを追加する。sync-evaluator の実装を参考テンプレートとする
  - `.claude/skills/l1-manager/agents/l2-evaluator.md`
  - `.claude/skills/triage-manager/agents/triage-evaluator.md`
  - `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md`
- **Expected Benefit**: 全 evaluator で対称性確認テーブルが統一され、将来の一貫性チェックで差分が出なくなる。セッション定義の保守性向上
- **Impact**: 低（推奨プラクティスの充足。実機能への影響なし。対称性要件自体は既に充足されている）
- **Effort**: 低（3ファイルへのテーブル追加。sync-evaluator からコピー＆カスタマイズの機械的作業）
- **Risk**: 極めて低。テーブル追加のみで既存の記述には影響しない
- **Backlog Entry Draft**: 「evaluator 3件に対称性確認テーブルを追加」— l2-evaluator、triage-evaluator、metacognition-evaluator に session-flow-policy §3.3 推奨の対称性確認テーブルが欠落。sync-evaluator を参考に3件に追加し、全 evaluator での統一性を確保する。

### IMP-004: l2-plan-worker/evaluator の commit-message 登録を明確化

- **SC ターゲット**: SC-007
- **Current State**: commit-message.md の施策作業テーブルに L1、L2-worker、L2-evaluator の3種が登録されているが、l2-plan-worker と l2-plan-evaluator の扱いが明示されていない。施策作業という分類は L2-worker/L2-evaluator と同一であり、独立した session-type にする必然性は低い
- **Proposed Change**: `.claude/rules/commit-message.md` の施策作業テーブルにおいて:
  - L2-worker の用途欄に「（l2-plan-worker を含む）」と追記
  - L2-evaluator の用途欄に「（l2-plan-evaluator を含む）」と追記
  - Phase 2 の推奨（方法1）に準拠
- **Expected Benefit**: l2-plan-worker/evaluator を使用するセッションでコミットメッセージの session-type 選択に迷わなくなる。規約の明確性向上
- **Impact**: 低（現状でも L2-worker/L2-evaluator で運用されていると推測され、実質的な動作変更はない。規約の明確化のみ）
- **Effort**: 低（1ファイル2箇所のテキスト追記）
- **Risk**: 極めて低。既存の運用を明文化するだけで、破壊的変更はない
- **Backlog Entry Draft**: 「commit-message 規約で l2-plan-worker/evaluator の session-type を明確化」— l2-plan-worker/evaluator の commit-message session-type が明示的に登録されていない。L2-worker/L2-evaluator の用途欄に包含関係を追記し、規約の明確性を向上する。

### IMP-006: session-consistency リファレンスの旧名称を更新

- **SC ターゲット**: 横断（SC-008 関連）
- **Current State**: `reference/session-consistency-reference.md` の SC-008 セクション（壊れた参照テーブル）に `triage-standard-policy` の記載がある。これは Phase 1 収集時点での事実記録であり、参照自体は壊れていないが、リファレンスが旧名称を含むことで混乱の原因となり得る
- **Proposed Change**: リファレンスファイルの次回更新時に、SC-008 セクションの壊れた参照テーブルのステータスを「修正済み」に更新する（IMP-001 の修正完了後）
- **Expected Benefit**: リファレンスが最新の状態を反映し、次回の SC チェック時に Phase 1 収集結果と現状の差分が明確になる
- **Impact**: 低（リファレンスの正確性向上。SC チェック自体は毎回新規収集を行うため、実運用への影響は限定的）
- **Effort**: 低（IMP-001 修正後にリファレンスのテーブルを更新するのみ）
- **Risk**: 極めて低。事実記録の更新のみ
- **Backlog Entry Draft**: 「session-consistency リファレンスの壊れた参照ステータスを更新」— IMP-001 による修正完了後、リファレンスの SC-008 セクションを最新状態に更新する。リファレンスの正確性を維持する定期メンテナンス。

---

## Nice-to-Haves（低 Impact / 高 Effort）

該当なし。

---

## Quick Wins まとめ

以下の3件は即座に着手可能で、合計6ファイル程度の機械的修正で完了する。

| # | Proposal | 対象ファイル数 | 作業内容 |
|---|----------|-------------|---------|
| IMP-001 | 壊れた参照の修正 | 2ファイル3箇所 | 文字列置換（triage-standard-policy → session-lifecycle-policy） |
| IMP-002 | §1.3 テーブル追加 | 1ファイル2行追加 | テンプレート実態に基づく行追加 |
| IMP-005 | テンプレート旧名称更新 | 1ファイル1箇所 | 見出しテキスト修正 |

推奨実施順序: IMP-001 → IMP-005 → IMP-002（依存関係: IMP-005 は IMP-001 と同種の修正のため連続実施が効率的）

---

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | Quick Wins の一括施策化 | backlog | IMP-001, IMP-002, IMP-005 は個別にバックログエントリにするよりも、一括で「SC チェック Quick Wins 是正」として1施策にまとめる方が効率的。個別施策のオーバーヘッドが作業量を上回る |
| 2 | SC チェック結果のフィードバックループ | session-consistency-manager | 提案作成後にマネージャーがバックログ登録 → 施策実施 → 次回 SC チェックで是正確認、というループが明示的に定義されていない。session-consistency-manager の作業フローに「前回提案の是正確認」ステップを追加することを検討すべき |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | Impact 評価の根拠パターン | 壊れた参照（動作不良リスク）> テーブル欠落（一貫性リスク）> 推奨プラクティス欠落（保守性リスク）の順で Impact を評価した。この優先順位付けの基準は、今後の SC チェックでも再利用可能 |
| 2 | Effort 評価と施策オーバーヘッドの関係 | 全提案の Effort が「低」または「中」であり、実作業量は小さい。しかし施策管理プロセス（proposal → plan → tasks → work → review）のオーバーヘッドを考慮すると、Quick Wins は一括施策として処理する方が合理的 |

---
**作成者**: sc-proposal-worker
**作成日**: 2026-03-17
