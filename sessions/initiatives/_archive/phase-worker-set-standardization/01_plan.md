# 実施計画: Phase/ワーカーセット構成の標準パターン化

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | テンプレートのディレクトリ移動（session-consistency + config-optimizer） | 両テンプレートが `phase-N-xxx/_template/` 構成に統一されている |
| 2 | SKILL.md + エージェント定義のパス参照更新 | 全パス参照が新標準パターンに一致 |
| 3 | ポリシーファイル更新（session-flow-policy §4.3 追加、session-lifecycle-policy §1.3 修正） | 標準パターンが文書化され、欠落列が追加されている |
| 4 | docs/workflow.md 更新 | 2フロー図のパスが新標準に一致 |
| 5 | 横断検証（メタルール・rule-change-checklist） | 旧パスの残存なし、連動更新完了 |

## 標準パターン定義

### ディレクトリ構成

```
sessions/<session-type>/_template/
├── 00_pre_investigation.md    ← セッションルートファイル群
├── 01_plan.md
├── 02_dispatch_log.md
├── 03_report.md
├── 04_gate_review.md
├── phase-1-<name>/
│   ├── 01_gate.md
│   └── _template/             ← Phase 直下に _template/（workers/ 不要）
│       ├── 01_tasks.md
│       ├── 02_scan_plan.md
│       ├── 03_work_log.md
│       ├── 04_scan_report.md
│       ├── 05_eval_plan.md
│       ├── 06_eval_report.md
│       └── 07_issues.md
├── phase-2-<name>/
│   ├── 01_gate.md
│   └── _template/             ← 同構成
└── phase-3-<name>/
    ├── 01_gate.md
    └── _template/             ← 同構成
```

### ランタイムパス

Phase 開始時に `_template/` を `set-1/` にコピーして使用:
- `phase-1-<name>/set-1/01_tasks.md`
- `phase-2-<name>/set-1/01_tasks.md`
- `phase-3-<name>/set-1/01_tasks.md`

### 変更前後の対比

| マネージャー | 変更前 | 変更後 |
|------------|--------|--------|
| session-consistency | `phase-N-xxx/workers/set-1/` | `phase-N-xxx/set-1/` |
| config-optimizer | `workers/set-N/` | `phase-N-xxx/set-1/` |

## 変更対象ファイル一覧

### テンプレート（ディレクトリ操作）

| 対象 | 操作 |
|------|------|
| `sessions/session-consistency/_template/phase-1-collection/workers/_template/` | `phase-1-collection/_template/` に移動、workers/ 削除 |
| `sessions/session-consistency/_template/phase-2-analysis/workers/_template/` | `phase-2-analysis/_template/` に移動、workers/ 削除 |
| `sessions/session-consistency/_template/phase-3-proposal/workers/_template/` | `phase-3-proposal/_template/` に移動、workers/ 削除 |
| `sessions/config-optimization/_template/workers/_template/` | 各 `phase-N-xxx/_template/` にコピー後、ルート workers/ 削除 |

### SKILL.md + エージェント定義（パス置換）

| ファイル | 変更内容 |
|---------|---------|
| `.claude/skills/session-consistency-manager/SKILL.md` | `workers/set-1/` → `set-1/` |
| `.claude/skills/session-consistency-manager/agents/sc-collection-worker.md` | 同上 |
| `.claude/skills/session-consistency-manager/agents/sc-analysis-worker.md` | 同上 |
| `.claude/skills/session-consistency-manager/agents/sc-proposal-worker.md` | 同上 |
| `.claude/skills/session-consistency-manager/agents/sc-evaluator.md` | 同上 |
| `.claude/skills/config-optimizer-manager/SKILL.md` | `workers/set-N/` → `phase-N-xxx/set-1/` |
| `.claude/skills/config-optimizer-manager/agents/config-collection-worker.md` | `workers/set-1/` → `phase-1-collection/set-1/` |
| `.claude/skills/config-optimizer-manager/agents/config-analysis-worker.md` | `workers/set-2/` → `phase-2-analysis/set-1/` |
| `.claude/skills/config-optimizer-manager/agents/config-proposal-worker.md` | `workers/set-3/` → `phase-3-proposal/set-1/` |
| `.claude/skills/config-optimizer-manager/agents/config-optimizer-evaluator.md` | 全Phase のパスを新形式に |

### ポリシーファイル

| ファイル | 変更内容 |
|---------|---------|
| `.claude/skills/session-flow-policy/SKILL.md` | §4.3「3フェーズセッションの標準ディレクトリ構成」を追加 |
| `.claude/skills/session-lifecycle-policy/SKILL.md` | §1.3 に「config最適化系」列を追加 |

### 可視化文書

| ファイル | 変更内容 |
|---------|---------|
| `docs/workflow.md` L634-695 | config最適化フロー: パス更新 |
| `docs/workflow.md` L698-761 | セッション一貫性フロー: パス更新 |

## 成功基準（全体）
1. `grep -r "workers/set-\|workers/_template" sessions/` で旧パスの残存がないこと
2. 両テンプレートの全 `phase-N-xxx/_template/` に7ファイル（01_tasks〜07_issues）が存在すること
3. SKILL.md / エージェント定義のパスが新標準パターンと一致すること
4. `session-flow-policy` §4.3 に標準パターンが文書化されていること
5. `session-lifecycle-policy` §1.3 に config最適化系列が追加されていること
6. `docs/workflow.md` の2フロー図が新パスを使用していること

## リソース・前提条件
- 対象リポジトリ: dev-process-improvement（リポジトリ内完結）
- 外部リポジトリへの変更なし

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| パス参照の更新漏れ | 中 | 中 | grep による残存チェックを検証手順に含める |
| SKILL.md 内のロジック不整合 | 低 | 中 | エージェント定義とSKILL.mdのパスが相互に一致していることを確認 |

---
**作成者**: L1
**作成日**: 2026-03-19
**最終更新**: 2026-03-19
