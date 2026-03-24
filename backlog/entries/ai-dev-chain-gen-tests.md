# ai-dev-chain gen-tests Skill プロンプト実装

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-106 |
| **優先度** | 🟡 中 |
| **ステータス** | initiative 開始済 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | ai-dev-chain-gen-tests |
| **起票日** | 2026-03-24 |
| **依存する環境前提** | gen-design 施策完了済み（openapi.yaml 出力が利用可能） |

## 課題・背景

ai-dev-chain の M5 マイルストーンとして `/gen-tests` Skill のプロンプト実装が次のステップとして定義されている。gen-design 完了により `openapi.yaml` / `design.md` が生成可能になり、gen-tests への入力が準備できた状態。SKILL.md には枠組みがあるが実際のプロンプト実装がまだない。

## 期待効果

- `/gen-tests projects/<name>` コマンドで `requirements.json` + `openapi.yaml` からテスト仕様（`tests.json` / `tests.md`）を自動生成できるようになる
- x-fr-id トレーサビリティを活用し、テストケースと FR の対応付けを自動検証できる設計が可能
- gen-req → gen-design → gen-tests のチェーンが通しで動作する状態になる

## 補足・参考情報

- gen-design の評価者知見: x-fr-id によるトレーサビリティは gen-tests でテストケースと FR の対応付けに活用可能
- gen-req / gen-design で確立した7ステップパターンを踏襲予定

## 関連エントリ

なし

---

## 起票時チェックリスト

- [x] バックログ ID を `BL-XXX` 形式で記載し、`backlog.csv` の ID 列と一致させた
- [x] 優先度を 🔴/🟡/🔵 のいずれかで記載した
- [x] ステータスを「候補 / initiative 開始済 / 完了」のいずれかで記載した
- [x] **対象リポジトリ**を明記した
- [x] 「依存する環境前提」に前提となる環境条件を記載した
- [ ] 関連エントリがある場合は「関連エントリ」セクションに `BL-XXX: <施策名>` 形式で記載した
- [ ] `backlog.csv` に対応する行を追加した
