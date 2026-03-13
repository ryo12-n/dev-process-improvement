# タスクリスト: automation-managerセッション作成

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `automation-candidates/` 管理ディレクトリ作成: README.md, automation-candidates.csv, _template.md, entries/ を作成。先行施策の R-001〜R-014 を AC-001〜AC-014 として entries/ に移行し CSV に登録 | ディレクトリ構造が完成し、14件の初期データが CSV と entries に登録されている | 🔴 | ⬜ |
| T-002 | `.claude/skills/automation-manager/SKILL.md` 作成: backlog-maintenance-manager を参照実装として AT-001〜AT-004 のタスク定義、セット数判断基準、8ステップワークフロー、出力先ガイドライン等を含める | session-flow-policy §2 の必須要素をすべて含み、backlog-maintenance-manager と同等の構成品質 | 🔴 | ⬜ |
| T-003 | `.claude/skills/automation-manager/agents/automation-worker.md` 作成: AT-001〜AT-004 の走査手順、壁打ちフェーズ、スキャンレポート構成、停止ルール、対称性テーブルを含める | session-flow-policy §3 の必須要素をすべて含み、evaluator との対称性が確保されている | 🔴 | ⬜ |
| T-004 | `.claude/skills/automation-manager/agents/automation-evaluator.md` 作成: 評価基準(4観点)、壁打ちフェーズ、評価レポート構成、停止ルール、対称性テーブルを含める | session-flow-policy §3 の必須要素をすべて含み、worker との対称性が確保されている | 🔴 | ⬜ |
| T-005 | `sessions/automation/_template/` 作成: backlog-maintenance テンプレートを参考にマネージャー用5ファイル + workers/_template/ 7ファイル | triage/backlog-maintenance テンプレートと同等の構成が揃っている | 🔴 | ⬜ |
| T-006 | `.claude/rules/commit-message.md` 更新: 非施策作業セクションに `[auto-mgr]`, `[auto-worker]`, `[auto-eval]` を追加 | 3つのプレフィックスが既存パターンと同じ形式でテーブルに追加されている | 🔴 | ⬜ |
| T-007 | `.claude/skills/triage-standard-policy/SKILL.md` 更新: ライフサイクル適用マトリクスに automation 系3行追加。ペアリング要件にも追加 | 適用マトリクスに3行追加、ペアリング構造テーブルに1ペア追加 | 🔴 | ⬜ |
| T-008 | `docs/workflow.md` 更新: automation セッションフローの記述を追加 | 既存セッションタイプと同等の詳細度で記述されている | 🔴 | ⬜ |
| T-009 | 知見記録（固定タスク）: 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録 | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-010 | メタルール横断検証（固定タスク）: `.claude/skills/`, `.claude/rules/` 配下の変更に対し、(1)メタルールフロー記述整合、(2)workflow.md同期、(3)TG-008基準連動 の3領域を検証 | 3領域の検証結果が `04_work_report.md` に記載されている | 🔴 | ⬜ |
| T-011 | 課題転記（固定タスク）: `07_issues.md` の未転記課題を `プロセス改善_課題管理.csv` へ転記 | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

## タスク実行順序

T-001 → T-002 → T-003, T-004（並行可） → T-005 → T-006, T-007, T-008（並行可） → T-009, T-010, T-011

## ワーカー成果物確認観点

- session-flow-policy §5.1 チェックリスト充足
- AC-001〜AC-014 が先行施策 R-001〜R-014 と1対1対応
- backlog-maintenance-manager との構成一貫性
- ワーカー・評価者のペアリング対称性

---
**作成者**: L1
**最終更新**: 2026-03-13
