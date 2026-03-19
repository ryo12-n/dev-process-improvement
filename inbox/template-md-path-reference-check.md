# テンプレート .md ファイル内のパス参照を走査対象に含める

## 気づき

`sessions/*/_template/*.md` 内にもパス参照が含まれるため、パス変更施策では SKILL.md・エージェント定義だけでなくテンプレートファイルも走査対象に含めるべき。

## 提案

`rule-change-checklist` の項目4（パス変更の走査対象網羅性）に `sessions/*/_template/*.md` を明示的にリストする。

## 発見元

- 施策: phase-worker-set-standardization（T-010 横断検証）
- 日付: 2026-03-19
