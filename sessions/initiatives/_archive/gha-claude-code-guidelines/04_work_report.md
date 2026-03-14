# 作業レポート: GHA-Claude-Code運用ガイドライン策定

## サマリ

GHA × Claude Code ワークフローの権限設計リファレンススキル（`.claude/skills/gha-guideline/SKILL.md`）を5セクション構成で作成し、`daily-triage.yml` の `--dangerously-skip-permissions` を `--allowedTools` による最小権限設定に置換した。既存4ワークフローの実際の設定を調査・整理し、設計判断の根拠をガイドラインに記載した。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | ガイドラインスキル SKILL.md 作成 | 5セクション記載 | 5セクション記載完了 | 差異なし |
| T-002 | daily-triage.yml 権限置換 | `--dangerously-skip-permissions` → `--allowedTools` | 置換完了、grep 確認済み | 差異なし |
| T-003 | 知見記録 | ルール化候補・参考情報各1行以上 | 各2行記載 | 差異なし |
| T-004 | 課題転記 | 未転記課題の転記判断 | 施策をまたぐ課題なし。転記対象なし | 課題が発生しなかったため転記作業は不要 |

## 成果物一覧
- `.claude/skills/gha-guideline/SKILL.md`（新規作成）
- `.github/workflows/daily-triage.yml`（更新: 権限設定置換）
- `03_work_log.md`（作業履歴記録）
- `04_work_report.md`（本ファイル）

## 発生した課題
- なし（`07_issues.md` への起票なし）

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | CLI の `--allowedTools` はスペース区切りで複数指定可能。`Bash(command *)` のようなパターンはシェルの glob 展開を避けるためクォートが必要 | `.github/workflows/` | `--allowedTools "Read" "Write" "Bash(cp *)"` のように各ツールを個別にクォートする形式が安全。YAML の `|` ブロック内でも展開リスクがあるため注意 |
| 2 | git/gh 操作を Shell ステップに分離する設計パターンは、Claude Code のツール許可を最小化できるため、固定パターンの操作では標準化すべき | `.github/workflows/`, `.claude/skills/gha-guideline/SKILL.md` | daily-triage.yml は commit/push/PR作成がすべて固定パターンのため Shell ステップで実行しており、Claude には Bash(git/gh *) を許可する必要がない。この判断基準をガイドラインのセクション2に明文化した |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | triage.md プロンプトに「コミット不要」の制約が明記されていることが、Bash(git *) 除外の根拠として機能した | プロンプト（L3）の制約が L2（ツール許可）の設計判断を裏付ける。3層モデルの整合性確認において、プロンプトの制約事項を先に確認する手順が有効 |
| 2 | `backlog-auto-execute.yml` は Action の settings JSON、`daily-triage.yml` は CLI の `--allowedTools` と、同リポジトリ内で2つの方式が共存している | 方式の違いは Claude Code の呼び出し方（Action vs CLI）に依存する。統一する必要はないが、ガイドラインで両方のパターンを記載する必要がある |

## 所感・次フェーズへの申し送り
- T-001 の5セクションは既存ワークフローの実際の設定を参照して作成したため、正確性は高いと考える
- T-002 の `--allowedTools` リストは triage.md の操作内容から導出した。評価フェーズ（E-002）で triage.md の全操作との突合検証を推奨
- `Bash(cat *)` や `Bash(date *)` など、triage.md で明示的には使用しないが暗黙的に必要になる可能性のあるコマンドについて、評価者による検証が望ましい

---
**作成者**: L2（実施）
**作成日**: 2026-03-14
