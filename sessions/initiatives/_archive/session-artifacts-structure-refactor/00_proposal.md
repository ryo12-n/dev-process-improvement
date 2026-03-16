# 改善施策提案: session-artifacts-structure-refactor

## 背景・課題

非施策セッション（config-optimizer, impl）の成果物ファイルが、フラットなプレフィックス番号で Phase を表現しており可読性が低い。

1. **config-optimizer**: 親テンプレート `00`〜`04` に加え、ランタイムで `15_collection_gate.md`, `25_analysis_gate.md`, `35_proposal_gate.md` がセッション直下にフラットに作成される。10番台飛び番でPhaseの区切りが分かりづらい
2. **impl**: 31ファイルがフラットに `00`〜`45` のプレフィックスで並ぶ。Phase 1〜4 の区切りがファイル名プレフィックスのみで表現されており、一覧性が悪い
3. 一方、triage 等のセッションは `workers/set-N/` のディレクトリ階層で整理されており可読性が高い

## 目標

- config-optimizer と impl のテンプレートを **Phase 別ディレクトリ構造** に再構成する
- プレフィックスは各ディレクトリ内で連番を維持し、triage パターン（ディレクトリ階層 + 連番）に統一する

## スコープ
### やること
- config-optimizer テンプレートに `phase-1-collection/`, `phase-2-analysis/`, `phase-3-proposal/` ディレクトリを追加し、gate テンプレートを配置
- impl テンプレートの 26 Phase ファイル（`10_`〜`45_`）を `phase-1-investigation/`, `phase-2-design/`, `phase-3-impl-plan/`, `phase-4-impl/` ディレクトリに移動・リネーム
- 対応する SKILL.md + エージェント定義のファイルパス参照を全更新
- `docs/workflow.md` の連動更新

### やらないこと
- triage, metacognition, backlog-maintenance, automation, sync テンプレートの変更（既に良構造）
- initiatives テンプレート（l1-manager）の変更
- 既存セッションインスタンスのリネーム（テンプレートのみ対象）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- セッション成果物を `ls` した際に Phase 構造が一目で分かる
- impl テンプレートのファイル数がルート直下 7 ファイル + 4 Phase ディレクトリに整理される（現状 31 ファイルフラット）
- 新セッションタイプ追加時のテンプレート設計指針が明確になる

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| SKILL.md / エージェント定義の参照更新漏れ | 高 | 旧ファイル名の grep による網羅的チェック |
| 既存セッションインスタンスとの乖離 | 低 | 既存は変更しないため影響なし。新セッションから新構造を適用 |

## 壁打ちの背景

- 当初は「10番台/20番台」のdecade-based プレフィックスリネームを検討したが、ユーザーから「基本は連番、Phase分離はディレクトリ階層で」という方針転換があった
- triage の `workers/set-N/` 構造が目標のモデル
- triage, metacognition, BM, automation, sync は既にこのパターンに準拠しているため変更対象から除外
- config-optimizer と impl の2セッションタイプに絞り込み

---
**起票者**: L1
**起票日**: 2026-03-16
**ステータス**: 起票
**backlog元ファイル**: session-artifacts-structure-refactor.md
