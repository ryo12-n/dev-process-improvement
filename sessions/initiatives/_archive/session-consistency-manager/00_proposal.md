# 改善施策提案: session-consistency-manager

## 背景・課題
現在8つのマネージャーセッション（l1, l1-impl, triage, metacognition, sync, backlog-maintenance, automation, config-optimizer）が存在し、それぞれ SKILL.md・エージェント定義・セッションテンプレートを持つ。しかし、これらの間の整合性を横断的・体系的にチェックする専門セッションがない。

TG-008（トリアージ走査チェックリスト）が部分的にこの役割を担うが、トリアージの1タスクに過ぎず、深い分析やベストプラクティスとの比較は行えていない。セッション定義の増加に伴い、構造準拠・ペアリング対称性・テンプレート整合など、横断的な不整合が蓄積するリスクがある。

## 目標
- session-consistency-manager セッションタイプの完全な定義（SKILL.md + 4エージェント + テンプレート）を作成する
- 連動ファイル（commit-message.md, manager-common-policy, session-flow-policy, triage-standard-policy, docs/workflow.md）を更新する
- session-flow-policy §5.1 のチェックリストを通過する自己整合的なセッション定義を達成する

## スコープ
### やること
- session-consistency-manager の SKILL.md 作成
- 4つのエージェント定義（sc-collection-worker, sc-analysis-worker, sc-proposal-worker, sc-evaluator）作成
- リファレンススナップショットの初期テンプレート作成
- sessions/session-consistency/_template/ 配下のテンプレート15ファイル作成
- 連動ファイル5件の更新

### やらないこと
- 実際の整合性チェックの実行（新セッションの初回実行時に行う）
- 既存マネージャーセッションの修正
- TG-008 の変更（完全独立の方針）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果
- マネージャーセッション定義の整合性を定期的にチェックする仕組みが確立される
- session-flow-policy、manager-common-policy の準拠状況を体系的に可視化できるようになる
- 不整合の早期検出と改善提案により、セッション定義の品質維持が継続的に行える

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| TG-008 との責務重複による混乱 | 低 | 完全独立の方針を SKILL.md に明記し、棲み分けを明確にする |
| セッション定義ファイルの肥大化 | 中 | config-optimizer の構造を踏襲し、既存パターンとの一貫性を保つ |

## 壁打ちの背景
- セッション名は `skills-integrity-manager`、`session-consistency-manager`、`skills-audit-manager` の3候補から `session-consistency-manager` を選択。理由: スキルだけでなくセッション全体（テンプレート・ポリシー準拠含む）のチェックが対象であるため
- TG-008 との関係は「補完関係」「置き換え」「完全独立」の3択から「完全独立」を選択。理由: TG-008 は軽量チェックとして維持しつつ、本セッションは独自の基準で深い分析を行う

## 備考・設計パターン
config-optimizer-manager の3フェーズ構造（情報収集 → 現状分析 → 改善提案）を踏襲する。SC-001〜SC-008 の8つのチェックターゲットを定義し、各フェーズで体系的にチェックする。

---
**起票者**: L1
**起票日**: 2026-03-16
**ステータス**: 起票
**backlog元ファイル**: なし
