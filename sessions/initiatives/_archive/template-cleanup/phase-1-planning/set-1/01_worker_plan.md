# ワーカー計画: template-cleanup — Set-1

## 壁打ちフェーズ [2026-03-24 10:00]

### 理解のサマリー
- タスクの目的: 施策ディレクトリから不要テンプレートファイル（`phase-*/01_gate.md`）を構造的に排除し、`_template/` の set コピー後の削除ステップを追加する
- スコープ: initiatives テンプレート本体の変更、関連スキル・ルール・可視化文書の連動更新（他セッションタイプは対象外）
- 完了条件: `08_task_division.md` が作成され、`03_worker_report.md` に計画レポートが記載されている

### 前提条件チェック
- [x] 施策計画（02_plan.md）の内容を理解: 理解済み
- [x] 提案書（01_proposal.md）の確認: 確認済み
- [x] 変更対象ファイル群の特定: 特定済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：計画開始

---

## 分析計画サマリ

### 調査結果

変更対象ファイル群を `Glob`/`Grep`/`Read` で調査した結果、以下を特定した。

#### A. テンプレート本体（DELETE）
- `sessions/initiatives/_template/phase-1-planning/01_gate.md`
- `sessions/initiatives/_template/phase-2-execution/01_gate.md`

#### B. スキル・ルール（MODIFY）
1. `.claude/skills/l1-manager/SKILL.md` — set コピー手順に `_template/` 削除ステップを追加（L126 付近）。`01_gate.md` への直接言及は確認されなかった
2. `.claude/rules/parallel-dev.md` — §2.1 set コピー手順に `_template/` 削除を明記
3. `.claude/skills/session-lifecycle-policy/SKILL.md` — §1.4.3 Initiative テンプレート構成から `01_gate.md` を除去（L123, L193, L205 付近）
4. `.claude/skills/session-flow-policy/SKILL.md` — initiatives 固有ではなく 3-phase 標準構成で `01_gate.md` を記載。initiatives 固有の記述はないため、変更不要と判断

#### C. 可視化文書（MODIFY）
5. `docs/workflow.md` — initiative フローの並列ディスパッチ部分に `_template/` 削除ステップを追加（L58 付近）。`01_gate.md` の言及は 3-phase セッション（config-optimization, session-consistency）のみで、initiatives には該当なし

#### D. 整合性リファレンス（MODIFY）
6. `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` — initiatives テンプレート構成から `01_gate.md` を除去（L122 付近のファイル一覧）

### 分割方針
- T-001: テンプレート本体の削除（01_gate.md 2ファイル）
- T-002: スキル・ルールの更新（l1-manager、parallel-dev、session-lifecycle-policy）
- T-003: 可視化文書・整合性リファレンスの更新（workflow.md、session-consistency-reference.md）

T-001 と T-002/T-003 はファイル競合なし。T-002 と T-003 もファイル競合なし。全タスク並列実行可能。
