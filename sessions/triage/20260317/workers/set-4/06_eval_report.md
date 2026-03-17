# 評価レポート: Set-4

## 評価サマリ

Set-4 ワーカーの TG-010（GHA ↔ Skills 整合性チェック）走査結果は高品質である。2 マッピング（triage-gha, l1-auto-execute-gha）の全チェックポイントが走査され、ドリフトの検出・重大度判定・inherent_differences 検証が適切に実施されている。CRITICAL-001（マニフェストの `gha_source.path` 不正）の検出は正確であり、課題起票も適切である。1 点、`prompt_location` のステップインデックスに軽微な誤りがあるが、結論（ステップ位置が不正である）自体は正しい。全体として承認を推奨する。

## TGタスク別完全性チェック

| タスクID | 完全性 | 備考 |
|---------|--------|------|
| TG-010 | 完全 | 2 マッピング・全チェックポイント（task_ids, workflow_steps, report_sections, file_templates, file_numbers）を網羅。inherent_differences 全 8 件の検証も完了 |

## 判断品質の評価

### マニフェスト読み込みの完全性

`.github/gha-skills-mapping.yml` の全フィールドが走査されている。triage-gha の 4 チェックポイント（task_ids, workflow_steps, report_sections, file_templates）、l1-auto-execute-gha の 3 チェックポイント（file_numbers, workflow_steps, file_templates）全てに結果が記載されている。マニフェストのメタ情報（gha_source, skill_source）についても独立にドリフト検証が行われており、漏れはない。

### チェックポイント突合の正確性

独立検証の結果:

1. **triage-gha / task_ids**: ワーカーの「TG-001〜TG-010 完全一致」の判定は、マニフェストの `pattern: "TG-\\d{3}"` と GHA プロンプト（`.github/prompts/triage.md`）の内容が一致することと整合する。正確。

2. **triage-gha / workflow_steps**: マニフェストに 8 ステップが定義されており、GHA 側に「ディスパッチログの記録」が追加されているとの報告は妥当。Skill 側の `02_dispatch_log.md` 管理と実質的に同等であるため INFO 判定は適切。

3. **triage-gha / report_sections**: 7 セクション全ての網羅確認は正確。

4. **triage-gha / file_templates**: Skill 側が個別ファイル参照、GHA 側がディレクトリレベル参照という差異の指摘は正確。INFO 判定は妥当。

5. **l1-auto-execute-gha / file_numbers**: Skill 側に追加 4 ファイル（00a, 02a, W_template 系）がある指摘は正確。GHA execute が単一エージェントモードで壁打ち・並列ディスパッチを省略するため inherent_differences の範疇とした判断は妥当。

6. **l1-auto-execute-gha / workflow_steps**: 「_template コピー」と「backlog エントリ削除」の欠落指摘は正確。`.github/workflows/initiative-execute.yml` を独立検証し、GHA execute フローに当該ステップがないことを確認した。WARNING 判定は妥当。

7. **l1-auto-execute-gha / file_templates**: GHA 側にテンプレート参照がないとの指摘は、`gha-execute/SKILL.md` が施策ディレクトリ作成済みの前提で動作することと整合。INFO 判定は妥当。

### ドリフト重大度判定の妥当性

- **CRITICAL-001（gha_source.path 不正）**: `.github/workflows/backlog-auto-execute.yml` が存在しないことを独立検証で確認した。実際のファイルは `.github/workflows/initiative-execute.yml` である。CRITICAL 判定は 01_tasks.md の基準（「Skill にあるが GHA にないタスク ID 等」に準じ、マニフェストが指すファイルが存在しないケース）に沿っている。正当な判定。
- **WARNING-001〜003**: いずれも「ステップ・構造の不一致」に該当し、WARNING 判定は基準に沿っている。
- **INFO 4 件**: いずれも軽微な差異（実運用上の影響なし）であり、INFO 判定は妥当。

### inherent_differences 検証の有効性

triage-gha 5 件、l1-auto-execute-gha 3 件、全 8 件について「有効」と判定されている。各判定の根拠（GHA プロンプトの明示的記載、スキルファイルの構造確認）が具体的に記載されており、妥当である。

### エビデンス品質

具体的なファイル名、ステップ数、タスク ID 範囲、件数が明記されている。曖昧な表現は見当たらない。

### 課題起票品質

07_issues.md に 2 件起票されている。いずれも走査結果の CRITICAL / WARNING と整合しており、対応方針案も具体的である。フォーマットも適切。

## 発見された課題

### 軽微な誤り: prompt_location のステップインデックス

ワーカーのスキャンレポートで WARNING-003 として「Claude Code の実行は steps[5]」と記載されているが、独立検証の結果、`.github/workflows/initiative-execute.yml` のステップ構成は以下の通り:

| インデックス（0-indexed） | ステップ名 |
|--------------------------|-----------|
| 0 | actions/checkout@v4 |
| 1 | Checkout initiative branch |
| 2 | Get issue title |
| 3 | Create PR (wallbashing to executing transition) |
| 4 | Update labels to executing |
| 5 | Update labels for reject re-execution |
| 6 | Run Claude Code |

正確には steps[6] である。ただし、ワーカーの結論（マニフェストの `prompt_location: "jobs.execute.steps[2].with.prompt"` が不正である点）自体は正しい。マニフェスト修正時には steps[6] を正しい値として使用すべきである。

この誤りは結論に影響しない軽微なものであり、差し戻しの理由にはならない。

## マネージャーへの推奨

**承認を推奨する。**

理由:
1. TG-010 の全マッピング・全チェックポイントが網羅的に走査されている
2. CRITICAL-001（マニフェストの `gha_source.path` 不正）の検出は正確であり、実害の評価と推奨アクションも適切
3. WARNING 3 件の検出・判定も妥当
4. inherent_differences 全 8 件の有効性検証が完了している
5. 課題起票が走査結果と整合している

軽微な指摘事項（マネージャー集約時に反映を推奨）:
- WARNING-003 の `prompt_location` の正しいステップインデックスは steps[6]（0-indexed）である。steps[5] ではない。マニフェスト修正 backlog 化の際にはこの点を反映すること

## 評価中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA ワークフロー構造変更時のマニフェスト連動更新ルール | `.github/gha-skills-mapping.yml`, `.claude/rules/gha-workflow-security.md` | CRITICAL-001 の根本原因は、ワークフローファイルのリネーム（backlog-auto-execute → initiative-execute）やプロンプトの外部化がマニフェストに反映されなかったこと。`gha-workflow-security.md` のチェック項目に「`gha-skills-mapping.yml` のパス・タイプ定義がワークフロー実態と一致することを確認する」を追加することを検討すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | triage-gha マッピングの整合性は高く維持されている | ワーカーの知見と一致。前回トリアージ以降の変更が GHA 側にも適切に反映されており、このマッピングの保守プロセスは機能している |
| 2 | l1-auto-execute-gha マッピングはマニフェスト定義自体の陳腐化が進んでいる | ワークフローファイル名の変更・プロンプト外部化・ステップ追加がマニフェストに未反映。initiative-dispatcher 導入に伴う構造変更が一因と推定される。マニフェスト更新を施策化する優先度は高い |
| 3 | ステップインデックスの検証には実ファイルの独立確認が不可欠 | ワーカーの steps[5] という記載は steps[6] の誤りだった。ワークフローファイルの条件付きステップ（`if:` 付き）の存在がインデックスのずれを生みやすい |

---
**作成者**: トリアージ評価者
**作成日**: 2026-03-17
