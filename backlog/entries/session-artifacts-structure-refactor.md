# 非施策セッション成果物の構造・プレフィックス見直し

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-072 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-15 |
| **起票元** | config-optimization/20260315 セッション終了時の気づき |

## 概要

非施策セッション（triage, metacognition, sync, backlog-maintenance, automation, config-optimizer）の成果物ディレクトリ構造とファイルプレフィックス番号を見直し、生成順・閲覧順が直感的に分かるようにする。

## 現状の問題

1. **マネージャー層のプレフィックスが飛び番**: `00`〜`04` の後に `15`, `25`, `35`（ゲート判定）が同階層に混在し、生成順が分かりづらい
2. **ワーカー set 内のプレフィックスが Phase 非依存**: set-1/2/3 全て `01`〜`07` で、ファイル名だけでは Phase が読み取れない
3. **全セッションタイプで同様の問題**: triage, metacognition 等も同じテンプレート構造を共有

## 対象スキル・テンプレート

- `.claude/skills/config-optimizer-manager/`（テンプレート + エージェント定義）
- `.claude/skills/triage-manager/`
- `.claude/skills/metacognition-manager/`
- `.claude/skills/sync-manager/`
- `.claude/skills/backlog-maintenance-manager/`
- `.claude/skills/automation-manager/`
- 各 `_template/` ディレクトリ

## 期待効果

- セッション成果物を上から順に読めば作業フローが追える
- Phase とファイルの対応が一目で分かる
- 新規セッションタイプ追加時のテンプレート設計が容易になる
