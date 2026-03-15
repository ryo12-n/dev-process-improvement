# スキャンレポート: Set-4

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-006 | rules/workflow 整合性チェック | 完了 |
| TG-008 | セッション構造標準ポリシーチェック | 完了 |

---

## TG-006: ルール・workflow 整合性チェック

### docs/workflow.md vs .claude/skills/ 乖離チェック

| スキル | workflow.md セクション | 記述の一致 | 備考 |
|--------|---------------------|:---------:|------|
| config-optimizer-manager | config最適化セッション フロー | OK | 3フェーズ構成・CO ターゲット・ワーカー構成が一致 |
| automation-manager | オートメーションメンテナンスセッション フロー | OK | AT タスク定義・ワーカーセット数基準が一致 |
| マネージャー共通ポリシー | マネージャーセッション共通ポリシー | **NG** | 下記「乖離の詳細」参照 |

#### 乖離の詳細

| # | 箇所 | workflow.md の記述 | SKILL.md の記述 | 乖離内容 |
|---|------|------------------|----------------|---------|
| 1 | マネージャー数と一覧 | 「6つ: l1, triage, meta, sync, bm, **automation**」（L623, L639） | 「6つ: l1, triage, meta, sync, bm, **config-optimizer**」（L3, L9） | workflow.md は automation を含み config-optimizer を含まない。SKILL.md は逆。実際は7マネージャー |
| 2 | manager-common-policy §1 テーブル | - | config-optimizer-manager のみ記載。automation-manager 欠落 | §1 適用対象から automation-manager が脱落 |
| 3 | manager-common-policy §9 関連ファイル | - | automation-manager の SKILL.md・agents が未記載 | 関連ファイル一覧の網羅性不足 |

**重大度**: 高（適用対象の不整合は、automation-manager が共通ポリシーの適用対象外と誤認されるリスクがある）

### 参考資料（ドラフト）ステータスチェック

| ファイル | バナー有無 | 統合状況 | 実態との矛盾 | 備考 |
|---------|:---------:|---------|:----------:|------|
| docs/coordination-protocol-guideline.md | OK | 一部統合済み | なし | セクション2.2 → .claude/rules/commit-message.md（実際に存在確認済み） |
| docs/git-worktree-guideline.md | OK | 一部統合済み | なし | l1-impl-manager の worktree 手順として統合済み |

### docs/ 分類テーブル網羅性

| ファイル | CLAUDE.md テーブル記載 | 備考 |
|---------|:-------------------:|------|
| docs/workflow.md | あり | 可視化文書 |
| docs/management-system-guide.md | あり | 運用ガイド |
| docs/subagent-permission-guide.md | あり | 運用ガイド |
| docs/implementation.md | あり | 運用ガイド |
| docs/coordination-protocol-guideline.md | あり | 参考資料（ドラフト） |
| docs/git-worktree-guideline.md | あり | 参考資料（ドラフト） |

全6ファイルが CLAUDE.md テーブルに記載済み。未記載ファイルなし。

### refs/ 孤立エントリ確認

refs/ ディレクトリには `.gitkeep` と `_knowledge_template.md`（テンプレート）のみ。実体エントリなし。孤立エントリなし。

### スキル定義の「関連ファイル一覧」整合性

| スキル | 関連ファイル一覧 | docs/workflow.md 記載 | 備考 |
|--------|:-------------:|:-------------------:|------|
| config-optimizer-manager/SKILL.md | あり | あり | OK |
| automation-manager/SKILL.md | あり | あり | OK |
| manager-common-policy/SKILL.md | あり | あり | ただし automation-manager 関連が欠落 |

---

## TG-008: セッション構造標準ポリシーチェック

### 走査結果サマリ
- 走査対象ファイル数: 14件（マネージャー3件 + エージェント8件 + 共通ポリシー3件）
- 不適合件数: 1件（必須: 0件 / 推奨: 0件 / 軽微: 0件 / メタルール不整合: 1件）

### ファイル別チェック結果

#### 重点対象1: config-optimizer-manager（新設）

| ファイル | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール | 総合判定 |
|---------|:-------------:|:----------:|:--------:|:----------:|:-------:|
| config-optimizer-manager/SKILL.md | OK | OK | OK | OK | OK |
| agents/config-collection-worker.md | OK | OK | OK | OK | OK |
| agents/config-analysis-worker.md | OK | OK | OK | OK | OK |
| agents/config-proposal-worker.md | OK | OK | OK | OK | OK |
| agents/config-optimizer-evaluator.md | OK | OK | OK | OK | OK |

**詳細**:
- A: 3フェーズ構成（Collection → Analysis → Proposal）の各フェーズに壁打ち・計画・レポート・ゲート判定あり。知見集約は manager-common-policy §5 参照
- B: config-optimizer-evaluator に3ワーカーとの対称性確認テーブルあり（壁打ち/計画/レポート/知見/課題/停止の6要素）。SKILL.md に worker→evaluator 順序制約明記
- C: 全エージェントに 07_issues.md 経由の課題起票を明記。知見記録セクション（ルール化候補/参考情報）が worker・evaluator 双方に定義
- D: 全エージェントに「やること」「やらないこと」「停止ルール」「担当ファイル」テーブルが完備

#### 重点対象2: automation-manager（大幅更新）

| ファイル | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール | 総合判定 |
|---------|:-------------:|:----------:|:--------:|:----------:|:-------:|
| automation-manager/SKILL.md | OK | OK | OK | OK | OK |
| agents/automation-worker.md | OK | OK | OK | OK | OK |
| agents/automation-evaluator.md | OK | OK | OK | OK | OK |

**詳細**:
- A: 壁打ち（事前調査）・計画・ワーカーディスパッチ・レポート・ゲート判定・知見集約の全ステージ完備
- B: automation-evaluator に対称性確認テーブルあり（6要素すべて確認）。SKILL.md に逐次起動明記（manager-common-policy §2.2 参照）
- C: 07_issues.md 経由の課題起票、知見記録セクション（ルール化候補/参考情報）が worker・evaluator 双方に定義
- D: 全エージェントに必要な構造要素完備

#### 重点対象3: l1-impl-manager（大幅更新）

| ファイル | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール | 総合判定 |
|---------|:-------------:|:----------:|:--------:|:----------:|:-------:|
| l1-impl-manager/SKILL.md | OK | OK | OK | OK | OK |
| agents/investigation-worker.md | OK | OK | OK | OK | OK |
| agents/design-worker.md | OK | OK | OK | OK | OK |
| agents/impl-plan-worker.md | OK | OK | OK | OK | OK |
| agents/impl-worker.md | OK | OK | OK | OK | OK |
| agents/impl-evaluator.md | OK | OK | OK | OK | OK |

**詳細**:
- A: 4フェーズ（Investigation → Design → Impl Planning → Implementation）の各フェーズに壁打ち・計画・実施・レポート・ゲート判定あり。Phase 4 の impl-worker は知見記録 N/A（B+C集約方式のため）→ triage-standard-policy マトリクスと整合
- B: impl-evaluator に5ワーカーとの対称性確認テーブルあり。SKILL.md に worker→evaluator 順序制約明記（Phase 4 のみ Wave 方式並列許可）
- C: 07_issues.md + per-worker 07_issues_W<N>.md の統合手順が明記。知見記録セクションが Phase 1-3 ワーカー・evaluator に定義
- D: 全エージェントに「やること」「やらないこと」「停止ルール」「担当ファイル」テーブル完備。impl-worker は ESCALATE メカニズムあり

#### 共通ポリシー3件

| ファイル | チェック結果 | 備考 |
|---------|:---------:|------|
| manager-common-policy/SKILL.md | **NG** | §1 適用対象テーブルに automation-manager 欠落。§9 関連ファイルに automation-manager 関連未記載 |
| session-flow-policy/SKILL.md | OK | §5 セッションタイプテーブルに全8タイプ記載済み |
| triage-standard-policy/SKILL.md | OK | 適用マトリクスに全セッションタイプ列あり。走査対象一覧に全スキルパス記載 |

### 不適合の詳細

| # | ファイル | チェック項目 | 不適合内容 | 重大度 | CSV起票 |
|---|---------|------------|----------|--------|---------|
| 1 | manager-common-policy/SKILL.md | E.メタルール横断整合性 | §1 適用対象テーブル・description・§9 関連ファイルに automation-manager が欠落。workflow.md とも不整合（workflow.md は automation を含み config-optimizer を含まない） | 高 | 07_issues.md に起票済み |

---

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票済み）
- manager-common-policy の適用対象不整合 + workflow.md との乖離（07_issues.md に起票済み）

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 新セッションタイプ追加時の連動更新漏れパターン | manager-common-policy, workflow.md | config-optimizer-manager 追加時に manager-common-policy を更新したが automation-manager が脱落。workflow.md は別タイミングで automation-manager を反映したが config-optimizer-manager が未反映。セッションタイプ追加時の連動更新チェックリスト（session-flow-policy §5.1）に「manager-common-policy §1 の適用対象テーブル更新」を追加することを推奨 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | config-optimizer-manager は非常に高品質に整備されている | 3フェーズ構成の各フェーズでワーカー・evaluator の対称性が完全に担保されており、ペアリング対称性確認テーブルも evaluator に含まれている。新セッションタイプ作成時のリファレンス実装として適切 |
| 2 | impl-worker (Phase 4) の知見記録 N/A は設計上の意図的判断 | B+C集約方式のため worker 個別の知見記録は不要。triage-standard-policy マトリクスでも N/A と明記されており整合している |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
