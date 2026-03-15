# タスクリスト: GHA 用 initiative skills の分離

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | GHA 壁打ちスキルの作成: `.claude/skills/gha-wallbash/SKILL.md` を作成する。`initiative-wallbash.yml` の `prompt:` セクション（行46〜79付近）から指示・制約を抽出し、SKILL.md 標準構造（frontmatter + あなたの役割 / 作業フロー / やること / やらないこと）で記述する。`user-invocable: false` とする。CLAUDE.md・l1-manager のルールに従わない旨を明記する | ファイルが存在し、frontmatter に `user-invocable: false` が設定され、作業フロー・禁止事項セクションが記載されている | 🔴 | ✅ |
| T-002 | GHA 実行スキルの作成: `.claude/skills/gha-execute/SKILL.md` を作成する。`initiative-execute.yml` の `prompt:` セクション（行77〜115付近）から指示・制約を抽出する。approve/reject の2サブフローを含める | ファイルが存在し、approve/reject 両サブフローが記載されている | 🔴 | ✅ |
| T-003 | GHA クローズスキルの作成: `.claude/skills/gha-close/SKILL.md` を作成する。`initiative-close.yml` の `prompt:` セクション（行45〜71付近）から指示・制約を抽出する | ファイルが存在し、知見ルーティング・アーカイブ移動の手順が記載されている | 🔴 | ✅ |
| T-004 | GHA 質問スキルの作成: `.claude/skills/gha-question/SKILL.md` を作成する。`initiative-question.yml` の `prompt:` セクション（行48〜68付近）から指示・制約を抽出する。読み取り専用であることを明記する | ファイルが存在し、読み取り専用の制約が明記されている | 🔴 | ✅ |
| T-005 | ワークフロー YAML のプロンプトリファクタ: 4ワークフロー（`initiative-wallbash.yml`, `initiative-execute.yml`, `initiative-close.yml`, `initiative-question.yml`）の `prompt:` を短縮化する。スキルファイルの Read 指示 + 動的コンテキスト（Issue番号、ブランチ名、施策ディレクトリ等）+ CLAUDE.md/l1-manager 無視の1行リマインダーのみとする | 4ファイルの prompt が短縮化され、スキルファイル参照方式になっている | 🔴 | ✅ |
| T-006 | execution_file 出力修正の横展開: `initiative-execute.yml`, `initiative-close.yml`, `initiative-question.yml` の3ファイルで `steps.claude.outputs.result` を jq 抽出パターンに置換する。`initiative-wallbash.yml`（行100〜130付近）のパターンをリファレンスとする。フォールバックメッセージも含める | 3ファイルで jq 抽出パターンが適用され、フォールバックメッセージが含まれている | 🔴 | ✅ |

## フェーズ2 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-007 | `gha-guideline/SKILL.md` の権限マトリクス更新: セクション5の権限マトリクスに4つの新スキルファイルへの参照を追加する。`initiative-question.yml` がマトリクスに含まれていない場合は追加する | 権限マトリクスに4スキルが記載されている | 🟡 | ✅ |
| T-008 | `docs/workflow.md` の更新: GHA ワークフロー用スキルの記述を追加する。各スキルの責務と対応ワークフローを記載する | docs/workflow.md に GHA スキルのセクションが追加されている | 🟡 | ✅ |
| T-009 | `refs/claude-code-action/knowledge.md` への知見追記: スキル分離アプローチの知見を追記する（#7, #8 の根本対策として） | knowledge.md に新規エントリが追加されている | 🟡 | ✅ |
| T-010 | `inbox/gha-execution-file-fix-rollout.md` の削除: execution_file 修正の横展開が完了したため、`git rm` で削除する | ファイルが削除されている | 🟡 | ✅ |

## 固定タスク（実施ワーカー）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-011 | 作業中の知見記録: 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-012 | 課題転記: `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |
| T-013 | メタルール横断検証: `.claude/skills/` 配下に新規ファイルを作成する施策のため、以下3領域の検証を実施し結果を `04_work_report.md` に記録する。(1) メタルールフロー記述: 新スキルを参照しているスキル・エージェント定義のフロー記述が実態と一致しているか確認 (2) workflow.md 同期: `docs/workflow.md` の該当セクションが変更内容と整合しているか確認・更新 (3) TG-008 基準連動: `triage-standard-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新 | 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている | 🔴 | ✅ |

## 固定タスク（評価ワーカー）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-014 | 評価中の知見記録: 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-015 | 評価中の課題起票・転記: 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

## 注意事項

- T-001〜T-004 のスキルファイル作成時、各ワークフロー YAML の `prompt:` 内容を正確に抽出すること。制約の欠落に注意
- T-005 のリファクタでは、ワークフロー固有の動的パラメータ（Issue番号、ブランチ名、フィードバック内容等）はスキルファイルに移動せず YAML に残すこと
- T-006 の execution_file 修正は `initiative-wallbash.yml` の実装を忠実に踏襲すること（jq クエリ、フォールバック処理）
- 適用対象環境: CLI / SDK いずれでも実施可（dev-process-improvement リポジトリ内で完結）

---
**作成者**: L1
**最終更新**: 2026-03-15
