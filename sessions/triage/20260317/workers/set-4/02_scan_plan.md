# スキャン計画: Set-4

## 壁打ちフェーズ [2026-03-17 00:00]

### 理解のサマリー
- タスクの目的: `.github/gha-skills-mapping.yml` に基づき、GHA プロンプト/ワークフローとスキル定義間のドリフト（乖離）を検出する
- スコープ: マニフェスト内の全2マッピング（triage-gha, l1-auto-execute-gha）のチェックポイント突合 + inherent_differences 検証
- 完了条件: 全マッピングのチェック完了、ドリフト重大度（CRITICAL/WARNING/INFO）判定済み、inherent_differences の有効性検証済み

### 前提条件チェック
- [x] 割り当てTGタスクの内容を理解: 理解済み
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み
  - `.github/gha-skills-mapping.yml`: 存在確認済み（2マッピング定義）
  - `.github/prompts/triage.md`: 存在確認済み
  - `.github/workflows/backlog-auto-execute.yml`: 不存在（マニフェスト記載パスが不正）
  - `.github/workflows/initiative-execute.yml`: 存在（実際の対応ワークフロー）
  - `.claude/skills/gha-execute/SKILL.md`: 存在（実際のプロンプト本体）
  - `.claude/skills/triage-manager/`: 存在確認済み
  - `.claude/skills/l1-manager/`: 存在確認済み
- [x] 走査に必要なツール・アクセス権限: 確認済み

### 不明点・確認事項
なし

### マネージャー確認結果
確認事項なし：実施開始

---

## スキャン計画

### 走査対象

| # | TGタスクID | 対象 | 走査方法 | 想定所要時間 |
|---|----------|------|---------|------------|
| 1 | TG-010 | triage-gha マッピング | task_ids / workflow_steps / report_sections / file_templates の突合 + inherent_differences 検証 | 中 |
| 2 | TG-010 | l1-auto-execute-gha マッピング | file_numbers / workflow_steps / file_templates の突合 + inherent_differences 検証 | 中 |

### 走査順序・依存関係
- triage-gha → l1-auto-execute-gha の順で走査（依存関係なし、順序は任意）

### 注意事項・制約
- `.claude/skills/` と `.github/prompts/` は読み取りのみ
- `l1-auto-execute-gha` の `gha_source.path` が `backlog-auto-execute.yml` を指すがファイル不存在。実際のワークフロー `initiative-execute.yml` と対応スキル `gha-execute/SKILL.md` で代替走査する
- マニフェストのパス不正自体を課題として起票する

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-17
