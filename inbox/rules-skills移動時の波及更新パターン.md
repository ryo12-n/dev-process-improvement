# rules/ → skills/ 移動時の参照パス波及更新

## 気づき

`.claude/rules/` から `.claude/skills/` へファイルを移動する際、移動ファイルを参照している他のスキルの参照パスも更新が必要になる。「関連ファイル一覧」セクションがないスキルでは grep 走査が唯一の発見手段であり、漏れのリスクがある。

## 提案

全スキル（SKILL.md）に「関連ファイル一覧」セクションを設けることをルール化する。これにより、ファイル移動・リネーム時の波及更新対象が明示的に把握できる。

## 出典

- `sessions/initiatives/claude-dir-optimization-adp/08_gate_review.md` 必須把握事項#1、次施策候補
- `sessions/initiatives/claude-dir-optimization-adp/04_work_report.md` 知見#1
