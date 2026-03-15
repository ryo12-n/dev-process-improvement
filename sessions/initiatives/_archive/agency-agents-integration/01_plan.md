# 実施計画: agency-agents-integration

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | refs 取り込み + インデックス作成 | agency-agents が refs/ に配置され、knowledge.md のカタログが全部門をカバー |
| 2 | マッチング仕組み構築 | manager-common-policy §10 が追加され、l1-manager に選定手順が記載 |
| 3 | l1-manager 統合 | l2-worker.md にエージェント参照手順が追加され、テンプレートが更新 |
| 4 | 連動更新 + 後続施策起票 | docs/workflow.md が更新され、backlog に後続施策 2 件が起票 |

## 成功基準（全体）

1. `refs/agency-agents/` に 12 部門のエージェント定義が配置されている
2. `refs/agency-agents/knowledge.md` に全部門のカタログ + 6 パターン以上の施策タイプ別マッピングがある
3. `manager-common-policy/SKILL.md` に §10（4 サブセクション）が追加されている
4. `l1-manager/SKILL.md` にエージェント選定手順が記載されている
5. `l2-worker.md` の作業フローにエージェント参照手順が追加されている
6. `_template/02_tasks.md` に「参照ドメインエージェント」セクションがある
7. `docs/workflow.md` に変更が反映されている
8. 後続施策 2 件が `backlog/entries/` + `backlog.csv` に起票されている

## リソース・前提条件

- agency-agents リポジトリへのインターネットアクセス（git clone）
- dev-process-improvement リポジトリ内の既存構造（manager-common-policy §1〜§9）の理解

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| リポジトリ容量圧迫 | 低 | 中 | ファイルサイズ確認。Markdown 中心なので通常は軽量 |
| L2-worker がエージェントの役割を引き受ける | 中 | 中 | §10.3 と l2-worker.md に「参照のみ」制約を明記 |
| knowledge.md の陳腐化 | 中 | 低 | 有効期限メタ情報 + 定期レビュー施策（backlog 起票） |
| 02_tasks.md テンプレート変更が進行中施策に影響 | 低 | 低 | テンプレートは新規施策のみに適用（既存はコピー済み） |

---
**作成者**: L1
**作成日**: 2026-03-15
**最終更新**: 2026-03-15
