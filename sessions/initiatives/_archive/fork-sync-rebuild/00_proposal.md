# 改善施策提案: fork-sync-rebuild

## 背景・課題

upstream リポジトリ `ryo12-n/ai-driven-dev-patterns` から `dev-process-improvement` ディレクトリが切り出され、独立リポジトリ `ryo12-n/dev-process-improvement` になった。

これにより、社内の疑似フォーク `ryo-nagata_monotaro/ai-driven-dev-patterns-fork` は以下の問題を抱えた:

1. **リポジトリ構成の不一致**: 社内は1リポジトリ、upstream は2リポジトリに分離済み
2. **同期スクリプトの無効化**: 既存の `scripts/sync.sh` は1リポジトリ前提の設計で、2リポジトリ体制に対応できない
3. **運用の継続不能**: upstream の変更を社内に取り込む手段が失われている

## 目標

1. 社内に upstream と同名の2リポジトリ（`ai-driven-dev-patterns`, `dev-process-improvement`）を作成し、同期体制を再構築する
2. 複数リポジトリの同期を一元管理する Claude スキル（`/fork-sync`）を作成する
3. main への直接 push ではなく、ブランチ + PR 方式で同期する

## スコープ
### やること
- 旧社内リポジトリ（ai-driven-dev-patterns-fork）の削除
- 社内リポジトリ2つの新規作成と初回同期
- fork-sync スキル（SKILL.md + repos.json）の作成
- MEMORY.md の更新

### やらないこと
- upstream の sync-manager（構成同期用）への変更
- 旧リポジトリのバックアップ（全データ upstream 反映済み）
- ai-driven-dev-patterns リポジトリへの社内固有の変更

## 期待される効果
- 2リポジトリ体制での upstream ↔ origin 同期が `/fork-sync` で対話的に実行可能になる
- 同期対象リポジトリを repos.json で管理することで、将来のリポジトリ追加にも対応できる
- PR 経由の差分確認により、同期内容の可視性が向上する

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| `gh pr create` が Enterprise Managed User 制限で失敗 | 中 | フォールバック URL 提示の仕組みを SKILL.md に組み込む |
| 旧リポジトリ削除後にデータ喪失 | 低 | 全データ upstream 反映済みであることを事前確認 |

## 壁打ちの背景

- 同期の仕組みの管理場所: `dev-process-improvement` に一元化する方針を選択。理由は開発プロセス改善の管轄であり、upstream の sync-manager との役割分担が明確になるため
- スキル名: `fork-sync` とした。upstream の `sync-manager`（構成同期用）と区別するため `fork-` プレフィックスを採用
- 同期方式: ブランチ + PR 方式を採用。main への直接 push を避け、差分レビューの機会を確保する

## 備考・設計パターン

upstream の sync-manager との違い:
| 観点 | sync-manager | fork-sync |
|------|-------------|-----------|
| 目的 | リポジトリ間の構成・ルール・テンプレート同期 | upstream ↔ origin の git レベル同期 |
| 操作 | ファイルコピー・差分適用・整合性検証 | git fetch → ff-only merge → ブランチ push → PR |
| セッション | sessions/sync/ に記録 | セッション記録なし（単発操作） |

---
**起票者**: L1
**起票日**: 2026-03-08
**ステータス**: 完了
