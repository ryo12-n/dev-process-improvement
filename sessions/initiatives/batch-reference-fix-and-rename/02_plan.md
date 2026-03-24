# 実施計画: batch-reference-fix-and-rename

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | 壊れた参照修正（SC-008） | `triage-standard-policy` の残存参照がゼロ |
| 2 | リネーム時全文検索チェックルール作成 | `.claude/rules/rename-reference-check.md` が作成され、内容がバックログエントリの実施案と整合 |
| 3 | バックログエントリクリーンアップ | 4件のバックログエントリが git rm 済み |

## 対象ファイル一覧

### 修正対象

| # | ファイル | 変更種別 | 内容 |
|---|---------|---------|------|
| 1 | `.claude/skills/l1-manager/agents/l2-plan-evaluator.md` | MODIFY | L112, L198: `triage-standard-policy` → `session-lifecycle-policy` |
| 2 | `.claude/skills/l1-manager/agents/l2-plan-worker.md` | MODIFY | L195: `triage-standard-policy` → `session-lifecycle-policy` |
| 3 | `.claude/rules/rename-reference-check.md` | CREATE | リネーム時の全文検索チェック義務化ルール |

### 削除対象（バックログクリーンアップ）

| # | ファイル | 理由 |
|---|---------|------|
| 1 | `backlog/entries/SC-008壊れた参照修正.md` | 本施策で対応完了 |
| 2 | `backlog/entries/SCチェックQuickWins一括是正.md` | 個別エントリに分解済み |
| 3 | `backlog/entries/リネーム時全文検索チェック義務化ルール追加.md` | 本施策で対応完了 |
| 4 | `backlog/entries/sync-worker同期先コミット漏れ防止.md` | アーカイブ済み施策の残存エントリ |

## 成功基準（全体）
1. `Grep` で `triage-standard-policy` を検索し、残存参照がゼロであること
2. `.claude/rules/rename-reference-check.md` が作成され、リネーム時の Grep チェック手順が記載されていること
3. 4件のバックログエントリが git rm されていること
4. ルール変更チェックリスト（rule-change-checklist）の全項目が確認済みであること

## リソース・前提条件
- dev-process-improvement リポジトリ内で完結（外部リポジトリ不要）
- 機械的修正が主体のため、1ワーカーの逐次実行で十分

## リスクと対策
| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| 参照修正箇所の見落とし | 低 | 低 | Grep で全文検索して確認 |
| リネームチェックルールのスコープ不足 | 低 | 中 | バックログエントリの実施案を参照 |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
