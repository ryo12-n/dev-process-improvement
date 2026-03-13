# 改善施策提案: SessionStart hook ブランチ整理自動化

## 背景・課題

セッション開始時のブランチ整理（6ステップ）は `.claude/rules/session-start-branch-cleanup.md` で定義され、全マネージャーセッション（L1, triage, metacognition, sync, backlog-maintenance, l1-impl）で毎回 LLM が手動実行している。

問題点:
- 毎セッション数分の作業コスト（LLM のコンテキスト消費含む）
- 手順の実行漏れ・ミスのリスク
- `.claude/rules/` に記載された手順を LLM が解釈・実行するという二重管理構造

`ai-automation-tool-review` 施策の費用対効果評価で最高スコア（9.0）を獲得しており、SessionStart hook + シェルスクリプトで完全自動化が可能。

## 目標

- SessionStart hook によるブランチ整理の完全自動化
- マネージャーセッション開始時の手動ステップを 0 に削減
- hook 出力の JSON をセッションが読み取り、結果を報告するだけの構造に移行

## スコープ
### やること
- `.claude/hooks/session-start-branch-cleanup.sh` シェルスクリプトの新規作成
- `.claude/settings.json` への hooks.SessionStart セクション追加
- 6つのマネージャースキルの「セッション開始時のブランチ整理」セクション更新
- `.claude/rules/session-start-branch-cleanup.md` の役割再定義（方針定義・設計仕様に変更）
- `docs/workflow.md` の更新

### やらないこと
- 外部リポジトリ整理の hook 統合（別スクリプト・別タイミングで管理。`external-repo-cleanup` スキルは変更しない）
- hook の matcher 変更（startup + resume のみ。clear/compact は対象外）
- セッション開始時の todo 登録（§8）の自動化（別施策）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- 毎セッション開始時の手動6ステップを完全に自動化
- 手順の実行漏れ・ミスを根絶
- セッション開始時のコンテキスト消費を削減（LLM が手順を解釈・実行する必要がなくなる）
- `.claude/rules/session-start-branch-cleanup.md` と実行ロジックの二重管理を解消

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| hook スクリプトの実行エラーでセッション開始がブロックされる | 高 | exit 0 を保証し、エラーは JSON の warnings/errors で報告 |
| gh コマンドが利用できない環境で PR 作成が失敗する | 中 | gh 不在時は PR ステップをスキップし、warnings に記録 |
| git push 失敗時の対応 | 中 | エラーを JSON で出力し、LLM がユーザーに報告する構造 |

## 壁打ちの背景

1. **Matcher 設定**: startup + resume のみ実行し、clear/compact では実行しない。clear は会話リセットでありブランチ状態は変わらないため不要。compact はコンテキスト圧縮であり同様に不要。
2. **gh 不在時の挙動**: SDK 環境等で gh が利用できない場合、PR 作成ステップをスキップしてログ出力する。セッションをブロックしない設計を優先。
3. **スクリプト分離方針**: 本リポジトリのブランチ整理（SessionStart hook、自動）と外部リポジトリ整理（external-repo-cleanup スキル、壁打ち後オンデマンド）は完全に分離する。タイミングも用途も異なるため、統合しない。

## 備考・設計パターン

参考実装方針: `sessions/initiatives/ai-automation-tool-review/04_work_report.md` の「順位1」セクション

---
**起票者**: L1
**起票日**: 2026-03-13
**ステータス**: 完了
**backlog元ファイル**: SessionStart-hookブランチ整理自動化.md
