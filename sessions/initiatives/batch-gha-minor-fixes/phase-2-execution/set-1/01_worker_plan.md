# ワーカー計画: batch-gha-minor-fixes — Set-1

## 壁打ちフェーズ [2026-03-24 10:00]

### 理解のサマリー
- タスクの目的: GHA 関連の軽微な4件のバックログエントリをバッチ消化する
- スコープ: gha-skills-mapping.yml マッピング追加、disable-model-invocation 追加、gha-guideline 追記2件、バックログ削除、知見記録・チェック・課題転記
- 完了条件: T-001〜T-005 のファイル変更完了、T-006〜T-008 の記録・チェック完了、03_worker_report.md 作成、コミット・プッシュ完了
- set 番号: set-1（指定あり）

### 前提条件チェック
- [x] 依存タスクの完了状態: なし（独立タスク群）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read, Write, Edit, Bash, Glob, Grep）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（対象ファイルすべて存在確認済み）
- [x] set 番号確認: 指定あり: set-1
- [x] set ディレクトリの存在確認: 確認済み
- [x] 外部リポジトリ成果物の記法スタイル確認（外部リポジトリあり施策のみ）: 該当なし

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

1. **T-001**: `gha-skills-mapping.yml` に initiative ワークフロー4件（wallbash, execute, close, question）のマッピング追加。既存エントリ（triage-gha, l1-auto-execute-gha）の構造を踏襲
2. **T-002**: GHA スキル6件の frontmatter に `disable-model-invocation: true` 追加
3. **T-003**: `gha-guideline/SKILL.md` に責務移動の対検証パターン追記（セクション7付近）
4. **T-004**: `gha-guideline/SKILL.md` のセクション7.2 後に用途クラス別「やらないこと」テンプレート追記
5. **T-005**: バックログエントリ4件を `git rm` で削除
6. **T-006**: 知見記録（作業レポート）
7. **T-007**: rule-change-checklist 全7項目確認
8. **T-008**: 課題転記確認
