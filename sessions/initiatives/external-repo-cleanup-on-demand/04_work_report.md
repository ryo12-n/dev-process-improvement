# 作業レポート: 外部リポジトリブランチ整理のオンデマンド化

## サマリ

セッション開始時に毎回実行されていた外部リポジトリのブランチ整理（旧ステップ6）を独立スキル `external-repo-cleanup` として切り出し、L1 マネージャーが壁打ちフェーズで外部リポジトリありと判断した場合にのみオンデマンドで呼び出す形に変更した。4ファイルの変更を完了。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | external-repo-cleanup/SKILL.md 新規作成 | 旧ステップ6の移植 | 完了 | 差異なし |
| T-002 | session-start-branch-cleanup.md 修正 | ステップ6削除・繰り上げ | 完了 | 差異なし |
| T-003 | l1-manager/SKILL.md 修正 | 壁打ちフェーズにステップ追加 | 完了 | 差異なし |
| T-004 | docs/workflow.md 更新 | フロー図の連動更新 | 完了 | 差異なし |

## 成果物一覧
- `.claude/skills/external-repo-cleanup/SKILL.md`（新規）
- `.claude/rules/session-start-branch-cleanup.md`（修正）
- `.claude/skills/l1-manager/SKILL.md`（修正）
- `docs/workflow.md`（修正）

## 発生した課題
- なし

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | ユーティリティスキルは `user-invocable: false` で定義する | `.claude/skills/` | マネージャーフロー内から参照される補助ツール（`rule-change-checklist`、`manager-common-policy` 等と同種）は `user-invocable: false` とし、他スキルから参照される形にする |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | ステップ番号の繰り上げ時は全ジャンプ先の参照を検証する | session-start-branch-cleanup.md でステップ6を削除した際、ステップ1とステップ5からの「ステップ6へ進む」参照が旧ステップ7（新ステップ6）を正しく指すことを確認する必要があった |

## 所感・次フェーズへの申し送り
- 特になし

---
**作成者**: L1
**作成日**: 2026-03-10
