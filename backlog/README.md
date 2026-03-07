# backlog 施策一覧

## 目的

`backlog/` 配下の施策候補を俯瞰的に把握するための管理フォルダ。各施策の優先度・ステータス・対象リポジトリを一目で確認でき、施策選定やトリアージの判断材料として利用する。

## 施策一覧（CSV）

施策の一覧は **[backlog.csv](./backlog.csv)** で管理している。

### CSV の列構成

| 列名 | 説明 |
|------|------|
| 施策名 | 施策の名称 |
| 優先度 | 高 / 中 / 低 |
| ステータス | 候補 / initiative 開始済 |
| 対象リポジトリ | ai-driven-dev-patterns / dev-process-improvement / 横断 |
| 起票日 | YYYY-MM-DD |
| 簡易説明 | 施策の1行説明 |
| ファイル名 | 対応する backlog ファイル名（`.md`） |

### CSV の見方

- テキストエディタや表計算ソフトで開ける
- ソート・フィルタで優先度別・リポジトリ別の一覧が容易に取得可能
- 各施策の詳細は `ファイル名` 列に記載された `.md` ファイルを参照

## 管理システムのすみわけ

inbox・backlog・課題管理 CSV の使い分けについては **[管理システムのすみわけガイド](../docs/management-system-guide.md)** を参照。

## 運用ルール

1. **新規 backlog 追加時**: backlog ファイル（`.md`）を作成したら、`backlog.csv` にも行を追加すること
2. **initiative 開始時**: 施策を `initiatives/` で開始したら、`backlog.csv` の該当行のステータスを「initiative 開始済」に更新すること
3. **backlog ファイル削除時**: `git rm` で backlog ファイルを削除した場合は、`backlog.csv` から該当行を削除すること

---

**最終更新**: 2026-03-07
