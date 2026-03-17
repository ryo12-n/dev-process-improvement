---
name: session-flow-policy
description: '新セッションタイプの作成・.claude/skills/ 配下のスキル/エージェント構成の変更時に参照するポリシー'
user-invocable: false
---
# セッションフロー作成ポリシー

## 適用対象

新しいセッションタイプ（マネージャー＋ワーカー構成）を作成するすべての場面に適用する。

---

## 1. 基本構造: マネージャー＝スキル、ワーカー＝エージェント

新しいセッションフローは以下の構造で作成すること。

```
.claude/skills/<session-type>-manager/
├── SKILL.md              # マネージャーのルール定義（スキルとして実装）
└── agents/               # ワーカー・評価者のエージェント定義
    ├── <session-type>-worker.md
    └── <session-type>-evaluator.md
```

### 1.1 マネージャーをスキルにする理由

- **ユーザーが `/` コマンドで明示的に起動する**ため、`user-invocable: true` のスキルが適切
- スキルの `description` のみが常時読み込まれ、**全文はオンデマンド読み込み**でコンテキストコストが低い
- オーケストレーションロジック（ワーカーのディスパッチ・成果物確認・集約）をマネージャーに集約できる

### 1.2 ワーカー・評価者をエージェントにする理由

- **独立したコンテキストウィンドウ**で動作するため、メインセッションを汚染しない
- マネージャーが Agent ツール（`subagent_type` 指定）で起動・制御する
- ワーカー間のファイル分離が自然に担保される

---

## 2. SKILL.md の必須要素

マネージャースキルの SKILL.md には以下を含めること。

### 2.1 YAML フロントマター

```yaml
---
name: <session-type>-manager
description: '<1行の説明>'
user-invocable: true
---
```

### 2.2 必須セクション（ロール定義フォーマットガイド準拠）

`role-format-guide.md` に従い、以下のセクションを含めること。

1. **あなたの役割** — マネージャーの責務を1〜2文で説明
2. **作業フロー** — 番号付きステップ。ワーカーのディスパッチ手順を含む
3. **やること** — マネージャーの責任範囲
4. **やらないこと** — ワーカー・評価者の成果物を直接編集しない等

### 2.3 オーケストレーション関連の必須記載

- **ワーカーのディスパッチ手順**: 起動時に渡す観点（エージェント定義パス・スコープ・完了定義）
- **成果物の確認観点**: evaluator 起動前にワーカー成果物を確認する基準
- **結果の集約手順**: 全ワーカー完了後のレポート集約方法
- **担当ファイル**: テーブル形式でファイルと操作権限を明記

> **注**: 上記の共通パターン（ディスパッチ・成果物確認・ゲート判定・知見集約・課題集約・差し戻し）は `manager-common-policy`（`.claude/skills/manager-common-policy/SKILL.md`）に一元定義されている。新しいマネージャースキルを作成する際は、共通ポリシーを参照し、固有ロジックのみ自身の SKILL.md に記載すること。

---

## 3. エージェント定義の必須要素

ワーカー・評価者エージェント（`agents/*.md`）には以下を含めること。

### 3.1 必須セクション（ロール定義フォーマットガイド準拠）

1. **あなたの役割** — ワーカー/評価者の責務
2. **作業フロー** — 壁打ちフェーズから始まる番号付きステップ
3. **やること** — 担当する作業の明示
4. **やらないこと** — スコープ外の明示（マネージャーの責務に属する操作等）
5. **担当ファイル** — テーブル形式（ファイル | 操作）
6. **停止ルール** — 作業を中断すべき条件

### 3.2 実施者/評価者ペアリングの対称性

実施者と評価者のペアでは、以下の要素が両方に存在すること。

| 要素 | 実施者に必須 | 評価者に必須 |
|------|------------|------------|
| 壁打ちフェーズ | あり | あり |
| 作業/評価計画 | あり | あり |
| レポート | あり | あり |
| 知見記録セクション | あり | あり |
| 課題起票手段 | あり | あり |
| 停止ルール | あり | あり |

### 3.3 推奨プラクティス: 対称性確認テーブル

evaluator 定義に「対称性確認テーブル」を含めることを推奨する。これは、ペアリング要件（§3.2）の各要素が実施者と評価者の双方に存在するかをテーブル形式で自己検証するもので、ペアリング不整合の早期検出に有効である。

参考実装: `.claude/skills/sync-manager/agents/sync-evaluator.md` の対称性確認テーブル

### 3.4 命名規約

エージェント定義の YAML フロントマターの `name` フィールドはケバブケース（小文字英字とハイフン）のみ許容される。スネークケースやキャメルケースは使用不可。

```yaml
# 良い例
name: triage-worker
name: l2-evaluator

# 悪い例（エラーになる）
name: triage_worker
name: triageWorker
```

### 3.5 順序制約

- **実施者が完了してから評価者を起動する**（並列起動禁止）
- 評価者は実施者の成果物を直接編集しない（読み取りのみ）

---

## 4. ディスパッチパターン

### 4.1 基本は逐次

ワーカーセットは1つずつ（worker → evaluator → 次のset）を基本とする。

### 4.2 並列ディスパッチの条件

並列ディスパッチは `.claude/rules/parallel-dev.md` に従い、以下をすべて満たす場合のみマネージャー判断で許可する。

1. ワーカー間に入力→出力の依存関係がない
2. 書き込み先ファイルが完全に分離している
3. 並列化による効果がオーバーヘッドを上回る

---

## 5. 既存セッションタイプとの整合性

新しいセッションタイプを作成する際は、既存のセッションタイプとの整合性を確認すること。

| セッションタイプ | マネージャー（スキル） | ワーカー（エージェント） |
|----------------|---------------------|----------------------|
| L1/L2 施策フロー | `.claude/skills/l1-manager/` | `agents/l2-plan-worker.md`, `agents/l2-plan-evaluator.md`, `agents/l2-worker.md`, `agents/l2-evaluator.md` |
| 実装マネージャーフロー | `.claude/skills/l1-impl-manager/` | `agents/investigation-worker.md`, `agents/design-worker.md`, `agents/impl-plan-worker.md`, `agents/impl-worker.md`, `agents/impl-evaluator.md` |
| トリアージフロー | `.claude/skills/triage-manager/` | `agents/triage-worker.md`, `agents/triage-evaluator.md` |
| メタ認知フロー | `.claude/skills/metacognition-manager/` | `agents/metacognition-worker.md`, `agents/metacognition-evaluator.md` |
| リポジトリ間同期フロー | `.claude/skills/sync-manager/` | `agents/sync-worker.md`, `agents/sync-evaluator.md` |
| バックログメンテナンスフロー | `.claude/skills/backlog-maintenance-manager/` | `agents/backlog-maintenance-worker.md`, `agents/backlog-maintenance-evaluator.md` |
| オートメーションフロー | `.claude/skills/automation-manager/` | `agents/automation-worker.md`, `agents/automation-evaluator.md` |
| config最適化フロー | `.claude/skills/config-optimizer-manager/` | `agents/config-collection-worker.md`, `agents/config-analysis-worker.md`, `agents/config-proposal-worker.md`, `agents/config-optimizer-evaluator.md` |

### 5.1 新セッションタイプ追加時のチェックリスト

- [ ] SKILL.md に必須セクション（あなたの役割・作業フロー・やること・やらないこと）が含まれている
- [ ] agents/ にワーカーと評価者のペアが定義されている
- [ ] ペアリングの対称性要件を満たしている
- [ ] `docs/workflow.md` に新セッションタイプのフローを追記した
- [ ] コミットメッセージ規約（`commit-message.md`）に新セッションタイプを追加した（必要な場合）
- [ ] `.claude/skills/triage-standard-policy/SKILL.md` の適用マトリクスに新セッションタイプを追加した（必要な場合）

---

## 関連ファイル一覧

本スキルファイルの内容を変更した場合、以下のファイルの連動更新が必要になる可能性がある。

| ファイル | 連動更新の内容 |
|---------|-------------|
| `.claude/skills/manager-common-policy/SKILL.md` | オーケストレーション共通パターンの変更が新セッション作成ガイダンスに影響する場合 |
| `.claude/skills/l1-manager/SKILL.md` | SKILL.md の必須要素・オーケストレーション関連の必須記載の変更がマネージャー定義に影響する場合 |
| `.claude/skills/l1-manager/agents/l2-worker.md` | エージェント定義の必須要素・ペアリング対称性の変更がワーカー定義に影響する場合 |
| `.claude/skills/l1-manager/agents/l2-evaluator.md` | エージェント定義の必須要素・ペアリング対称性の変更が評価者定義に影響する場合 |
| `.claude/skills/triage-manager/SKILL.md` | SKILL.md の必須要素の変更がトリアージマネージャー定義に影響する場合 |
| `.claude/skills/triage-manager/agents/triage-worker.md` | エージェント定義の必須要素の変更がトリアージワーカー定義に影響する場合 |
| `.claude/skills/triage-manager/agents/triage-evaluator.md` | エージェント定義の必須要素の変更がトリアージ評価者定義に影響する場合 |
| `.claude/skills/metacognition-manager/SKILL.md` | SKILL.md の必須要素の変更がメタ認知マネージャー定義に影響する場合 |
| `.claude/skills/metacognition-manager/agents/metacognition-worker.md` | エージェント定義の必須要素の変更がメタ認知ワーカー定義に影響する場合 |
| `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md` | エージェント定義の必須要素の変更がメタ認知評価者定義に影響する場合 |
| `.claude/skills/sync-manager/SKILL.md` | SKILL.md の必須要素の変更が同期マネージャー定義に影響する場合 |
| `.claude/skills/sync-manager/agents/sync-worker.md` | エージェント定義の必須要素の変更が同期ワーカー定義に影響する場合 |
| `.claude/skills/sync-manager/agents/sync-evaluator.md` | エージェント定義の必須要素の変更が同期評価者定義に影響する場合 |
| `.claude/skills/backlog-maintenance-manager/SKILL.md` | SKILL.md の必須要素の変更がバックログメンテナンスマネージャー定義に影響する場合 |
| `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md` | エージェント定義の必須要素の変更がバックログメンテナンスワーカー定義に影響する場合 |
| `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md` | エージェント定義の必須要素の変更がバックログメンテナンス評価者定義に影響する場合 |
| `.claude/skills/triage-standard-policy/SKILL.md` | ペアリング要件・ライフサイクル定義の変更が標準ポリシーに影響する場合 |
| `docs/workflow.md` | セッションフロー構造の変更がワークフロー記述に影響する場合（人間向け可視化） |
| `.claude/rules/commit-message.md` | セッション種別の追加・変更がコミットメッセージ規約に影響する場合 |

---

**作成日**: 2026-03-06
**根拠**: l1-manager / triage-manager セッションフローの実装パターンを標準化
