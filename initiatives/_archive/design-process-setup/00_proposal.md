# 改善施策提案: ai-driven-dev-patterns の設計プロセス整備

## 背景・課題

ai-driven-dev-patterns リポジトリにおいて、以下の課題がある。

1. **設計プロセスの体系化不足**: dev_manager のシナリオ1（要件定義〜設計）が定義されているが、人間のエントリーポイントから具体的なセッション開始までの導線が不明確
2. **気づき・知見のルーティング未整備**: dev_manager の知見収集ステップ（report.md）にルーティング判断基準はあるが、inbox → backlog への流れが仕組みとして弱い。トリアージプロセスが未整備
3. **設計用ロール定義のブラッシュアップ余地**: openspec_specialist は整備済みだが、設計プロセス全体のフローとしての統合が不十分

## 目標

- 設計プロセスの全体像を描き、ステップ分解した backlog を ai-driven-dev-patterns 側に作成する
- 気づきルーティングの仕組みを ai-driven-dev-patterns に構築する（inbox → backlog、CSV への知見転記）
- 各ステップの優先順位を付け、順番に着手できる状態にする

## スコープ

### やること
- ai-driven-dev-patterns の現状調査（ロール・セッション・ドキュメント構造）
- 設計プロセスの全体像マップ作成（docs/ に配置）
- 気づきルーティングの仕組み設計・実装（inbox/backlog の README 更新、CLAUDE.md への反映）
- 全体像をステップ分解し、ai-driven-dev-patterns の backlog に個別施策として起票

### やらないこと
- 個別ステップの実施（backlog 起票後に別施策として着手）
- ロール定義の大幅な書き換え（調査結果を元に backlog 化する）
- dev-process-improvement 側の仕組み変更

## 期待される効果

- 設計プロセスが体系化され、散在する資材が統一される
- 人間がどこから始めてどう進めるかが明確になる
- 気づき→知見のフィードバックループが確立される

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| ai-driven-dev-patterns の構造理解不足 | 中 | 現状調査を丁寧に行い、既存の roles/ と docs/ を精読する |
| スコープ拡大 | 中 | 本施策は「全体像＋ルーティング仕組み＋backlog 起票」に限定 |

## 壁打ちの背景

- 作業対象は `/home/nr202/projects/ai-driven-dev-patterns`（別リポジトリ）。ブランチ `initiative/design-process-setup` で作業する
- 本施策のスコープは「全体像の計画策定＋ステップ分解まで」。個別ステップの実施は別施策として切り出す
- 気づきルーティングは dev-process-improvement のパターン（inbox → triage → backlog / CSV）に倣う。AI は課題管理 CSV へルーティング、inbox は人間のアイデア保管場所
- 前ブランチ `initiative/triage-process-brushup` の未プッシュコミットを push し、PR #84 を作成してから main に戻り新ブランチを作成した

---
**起票者**: L1
**起票日**: 2026-03-07
**ステータス**: 実施中
