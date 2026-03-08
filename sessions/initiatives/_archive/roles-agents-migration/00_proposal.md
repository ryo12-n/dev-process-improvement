# 改善施策提案: roles/ → .claude/agents/ 移行

## 背景・課題

ai-driven-dev-patterns リポジトリでは、ロール定義が `roles/` ディレクトリに独自形式の Markdown ファイルとして配置されている（9ファイル + `_base/common.md`）。Claude Code は `.claude/agents/` でカスタムサブエージェントをネイティブにサポートしており、以下のメリットが得られる。

- **独立コンテキスト**: agents のサブエージェントはメインセッションとは別のコンテキストウィンドウで動作
- **ツール制限**: `tools:` フィールドで使用可能ツールを制限可能（例: reviewer には Read/Grep/Glob のみ）
- **スキルプリロード**: `skills:` フィールドで必要なスキルだけ渡せる
- **Claude Code ネイティブ統合**: Agent ツールの subagent_type で直接指定可能

## 目標

`roles/` を廃止し、Claude Code ネイティブの `.claude/agents/` + `.claude/skills/` + `.claude/rules/` 構成に移行する。

## スコープ

### やること

- 8つの専門ロール（feature_builder, test_writer, reviewer, bug_fixer, refactorer, optimizer, documentarian, openspec_specialist）を `.claude/agents/*.md` に変換
- `dev_manager` を `.claude/skills/dispatcher/` に統合（マネージャー＝スキル構成）
- `_base/common.md` の共通ルールを `.claude/rules/` に分離（全 agent に自動適用）
- `roles/` を参照している約40ファイル（歴史的記録の docs/design/ を除く）のパス更新
- `roles/` ディレクトリの削除

### やらないこと

- ロール定義の内容・ロジックの変更（フォーマット変換のみ）
- docs/design/ 配下の歴史的設計書のパス更新（設計時点の記録として保持）
- 新ロールの追加
- ai-driven-dev-patterns 以外のリポジトリへの変更

## 期待される効果

- ロールのスコープ制御が `tools:` フィールドで仕組みレベルに強化
- サブエージェントの独立コンテキストにより、メインセッションの精度向上
- Claude Code 標準機能に準拠した一貫性のある構成
- dev-process-improvement と ai-driven-dev-patterns のセッション構造が統一（マネージャー＝スキル、ワーカー＝エージェント）

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| 参照更新漏れによるリンク切れ | 中 | grep で `roles/` 参照を網羅的に検出し、移行後に再チェック |
| agents 形式変換時の情報欠落 | 中 | 変換前後で diff を取り、内容の同等性を確認 |
| dev_manager のオーケストレーションロジック破壊 | 高 | 既存の dispatcher スキルとの整合を慎重に確認 |
| common.md 分離時のルール適用漏れ | 中 | `.claude/rules/` に配置すれば全 agent に自動適用される仕様を活用 |

## 壁打ちの背景

### 不明点1: `_base/common.md` の扱い

3案を検討し、**案B（`.claude/rules/` に配置）** を選択。
- 案A（各 agent にインライン展開）: 重複が多くメンテナンスコスト高
- 案B（`.claude/rules/` に配置）: Claude Code が全 agent に自動適用するため、common.md の役割と合致
- 案C（agents 配下に _base を維持）: agents の標準仕様外

### 不明点2: `dev_manager` の位置づけ

dev-process-improvement の構成（マネージャー＝スキル、ワーカー＝エージェント）に揃え、**`.claude/skills/dispatcher/` に統合** する方針。dev_manager はコードを書かずタスク分配・判断を行うオーケストレーターであり、スキルとしての位置づけが適切。

### 不明点3: 施策の実行リポジトリ

施策管理は dev-process-improvement、変更対象は ai-driven-dev-patterns。L2 ワーカーへの指示で作業対象リポジトリを明示する。

### 不明点4: 一括 vs 段階的移行

参照箇所を分析した結果（136箇所 / 51ファイル）、大半が機械的パス置換であり、中間状態での混在リスクの方が高いため、**一括移行** を選択。

---
**起票者**: L1
**起票日**: 2026-03-08
**ステータス**: 承認済
