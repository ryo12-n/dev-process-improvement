# 実施計画: l1-no-direct-work-enforcement

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | L1 担当ファイルテーブルの設計・実装 | L1 SKILL.md に担当ファイルテーブルが追加され、編集可能/禁止ファイルが明示されている |
| 2 | CLAUDE.md 禁止事項の強化 | CLAUDE.md の禁止事項に L1 の実作業ファイル編集禁止が追記されている |
| 3 | L1 SKILL.md「やらないこと」セクションの拡充 | 具体的なファイルパスパターンで禁止範囲が明示されている |

## 成功基準（全体）

1. L1 SKILL.md に「担当ファイルテーブル」が存在し、L1 が作成・編集可能なファイルが明示的に列挙されている
2. CLAUDE.md の禁止事項に「L1セッションが施策のタスク対象ファイル（`.claude/skills/`, `.claude/rules/`, テンプレート等）を直接編集すること」が追記されている
3. L1 SKILL.md の「やらないこと」セクションに、禁止対象のファイルパスパターンが具体的に列挙されている
4. L2-worker, L2-evaluator の既存「担当ファイルテーブル」との整合性が確認されている

## 変更対象ファイル

| ファイル | 変更内容 |
|---------|---------|
| `.claude/skills/l1-manager/SKILL.md` | 「担当ファイルテーブル」セクション新設、「やらないこと」セクション拡充 |
| `CLAUDE.md` | 禁止事項に L1 の実作業ファイル編集禁止を追記 |
| `docs/workflow.md` | L1 の担当ファイル制約の記述を追加（可視化文書の連動更新） |

## L1 担当ファイルテーブル（設計案）

L1 が作成・編集可能なファイル:

| ファイル | 操作 |
|---------|------|
| `sessions/initiatives/<施策名>/00_wallbash_log.md` | 作成・編集 |
| `sessions/initiatives/<施策名>/01_proposal.md` | 作成・編集 |
| `sessions/initiatives/<施策名>/02_plan.md` | 作成・編集 |
| `sessions/initiatives/<施策名>/03_tasks.md` | 作成・編集 |
| `sessions/initiatives/<施策名>/04_dispatch_log.md` | 作成・編集 |
| `sessions/initiatives/<施策名>/05_gate_review.md` | 作成・編集 |
| `sessions/initiatives/<施策名>/06_cost_record.md` | 作成・編集 |
| `sessions/initiatives/<施策名>/phase-1-planning/set-N/` | ディレクトリ作成（テンプレートコピー） |
| `sessions/initiatives/<施策名>/phase-2-execution/set-N/` | ディレクトリ作成（テンプレートコピー） |
| `backlog/entries/*.md` | 削除（施策化時）・ステータス更新 |
| `issues/entries/ISS-XXX.md` | 作成（L2 が resume 不可の場合の代理転記のみ） |
| `inbox/*.md` | 作成（知見ルーティング時） |

L1 が編集禁止のファイル（= L2 ワーカーに委任すべき実作業対象）:

| パスパターン | 理由 |
|------------|------|
| `.claude/skills/**` | スキル定義の変更は実作業 |
| `.claude/rules/**` | ルールファイルの変更は実作業 |
| `.claude/templates/**` | テンプレートの変更は実作業 |
| `sessions/initiatives/_template/**` | 施策テンプレートの変更は実作業 |
| `sessions/triage/_template/**` | トリアージテンプレートの変更は実作業 |
| `docs/**` | ドキュメントの変更は実作業（ただし知見ルーティングによる追記は例外） |
| `phase-*/set-N/01_worker_plan.md` 〜 `07_issues.md` | L2 成果物（既存ルール） |

## リソース・前提条件

- 変更対象は3ファイルのみ（小規模施策）
- L2-worker/L2-evaluator の既存「担当ファイルテーブル」を参照して整合性を確認する

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| L1 の正当な編集対象の漏れ | 中 | 低 | plan-worker で網羅性を検証する |
| 禁止範囲が広すぎてクローズ手順等に支障 | 低 | 中 | クローズ手順で必要な操作（inbox/backlog への書き込み等）を許可リストに含める |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
