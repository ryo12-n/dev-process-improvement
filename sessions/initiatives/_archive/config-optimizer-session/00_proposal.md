# 改善施策提案: config-optimizer-session

## 背景・課題

`.claude/` 配下の設定ファイル（settings.json, rules, skills, hooks, CLAUDE.md）は施策を重ねるごとに増加しているが、公式ドキュメントのベストプラクティスとの整合性や、未活用の設定オプションの把握が体系的に行われていない。

- 既存の `plugin-reference` や `builtin-skills-reference` は特定領域の評価を行うが、設定全体を横断的に最適化する仕組みがない
- コンテキスト予算の肥大化リスク（20+ skills × ~2% = ~40%）が未検証
- hooks（SessionStart 以外のフックタイプ活用）、path-scoped rules、import(@) 構文など未活用の可能性がある機能が散在

## 目標

config最適化マネージャーセッション（3フェーズ構成）を新規作成し、設定の定期的な最適化サイクルを確立する。

## スコープ
### やること
- config-optimizer-manager SKILL.md の作成（3フェーズオーケストレーション）
- 4つのエージェント定義の作成（collection-worker, analysis-worker, proposal-worker, evaluator）
- セッションテンプレート作成（`sessions/config-optimization/_template/`）
- リファレンススナップショットの初期ファイル作成（`reference/claude-code-config-reference.md`）
- 既存ファイルの連動更新（commit-message.md, session-flow-policy, triage-standard-policy, manager-common-policy, workflow.md）

### やらないこと
- 実際の最適化実施（セッション定義の作成のみ）
- plugin-reference / builtin-skills-reference との統合
- リファレンススナップショットの実データ収集（初回セッション実行時に実施）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- 設定の最適化サイクルが仕組み化され、定期的な見直しが可能になる
- 公式ドキュメントとの差分を定量的に把握できる
- 未活用機能の発見と活用提案が体系的に行われる
- コンテキスト予算の管理が改善される

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| セッション定義が複雑すぎて運用負荷が高い | 中 | 3フェーズの逐次実行で段階的に進める構成にする |
| リファレンス収集の精度が Web 検索に依存する | 中 | collection-worker に WebSearch/WebFetch ツールを付与し、複数ソースを照合する |
| 既存スキル数がさらに増加しコンテキスト予算を圧迫する | 低 | description を簡潔にし、user-invocable: true でオンデマンド読み込みにする |

## 壁打ちの背景

- l1-impl-manager の多フェーズゲート管理パターンと、triage/metacognition の日付ベースセッションパターンを組み合わせる方針を決定
- 単一 evaluator パターン（impl-evaluator と同様）を採用し、フェーズパラメータで評価基準を切り替える設計とした
- リファレンススナップショットは SKILL.md 内ではなく `reference/` サブディレクトリに分離する方針とした（plugin-reference の 346 行問題を回避）
- 7つの最適化ターゲット（CO-001〜CO-007）をスコープとして定義した

## 備考・設計パターン

- **3フェーズ構成**: Phase 1（情報収集）→ Phase 2（現状分析）→ Phase 3（最適化提案）
- **日付ベースセッション**: `sessions/config-optimization/YYYYMMDD/` で実行ごとにトレンド追跡可能
- **参照パターン**: l1-impl-manager（多フェーズゲート）、metacognition-manager（日付ベース・集約レポート）、plugin-reference（スナップショット管理）

---
**起票者**: L1
**起票日**: 2026-03-14
**ステータス**: 完了
**backlog元ファイル**: なし
