# backlog-auto-execute.yml への GHA スキル分離パターン適用

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-078 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | |
| **起票日** | 2026-03-15 |
| **依存する環境前提** | GHA |

## 課題・背景

gha-initiative-skills-separation 施策で initiative ワークフロー4つに GHA 専用スキルを作成し、YAML プロンプトのリファクタを完了した。`backlog-auto-execute.yml` も同様のスコープクリープリスクがあるが、スコープ限定のため本施策では対象外とした。

`backlog-auto-execute.yml` に対しても同パターン（`gha-auto-execute/SKILL.md` 作成 + YAML プロンプトリファクタ + execution_file 修正）を適用する必要がある。

## 期待効果

- GHA ワークフロー保守性向上
- YAML プロンプトのスキル分離による可読性向上
- gha-initiative-skills-separation パターンの横展開

## 補足・参考情報

- 起票元: `sessions/initiatives/gha-initiative-skills-separation/08_gate_review.md` 横展開セクション
- inbox ソース: inbox/gha-auto-execute-skills-separation.md

## 関連エントリ

なし

---

## 起票時チェックリスト

- [x] バックログ ID を `BL-XXX` 形式で記載し、`backlog.csv` の ID 列と一致させた
- [x] 優先度を 🔴/🟡/🔵 のいずれかで記載した
- [x] ステータスを「候補 / initiative 開始済 / 完了」のいずれかで記載した
- [x] **対象リポジトリ**を明記した（`ai-driven-dev-patterns` / `dev-process-improvement` / `横断` のいずれか）。精査・変更対象ファイルが実際に存在するリポジトリを記載し、GHA/SDK 環境での実施可否判断に影響しないか確認した
- [x] 「依存する環境前提」に前提となる環境条件を記載した（不明な場合は「なし」と記載）
- [x] 関連エントリがある場合は「関連エントリ」セクションに `BL-XXX: <施策名>` 形式で記載した
- [x] `backlog.csv` に対応する行を追加した
