# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox 17件の分類 | 完了 |
| TG-003 | CSV 課題管理棚卸し | 完了 |
| TG-004 | 進行中施策5件の状態確認 | 完了 |
| TG-007 | README 整合性チェック | 完了 |

---

## TG-001: inbox 走査

### 分類結果

| # | アイテム | 判断 | 理由 |
|---|---------|------|------|
| 1 | ai-driven-dev-patterns-design-vs-operation-gap.md | backlog候補 | dev-workflow-detail.md §8 の設計構想と実運用の乖離調査。独立した施策テーマ |
| 2 | backlog-entries-format-unification.md | backlog候補 | 13件の旧フォーマットエントリの統一。BM走査・トリアージ効率改善 |
| 3 | backlog-target-repo-column-guideline.md | ルール反映 | backlog 起票ガイドラインへの「対象リポジトリ」記載基準追記。l1-manager または backlog テンプレートに反映可能 |
| 4 | gha-auto-execute-skills-separation.md | backlog候補 | backlog-auto-execute.yml への GHA スキル分離パターン適用。独立施策 |
| 5 | gha-skill-usage-class-template.md | backlog候補 | GHA スキルの「やらないこと」セクションの用途クラス別テンプレート化。gha-guideline 改善 |
| 6 | gha-skills-mapping-initiative-coverage.md | 重複 | gha-skills-mapping-initiative-registration.md（#7）と実質同一テーマ。#7 に統合推奨 |
| 7 | gha-skills-mapping-initiative-registration.md | backlog候補 | gha-skills-mapping.yml に initiative 4件のマッピング追加。TG-010 ドリフト検出に必要 |
| 8 | gha-trigger-coexistence-job-isolation.md | ルール反映 | .claude/rules/gha-workflow-security.md のチェック項目に追加可能。小規模変更 |
| 9 | gha-user-input-escape-rule.md | ルール反映 | gha-guideline SKILL.md または rules/ に追加。ISS-059 と関連。セキュリティ上重要 |
| 10 | gha-workflow-responsibility-transfer-verification.md | backlog候補 | GHA ワークフロー変更施策の評価項目テンプレートへの「責務移動の対検証」追加 |
| 11 | gha-workflow-trigger-change-reindex.md | 対応不要 | GitHub Actions の再インデックス遅延に関する知見。現象の記録であり施策化不要。refs/ に移動するか inbox から削除 |
| 12 | gha-yaml-heredoc-conflict.md | 対応不要 | YAML ブロックスカラーと HEREDOC の競合に関する知見。現象の記録であり施策化不要。refs/ に移動するか inbox から削除 |
| 13 | import-inline-expansion-limitation.md | 対応不要 | @import のインライン展開はコンテキスト削減に寄与しない知見。BL-068（claude-md-import-shrink）の計画時参考情報として把握済み |
| 14 | plugin-staged-introduction.md | backlog候補 | 高優先度プラグイン4件の段階的導入。BL-058（plugin-high-applicability-trial）と重複の可能性あり → 確認要 |
| 15 | posttooluse-hook-quality-check.md | backlog候補 | PostToolUse hook による品質チェック自動化。BL-030（PostToolUse-hookルール変更連動チェック）と関連するが観点が異なる（行数/フロントマター検証 vs ルール変更連動） |
| 16 | refs-intake-plan-verification.md | ルール反映 | l1-manager の計画作成フローに外部リポジトリ構成確認ステップ追加。小規模変更 |
| 17 | refs-meta-info-template.md | backlog候補 | refs/_knowledge_template.md にメタ情報セクション追加。独立した小規模施策 |

### 分類サマリ

| 分類 | 件数 | 対象 |
|------|------|------|
| backlog候補 | 8件 | #1, #2, #4, #5, #7, #10, #15, #17 |
| ルール反映 | 4件 | #3, #8, #9, #16 |
| 対応不要 | 3件 | #11, #12, #13 |
| 重複 | 1件 | #6（→ #7 に統合） |
| 要確認 | 1件 | #14（BL-058 との重複確認要） |

---

## TG-003: 課題管理 CSV 棚卸し

### 新規4件の確認

| ID | タイトル | 種別 | 優先度 | ステータス | 関連施策 | 特記事項 |
|----|---------|------|--------|-----------|---------|---------|
| ISS-059 | GHA ユーザー入力 JSON 構築にシェルインジェクションリスク | リスク | 高 | 起票 | initiative-dispatcher | セキュリティ。inbox #9 に対応ルール提案あり |
| ISS-060 | 新セッションタイプ追加時の manager-common-policy 連動更新漏れ | 改善提案 | 中 | 起票 | triage/20260315 | session-flow-policy チェックリスト改善 |
| ISS-061 | settings.json deny ルールの非機能性（v1.0.93 既知バグ） | リスク | 高 | 起票 | config-optimization | BL-071 + BL-067 で二重防御構築が対応方針 |
| ISS-062 | PreToolUse hook Bash パターンマッチングのバイパスリスク | リスク | 中 | 起票 | config-optimization | sandbox との二重防御が必須 |

### 既存課題ステータス棚卸し

| ステータス | 件数 | ID 範囲 |
|-----------|------|---------|
| クローズ | 33件 | ISS-001〜ISS-005, ISS-007〜ISS-012, ISS-014〜ISS-015, ISS-017〜ISS-018, ISS-023, ISS-025〜ISS-026, ISS-028〜ISS-030, ISS-034〜ISS-037, ISS-040〜ISS-041, ISS-048, ISS-051 |
| 起票 | 24件 | ISS-006, ISS-013, ISS-016, ISS-019〜ISS-022, ISS-027, ISS-031〜ISS-033, ISS-038〜ISS-039, ISS-042〜ISS-047, ISS-049〜ISS-050, ISS-052〜ISS-058 |
| 方針確定 | 1件 | ISS-031 |
| 新規（今回） | 4件 | ISS-059〜ISS-062 |

### 長期滞留課題（起票ステータスで3回以上のトリアージを通過）

| ID | タイトル | 起票日 | 滞留期間 | 推奨アクション |
|----|---------|--------|---------|-------------|
| ISS-006 | ロール定義と OpenSpec 開発ライフサイクルの統合が未定義 | 2026-02-23 | 20日 | 前提条件（OpenSpec ライフサイクル定義）未整備のため保留妥当。定期見直し |
| ISS-013 | Claude Code Agent Teams 機能が worktree ガイドラインで未言及 | 2026-02-25 | 18日 | 低優先度。ガイドライン次回改訂時に対応 |
| ISS-016 | m6o-es-product-api の .claude/rules/ 向けルールファイル整備 | 2026-02-27 | 16日 | 外部リポジトリ依存。優先度中だが着手条件不明 |
| ISS-019 | claude-directory-guide.md の skills/ 移動検討 | 2026-02-27 | 16日 | 低優先度。保留妥当 |
| ISS-020 | config.yaml tasks ルールのカテゴリ分け | 2026-02-28 | 15日 | 低優先度。OpenSpec 運用が安定してから対応 |
| ISS-021 | spec 作成時にエッジケースが漏れやすい | 2026-02-28 | 15日 | 低優先度。チェックリスト化候補 |
| ISS-022 | spec 作成フェーズがボトルネック | 2026-02-28 | 15日 | 中優先度。OpenSpec 運用改善の核心課題 |

### セキュリティ関連課題クラスタ

ISS-045, ISS-059, ISS-061, ISS-062 がセキュリティ防御の多層化に関連する課題群を形成。BL-067（PreToolUse hook）、BL-071（sandbox 有効化）が対応施策として計画済み。

---

## TG-004: 進行中施策の状態確認

| 施策名 | BL-ID | フェーズ | 状態 | 特記事項 |
|--------|-------|---------|------|---------|
| backlog-id-and-issue-template | - | 実施前 | 正常 | proposal/plan/tasks 作成済み、全5タスク未着手。直接起票（BL 経由でない） |
| external-repo-cleanup-on-demand | - | 評価待ち | 正常 | 作業レポート完了（全4タスク完了）、評価レポートはテンプレート状態 |
| impl-worker-worklog-reliability | - | 実施前 | 正常 | proposal/plan/tasks 作成済み、全5タスク未着手 |
| sync-worker-target-commit | BL-020 | 実施前 | 正常 | proposal/plan/tasks 作成済み、作業レポート・評価レポートともテンプレート状態 |
| triage-phase-gate-and-gha-sync | - | 実施前 | 正常 | proposal/plan/tasks 作成済み、全8タスク未着手 |

### 状態サマリ

- 全5件が正常ステータス。ブロックされている施策はなし
- 1件（external-repo-cleanup-on-demand）が評価待ち → L2-evaluator のディスパッチが必要
- 4件が実施前 → L2-worker のディスパッチ待ち

---

## TG-007: README 整合性チェック

### 1. ディレクトリ構成図

| 確認項目 | 整合 | 乖離内容 |
|---------|:----:|---------|
| .claude/rules/ ファイル一覧 | NG | gha-workflow-security.md と rebase-conflict-handling.md が未記載（2件） |
| .claude/skills/ ディレクトリ一覧 | OK | 「起動型のみ記載」の方針に基づき、非起動型（gha-*, policy, checklist 等）の未記載は仕様通り |
| sessions/ サブディレクトリ | NG | automation/, config-optimization/, impl/ が未記載（3件） |
| inbox/, issues/, backlog/, docs/ | OK | 実態と一致 |

### 2. セッション種別テーブル

| 確認項目 | 整合 | 乖離内容 |
|---------|:----:|---------|
| 全セッション種別の網羅 | OK | 8セッション + 2ユーティリティが正しく記載 |
| 使用ルール列のパス | OK | 全パスが実在 |
| 成果物の場所列 | NG | automation-manager の成果物は `sessions/automation/YYYYMMDD/` だが README には記載あり。config-optimizer-manager の成果物は `sessions/config-optimization/YYYYMMDD/` で README にも記載あり。ただしディレクトリ構成図には sessions/automation/ と sessions/config-optimization/ が欠落（上記と重複） |

### 3. AI 向けスキル定義テーブル

| 確認項目 | 整合 | 乖離内容 |
|---------|:----:|---------|
| 起動型スキル（マネージャー系） | OK | 8マネージャー + 2ユーティリティの全10件が記載 |
| 各スキルの構成（agents 等） | OK | 実態と一致 |
| 非起動型スキル | N/A | 「起動型のみ記載」の方針により対象外 |

### 4. ドキュメントマップ

| 確認項目 | 整合 | 乖離内容 |
|---------|:----:|---------|
| 人間向けドキュメント | OK | docs/ 配下6ファイルが正しく分類・記載 |
| 文書分類ポリシー | OK | 4分類が正しく記載 |

### 乖離サマリ

| # | 乖離内容 | 重大度 | 推奨アクション |
|---|---------|--------|-------------|
| 1 | .claude/rules/ に gha-workflow-security.md, rebase-conflict-handling.md 未記載 | 低 | README ディレクトリ構成図に追記 |
| 2 | sessions/ に automation/, config-optimization/, impl/ 未記載 | 中 | README ディレクトリ構成図に追記 |

---

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票済み）
- README ディレクトリ構成図の乖離（sessions/ サブディレクトリ3件 + rules/ ファイル2件の未記載）

---

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | inbox の GHA 関連アイテム集中パターン | triage-manager / inbox | 17件中11件が GHA 関連。GHA 施策の活発な時期には inbox の分類粒度を「GHA ルール」「GHA スキル」「GHA ワークフロー」に細分化すると効率的 |
| 2 | セキュリティ課題の多層防御クラスタ | 課題管理 CSV | ISS-045/059/061/062 が「deny 非機能 → hook バイパス → sandbox 未導入」の連鎖リスクを形成。セキュリティ施策は優先的にクラスタ管理すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | 進行中施策5件中4件が実施前で滞留 | 施策起票ペースに対してワーカーディスパッチが追いついていない可能性。L1 セッションの頻度見直しが必要かもしれない |
| 2 | 「起票」ステータスの長期滞留課題（7件が15日以上） | 前提条件未整備や低優先度による正当な保留が多いが、定期的な棚卸しで「クローズ（保留）」等のステータスに移行するか判断が必要 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
