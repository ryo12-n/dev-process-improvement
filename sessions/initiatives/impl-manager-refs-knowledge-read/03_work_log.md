# 作業履歴: impl-manager-refs-knowledge-read

## 壁打ちフェーズ [2026-03-17 11:06]

### 理解のサマリー
- タスクの目的: l1-impl-manager の知見フローを「書き込み一方通行」から「読み書き双方向」にする。各フェーズで refs 知見を参照し、ドメインエージェント参照の選定フローも移植する
- スコープ: l1-impl-manager/SKILL.md（Phase 1〜4 に refs 参照ステップ追加 + ドメインエージェント参照セクション追加）、investigation-worker.md / design-worker.md / impl-plan-worker.md の作業フロー・担当ファイルテーブル更新。impl-worker.md は変更対象外
- 完了条件: T-001〜T-010 全完了、03_work_log.md に作業記録、04_work_report.md に作業レポート（知見セクション含む）、07_issues.md の課題に転記判断

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（前提タスクなし）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Edit / Write / Read ツールで対応可能）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（全対象ファイルの存在を確認）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

### 参照ドメインエージェント確認
`refs/agency-agents/specialized/specialized-workflow-architect.md` を Read 済み。ワークフロー設計の専門知識（フロー網羅性、ハンドオフ契約、条件分岐の明示）を参考にする。特にフローに条件分岐（knowledge.md 存在/非存在）を追加する際の設計パターンとして活用する。

### 作業順序
1. **T-001〜T-003**: l1-impl-manager/SKILL.md への refs 参照ステップ追加（Phase 1, 2, 3, 4）
2. **T-007**: l1-impl-manager/SKILL.md へのドメインエージェント参照セクション追加
3. **T-004**: investigation-worker.md への refs 読み込みステップ追加
4. **T-005**: design-worker.md への refs 参照ステップ追加
5. **T-006**: impl-plan-worker.md への refs 参照ステップ追加
6. **T-009**: メタルール横断検証
7. **T-008**: 知見セクション記録
8. **T-010**: 課題転記判断

### 設計方針
- l1-manager/SKILL.md の「ドメインエージェント参照の選定」セクションをパターンとして使用
- refs 参照は「存在する場合に参照」の条件付き（knowledge.md が存在しない施策もある）
- 「知見は参考情報として扱い、最新コードベースの調査を省略しない」旨を必ず明記
- impl-worker は直接 refs を読まず、マネージャーからのディスパッチ時に知見要約を受け取る設計

---

## 作業ログ

