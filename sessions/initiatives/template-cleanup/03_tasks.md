# タスクリスト: template-cleanup

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 標準的なファイル削除・テキスト編集のみ | Worker |
| なし | - | 整合性確認は 02_plan.md の成功基準に基づく照合のみ | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker set-1 | T-001 | テンプレートファイル削除 |
| L2-worker set-2 | T-002 | スキル・ルール更新 |
| L2-worker set-3 | T-003 | 可視化・リファレンス更新 |
| L2-evaluator | T-E01 | 全タスクの整合性評価 |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | - | T-001 | Wave 1 |
| Set-2 | L2-worker | - | T-002 | Wave 1 |
| Set-3 | L2-worker | - | T-003 | Wave 1 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1, Set-2, Set-3 | 並列 | なし | Wave 1: 全タスク独立・ファイル競合なし |

> **方式**: 並列（Wave 方式、`.claude/rules/parallel-dev.md` 参照）

## 施策フェーズ1 タスク（計画）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-P01 | L2-plan-worker: タスク分割・08_task_division.md 作成 | 08_task_division.md 作成済み | 🔴 | ✅ |

## 施策フェーズ1 タスク（実行）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | initiatives テンプレートから 01_gate.md を削除 | `_template/phase-*/01_gate.md` が削除済み。他セッションタイプは未変更 | 🔴 | ✅ |
| T-002 | スキル・ルール更新（_template/ 削除ステップ追加 + 01_gate.md 参照除去） | l1-manager, parallel-dev, session-lifecycle-policy が更新済み。session-flow-policy は変更なし | 🔴 | ✅ |
| T-003 | 可視化文書・整合性リファレンスの連動更新 | docs/workflow.md, session-consistency-reference.md が更新済み | 🟡 | ✅ |

## 施策フェーズ2 タスク（評価）
<!-- 施策フェーズ1 の全ワーカー完了後に評価ワーカーをディスパッチ -->

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | 全タスクの整合性評価 | 02_plan.md の成功基準4項目すべて充足を確認 | 🔴 | ✅ |

## 注意事項
- `session-flow-policy/SKILL.md` は `02_plan.md` に変更対象として挙がっていたが、L2-plan-worker の調査で initiatives 固有の `01_gate.md` 記述は存在せず変更不要と判断。L1 として妥当と承認
- `session-lifecycle-policy/SKILL.md` の基本モデル（§1.4 冒頭）の `01_gate.md` は 3-phase 共通なので残す。§1.4.3 initiatives 固有ツリーのみ除去

---
**作成者**: L1
**最終更新**: 2026-03-24
