# ワーカー計画: template-cleanup — Set-3

## 壁打ちフェーズ [2026-03-24]

### 理解のサマリー
- タスクの目的: 可視化文書・整合性リファレンスの連動更新（T-003）
- スコープ: `docs/workflow.md` と `session-consistency-reference.md` の2ファイル
- 完了条件:
  1. `docs/workflow.md` のイニシアティブフローに `_template/` 削除ステップが追加されている
  2. `session-consistency-reference.md` の initiatives テンプレート構成が `01_gate.md` 除去後の状態に更新されている
  3. `docs/workflow.md` の 3-phase セッションフロー（config-optimization, session-consistency）の `01_gate.md` 記述は変更されていない
- set 番号: set-3

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（T-001, T-002 が先行して `01_gate.md` 削除済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
- [x] set 番号確認: 指定あり: set-3
- [x] set ディレクトリの存在確認: 確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. `docs/workflow.md` L56-66 付近を Read して `_template/` 削除ステップの有無を確認 → 必要なら追加
2. `session-consistency-reference.md` L120-122 付近（SC-004 テンプレート一覧）を確認 → initiatives の `01_gate.md` 関連を更新
3. `session-consistency-reference.md` L301-303 付近（SC-009 仕様突合結果）を確認 → initiatives のファイル数を 15 → 13 に更新
4. `docs/workflow.md` の 3-phase セッションフローの `01_gate.md` 記述が変更されていないことを確認
