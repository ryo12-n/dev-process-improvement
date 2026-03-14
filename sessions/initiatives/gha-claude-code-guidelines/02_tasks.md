# タスクリスト: GHA-Claude-Code運用ガイドライン策定

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 実施ワーカー（l2-worker）タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | ガイドラインスキル `.claude/skills/gha-guideline/SKILL.md` を作成する。frontmatter に `user-invocable: false` を設定し、以下の5セクションを記載する: (1) 権限3層モデル（GHA permissions / Claude Code allow / プロンプト指示の対応関係テーブルと整合性チェックポイント）、(2) 設計判断基準: Claude委任 vs shellステップ（判断フロー）、(3) Claude Code 権限設定パターン（Action の settings JSON 形式 / CLI の --allowedTools 形式、最小権限の原則、ツール別リスクレベル）、(4) gh コマンド前提条件チェックリスト（コマンド別の前提条件・エラーパターン・回避策）、(5) 既存ワークフロー権限マトリクス（4ワークフローの現状整理） | 5セクションすべてが記載されている。frontmatter に `user-invocable: false` と適切な `description` が設定されている | 🔴 | ⬜ |
| T-002 | `.github/workflows/daily-triage.yml` の `--dangerously-skip-permissions` を適切な権限設定に置換する。triage.md プロンプトの操作内容から必要なツールを導出し、`--allowedTools` フラグで設定する。参考: Read, Write, Edit, Glob, Grep, Bash(cp *), Bash(mkdir *), Bash(rm *), Bash(ls *) 等が必要。`Bash(git *)` と `Bash(gh *)` は不要（git 操作は workflow の shell ステップで実行）。CLI の `--allowedTools` 書式は Claude Code CLI ドキュメントで確認すること | `--dangerously-skip-permissions` がワークフロー内に残っていない。`--allowedTools` で必要十分なツールが列挙されている。適用対象環境: CLI（GHA 上の CLI 実行） | 🔴 | ⬜ |
| T-003 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-004 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

## 評価ワーカー（l2-evaluator）タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| E-001 | ガイドラインスキルの網羅性・正確性を評価する。5セクションの各項目が正確かつ実用的であるかを確認する | 評価結果が `06_eval_report.md` に記載されている | 🔴 | ⬜ |
| E-002 | daily-triage.yml の allow リストが過不足ないか検証する。`.github/prompts/triage.md` の全操作を列挙し、allow リストの各エントリと突合する。不足ツール・過剰ツールがないか確認する | 突合結果が `06_eval_report.md` に記載されている。過不足がある場合は具体的な指摘がある | 🔴 | ⬜ |
| E-003 | 権限3層整合性チェックを実施する。daily-triage.yml について GHA permissions × allow リスト × プロンプト指示の3層が整合しているか確認する | 3層整合性チェック結果が `06_eval_report.md` に記載されている | 🔴 | ⬜ |
| E-004 | 評価中に発見した知見を `06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| E-005 | 評価中に新たに発見した課題を `07_issues.md` へ起票し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-14
