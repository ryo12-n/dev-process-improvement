# 評価レポート: initiative-dispatcher

## 評価サマリ

L2-worker の作業成果は `01_plan.md` の成功基準5項目のうち4項目を完全に達成し、1項目（成功基準2: ルーティングの正しい動作）はコードレビューベースでは合格と判定するが、`dispatch_inputs` の JSON 構築にシェルインジェクションのリスクがあり、条件付き合格とする。全体として施策の目的は達成されているが、セキュリティ課題の対処を推奨する。

## 評価結果

| # | 評価項目 | 判定基準 | 結果 | 判定 |
|---|---------|---------|------|------|
| E-001 | `issue_comment` トリガーの排他性 | `initiative-dispatcher.yml` のみが `issue_comment` トリガーを持つこと | Grep で全 initiative 関連 `.yml` を検索し、`initiative-dispatcher.yml` のみが `issue_comment` を持つことを確認 | PASS |
| E-002 | ルーティングテーブルの完全性 | 5パターン全てが正しいラベル条件・起動先で実装されていること | `/start`(initiative なし→wallbash), `/approve`(wallbashing→execute), `/reject`(gate-review→execute), `/approve`(gate-review→close), `/question`(initiative あり→question) の5パターンが case 文で正しく実装されている | PASS |
| E-003 | フェーズ不一致エラーハンドリング | 全コマンドでフェーズ不一致時にエラーコメントが返ること | `/start`(既存initiative時), `/approve`(不正フェーズ時), `/reject`(非gate-review時), `/question`(非initiative時), 不明コマンド時 の全パターンでエラーメッセージが定義されている | PASS |
| E-004 | `backlog-to-issue.yml` の直接 dispatch | Issue 作成後に wallbash を直接 dispatch し、`initiative-start` ラベル付与が除去されていること | diff で確認: `--label "initiative-start"` が除去され、`Dispatch wallbash workflow` ステップで `gh workflow run initiative-wallbash.yml` が実行されている。`actions: write` パーミッション追加も確認 | PASS |
| E-005 | `initiative-start` ラベルの完全廃止 | ワークフロー `.yml` ファイル内に `initiative-start` への参照がないこと | Grep で全 `.yml` ファイルを検索し、該当なしを確認 | PASS |
| E-006 | `@ai-task` 形式の統一 | 全ての次ステップ案内が `@ai-task /command` 形式であること | wallbash の次ステップ案内（`@ai-task /approve`）、wallbash の PR body（`@ai-task /approve`）、execute の次ステップ案内（`@ai-task /approve`, `@ai-task /reject`）が全て `@ai-task` 形式であることを確認 | PASS |
| E-007 | 既存 Claude プロンプトの非変更 | トリガー・入力部分のみ変更され、プロンプトの趣旨・指示内容が維持されていること | git diff で wallbash / execute / close の変更を精査。変更はトリガー定義、`if:` 条件、issue 番号参照の `inputs.issue_number` 化、コメントパース処理の除去、次ステップ案内の `@ai-task` 化に限定。Claude プロンプトの指示内容は維持されている | PASS |
| E-008 | シェルインジェクションリスク | ユーザー入力が JSON 構築に直接展開される箇所でインジェクションリスクがないこと | `ARGS` 変数（ユーザーコメントから抽出）が `dispatch_inputs` の JSON 文字列内にエスケープなしで直接展開されている（例: `"feedback\":\"${ARGS}\"`）。さらに `eval gh workflow run` で実行されるため、`ARGS` に `"`, `\`, `$()`, バッククォート等を含む入力でシェルインジェクションが成立する可能性がある | FAIL |
| E-009 | 作業レポートの完全性 | 全タスクの実績・成果物一覧・知見が記載されていること | T-001〜T-008 の実績、成果物一覧6件、知見（ルール化候補1件、参考情報1件）が全て記載されている | PASS |
| E-010 | 課題メモの適切性 | 全課題に転記判断が付いていること | 1件の施策内課題（README 更新）に「転記不要」の判断が付いている | PASS |

## 計画の成功基準に対する達成度

| 成功基準 | 達成度 | 根拠 |
|---------|--------|------|
| 1. `issue_comment` トリガーを持つ initiative 関連ワークフローが `initiative-dispatcher.yml` のみ | 達成 | E-001 で確認。wallbash/execute/close から `issue_comment` が除去されている |
| 2. `@ai-task /command` 形式で全フェーズのルーティングが正しく動作すること | 条件付き達成 | E-002, E-006 はPASS。ルーティングロジックは正しいが、E-008 のインジェクションリスクにより `feedback` を含むコマンド（`/approve <フィードバック>`、`/reject <フィードバック>`）で予期しない動作が発生する可能性がある |
| 3. フェーズ不一致時にディスパッチャーがエラーコメントを返すこと | 達成 | E-003 で全パターンのエラーハンドリングを確認 |
| 4. `backlog-to-issue.yml` が Issue 作成後に wallbash を直接 dispatch すること | 達成 | E-004 で diff による確認済み |
| 5. `initiative-start` ラベルがトリガーとして使用されていないこと | 達成 | E-005 で全 `.yml` ファイルを検索し、該当なしを確認 |

## 発見された課題・改善提案

### 評価で発見した課題

1. **[E-008] `dispatch_inputs` のシェルインジェクションリスク** — `initiative-dispatcher.yml` の Route command ステップで、ユーザーのコメント本文から抽出した `ARGS` を JSON 文字列に直接展開している（例: 行110 `"feedback\":\"${ARGS}\"`）。さらに Dispatch workflow ステップで `eval gh workflow run "$WORKFLOW" $input_flags` を使用している（行162）。`ARGS` に `"`, `\`, `$()`, バッククォート等が含まれる場合に JSON 破壊やシェルインジェクションが成立する。対策として `jq` による JSON エスケープの使用と `eval` の回避を推奨する。

### 実施ワーカー未転記課題

- **件数**: 0件
- 実施ワーカーが起票した1件の課題（README 更新）は「転記不要」の判断が適切に付与されており、施策内で完結する修正のため転記は不要。

## 評価中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | ワークフローでのユーザー入力のエスケープ | `.github/workflows/` 全般 | `issue_comment` 経由で受け取るユーザー入力を shell 変数やJSON に展開する際、`jq` によるエスケープ（`jq -Rn --arg v "$VAR" '$v'`）を必須とするルール。`eval` の使用も禁止すべき。GitHub Actions のワークフロー作成ガイドラインとして定めることで、今後の同種リスクを防止できる |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | `gh workflow run` は `-f key=value` 形式で inputs を個別指定できるため、JSON 構築→パースの間接方式を取らずに直接 `-f` フラグを構築すれば `eval` が不要になる | ディスパッチャーが JSON をビルドして `jq` でパースし直し `eval` で展開するという3段階の処理を行っているが、最初からコマンド別に `-f` フラグを直接構築する方式に変更すれば、JSON エスケープ問題と `eval` リスクの両方を解消できる |

## 次フェーズへの推奨

**条件付きで進める**: 施策の主目的（Skipped ラン排除・コマンド体系統一・ディスパッチャーパターン導入）は達成されている。ただし、E-008 のシェルインジェクションリスクはデプロイ前に修正すべきである。修正は `dispatch_inputs` の JSON 構築を `jq` ベースのエスケープに変更する、または各コマンド分岐で `-f` フラグを直接構築する方式への変更が推奨される。修正範囲は `initiative-dispatcher.yml` の Route command ステップと Dispatch workflow ステップに限定されるため、手戻りではなく追加修正として対処可能。

---
**作成者**: L2（評価）
**作成日**: 2026-03-15
