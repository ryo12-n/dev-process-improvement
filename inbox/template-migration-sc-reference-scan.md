# テンプレート構造変更時の session-consistency-reference.md 走査

## 概要

テンプレート構造変更施策（initiative-template-2phase-migration）で、rule-change-checklist の項目6「テンプレートの連動更新」に `session-consistency-reference.md` を走査対象として追加する価値があるとの知見が得られた。

## 背景

- テンプレートファイルの構造変更を行った際、`session-consistency-reference.md` のファイル一覧が旧構造のままであることが判明した
- SC セッション次回実行時に自動検出・更新される参照データのため本施策での修正は見送ったが、チェックリストに含めることで検出を早められる
- 優先度は低い（SC セッションの自動検出で補完される）

## 発見元

- L2-worker（initiative-template-2phase-migration T-004 grep 走査）

---
**作成日**: 2026-03-20
