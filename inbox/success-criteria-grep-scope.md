# 成功基準の grep コマンドにスコープを明示する

## 気づき

`01_plan.md` の成功基準で `grep -r` を使う場合、対象ディレクトリが施策スコープと一致しないと評価時に false positive が発生する。

## 提案

成功基準に grep を含める場合、対象パスを施策スコープに限定する記述を推奨するガイドラインを追加する。

## 発見元

- 施策: phase-worker-set-standardization（L2-evaluator E-1）
- 日付: 2026-03-19
