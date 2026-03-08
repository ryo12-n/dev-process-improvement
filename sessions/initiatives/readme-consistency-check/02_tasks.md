# タスクリスト: README 整合性チェック

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク

### 実施ワーカー（l2-worker）向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | README.md のディレクトリ構成図を実態に合わせて更新する。`.claude/rules/`（3ファイル）、`.claude/skills/`（起動型4スキルのみ記載、ポリシー系は省略）、`sessions/sync/`、`sessions/metacognition/`、`backlog/`（entries/ + backlog.csv + README.md 形式）、`issues/`（entries/ + README.md + _template.md 形式）、トリアージテンプレート（00〜04 + workers/_template/ 構成）を反映する | ディレクトリ構成図の各エントリが `ls` で確認できる実ファイル/ディレクトリと一致している | 🔴 | ✅ |
| T-002 | README.md のセッション種別テーブルにメタ認知セッション（metacognition-manager）を追加する。セクション4として「メタ認知セッション」の起動方法説明を追加する | テーブルに metacognition-manager の行があり、起動方法セクション（`/metacognition-manager`）が記載されている | 🔴 | ✅ |
| T-003 | README.md の AI 向けスキル定義テーブルに sync-manager 系（sync-manager, sync-worker, sync-evaluator）と metacognition-manager 系（metacognition-manager, metacognition-worker, metacognition-evaluator）を追加する。起動型スキルのみ記載する（ポリシー系は含めない） | テーブルに sync 系3行 + metacognition 系3行が追加されている | 🔴 | ✅ |
| T-004 | README.md のドキュメントマップ「その他」セクションの `backlog/ideas.md` リンクを `backlog/README.md` に修正する | リンク先が実在するファイルを指している | 🟡 | ✅ |
| T-005 | triage-manager SKILL.md の「ルールとworkflowの整合性チェック」（174行目付近）に README 整合性チェック観点を追加する。チェック対象: ディレクトリ構成図・セッション種別テーブル・スキル定義テーブル・ドキュメントマップが実態と一致しているか。乖離発見時のアクション: 軽微なズレはそのセッション内で修正、大きな乖離は `プロセス改善_課題管理.csv` に起票。適用対象環境: SDK / CLI 共通 | SKILL.md に README 整合性チェックの観点・対象・アクションが記載されている | 🔴 | ✅ |
| T-006 | docs/workflow.md のトリアージフローに README 整合性チェックの記述を追加する。「ルール・workflow 整合性チェック」セクションに README を含む旨を明記する。適用対象環境: SDK / CLI 共通 | workflow.md に README 整合性チェックが含まれている | 🟡 | ✅ |
| T-007 | README.md の行数が150行以内に収まっているか確認する。超過する場合はディレクトリ構成図を簡略化するか、詳細を docs/ に切り出す | `wc -l README.md` が150以下、または超過理由が妥当で 04_work_report.md に記載されている | 🟡 | ✅ |
| T-008 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ✅ |
| T-009 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ✅ |

### 評価ワーカー（l2-evaluator）向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| E-001 | README.md の全セクションを実態と突合し、乖離が残っていないか検証する | 全チェック項目が PASS / FAIL で判定され、FAIL がない | 🔴 | ⬜ |
| E-002 | triage-manager SKILL.md の追記内容が既存のチェック項目と整合しているか確認する | 既存の記述と矛盾がないことが確認されている | 🔴 | ⬜ |
| E-003 | docs/workflow.md の追記内容がスキル定義と整合しているか確認する | workflow.md の記述が SKILL.md の内容を正しく反映している | 🟡 | ⬜ |
| E-004 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| E-005 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-08
