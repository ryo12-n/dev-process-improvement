# タスクリスト: GHA 壁打ちフェーズの独立・反復化

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker | T-001〜T-012 | スキル・テンプレート変更施策のためメタルール横断検証必須 |
| L2-evaluator | T-E01〜T-E03 | - |

## フェーズ1 タスク

### 実施ワーカー向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `sessions/initiatives/_template/00a_wallbash_log.md` を新規作成する。「現在の合意事項」セクション（毎回上書き）と「イテレーション履歴」セクション（追記）を持つ構造にする | テンプレートファイルが存在し、所定の2セクション構造を持つこと | 🔴 | ⬜ |
| T-002 | `sessions/initiatives/_template/02_tasks.md` にディスパッチ計画セクションを追加する。既存のフェーズ1タスクテーブルの前に配置する | テンプレートに「ディスパッチ計画」セクションと Worker/担当タスク/特記事項のテーブルが存在すること | 🔴 | ⬜ |
| T-003 | `.claude/skills/gha-wallbash/SKILL.md` を init/continue の2モード対応に書き換える。init モード: テンプレートコピー + `00_proposal.md`, `01_plan.md`, `02_tasks.md` のドラフト作成 + `00a_wallbash_log.md` の Round 1 記録。continue モード: `00a_wallbash_log.md` を読んでコンテキスト復元 → フィードバック反映 → ドラフト更新 → ログ追記。PR 作成は「やらないこと」に追加する | スキルファイルに init/continue 両モードのフローが記載され、成果物範囲が `00_proposal.md`, `01_plan.md`, `02_tasks.md`, `00a_wallbash_log.md` であること。PR 作成が「やらないこと」に含まれること | 🔴 | ⬜ |
| T-004 | `.github/workflows/initiative-wallbash.yml` に新 inputs（`mode`, `feedback`, `initiative_dir`, `branch`）を追加する。`mode=continue` 時は既存ブランチをチェックアウトするステップを追加する。PR 作成ステップを削除する。メタデータコメント投稿を `mode=init` 時のみに制限する。壁打ちサマリーの「次のステップ」に `/continue <feedback>` を追加する。適用対象環境: SDK（GHA） | YAML が構文的に正しく、新 inputs が定義され、mode=continue 時のブランチチェックアウトステップが存在し、PR 作成ステップが削除されていること | 🔴 | ⬜ |
| T-005 | `.github/workflows/initiative-dispatcher.yml` に `/continue` コマンドのルーティングを追加する。`phase=wallbashing` かつメタデータ存在時に `initiative-wallbash.yml` を `mode=continue` で dispatch する。エラーメッセージのヘルプテキストに `/continue` を追加する。適用対象環境: SDK（GHA） | dispatcher が `/continue` コマンドを受け付け、wallbashing フェーズで wallbash ワークフローに routing すること。wallbashing 以外のフェーズではエラーメッセージが返ること | 🔴 | ⬜ |
| T-006 | `.github/workflows/initiative-execute.yml` に PR 作成ステップを追加する。`phase=wallbashing` の場合、Claude 実行前に PR を作成する。PR body にフェーズ進捗テーブルを含める。Issue タイトルの取得も追加する。適用対象環境: SDK（GHA） | `phase=wallbashing` 時に PR 作成ステップが実行される条件付きステップが存在すること | 🔴 | ⬜ |
| T-007 | `.claude/skills/gha-execute/SKILL.md` の `/approve` サブフローを修正する。ステップ 3-4 を「既存の壁打ちドラフト（`01_plan.md`, `02_tasks.md`）を読み取り、不足があれば補完・最終化する」に変更する。ドラフトがない（テンプレートのまま）場合はゼロから作成するフォールバックを明記する。適用対象環境: SDK（GHA） | approve サブフローが壁打ちドラフト活用の記述を持ち、フォールバック（テンプレートのみの場合は従来動作）が明記されていること | 🟡 | ⬜ |
| T-008 | `.claude/skills/l1-manager/SKILL.md` の Phase 0 壁打ちフェーズに `00a_wallbash_log.md` 記録ステップを追加する。壁打ち完了後に意思決定サマリーを記録する。「関連ファイル一覧」に `00a_wallbash_log.md` を追加する。適用対象環境: CLI | Phase 0 のステップに `00a_wallbash_log.md` への記録が含まれ、関連ファイル一覧に追記されていること | 🟡 | ⬜ |
| T-009 | `docs/workflow.md` の GHA Initiative フローセクションを更新する。壁打ちフェーズに `/continue` ループを追記し、壁打ちフェーズの成果物に `00a_wallbash_log.md`, `01_plan.md`, `02_tasks.md` を追記する | `docs/workflow.md` が新フロー（`/continue` による壁打ち反復）を反映していること | 🟡 | ⬜ |
| T-010 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-011 | 以下3領域のメタルール横断検証を実施し、結果を `04_work_report.md` に記録する: (1) メタルールフロー記述: 変更対象パスを参照しているスキル・エージェント定義のフロー記述が変更後の実態と一致しているか確認・修正 (2) workflow.md 同期: `docs/workflow.md` の該当セクションが変更内容と整合しているか確認・更新（T-009 で実施） (3) TG-008 基準連動: `triage-standard-policy/SKILL.md` のチェック基準が変更内容に対応しているか確認・更新 | 3領域の検証結果（合格/修正済/該当なし）が `04_work_report.md` に記載されている | 🔴 | ⬜ |
| T-012 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

### 評価ワーカー向け

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | 全変更ファイルの整合性を検証する: (1) `gha-wallbash/SKILL.md` の init/continue フローが `initiative-wallbash.yml` の inputs と対応していること (2) dispatcher の `/continue` routing が wallbash ワークフローの inputs に合致すること (3) execute の PR 作成ステップが wallbash からの PR 削除と整合すること (4) テンプレートの `00a_wallbash_log.md` が gha-wallbash スキルの参照と一致すること | 4項目の検証結果が `06_eval_report.md` に記載されている | 🔴 | ⬜ |
| T-E02 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E03 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-15
