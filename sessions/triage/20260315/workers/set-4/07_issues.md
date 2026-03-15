# 課題メモ（ワーカーセット別バッファ）: Set-4

> **このファイルの役割**: ワーカーセット内で発見された課題・知見・リスクの一時メモ置き場。
> マネージャーが `03_report.md` 作成時に全ワーカーセットの課題を集約し、`プロセス改善_課題管理.csv` へ転記する。

## 転記ルール

- ワーカー・評価者は課題をこのファイルに起票する（CSV 直接起票はしない）
- マネージャーが集約時に CSV 転記の要否を判断する
- 施策スコープ外・他のセッションでも再発しうる課題 → **マネージャーが CSV に転記**
- 当セッション内だけで完結する軽微な修正メモ → 転記不要（クローズ扱い）
- 転記済みの項目には `[転記済 ISS-XXX]` を末尾に追記する

---

## 未転記メモ

### [2026-03-15] manager-common-policy の適用対象不整合（automation-manager 欠落 + workflow.md 乖離）
- **種別**: 改善提案
- **発見者**: ワーカー（TG-006 + TG-008 横断）
- **内容**:
  1. `manager-common-policy/SKILL.md` の §1 適用対象テーブルに automation-manager が欠落している。description（L3）および本文（L9）では「6つのマネージャー」として config-optimizer-manager を含むが automation-manager を含まない
  2. `docs/workflow.md` L623, L639 のマネージャー共通ポリシーセクションでは、逆に automation-manager を含むが config-optimizer-manager を含まない
  3. 実際には l1-manager, triage-manager, metacognition-manager, sync-manager, backlog-maintenance-manager, automation-manager, config-optimizer-manager の **7マネージャー** が存在する
  4. manager-common-policy §9 関連ファイル一覧にも automation-manager の SKILL.md・agents が未記載
- **対応方針（案）**:
  - manager-common-policy/SKILL.md: description と §1 を「7つのマネージャー」に更新し、automation-manager を適用対象テーブルに追加。§9 に automation-manager 関連ファイルを追加
  - docs/workflow.md: マネージャー共通ポリシーセクションを「7つのマネージャー」に更新し、config-optimizer-manager を追加
  - session-flow-policy §5.1 のチェックリストに「manager-common-policy §1 の適用対象テーブル更新」を追加することを検討
- **関連タスク**: TG-006, TG-008
