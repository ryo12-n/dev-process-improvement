# ai-driven-dev-patterns documentarian 参照切れルール修正

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-077 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | ai-driven-dev-patterns |
| **施策ディレクトリ名** | <!-- 施策化時に L1 が記入 --> |
| **起票日** | 2026-03-16 |
| **依存する環境前提** | ローカル CLI 推奨（ai-driven-dev-patterns への変更を含むため） |

## 課題・背景

`.claude/agents/documentarian.md` が参照する `rules/design-doc.md` と `rules/code-in-docs.md` が `.claude/rules/` に存在しない（参照切れ）。documentarian が設計書を作成する際にこれらのルールを参照できず、不整合な設計書が生成されるリスクがある（ハーネスエンジニアリング観点調査での発見）。

## 期待効果

- documentarian エージェントが設計書作成時に適切なルールを参照できる
- 設計書品質の一貫性が確保される
- 参照切れによる暗黙的な動作（ルールなしで設計書生成）が解消される

## 補足・参考情報

- 発見施策: harness-engineering-brushup（ISS-HEB-001）
- 課題詳細: issues/entries/ISS-063.md
- 対応方針案: 1) `.claude/rules/design-doc.md` と `code-in-docs.md` を新規作成する、または 2) documentarian の参照先を存在するファイルに修正する

## 関連エントリ

- BL-076: ai-driven-dev-patterns テストインフラ整備

---

## 起票時チェックリスト

- [x] バックログ ID を `BL-077` 形式で記載し、`backlog.csv` の ID 列と一致させた
- [x] 優先度を 🟡 中 で記載した
- [x] ステータスを「候補」で記載した
- [x] **対象リポジトリ**を明記した（`ai-driven-dev-patterns`）
- [x] 「依存する環境前提」に前提となる環境条件を記載した
- [x] 関連エントリを「関連エントリ」セクションに記載した
- [x] `backlog.csv` に対応する行を追加した
