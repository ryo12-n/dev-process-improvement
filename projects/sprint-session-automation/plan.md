# 全体計画書: sprint-session-automation

## 目的
Claude Code の planner / generator / evaluator スキルを段階的に自律化し、
人間のオーケストレーション負荷を下げながらスプリント開発サイクルを回せる
仕組みを構築する。

## スコープ
- 実装先リポジトリ: `dev-process-improvement`
- 動作環境: Claude Code CLI
- 対象 skill: sprint-planner / sprint-generator / sprint-evaluator

## 自律化ロードマップ

```
Phase 1: 手動運用（基盤整備）
  人間がターミナルで各 skill を起動・判断・承認する
Phase 2: Hooks 通知（半自動）
  SessionEnd hook で「次に起動すべき skill」を macOS 通知
Phase 3: SDK オーケストレーター（全自動）
  Python スクリプトがファイル状態を読んで次セッションを自動起動
```

## 施策一覧

| # | 施策名 | 概要 | 優先度 | ステータス |
|---|--------|------|--------|-----------|
| 1 | sprint-skill-implementation | skill 3本 + sessions/sprints 整備 | 高 | 未着手 |
| 2 | sprint-hooks-handoff | SessionEnd hook で次セッション通知 | 中 | 未着手 |
| 3 | sprint-sdk-orchestrator | SDK からの自動セッション起動 | 低 | 未着手 |

## マイルストーン

| # | マイルストーン | 完了条件 | ステータス |
|---|-------------|---------|-----------|
| M1 | skill 基盤完成 | 3 skill + sessions/sprints が動作する | 未着手 |
| M2 | Hooks 通知動作 | SessionEnd で次起動指示が通知される | 未着手 |
| M3 | SDK 自動起動動作 | todo.md 状態を読んで次セッションが自動起動する | 未着手 |

## 方針・制約
- 各施策は独立した initiative として管理する
- Phase 1 が完了・検証済みになってから Phase 2 に着手する
- Phase 3 は Phase 2 の運用実績をもとに設計を固める

---
**作成日**: 2026-03-26
**最終更新**: 2026-03-26
