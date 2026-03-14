# タスクリスト: config-optimizer-session

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1 タスク（スキル・エージェント・テンプレート作成）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | セッションテンプレート作成 | `sessions/config-optimization/_template/` に 00〜04 + workers/_template/ が存在する | 🔴 | ✅ |
| T-002 | リファレンス初期ファイル作成 | `reference/claude-code-config-reference.md` にスケルトン構造が存在する | 🔴 | ✅ |
| T-003 | SKILL.md 作成 | config-optimizer-manager SKILL.md が session-flow-policy §2 の必須セクションを満たす | 🔴 | ✅ |
| T-004 | config-collection-worker 定義 | agents/config-collection-worker.md が session-flow-policy §3 の必須要素を満たす。WebSearch/WebFetch がツールに含まれる | 🔴 | ✅ |
| T-005 | config-analysis-worker 定義 | agents/config-analysis-worker.md が session-flow-policy §3 の必須要素を満たす | 🔴 | ✅ |
| T-006 | config-proposal-worker 定義 | agents/config-proposal-worker.md が session-flow-policy §3 の必須要素を満たす | 🔴 | ✅ |
| T-007 | config-optimizer-evaluator 定義 | agents/config-optimizer-evaluator.md が session-flow-policy §3 の必須要素を満たす。対称性確認テーブルを含む | 🔴 | ✅ |

## フェーズ2 タスク（既存ファイル連動更新）

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-008 | commit-message.md 更新 | co-mgr, co-worker, co-eval がセッション種別テーブルに追加されている | 🔴 | ✅ |
| T-009 | manager-common-policy §1 更新 | 適用対象テーブルに config-optimizer-manager が追加されている | 🟡 | ✅ |
| T-010 | session-flow-policy §5 更新 | 既存セッションタイプテーブルに config-optimizer-manager が追加されている | 🟡 | ✅ |
| T-011 | triage-standard-policy 更新 | 適用マトリクス・ペアリング構造・走査対象に追加されている | 🟡 | ✅ |
| T-012 | docs/workflow.md 更新 | config optimization セッションフローの記述が追加されている | 🟡 | ✅ |

---
**作成者**: L1
**最終更新**: 2026-03-14
