# ai-driven-dev-patterns 同期チェックリスト

> dev-process-improvement の `sessions/` 構成を基に、ai-driven-dev-patterns への同期時に確認すべき要素を整理する。

## 1. 導入すべき要素

| # | 要素 | dev-process-improvement での実装 | ai-driven-dev-patterns への適用方針 |
|---|------|-------------------------------|----------------------------------|
| 1 | `sessions/` ディレクトリ | `sessions/initiatives/`, `sessions/triage/` の2階層 | initiatives が存在する場合は同構成を導入。triage は dev-process-improvement 固有のため不要 |
| 2 | `sessions/initiatives/_template/` | 00〜08 の番号付きファイル | ai-driven-dev-patterns に initiative テンプレートを持ち込む場合はそのまま適用 |
| 3 | `sessions/initiatives/_archive/` | 完了済み施策の移動先 | 同等のアーカイブディレクトリを作成 |
| 4 | テンプレートコピー手順の改善 | workers/ を空ディレクトリで作成、ワーカーセットは _template/workers/_template/ から直接コピー | triage 構成を持ち込む場合のみ適用 |

## 2. 差異が許容されるポイント

| # | ポイント | 理由 |
|---|---------|------|
| 1 | `sessions/triage/` の有無 | トリアージセッションは dev-process-improvement 固有のプロセス改善サイクル。ai-driven-dev-patterns ではプロダクト開発が主目的であり、同じトリアージフローは不要な場合がある |
| 2 | `_archive/` 配下の移動タイミング | アーカイブ移動のタイミングやルールはリポジトリの運用頻度に応じて調整可 |
| 3 | テンプレートファイルの番号付け | ai-driven-dev-patterns のプロジェクト規模・ワークフローに応じてファイル構成をカスタマイズしてよい |
| 4 | 課題管理 CSV の列定義 | プロジェクト固有の列を追加・削除してよい |
| 5 | `sessions/triage/_archive/` | triage セッションを持ち込まない場合は不要 |

## 3. 統一すべきポイント

| # | ポイント | 理由 | 統一方法 |
|---|---------|------|---------|
| 1 | `sessions/` をトップレベルディレクトリとして使用 | 2リポジトリ間でセッション成果物の配置規則を揃え、相互参照時の混乱を防ぐ | ai-driven-dev-patterns に initiative 構造を導入する際は `sessions/initiatives/` を使用する |
| 2 | 施策テンプレートの基本構造（proposal → plan → tasks → report → gate_review） | ライフサイクルの統一により、リポジトリ間で施策の進捗把握方法が共通化される | テンプレートの番号付けとファイル名は統一する |
| 3 | コミットメッセージ規約の `[session-type] category:` 形式 | 2リポジトリ間でコミット履歴の解析方法を統一する | `.claude/rules/commit-message.md` を同期する |
| 4 | `.claude/skills/` のスキル・エージェント構成 | マネージャー=スキル、ワーカー=エージェントの基本パターンを統一する | session-flow-policy の基本構造に従う |
| 5 | `issues/` + CSV の課題管理パターン | 施策横断の課題管理方法を統一する | CSV のコア列（ID, 起票日, カテゴリ, 種別, タイトル, ステータス）は統一する |

## 4. 同期時の注意事項

- ai-driven-dev-patterns は dev-process-improvement のコンテキストに **依存される側** である（CLAUDE.md のリポジトリ境界ポリシー参照）
- 同期は dev-process-improvement → ai-driven-dev-patterns の方向で行う（逆方向の依存は発生しない）
- 同期対象は **構成・ルール・テンプレート** であり、セッション成果物（作業ログ等）は同期しない
- 実際の同期実施は後続施策（「リポジトリ間テンプレート同期の検証チェックリスト」）で行う

---
**作成者**: L2（実施）
**作成日**: 2026-03-08
**関連施策**: `sessions/initiatives/partial-repo-sync/`
