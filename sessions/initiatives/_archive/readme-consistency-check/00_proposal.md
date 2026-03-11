# 改善施策提案: README 整合性チェック

## 背景・課題

README.md は人間のエントリーポイントであり、リポジトリの全体像を正確に反映している必要がある。しかし、施策の積み重ねにより以下の乖離が確認されている。

### 確認済みの乖離

1. **ディレクトリ構成図の欠落**
   - `.claude/rules/` に `pr-url-output.md`, `session-start-branch-cleanup.md` が記載されていない
   - `.claude/skills/` に `metacognition-manager/`, `sync-manager/`, `manager-common-policy/`, `session-flow-policy/`, `triage-standard-policy/`, `rule-change-checklist/`, `repo-sync-checklist/`, `fork-sync/` が記載されていない
   - `sessions/sync/`, `sessions/metacognition/` ディレクトリが記載されていない

2. **セッション種別テーブルの欠落**
   - メタ認知セッション（metacognition-manager）が記載されていない

3. **AI向けスキル定義テーブルの欠落**
   - sync-manager, sync-worker, sync-evaluator が記載されていない
   - metacognition-manager, metacognition-worker, metacognition-evaluator が記載されていない

4. **構成の実態との乖離**
   - `backlog/ideas.md` → 実態は `backlog/entries/` + `backlog.csv` + `backlog/README.md` 形式
   - `issues/ISS-NNN.md` → 実態は `issues/entries/ISS-NNN.md` + `issues/README.md` + `issues/_template.md` 形式
   - トリアージテンプレート: `02_work_log.md`, `03_report.md` → 実態は `00〜04` + `workers/_template/` 構成

5. **ドキュメントマップ「その他」のリンク切れ**
   - `backlog/ideas.md` が存在しない

## 目標

1. README.md の記載内容を実態に一致させる
2. トリアージで README 整合性が継続的にチェックされる仕組みをルール化する

## スコープ

### やること
- README.md の乖離箇所を修正する（ディレクトリ構成図・テーブル・リンク）
- triage-manager SKILL.md の「ルールとworkflowの整合性チェック」に README 整合性チェック観点を追加する
- docs/workflow.md のトリアージセクションに README チェックの記述を追加する

### やらないこと
- README の構成を大幅にリデザインすること（既存構造を維持しつつ更新）
- 新しい TG タスク番号の追加（既存の整合性チェックに統合する）
- ポリシー系スキル（manager-common-policy 等）の AI 向けスキル定義テーブルへの追加（起動型スキルのみ記載する方針）

## 期待される効果

- 人間がリポジトリの全体像を正確に把握できるようになる
- 新セッションタイプ（sync, metacognition）の存在と起動方法が README から分かるようになる
- トリアージで README の乖離が検出され、放置されなくなる

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| README 更新中に他施策が進み新たな乖離が発生 | 低 | ルール化で継続的にキャッチする |
| 150行制限を超過する | 中 | 起動型スキルのみに絞り、ディレクトリ構成図をコンパクトに保つ |

## 壁打ちの背景

- AI向けスキル定義テーブルにポリシー系スキルも全て列挙するか検討したが、**起動型スキル（l1-manager, triage-manager, sync-manager, metacognition-manager）のみ**に絞る方針をユーザーと合意した
- README 整合性チェックのルール化は、新規 TG タスクを追加せず、**既存の「ルールとworkflowの整合性チェック」の拡張**として組み込む方針とした

---
**起票者**: L1
**起票日**: 2026-03-08
**ステータス**: 起票
