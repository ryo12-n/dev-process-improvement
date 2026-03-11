# 評価計画: マネージャーセッション共通ポリシー策定

## 壁打ちフェーズ [2026-03-08]

### 理解のサマリー
- 評価の目的: L2-worker が作成した `manager-common-policy/SKILL.md` と各マネージャースキルの参照置換が、計画の成功基準（E-1〜E-6）を達成しているか評価する
- 評価スコープ: 共通ポリシー（§1〜§8）、4マネージャースキルの参照、情報欠落の有無、欠落補完、docs/workflow.md 整合性、関連ファイル相互参照
- 完了条件: 全6基準の達成度評価、推奨アクション記載、課題記録

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（T-001〜T-012 全完了、成果物一覧あり）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（E-1〜E-6 が具体的に定義済み）
- [x] 評価に必要なツール・アクセス権限: 確認済み（git diff、全ファイル読み取り可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.claude/skills/manager-common-policy/SKILL.md`（新規作成）
- `.claude/skills/l1-manager/SKILL.md`（参照置換）
- `.claude/skills/triage-manager/SKILL.md`（参照置換 + 欠落補完）
- `.claude/skills/metacognition-manager/SKILL.md`（参照置換 + 欠落補完）
- `.claude/skills/sync-manager/SKILL.md`（参照置換 + 欠落補完）
- `docs/workflow.md`（連動更新）
- `.claude/skills/triage-standard-policy/SKILL.md`（チェック項目追加）
- `.claude/skills/session-flow-policy/SKILL.md`（参照注記追加）

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| E-1 | 共通ポリシー §1〜§8 が全て存在し6つの共通パターンをカバー | `manager-common-policy/SKILL.md` 目視確認 | 全8セクションが存在し、ディスパッチ・成果物確認・ゲート判定・知見集約・課題集約・差し戻しの6パターンがカバーされている |
| E-2 | 各スキルの参照先セクション番号が正確 | 4スキルの「§N」参照を `manager-common-policy` の実セクション番号と1つずつ突合 | 全ての参照先セクション番号が実際のセクションと一致 |
| E-3 | 置換前後で情報が欠落していない | git diff で削除された内容が共通ポリシーに含まれているか確認 | 削除された全情報が共通ポリシーまたは固有部分として維持されている |
| E-4 | 欠落の補完（triage: ゲート判定+差し戻し、meta: 同、sync: 差し戻し） | 各スキルに該当参照が存在することを確認 | 指定された欠落項目がすべて参照として追加されている |
| E-5 | docs/workflow.md の整合性 | 共通ポリシー + 各スキルの内容と突合 | workflow.md の記述が共通ポリシーおよび各スキルの内容と矛盾しない |
| E-6 | 関連ファイル一覧の相互参照 | 全ファイルの一覧を確認 | manager-common-policy ↔ 4マネージャースキル、+ triage-standard-policy, session-flow-policy の相互参照が整合 |

## 評価スケジュール
- E-1〜E-6 を順に評価し、結果を `06_eval_report.md` に記載

## 前提・制約
- main ブランチと比較して変更内容を検証する

---
**作成者**: L2（評価）
**作成日**: 2026-03-08
