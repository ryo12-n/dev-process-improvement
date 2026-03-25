# knowledge.md 不在時のエラーハンドリング追加

## 概要
project-progress-sync スキルのエラーハンドリングテーブルに `knowledge.md` が存在しない場合の処理を追加する。

## 背景
project-progress-sync-skill 施策の評価レポートで指摘。`project-init` で作成されるため実害は低いが、防御的に追加すると堅牢性が向上する。

## 発見元
sessions/initiatives/_archive/project-progress-sync-skill/phase-2-execution/set-1/06_eval_report.md

---
**起票日**: 2026-03-24
