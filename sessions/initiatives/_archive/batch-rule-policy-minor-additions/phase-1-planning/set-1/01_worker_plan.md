# ワーカー計画: batch-rule-policy-minor-additions — Set-1

## 壁打ちフェーズ [2026-03-25 12:00]

### 理解のサマリー
- タスクの目的: 7件のバックログエントリ（BL-022, BL-028, BL-063, BL-044, BL-046, BL-041, BL-025）に対応するルール・ポリシーの軽微追記を計画し、ファイルレベルのタスク分割を作成する
- スコープ: 既存ルール・ポリシーファイルへの追記7件 + docs/workflow.md の連動更新。逐次ディスパッチ（1ワーカー）前提
- 完了条件: `08_task_division.md` に全7件のタスク割当・Conflict Check Matrix・Wave Assignment が記載されていること

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

### 変更対象ファイルの調査結果

| # | BL ID | 変更先ファイル | 変更種別 | 行数 | 影響セクション |
|---|-------|-------------|---------|------|-------------|
| 1 | BL-022 | `.claude/skills/rule-change-checklist/SKILL.md` | MODIFY | 119行 | §5 の後に新チェック項目を追加 |
| 2 | BL-028 | `.claude/skills/manager-common-policy/SKILL.md` | MODIFY | 268行 | §4 ゲート判定基準にサブセクション追加 |
| 3 | BL-063 | `.claude/skills/manager-common-policy/SKILL.md` | MODIFY | 268行 | §5.3 付近にリファレンス粒度基準サブセクションを追加 |
| 4 | BL-044 | `.claude/skills/session-flow-policy/SKILL.md` | MODIFY | 247行 | §2.1 YAML フロントマターの後に description 設計パターンを追記 |
| 5 | BL-046 | `.claude/skills/l1-manager/SKILL.md` | MODIFY | 428行 | 「タスクリストに含める固定タスク」セクションをサブヘッダで構造化 |
| 6 | BL-041 | `.claude/skills/session-flow-policy/SKILL.md` | MODIFY | 247行 | §2.2 または §3 に「関連ファイル一覧」セクション義務化ルールを追加 |
| 7 | BL-025 | `.claude/skills/session-flow-policy/SKILL.md` | MODIFY | 247行 | 新セクション §3.6 または §3.7 にエージェント管理ガイドラインを追加 |
| 8 | 連動 | `docs/workflow.md` | MODIFY | 大 | ルール変更に伴う該当セクションの更新 |

### 競合分析

- **session-flow-policy/SKILL.md**: BL-044, BL-041, BL-025 の3件が同一ファイルを MODIFY
  - BL-044: §2 の YAML フロントマター説明に description パターンを追記
  - BL-041: §2.2 または §3 に関連ファイル一覧ルールを追加
  - BL-025: §3 にエージェント管理ガイドラインを追加
  - → 追記箇所が異なるセクションのため、逐次処理で競合なし
- **manager-common-policy/SKILL.md**: BL-028 と BL-063 の2件が同一ファイルを MODIFY
  - BL-028: §4 にサブセクション追加
  - BL-063: §5.3 付近に粒度基準追加
  - → 追記箇所が異なるセクションのため、逐次処理で競合なし
- **docs/workflow.md**: 全タスク完了後の連動更新として最後に処理

### BL-063 配置先の検討

BL-063（リファレンス文書の粒度基準ルール化）について、現状の refs/ と関連スキルを調査した結果:

- `refs/` の用途は CLAUDE.md で「他PJの実装・構成など、施策の参考にする参照物置き場」と定義
- `refs/_knowledge_template.md` は外部リポジトリ知見の蓄積テンプレート
- `manager-common-policy/SKILL.md` §5.3 が refs ルーティング実行手順を定義
- BL-063 のスコープは「L2-worker が作成するリファレンス文書の粒度基準」

**配置先の提案**: `manager-common-policy/SKILL.md` の §5 知見集約手順に `§5.4 リファレンス文書の粒度基準` として追加するのが最も自然。理由:
1. refs/ に関する運用手順は §5.3 に既にあり、粒度基準は同じ文脈
2. 新規ファイル作成より既存セクションへの追記の方が発見容易性が高い
3. マネージャーがレビューする際の参照導線に沿っている

### タスク分割方針

- 逐次ディスパッチ（1ワーカー）前提のため、全タスクを Wave 1 に配置
- session-flow-policy への3件追記は、セクション位置が異なるため順次処理で問題なし
- docs/workflow.md の連動更新は全追記完了後に一括で実施
- rule-change-checklist の固定タスクと知見記録の固定タスクを末尾に配置
