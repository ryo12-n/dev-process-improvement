# 実施計画: session-artifacts-structure-refactor

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | config-optimizer テンプレート再構成 + SKILL.md/エージェント参照更新 | phase ディレクトリが存在し、SKILL.md 内に旧ファイル名参照が残っていない |
| 2 | impl テンプレート再構成 + SKILL.md/エージェント参照更新 | 26ファイルが4 phase ディレクトリに移動済み、旧ファイルが削除済み、全参照が更新済み |
| 3 | docs/workflow.md 連動更新 + 検証 | 可視化文書が新構造を反映、旧ファイル名の grep 結果が 0 件 |

## 成功基準（全体）

1. config-optimizer テンプレートに `phase-1-collection/`, `phase-2-analysis/`, `phase-3-proposal/` が存在し、各 `01_gate.md` がある
2. impl テンプレートの Phase ファイル（旧 `10_`〜`45_`）が全て phase ディレクトリに移動済み
3. `.claude/skills/` 配下の全 SKILL.md + エージェント定義で旧ファイル名参照が 0 件
4. `docs/workflow.md` が新構造を反映済み
5. triage, metacognition, BM, automation, sync のテンプレートが未変更

## リソース・前提条件

- 対象リポジトリ: dev-process-improvement（本リポジトリ内で完結）
- テンプレートのみ変更。既存セッションインスタンスは変更しない

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| SKILL.md/エージェント内の参照更新漏れ | 中 | 高 | 旧ファイル名を grep で網羅的にチェック |
| impl テンプレートの移動でファイル内容の欠損 | 低 | 高 | 移動前後の diff で内容変更がないことを確認 |

---
**作成者**: L1
**作成日**: 2026-03-16
**最終更新**: 2026-03-16
