# 全体計画書: backlog-batch-execution

## 目的
backlog-inventory-batch 施策で棚卸し・分類した78件のバックログエントリを、バッチ施策として順次消化する。

## スコープ
- S分類35件 → 6バッチ施策として実行
- M分類34件 → 個別施策（統合候補3組あり）
- L分類9件 → 個別施策

## 施策一覧

### バッチ施策（S分類: 35件）

| # | 施策名 | 対象件数 | 概要 | 優先度 | ステータス |
|---|--------|---------|------|--------|-----------|
| 1 | batch-reference-fix-and-rename | 4件 | 壊れた参照修正・リネーム追従ルール追加 | 高 | 未着手 |
| 2 | batch-gha-minor-fixes | 4件 | GHAスキル設定追加・マッピング登録 | 高 | 未着手 |
| 3 | batch-template-doc-fixes | 6件 | docs/workflow.md更新・テンプレート統一 | 中 | 未着手 |
| 4 | batch-rule-policy-minor-additions | 7件 | ルール・ポリシーへの軽微な追記 | 中 | 未着手 |
| 5 | batch-aidd-minor-fixes | 6件 | ai-driven-dev-patterns関連の軽微修正 | 中 | 未着手 |
| 6 | batch-skill-session-tweaks | 8件 | スキル・セッション定義の微調整 | 低 | 未着手 |

### M分類 統合候補（3組）

| # | 統合施策候補 | 対象エントリ | ステータス |
|---|------------|------------|-----------|
| 1 | 非施策セッション GHA 自動化 | BL-055 + BL-057 | 未着手 |
| 2 | docs/workflow.md 網羅性改善 | BL-054 + BL-065 | 未着手 |
| 3 | PostToolUse hook 品質チェック統合 | BL-030 + BL-082 | 未着手 |

### M/L個別施策
M残り28件、L9件は通常のトリアージ・施策フローで個別対応。本プロジェクトではトラッキング対象外。

## 方針・制約
- batch-aidd-minor-fixes は CLI `--add-dir` 環境が必要（SDK環境では実行不可: ISS-027）
- バッチ施策は1施策=1イニシアティブとして L1→L2 フローで実行
- 相互依存が少ない施策から着手

## 参照元
- 棚卸し結果: `sessions/initiatives/_archive/backlog-inventory-batch/phase-2-execution/set-1/03_worker_report.md`

---
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
