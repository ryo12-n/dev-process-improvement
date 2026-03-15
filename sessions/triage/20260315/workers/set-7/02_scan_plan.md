# スキャン計画: Set-7

## 壁打ちフェーズ [2026-03-15 02:00]

### 理解のサマリー
- タスクの目的: `.github/gha-skills-mapping.yml` のマッピングマニフェストに基づき、GHA プロンプト/ワークフロー定義とスキル定義の間のドリフト（乖離）を検出する
- スコープ: マニフェストに定義された2件のマッピング（triage-gha, l1-auto-execute-gha）の全チェックポイント突合 + 未マッピングワークフローのギャップ報告
- 完了条件: 全マッピングのチェック完了、ドリフト重大度判定済み、未マッピングワークフローの一覧報告

### 前提条件チェック
- [x] 割り当てTGタスクの内容を理解: 理解済み
- [x] 走査対象ファイル・ディレクトリの存在確認: 確認済み（`.github/gha-skills-mapping.yml` 存在、全 GHA/Skill ソース存在確認済み）
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
| 1 | TG-010 | GHA/Skills マッピング2件 + 未マッピングワークフロー | マニフェスト読み込み → 各マッピングの GHA/Skill ソース読み込み → チェックポイント突合 → inherent_differences 検証 → 未マッピング一覧作成 | 中 |

### 走査順序・依存関係
- TG-010 は単独タスク。依存関係なし
- マッピング内の走査順序: triage-gha → l1-auto-execute-gha → 未マッピングギャップ

### 走査対象ファイル一覧

**マニフェスト:**
- `.github/gha-skills-mapping.yml`

**triage-gha マッピング:**
- GHA: `.github/prompts/triage.md`
- Skill: `.claude/skills/triage-manager/SKILL.md`, `agents/triage-worker.md`, `agents/triage-evaluator.md`

**l1-auto-execute-gha マッピング:**
- GHA: `.github/workflows/backlog-auto-execute.yml`（inline prompt）
- Skill: `.claude/skills/l1-manager/SKILL.md`, `agents/l2-worker.md`, `agents/l2-evaluator.md`

**未マッピングワークフロー:**
- `.github/workflows/daily-triage.yml`
- `.github/workflows/backlog-candidate-propose.yml`
- `.github/workflows/backlog-to-issue.yml`
- `.github/workflows/initiative-close.yml`
- `.github/workflows/initiative-execute.yml`
- `.github/workflows/initiative-wallbash.yml`
- `.github/workflows/test-permissions.yml`

### 注意事項・制約
- set-4 で manager-common-policy の適用対象不整合が検出済み。GHA プロンプトとの突合で差異がないか注意
- ドリフト重大度は CRITICAL / WARNING / INFO の3段階で判定
- 未マッピングワークフローについては、マッピング追加の必要性を判断して報告

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-15
