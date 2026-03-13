# GHA ワークフロー作成チェックリスト

## 背景
施策 `backlog-auto-initiative-gha` の評価で、`${{ }}` 式をシェルコマンドに直接展開するインジェクションリスクが発見された（ISS-058）。Phase 1 では env 経由パターンが採用されていたが Phase 2 では直接展開が残っており、一貫性がなかった。

## 提案
GHA ワークフロー作成時のセキュリティベストプラクティスをチェックリスト化し、`.claude/rules/` にルール追加する。

## チェック項目案
- `run:` ブロックで `${{ }}` を直接展開せず `env:` 経由で渡す
- `permissions` は最小権限に設定する
- secrets はハードコードせず `${{ secrets.XXX }}` で参照する

## 起票元
- 施策: `sessions/initiatives/backlog-auto-initiative-gha/`
- 評価レポート: `06_eval_report.md` ルール化候補 #1
- 関連課題: ISS-058
