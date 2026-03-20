# 単体スキルの session-lifecycle-policy 記載方針

## 気づき

現在の `session-lifecycle-policy` はマネージャー/ワーカー/評価者の3アーキタイプを前提としている。design-partner のような単体スキル（マネージャー＋ワーカー構成を取らない、人間との直接対話で完結するスキル）が増えた場合、例外テーブルまたは別カテゴリの追加が必要になる。

## 背景

- design-partner-skill 施策の L2-worker / L2-evaluator 双方から同様の知見が報告された
- 現時点では design-partner が唯一の単体スキルだが、今後類似のパターンが増える可能性がある

## 提案

- `session-lifecycle-policy` に「単体スキル」カテゴリを追加し、適用マトリクスに記載する
- または、適用除外テーブルを作成して単体スキルを明示的に除外する

---
**起票日**: 2026-03-20
**発見元**: sessions/initiatives/design-partner-skill/
