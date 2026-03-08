# 作業レポート: ルール変更連動更新標準化

## サマリ

T-001〜T-010 の全10タスクを完了した。7つのスキル/エージェント定義ファイルに「関連ファイル一覧」セクションを追加し、ルール変更時の連動更新チェックリスト（docs/rule-change-checklist.md）を新規作成、docs/workflow.md にチェックリスト参照を追記した。triage-manager/SKILL.md に既にあった「関連ファイル一覧」パターンを横展開する形で、全スキル/エージェント定義の連動更新先が明示された。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | 参照関係調査 | 7ファイル分の調査 | 7ファイル分完了 | 順方向参照・逆方向参照・テンプレート対応の3軸で調査 |
| T-002 | l1-manager/SKILL.md | セクション追加 | 7件の連動更新先を記載 | 差異なし |
| T-003 | l2-worker.md | セクション追加 | 7件の連動更新先を記載 | 差異なし |
| T-004 | l2-evaluator.md | セクション追加 | 7件の連動更新先を記載 | 差異なし |
| T-005 | triage-worker.md | セクション追加 | 5件の連動更新先を記載 | 差異なし |
| T-006 | triage-evaluator.md | セクション追加 | 5件の連動更新先を記載 | 差異なし |
| T-007 | triage-standard-policy/SKILL.md | セクション追加 | 8件の連動更新先を記載 | 差異なし |
| T-008 | session-flow-policy/SKILL.md | セクション追加 | 9件の連動更新先を記載 | 差異なし |
| T-009 | rule-change-checklist.md 作成 | チェックリスト作成 | 5項目のチェックリスト作成 | 統合元4件の要件をすべて反映 |
| T-010 | workflow.md 更新 | チェックリスト参照追記 | セクション追加完了 | 差異なし |

## 成果物一覧

- `.claude/skills/l1-manager/SKILL.md` -- 関連ファイル一覧セクション追加
- `.claude/skills/l1-manager/agents/l2-worker.md` -- 関連ファイル一覧セクション追加
- `.claude/skills/l1-manager/agents/l2-evaluator.md` -- 関連ファイル一覧セクション追加
- `.claude/skills/triage-manager/agents/triage-worker.md` -- 関連ファイル一覧セクション追加
- `.claude/skills/triage-manager/agents/triage-evaluator.md` -- 関連ファイル一覧セクション追加
- `.claude/skills/triage-standard-policy/SKILL.md` -- 関連ファイル一覧セクション追加
- `.claude/skills/session-flow-policy/SKILL.md` -- 関連ファイル一覧セクション追加
- `docs/rule-change-checklist.md` -- 新規作成
- `docs/workflow.md` -- ルール変更時の連動更新セクション追加

## 発生した課題

なし（07_issues.md への起票なし）

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 「関連ファイル一覧」セクションは連動更新先の件数がファイルによって大きく異なる（5〜9件） | 全スキル/エージェント定義 | ポリシー系ファイル（session-flow-policy, triage-standard-policy）は横断的に多くのファイルに影響するため連動更新先が多い。エージェント定義（worker/evaluator）は比較的少ない。ルール変更施策ではポリシー系ファイルの変更を特に注意すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | triage-manager/SKILL.md の「関連ファイル一覧」は既にテンプレート（triage/_template/）との対応関係も含んでおり、良い参考パターンだった | 横展開時にこのパターンを踏襲し、イニシアティブ系ではinitiatives/_template/との対応を、トリアージ系ではtriage/_template/との対応を記載した |

## 所感・次フェーズへの申し送り

- 全タスクが計画通り完了。調査（T-001）で得た参照関係データに基づいて各ファイルに正確な連動更新先を記載できた
- チェックリスト（T-009）は統合元4件の backlog 要件（workflow.md更新、TG-008基準連動更新、関連ファイル一覧確認、定型パターン）をすべてカバーしている
- 評価者による検証（T-012: Grep等による機械的検証）で参照関係の正確性を確認することを推奨

---
**作成者**: L2（実施）
**作成日**: 2026-03-07
