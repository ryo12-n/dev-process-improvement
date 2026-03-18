# スキャンレポート: Phase 1（情報収集）

## サマリ

全8ターゲット（SC-001〜SC-008）の情報収集を完了した。9マネージャー SKILL.md、27エージェント定義、9テンプレートディレクトリを走査し、リファレンス（session-consistency-reference.md）を初回作成した。全体的に高い準拠率が確認されたが、SC-008 で壊れた参照2件（l2-plan-worker/l2-plan-evaluator の旧名称 triage-standard-policy 参照）、SC-007 で commit-message 規約の未登録候補2件（l2-plan-worker/l2-plan-evaluator）を検出した。

## SC ターゲット別結果

### SC-001: SKILL.md 構造準拠

全9マネージャー SKILL.md が session-flow-policy §2 の必須セクション4項目（あなたの役割・作業フロー・やること・やらないこと）およびオーケストレーション関連4項目（ディスパッチ手順・成果物確認観点・結果集約手順・担当ファイル）を完備。

| マネージャー | 必須セクション | オーケストレーション | 判定 |
|-------------|-------------|-------------------|------|
| l1-manager | 4/4 | 4/4 | OK |
| triage-manager | 4/4 | 4/4 | OK |
| metacognition-manager | 4/4 | 4/4 | OK |
| sync-manager | 4/4 | 4/4 | OK |
| backlog-maintenance-manager | 4/4 | 4/4 | OK |
| automation-manager | 4/4 | 4/4 | OK |
| config-optimizer-manager | 4/4 | 4/4 | OK |
| session-consistency-manager | 4/4 | 4/4 | OK |
| l1-impl-manager | 4/4 | 4/4 | OK |

### SC-002: エージェント定義構造準拠

全27エージェント定義が session-flow-policy §3 の必須セクション6項目（あなたの役割・作業フロー・やること・やらないこと・担当ファイル・停止ルール）を完備。全件に壁打ちフェーズが定義されている。YAML フロントマターの `name` フィールドは全件ケバブケース準拠。

| 項目 | 合格 / 全件 |
|------|-----------|
| 必須6セクション | 27/27 |
| 壁打ちフェーズ | 27/27 |
| YAML name ケバブケース | 27/27 |

### SC-003: Worker ↔ Evaluator 対称性

全ペアで session-flow-policy §3.2 の対称性要件6項目（壁打ち・計画・レポート・知見記録・課題起票・停止ルール）を満たしている。

対称性確認テーブル（§3.3 推奨プラクティス）の有無:

| Evaluator | テーブルあり | 備考 |
|-----------|:----------:|------|
| l2-evaluator | なし | |
| l2-plan-evaluator | あり | |
| impl-evaluator | あり | |
| triage-evaluator | なし | |
| metacognition-evaluator | なし | |
| sync-evaluator | あり | 参考実装として session-flow-policy に記載 |
| backlog-maintenance-evaluator | あり | |
| automation-evaluator | あり | |
| config-optimizer-evaluator | あり | |
| sc-evaluator | あり | |

3件の evaluator（l2-evaluator, triage-evaluator, metacognition-evaluator）に対称性確認テーブルが欠落。推奨プラクティスのため必須ではないが、早期不整合検出に有効。

### SC-004: テンプレート ↔ エージェント担当ファイル整合

9セッションタイプのテンプレートディレクトリを確認。テンプレートファイルとエージェント担当ファイルの関係は設計上正常。テンプレートにはマネージャー・全エージェント分のファイルが含まれるが、各エージェントの担当ファイルテーブルは自分の操作対象のみを記載する構造。

### SC-005: manager-common-policy 準拠

全9マネージャーが §2〜§8 を参照済み。§10（ドメインエージェント参照）は任意適用で、l1-manager と l1-impl-manager のみが参照。

| マネージャー | §2 | §3 | §4 | §5 | §6 | §7 | §8 | §10 |
|-------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| l1-manager | OK | OK | OK | OK | OK | OK | OK | OK |
| triage-manager | OK | OK | OK | OK | OK | OK | OK | — |
| metacognition-manager | OK | OK | OK | OK | OK | OK | OK | — |
| sync-manager | OK | OK | OK | OK | OK | OK | OK | — |
| backlog-maintenance-manager | OK | OK | OK | OK | OK | OK | OK | — |
| automation-manager | OK | OK | OK | OK | OK | OK | OK | — |
| config-optimizer-manager | OK | OK | OK | OK | OK | OK | OK | — |
| session-consistency-manager | OK | OK | OK | OK | OK | OK | OK | — |
| l1-impl-manager | OK | OK | OK | OK | OK | OK | OK | OK |

### SC-006: session-lifecycle-policy 適用マトリクス整合

§1.2 マトリクスの全30列（セッションタイプ）について対応するセッション定義が存在することを確認。§1.3 記録先ファイル対応テーブルの7系統（イニシアティブ・トリアージ・メタ認知・同期・バックログメンテナンス・オートメーション・セッション一貫性）の記載が実態と一致。

注: マトリクスのセクション見出しが「SC-006: triage-standard-policy」となっているテンプレートファイルは旧名称を使用（04_scan_report.md テンプレート）。session-lifecycle-policy が正しい。

### SC-007: commit-message 規約カバレッジ

commit-message.md のセッション種別テーブルに29種の session-type が登録済み。実際のセッション定義との突合の結果、以下2件が未登録の可能性あり:

| 未登録候補 | 推奨 session-type | 備考 |
|-----------|-----------------|------|
| l2-plan-worker | L2-worker に含まれるか要確認 | l1-manager Phase 2 で使用 |
| l2-plan-evaluator | L2-evaluator に含まれるか要確認 | l1-manager Phase 3 で使用 |

### SC-008: 関連ファイル一覧の相互参照整合

全9マネージャー SKILL.md、全27エージェント定義、全3ポリシー SKILL.md に「関連ファイル一覧」セクションが存在。マネージャー↔エージェント間の双方向参照は正常。

**壊れた参照 2件**:

| 参照元 | 参照先（不在） | 正しい参照先 |
|--------|-------------|------------|
| `l1-manager/agents/l2-plan-evaluator.md` | `.claude/skills/triage-standard-policy/SKILL.md` | `.claude/skills/session-lifecycle-policy/SKILL.md` |
| `l1-manager/agents/l2-plan-worker.md` | `.claude/skills/triage-standard-policy/SKILL.md` | `.claude/skills/session-lifecycle-policy/SKILL.md` |

原因: 2026-03-17 に triage-standard-policy が session-lifecycle-policy にリネームされたが、l2-plan-worker.md と l2-plan-evaluator.md の関連ファイル一覧が更新されていない。

## 課題起票

- 起票件数: 2件（`07_issues.md` に起票済み）

## 走査中の知見

### ルール化候補

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 対称性確認テーブルの網羅化 | session-flow-policy §3.3 | 現在「推奨」だが、l2-evaluator, triage-evaluator, metacognition-evaluator の3件が欠落。全 evaluator への適用を検討 |
| 2 | リネーム時の関連ファイル一覧更新チェック | rule-change-checklist | triage-standard-policy → session-lifecycle-policy リネーム時に l2-plan-worker/evaluator の関連ファイル一覧が更新漏れ。リネーム時のチェックリストに「関連ファイル一覧の参照先更新」を追加すべき |

### 参考情報

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | 04_scan_report.md テンプレートに旧名称残存 | テンプレートの SC-006 セクション見出しが「triage-standard-policy」のまま。テンプレート更新が必要 |
| 2 | commit-message 規約での plan-worker/evaluator の扱い | l2-plan-worker/evaluator が L2-worker/L2-evaluator の session-type に含まれるのか、別途登録が必要かは Phase 2 で分析すべき |

---
**作成者**: sc-collection-worker
**作成日**: 2026-03-17
