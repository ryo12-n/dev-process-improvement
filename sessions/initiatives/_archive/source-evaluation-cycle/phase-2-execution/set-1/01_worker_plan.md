# ワーカー計画: 情報ソース管理・評価サイクル基盤の構築 — Set-1

## 壁打ちフェーズ [2026-03-20 10:00]

### 理解のサマリー
- タスクの目的: ai-research-notebook リポジトリに情報ソース管理・評価サイクルの基盤を構築する
- スコープ: `spaces/ai-news-lab/source-management/` 配下にディレクトリ構造、ソースリスト、評価基準、テンプレート3種、運用ガイド（README）を作成。既存 README に1行追記
- 完了条件: T-001〜T-010 の全タスク完了、作業レポート記録
- set 番号: set-1（逐次ディスパッチ）

### 前提条件チェック
- [x] 依存タスクの完了状態: 依存タスクなし
- [x] 必要ツール・コマンドの利用可否: 確認済み（git, mkdir, Write ツール）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み（ai-research-notebook リポジトリ存在、initiative/source-evaluation-cycle ブランチにチェックアウト済み、source-management/ は未作成）
- [x] set 番号確認: set-1
- [x] set ディレクトリの存在確認: 確認済み（_template からコピー済み）

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

T-001〜T-008 を順に実行する。既存テンプレートの frontmatter スタイル（date, tags, task_type）を踏襲。

1. T-001: ディレクトリ構造作成（mkdir + .gitkeep）
2. T-002: evaluation-criteria.md 作成（5軸スコアリングガイド）
3. T-003: source-list.md 作成（空テーブル + ステータス/カテゴリ定義）
4. T-004: source-discovery-template.md 作成
5. T-005: source-evaluation-template.md 作成（2層構造）
6. T-006: quarterly-review-template.md 作成
7. T-007: README.md（運用ガイド）作成
8. T-008: ai-news-lab/README.md に1行追記
9. T-009: 知見記録
10. T-010: 課題転記確認
