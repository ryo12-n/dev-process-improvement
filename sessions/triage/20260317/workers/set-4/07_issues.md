# 課題メモ（ワーカーセット別バッファ）: Set-4

> **このファイルの役割**: ワーカーセット内で発見された課題・知見・リスクの一時メモ置き場。
> マネージャーが `03_report.md` 作成時に全ワーカーセットの課題を集約し、`プロセス改善_課題管理.csv` へ転記する。

## 転記ルール

- ワーカー・評価者は課題をこのファイルに起票する（CSV 直接起票はしない）
- マネージャーが集約時に CSV 転記の要否を判断する
- 施策スコープ外・他のセッションでも再発しうる課題 → **マネージャーが CSV に転記**
- 当セッション内だけで完結する軽微な修正メモ → 転記不要（クローズ扱い）
- 転記済みの項目には `[転記済 ISS-XXX]` を末尾に追記する

---

## 未転記メモ

### [2026-03-17] マニフェストの gha_source.path 不正（l1-auto-execute-gha）
- **種別**: 不具合
- **発見者**: ワーカー
- **内容**: `.github/gha-skills-mapping.yml` の `l1-auto-execute-gha` マッピングにおいて、`gha_source.path` が `.github/workflows/backlog-auto-execute.yml` を指しているが、このファイルは存在しない。実際のワークフローは `.github/workflows/initiative-execute.yml` であり、プロンプト本体は `.claude/skills/gha-execute/SKILL.md` に定義されている。また `gha_source.type` が `workflow-inline` で `prompt_location: "jobs.execute.steps[2].with.prompt"` と指定されているが、実際のプロンプトは外部スキルファイルへの Read 指示であり、inline prompt ではない。
- **対応方針（案）**: マニフェストの `l1-auto-execute-gha` マッピングを以下のように修正する:
  - `gha_source.path`: `.github/workflows/initiative-execute.yml` に修正
  - `gha_source.type`: `prompt` ではなく、新たに `type: skill-reference` 等のタイプを検討するか、skill_source 側に `gha-execute/SKILL.md` を追加する
  - あるいは GHA ソースを `gha-execute/SKILL.md` として `type: prompt` に変更する
- **関連タスク**: TG-010

### [2026-03-17] l1-auto-execute-gha: backlog エントリ削除ステップの欠落
- **種別**: 改善提案
- **発見者**: ワーカー
- **内容**: マニフェストの `workflow_steps.keys` に「backlog エントリ削除」が含まれているが、`gha-execute/SKILL.md` にはこのステップが存在しない。GHA execute フローでは施策ディレクトリが wallbash フェーズで既に作成済みであり、backlog エントリの削除は wallbash フェーズまたは initiative-dispatcher が担当している可能性がある。マニフェストの `workflow_steps` を実態に合わせて更新するか、inherent_differences に宣言すべき。
- **対応方針（案）**: マニフェストの `workflow_steps.keys` から「backlog エントリ削除」を削除するか、inherent_differences に `backlog-deletion-omission` を追加する
- **関連タスク**: TG-010
