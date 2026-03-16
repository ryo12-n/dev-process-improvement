# ai-driven-dev-patterns テストインフラ整備

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-076 |
| **優先度** | 🔴 高 |
| **ステータス** | 候補 |
| **対象リポジトリ** | ai-driven-dev-patterns |
| **施策ディレクトリ名** | <!-- 施策化時に L1 が記入 --> |
| **起票日** | 2026-03-16 |
| **依存する環境前提** | ローカル CLI 推奨（ai-driven-dev-patterns への変更を含むため） |

## 課題・背景

`.claude/agents/feature-builder.md` と `test-writer.md` にテスト実行コマンドが `<!-- TODO: 本リポジトリのCIスクリプトパスに修正 -->` のまま未設定。TDD フローが設計されているが、実際には機能しない状態（ハーネスエンジニアリング観点4評価での発見）。

## 期待効果

- feature-builder / test-writer エージェントのTDDフローが実際に機能する
- テストスクリプトパスが設定されることで自動テスト実行・CI連携が有効化される
- ハーネスエンジニアリング観点4（検証とガードレール）のスコアが3/5→4/5以上に改善が見込まれる

## 補足・参考情報

- 発見施策: harness-engineering-brushup（ISS-HEB-002）
- 評価レポート: sessions/initiatives/_archive/harness-engineering-brushup/04_work_report.md
- 改善候補優先度: 🔴 高（テスト駆動開発の前提条件・現状TDDが機能しない唯一のブロッカー）

## 関連エントリ

- BL-077: ai-driven-dev-patterns documentarian 参照切れルール修正

---

## 起票時チェックリスト

- [x] バックログ ID を `BL-076` 形式で記載し、`backlog.csv` の ID 列と一致させた
- [x] 優先度を 🔴 高 で記載した
- [x] ステータスを「候補」で記載した
- [x] **対象リポジトリ**を明記した（`ai-driven-dev-patterns`）
- [x] 「依存する環境前提」に前提となる環境条件を記載した
- [x] 関連エントリを「関連エントリ」セクションに記載した
- [x] `backlog.csv` に対応する行を追加した
