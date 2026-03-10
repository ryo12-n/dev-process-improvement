---
name: external-repo-cleanup
description: '外部リポジトリのブランチ整理をオンデマンドで実行する。L1マネージャーが壁打ちフェーズ後に呼び出す。'
user-invocable: false
---

# 外部リポジトリのブランチ整理（オンデマンド）

## 目的

外部リポジトリのブランチ整理をオンデマンドで実行する。セッション開始時の自動実行から分離し、L1 マネージャーが壁打ちフェーズ後に外部リポジトリありと判断した時点で呼び出す。

## 呼び出しタイミング

L1 マネージャーの壁打ちフェーズ（フェーズ0）のステップ4「外部リポジトリのブランチ整理」で実行する。外部リポジトリの施策ブランチを作成する前に、前セッションの残留ブランチを整理する必要があるため。

## 走査手順

1. `sessions/initiatives/` 配下のアクティブ施策ディレクトリを列挙する（`_template`・`_archive` を除く）
2. 各施策の `00_proposal.md` の「外部リポジトリ」セクションを確認する
3. リポジトリ名が「なし」の場合はスキップする
4. 記載されたローカルパスが存在しない場合は警告を表示してスキップする

## 各外部リポジトリに対する整理フロー

既存の `.claude/rules/session-start-branch-cleanup.md` のステップ 1〜5 と同じフローを `git -C <path>` で実行する:

```bash
# ステップ 1 相当: 現在ブランチの確認
git -C <path> branch --show-current

# ステップ 2 相当: 未プッシュコミットの確認
git -C <path> log origin/<ブランチ>..HEAD --oneline

# ステップ 3 相当: 未プッシュコミットのプッシュ
git -C <path> push -u origin <ブランチ>

# ステップ 4 相当: PR の確認・作成（gh は -C 未対応のため cd で移動）
cd <path> && gh pr list --head <ブランチ> --base main --state open

# ステップ 5 相当: main への切り替え・最新化
git -C <path> checkout main && git -C <path> pull
```

### エラーハンドリング

- パスが存在しない場合: 「⚠️ 外部リポ <リポジトリ名>: パス <path> が存在しません（スキップ）」と表示し、次のリポジトリへ進む
- `git -C` でエラーが発生した場合: エラーを報告し、ユーザーに判断を仰ぐ

## 注意事項

- **マージは行わない**: PR の作成までが本フローの責務。マージはユーザーの判断に委ねる。
- **PR 作成済みならブロックしない**: 前セッションの PR がマージ待ちでも、main に切り替えて新しい作業を開始してよい。

## 関連ファイル一覧

| ファイル | 用途 |
|---------|------|
| `.claude/rules/session-start-branch-cleanup.md` | 本体リポの整理フロー（本スキルの元ロジック） |
| `.claude/skills/l1-manager/SKILL.md` | 呼び出し元（壁打ちフェーズのステップ4） |
| `docs/workflow.md` | 人間向け可視化 |

---
**作成日**: 2026-03-10
**関連施策**: `sessions/initiatives/external-repo-cleanup-on-demand/`
