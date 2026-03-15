# 評価レポート: GHA 壁打ちフェーズの独立・反復化

## 評価サマリ

全4項目の整合性検証を実施した結果、gha-wallbash スキルと initiative-wallbash.yml の init/continue フロー対応、dispatcher の `/continue` routing、execute の PR 作成ステップ移動、テンプレートとスキルの参照一致のいずれも整合しており、01_plan.md の成功基準7項目は全て達成されている。メタルール横断検証でも新たな不整合は検出されなかった。次フェーズへの進行を推奨する。

## 評価結果

| # | 評価項目 | 判定基準 | 結果 | 判定 |
|---|---------|---------|------|------|
| 1 | gha-wallbash/SKILL.md の init/continue フローと initiative-wallbash.yml の inputs の対応 | init で issue_number のみ必須、continue で mode/feedback/initiative_dir/branch が使用。フローが YAML の条件分岐と整合 | init: YAML の `mode` デフォルト `init`、`issue_number` 必須。スキルのステップ1（`/tmp/issue_body.txt` 読み取り）は YAML の `Extract initiative info` ステップで保存済み。continue: YAML に `mode=continue` 時の既存ブランチチェックアウトステップ（L46-51）、フィードバック保存ステップ（L69-72）が存在し、スキルのステップ1-2（`00a_wallbash_log.md` 読み取り、`/tmp/feedback.txt` 読み取り）と一致。YAML の env で `WALLBASH_MODE` と `INITIATIVE_DIR` がスキルに渡される | ✅ |
| 2 | dispatcher の `/continue` routing と wallbash ワークフローの inputs の合致 | 4つの inputs が全て正しく渡され、wallbashing 以外でエラー | dispatcher L149-165: `PHASE=wallbashing` を条件とし、`META_FOUND=true` を確認後、`initiative-wallbash.yml` に `issue_number`, `mode=continue`, `feedback=$ARGS`, `initiative_dir=$INITIATIVE_DIR`, `branch=$BRANCH` の5つを渡す。wallbash.yml の input 定義と完全一致。wallbashing 以外のフェーズではエラーメッセージ「`/continue` は `initiative:wallbashing` フェーズでのみ使用できます」が返る | ✅ |
| 3 | execute の PR 作成ステップと wallbash の PR 削除の整合 | wallbash に PR 作成なし、execute に phase=wallbashing 条件の PR 作成あり | wallbash.yml: 全ステップを確認し PR 作成ステップは存在しない。スキルの「やらないこと」に「PR の作成（`/approve` 時に `initiative-execute.yml` が担当する）」と明記。execute.yml L61-103: `if: inputs.phase == 'wallbashing'` 条件の「Create PR (wallbashing to executing transition)」ステップが存在し、既存 PR チェック（L73-78）、PR body のフェーズ進捗テーブル（L83-96）を含む | ✅ |
| 4 | テンプレート 00a_wallbash_log.md と gha-wallbash スキルの参照の一致 | テンプレートにスキルが期待する2セクション構造が存在 | テンプレート: 「現在の合意事項」セクション（施策の目的/スコープ/計画の方向性/未解決事項の4サブセクション）と「イテレーション履歴」セクション（Round N: 入力/調査・推論/更新内容/合意事項の変更）が存在。スキル init ステップ4: 「現在の合意事項」セクションに目的・スコープ・計画の方向性・未解決事項を記載、「イテレーション履歴」に Round 1 を追記と記述 -- テンプレートと完全一致。テンプレートのヘッダーにも `gha-wallbash/SKILL.md` への参照あり | ✅ |
| 5 | メタルール横断検証（評価者側） | 3領域で不整合なし | (1) フロー記述整合性: `docs/workflow.md` の GHA Initiative スキル一覧テーブル（L447-454）に `gha-wallbash` の description が「壁打ちフェーズ（init: テンプレートコピー・ドラフト作成 / continue: フィードバック反映・ドラフト更新）」と記載され、SKILL.md の description と一致。GHA Initiative フロー図（L458-484）に `/continue` ループが追記済み。壁打ちフェーズ成果物テーブル（L486-493）に 00a_wallbash_log.md を含む4ファイルが記載済み。(2) workflow.md 同期: T-009 で更新済み、評価時点で乖離なし。(3) TG-008 基準連動: GHA スキルは TG-008 走査対象外（実施ワーカーの判断と一致） | ✅ |
| 6 | 01_plan.md 成功基準7項目の達成度 | 全7項目達成 | 下記「計画の成功基準に対する達成度」セクション参照 | ✅ |

## 計画の成功基準に対する達成度

| 成功基準 | 達成度 | 根拠 |
|---------|--------|------|
| 1. `00a_wallbash_log.md` が存在し所定の構造を持つ | 達成 | テンプレートに「現在の合意事項」「イテレーション履歴」の2セクション構造が存在。L1 が事前作成済みで構造を確認 |
| 2. `gha-wallbash/SKILL.md` が init/continue の2モードを定義 | 達成 | SKILL.md に「init モード（mode=init）」「continue モード（mode=continue）」の2つの作業フローが詳細に記載 |
| 3. `initiative-wallbash.yml` が mode, feedback, branch, initiative_dir の inputs を持ち、mode=continue 時に既存ブランチをチェックアウト | 達成 | YAML L4-30 に4つの inputs が定義（mode: デフォルト `init`、feedback/initiative_dir/branch: オプション）。L45-51 に `if: inputs.mode == 'continue'` の既存ブランチチェックアウトステップが存在 |
| 4. `initiative-dispatcher.yml` が `/continue` を `initiative:wallbashing` フェーズで受け付け wallbash にルーティング | 達成 | L149-165 に `continue` ケースが追加され、`PHASE=wallbashing` を条件に `initiative-wallbash.yml` を dispatch。フェーズ不一致時はエラーメッセージを返す |
| 5. `initiative-execute.yml` が `phase=wallbashing` 時に PR を作成するステップを持つ | 達成 | L61-103 に「Create PR (wallbashing to executing transition)」ステップが `if: inputs.phase == 'wallbashing'` 条件で追加。既存 PR チェック付き |
| 6. `gha-execute/SKILL.md` が壁打ちドラフト（01/02）を活用する記述を持つ | 達成 | SKILL.md の /approve フローのステップ3 に「既存の壁打ちドラフト（`01_plan.md`, `02_tasks.md`）を読み取る」と記載。ドラフト存在/不存在の2分岐（活用 or ゼロから作成）が明記 |
| 7. `docs/workflow.md` が新フロー（`/continue` ループ）を反映 | 達成 | workflow.md L457-484 に GHA Initiative フロー図が追加。`/continue <feedback>` のループフロー、壁打ちフェーズ成果物テーブル、コンテキスト保持の仕組みが記載 |

## 発見された課題・改善提案

### 新規発見課題
- GHA-EVAL-001: initiative-wallbash.yml の prompt ブロック内で `${{ inputs.feedback }}` が直接展開されている（L141 の execute.yml も同様）。`workflow_dispatch` トリガーのため外部入力の直接注入リスクは低いが、`${{ }}` 式を `run:` ブロック外（`with.prompt:` 内）で使用している点は、gha-workflow-security ルールの趣旨（インジェクション防止）との関係で注意が必要。ただし `prompt:` は YAML string input でありシェルコマンドとして実行されないため、実質的なセキュリティリスクはない → 転記不要（施策スコープ外、参考情報として記録）

### 実施ワーカーの未転記確認
- 07_issues.md に1件の未転記課題あり（gha-skills-mapping.yml に initiative 系ワークフローのマッピングが未登録）
- 実施ワーカーが「転記不要」と判断済み（理由: 本施策スコープ外であり、変更前から存在していた問題）
- 判断は妥当。未転記ではなく「転記不要」の判断が付いている

## 評価中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA ワークフロー間で責務移動（PR 作成等）を行う際は、移動元の削除確認と移動先の条件付きステップ追加を対で検証すべき | `.github/workflows/` | 本施策では wallbash から execute への PR 作成責務移動が行われた。評価時に「移動元に残存がないか」「移動先の条件（`if: inputs.phase == 'wallbashing'`）が正しいか」の対検証が有効だった。GHA ワークフロー変更施策の評価項目テンプレートに「責務移動の対検証」を含めることを推奨 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | `with.prompt:` 内の `${{ }}` 展開はシェルインジェクションのリスクにはならないが、プロンプトインジェクションの経路にはなりうる | initiative-wallbash.yml / initiative-execute.yml の `prompt:` ブロックで `${{ inputs.feedback }}` 等を直接展開している。`workflow_dispatch` トリガーのため入力は信頼されたソース（dispatcher 経由）からだが、将来的に入力経路が変わった場合はリスクになりうる |

## 次フェーズへの推奨

**進めるべき**。全4項目の整合性検証に合格し、01_plan.md の成功基準7項目を全て達成している。メタルール横断検証でも新たな不整合は検出されなかった。実施ワーカーのメタルール横断検証で発見・修正された gha-guideline/SKILL.md と workflows/README.md の連動更新も適切に行われている。

---
**作成者**: L2（評価）
**作成日**: 2026-03-15
