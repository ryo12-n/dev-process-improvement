# GHAスキル「やらないこと」の用途クラス別テンプレート化

## 背景

gha-session-prompt-conversion-pattern 施策の評価で、GHAスキルの「やらないこと」セクションが用途クラスごとに類型化できることが判明した。

- **書き込み系スキル**（wallbash/execute/close）: 共通4項目（PR作成禁止、gh禁止、破壊的git禁止、force push禁止）
- **読み取り専用スキル**（question）: git/gh 禁止 + Write/Edit 禁止の3項目
- **検証用スキル**（test）: 独自構成

## 提案

gha-guideline/SKILL.md セクション7.2のテンプレートを用途クラス別に拡張し、新規スキル作成時の判断を効率化する。

## 起票元
- 施策: `sessions/initiatives/gha-session-prompt-conversion-pattern/`
- 評価レポート: `06_eval_report.md` ルール化候補#1
