# 作業レポート: CSV コンフリクト防止の仕組み構築

## サマリ

CSV マージコンフリクトを原理的に回避するため、個別 `.md` ファイルを正の情報源（Source of Truth）とし、CSV をスクリプトで自動生成する方式への移行を完了した。`scripts/generate-csvs.py`（生成）と `scripts/migrate-csv-to-md.py`（移行）を作成し、既存データの移行・ラウンドトリップ検証を実施した。PreToolUse hook による自動生成、スキルファイル 25 件 + テンプレート 1 件の CSV 参照更新、ドキュメント更新、メタルール横断検証を完了した。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | `issues/_template.md` に対応・クローズ情報セクション追加 | テンプレートに `## 対応・クローズ情報` セクション追加 | 完了 | 差異なし |
| T-002 | `scripts/generate-csvs.py` 新規作成 | Python stdlib のみで CSV 生成スクリプト作成 | 完了 | 機能: issues/backlog パース、`--check`、`--next-issue-id`、`--next-backlog-id` |
| T-003 | `scripts/migrate-csv-to-md.py` 新規作成 | CSV → .md 移行スクリプト作成 | 完了 | 51 件新規作成、12 件既存更新、14 件旧フォーマット変換（計画の 13 件 + BL-048） |
| T-004 | 移行実行・ラウンドトリップ検証 | 全 CSV 行に対応する .md 生成 + ラウンドトリップテスト | 完了 | 5 件の正当差異を確認（.md が権威ある情報源として CSV より新しいデータを持つケース） |
| T-005 | PreCommit hook 設定 | `.claude/settings.json` に hook 追加 | 完了 | `PreCommit` キーは無効 → `PreToolUse` + `Bash` matcher + shell script で実装 |
| T-006 | スキルファイル 25 件 + テンプレート 1 件の CSV 参照更新 | CSV 直接編集指示を .md 編集指示に更新 | 完了 | Python 一括置換スクリプト + 手動修正（l1-manager, manager-common-policy, triage-manager, gha-close） |
| T-007 | ドキュメント更新 | issues/README.md, backlog/README.md, docs/workflow.md, CLAUDE.md 更新 | 完了 | workflow.md は約 15 箇所の置換 |
| T-008 | メタルール横断検証 | 3 領域（フロー記述・workflow.md・TG-008 基準）の検証 | 完了 | gha-close に残存指示 1 件修正、workflow.md に残存参照 5 件修正。triage-standard-policy の「CSV転記」は概念名として許容 |
| T-009 | 知見記録 | 作業中の知見を記録 | 完了 | 下記「作業中の知見」セクション参照 |
| T-010 | 課題転記 | 07_issues.md の未転記課題確認 | 完了 | git push 403 エラーのみ記録 → 既知の環境制約（ISS-027 関連）につき転記不要 |

## 成果物一覧

- `scripts/generate-csvs.py` — CSV 自動生成スクリプト（issues + backlog）
- `scripts/migrate-csv-to-md.py` — CSV → .md 移行スクリプト（一度きり使用）
- `.claude/hooks/pre-commit-generate-csvs.sh` — PreToolUse hook 用シェルスクリプト
- `.claude/settings.json` — PreToolUse hook 設定追加
- `issues/entries/ISS-001.md` ～ `ISS-062.md` — 51 件新規作成、12 件既存更新
- `issues/_template.md` — 対応・クローズ情報セクション追加
- `backlog/entries/*.md` — 14 件旧フォーマット変換、3 件ステータス同期
- `.claude/skills/**/*.md` — 25 件の CSV 参照更新
- `sessions/initiatives/_template/07_issues.md` — テンプレート CSV 参照更新
- `issues/README.md`, `backlog/README.md`, `docs/workflow.md`, `CLAUDE.md` — ドキュメント更新

## 発生した課題

- git push 403 エラー（SDK 環境制約、ISS-027 関連）— 転記不要、L1 がプッシュ担当

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 発見元 | 対象ファイル・領域 | 詳細 |
|---|------|--------|-----------------|------|
| 1 | PreToolUse hook で git commit 前の自動処理を実現できる | T-005 | `.claude/settings.json` | `PreCommit` キーは Claude Code settings.json のスキーマに存在しない。代替として `PreToolUse` + `"matcher": "Bash"` を使い、hook スクリプト内で `git commit` コマンドかどうかを判定する方式が有効。今後同様の pre-commit 自動処理を追加する際の標準パターンとして利用可能 |
| 2 | .md テーブルパース時の HTML コメント除去が必要 | T-002, T-004 | `scripts/generate-csvs.py` | メタ情報テーブルの値に `<!-- 施策化時に L1 が記入する -->` のような HTML コメントが含まれるケースがある。`re.sub(r"<!--.*?-->", "", val).strip()` で除去しないと CSV に混入する |
| 3 | 旧フォーマット backlog の blockquote + table 混在パターンへの対応 | T-002, T-003 | `scripts/generate-csvs.py` | 一部のエントリが blockquote の BL ID とメタ情報テーブルの両方を持つ混在形式だった。パーサーは table → blockquote のフォールバック順で処理する設計が堅牢 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 | 背景・文脈 |
|---|------|--------|-----------|
| 1 | スキルファイル一括更新は Python スクリプトで置換パターンを定義して実行するのが効率的 | T-006 | 25 件のスキルファイルに対し、5 つの正規表現パターンで一括置換を実行した後、パターンに乗らないエッジケース（l1-manager の CSV ルーティング記述、manager-common-policy §6 の手順記述等）を手動修正した。一括 + 個別修正の2段階が現実的 |
| 2 | ラウンドトリップテストで「正当な差異」の判別基準が必要 | T-004 | 移行後に .md が権威ある情報源となるため、CSV と .md で差異があっても .md 側が正しい場合がある（例: ISS-048/051 のステータス修正、BL-002/020/031 のステータス同期）。テスト設計時に「差異＝バグ」ではなく「差異の正当性を判定する」観点が重要 |

## 所感・次フェーズへの申し送り

- 全 T-001 ～ T-010 を完了。主要な技術的ハードルは PreToolUse hook の実装方式（PreCommit 非対応 → PreToolUse + Bash matcher）とラウンドトリップテストの差異判定だった
- `scripts/migrate-csv-to-md.py` は一度きりの移行スクリプトであり、今後は不要。削除またはアーカイブを検討してよい
- `triage-standard-policy/SKILL.md` の「CSV転記」はプロセス概念名として残存しているが、実際の操作手順（manager-common-policy §6）は .md ベースに更新済みのため問題なし
- git push は SDK 環境の 403 制約によりブロック中。L1 がプッシュを担当する

---
**作成者**: L2（実施）
**作成日**: 2026-03-16
