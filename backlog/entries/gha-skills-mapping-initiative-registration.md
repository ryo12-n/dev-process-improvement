# gha-skills-mapping.yml に initiative ワークフロー4件のマッピング追加

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-079 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | |
| **起票日** | 2026-03-15 |
| **依存する環境前提** | GHA |

## 課題・背景

gha-initiative-skills-separation 施策で GHA 専用スキル4つ（gha-wallbash, gha-execute, gha-close, gha-question）を作成したが、`.github/gha-skills-mapping.yml` にこれら4件のマッピングが未登録。TG-010（GHA↔Skills 整合性チェック）でドリフト検出ができない状態であり、CRITICAL ドリフトとなっている。

追加対象:
- `initiative-wallbash.yml` → `.claude/skills/gha-wallbash/SKILL.md`
- `initiative-execute.yml` → `.claude/skills/gha-execute/SKILL.md`
- `initiative-close.yml` → `.claude/skills/gha-close/SKILL.md`
- `initiative-question.yml` → `.claude/skills/gha-question/SKILL.md`

## 期待効果

- TG-010 ドリフト検出精度向上
- CRITICAL ドリフト解消
- GHA↔Skills 整合性の完全化

## 補足・参考情報

- 起票元: `sessions/initiatives/gha-initiative-skills-separation/07_issues.md`
- 関連課題: ISS-063
- inbox ソース: inbox/gha-skills-mapping-initiative-registration.md

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
