# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| BM-001 | backlog/entries/ 長期滞留検出 | 完了 |
| BM-002 | backlog/entries/ vs 完了施策17件 照合 | 完了 |

---

## BM-001: 長期滞留エントリの検出（簡易チェック）

### 90日以上滞留エントリ

**検出件数: 0件**

全92件のエントリの起票日は 2026-02-25 〜 2026-03-17 の範囲にあり、最大経過日数は 20日。90日以上の長期滞留エントリは存在しない。

### Top5 最古エントリ

| 順位 | BL-ID | 施策名 | 起票日 | 経過日数 | ステータス |
|------|-------|--------|--------|---------|-----------|
| 1 | BL-005 | マルチAIエージェント共通ルール適用（Devin 対応） | 2026-02-25 | 20日 | 候補 |
| 2 | BL-004 | ハーネスエンジニアリング観点でのブラッシュアップ | 2026-03-01 | 16日 | 完了 |
| 3 | BL-007 | 北村さんの取り組みを取り込む | 2026-03-02 | 15日 | 候補 |
| 4 | BL-009 | Stage 3: 高度な並列化 + 協調プロトコル統合 | 2026-03-02 | 15日 | 候補 |
| 5 | BL-001 | LLM ローカル開発のセキュリティ強化 | 2026-03-03 | 14日 | 候補 |

### 経過日数分布サマリ

| 経過日数 | 件数 | 比率 |
|---------|------|------|
| 0〜7日 | 62件 | 67.4% |
| 8〜14日 | 26件 | 28.3% |
| 15〜21日 | 4件 | 4.3% |
| 22日以上 | 0件 | 0.0% |
| **合計** | **92件** | **100%** |

### BM-001 所見

- バックログの運用開始が約3週間前（2026-02-25）であるため、長期滞留は構造的に発生しない段階
- 最古の BL-005（20日）は `ai-driven-dev-patterns` 対象かつ低優先度のため、自然な滞留
- 過半数（67.4%）が起票後1週間以内であり、活発にバックログが蓄積されている状態

---

## BM-002: 関連施策での解決状況確認（17件の完了施策との照合）

### 走査対象

- 全92件のうち、.md ファイルでステータスが「完了」の7件をスキップ
- 残り85件（候補84件 + initiative開始済1件）を走査対象とした

### 解消済みエントリ一覧

| # | BL-ID | 施策名 | 解消の根拠となる完了施策 | 解消確度 | 備考 |
|---|-------|--------|----------------------|---------|------|
| 1 | BL-033 | 施策間の競合防止方針策定 | l1-manager-enhanced-planning | 部分的解消 | parallel-dev.md のコンフリクトチェックマトリクス（Conflict Check Matrix）により、同一 Wave 内のタスク間ファイル競合は事前検出される。ただし異なるブランチ上の施策間での競合防止（BL-033 の主課題）は未解決 |
| 2 | BL-052 | backlog-maintenance-worker 走査手順改善 | csv-conflict-prevention | 部分的解消 | CSV/エントリ間の優先度不一致問題（課題2）は .md → CSV 自動生成により原理的に解消される。ただし BM タスクでの機械的集計手順の定義（課題1）は未解決 |
| 3 | BL-077 | backlog エントリ旧フォーマット統一 | csv-conflict-prevention | 部分的解消 | csv-conflict-prevention 施策で旧フォーマット backlog 13件のテーブル形式変換を実施（スコープ内）。ただし csv-conflict-prevention の主目的は CSV 自動生成であり、旧フォーマットの完全統一が完了したかは要確認 |
| 4 | BL-084 | 並列セッション環境でのBL ID衝突防止 | csv-conflict-prevention | 部分的解消 | csv-conflict-prevention でファイル名ベースの ID 管理に移行。ただし並列セッションでの .md ファイル名の採番衝突は別の問題であり、完全には解消されていない |

### 非解消判定の主要エントリ（完了施策と関連あるが解消には至らないもの）

| BL-ID | 施策名 | 関連する完了施策 | 非解消理由 |
|-------|--------|---------------|-----------|
| BL-042 | session-flow-policy §5.1 チェックリスト精度向上 | session-lifecycle-policy-rename | リネームのみで、チェックリスト内容の精度向上は未対応。なお BL-042 のエントリ名は旧名称「session-flow-policy」のままであり、参照名の更新が必要 |
| BL-043 | session-lifecycle-policy テーブル幅肥大化 | session-lifecycle-policy-rename | リネームのみで、テーブル幅の問題は未対応 |
| BL-046 | 条件付き固定タスク配置ルール整備 | l1-manager-enhanced-planning | Phase 構造再構築により固定タスクセクションの文脈は変化したが、条件付き/無条件タスクの視覚的分離は直接対応されていない |
| BL-053 | L1マネージャー実作業禁止の構造的強制 | l1-manager-enhanced-planning | plan-worker 導入により計画フェーズがワーカー委譲されるが、L1 が施策ファイル（スキル定義等）を直接編集する構造的禁止は実装されていない |
| BL-073 | ドメインエージェント活用状況レビュー | agency-agents-integration | 明示的に後続施策として起票された項目。agency-agents-integration は基盤構築のみ |
| BL-074 | ドメインエージェント参照の他マネージャー展開 | agency-agents-integration | 明示的に後続施策として起票された項目。l1-manager のみに適用 |
| BL-078 | backlog-auto-execute.yml GHA スキル分離 | gha-initiative-skills-separation | 明示的にスコープ外とされた後続施策 |
| BL-079 | GHA スキル用途クラス別テンプレート化 | gha-session-prompt-conversion-pattern | 評価レポートからの知見であり、変換パターン施策自体では対応していない |
| BL-080 | gha-skills-mapping initiative 登録 | gha-initiative-skills-separation | skills-separation でスキル作成は完了したが mapping.yml への登録は ISS-063 として課題化されたままの可能性あり |
| BL-081 | GHA ワークフロー責務移動の対検証パターン | gha-wallbash-iterative-phase | wallbash 施策で知見は得られたが、評価テンプレートへの制度化は未実施 |
| BL-083 | refs/ メタ情報テンプレート標準化 | agency-agents-integration + refs-work-log-directory | agency-agents で knowledge.md にメタ情報を実践、refs-work-log で二層構造を確立したが、_knowledge_template.md へのメタ情報セクション追加は未実施 |

### 完了施策と backlog エントリの対応がないもの（17施策中）

以下の完了施策は、未解消 backlog エントリとの直接的な対応関係がなかった:

| 完了施策 | 理由 |
|---------|------|
| gha-issue-usage-guide | GHA コメント UX 改善であり、対応する backlog エントリなし |
| backlog-to-issue-scheduled | スケジュールトリガー実装。対応する backlog エントリなし |
| backlog-template-legend-enhancement | 対応する BL-010 は既に完了ステータス |
| dev-workflow-detail-l1-ref-review | 対応する BL-002 は既に完了ステータス |
| automation-action-step | automation-manager の Step 7 詳細化。対応する backlog エントリなし |
| backlog-to-issue-schedule-frequency | 頻度変更のみ。対応する backlog エントリなし |
| backlog-to-issue-status-sync | ログ調査からの新規施策。対応する backlog エントリなし |
| skill-plugin-overlap-check-rule | 対応する BL-064 は既に完了ステータス |
| session-artifacts-structure-refactor | 対応する BL-072 は既に完了ステータス |

---

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票）
- CSV とエントリ .md ファイル間のステータス不一致（4件）

---

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | CSV と .md のステータス不一致が4件存在 | backlog/backlog.csv, backlog/entries/ | BL-004, BL-010, BL-012, BL-072 の4件で .md は「完了」だが CSV は「候補」のまま。csv-conflict-prevention 施策で .md → CSV 自動生成が実装されているはずだが、反映されていない。PreCommit hook の実行タイミングまたは CSV 再生成スクリプトのステータスマッピングに問題がある可能性 |
| 2 | BL-042 のエントリ名が旧名称「session-flow-policy」のまま | backlog/entries/session-flow-checklist-precision.md | session-lifecycle-policy-rename 施策で triage-standard-policy → session-lifecycle-policy にリネーム済みだが、BL-042 エントリ本文の参照名が旧名称のまま。backlog エントリ内の参照パスも連動更新の対象にすべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | BM-002 の部分的解消判定は次回 BM で再確認が必要 | csv-conflict-prevention 施策は .md 上で完了ステータスだが、旧フォーマット変換（BL-077 関連）や ID 衝突防止（BL-084 関連）の実効性は成果物を詳細確認しないと確定できない |
| 2 | 完了施策から明示的に後続起票された backlog エントリが複数存在 | BL-073, BL-074（agency-agents-integration から）、BL-078, BL-079, BL-080, BL-081（gha 系施策から）など。これらは「解消」ではなく「次段階」として意図的に残されている |
| 3 | l1-manager-enhanced-planning の影響範囲が広い | Phase構造再構築、plan-worker 導入、並列ディスパッチなど L1 のフロー全体に影響する変更であり、関連する backlog エントリ（BL-033, BL-046, BL-053）への間接的影響がある |

---
**作成者**: バックログメンテナンスワーカー
**作成日**: 2026-03-17
