# タスクリスト: phase-worker-set-standardization

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | パス置換中心の定型作業のため | Worker |
| なし | - | パス整合性検証は汎用的なため | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-013 | 逐次ディスパッチ |
| L2-evaluator | 全タスクの成果物評価 | - |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-013 | Wave 1（逐次） |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | 全タスクを1ワーカーで逐次実行 |

> **方式**: 逐次（1ワーカーずつ）。Conflict 0件だが、タスク数が多く並列のオーバーヘッドが効果を上回るため逐次を選択。

## タスク一覧

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | session-consistency テンプレート: `phase-N-xxx/workers/_template/` を `phase-N-xxx/_template/` に `git mv` で移動（3Phase分）。空になった `workers/` ディレクトリを削除 | 各 `phase-N-xxx/_template/` に7ファイル存在、旧 `workers/_template/` が削除済み | 🔴 | ⬜ |
| T-002 | config-optimization テンプレート: `workers/_template/` の7ファイルを各 `phase-N-xxx/_template/` にコピー（3Phase分）。ルート `workers/` を `git rm -r` で削除 | 各 `phase-N-xxx/_template/` に7ファイル存在、旧 `workers/_template/` が削除済み | 🔴 | ⬜ |
| T-003 | session-consistency-manager SKILL.md のパス参照更新: `phase-N-xxx/workers/_template/` → `phase-N-xxx/_template/`、`phase-N-xxx/workers/set-1/` → `phase-N-xxx/set-1/` に一括置換 | `grep -c "workers/" SKILL.md` で一般用語を除くパス参照が0 | 🔴 | ⬜ |
| T-004 | config-optimizer-manager SKILL.md のパス参照更新: `workers/set-1/` → `phase-1-collection/set-1/`、`workers/set-2/` → `phase-2-analysis/set-1/`、`workers/set-3/` → `phase-3-proposal/set-1/`、`workers/set-N/` → `phase-N-xxx/set-1/` に変更。`_template/workers/` → Phase別 `_template/phase-N-xxx/_template/` に変更 | `grep -c "workers/set-\|workers/_template" SKILL.md` が0 | 🔴 | ⬜ |
| T-005 | session-consistency エージェント定義（4ファイル）のパス参照更新: `sc-collection-worker.md`、`sc-analysis-worker.md`、`sc-proposal-worker.md`、`sc-evaluator.md` の `workers/set-1/` → `set-1/` に置換（担当ファイルテーブル・フローステップ・クロスPhase参照を含む） | 4ファイルすべてで `grep -c "workers/set-1"` が0 | 🔴 | ⬜ |
| T-006 | config-optimizer エージェント定義（4ファイル）のパス参照更新: `config-collection-worker.md`（`workers/set-1/` → `phase-1-collection/set-1/`）、`config-analysis-worker.md`（`workers/set-2/` → `phase-2-analysis/set-1/`）、`config-proposal-worker.md`（`workers/set-3/` → `phase-3-proposal/set-1/`）、`config-optimizer-evaluator.md`（全Phase パスを新形式に） | 4ファイルすべてで `grep -c "workers/set-"` が0 | 🔴 | ⬜ |
| T-007 | session-flow-policy/SKILL.md に §4.3「3フェーズセッションの標準ディレクトリ構成」を追加。テンプレートパス `phase-N-xxx/_template/`、ランタイムパス `phase-N-xxx/set-1/` の標準パターンを定義 | §4.3 が存在し、`01_plan.md` の標準パターン定義と一致 | 🟡 | ⬜ |
| T-008 | session-lifecycle-policy/SKILL.md §1.3 テーブルに「config最適化系」列を追加（「セッション一貫性系」と同じ構成） | §1.3 に「config最適化系」列が存在 | 🟡 | ⬜ |
| T-009 | docs/workflow.md の2フロー図を更新。config最適化フロー（L634-695）: `workers/set-N/` → `phase-N-xxx/set-1/`。セッション一貫性フロー（L698-761）: `phase-N-xxx/workers/set-1/` → `phase-N-xxx/set-1/` | 2フロー図内で `grep -c "workers/"` が0 | 🟡 | ⬜ |
| T-010 | 横断検証: `grep -r "workers/set-\|workers/_template"` で旧パス残存なし確認。全 `phase-N-xxx/_template/` に7ファイル存在確認。session-flow-policy §4.3・session-lifecycle-policy §1.3 config最適化系の存在確認 | 全検証項目がPASS | 🔴 | ⬜ |
| T-011 | （固定タスク）メタルール横断検証 + rule-change-checklist: `.claude/skills/`, `.claude/rules/` の変更に対し3領域検証（メタルールフロー記述・workflow.md 同期・TG-008 基準連動）を実施し `04_work_report.md` に記録。`rule-change-checklist` スキルの全7項目を確認し `03_work_log.md` に記録。適用対象環境: CLI / SDK 横断 | 3領域検証結果 + チェックリスト全7項目の結果が記録されている | 🔴 | ⬜ |
| T-012 | （固定タスク）知見記録: 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録。「ルール化候補」と「参考情報」に分類 | 両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-013 | （固定タスク）課題転記: `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` として作成。`issues/_template.md` をコピーして作成 | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-19
