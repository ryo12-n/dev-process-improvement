# 評価計画: builtin-skills-evaluation

## 壁打ちフェーズ [2026-03-12 07:00]

### 理解のサマリー
- 評価の目的: L2-worker が作成した「ビルトイン skills 評価リファレンス」（SKILL.md）と `docs/workflow.md` の連動更新の品質を検証する
- 評価スコープ: E-001（品質検証4項目）、E-002（知見記録）、E-003（課題起票・転記判断）
- 完了条件: 06_eval_report.md に全評価項目の結果、知見セクションに最低1行、07_issues.md の全課題に転記判断

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（サマリ・タスク実績・成果物一覧・知見セクション全て記載済み）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（3つの成功基準が明確に定義されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（Read/Write/Edit/Glob/Grep で全ファイルアクセス可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.claude/skills/builtin-skills-reference/SKILL.md`（新規作成）
- `docs/workflow.md`（連動更新部分）
- `sessions/initiatives/builtin-skills-evaluation/04_work_report.md`（作業レポート）
- `sessions/initiatives/builtin-skills-evaluation/07_issues.md`（課題メモ）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | 5 skills 全てに評価があるか | SKILL.md の「各 Skill の詳細評価」セクションを確認し、/simplify, /batch, /debug, /loop, /claude-api の5件が揃っているか | 5件全てに「機能概要」「適用可能性」「具体的な利用シーン」「制約事項」の4項目が記載されている |
| 2 | 適用可能性の判定理由が具体的か | 各 skill の判定理由がプロジェクト特性（Markdown 文書・プロセスルール管理主体）に基づく具体的根拠を含むか | 抽象的な「使えない」ではなく、プロジェクト特性との対比による具体的理由が記載されている |
| 3 | SKILL.md の frontmatter（description）が適切なトリガー条件を含むか | description の内容が `user-invocable: false` のスキルとして適切なトリガー条件（どのような質問・文脈で参照されるか）を含むか | description に参照されるべき文脈（skill 評価、活用相談、利用判断）が明記されている |
| 4 | `docs/workflow.md` の連動更新が正しいか | workflow.md に追加されたセクションが (a) 正の情報源の表記がある、(b) 評価サマリーが SKILL.md と一致する、(c) 既存のセクション構造と整合する | 3条件全てを満たす |
| 5 | 01_plan.md 成功基準1: 5つのビルトイン skills 全てに評価結果が記載 | SKILL.md の評価サマリーテーブルに5件の skill が記載されているか | 5件全てに適用可能性と推奨利用場面がある |
| 6 | 01_plan.md 成功基準2: SKILL.md が適切な frontmatter を持つ | frontmatter に name, description, user-invocable: false があるか | 3フィールド全てが存在し、02_tasks.md の指定値と一致する |
| 7 | 01_plan.md 成功基準3: docs/workflow.md に連動更新されている | workflow.md にビルトイン skills 関連の記載があるか | 該当セクションが存在する |

## 評価スケジュール
- 評価項目1〜4（E-001）→ 評価項目5〜7（成功基準達成度）→ E-002（知見記録）→ E-003（課題起票）の順で実施

## 前提・制約
- 評価はファイルの内容確認に基づく静的検証のみ（実行時の動作確認は含まない）
- SKILL.md の skill 情報の正確性は公式ドキュメントとの突合で検証（ただし Web 検索は実施しない。worker の参照元を信頼する）

---
**作成者**: L2（評価）
**作成日**: 2026-03-12
