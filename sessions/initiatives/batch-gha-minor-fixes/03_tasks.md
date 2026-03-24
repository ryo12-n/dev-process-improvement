# タスクリスト: batch-gha-minor-fixes

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | - | Worker |
| なし | - | - | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-008 | 逐次実行 |
| L2-evaluator | T-E01 | 成果物評価 |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | L2-evaluator | T-001〜T-008 | Wave 1 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | - |

## 実施タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `gha-skills-mapping.yml` に initiative ワークフロー4件のマッピングを追加する。追加対象: `initiative-wallbash.yml` → `.claude/skills/gha-wallbash/SKILL.md`、`initiative-execute.yml` → `.claude/skills/gha-execute/SKILL.md`、`initiative-close.yml` → `.claude/skills/gha-close/SKILL.md`、`initiative-question.yml` → `.claude/skills/gha-question/SKILL.md`。既存エントリ（triage-gha, l1-auto-execute-gha）の構造を踏襲すること | 4件のマッピングが `gha-skills-mapping.yml` に追加されている。checkpoints と inherent_differences を適切に設定している | 🔴 | ⬜ |
| T-002 | GHA スキル6件（gha-close, gha-execute, gha-guideline, gha-question, gha-test, gha-wallbash）の SKILL.md frontmatter に `disable-model-invocation: true` を追加する | 6件すべての SKILL.md frontmatter に `disable-model-invocation: true` が含まれている | 🔴 | ⬜ |
| T-003 | `gha-guideline/SKILL.md` に GHA ワークフロー間の責務移動時の対検証パターンを追記する。内容: (1) 移動元にステップが残存していないか確認、(2) 移動先に条件付きステップ（`if:` ガード）が正しく設定されているか確認、(3) 既存リソースの重複作成防止ロジックがあるか確認。追記場所はセクション7（変換パターン）付近の適切な位置 | `gha-guideline/SKILL.md` に責務移動の対検証パターンが3項目記載されている | 🟡 | ⬜ |
| T-004 | `gha-guideline/SKILL.md` のセクション7.2 の「やらないこと」テンプレートを用途クラス別に拡張する。書き込み系（wallbash/execute/close）: 共通4項目、読み取り専用系（question）: git/gh 禁止 + Write/Edit 禁止の3項目、検証用（test）: 独自構成。既存の共通4項目テンプレートの後に用途クラス別の差分を追記する形式 | 用途クラス（書き込み系・読み取り専用系・検証用）ごとの「やらないこと」テンプレートが記載されている | 🟡 | ⬜ |
| T-005 | バックログエントリ4件を `git rm` で削除する: `backlog/entries/gha-skills-disable-model-invocation.md`、`backlog/entries/gha-skills-mapping-initiative-registration.md`、`backlog/entries/gha-workflow-responsibility-transfer-verification.md`、`backlog/entries/gha-skill-usage-class-template.md` | 4件のバックログエントリファイルが削除されている | 🔴 | ⬜ |
| T-006 | 作業中に発見した知見を `phase-2-execution/set-1/03_worker_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-007 | `rule-change-checklist` スキル（`.claude/skills/rule-change-checklist/SKILL.md`）のチェックリスト全7項目を確認する。結果を `phase-2-execution/set-1/02_worker_log.md` に記録する | チェックリスト全7項目の結果が記録されている | 🔴 | ⬜ |
| T-008 | `phase-2-execution/set-1/07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` に作成する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

## 評価タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | T-001〜T-005 の成果物を評価する。成功基準: (1) マッピング4件の追加が正しいか、(2) disable-model-invocation が6件に設定されているか、(3) 責務移動検証パターンが適切か、(4) 用途クラス別テンプレートが既存構造と整合しているか、(5) バックログ削除が完了しているか | 評価レポートに全成功基準の合否判定が記載されている | 🔴 | ⬜ |
| T-E02 | 評価中に発見した知見を `phase-2-execution/set-1/06_eval_report.md` の「評価中の知見」セクションに記録する | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E03 | 評価中に新たに発見した課題を `phase-2-execution/set-1/07_issues.md` へ起票し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` に作成する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-24
