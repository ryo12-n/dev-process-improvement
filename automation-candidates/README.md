# automation-candidates/ ディレクトリ

## 用途

自動化候補の管理ディレクトリ。`automation-candidates.csv`（全体俯瞰ハブ）と対になる1候補1ファイル形式で、各候補の詳細情報（定型作業の発生源・自動化手段・費用対効果・実装方針など）を管理する。

## ディレクトリ構成

```
automation-candidates/
├── README.md                    # 本ファイル
├── automation-candidates.csv    # 全候補の一覧管理（俯瞰ハブ）
├── _template.md                 # 新規候補作成時のテンプレート
└── entries/                     # 候補詳細ファイル格納先
    ├── AC-001.md
    ├── AC-002.md
    └── ...
```

- **ルート直下**: README・CSV・テンプレートのみ配置
- **entries/**: 全候補の `AC-XXX.md` ファイルを格納。新規作成時は `_template.md` をコピーして `entries/` 配下に作成する

## 命名規則

- ファイル名: `AC-XXX.md`（CSV の候補ID と一致させる）
- テンプレート: `_template.md` をコピーして `entries/` 配下に新規作成する
- 例: `entries/AC-001.md`, `entries/AC-014.md`

## CSV との関係

| 管理対象 | CSV | entries/ |
|---------|-----|---------|
| 全体一覧・ステータス管理 | 主 | - |
| 候補の詳細情報 | 要約（候補名・カテゴリ・手段・スコア） | 詳細（発生源・実装方針・費用対効果分析） |
| リンク | `ファイル名` 列で参照 | - |

CSV の `ファイル名` 列に `entries/AC-XXX.md` を記入することで、CSV から詳細ファイルへのナビゲーションを確保する。

## ステータス定義

| ステータス | 説明 |
|-----------|------|
| 候補 | 自動化候補として登録済み。未評価または評価済みだが未起票 |
| backlog起票済 | backlog エントリとして起票済み。施策化待ち |
| 施策化済 | sessions/initiatives/ で施策として進行中 |
| 実装完了 | 自動化が実装・稼働している |
| 却下 | 評価の結果、自動化不要と判断 |

## 初期データの出典

AC-001〜AC-014 は先行施策「ai-automation-tool-review」（`sessions/initiatives/_archive/ai-automation-tool-review/`）の R-001〜R-014 から移行したデータ。

## 作成タイミング

automation-worker が AT-001（新規自動化候補スキャン）で新候補を発見した際に、`_template.md` をコピーして `entries/` 配下に作成する。
