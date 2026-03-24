# gen-* チェーン Skill のテンプレート管理方針ルール化

## 背景

ai-dev-chain-gen-design 施策で worker・evaluator 双方から同一の知見が報告された:
「テンプレートは SKILL.md の構造を反映したプレースホルダーとして管理すべき（SKILL.md が Source of Truth）」

現状この方針は暗黙知であり、チェーン Skill 追加時に毎回再発見される可能性がある。

## 提案

gen-* チェーン Skill 追加時の標準ルールとして以下を明文化する:
- テンプレート（`projects/_template/artifacts/`）は SKILL.md 生成ルールの subset を例示する位置づけ
- SKILL.md 側が Source of Truth
- テンプレートと SKILL.md の間に微小な差異が生じても、SKILL.md のルールが優先される

## 発見元

- `sessions/initiatives/ai-dev-chain-gen-design/phase-2-execution/set-1/03_worker_report.md` 知見 #1
- `sessions/initiatives/ai-dev-chain-gen-design/phase-2-execution/set-2/06_eval_report.md` ルール化候補 #1

---
**起票日**: 2026-03-24
**起票元施策**: ai-dev-chain-gen-design
