# 作業レポート: マネージャーセッション共通ポリシー策定

## サマリ

T-001〜T-012 の全12タスクを計画通り完了した。`manager-common-policy/SKILL.md` を新規作成し、4つのマネージャースキルの共通部分を参照に置換した。欠落していたゲート判定基準・差し戻し手順の補完、docs/workflow.md の連動更新、triage-standard-policy のチェック項目拡張、session-flow-policy への参照注記追加をすべて実施した。施策横断の課題は発見されなかった。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | manager-common-policy/SKILL.md 新規作成 | §1〜§8 全セクション | §1〜§8 全セクション作成 | 差異なし |
| T-002 | l1-manager 参照置換 | 共通部分を参照に置換、固有部分維持 | 起動観点→§2、確認観点→§3+固有、差し戻し→§7、判定→§4、知見→§5、課題転記→§6 | 差異なし |
| T-003 | triage-manager 参照置換+欠落補完 | 共通部分を参照に置換+ゲート判定・差し戻し追記 | §2, §3, §2.2, §5, §6 参照置換 + §4, §7 追記 | 差異なし |
| T-004 | metacognition-manager 参照置換+欠落補完 | T-003 と同様 | §2, §3, §2.2, §5, §6 参照置換 + §4, §7 追記 | 差異なし。結果集約セクションの手順3,4も§5,§6参照に更新 |
| T-005 | sync-manager 参照置換+欠落補完 | 共通部分を参照に置換+差し戻し追記 | §2, §3, §5, §6, §4 参照置換 + §7 追記 | 差異なし |
| T-006 | workflow.md 更新 | 共通ポリシーセクション追加 | セクション追加（3層構造・共通パターン一覧） | 差異なし |
| T-007 | 関連ファイル一覧の相互参照 | 5ファイル（4マネージャー+共通ポリシー） | 7ファイル（+triage-standard-policy, session-flow-policy） | 計画より拡大。T-008/T-009 で変更した2ファイルにも相互参照を追加 |
| T-008 | triage-standard-policy チェック項目追加 | ゲート判定・差し戻し確認項目追加 | セクション D として2項目追加、既存 D を E にリネーム | 差異なし |
| T-009 | session-flow-policy 参照注記追加 | §2.3 に注記 | §2.3 末尾に注記 + 関連ファイル一覧に追加 | 差異なし |
| T-010 | 知見記録 | ルール化候補・参考情報各1行以上 | 各1行記載 | 差異なし |
| T-011 | 課題転記 | 未転記課題をCSV転記 | 課題なし。「なし」と記載 | 差異なし |
| T-012 | rule-change-checklist 実施 | 全項目確認 | 6項目すべて確認済み | 差異なし |

## 成果物一覧
- `.claude/skills/manager-common-policy/SKILL.md`（新規作成）
- `.claude/skills/l1-manager/SKILL.md`（更新）
- `.claude/skills/triage-manager/SKILL.md`（更新）
- `.claude/skills/metacognition-manager/SKILL.md`（更新）
- `.claude/skills/sync-manager/SKILL.md`（更新）
- `docs/workflow.md`（更新）
- `.claude/skills/triage-standard-policy/SKILL.md`（更新）
- `.claude/skills/session-flow-policy/SKILL.md`（更新）
- `sessions/initiatives/manager-common-policy/03_work_log.md`
- `sessions/initiatives/manager-common-policy/04_work_report.md`
- `sessions/initiatives/manager-common-policy/07_issues.md`

## 発生した課題
なし

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 共通パターンの参照置換時、blockquote（`> **共通N項目**: ...`）形式が固有部分との区別に効果的 | 全マネージャースキル | 参照部分を blockquote で囲み、固有部分を通常テキストで書くパターンにより、どこが共通ポリシーからの参照でどこが固有かが一目で分かる。今後の共通化施策でも同様のフォーマットを推奨 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | metacognition-manager には triage-manager のような独立した「知見集約手順」「課題集約手順」セクションがなく、「結果の集約」セクション内のステップとして記載されていた | triage と meta で記述構造が微妙に異なるため、参照の置換方法がスキルごとに違った。将来的に記述構造の統一（独立セクション化）を検討してもよい |

## 所感・次フェーズへの申し送り
- 全タスクを計画通り完了。置換漏れや固有部分の誤削除はないと判断
- 評価ワーカーでの参照先セクション番号の突合検証を推奨

---
**作成者**: L2（実施）
**作成日**: 2026-03-08
