# 作業レポート: builtin-skills-evaluation

## サマリ

Claude Code のビルトイン skills 5件（/simplify, /batch, /debug, /loop, /claude-api）を公式ドキュメントに基づいて評価し、dev-process-improvement プロジェクトでの適用可能性を明確化した。全5件のうち積極活用を推奨するものはなく、/debug と /batch を状況に応じて活用する方針を策定した。評価結果を `.claude/skills/builtin-skills-reference/SKILL.md` に配置し、`docs/workflow.md` を連動更新した。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | 5つのビルトイン skills の評価 | Web 検索で公式ドキュメントを参照し、各 skill を4段階で評価 | 公式ドキュメント（https://code.claude.com/docs/en/skills）を参照し、全5件を評価。/batch, /debug の存在も確認 | 差異なし。/batch, /debug はビルトインとして存在を確認 |
| T-002 | SKILL.md 作成 | frontmatter + 4セクション構成 | 指定の frontmatter と構成で作成。各 skill に機能概要・適用可能性・具体的利用シーン・制約事項を記載 | 差異なし |
| T-003 | workflow.md 連動更新 | skills 一覧セクションに追記 | 「フォーマット変換時の同等性検証」セクション直後に新セクション追加。正の情報源表記・評価サマリー・総合方針を記載 | 差異なし |
| T-004 | 作業中の知見記録 | 04_work_report.md に知見セクション記載 | 本レポートに記載 | 差異なし |
| T-005 | 課題 CSV 転記 | 07_issues.md の課題を確認し転記判断 | 1件の知見メモあり、転記不要と判断 | 施策横断の課題は発生せず |

## 成果物一覧
- `.claude/skills/builtin-skills-reference/SKILL.md`（新規作成）
- `docs/workflow.md`（連動更新）
- `sessions/initiatives/builtin-skills-evaluation/03_work_log.md`（作業履歴）
- `sessions/initiatives/builtin-skills-evaluation/07_issues.md`（課題メモ）

## 発生した課題
- 施策横断の課題は発生しなかった
- 07_issues.md に1件の知見メモを記録（転記不要判断済み）

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | ビルトイン skills 評価は新プロジェクト立ち上げ時のチェックリスト項目にすべき | `.claude/skills/builtin-skills-reference/SKILL.md` | ビルトイン skills の適用可能性はプロジェクト特性（コード主体 vs 文書主体）に強く依存する。プロジェクト開始時に一度評価しておくことで、不要な試行錯誤を避けられる。ただし現時点で本リポジトリのみの運用であり、ルール化の優先度は低い |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | Claude Code のビルトイン skills は slash commands が skills に統合された結果（v2.1.3）であり、今後も新しいビルトイン skill が追加される可能性がある | 公式ドキュメントの記述と Web 検索結果から。/simplify, /batch, /debug, /loop, /claude-api の5件が2026-03-12時点の全ビルトイン skills。バージョンアップ時に再評価が必要 |
| 2 | `user-invocable: false` の skill は description がコンテキストに常時ロードされるが、full content は必要時のみロードされる | 公式ドキュメントの skill invocation control セクションから。builtin-skills-reference の設計判断（user-invocable: false）が適切であることを確認 |

## 所感・次フェーズへの申し送り
- 本施策は調査・評価・文書化が中心の小規模施策であり、計画通りに完了した
- ビルトイン skills の再評価タイミング（Claude Code メジャーバージョンアップ時等）を SKILL.md に明記済み
- ai-driven-dev-patterns リポジトリでは /claude-api や /simplify の活用可能性が高い可能性があるが、本施策のスコープ外

---
**作成者**: L2（実施）
**作成日**: 2026-03-12
