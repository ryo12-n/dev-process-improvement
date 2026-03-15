# GHA ワークフローのトリガー変更時の再インデックス問題

## 知見

GitHub Actions のワークフローファイルで `on:` トリガーを変更した場合（例: `issues: [labeled]` → `workflow_dispatch`）、以下の問題が発生する。

### 症状

- Actions UI のサイドバーでワークフローが `name:` ではなくファイルパス（`.github/workflows/xxx.yml`）で表示される
- `gh workflow run <filename>` で `HTTP 422: Workflow does not have 'workflow_dispatch' trigger` エラーが発生する
- 他のワークフローからの `workflow_dispatch` ディスパッチも同様に失敗する

### 原因

- GitHub はワークフローを内部 ID で管理しており、トリガー変更時にキャッシュ/インデックスの更新に遅延が生じる
- PR マージ直後は特に、古いトリガー定義がキャッシュに残っている場合がある

### 対処法

1. **時間を置く**: GitHub の再インデックスを待つ（数分〜数十分）
2. **空コミット**: ワークフローファイルに無害な変更（コメント追加等）を push して再インデックスを促す
3. **再実行**: キャッシュ更新後に失敗したワークフローを再実行する

### 予防策

- `on:` トリガーを大幅に変更する PR をマージした直後に、そのワークフローを呼び出す別のワークフローを実行しない
- トリガー変更を含む PR のマージ後は、Actions UI で `name:` 表示に切り替わったことを確認してから後続の操作を行う

## 発生事例

- 2026-03-15: `initiative-wallbash.yml`, `initiative-execute.yml`, `initiative-close.yml` のトリガーを `issues: [labeled]` → `workflow_dispatch` に変更した PR マージ後、`backlog-to-issue.yml` からの `gh workflow run initiative-wallbash.yml` が 422 エラーで失敗
