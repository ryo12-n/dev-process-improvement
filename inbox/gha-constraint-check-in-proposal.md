# 施策設計段階での GHA 実行不可チェック（提案）

## 背景

施策 `external-repo-artifact-style-check` において、変更対象ファイルが `.claude/skills/l2-worker.md`（`.claude/` 配下）であったため、GHA execute ワークフローから実行不可となった（`claude-code-action@v1` が `.claude/` を sensitive directory として保護）。T-001 が実行フェーズでブロックされ、CLI モードでの手動対応が必要になった。

## 提案内容

施策の `00_proposal.md` テンプレートまたは壁打ちフェーズの確認項目に、変更対象ファイルと実行環境のチェックを追加する。

具体的には:
- 変更対象ファイルに `.claude/` 配下が含まれる場合 → 「GHA 実行不可 / CLI 必須」を明記する
- バックログエントリの「対象リポジトリ」欄に実行環境制約（CLI必須）を反映する

これにより、実行フェーズでのブロックを設計段階で事前検出できる。

## 参考

- 関連施策: `sessions/initiatives/external-repo-artifact-style-check/`（T-001 ブロック事例）
- 類似 inbox: `inbox/gha-claude-dir-write-restriction.md`（git plumbing 回避手順）
- 課題: `issues/entries/ISS-068.md`（施策横断技術制約として起票）

**起票元**: external-repo-artifact-style-check 施策 クローズフェーズ
**起票日**: 2026-03-19
