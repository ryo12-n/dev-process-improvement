# タスクリスト: テンプレート構成仕様の統一

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-004 | - |
| L2-evaluator | T-E01 | - |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-004, T-E01 | Wave 1 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | - |

> **方式**: 逐次（1ワーカーずつ）

## 施策フェーズ1 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | テンプレートディレクトリのリネーム | 4セッションの `workers/_template/` → `phase-1-<name>/_template/` 完了 | 🔴 | ⬜ |
| T-002 | マネージャー SKILL.md のパス参照更新 | triage-manager, metacognition-manager, backlog-maintenance-manager, automation-manager の `workers/` 参照を `phase-1-<name>/` に置換 | 🔴 | ⬜ |
| T-003 | エージェント定義のパス参照更新 | 8ファイル（worker×4 + evaluator×4）の `workers/` 参照を `phase-1-<name>/` に置換 | 🔴 | ⬜ |
| T-004 | ポリシー・参照ファイルの更新 | session-lifecycle-policy §1.4.4、session-flow-policy、session-consistency-reference、sc-collection-worker、repo-sync-checklist の `workers/` 参照を更新 | 🔴 | ⬜ |

### T-001 詳細: テンプレートディレクトリのリネーム

| セッションタイプ | 変更前 | 変更後 |
|----------------|--------|--------|
| triage | `sessions/triage/_template/workers/_template/` | `sessions/triage/_template/phase-1-scan/_template/` |
| metacognition | `sessions/metacognition/_template/workers/_template/` | `sessions/metacognition/_template/phase-1-analysis/_template/` |
| backlog-maintenance | `sessions/backlog-maintenance/_template/workers/_template/` | `sessions/backlog-maintenance/_template/phase-1-scan/_template/` |
| automation | `sessions/automation/_template/workers/_template/` | `sessions/automation/_template/phase-1-scan/_template/` |

### T-002 詳細: マネージャー SKILL.md 更新対象

| ファイル | 置換パターン |
|---------|------------|
| `.claude/skills/triage-manager/SKILL.md` | `workers/` → `phase-1-scan/` |
| `.claude/skills/metacognition-manager/SKILL.md` | `workers/` → `phase-1-analysis/` |
| `.claude/skills/backlog-maintenance-manager/SKILL.md` | `workers/` → `phase-1-scan/` |
| `.claude/skills/automation-manager/SKILL.md` | `workers/` → `phase-1-scan/` |

### T-003 詳細: エージェント定義更新対象

| ファイル | 置換パターン |
|---------|------------|
| `.claude/skills/triage-manager/agents/triage-worker.md` | `workers/` → `phase-1-scan/` |
| `.claude/skills/triage-manager/agents/triage-evaluator.md` | `workers/` → `phase-1-scan/` |
| `.claude/skills/metacognition-manager/agents/metacognition-worker.md` | `workers/` → `phase-1-analysis/` |
| `.claude/skills/metacognition-manager/agents/metacognition-evaluator.md` | `workers/` → `phase-1-analysis/` |
| `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md` | `workers/` → `phase-1-scan/` |
| `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-evaluator.md` | `workers/` → `phase-1-scan/` |
| `.claude/skills/automation-manager/agents/automation-worker.md` | `workers/` → `phase-1-scan/` |
| `.claude/skills/automation-manager/agents/automation-evaluator.md` | `workers/` → `phase-1-scan/` |

### T-004 詳細: ポリシー・参照ファイル更新対象

| ファイル | 更新内容 |
|---------|---------|
| `.claude/skills/session-lifecycle-policy/SKILL.md` | §1.4.4 の構成仕様をモダンパターンに更新 |
| `.claude/skills/session-flow-policy/SKILL.md` | レガシーパターンの記述を削除/更新 |
| `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` | `workers/_template/` 参照を更新 |
| `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md` | `workers/` 参照を更新 |
| `.claude/skills/repo-sync-checklist/SKILL.md` | `workers/` 参照を更新 |

## 施策フェーズ2 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | 整合性検証 | `.claude/skills/` 配下で `workers/` 残存ゼロ（grep 検証）。全パス参照が正当 | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-20
