# GHA スキル「やらないこと」の用途クラス別テンプレート化

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-079 |
| **優先度** | 🔵 低 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | |
| **起票日** | 2026-03-15 |
| **依存する環境前提** | GHA |

## 課題・背景

gha-session-prompt-conversion-pattern 施策の評価で、GHA スキルの「やらないこと」セクションが用途クラスごとに類型化できることが判明した。

- **書き込み系スキル**（wallbash/execute/close）: 共通4項目（PR作成禁止、gh禁止、破壊的git禁止、force push禁止）
- **読み取り専用スキル**（question）: git/gh 禁止 + Write/Edit 禁止の3項目
- **検証用スキル**（test）: 独自構成

現状、各スキルで「やらないこと」セクションを個別に記述しており、テンプレート化されていない。

## 期待効果

- スキル定義の標準化
- 新規 GHA スキル作成時の判断効率化
- 用途クラス別テンプレートによる抜け漏れ防止

## 補足・参考情報

- 起票元施策: `sessions/initiatives/gha-session-prompt-conversion-pattern/`
- 評価レポート: `06_eval_report.md` ルール化候補#1
- gha-guideline/SKILL.md セクション7.2のテンプレートを用途クラス別に拡張する方針
- inbox ソース: inbox/gha-skill-usage-class-template.md

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
