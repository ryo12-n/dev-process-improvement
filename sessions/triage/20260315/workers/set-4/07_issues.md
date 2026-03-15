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

### [2026-03-15] manager-common-policy §9 関連ファイル一覧に config-optimizer-manager も欠落
- **種別**: 改善提案（ワーカー課題の補完）
- **発見者**: 評価者（独自検証時）
- **内容**:
  1. ワーカーは §9 関連ファイル一覧から automation-manager が欠落していることを報告したが、config-optimizer-manager も同様に §9 に記載されていない
  2. §9 には l1-manager, triage-manager, metacognition-manager, sync-manager, backlog-maintenance-manager の5件のみが記載されている
  3. §1 適用対象テーブルには config-optimizer-manager が含まれているにもかかわらず、§9 の連動更新対象に含まれていない。これはポリシー変更時に config-optimizer-manager への通知漏れを引き起こすリスクがある
- **対応方針（案）**:
  - ワーカーの課題（上記）の対応方針に「§9 に config-optimizer-manager と automation-manager の双方を追加」を含める
  - §1 と §9 の対応関係を一致させることで、新マネージャー追加時の整合性確認を容易にする
- **関連タスク**: TG-008（評価者独自検証）
