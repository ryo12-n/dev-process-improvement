# refs 読み込みステップの標準配置パターン

## 気づき

l1-impl-manager への refs 知見参照ステップ追加で確立された配置パターン:

- **マネージャー**: タスク作成「前」（各フェーズのステップ1）に配置
- **ワーカー**: 壁打ち「前」に配置

この順序により「知見把握 → 理解確認（壁打ち） → 作業実施」の流れが成立する。

## 背景

- 施策: `impl-manager-refs-knowledge-read`
- 発見元: L2-evaluator の評価項目1検証
- l1-impl-manager の Phase 1-4 と 3 ワーカー（investigation, design, impl-plan）で一貫して適用

## トリアージでの判断依頼

今後他マネージャースキルに refs 読み込みを追加する際の標準パターンとして rules/ に記載すべきか検討。

---
**起票日**: 2026-03-17
**起票元施策**: impl-manager-refs-knowledge-read
