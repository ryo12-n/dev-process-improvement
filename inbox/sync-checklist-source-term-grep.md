# repo-sync-checklist に「ソース固有用語リスト」ステップを追加

## 概要

概念移植を含むリポジトリ間同期において、ターゲットにソース固有の用語（L1/L2、manager-common-policy 等）が意図せず残存するリスクがある。現行の repo-sync-checklist セクション5（参照整合性の検証）に、「ソース固有用語リスト」を事前定義し grep で網羅チェックするステップを追加する提案。

## 背景

2026-03-12 の同期セッション（dev-process-improvement → ai-driven-dev-patterns）で、evaluator が `L1`, `L2`, `l1-manager`, `manager-common-policy`, `triage-standard-policy` を検索語として使用し、意図しない残存がないことを確認した。この手順が品質安定に有効であることが実証された。

## 提案

repo-sync-checklist セクション5.4（参照整合性の検証）に以下を追加:

- 同期計画作成時に「ソース固有用語リスト」を定義する（例: ソースのみに存在するスキル名、ロール名、ディレクトリ名）
- 同期完了後、evaluator がターゲットリポジトリの変更ファイルに対し用語リストの grep チェックを実施する
- 正当な使用（ターゲットでも実際に使われている用語）と意図しない残存を区別する

## 発見元

sessions/sync/20260312/ — sync-evaluator の知見 #1
