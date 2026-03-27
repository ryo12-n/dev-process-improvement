# ワーカー計画: batch-skill-session-tweaks — Plan-Worker Set-1

## 壁打ちフェーズ [2026-03-26 12:00]

### 理解のサマリー
- タスクの目的: backlog-batch-execution batch #6 として、スキル・セッション定義の微調整7件のファイルレベルタスク分割を作成する
- スコープ: `.claude/skills/` 配下の6ファイルへの追記 + 1件の調査レポート。すべて追記のみで既存構造の変更なし
- 完了条件: `08_task_division.md` が作成され、7件のタスクが適切に定義されている。`03_worker_report.md` に計画レポートが記載されている

### 前提条件チェック
- [x] 施策計画（02_plan.md）の内容を理解: 理解済み
- [x] 提案書（01_proposal.md）の確認: 確認済み
- [x] 変更対象ファイル群の特定: 特定済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：計画開始

---

## 分析計画サマリ

7件のバックログエントリを調査し、それぞれの変更対象ファイル・追記箇所・受入基準を特定する。

### 変更対象ファイル一覧（調査結果）

| BL-ID | 変更対象ファイル | 変更種別 |
|-------|----------------|---------|
| BL-017 | `.claude/skills/l1-manager/agents/l2-worker.md` | MODIFY（壁打ちチェック項目への追記） |
| BL-027 | `.claude/skills/metacognition-manager/SKILL.md` | MODIFY（知見集約・課題集約セクション追加） |
| BL-040 | `.claude/skills/metacognition-manager/agents/metacognition-worker.md` | MODIFY（スキャンレポート構成ガイドへの追記） |
| BL-042 | `.claude/skills/session-flow-policy/SKILL.md` | MODIFY（§5.1 チェックリストへの追記） |
| BL-043 | （調査のみ。成果物は worker_report 内レポート） | READ のみ |
| BL-052 | `.claude/skills/backlog-maintenance-manager/agents/backlog-maintenance-worker.md` | MODIFY（BM-004 走査手順への追記 + スキャンレポート構成への追記） |
| BL-062 | `.claude/skills/l1-manager/SKILL.md` | MODIFY（タスク設計ガイダンス追記） |

### 並列性分析

全7タスクが異なるファイルを変更対象としているため、全タスクを Wave 1 で並列実行可能。ただし BL-043 は調査タスクで成果物がレポートのみであり、他タスクとの依存関係はない。
