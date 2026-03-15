# GHA ワークフロー間の責務移動時の対検証パターン

## 背景
gha-wallbash-iterative-phase 施策で wallbash → execute への PR 作成責務移動を行った際、以下の検証パターンが有効だった:
1. 移動元にステップが残存していないか確認
2. 移動先に条件付きステップ（`if:` ガード）が正しく設定されているか確認
3. 既存リソースの重複作成防止ロジックがあるか確認

## 提案
- GHA ワークフロー変更施策の評価項目テンプレートに「責務移動の対検証」を含める
- `.claude/rules/gha-workflow-security.md` に追記する、または独立ルールとして作成する

## 起票元
`sessions/initiatives/gha-wallbash-iterative-phase/08_gate_review.md` 横展開セクション
