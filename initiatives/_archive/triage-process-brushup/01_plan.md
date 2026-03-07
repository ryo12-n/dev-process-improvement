# 実施計画: ai-driven-dev-patterns トリアージプロセスのブラッシュアップ

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|---------|
| フェーズ1 | テンプレートファイル構造の整備 | ワーカーテンプレートが7ファイル構成になっている |
| フェーズ2 | マネージャーテンプレートの拡充 | 事前調査/計画/レポート/ゲート判定テンプレートが拡充されている |
| フェーズ3 | スキル定義の更新 + backlog起票 | スキル定義3ファイルが更新され、TG-001〜TG-009体系になっている |

## 対象リポジトリ・ファイル

変更先: **ai-driven-dev-patterns** (`/home/nr202/projects/ai-driven-dev-patterns/`)

### スキル定義（フェーズ3で編集）
- `.claude/skills/triage/triage-manager.md` (205行)
- `.claude/skills/triage/triage-worker.md` (181行)
- `.claude/skills/triage/triage-evaluator.md` (109行)

### テンプレート（フェーズ1-2で編集）
- `triage/_template/workers/_template/` 配下（リナンバリング + 新規3ファイル）
- `triage/_template/00_pre_investigation.md` (82行)
- `triage/_template/01_plan.md`
- `triage/_template/03_report.md`
- `triage/_template/04_gate_review.md` (新規)

### 参照元（dev-process-improvement、読取のみ）
- `.claude/skills/triage-manager/` 配下
- `.claude/skills/triage-standard-policy/SKILL.md`
- `triage/_template/` 配下

## 成功基準（全体）

1. ワーカーテンプレートが7ファイル（01〜07）揃っている
2. スキル定義3ファイル内のファイル名参照が全て新番号に更新されている
3. TGタスク体系が TG-001〜TG-009 の9タスクになっている
4. 「CSV に直接起票」の記述が全て「07_issues.md に起票」に変更されている
5. scan_report / eval_report テンプレートに知見テーブルが存在する
6. triage-standard-policy 作成の backlog が dev-process-improvement 側に起票されている

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| リナンバリングの参照漏れ | 中 | 中 | フェーズ3完了後に grep で旧番号の残存チェック |
| 用語の不整合 | 中 | 中 | initiatives/→sessions/ 等の置換を検証 |
| 既存セッション実績への影響 | 低 | 高 | triage/20260305/ 等の過去実績は変更しない |

---
**作成者**: L1
**作成日**: 2026-03-07
**最終更新**: 2026-03-07
