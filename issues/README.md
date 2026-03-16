# issues/ ディレクトリ

## 用途

課題詳細の管理ディレクトリ。`プロセス改善_課題管理.csv`（全体俯瞰ハブ）と対になる1課題1ファイル形式で、CSV の1行では書ききれない背景・経緯・前提条件・参照資料などの詳細情報を管理する。

## ディレクトリ構成

```
issues/
├── README.md         # 本ファイル
├── _template.md      # 新規課題作成時のテンプレート
└── entries/          # 課題詳細ファイル格納先
    ├── ISS-042.md
    ├── ISS-045.md
    └── ...
```

- **ルート直下**: README・テンプレートのみ配置
- **entries/**: 全課題の `ISS-XXX.md` ファイルを格納。新規作成時は `_template.md` をコピーして `entries/` 配下に作成する

## 命名規則

- ファイル名: `ISS-XXX.md`（CSV の ID と一致させる）
- テンプレート: `_template.md` をコピーして `entries/` 配下に新規作成する
- 例: `entries/ISS-042.md`, `entries/ISS-045.md`

## CSV との関係

**`issues/entries/ISS-XXX.md` が正の情報源（Source of Truth）**。`プロセス改善_課題管理.csv` は `scripts/generate-csvs.py` により .md ファイルから自動生成される（PreToolUse hook で git commit 前に自動実行）。

CSV は手動で編集しないこと。課題の追加・更新は `.md` ファイルに対して行う。

| 管理対象 | .md ファイル | CSV（自動生成） |
|---------|-------------|----------------|
| 全体一覧・ステータス管理 | 正の情報源 | 俯瞰用（自動生成） |
| 課題の詳細情報 | 詳細（制限なし） | 要約（自動抽出） |

## 作成タイミング

L2（実施/評価）が `07_issues.md` の課題を転記する際に、`issues/entries/ISS-XXX.md` を作成する。ID は `python3 scripts/generate-csvs.py --next-issue-id` で取得する。
