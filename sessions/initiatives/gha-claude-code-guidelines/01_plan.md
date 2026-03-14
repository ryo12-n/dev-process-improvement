# 実施計画: GHA-Claude-Code運用ガイドライン策定

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | ガイドラインスキル作成 + daily-triage.yml 権限適用 | スキルに5セクション記載済み。daily-triage.yml から `--dangerously-skip-permissions` が除去済み |
| 2 | 評価・ゲート判定 | 評価で権限3層の整合性が確認されている。allow リストが過不足ないことが検証されている |

## 成功基準（全体）

1. `.claude/skills/gha-guideline/SKILL.md` が作成され、権限3層モデル・設計判断基準・権限設定パターン・ghコマンド前提条件・既存マトリクスの5セクションが記載されている
2. `daily-triage.yml` から `--dangerously-skip-permissions` が除去され、適切な `--allowedTools` が設定されている
3. 評価で daily-triage.yml の allow リストと triage.md プロンプトの操作内容が突合検証され、過不足がないことが確認されている

## リソース・前提条件

- 既存4ワークフローの調査は L1 壁打ちフェーズで完了済み
- Claude Code CLI の `--allowedTools` フラグの書式確認が必要

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| allow リスト不足で triage が動かなくなる | 中 | 高 | triage.md の全操作を洗い出し済み。評価時に突合検証する |
| CLI の `--allowedTools` 書式が想定と異なる | 低 | 中 | Claude Code CLI ドキュメントで確認。`--help` 出力も参照する |

---
**作成者**: L1
**作成日**: 2026-03-14
**最終更新**: 2026-03-14
