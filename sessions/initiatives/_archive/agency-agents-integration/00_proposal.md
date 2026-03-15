# 改善施策提案: agency-agents-integration

## 背景・課題

現在の L1 マネージャーセッションでは、L2-worker/evaluator は汎用的なプロセス改善ワーカーとして動作する。施策の性質によってはドメイン専門知識（コードレビュー、セキュリティ監査、DevOps、テスト戦略等）が求められるが、現状はその知見源がない。

GitHub の agency-agents リポジトリ（msitarzewski/agency-agents、46K+ スター）は 144+ のドメイン専門エージェント定義を Markdown 形式で提供しており、Claude Code と親和性が高い。

## 目標

1. agency-agents リポジトリ全体を `refs/` に取り込み、参照可能な知見ライブラリとして整備する
2. エージェントカタログ（インデックス+施策タイプ別マッチング）を構築し、L1 マネージャーがディスパッチ計画時に適切なドメインエージェントを選定できるようにする
3. L2-worker への専門性注入の仕組みを manager-common-policy + l1-manager に実装する

## スコープ
### やること
- agency-agents リポジトリ全体を `refs/agency-agents/` に配置
- `refs/agency-agents/knowledge.md` にエージェントカタログ + 施策タイプ別推奨マッピングを構築
- `manager-common-policy` に §10「ドメインエージェント参照」を新設
- `l1-manager/SKILL.md` にエージェント選定手順を追加
- `l2-worker.md` の作業フローにエージェント参照手順を追加
- `_template/02_tasks.md` に「参照ドメインエージェント」セクションを追加
- `docs/workflow.md` を連動更新
- 後続施策 2 件（定期レビューセッション、他マネージャー展開）を backlog に起票

### やらないこと
- `.claude/agents/` への全エージェント配置（コンテキスト汚染リスク。有用なものの移動は後続施策）
- l1-manager 以外のマネージャーへの統合（後続施策として起票）
- agency-agents のエージェント定義の改変・カスタマイズ（参照のみ）
- 定期レビューセッションの作成（backlog 起票のみ）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- L2-worker が施策の性質に応じた専門的アプローチ・チェックリスト・品質基準を参照でき、作業品質が向上する
- L1 マネージャーがカタログから体系的にエージェントを選定でき、ディスパッチ計画の再現性が向上する
- 将来的に他マネージャーへの展開基盤となる

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| リポジトリ容量圧迫 | 中 | ファイルサイズ確認。大きすぎる場合は部門選択的取り込み |
| L2-worker がエージェントの「役割」を引き受けてしまう | 中 | l2-worker.md と §10.3 に「専門知識の参照のみ」制約を明記 |
| knowledge.md の陳腐化 | 低 | 有効期限メタ情報 + 定期レビュー施策で対応 |

## 壁打ちの背景

### 統合方式の選択

3つの選択肢を検討した:
- **(A) 既存エージェントにドメイン知識を注入**: l2-worker に「参照せよ」と指示する方式
- **(B) ディスパッチガイド方式**: A + manager-common-policy にマッチングガイドを追加
- **(C) 新しいエージェント層を追加**: 独立したドメイン専門家エージェントを起動

**決定: B 方式を採用（実際の使用は A の形）**
- 判断基準が明文化され再現性がある
- 既存の manager-worker-evaluator 構造を破壊しない
- `.claude/agents/` に 144+ ファイル配置はコンテキスト汚染リスクが高い

### 取り込み粒度

全エージェントを `refs/` に取り込む。理由:
- 選別コストが高く、将来的に必要になるエージェントを予測しにくい
- `refs/` は参照物置き場であり、全量保持しても問題ない
- knowledge.md のインデックスで必要なものだけを効率的に検索できる

### 適用範囲

まず l1-manager から適用し、3施策以上の実地検証後に他マネージャーへ展開する。

## 備考・設計パターン

agency-agents のエージェント定義フォーマット:
- YAML frontmatter（name, description, color, emoji, vibe）
- Markdown body: Identity, Communication Style, Critical Rules, Core Mission, Technical Deliverables, Workflow Process, Success Metrics, Advanced Capabilities
- 12部門: Engineering, Design, Marketing, Sales, Paid Media, Product, PM, Testing, Support, Spatial Computing, Game Development, Academic/Specialized

---
**起票者**: L1
**起票日**: 2026-03-15
**ステータス**: 実施中
**backlog元ファイル**: なし（壁打ちからの新規提案）
