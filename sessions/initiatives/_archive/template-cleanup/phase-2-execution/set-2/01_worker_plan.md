# ワーカー計画: template-cleanup — Set-2

## 壁打ちフェーズ [2026-03-24]

### 理解のサマリー
- タスクの目的: T-002 — スキル・ルールの更新（_template/ 削除ステップ追加 + 01_gate.md 参照除去）
- スコープ: 3ファイルの修正（l1-manager/SKILL.md, parallel-dev.md, session-lifecycle-policy/SKILL.md）
- 完了条件:
  - `l1-manager/SKILL.md` の set コピー手順に `_template/` 削除ステップが含まれている
  - `parallel-dev.md` §2.1 に `_template/` 削除が明記されている
  - `session-lifecycle-policy/SKILL.md` §1.4.3 から initiatives の `01_gate.md` が除去されている
  - `session-flow-policy/SKILL.md` は変更されていない
- set 番号: set-2

### 前提条件チェック
- [x] 依存タスクの完了状態: 依存なし（T-001 と並列実行可能）
- [x] 必要ツール・コマンドの利用可否: 確認済み
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
- [x] set 番号確認: 指定あり: set-2
- [x] set ディレクトリの存在確認: 確認済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ
1. 3つの対象ファイルを読み込み、変更箇所を特定
2. `l1-manager/SKILL.md` L127 の後に `_template/` 削除ステップを追加
3. `parallel-dev.md` §2.1 のコピー手順に削除を追記
4. `session-lifecycle-policy/SKILL.md` §1.4.3 の initiatives ツリーから `01_gate.md` 行を2箇所削除（基本モデルの L123 は残す）
5. `session-flow-policy/SKILL.md` が未変更であることを確認
