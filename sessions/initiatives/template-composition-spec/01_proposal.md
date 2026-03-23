# 改善施策提案: テンプレート構成仕様の統一（レガシー workers/ → phase-1/ パターン）

## 背景・課題

4セッションタイプ（triage, metacognition, backlog-maintenance, automation）が `workers/_template/` パターンを使用しているが、session-flow-policy §4.3 のモダンパターン（`phase-N-xxx/_template/`）と不整合。

- **レガシー（4セッション）**: `workers/_template/` → ランタイム `workers/set-N/`
- **モダン（config-optimization, session-consistency）**: `phase-1-xxx/_template/` → ランタイム `phase-1-xxx/set-N/`
- session-lifecycle-policy §1.4.4: 「Future `phase-1-xxx/` unification is to be considered in a separate initiative」と明記

## 目標

レガシー `workers/` パターンをモダン `phase-1-xxx/` パターンに統一する。

## スコープ

### やること

- テンプレートディレクトリのリネーム（`workers/_template/` → `phase-1-<name>/_template/`）
  - triage → `phase-1-scan`、metacognition → `phase-1-analysis`、backlog-maintenance → `phase-1-scan`、automation → `phase-1-scan`
- マネージャー SKILL.md のパス参照更新（4ファイル）
- エージェント定義のパス参照更新（8ファイル: worker×4 + evaluator×4）
- ポリシーファイルの更新（session-lifecycle-policy §1.4.4、session-flow-policy、repo-sync-checklist 等 5ファイル）

### やらないこと

- 既存セッションインスタンスの移行（過去データは保持）
- テンプレートファイルの内容変更（構造のみ変更）
- 新しいフェーズの追加（単一フェーズ構造を維持）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- session-flow-policy §4.3 との整合性確保
- SC チェック時の構造パターン統一による検出精度向上
- 新セッションタイプ追加時の参照パターンが1つに収束

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| パス参照の更新漏れ | 中 | Grep で `workers/` を網羅検索済み（17ファイル特定） |
| 既存セッションとの混在 | 低 | 過去インスタンスは移行しない方針 |

## 壁打ちの背景

- ユーザー方針: 正解定義は現状維持、レガシーパターンをモダンパターンへ統一
- session-lifecycle-policy §1.4 に正解定義が既存のため新規テーブル作成は不要
- フェーズ名は各セッションの主要活動に基づき決定

## 備考・設計パターン

フォーマット変換（パスのリネーム）が中心。内容・ロジックの変更は含まない。

---
**起票者**: L1
**起票日**: 2026-03-20
**ステータス**: 承認済
**backlog元ファイル**: backlog/entries/template-composition-spec.md
