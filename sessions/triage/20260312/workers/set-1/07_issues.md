# 課題メモ（ワーカーセット別バッファ）: Set-1

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

### [2026-03-12] README.md の backlog-maintenance-manager 連動更新漏れ
- **種別**: 改善提案
- **発見者**: ワーカー
- **内容**: README.md の4セクション（ディレクトリ構成図・セッション種別テーブル・AI向けスキル定義テーブル・ドキュメントマップ）に backlog-maintenance-manager が未記載。backlog-maintenance-session 施策で追加されたセッションタイプだが、README への連動更新が漏れた。同様に docs/ 配下の4ファイル（management-system-guide.md, subagent-permission-guide.md, coordination-protocol-guideline.md, git-worktree-guideline.md）がドキュメントマップに未記載。
- **対応方針（案）**: (1) README.md を修正して backlog-maintenance-manager と不足 docs/ ファイルを追記する（セッション内修正可能）。(2) session-flow-policy §5.1 のチェックリストまたは rule-change-checklist に README.md の更新を追加し、再発を防止する。
- **関連タスク**: TG-INT(2)
- **評価者補足**: fork-sync（user-invocable: true）も README.md に未記載であることを確認。backlog-maintenance-manager とは別経緯での追加だが、README 更新時に合わせて対応すべき。
