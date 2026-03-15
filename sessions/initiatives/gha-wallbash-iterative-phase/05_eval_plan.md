# 評価計画: GHA 壁打ちフェーズの独立・反復化

## 壁打ちフェーズ [2026-03-15 12:00]

### 理解のサマリー
- 評価の目的: 実施ワーカーが作成した成果物（スキル・ワークフロー・テンプレート・ドキュメント変更）の整合性を検証し、GHA 壁打ちフェーズの独立・反復化が設計通りに実装されているかを判定する
- 評価スコープ: T-E01（4項目の整合性検証）、T-E02（知見記録）、T-E03（課題起票・CSV転記）
- 完了条件: 4項目の検証結果が `06_eval_report.md` に記載され、知見セクションに最低1行の記載があり、課題の起票・転記判断が完了していること

### 前提条件チェック
- [x] 評価対象（04_work_report.md）の完成度: 十分（全12タスク完了、メタルール横断検証も実施済み）
- [x] 評価基準（01_plan.md の成功基準）の明確さ: 評価可能（7項目の成功基準が明確に定義されている）
- [x] 評価に必要なツール・アクセス権限: 確認済み（全検証対象ファイルが読み取り可能）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：評価開始

---

## 評価対象
- `.claude/skills/gha-wallbash/SKILL.md` — init/continue 2モード対応
- `.github/workflows/initiative-wallbash.yml` — 新 inputs + 条件分岐
- `.github/workflows/initiative-dispatcher.yml` — `/continue` コマンド routing
- `.github/workflows/initiative-execute.yml` — PR 作成ステップ追加
- `.claude/skills/gha-execute/SKILL.md` — 壁打ちドラフト活用対応
- `.claude/skills/l1-manager/SKILL.md` — `00a_wallbash_log.md` 記録ステップ追加
- `sessions/initiatives/_template/00a_wallbash_log.md` — 壁打ちログテンプレート
- `sessions/initiatives/_template/02_tasks.md` — ディスパッチ計画セクション追加
- `docs/workflow.md` — GHA Initiative フロー更新

## 評価項目

| # | 評価項目 | 評価方法 | 判定基準（合格ライン） |
|---|---------|---------|---------------------|
| 1 | gha-wallbash/SKILL.md の init/continue フローと initiative-wallbash.yml の inputs の対応 | スキルの init/continue 各ステップが参照するファイル・パスが YAML の inputs・ステップと一致するかを逐一確認 | init モードで issue_number のみ必須、continue モードで mode/feedback/initiative_dir/branch が使用されること。スキルのフローが YAML の条件分岐と整合すること |
| 2 | dispatcher の `/continue` routing と wallbash ワークフローの inputs の合致 | dispatcher の continue ケースで wallbash.yml に渡す inputs（mode, feedback, initiative_dir, branch）を確認 | 4つの inputs が全て正しく渡されること。wallbashing 以外のフェーズではエラーメッセージが返ること |
| 3 | execute の PR 作成ステップと wallbash の PR 削除の整合 | wallbash.yml から PR 作成ステップが削除されていることを確認し、execute.yml に phase=wallbashing 時の PR 作成ステップが存在することを確認 | wallbash には PR 作成ステップがなく、execute に phase=wallbashing 条件の PR 作成ステップがあること |
| 4 | テンプレート 00a_wallbash_log.md と gha-wallbash スキルの参照の一致 | スキルが参照する「現在の合意事項」「イテレーション履歴」セクションがテンプレートに存在するかを確認 | テンプレートにスキルが期待する2セクション構造（現在の合意事項: 目的/スコープ/計画の方向性/未解決事項、イテレーション履歴: Round N 形式）が存在すること |
| 5 | メタルール横断検証（評価者側） | スキル・テンプレート変更施策のため、フロー記述整合性・workflow.md 同期・TG-008 基準連動を確認 | 3領域の検証で不整合がないこと |
| 6 | 01_plan.md の成功基準7項目に対する達成度 | 各成功基準に対して実装ファイルの該当箇所を確認 | 全7項目が達成されていること |

## 評価スケジュール
- 項目1〜4: T-E01 として一括実施
- 項目5〜6: T-E01 の補完として実施
- T-E02: 評価中の知見を随時記録
- T-E03: 評価完了後に課題起票・転記判断

## 前提・制約
- 全検証対象ファイルはリポジトリ内で読み取り可能
- E2E テスト（実際の GHA 実行）は本評価のスコープ外（施策計画にも明記されている）

---
**作成者**: L2（評価）
**作成日**: 2026-03-15
