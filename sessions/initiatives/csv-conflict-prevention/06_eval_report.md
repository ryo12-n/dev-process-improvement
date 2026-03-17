# 評価レポート: CSV コンフリクト防止の仕組み構築

## 評価サマリ

全成功基準 SC-1〜SC-7 を達成している。`scripts/generate-csvs.py` はエラーなく CSV を生成し、ラウンドトリップテスト（`--check`）も差分なしで合格した。issues/entries/ の .md ファイル数（64件）と CSV 行数（64行）が一致し、backlog も同様（82件/82行）。旧 CSV 直接編集指示は残存せず（残存参照はすべて読み取り専用または概念名）、PreToolUse hook が設定済み、ドキュメント3件も更新されている。メタルール横断検証も合格。次フェーズ（ゲート判定）への進行を推奨する。

## 評価結果

| # | 評価項目 | 判定基準 | 結果 | 判定 |
|---|---------|---------|------|------|
| E-1 | SC-1: CSV 生成スクリプト動作 | エラーなしで CSV 2 ファイル生成 | `python3 scripts/generate-csvs.py` 実行: `Generated: プロセス改善_課題管理.csv` / `Generated: backlog/backlog.csv` の 2 ファイル生成、エラーなし | ✅ |
| E-2 | SC-2: テンプレートの対応・クローズ情報セクション | `## 対応・クローズ情報` セクション存在、4 項目テーブル | `issues/_template.md` に `## 対応・クローズ情報` セクションが存在し、対応方針（確定）/ 確定日 / タスク化先 / 備考 の 4 項目テーブルあり | ✅ |
| E-3 | SC-3: .md ファイル数と CSV 行数の対応 | 全 CSV 行に対応する .md が存在 | issues: .md 64 件 = CSV 64 行。backlog: .md 82 件 = CSV 82 行。完全一致 | ✅ |
| E-4 | SC-4: ラウンドトリップテスト | `--check` が合格 | `python3 scripts/generate-csvs.py --check` 実行: `No changes detected.` — 差分なしで合格 | ✅ |
| E-5 | SC-5: 旧指示の残存チェック | CSV 直接編集指示が残存しない | `grep -r` で 17 件の参照を検出。全件を精査した結果: (1) metacognition-worker — 読み取り専用（分析対象） (2) triage-manager — 照合用の読み取り参照 (3) l1-manager — 関連ファイル一覧テーブル (4) backlog-maintenance-worker — 読み取り専用。「CSV に行を追加」「CSV へ転記」等の直接編集指示は 0 件 | ✅ |
| E-6 | SC-6: PreCommit hook 設定 | hook が設定され CSV 自動再生成が動作 | `.claude/settings.json` に `PreToolUse` + `Bash` matcher で `pre-commit-generate-csvs.sh` を設定済み。hook スクリプトは `git commit` コマンド検出時のみ CSV 再生成 + `git add` を実行する設計。計画時点の「PreCommit」キーは未対応だったため `PreToolUse` で代替実装 — 目的は達成 | ✅ |
| E-7 | SC-7: ドキュメント更新 | CSV 自動生成の旨が 3 ファイルに記載 | `issues/README.md`: .md が正の情報源、CSV は自動生成の旨を記載。`backlog/README.md`: CSV は自動生成、手動編集禁止を記載。`docs/workflow.md`: 課題管理フローが .md ベースに更新済み（9箇所以上で「CSV は自動生成」記述を確認） | ✅ |
| E-8 | メタルール横断検証 | 変更後の実態と一致 | (1) フロー記述: `triage-standard-policy/SKILL.md` の TG-008 不適合時アクションが `issues/entries/ISS-XXX.md` + 「CSV は自動生成」に更新済み (2) `docs/workflow.md`: 課題転記フローが .md ベースに更新済み (3) TG-008 基準: テンプレート・メタルール不整合の対応指示が .md 作成に更新済み | ✅ |

## 計画の成功基準に対する達成度

| 成功基準 | 達成度 | 根拠 |
|---------|--------|------|
| SC-1: CSV 生成スクリプト動作 | 達成 | エラーなしで issues + backlog の 2 CSV を生成。`--next-issue-id`（ISS-065）、`--next-backlog-id` も動作確認済み |
| SC-2: テンプレート拡張 | 達成 | `issues/_template.md` に 4 項目の対応・クローズ情報テーブルが存在 |
| SC-3: 既存データ移行 | 達成 | issues 64 件 = CSV 64 行、backlog 82 件 = CSV 82 行で完全一致 |
| SC-4: ラウンドトリップテスト | 達成 | `--check` で差分なし（`No changes detected.`） |
| SC-5: スキルファイル更新 | 達成 | 残存参照 17 件を全件精査し、CSV 直接編集指示は 0 件。全て読み取り専用または概念名 |
| SC-6: PreCommit hook 設定 | 達成 | `PreToolUse` + `Bash` matcher + shell script で実装。計画の `PreCommit` キー非対応を代替方式で解決 |
| SC-7: ドキュメント更新 | 達成 | issues/README.md, backlog/README.md, docs/workflow.md の 3 ファイルが CSV 自動生成の旨に更新済み |

## 発見された課題・改善提案

評価の結果、成功基準をブロックする課題は発見されなかった。以下は改善提案として記録する。

- **改善提案 1**: `pre-commit-generate-csvs.sh` の `jq` フォールバック（grep による command 抽出）は、JSON 値にエスケープ文字を含む場合に誤動作する可能性がある。現状では実害はないが、将来的に jq を前提条件とするか、Python ベースの JSON パーサーに置き換えることを検討してよい（施策内で完結する軽微な改善のため転記不要）

#### 実施ワーカー未転記課題
- **件数**: 0 件
- **課題一覧**: `07_issues.md` に未転記課題なし（SDK 環境 git push 403 エラーは「転記不要」判定済み）
- **対応依頼**: なし

## 評価中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | PreToolUse hook の `Bash` matcher は PreCommit の代替として機能するが、全 Bash コマンドにフックが発火するため hook スクリプト側で対象コマンドのフィルタリングが必要 | E-6 検証 | `.claude/settings.json`, `.claude/hooks/` | 今後の hook 追加時に「matcher 粒度とスクリプト側フィルタの設計パターン」としてルール化を検討できる。現在の `pre-commit-generate-csvs.sh` の `git commit` 判定パターンが参考実装になる |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | SC-5 の「旧指示残存チェック」は grep 結果の件数だけでなく、各参照の文脈（読み取り専用 / 概念名 / 直接編集指示）を判別する必要がある | E-5 検証 | 17 件の grep ヒットのうち直接編集指示は 0 件だった。件数だけで判定すると false positive になるため、評価基準に「文脈判別」を含めることが重要 |

## 次フェーズへの推奨

**進めるべき**。全成功基準 SC-1〜SC-7 を達成しており、メタルール横断検証も合格。未解決の課題は発見されなかった。ゲート判定に進むことを推奨する。

---
**作成者**: L2（評価）
**作成日**: 2026-03-16
