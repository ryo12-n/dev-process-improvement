# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox | 完了 |
| TG-002 | backlog | 完了 |
| TG-003 | CSV | 完了 |
| TG-004 | initiative | 完了 |
| TG-005 | backlog 関係性分析 | 完了 |
| TG-008 | skills/agents ポリシーチェック | 完了 |
| TG-009 | 情報欠損リスク評価 | スキップ（削除・統合候補なし） |

---

## TG-001: inbox 走査

### 未処理アイテム一覧（6件）

| アイテム | 種別 | 判断 | 理由 |
|---------|------|------|------|
| 2つのリポジトリの部分的同期.md | 新規提案 | backlog候補（中） | dev-process-improvement のディレクトリ構成改善（sessions ディレクトリ導入、triage archive、テンプレートコピー改善）と ai-driven-dev-patterns への横展開を含む中規模施策。具体的なスコープが明確で施策化可能 |
| ai-driven-dev-patterns_source-of-truth明示.md | 新規提案（施策由来） | backlog候補（中） | design-process-setup 施策の gate_review から起票。ai-driven-dev-patterns の CLAUDE.md に Source of Truth 明示ルールを追加する改善提案。L2-evaluator も同一課題を指摘しており妥当性が高い |
| ref_ai-driven-development-poc.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |
| ref_ai-functions.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |
| ref_openspec-official-summary.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |
| ref_個人PCローカル環境構築-手順書.md | ref ポインター | 対応不要（安定保持） | 前回確認済み。「参照のみ保持」方針確定。変更なし |

### 新規 inbox エントリ詳細分析

#### 2つのリポジトリの部分的同期.md

- **内容**: dev-process-improvement に sessions ディレクトリを導入し triage/initiatives の作業履歴を管理。triage の archive ディレクトリ追加。空テンプレートが作業履歴に残らないようコピー方法改善。完了後に ai-driven-dev-patterns にも同等機能を展開し、チェックリスト整備
- **対象リポジトリ**: dev-process-improvement（主）→ ai-driven-dev-patterns（横展開）
- **施策規模**: 中〜大（ディレクトリ構成変更+運用改善+横展開）
- **推奨優先度**: 中（現行運用に実害はないが構成改善として有効）
- **推奨施策名**: 「2つのリポジトリの部分的同期」

#### ai-driven-dev-patterns_source-of-truth明示.md

- **内容**: ai-driven-dev-patterns の CLAUDE.md と roles/dev_manager.md に知見ルーティングテーブルが重複。dev-process-improvement と同様に「roles/ 配下が正の情報源」と .claude/rules/ に明記する
- **対象リポジトリ**: ai-driven-dev-patterns
- **施策規模**: 小（ルール追加1件）
- **推奨優先度**: 中（将来的な乖離リスク防止）
- **推奨施策名**: 「ai-driven-dev-patterns_source-of-truth明示」

---

## TG-002: backlog 棚卸し

### backlog.csv とファイル実体の突合

| # | 突合結果 | 施策名 | 詳細 |
|---|---------|--------|------|
| 1 | ファイル不在 | 課題管理とinbox管理の方法見直し | CSV に「（ファイル不在）」と記載。initiatives/_archive/ に施策化済み（完了・アーカイブ済み）。CSV からの削除が推奨 |
| 2 | ファイル不在 | ai-driven-dev-patternsの設計プロセス整備 | CSV にファイル名 `ai-driven-dev-patternsの設計プロセス整備.md` だが backlog/ に実体なし。initiatives/_archive/design-process-setup として施策化済みの可能性あり（名前が異なるため要確認） |
| 3 | ファイル不在 | ai-driven-dev-patternsトリアージプロセスのブラッシュアップ | CSV にファイル名 `ai-driven-dev-patternsトリアージプロセスのブラッシュアップ.md` だが backlog/ に実体なし |

### 施策化済みチェック（initiatives/_archive/ との突合）

| # | backlog 施策名 | _archive 内の対応施策 | ステータス | 推奨アクション |
|---|---------------|---------------------|----------|-------------|
| 1 | 課題管理とinbox管理の方法見直し | 課題管理とinbox管理の方法見直し（完全一致） | 施策化済み・アーカイブ済み | CSV エントリを削除 |
| 2 | ai-driven-dev-patternsの設計プロセス整備 | design-process-setup（名前異なるが対応施策と推定） | 施策化済み・アーカイブ済み | CSV エントリを削除（要ユーザー確認） |
| 3 | ai-driven-dev-patternsトリアージプロセスのブラッシュアップ | triage-process-brushup（名前異なるが対応施策と推定） | 施策化済み・アーカイブ済み | CSV エントリを削除（要ユーザー確認） |

### backlog 変動（前回トリアージ以降）

前回トリアージ（20260307-3）以降、backlog ファイルの追加・変更なし。

---

## TG-003: CSV 課題管理（起票11件 + 方針確定1件）

### ステータス「起票」の課題（11件）

| ISS-ID | タイトル | 起票日 | 経過回数 | 対応方針案 |
|--------|---------|--------|---------|----------|
| ISS-006 | ロール定義と OpenSpec 開発ライフサイクルの統合が未定義 | 02-23 | 多数 | **保留継続**: OpenSpec ライフサイクルが未定義のため着手不可。OpenSpec 関連施策の進展待ち。ステータス「起票」のまま維持 |
| ISS-013 | Claude Code Agent Teams 機能が worktree ガイドラインで言及されていない | 02-25 | 多数 | **保留継続**: Agent Teams は実験的機能。ガイドライン次回改訂時に追記予定。低優先度のため急がない |
| ISS-016 | m6o-es-product-api の .claude/rules/ 向けルールファイル整備 | 02-27 | 多数 | **保留継続**: m6o-es-product-api 側の作業。dev-process-improvement 側では追跡のみ。着手タイミングは別途判断 |
| ISS-019 | claude-directory-guide.md の skills/ 移動検討 | 02-27 | 多数 | **保留継続**: 現時点で rules/ ファイルは commit-message.md + session-start-branch-cleanup.md のみでコンテキスト圧迫は軽微。skills 増加時に再検討 |
| ISS-020 | config.yaml の tasks ルールのカテゴリ分けが CLI ツールに適合しない | 02-28 | 多数 | **保留継続**: OpenSpec 関連。openspec-code-trial の知見。次回 OpenSpec 利用時に反映を検討 |
| ISS-021 | spec 作成時にエッジケース・境界条件のシナリオが漏れやすい | 02-28 | 多数 | **保留継続**: OpenSpec 利用時のガイドライン改善提案。次回 OpenSpec 利用時に反映を検討 |
| ISS-022 | spec 作成フェーズが openspec サイクルのボトルネック | 02-28 | 多数 | **保留継続**: OpenSpec のプロセス改善知見。ISS-020/021 と同じく次回 OpenSpec 利用時に検討 |
| ISS-027 | Claude Code Web は1セッション=1リポジトリの制約がある | 03-02 | 多数 | **保留継続**: プラットフォーム制約の記録。ローカル環境に移行済みのため実害なし。Claude Code のマルチリポ対応時に再検討 |
| ISS-032 | CSV ステータスの同期漏れパターン | 03-04 | 3回 | **施策化検討**: トリアージの走査ステップにCSVステータス更新確認を追加する提案。backlog「トリアージセッションのtodo管理義務化」と関連。統合して施策化を推奨 |
| ISS-033 | 成功基準と CSV 対応方針案のスコープ整合 | 03-04 | 3回 | **保留継続**: l1-manager の成功基準作成時のガイドライン改善提案。低優先度で単独施策化は不要。l1-manager 改訂時に併せて対応 |
| ISS-038 | CSV列追加時に全既存行の列数整合性を検証すべき | 03-07 | 1回 | **保留継続**: CSV操作の品質チェック知見。手順書に追記するレベル。次回CSV列変更時に対応 |
| ISS-039 | L1クローズ手順で gate_review の Write と git mv の実行順序に注意が必要 | 03-07 | 1回 | **保留継続**: l1-manager.md のクローズ手順に注意書き追加の提案。次回 l1-manager 改訂時に対応 |
| ISS-040 | triage-evaluator 壁打ちフェーズの policy 不整合（推奨→必須更新が必要） | 03-07 | 1回 | **要対応**: triage-standard-policy の適用マトリクスを「推奨」→「必須」に更新すべき。軽微修正で対応可能。次回ルール改訂時に実施推奨 |

### ステータス「方針確定」の課題（1件）

| ISS-ID | タイトル | 確定方針 | 対応方針案 |
|--------|---------|---------|----------|
| ISS-031 | inbox/backlog が ai-driven-dev-patterns と dev-process-improvement の両方に存在する二重構造 | 当面は二重構造を許容。README.md でスコープ明記 | **維持**: 方針確定済み。経過観察。統合の必要性が出た場合に再検討 |

### 総括

- 起票11件中、長期保留が多い（ISS-006/013/016/019/020/021/022/027: 8件）
- これらは OpenSpec 関連・プラットフォーム制約・外部リポジトリ関連であり、dev-process-improvement 側で即時対応が困難
- ISS-032 は backlog「トリアージセッションのtodo管理義務化」との統合で施策化を検討する価値あり
- ISS-040 は軽微修正で対応可能

---

## TG-004: initiative 状態確認

### 進行中施策

| 施策名 | フェーズ | 状態 | 特記事項 |
|--------|---------|------|---------|
| （進行中施策なし） | - | - | initiatives/ 直下は _archive/ と _template/ のみ |

### 前回トリアージ以降の変動

- design-process-setup 施策が完了・アーカイブ済み（commit 133c18f）
- triage-process-brushup 施策が完了・アーカイブ済み（commit 5af5313、現ブランチ）

---

## TG-005: backlog 関係性分析

### 重複候補

| # | 施策A | 施策B | 関係性 | 推奨 |
|---|-------|-------|--------|------|
| 1 | ai-driven-dev-patternsトリアージプロセスのブラッシュアップ | ルートリポのトリアージにTG-008走査観点追加 | 部分重複: 両方とも ai-driven-dev-patterns 側トリアージの改善 | 統合検討。ただし前者は CSV 上施策化済み可能性あり（TG-002 参照） |
| 2 | claude-directory最適化(ai-driven-dev-patterns) | roles-agents移行(ai-driven-dev-patterns) | 部分重複: 両方とも ai-driven-dev-patterns の .claude/ 配下構成改善 | 依存順序あり。roles-agents移行を先行し、claude-directory最適化で仕上げる |
| 3 | トリアージセッションのtodo管理義務化 | ISS-032（CSVステータス同期漏れ） | 関連: トリアージ走査ステップの改善 | トリアージセッションのtodo管理義務化に ISS-032 の観点を統合 |

### 依存関係

| # | 先行施策 | 後続施策 | 依存内容 |
|---|---------|---------|---------|
| 1 | roles-agents移行(ai-driven-dev-patterns) | claude-directory最適化(ai-driven-dev-patterns) | roles/ が agents/ に移行後に .claude/ 配下を最適化 |
| 2 | 2つのリポジトリの部分的同期（inbox新規） | リポジトリ間テンプレート同期の検証チェックリスト | sessions ディレクトリ導入後にテンプレート同期チェックリストを策定 |

### 統合候補

| # | 統合対象 | 統合後の施策名案 | 理由 |
|---|---------|---------------|------|
| 1 | ガイドラインとルールファイルの二重管理リスク対策 + 長文rulesのコンテキストコスト最適化 | ルール管理最適化 | 両方とも rules/ と docs/ の管理方式に関する施策。二重管理リスク対策とコンテキストコスト最適化は同時に検討すべき |

### 対象リポジトリ別分布

| 対象リポジトリ | 件数 | 施策例 |
|-------------|------|--------|
| dev-process-improvement | 16件 | 外部リポ運用ルール、backlogテンプレート凡例強化、リンク整合性チェック等 |
| ai-driven-dev-patterns | 13件 | Claude Code標準skills評価、マルチAIエージェント、ディレクトリ構成最適化等 |
| 横断 | 2件 | LLMローカル開発セキュリティ、長文rulesコンテキストコスト最適化 |

---

## TG-008: セッション構造標準ポリシーチェック

### 走査結果サマリ
- 走査対象ファイル数: 6件
- 前回トリアージ（20260307-3）以降の skills 変更: 0件
- 不適合件数: 1件（推奨: 1件）— 前回から継続

### ファイル別チェック結果

| ファイル | A.ライフサイクル | B.ペアリング | C.課題起票 | D.停止ルール | 総合判定 |
|---------|:-------------:|:----------:|:--------:|:----------:|:-------:|
| l1-manager/SKILL.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-worker.md | OK | OK | OK | OK | OK |
| l1-manager/agents/l2-evaluator.md | OK | OK | OK | OK | OK |
| triage-manager/SKILL.md | OK | OK | OK | OK | OK |
| triage-manager/agents/triage-worker.md | OK | OK | OK | OK | OK |
| triage-manager/agents/triage-evaluator.md | OK（注1） | OK | OK | OK | OK（注1） |

**注1**: triage-evaluator の壁打ちフェーズは triage-standard-policy で「推奨」だが実装では「必須」的に記述。ISS-040 として既に起票済み（前回 20260307-3）。policy 側の更新待ち。

### 前回からの差分

- skills 変更: なし（git log で確認済み）
- 新規 roles/*.md: なし
- 前回検出の不適合（ISS-040）: 未解消（policy 更新待ち）

### 不適合の詳細

| # | ファイル | チェック項目 | 不適合内容 | 重大度 | CSV起票 |
|---|---------|------------|----------|--------|---------|
| 1 | triage-standard-policy/SKILL.md | A.ライフサイクル（適用マトリクス） | triage-evaluator の壁打ちが「推奨」だが実装は「必須」| 推奨 | ISS-040（起票済み・前回から継続） |

---

## TG-009: 情報欠損リスク評価

削除・統合候補なし：スキップ

TG-002 で検出した backlog CSV エントリの削除候補3件は、CSV エントリの削除であり backlog ファイル自体が不在のため情報欠損リスクはない。

---

## 課題起票

- 起票件数: 1 件（`07_issues.md` に起票済み）
- backlog CSV に施策化済みエントリ3件が残存（TG-002 で検出）

---

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | backlog.csv に施策化済みエントリが残存するパターン | backlog/backlog.csv | 施策化後に backlog.md は git rm されるが、CSV エントリの削除漏れが発生。l1-manager のクローズチェックリストに「backlog.csv エントリの削除確認」を追加すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | CSV 起票課題の長期滞留パターン | ISS-006/013/016/019/020/021/022/027 の8件が起票から10日以上経過。OpenSpec 関連・外部依存の課題は起票のまま長期滞留する傾向。「保留」ステータスの追加を検討する価値あり |
| 2 | inbox 新規エントリの施策由来（gate_review 起点）が増加 | design-process-setup の gate_review から ai-driven-dev-patterns_source-of-truth明示.md が起票。l1-manager のクローズ手順の知見ルーティングが機能している証拠 |

---
**作成者**: トリアージワーカー
**作成日**: 2026-03-08
