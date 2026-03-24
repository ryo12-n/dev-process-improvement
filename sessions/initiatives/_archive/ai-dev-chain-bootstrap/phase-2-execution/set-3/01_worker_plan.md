# ワーカー計画: ai-dev-chain-bootstrap — Set-3

## 壁打ちフェーズ [2026-03-24 12:00]

### 理解のサマリー
- タスクの目的: `/project-init` コマンド用の SKILL.md 骨格ファイルを作成する。`projects/_template/` を `projects/<project-name>/` にコピーする処理フローを定義する
- スコープ: `.claude/skills/project-init/SKILL.md` 1ファイルの作成。実装は TODO で示すのみ
- 完了条件: YAML フロントマター（name, description, user-invocable: true）、引数仕様、処理フロー、TODO コメントが記載されていること
- set 番号: 指定あり → set-3

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（T-001 は Wave 1 で完了済み。`projects/_template/` が存在することを確認済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Write ツールのみで完結）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（`projects/_template/` に 10 ファイル存在。gen-* Skills 5つも Wave 1 で作成済み）
- [x] set 番号確認: 指定あり: set-3
- [x] set ディレクトリの存在確認: 確認済み（7ファイル存在）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. gen-req/SKILL.md の構造を参考に、project-init/SKILL.md を作成する
2. overview.md の仕様に基づき、引数仕様（`<project-name>`、なしの場合はユーザーへ質問）を記載する
3. `projects/_template/` の実際の構成（10ファイル）を反映した処理フローを記載する
4. 後続実装箇所を TODO コメントで明示する
5. 作業ログ・レポートを記録する
