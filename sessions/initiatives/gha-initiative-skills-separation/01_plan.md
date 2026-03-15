# 実施計画: GHA 用 initiative skills の分離

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | GHA スキルファイル作成 + ワークフロー YAML リファクタ + execution_file 修正 | 4スキルファイル作成済み、4ワークフロー YAML 更新済み、execution_file 修正3件完了 |
| 2 | ドキュメント更新 + クリーンアップ | gha-guideline 更新済み、docs/workflow.md 更新済み、knowledge.md 追記済み、inbox 削除済み |

## スケジュール

1. フェーズ1: スキル作成・YAML リファクタ・execution_file 修正（メイン作業）
2. フェーズ2: ドキュメント整合性更新・クリーンアップ

## 成功基準（全体）

1. `.claude/skills/gha-wallbash/SKILL.md`, `gha-execute/SKILL.md`, `gha-close/SKILL.md`, `gha-question/SKILL.md` の4ファイルが作成されている
2. 4ワークフロー YAML の `prompt:` がスキルファイル参照 + 動的コンテキストのみで構成されている
3. `initiative-execute.yml`, `initiative-close.yml`, `initiative-question.yml` で execution_file の jq 抽出パターンが適用されている
4. `gha-guideline/SKILL.md` の権限マトリクスに新スキルへの参照が含まれている
5. `docs/workflow.md` に GHA スキルの記述が追加されている
6. `inbox/gha-execution-file-fix-rollout.md` が削除されている

## リソース・前提条件

- `initiative-wallbash.yml` の execution_file 抽出パターンをリファレンスとする
- `refs/claude-code-action/knowledge.md` の知見（#7, #8, #9）を参照する
- `gha-guideline/SKILL.md` の3層権限モデルに準拠する

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| Claude がスキルファイルを Read しない | 低 | 中 | プロンプトに明示的 Read 指示を含める |
| YAML リファクタ後のプロンプトが不足する | 低 | 中 | wallbash.yml の既存パターンを踏襲する |

---
**作成者**: L1
**作成日**: 2026-03-15
**最終更新**: 2026-03-15
