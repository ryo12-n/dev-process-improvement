# 同期レポート: 20260308

## 同期パラメータ
- 同期元: dev-process-improvement (`/home/nr202/projects/dev-process-improvement/`)
- 同期先: ai-driven-dev-patterns (`/home/nr202/projects/ai-driven-dev-patterns/`)
- 同期スコープ: `.claude/rules/commit-message.md`, `.claude/rules/session-start-branch-cleanup.md`, `.claude/skills/rule-change-checklist/SKILL.md`, `.claude/skills/session-flow-policy/SKILL.md`, `sessions/initiatives/_template/`

## セクション1: 導入すべき要素

| # | 要素 | 判断 | 対応内容 |
|---|------|------|---------|
| 1 | `sessions/initiatives/` ディレクトリ | 導入 | 同期先に `sessions/initiatives/_template/`（00〜08 の番号付きファイル）と `sessions/initiatives/_archive/` を新規作成 |
| 2 | `session-start-branch-cleanup.md` | 導入 | `.claude/rules/` に新規作成。適用対象を `dev_manager` と `triage` スキルに適応 |
| 3 | `rule-change-checklist/SKILL.md` | 導入 | `.claude/skills/` に新規作成。関連ファイル一覧を同期先のパス体系（roles/, docs/）に適応 |
| 4 | `session-flow-policy/SKILL.md` | 導入 | `.claude/skills/` に新規作成。基本構造を dispatcher+dev_manager+roles パターンに適応 |

**チェック**:
- [x] 同期先に必要な要素を導入したか
- [x] テンプレートファイルが正しくコピーされたか（9ファイル: 00〜08）
- [x] アーカイブディレクトリが作成されたか（`sessions/initiatives/_archive/` + `.gitkeep`）

## セクション2: 差異が許容されるポイント

| # | ポイント | 判断 | 判断理由 |
|---|---------|------|---------|
| 1 | `sessions/triage/` の有無 | 差異許容 | 同期先には `.claude/skills/triage/` スキルがあるが、dev-process-improvement のトリアージセッション構成（triage-manager + agents）とは異なる。トリアージテンプレートは同期しない |
| 2 | テンプレートのロール名表記 | 差異許容 | 同期元は L1/L2 表記、同期先は dev_manager/specialist role 表記。同期先の既存パターンに合わせて適応済み |
| 3 | 課題管理 CSV 名 | 差異許容 | 同期元は `プロセス改善_課題管理.csv`、同期先は `課題管理.csv`。各リポジトリで独立管理。テンプレート内の参照を適応済み |
| 4 | session-flow-policy の既存セッションタイプ一覧 | 差異許容 | 同期先には triage-manager/sync-manager が存在しないため、同期先の実際のセッションタイプ（dispatcher, triage）のみを記載 |
| 5 | rule-change-checklist の TG-008 基準 | 差異許容 | 同期先に triage-standard-policy が存在しないため、「品質基準ポリシー」として汎用化 |
| 6 | 既存テンプレート（sessions/_template/）の維持 | 差異許容 | 同期先の既存テンプレート（plan.md, log.md, report.md, issues.md）はそのまま維持。initiatives 用の番号付きテンプレートは別ディレクトリとして導入 |

**チェック**:
- [x] 差異許容ポイントについて、同期先の事情に合わせた判断を行ったか
- [x] 判断理由を記録したか

## セクション3: 統一すべきポイント

| # | ポイント | 状態 | 対応内容 |
|---|---------|------|---------|
| 1 | `sessions/` をトップレベルディレクトリとして使用 | 統一済み | 同期先にも `sessions/` が既に存在。`sessions/initiatives/` を追加導入 |
| 2 | 施策テンプレートの基本構造（proposal → plan → tasks → report → gate_review） | 統一済み | `sessions/initiatives/_template/` に 00〜08 の番号付きテンプレートを導入 |
| 3 | コミットメッセージ規約の `[session-type] category:` 形式 | 統一済み | 既存の Conventional Commits 形式を維持しつつ、セッションプレフィックス形式を追記。使い分けガイドを追加 |
| 4 | `.claude/skills/` のスキル構成 | 統一済み | session-flow-policy を導入し、基本パターン（ディスパッチャー → マネージャー → 専門ロール）を明文化 |

**チェック**:
- [x] 統一すべきポイントが同期先でも同じ構成になっているか
- [x] コミットメッセージ規約が同期されたか
- [x] スキル構成が統一パターンに従っているか
- [x] 課題管理の CSV コア列が統一されているか（N/A: CSV 自体は同期対象外）

## セクション4: 同期時の注意事項

- [x] 同期元・同期先が計画どおりか — dev-process-improvement → ai-driven-dev-patterns で正しい
- [x] セッション成果物を誤って同期していないか — 同期対象はルール・スキル・テンプレートのみ。セッション成果物（work_log, sync_report 等）は含まれていない
- [x] 同期後に不要な依存関係が発生していないか — 同期先から dev-process-improvement への機能的な参照・依存なし。メタデータ（同期元の記載）は情報提供のみで依存関係を形成しない

## 課題起票
- 起票件数: 2 件（`07_issues.md` に起票済み）

## 同期中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 同期時のロール名適応パターン | 同期チェックリスト | 同期元と同期先でセッション構成が異なる場合（L1/L2 vs dev_manager/specialist）、テンプレート内のロール名を機械的に置換するのではなく、同期先のコンテキストに合わせた意味的な適応が必要。今回は L1→dev_manager, L2(実施)→specialist role, L2(評価)→evaluator role と適応した |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | commit-message.md の2系統共存 | 同期先では Conventional Commits（コード変更用）とセッションプレフィックス（管理作業用）の2系統が共存する形になった。使い分けガイドを追記したが、実運用で混乱が生じないか経過観察が必要 |
| 2 | sessions/_template/ と sessions/initiatives/_template/ の共存 | 同期先では既存テンプレート（openspec 開発向け）と initiatives テンプレート（施策管理向け）が並存する。用途が異なるため問題ないが、将来的な統一を検討する余地がある |

---
**作成者**: sync-worker
**作成日**: 2026-03-08
