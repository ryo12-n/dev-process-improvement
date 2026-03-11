# 評価計画: 2026-03-12 同期

## 壁打ちフェーズ [2026-03-12 11:00]

### 理解のサマリー
- 評価の目的: ワーカーが実施した dev-process-improvement → ai-driven-dev-patterns 同期（A-1〜D-3、計13項目、9ファイル）の品質を repo-sync-checklist セクション5 の7つの検証観点で評価する
- 評価スコープ: ターゲットリポジトリ（ai-driven-dev-patterns）の9ファイルの同期結果、および 04_sync_report.md の判断品質
- 完了条件: (1) 06_eval_report.md に7観点の PASS/FAIL/N/A 判定 (2) マネージャーへの推奨明記 (3) 知見セクション最低1行 (4) 課題があれば 07_issues.md に起票

### 前提条件チェック
- [x] 評価対象（04_sync_report.md）の完成度: 十分（全13項目のステータスと判断理由が記載済み）
- [x] 評価基準（repo-sync-checklist セクション5）の明確さ: 評価可能（7観点とも具体的なチェック項目あり）
- [x] 同期元・同期先リポジトリへのアクセス: 確認済み（双方のファイル読み取りに成功）

### 不明点・確認事項
なし

### マネージャー確認結果
確認事項なし：評価開始

---

## 評価計画

### 評価基準

repo-sync-checklist セクション5 の7つの検証観点を使用する。

### パラメータ具体化

- 同期元（{source_repo}）: dev-process-improvement (`/home/nr202/projects2/dev-process-improvement/`)
- 同期先（{target_repo}）: ai-driven-dev-patterns (`/home/nr202/projects2/ai-driven-dev-patterns/`)
- 同期スコープ（{sync_scope}）: 以下の9ファイル
  1. `.claude/rules/pr-url-output.md`（新規作成 A-2）
  2. `.claude/rules/commit-message.md`（編集 B-1）
  3. `.claude/skills/dispatcher/session-start-branch-cleanup.md`（編集 A-1）
  4. `.claude/skills/dispatcher/SKILL.md`（編集 C-1〜C-5）
  5. `.claude/skills/rule-change-checklist/SKILL.md`（編集 B-2）
  6. `.claude/skills/session-flow-policy/SKILL.md`（編集 B-3）
  7. `.claude/skills/triage/triage-evaluator.md`（編集 D-1）
  8. `.claude/skills/triage/triage-manager.md`（編集 D-2）
  9. `.claude/skills/triage/triage-worker.md`（編集 D-3）

### 評価項目と検証方法

| # | 検証観点 | 検証方法 | 判定基準 |
|---|---------|---------|---------|
| 1 | ファイル存在性 | ターゲットの9ファイルの存在を ls/Read で確認 | 全9ファイルが存在すること |
| 2 | 内容一致性 | 統一すべきポイント（A-1, A-2, B-1〜B-3）の内容をソースと突合。概念移植（C, D）は適応内容の反映を確認 | 差異許容ポイント以外に意図しない差異がないこと |
| 3 | 構造整合性 | ターゲットのディレクトリ階層・ファイル命名規則を確認 | 既存構造を尊重し、追記ベースで反映されていること |
| 4 | 参照整合性 | 9ファイル内のパス参照をターゲットのディレクトリ構造と突合 | 全パス参照が有効であること |
| 5 | ポリシー準拠性 | ターゲットの CLAUDE.md と同期結果を突合 | ポリシー違反がないこと |
| 6 | 差異許容の妥当性 | 04_sync_report.md セクション2 の判断理由を検証 | 各判断に合理的理由があること |
| 7 | 連動更新の完全性 | 各ファイルの関連ファイル一覧の更新状態を確認 | 連動更新が漏れなく実施されていること |

### 重点検証項目（マネージャー指示）

- 概念移植の適応品質: L1/L2 用語がターゲットに残存していないか
- パス参照の有効性: ターゲットのディレクトリ構造で有効なパスか
- dispatcher/SKILL.md の肥大化度合い
- commit-message.md の後方互換性（既存 triage タイプが保持されているか）
- ターゲット既存ポリシー（CLAUDE.md）との整合性

---
**作成者**: sync-evaluator
**作成日**: 2026-03-12
