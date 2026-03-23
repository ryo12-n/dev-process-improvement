# 改善施策提案: initiative-template-2phase-migration

## 背景・課題

template-structure-unification 施策でポリシー・スキル定義（session-lifecycle-policy、l1-manager SKILL.md、4エージェント定義、parallel-dev.md、workflow.md）は新テンプレート構造（2-phase + set コピー方式）に更新済みだが、実テンプレートファイル（`sessions/initiatives/_template/`）は旧構造（フラット16ファイル）のまま残存している。

現状の不整合:
- `session-lifecycle-policy` §1.4.3 に新構造が定義済みだが「移行中」注記付き
- L1 マネージャーが initiative を開始する際、旧テンプレートをコピーした後に手動で 2-phase 構造に変換する必要がある
- 旧番号体系（`00_proposal.md`、`08_gate_review.md`、`09_cost_record.md` 等）がテンプレートに残存

## 目標

1. `sessions/initiatives/_template/` を §1.4.3 定義の 2-phase 構造に完全移行する
2. ポリシーの「移行中」注記を解除し、ポリシーと実ファイルを一致させる
3. L1 マネージャーの initiative 開始手順が手動変換なしで動作する状態にする

## スコープ
### やること
- マネージャールートファイル 7 件の番号リネーム・内容更新
- `phase-1-planning/_template/` の作成（計画ワーカーセット 7 ファイル + `08_task_division.md`）
- `phase-2-execution/_template/` の作成（実施ワーカーセット 7 ファイル）
- `phase-*/01_gate.md` の新規作成
- 旧ファイル（`02a_task_division.md`, `02b_dispatch_log.md`, `03_work_log_W_template.md`, `07_issues_W_template.md` 等）の削除
- `session-lifecycle-policy` §1.4.3 の「移行中」注記解除
- `l1-manager/SKILL.md` のテンプレートコピー手順・関連ファイル一覧の整合確認

### やらないこと
- GHA ワークフローのファイル名更新（BL-119 で対応）
- テンプレート内容の改善（構造変更のみ、テキスト内容はそのまま移行）
- 既存の進行中・完了済み施策への遡及変更

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- L1 マネージャーの initiative 開始時の手動変換が不要になる
- ポリシー（§1.4.3）と実テンプレートの完全一致により、整合性チェックで false positive が発生しない
- 新規セッション参加者がテンプレート構造を直感的に理解できる

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| 旧テンプレートを参照するスキル・エージェント定義が壊れる | 中 | 前施策で参照は更新済み。念のため grep で残存参照を確認 |
| GHA ワークフローが旧ファイル名を参照して動作しなくなる | 低 | GHA は BL-119 で別施策対応。GHA スキルは独自命名体系 |

## 壁打ちの背景

- ブランチは前セッション（template-structure-unification）の `claude/l1-manager-cyWeq` を継続使用
- 前施策でポリシー側は完全更新済みのため、本施策は実ファイルの構造変更に集中する
- ファイル対応（旧→新番号体系）は壁打ちで合意済み

---
**起票者**: L1
**起票日**: 2026-03-20
**ステータス**: 起票
**backlog元ファイル**: initiative-template-2phase-migration.md
