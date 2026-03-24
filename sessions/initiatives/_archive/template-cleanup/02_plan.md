# 実施計画: template-cleanup

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | テンプレート構造変更 + スキル・ルール更新 | `_template` から不要ファイル削除済み、関連スキル・ルール更新済み |
| 2 | 評価 | 整合性確認、新施策開始シミュレーション |

## 変更対象ファイル一覧

### A. テンプレート本体の変更
- `sessions/initiatives/_template/phase-1-planning/01_gate.md` — **削除**
- `sessions/initiatives/_template/phase-2-execution/01_gate.md` — **削除**

### B. スキル・ルールの更新（_template/ 削除ステップ追加・01_gate.md 参照除去）
- `.claude/skills/l1-manager/SKILL.md` — set コピー手順に `_template/` 削除ステップを追加、01_gate.md への言及があれば除去
- `.claude/rules/parallel-dev.md` — set コピー方式の手順に `_template/` 削除を明記
- `.claude/skills/session-lifecycle-policy/SKILL.md` — initiative テンプレート構成から `01_gate.md` を除去
- `.claude/skills/session-flow-policy/SKILL.md` — initiative 向けの構造例から `01_gate.md` を除去（他セッションタイプの記述は変更しない）

### C. 可視化文書の連動更新
- `docs/workflow.md` — 該当セクションがあれば更新

### D. 整合性リファレンスの更新
- `.claude/skills/session-consistency-manager/reference/session-consistency-reference.md` — initiative テンプレート構成を更新

## 成功基準（全体）
1. `sessions/initiatives/_template/` から `phase-*/01_gate.md` が削除されている
2. L1 マネージャーの set コピー手順に `_template/` 削除ステップが含まれている
3. 関連スキル・ルール・可視化文書が整合している
4. 他セッションタイプ（triage, metacognition 等）のテンプレートに影響がない

## リソース・前提条件
- initiatives テンプレートのみが対象。他セッションタイプは変更しない
- 既存アーカイブの遡及修正は行わない

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 他セッションタイプへの波及 | 低 | 中 | initiatives 固有の変更に限定。session-flow-policy の共通構造定義は変更しない |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
