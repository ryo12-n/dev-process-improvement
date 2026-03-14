# 改善施策提案: refs-knowledge-accumulation

## 背景・課題

外部リポジトリでの実装作業で得られた知見（アーキテクチャ、API パターン、制約等）が施策クローズとともに散逸している。現在の知見ルーティングは CSV / backlog / inbox / なし の4経路のみで、「特定の外部リポジトリに固有の知見」を蓄積する場所がない。同じ外部リポジトリを対象とした次の施策で、前回の知見を参照できず、調査の重複が発生する。

## 目標

- `refs/<リポジトリ名>/knowledge.md` に外部リポジトリ固有の知見を追記形式で蓄積できるようにする
- 知見ルーティングに `refs` を第5の経路として追加し、l1-impl-manager と l1-manager の両方で利用可能にする
- impl-manager の Phase 1 Investigation 後にリポジトリ概要を自動抽出する仕組みを導入する

## スコープ
### やること
- `refs/_knowledge_template.md` の新規作成
- `manager-common-policy` §5.2 に `refs` ルーティング先を追加、§5.3 を新設
- `l1-impl-manager` に Phase 1 後の概要自動抽出ステップとクローズ手順の `refs` 追加
- `l1-manager` のクローズ手順に `refs` ルーティングを追加
- ゲートテンプレート（`08_gate_summary.md`, `08_gate_review.md`）のルーティング先選択肢に `refs` 追加
- `CLAUDE.md` の `refs/` ディレクトリ説明を更新
- `docs/workflow.md` のルーティング先一覧を更新

### やらないこと
- 既存の `refs/` 配下ディレクトリ（`ai-driven-development-poc/`, `ai-functions/` 等）への knowledge.md 遡及作成
- Worker/Evaluator エージェント定義の変更（知見の分類は既存の「ルール化候補」「参考情報」の2分類を維持し、ルーティング判断はマネージャーが行う）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- 同じ外部リポジトリを対象とした複数施策間で知見が引き継がれ、調査の重複が削減される
- リポジトリ概要が Phase 1 で自動蓄積されるため、次回の Investigation フェーズが効率化される

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| ルーティング先が5つに増えることで判断基準が複雑化 | 低 | §5.2 テーブルの順序で明確に分離（外部リポジトリ固有 → CSV 汎用）|

## 壁打ちの背景

- スコープ: l1-impl-manager だけでなく l1-manager にも適用する（外部リポジトリ変更を含む施策は両方で発生する）
- リポジトリ概要: impl-manager の Phase 1 Investigation 成果物（`12_investigation_work_report.md`）から自動抽出する
- 知見の粒度: 1ファイルに追記していく形式（`knowledge.md`）。施策ごとにセクションを追加し、最新が上
- ブランチ: `initiative/impl-manager-external-repo-knowledge` → 指定ブランチ `claude/l1-manager-HCapk` で作業

---
**起票者**: L1
**起票日**: 2026-03-14
**ステータス**: 実施中
**backlog元ファイル**: なし
