---
name: manager-overview
description: 'マネージャーセッション全体の責務・連携関係のオーバービュー。整合性管理や新規マネージャー設計時に参照する'
user-invocable: false
---
# マネージャーセッション オーバービュー

> **このファイルの位置づけ**
> 8つのマネージャーセッションの責務・連携関係・共通基盤参照を俯瞰するための参照スキル。
> 詳細は各マネージャーの SKILL.md を参照すること。

---

## §1 責務一覧

| マネージャー | 責務 | トリガー | 主要出力 | サブエージェント |
|-------------|------|---------|---------|----------------|
| L1 (l1-manager) | 施策の提案・計画・タスク分解・L2 オーケストレーション・ゲートレビュー | `backlog: <施策名>` / `施策: <パス>` | 00_proposal, 01_plan, 02_tasks, 08_gate_review | l2-worker, l2-evaluator |
| L1-impl (l1-impl-manager) | コード実装専用の4フェーズオーケストレーション（Investigation → Design → Impl Planning → Implementation） | `impl: <施策名>` / `impl-continue: <パス>` | 00_proposal, 01_plan, phase-1〜4 の各 gate, 08_gate_summary | investigation-worker, design-worker, impl-plan-worker, impl-worker, impl-evaluator |
| triage (triage-manager) | inbox/backlog/CSV の日常的ハウスキーピング + ルール準拠チェック + GHA 整合性チェック | ユーザー任意起動 | 00_pre_investigation, 01_plan, 03_report, 04_gate_review | triage-worker, triage-evaluator |
| metacognition (metacognition-manager) | 施策アーカイブの横断分析・反復パターン検出・未回収知見追跡・プロセス効率評価 | ユーザー任意起動 | 00_pre_investigation, 01_plan, 03_report, 04_gate_review | metacognition-worker, metacognition-evaluator |
| sync (sync-manager) | リポジトリ間の構成・ルール・テンプレートの同期管理 | ユーザー任意起動（同期元・同期先を対話で確定） | 00_pre_investigation, 01_plan, 08_gate_review | sync-worker, sync-evaluator |
| backlog-maintenance (backlog-maintenance-manager) | backlog エントリの陳腐化チェック・鮮度管理（長期滞留・解決済み・前提変化・優先度・重複） | ユーザー任意起動 | 00_pre_investigation, 01_plan, 03_report, 04_gate_review | backlog-maintenance-worker, backlog-maintenance-evaluator |
| automation (automation-manager) | 自動化候補の継続的探索・再評価・進捗追跡・backlog 起票提案 | ユーザー任意起動 | 00_pre_investigation, 01_plan, 03_report, 04_gate_review | automation-worker, automation-evaluator |
| config-optimizer (config-optimizer-manager) | .claude/ 配下の設定ファイルを3フェーズ（情報収集→現状分析→最適化提案）で分析 | `config-optimize` / `config-optimize-continue: <パス>` | 00_pre_investigation, 01_plan, 03_report, 04_gate_review, phase-1〜3 の各 gate | config-collection-worker, config-analysis-worker, config-proposal-worker, config-optimizer-evaluator |

---

## §2 連携フロー

### (1) メインデータフロー

```
inbox/ ──→ [triage-manager] ──→ backlog/entries/
                                      │
                                      ▼
                               [L1-manager] ──→ sessions/initiatives/<施策>/
                                                        │
                                                        ▼ (完了後)
                                                sessions/initiatives/_archive/
                                                        │
                                                        ▼
                                              [metacognition-manager]
                                                        │
                                                        ▼
                                              inbox/ / backlog/ / CSV
```

- **triage** が `inbox/` を走査し、判断済みアイテムを `backlog/entries/` に起票または削除する
- **L1** が `backlog/entries/` から施策を起動し、`sessions/initiatives/` で管理する。完了後 `_archive/` に移動する
- **metacognition** が `_archive/` を横断分析し、知見を `inbox/` / `backlog/` / `CSV` にルーティングする

### (2) 自動化フロー

```
.claude/skills/, sessions/*/ ──→ [automation-manager]
                                        │
                                        ▼
                              automation-candidates/entries/
                                        │
                                        ▼ (起票提案)
                                  backlog/entries/ ──→ [L1-manager] ──→ 施策化
```

- **automation** が skills/rules/テンプレートを走査して新規自動化候補を検出し、`automation-candidates/` で管理する
- 優先度の高い候補を `backlog/entries/` に起票提案し、**L1** が施策化する

### (3) 同期フロー

```
dev-process-improvement ←──→ [sync-manager] ←──→ 外部リポジトリ
                                    │
                                    ▼
                           sessions/sync/YYYYMMDD/
```

- **sync** がリポジトリ間の構成・ルール・テンプレートの差分を検出し、sync-worker に同期作業を委任する
- 同期結果は `sessions/sync/YYYYMMDD/` に記録する

### (4) メンテナンスフロー

```
backlog/entries/ ──→ [backlog-maintenance-manager]
                              │
                              ▼
                     03_report.md (削除候補・優先度変更候補・統合候補)
                              │
                              ▼ (ユーザー承認後)
                     backlog/entries/ の更新・削除
```

- **backlog-maintenance** が `backlog/entries/` を深掘り分析し、陳腐化・解決済み・前提変化・優先度乖離・重複を検出する
- 変更提案は PR レビューでユーザーが承認する

### (5) 設定最適化フロー

```
.claude/ (settings, rules, skills, hooks, CLAUDE.md)
        │
        ▼
[config-optimizer-manager]
   Phase 1: 情報収集 → Phase 2: 現状分析 → Phase 3: 最適化提案
        │
        ▼
backlog/entries/ (施策候補) / inbox/ (洞察) / CSV (課題)
```

- **config-optimizer** が `.claude/` 配下の設定ファイルを公式ドキュメントのベストプラクティスと比較し、3フェーズで最適化提案を行う
- 提案結果を `backlog/` / `inbox/` / `CSV` にルーティングする

---

## §3 共通基盤マッピング

`manager-common-policy` の各セクションを参照しているマネージャーの対応表。

| § | セクション名 | L1 | L1-impl | triage | meta | sync | bm | auto | co |
|---|-------------|:---:|:-------:|:------:|:----:|:----:|:--:|:----:|:--:|
| §1 | 適用対象 | - | - | - | - | - | - | - | - |
| §2.1 | 起動時共通4項目 | o | o | o | o | o | o | o | o |
| §2.2 | ディスパッチ順序制約 | - | o | o | o | - | o | o | o |
| §3 | 成果物確認観点 | o | o | o | o | o | o | o | o |
| §4 | ゲート判定基準 | o | o | o | o | o | o | o | o |
| §5 | 知見集約手順 | o | o | o | - | o | o | o | o |
| §5.3 | refs ルーティング | o | o | - | - | - | - | - | - |
| §6 | 課題集約手順 | o | o | o | o | o | o | o | o |
| §7 | 差し戻し手順 | o | o | o | o | o | o | o | o |
| §8 | todo 登録 | o | o | o | o | o | o | o | o |
| §9 | 関連ファイル一覧 | - | - | - | - | - | - | - | - |
| §10 | ドメインエージェント参照 | o | - | - | - | - | - | - | - |

**凡例**: `o` = 明示的に参照、`-` = 参照なし
**略称**: meta = metacognition, bm = backlog-maintenance, auto = automation, co = config-optimizer

**備考**:
- §1（適用対象）と §9（関連ファイル一覧）は共通ポリシー自体のメタ情報であり、各マネージャーが直接参照するセクションではない
- L1-impl は `manager-common-policy` §1 の適用対象テーブルに未掲載だが、実際には §2〜§8 を参照している
- metacognition は §5（知見集約手順）を明示的に参照している（結果集約セクション内で `manager-common-policy §5 に従い` と記載）
- L1 のみが §10（ドメインエージェント参照）を利用する

---

## §4 関連ファイル一覧

| マネージャー | SKILL.md パス |
|-------------|--------------|
| L1 マネージャー | `.claude/skills/l1-manager/SKILL.md` |
| L1 実装マネージャー | `.claude/skills/l1-impl-manager/SKILL.md` |
| トリアージマネージャー | `.claude/skills/triage-manager/SKILL.md` |
| メタ認知マネージャー | `.claude/skills/metacognition-manager/SKILL.md` |
| 同期マネージャー | `.claude/skills/sync-manager/SKILL.md` |
| バックログメンテナンスマネージャー | `.claude/skills/backlog-maintenance-manager/SKILL.md` |
| 自動化マネージャー | `.claude/skills/automation-manager/SKILL.md` |
| config最適化マネージャー | `.claude/skills/config-optimizer-manager/SKILL.md` |
| **共通ポリシー** | `.claude/skills/manager-common-policy/SKILL.md` |

---

**作成日**: 2026-03-16
**関連施策**: `sessions/initiatives/manager-overview-doc/`
