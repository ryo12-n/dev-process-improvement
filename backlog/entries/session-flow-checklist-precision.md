# session-flow-policy §5.1 チェックリストの精度向上

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-042 |
| **優先度** | 🔵 低 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** |  |
| **起票日** | 2026-03-12 |
| **依存する環境前提** | なし |

## 課題・背景

新セッションタイプ追加時（backlog-maintenance-session 施策）の実施・評価で、session-flow-policy §5.1 チェックリストに明記されていない連動更新箇所が発見された。

### チェックリストに含まれていない更新箇所

- `session-lifecycle-policy` の §1.3 記録先対応テーブル
- `session-lifecycle-policy` の §2.1 ペアリング構造テーブル
- `session-lifecycle-policy` の §3.1 走査対象リスト
- 各変更ファイルの「関連ファイル一覧」セクション

### 提案

§5.1 チェックリストに session-lifecycle-policy の更新箇所を明示する項目を追加し、次のセッションタイプ追加時の漏れを防ぐ。

## 期待効果

- セッションタイプ追加時の連動更新漏れ防止

## 補足・参考情報

- 発見元施策: `sessions/initiatives/backlog-maintenance-session/`
- 08_gate_review.md 必須把握事項 #1
- worker/evaluator 双方から同じ知見が報告された

## 関連エントリ

- **前提変化（2026-03-17 BM-003 検出）**: session-lifecycle-policy-rename 施策完了により `session-flow-policy` → `session-lifecycle-policy` にリネーム済み。本エントリのタイトル・本文の参照名を `session-lifecycle-policy` に更新し、現在の構造に合わせてスコープを再定義すること

---

## 起票時チェックリスト

- [x] バックログ ID を `BL-XXX` 形式で記載し、`backlog.csv` の ID 列と一致させた
- [x] 優先度を 🔴/🟡/🔵 のいずれかで記載した
- [x] ステータスを「候補 / initiative 開始済 / 完了」のいずれかで記載した
- [x] **対象リポジトリ**を明記した（`ai-driven-dev-patterns` / `dev-process-improvement` / `横断` のいずれか）。精査・変更対象ファイルが実際に存在するリポジトリを記載し、GHA/SDK 環境での実施可否判断に影響しないか確認した
- [x] 「依存する環境前提」に前提となる環境条件を記載した（不明な場合は「なし」と記載）
- [x] 関連エントリがある場合は「関連エントリ」セクションに `BL-XXX: <施策名>` 形式で記載した
- [x] `backlog.csv` に対応する行を追加した
