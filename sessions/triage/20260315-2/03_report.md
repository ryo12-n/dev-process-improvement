# トリアージ振り返りレポート: 2026-03-15（2回目）

## サマリ

前回トリアージ（20260315 1回目）から同日2回目。inbox 17件の分類、backlog 72件の突合・関係性分析、CSV 28件の棚卸し、initiative 5件の状態確認、ルール/workflow 整合性チェック、GHA ↔ Skills 整合性チェックを2セットで実施した。主要な発見: (1) inbox から backlog 候補8件・ルール反映4件を抽出、(2) gha-skills-mapping.yml のファイル参照 stale を CRITICAL ドリフトとして検出、(3) README の git-worktree-guideline.md 統合状況乖離を検出、(4) backlog 新規21件のテンプレート非準拠を確認、(5) backlog 関係性分析でコンテキスト最適化・セキュリティ二重防御の統合候補を特定。TG-008 はスキップ（同日実施済み）、TG-009 は条件未達でスキップ。

## Worker Set サマリ

| Set | 担当 TG タスク | 評価結果 | 備考 |
|-----|--------------|---------|------|
| set-1 | TG-001, TG-003, TG-004, TG-007 | 条件付き承認 | inbox 17件分類、CSV 28件棚卸し、initiative 5件確認、README 整合性。TG-003 件数不一致は軽微 |
| set-2 | TG-002, TG-005, TG-006, TG-010 | 条件付き承認 | backlog 突合、関係性分析、ルール整合性、GHA整合性。TG-002 品質チェック範囲は BL-054〜BL-074 全21件に拡大 |

## 走査結果

### inbox（TG-001）

全17件を分類。

| # | ファイル名 | 分類 | 備考 |
|---|-----------|------|------|
| 1 | ai-driven-dev-patterns-design-vs-operation-gap.md | backlog候補 | 優先度: 低。設計構想と実運用の乖離調査 |
| 2 | backlog-entries-format-unification.md | backlog候補 | 優先度: 低。旧フォーマット13件の統一 |
| 3 | backlog-target-repo-column-guideline.md | ルール反映 | l1-manager/backlog テンプレートに反映 |
| 4 | gha-auto-execute-skills-separation.md | backlog候補 | 優先度: 中。GHA スキル分離パターン適用 |
| 5 | gha-skill-usage-class-template.md | backlog候補 | 優先度: 低。用途クラス別テンプレート化 |
| 6 | gha-skills-mapping-initiative-coverage.md | 重複 | #7 に統合 |
| 7 | gha-skills-mapping-initiative-registration.md | backlog候補 | 優先度: 中。マッピング追加 |
| 8 | gha-trigger-coexistence-job-isolation.md | ルール反映 | gha-workflow-security.md に追記 |
| 9 | gha-user-input-escape-rule.md | ルール反映 | gha-guideline に追記。ISS-059 関連 |
| 10 | gha-workflow-responsibility-transfer-verification.md | backlog候補 | 優先度: 低。責務移動の対検証 |
| 11 | gha-workflow-trigger-change-reindex.md | 対応不要 | 知見記録。削除 |
| 12 | gha-yaml-heredoc-conflict.md | 対応不要 | 知見記録。削除 |
| 13 | import-inline-expansion-limitation.md | 対応不要 | BL-068 参考情報。削除 |
| 14 | plugin-staged-introduction.md | 重複（BL-058 吸収） | BL-058 と実質同一テーマ |
| 15 | posttooluse-hook-quality-check.md | backlog候補 | 優先度: 中。PostToolUse hook 品質チェック |
| 16 | refs-intake-plan-verification.md | ルール反映 | l1-manager に外部リポ構成確認ステップ追加 |
| 17 | refs-meta-info-template.md | backlog候補 | 優先度: 低。メタ情報テンプレート |

**分類サマリ**: backlog候補 8件 / ルール反映 4件 / 対応不要 3件 / 重複 2件

### backlog 棚卸し（TG-002）

72件を突合（BL-032/BL-061 欠番）。評価者指摘に基づき、テンプレート非準拠の対象を BL-054〜BL-074 全21件に拡大。

| 項目 | 結果 |
|------|------|
| 完了済みエントリ（BL-002, BL-031） | _archive/ に存在確認済み。正常 |
| 進行中エントリ（BL-020） | initiatives/ に存在確認済み。正常 |
| 施策化済み CSV 未登録（initiatives/ 直接起票） | 4件（backlog-id-and-issue-template, external-repo-cleanup-on-demand, impl-worker-worklog-reliability, triage-phase-gate-and-gha-sync） |
| 対象リポジトリ未記入 | 0件 |
| テンプレート非準拠（BL-054〜BL-074） | 21件。「依存する環境前提」「関連エントリ」「起票時チェックリスト」欠落。BL-067〜BL-072 は「概要」セクション使用 |
| 削除・クローズ候補 | なし |

### 課題管理 CSV（TG-003）

新規4件（ISS-059〜ISS-062）の確認と既存24件の棚卸し。

| ID | タイトル | 種別 | 優先度 | 特記事項 |
|----|---------|------|--------|---------|
| ISS-059 | GHA ユーザー入力シェルインジェクションリスク | リスク | 高 | inbox #9 に対応ルール提案 |
| ISS-060 | session-flow-policy 連動更新漏れ | 改善提案 | 中 | 前回トリアージで起票 |
| ISS-061 | deny ルール非機能性 | リスク | 高 | BL-071 + BL-067 で対応 |
| ISS-062 | PreToolUse hook バイパスリスク | リスク | 中 | sandbox 二重防御が必須 |

**セキュリティクラスタ**: ISS-045/059/061/062 が多層防御の連鎖リスクを形成。BL-067/BL-071 が対応施策。

**長期滞留課題**: ISS-006（20日）、ISS-013（18日）等7件。前提条件未整備や低優先度による正当な保留が多い。

### backlog 関係性分析（TG-005）

重複2組・依存6組・統合5グループを検出。

| 関係種別 | エントリ | 詳細 | 提案 |
|---------|---------|------|------|
| 重複 | BL-008 ↔ BL-068 | BL-068 は BL-008 の部分実装手段 | BL-068 を BL-008 下位施策に統合 |
| 重複 | BL-008 ↔ BL-070 | BL-070 は BL-008 の主要実装手段 | BL-070 を BL-008 下位施策に統合 |
| 依存 | BL-067 → BL-071 | 二重防御の前提 | 同時実施推奨 |
| 依存 | BL-068 → BL-070 | rules/ 委譲が path-scoped 前提 | BL-070 先行 |
| 依存 | BL-073 → agency-agents-integration | 施策完了が前提 | 施策完了待ち |
| 依存 | BL-074 → agency-agents-integration | 施策完了が前提 | 施策完了待ち |
| 依存 | BL-074 → BL-073 | レビュー実績後 | 順次実施 |
| 依存 | BL-069 → gha-initiative-skills-separation | 分離完了が前提 | 施策完了待ち |
| 統合 | BL-008 + BL-068 + BL-070 | コンテキスト最適化 | 親施策 BL-008 に統合 |
| 統合 | BL-067 + BL-071 | セキュリティ二重防御 | 統合推奨 |
| 統合 | BL-029 + BL-067 | PreToolUse hook 基盤共有 | 基盤部分のみ統合検討 |
| 統合 | BL-055 + BL-057 | GHA 自動化拡張 | 統合推奨 |
| 統合 | BL-073 + BL-074 | ドメインエージェント展開 | 統合推奨 |

### initiative 状態確認（TG-004）

| 施策名 | BL-ID | フェーズ | 状態 | 特記事項 |
|--------|-------|---------|------|---------|
| backlog-id-and-issue-template | - | 実施前 | 正常 | 全5タスク未着手 |
| external-repo-cleanup-on-demand | - | 評価待ち | 正常 | 作業完了、evaluator ディスパッチ要 |
| impl-worker-worklog-reliability | - | 実施前 | 正常 | 全5タスク未着手 |
| sync-worker-target-commit | BL-020 | 実施前 | 正常 | テンプレート状態 |
| triage-phase-gate-and-gha-sync | - | 実施前 | 正常 | 全8タスク未着手 |

### ルール・workflow 整合性（TG-006）

- 前回修正反映: 7項目すべて OK
- 参考資料ステータスチェック: 2件問題なし
- docs/ テーブル網羅性: 全6ファイル記載済み
- **README 乖離**: git-worktree-guideline.md の統合状況が「未着手」→実態は「一部統合済み」

### GHA ↔ Skills 整合性チェック（TG-010）

| マッピングID | ドリフト | 重大度 | 詳細 |
|------------|---------|--------|------|
| triage-gha | なし | - | inherent_differences 5件すべて有効 |
| l1-auto-execute-gha | ファイル参照 stale | CRITICAL | `backlog-auto-execute.yml` → 実際は `initiative-execute.yml` |
| initiative 系4件 | マッピング未定義 | WARNING | wallbash/execute/close/question の4スキル |

## backlog 追加・変更案

### 追加候補

| 優先度 | 施策名 | 課題概要 | 期待効果 | inbox元 |
|--------|--------|---------|---------|---------|
| 低 | ai-driven-dev-patterns-design-vs-operation-gap | 設計構想と実運用の乖離調査 | 設計文書の実用性向上 | #1 |
| 低 | backlog-entries-format-unification | 旧フォーマット13件の統一 | BM走査・トリアージ効率改善 | #2 |
| 中 | gha-auto-execute-skills-separation | backlog-auto-execute.yml の GHA スキル分離 | GHA ワークフロー保守性向上 | #4 |
| 低 | gha-skill-usage-class-template | GHA スキル用途クラス別テンプレート | スキル定義の標準化 | #5 |
| 中 | gha-skills-mapping-initiative-registration | initiative 4件のマッピング追加 | TG-010 精度向上 | #7 |
| 低 | gha-workflow-responsibility-transfer-verification | 責務移動の対検証テンプレート | GHA 変更の検証品質向上 | #10 |
| 中 | posttooluse-hook-quality-check | PostToolUse hook 品質チェック自動化 | 規約違反の自動検出 | #15 |
| 低 | refs-meta-info-template | refs/ メタ情報テンプレート | 参照物管理の標準化 | #17 |

### 優先度変更候補

なし

### 削除・クローズ候補

なし（BL-002/BL-031 は完了ステータスで正常）

## 振り返り

### うまくいったこと
- 2セット構成で効率的に全TGタスクを完了（TG-008/TG-009 は適切にスキップ）
- Set-1/Set-2 ともに評価者が具体的な補完点を指摘し品質向上に寄与

### 改善すべきこと
- BL-054〜BL-074 全21件のテンプレート非準拠が検出された。起票時のテンプレート強制メカニズムが必要
- TG-005 で前回結果との差分説明が欠如。ワーカーへの指示に差分記載を含めるべき

### プロセス改善の気づき
- 自動起票ツール（config-optimizer-manager 等）の出力がテンプレートに準拠していない
- CSV 棚卸し時のステータス別件数検証手順の追加が望ましい
- GHA スキル改名時の gha-skills-mapping.yml 更新漏れパターンを防止する仕組みが必要

### 次回トリアージへの申し送り

なし（全アクションを当セッション内で完了予定）

## 知見集約

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 Set | 対象ファイル・領域 | 詳細 |
|---|------|----------|-----------------|------|
| 1 | GHA 関連 inbox 集中時の分類細分化 | set-1 worker | triage-manager / inbox | 17件中11件が GHA 関連。活発時には「GHA ルール/スキル/ワークフロー」に細分化 |
| 2 | セキュリティ課題の多層防御クラスタ管理 | set-1 worker | 課題管理 CSV | ISS-045/059/061/062 の連鎖リスク。セキュリティ施策は優先的にクラスタ管理すべき |
| 3 | CSV 棚卸し時のステータス別件数検証手順 | set-1 evaluator | triage-worker エージェント定義 | 集計後に ID リストの件数と報告値の一致を確認するステップ追加 |
| 4 | config-optimization 起票元のテンプレート非準拠 | set-2 worker | backlog/_template.md, config-optimizer-manager | 起票時にテンプレート準拠を強制する仕組みが必要 |
| 5 | GHA スキル改名時のマッピングマニフェスト更新漏れ | set-2 worker | .github/gha-skills-mapping.yml | ワークフロー改名時の連動更新チェック |
| 6 | 品質チェック時の対象範囲明示ルール | set-2 evaluator | triage-worker エージェント定義 | 「特に注目」は重点チェック指示であり対象範囲の絞り込みではない旨を明確化 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 Set | 背景・文脈 |
|---|------|----------|-----------|
| 1 | 進行中施策5件中4件が実施前で滞留 | set-1 worker | L1 セッション頻度見直しの検討材料 |
| 2 | 「起票」ステータスの長期滞留課題7件（15日以上） | set-1 worker | 正当な保留が多いが定期棚卸しでステータス移行判断が必要 |
| 3 | ISS-025 の "reviewer" ステータスが標準値外 | set-1 evaluator | CSV ステータス値の列挙定義の明文化を検討 |
| 4 | CSV 未登録の進行中 initiative 4件 | set-2 worker | 施策管理の網羅性向上、または「CSV 登録不要な施策」基準の明確化 |
| 5 | コンテキスト最適化系施策の親子関係 | set-2 worker | BL-008 が上位目標、BL-068/BL-070 が実装手段。親子関係の表現手段が必要 |
| 6 | 関係性分析での前回差分記載 | set-2 evaluator | ワーカー指示に差分説明を含めることを検討 |

## 課題集約

### ワーカーセット別課題件数

| Set | 課題件数 | CSV転記件数 | 備考 |
|-----|---------|-----------|------|
| set-1 | 1件 | 0件 | README 乖離（当セッション修正） |
| set-2 | 3件 | 1件 | テンプレート非準拠・README 乖離・GHA マッピング stale |

### CSV転記済み課題

| ISS-ID | タイトル | 発見元 Set | 優先度 |
|--------|---------|----------|--------|
| ISS-063 | gha-skills-mapping.yml のファイル参照 stale + initiative 系マッピング未定義 | set-2 | 中 |

## 課題起票

- 起票した課題（合計）：1件（プロセス改善_課題管理.csv に転記済み）
- 当セッション修正: 2件（README 乖離修正 × 2）
- テンプレート非準拠: BL-054〜BL-074 の21件は既存の BL-010（backlogテンプレート凡例強化）のスコープに含まれるため別途起票不要

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-15
**レビュー依頼先**: ユーザー
**レビュー状態**: レビュー待ち
