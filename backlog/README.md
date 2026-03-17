# backlog 施策一覧

## 目的

`backlog/` 配下の施策候補を俯瞰的に把握するための管理フォルダ。各施策の優先度・ステータス・対象リポジトリを一目で確認でき、施策選定やトリアージの判断材料として利用する。

## 施策一覧（CSV）

施策の一覧は **[backlog.csv](./backlog.csv)** で俯瞰できる。**CSV は `scripts/generate-csvs.py` により `entries/` の .md ファイルから自動生成される**（PreToolUse hook で git commit 前に自動実行）。CSV は手動で編集しないこと。

### CSV の列構成

| 列名 | 説明 |
|------|------|
| ID | バックログ ID（BL-001 形式）。一意の識別子 |
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
- 各施策の詳細は `ファイル名` 列に記載された `.md` ファイルを参照（`entries/` 配下に格納）

## ディレクトリ構成

```
backlog/
├── backlog.csv       # 施策一覧（全体俯瞰ハブ）
├── README.md         # 本ファイル
├── _template.md      # 新規施策作成時のテンプレート
└── entries/          # 施策詳細ファイル格納先
    ├── 施策A.md
    ├── 施策B.md
    └── ...
```

- **ルート直下**: CSV・README・テンプレートのみ配置
- **entries/**: 全施策の `.md` ファイルを格納。新規作成時は `_template.md` をコピーして `entries/` 配下に作成する

## 管理システムのすみわけ

inbox・backlog・課題管理 CSV の使い分けについては **[管理システムのすみわけガイド](../docs/management-system-guide.md)** を参照。

## 運用ルール

1. **新規 backlog 追加時**: `_template.md` をコピーして `entries/` 配下に `.md` ファイルを作成する。ID は `python3 scripts/generate-csvs.py --next-backlog-id` で取得する。CSV は自動生成されるため手動追加不要。**テンプレート末尾の「起票時チェックリスト」で記載漏れを確認すること**
2. **initiative 開始時**: 施策を `sessions/initiatives/` で開始したら、該当する `entries/*.md` のメタ情報テーブルのステータスを「initiative 開始済」に更新すること
3. **backlog ファイル削除時**: `git rm` で `entries/` 配下の backlog ファイルを削除する。CSV は自動再生成される
4. **Issue 起票時**: 「Backlog to Issue」ワークフロー（`.github/workflows/backlog-to-issue.yml`）を BL-xxx ID を指定して手動実行する。backlog エントリの内容がそのまま Issue body に転記される

### 記載ルール（凡例）

- **優先度**: 🔴 高 / 🟡 中 / 🔵 低（詳細は `_template.md` の凡例を参照）
- **対象リポジトリ**: `ai-driven-dev-patterns` / `dev-process-improvement` / `横断` のいずれかを必ず記載する
- **依存する環境前提**: この施策が前提とする環境条件（例: SDK 環境 / ローカル CLI / GHA）を記載する。バックログメンテナンス BM-003 の前提条件変化チェックで参照される
- **関連エントリ**: `BL-XXX: <施策名>` 形式で記載する。バックログメンテナンス BM-005 の重複・統合候補検出で参照される

---

**最終更新**: 2026-03-15
