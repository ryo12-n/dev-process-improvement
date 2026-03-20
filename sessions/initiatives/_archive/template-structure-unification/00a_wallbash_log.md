# 壁打ちログ: テンプレート構造統一改修

> **このファイルの役割**: 壁打ちフェーズのコンテキスト保持用ログ。
> 「現在の合意事項」は毎回上書きし、「イテレーション履歴」は追記する。

---

## 現在の合意事項

### 施策の目的
session-lifecycle-policy §1.4 の基本モデル（multi-phase manager パターン）に initiative テンプレートのポリシー定義を統一する。

### スコープ
**やること**:
- ポリシー・スキル定義・エージェント定義の修正（あるべき姿の定義）
- initiative テンプレートを 2-phase 構造（phase-1-planning / phase-2-execution）に再設計
- ワーカーセットテンプレートを worker 3ファイル（plan/log/report）+ eval 3ファイル（plan/log/report）+ issues に統一
- ファイル番号の連番振り直し（ルート 00〜06、phase 内 01〜連番）
- 並列ディスパッチを set コピー方式に変更（W_template 廃止）

**やらないこと**:
- 実際のテンプレートファイル・ディレクトリ構造の改修（別施策）
- single-phase セッション（triage, meta, bm, auto）の統一（別施策）
- impl の `_template/` sub-dir 導入（別施策）
- 既存セッションインスタンスの遡及変更

### 計画の方向性
1. 新しい initiative テンプレート構造を設計（2-phase + ワーカーセット統一）
2. session-lifecycle-policy §1.4.3 を改訂
3. l1-manager SKILL.md のファイル参照パス・並列ディスパッチ手順を更新
4. エージェント定義（l2-worker, l2-evaluator, l2-plan-worker, l2-plan-evaluator）の担当ファイルテーブルを更新
5. parallel-dev.md を set コピー方式に更新
6. docs/workflow.md を連動更新

### 未解決事項
なし

---

## イテレーション履歴

### Round 1 [2026-03-19]
**入力**: backlog/entries/テンプレート構造統一改修.md（BL-106 起票元）
**調査・推論**:
- 現行 initiative テンプレート（フラット・15ファイル）の構成を確認
- multi-phase 基本モデル（co/sc）との比較を実施
- ファイル名衝突の問題（Phase 2-3 と Phase 4-5 で同一ファイル名再利用）を特定

**議論内容**:
1. 段階的実施 → initiative から着手（single-phase, impl は別施策）
2. 既存インスタンス → 変更なし（テンプレートのみ）
3. 2-phase 構造（phase-1-planning / phase-2-execution）を提案 → 合意
4. ブランチ名 `initiative/template-structure-unification` → 合意

### Round 2 [2026-03-19]
**入力**: ファイルプレフィックスの連番振り直し・W_template 廃止の提案
**議論内容**:
1. 連番振り直し → ルート 00〜06、phase 内 01〜連番で合意
2. W_template 廃止 → `_template/` を set-N/ にコピーする方式で合意
3. 指示文書の修正が必要 → 影響範囲を整理

### Round 3 [2026-03-19]
**入力**: 番号順序・ワーカーセットテンプレート構成の詳細化
**議論内容**:
1. `00_wallbash_log.md` → `01_proposal.md` の順序 → 壁打ちが先、提案がその成果で整合
2. `task_division.md` は phase-1 の成果物なので連番最後（08）に配置
3. manager が 03_tasks.md を作成 → plan-worker が詳細分割して 08_task_division.md を出力 → manager が参照してディスパッチ
4. ワーカーセットテンプレートに worker/eval 各3ファイル（plan/log/report）を配置:
   - plan: 着手前のタスク理解・不明点解消
   - log: 作業中の判断背景・つまづきの記録
   - report: plan+log+成果物の振り返り・課題発見

### Round 4 [2026-03-19]
**入力**: スコープ変更 — ポリシー修正のみ（実ファイル改修は別施策）
**議論内容**:
- 本施策: ポリシー・スキル定義・エージェント定義の修正
- 別施策: 実際のテンプレートファイル・ディレクトリ構造の改修
- ポリシーを先に固めて、実装は別施策で確実にやるアプローチで合意

**合意事項の変更**: スコープを「ポリシー修正のみ」に限定

---
**作成日**: 2026-03-19
**施策ブランチ**: initiative/template-structure-unification
