# タスクリスト: fork-sync-rebuild

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク（社内リポジトリの削除と再作成）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | 旧社内リポジトリ削除 | ai-driven-dev-patterns-fork が GitHub 上で削除済み | 🔴 | ✅ |
| T-002 | 社内リポジトリ2つの新規作成 | ai-driven-dev-patterns, dev-process-improvement が作成済み | 🔴 | ✅ |
| T-003 | ローカル clone + upstream リモート設定 | 両リポジトリが clone 済みで upstream リモートが設定済み | 🔴 | ✅ |
| T-004 | 初回同期（upstream → origin push） | 両リポジトリの origin/main が upstream/main と一致 | 🔴 | ✅ |

## フェーズ2 タスク（fork-sync スキルの作成）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-005 | repos.json の作成 | .claude/skills/fork-sync/repos.json が配置済み | 🔴 | ✅ |
| T-006 | SKILL.md の作成（初版） | .claude/skills/fork-sync/SKILL.md が配置済み | 🔴 | ✅ |
| T-007 | SKILL.md をブランチ+PR方式に修正 | main 直接 push ではなくブランチ+PR方式に変更済み | 🔴 | ✅ |
| T-008 | origin 側 PR 作成・マージ | ryo-nagata_monotaro/dev-process-improvement に PR マージ済み | 🔴 | ✅ |
| T-009 | upstream 側 PR 作成・マージ | ryo12-n/dev-process-improvement に PR マージ済み | 🔴 | ✅ |

## フェーズ3 タスク（MEMORY.md の更新）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-010 | MEMORY.md の更新 | 新2リポジトリ構成 + /fork-sync スキルの記載に更新済み | 🟡 | ✅ |

---
**作成者**: L1
**最終更新**: 2026-03-08
