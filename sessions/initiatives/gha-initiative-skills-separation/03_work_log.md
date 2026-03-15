# 作業履歴: GHA 用 initiative skills の分離

## 壁打ちフェーズ [2026-03-15 10:00]

### 理解のサマリー
- タスクの目的: GHA ワークフロー（wallbash/execute/close/question）で Claude が CLAUDE.md や l1-manager のルールに従ってしまう問題を解消するため、GHA 専用スキルファイルを4つ作成し、ワークフロー YAML のプロンプトをスキルファイル参照方式にリファクタする。併せて execution_file 出力修正を3ワークフローに横展開する
- スコープ: T-001〜T-013（フェーズ1: スキル作成・YAML リファクタ・execution_file 修正、フェーズ2: ドキュメント更新・クリーンアップ、固定タスク: 知見記録・課題転記・メタルール検証）
- 完了条件: 4スキルファイル作成済み、4ワークフロー YAML 更新済み、execution_file 修正3件完了、gha-guideline 更新済み、docs/workflow.md 更新済み、inbox 削除済み、04_work_report.md と 07_issues.md が作成されている

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（施策ディレクトリ・提案・計画・タスクリスト作成済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read/Write/Edit/Bash/Glob/Grep 利用可能）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
  - 4つの YAML ファイルが存在（initiative-wallbash/execute/close/question.yml）
  - gha-guideline/SKILL.md が存在
  - docs/workflow.md が存在
  - refs/claude-code-action/knowledge.md が存在
  - inbox/gha-execution-file-fix-rollout.md が存在
  - .github/gha-skills-mapping.yml が存在

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

フェーズ1（T-001〜T-006）→ フェーズ2（T-007〜T-010）→ 固定タスク（T-011〜T-013）の順で実施する。

1. T-001〜T-004: 各ワークフロー YAML の prompt セクションからスキルファイルを作成（4ファイル並行可能だが順次作成）
2. T-005: 4ワークフロー YAML のプロンプトをスキルファイル参照方式にリファクタ
3. T-006: execution_file 出力修正を execute/close/question の3ファイルに横展開
4. T-007: gha-guideline の権限マトリクスに新スキルと question ワークフローを追加
5. T-008: docs/workflow.md に GHA スキルのセクションを追加
6. T-009: knowledge.md にスキル分離アプローチの知見を追記
7. T-010: inbox/gha-execution-file-fix-rollout.md を git rm で削除
8. T-011〜T-013: 知見記録・課題転記・メタルール横断検証

---

## 作業ログ

