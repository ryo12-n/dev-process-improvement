# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox | 完了 |
| TG-002 | backlog | 完了 |
| TG-004 | CSV | 完了 |
| TG-005 | initiatives | 完了 |
| TG-006 | backlog関係性分析 | 完了 |
| TG-007 | rules/workflow整合性 | 完了 |
| TG-008 | セッション構造ポリシーチェック | 完了 |

---

## TG-001: inbox 走査

### 非ref アイテム（4件）

| ファイル名 | 分類 | 根拠 |
|-----------|------|------|
| `課題管理とinbox管理の方法見直し.md` | backlog候補 | ユーザー起票。CSV運用改善の提案（課題詳細ファイルを別ディレクトリで管理）。backlog としてプロセス改善施策に位置づけるのが適切 |
| `triage-handoff-20260306.md` | 処理済み・削除候補 | 前回トリアージからの申し送り3件。ISS-017/018の4回目未着手（TG-004で対処）、backlog施策化率0%（TG-002/TG-005で確認）、claude-directory最適化の分離維持（TG-002で確認）。全件今回トリアージの走査スコープに含まれており処理済み |
| `triage-session-todo-tracking.md` | backlog候補 | triage-manager SKILL.md へのtodo管理ステップ追加提案。l1-manager への横展開可能性あり。改善提案として backlog に起票が適切 |
| `ルートリポのトリアージにTG-008相当の走査観点を追加.md` | backlog候補 | ルートリポ（ai-driven-dev-patterns）側トリアージへの TG-008 横展開。対象リポが異なるため独立 backlog として管理が適切 |

### ref アイテム（4件）

| ファイル名 | 状態 | refs/ 実体 |
|-----------|------|-----------|
| `ref_ai-functions.md` | 安定保持 | `refs/ai-functions/` 存在確認済み |
| `ref_個人PCローカル環境構築-手順書.md` | 安定保持 | `refs/個人PCローカル環境構築-手順書.md` 存在確認済み |
| `ref_openspec-official-summary.md` | 安定保持 | `refs/openspec-official-summary.md` 存在確認済み |
| `ref_ai-driven-development-poc.md` | 安定保持 | `refs/ai-driven-development-poc/` 存在確認済み |

---

## TG-002: backlog 棚卸し

### 概要
- backlog ファイル数（テンプレート・README除く）: 28件
- 全件ステータス: 候補（施策化着手 0件）
- 施策化済み（_archive突合）: 0件（backlog名と_archive名の完全一致なし）
- `claude-directory最適化` は _archive に同名ディレクトリが存在 → backlog ファイルは不在のため既にクリーンだが、README テーブルに行が残存

### README.md 不整合

| # | 種別 | 対象 | 現状 | 修正方針 |
|---|------|------|------|---------|
| 1 | ファイル不在 | `triage-evaluator対称性改善.md` | README記載あり、ファイルなし | ISS-036/037 で対応済みのため不要化。README から行を削除 |
| 2 | ファイル不在 | `triageテンプレートのブラッシュアップ.md` | README記載あり、ファイルなし | `ai-driven-dev-patternsトリアージプロセスのブラッシュアップ.md` と混同の可能性あるが、スコープが異なる（前者は dev-process-improvement 側テンプレート、後者は ai-driven-dev-patterns 側プロセス）。ファイルを再作成するか、README から削除するかユーザー判断 |
| 3 | ファイル不在 | `トリアージ情報欠損リスク評価ステップ追加.md` | README記載あり、ファイルなし | TG-009 として実装済み（triage-worker.md, triage-manager.md に組み込み済み）。不要化のため README から行を削除 |
| 4 | README未記載 | `roles-agents移行(ai-driven-dev-patterns).md` | ファイル存在、READMEに行なし | README テーブルに行を追加 |
| 5 | 施策化済み残存 | `claude-directory最適化.md`（READMEのみ） | READMEに行あり、ファイルは不在。_archive に同名施策あり | 施策化済み・アーカイブ済みのため README から行を削除 |

### 施策化済みチェック結果
- initiatives/ に進行中施策: 0件
- initiatives/_archive/ と backlog の完全名一致: 0件
- 削除候補: なし（README不整合の修正のみ）

---

## TG-004: CSV 棚卸し

### ステータス別集計

| ステータス | 件数 | 対象ISS |
|-----------|------|---------|
| クローズ | 21件 | ISS-001〜005, 007〜012, 014, 015, 023〜025, 028〜030, 034, 035 |
| 起票 | 15件 | ISS-006, 013, 016〜022, 026, 027, 032, 033, 036, 037 |
| 方針確定 | 1件 | ISS-031 |

### 起票ステータス課題の棚卸し

| ISS | タイトル | 回数未着手 | 対応方針案・推奨 |
|-----|---------|----------|---------------|
| ISS-006 | ロール定義の openspec 統合 | - | 保留妥当（openspec ライフサイクル未定義が前提） |
| ISS-013 | Agent Teams 機能の worktree ガイドライン言及 | - | 保留妥当（低優先度。次回改訂時に検討） |
| ISS-016 | m6o-es-product-api の .claude/rules/ 整備 | - | 保留妥当（フェーズ2完了後の後続施策） |
| ISS-017 | settings.json の充実 | **4回** | **推奨: maintenance コミットで即実施。initiative 不要。$schema追加・denyルール設定は30分以内で完了可能。毎回トリアージで棚卸しするコストの方が高い** |
| ISS-018 | rules/ の paths 活用 | **4回** | **推奨: ISS-017 と同時に maintenance コミットで即実施。paths フロントマター追加は軽微作業** |
| ISS-019 | claude-directory-guide.md の skills/ 移動 | - | 保留妥当（ISS-017/018 完了後に検討） |
| ISS-020 | config.yaml tasks ルールのカテゴリ分け | - | 保留妥当（低優先度） |
| ISS-021 | spec 作成時のエッジケース漏れ | - | 保留妥当（低優先度） |
| ISS-022 | spec 作成フェーズのボトルネック | - | 保留妥当（中優先度だがすぐの施策化は不要） |
| ISS-026 | gh CLI 未インストール | - | 保留妥当（環境制約） |
| ISS-027 | Claude Code Web 1セッション=1リポ制約 | - | 保留妥当（環境制約） |
| ISS-032 | CSV ステータス同期漏れ | - | backlog候補として検討推奨。根本原因対策が必要 |
| ISS-033 | 成功基準とCSV対応方針案のスコープ整合 | - | 保留妥当（低優先度の知見） |
| ISS-036 | triage-worker.md 知見記録テーブル未定義 | 1回 | **対応済み確認**: triage-worker.md スキャンレポートテンプレートに「ルール化候補」「参考情報」分類テーブル追加済み。クローズ推奨 |
| ISS-037 | triage-evaluator.md 知見記録・担当ファイル | 1回 | **対応済み確認**: (1) 知見記録セクション追加済み (2) 02_scan_plan.md 読み取り対象追加済み。クローズ推奨 |

### 方針確定ステータスの確認

| ISS | タイトル | 方針 | 現状 |
|-----|---------|------|------|
| ISS-031 | inbox/backlog 二重構造 | 二重構造を許容。README でスコープ明記 | 方針通り運用中。変更不要 |

---

## TG-005: initiatives 状態確認

### 進行中施策
- 該当なし（initiatives/ 配下に _archive/ と _template/ のみ）

### アーカイブ確認
- _archive/ 内: 35件の完了済み施策
- 未アーカイブの完了済み施策（08_gate_review.md が「通過」判定で initiatives/ 直下に残存）: 0件

---

## TG-006: backlog 関係性分析

### 関係性テーブル

| # | 関係種別 | アイテムA | アイテムB | 関係の詳細 | 推奨 |
|---|---------|----------|----------|-----------|------|
| 1 | 統合候補 | ルール変更施策の標準タスクパターン化 | workflow-md更新プロセス整備 | 両方ともルール変更時の連動更新パターンを扱う。前者は「調査->文書化->ルール反映->workflow更新」のパターン化、後者は workflow.md 更新漏れ防止。スコープが大きく重複 | 統合して1施策にする |
| 2 | 統合候補 | TG-008チェック基準のルール変更連動更新 | ルール変更施策の標準タスクパターン化 | 前者はTG-008基準の連動更新、後者はルール変更全般のパターン化。前者を後者に包含可能 | 3件統合（#1と合わせて） |
| 3 | 統合候補 | 関連ファイル一覧セクション横展開 | ルール変更施策の標準タスクパターン化 | 関連ファイル一覧は連動更新の仕組みの一部。標準タスクパターンの中で横展開を実施可能 | 3件統合に含める |
| 4 | 依存関係 | claude-directory最適化(ai-driven-dev-patterns) | roles-agents移行(ai-driven-dev-patterns) | roles-agents移行によるディレクトリ構成変更が claude-directory最適化に影響。移行を先に実施すべき | roles-agents移行 -> claude-directory最適化 |
| 5 | 依存関係 | ai-driven-dev-patternsの設計プロセス整備 | ai-driven-dev-patternsトリアージプロセスのブラッシュアップ | トリアージプロセスは設計プロセスの一部。設計プロセス整備を先に実施すべき | 設計プロセス整備 -> トリアージブラッシュアップ |
| 6 | 依存関係 | 長文rulesのコンテキストコスト最適化 | claude-directory最適化(ai-driven-dev-patterns) | 長文 rules の skills 化は claude-directory 最適化の一部として実施可能 | 順序なし（並行可能だが関連性あり） |
| 7 | 重複候補 | ガイドラインとルールファイルの二重管理リスク対策 | リネーム施策メタルール横断検証スコープ拡大 | 両方ともルール文書の整合性維持を扱う。二重管理リスクとメタルール横断検証は別アプローチだが目的は類似 | 統合ではなく順序付け（二重管理リスク -> メタルール横断検証） |
| 8 | 重複候補 | backlogテンプレート凡例強化 | triageテンプレートのブラッシュアップ（README記載・ファイル不在） | backlogテンプレートとtriageテンプレートは別対象だが、テンプレート改善という共通テーマ | 別施策として維持（対象が異なるため） |

### 統合推奨

**「ルール変更連動更新」統合施策**: 以下の3件（+1件）を1つの施策に統合することを推奨:
1. `ルール変更施策の標準タスクパターン化.md`
2. `workflow-md更新プロセス整備.md`
3. `TG-008チェック基準のルール変更連動更新.md`
4. `関連ファイル一覧セクション横展開.md`（関連度高。含めるかはユーザー判断）

理由: 4件とも「ルール変更時に何を連動更新すべきか」という同一の根本課題を扱っている。個別施策では重複作業が発生する。

---

## TG-007: rules/workflow 整合性確認

### 乖離リスト

| # | 箇所 | skills/agents 側 | workflow.md 側 | 重大度 | 推奨 |
|---|------|-----------------|---------------|--------|------|
| 1 | トリアージ課題起票フロー | triage-worker/evaluator は 07_issues.md に起票 -> マネージャーが集約・CSV転記（triage-manager SKILL.md, triage-worker.md, triage-evaluator.md） | 「CSVに直接起票します」（126行目付近の課題起票の考え方セクション） | 高 | workflow.md の記述を更新。07_issues.md 経由のフローに書き換え |
| 2 | triage-worker 壁打ち記録先 | 02_scan_plan.md に記録（triage-worker.md 30行目付近） | 「02_work_log.md」と記載（triage-standard-policy SKILL.md 56行目） | 中 | triage-standard-policy SKILL.md の記録先ファイル対応テーブルを確認・修正（実装は 02_scan_plan.md が正） |
| 3 | ゲート判定ステップ | triage-manager SKILL.md に 04_gate_review.md 作成ステップあり | workflow.md のトリアージフローに明示的なゲート判定ステップなし（「PR でまとめてレビュー・承認」のみ） | 中 | 継続確認事項。前回から未修正。workflow.md のトリアージフローに 04_gate_review.md 作成ステップを追加すべき |
| 4 | triage-manager 壁打ち | 事前調査（00_pre_investigation.md）が壁打ちフェーズに相当（triage-standard-policy SKILL.md 36行目） | workflow.md のトリアージフロー ステップ1 に記載あり | 低 | 整合。問題なし |

### 継続確認事項
- ゲート判定ステップの workflow.md 未追加は前回トリアージ（20260306）から継続。ISS-034/035 はクローズ済みだが、triage-manager の 04_gate_review.md に関する同種の乖離が残存

---

## TG-008: セッション構造標準ポリシーチェック

### 走査結果サマリ
- 走査対象ファイル数: 6件（roles/ は存在しないため対象外）
- 不適合件数: 3件（必須: 0件 / 推奨: 1件 / 軽微: 2件）

### ファイル別チェック結果

| ファイル | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール | 総合判定 |
|---------|:-------------:|:----------:|:--------:|:----------:|:-------:|
| l1-manager/SKILL.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-worker.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-evaluator.md | OK（軽微注記あり） | OK | OK | OK | OK |
| triage-manager/SKILL.md | OK | OK | OK | OK | OK |
| triage-manager/agents/triage-worker.md | OK | OK | OK | OK | OK |
| triage-manager/agents/triage-evaluator.md | OK | OK | OK（推奨注記あり） | OK | OK |

### ISS-036/037 対応状況

| ISS | 内容 | 対応状況 | 推奨 |
|-----|------|---------|------|
| ISS-036 | triage-worker.md 知見記録分類テーブル | 対応済み: スキャンレポートテンプレートに「ルール化候補」「参考情報」テーブル追加 | CSV クローズ |
| ISS-037 | triage-evaluator.md 知見記録・担当ファイル | 対応済み: (1) 評価レポートテンプレートに「評価中の知見」セクション追加 (2) 担当ファイルテーブルに 02_scan_plan.md 追加 | CSV クローズ |

### 不適合の詳細

| # | ファイル | チェック項目 | 不適合内容 | 重大度 | 対応 |
|---|---------|------------|----------|--------|------|
| 1 | l2-evaluator.md | D. 担当ファイルテーブル | `03_work_log.md` が読み取り対象として未記載。実務上は `04_work_report.md` が主な評価対象だが、壁打ちフェーズの記録確認や作業経緯の参照で必要になる場合がある | 軽微 | セッション内修正可能 |
| 2 | triage-evaluator.md | C. 課題起票 | CSV 直接起票を行わない旨は明記されているが、07_issues.md への起票手段の記載が「やること」セクションにのみあり、「課題起票」の専用セクション（l2-evaluator の「課題のCSV転記」に相当）がない | 推奨 | 07_issues.md に起票する旨は明記されており機能的問題はない。「やること」セクションに記載あるため緊急ではないが、他ロール定義との対称性向上のため専用セクション追加を推奨 |
| 3 | triage-standard-policy SKILL.md | 1.3 記録先テーブル | triage-worker の壁打ち記録先が「02_work_log.md」だが、実装は「02_scan_plan.md」 | 軽微 | セッション内修正可能（基準文書の記録先テーブルを修正） |

---

## TG-009: 情報欠損リスク評価

削除・統合候補として検出されたのは backlog/README.md の不整合行（ファイル不在3件 + 施策化済み1件）のみ。これらは README テーブルの行削除であり、backlog ファイル自体の削除・統合ではない。

TG-006 の統合候補（ルール変更連動更新4件）は backlog アイテムの統合提案であり、ファイル削除を伴わない（統合後も新施策として管理される）。

**削除・統合候補なし：スキップ**

---

## 課題起票

- 起票件数: 2 件（`07_issues.md` に起票済み）
- workflow.md のトリアージ課題起票フロー乖離（07_issues.md に起票済み）
- triage-standard-policy SKILL.md の記録先テーブル不整合（07_issues.md に起票済み）

---

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | ISS-017/018 のような軽微タスクは initiative 必須化ルールの例外として maintenance コミットで即実施すべき | CLAUDE.md「施策管理の必須化」 | 4回連続未着手は initiative ルールが軽微タスクの即時対応を阻害している証拠。CLAUDE.md に「maintenance コミットで対応可能な軽微修正は initiative 不要」の例外を明記すべき |
| 2 | トリアージで繰り返し検出される同一乖離は maintenance コミットでの即時修正を標準化すべき | triage-manager SKILL.md | ゲート判定ステップの workflow.md 未追加が複数回検出されている。「CRITICAL かつ軽微修正可能」な乖離はトリアージセッション内で maintenance コミットとして修正するルールを明確化すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | backlog 施策化率 0% が継続しており、backlog が「参照されない todo リスト」化するリスクがある | 前回申し送りでも指摘。着手可能な施策の優先順位付けが必要 |
| 2 | ルール変更連動更新系の backlog が4件に膨らんでおり、統合による複雑性削減が有効 | TG-006 分析で3つの統合候補組を検出 |
| 3 | ISS-036/037 は前回起票から今回までに対応済み。CSVステータスの同期漏れパターン（ISS-032）の実例 | ルール修正時に CSV ステータスを同時に更新するフローが未整備であることの傍証 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-07
