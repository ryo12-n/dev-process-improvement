# トリアージ振り返りレポート: 2026-03-09

## サマリ

前回トリアージ（20260308-2）から1日後の定期トリアージ。inbox に13件の新規気づきエントリが蓄積。backlog 候補 7件、ルール反映 3件、軽微修正 1件、却下 1件、判断保留 3件に分類。backlog CSV/ファイル整合性で施策化済みCSV残存 4件を検出（ISS-041 の再発パターン）。ワーカーエージェントがコンテキスト制約で成果物未出力のため、マネージャーが代理実施した。

## Worker Set サマリ

| Set | 担当 TG タスク | 評価結果 | 備考 |
|-----|--------------|---------|------|
| set-1 | TG-001〜005 | マネージャー代理実施 | ワーカーエージェントは壁打ちのみ完了。evaluator スキップ |

## 走査結果

### inbox

| アイテム | 判断 | 理由 |
|---------|------|------|
| L2知見発見と修正適用のギャップ改善.md | backlog候補 | L2-worker の知見発見と修正適用のギャップ。プロセス本質的課題 |
| agentsの管理方法のガイドライン追記.md | backlog候補 | エージェント管理ベストプラクティスのガイドライン化 |
| backlog-ideas-md整理.md | 軽微修正 | triage-manager 担当ファイルの ideas.md 参照削除。セッション内修正 |
| disallowedToolsフィールド活用検討.md | backlog候補 | deferred tools 制限の代替案。ISS-047 と関連 |
| entries-pattern-inbox適用検討.md | 判断保留 | inbox ファイル数が少なく entries/ パターンの必要性低い |
| metacognition-managerの記述構造統一検討.md | backlog候補 | metacognition-manager に知見集約・課題集約の独立セクション追加 |
| rule-change-checklist_deny対称性チェック追加.md | ルール反映 | ISS-050 直結。rule-change-checklist への項目追加 |
| triage-metacognition テンプレート共通化検討.md | 判断保留 | 前回保留継続。2セッションタイプのみでコスト対効果低い |
| エージェント名ケバブケース規則.md | ルール反映 | Claude Code agents の命名制約を session-flow-policy に追記 |
| ゲート判定基準での課題重大度の明文化.md | backlog候補 | manager-common-policy §4 への重大度判断明文化 |
| フォーマット変換の内容同等性基準.md | backlog候補 | フォーマット変換時の省略可/不可基準の明確化 |
| ルール分離テーマ別分割パターン.md | backlog候補 | 1ファイル1テーマ原則。長文rules最適化と統合推奨 |
| 共通ポリシー参照のblockquote形式標準化.md | 却下 | 既に実装済み。追加アクション不要 |
| 複数リポジトリ施策のPR作成漏れ防止.md | ルール反映 | l1-manager クローズ手順にPR作成確認チェック追加 |
| 適用マトリクス列数増加リスク.md | 判断保留 | 前回保留継続。4セッションタイプ目追加時に再検討 |

### backlog 棚卸し

#### CSV/ファイル整合性

| # | 施策名 | 問題 | 推奨アクション |
|---|--------|------|-------------|
| 1 | 外部リポジトリ変更時のブランチ・PR運用ルール整備 | 施策化済み（CSV残存） | CSV行削除 |
| 2 | ガイドラインとルールファイルの二重管理リスク対策 | 施策化済み（CSV残存） | CSV行削除 |
| 3 | README整合性チェック | 施策化済み（CSV残存） | CSV行削除 |
| 4 | inboxと課題管理とbacklogを管理方法見直し(v2) | 施策化済み（CSV残存） | CSV行削除 |
| 5 | 社内施策_devkitスペシャリストロール作成 | CSVファイル名不一致 | CSV修正 |
| 6 | claude-directory最適化(ai-driven-dev-patterns) | 施策化済み（前回報告・未回答） | ユーザー確認後CSV行削除 |

### 課題管理 CSV（未対応課題）

#### 高優先度

| ID | タイトル | 対応状況 |
|----|---------|---------|
| ISS-027 | Claude Code Web 1セッション=1リポ制約 | 環境制約。当面対応不可 |

#### ブロック中（前提条件待ち）

| ID | タイトル | ブロック理由 |
|----|---------|-----------|
| ISS-006 | ロール定義とOpenSpecの統合が未定義 | openspec 開発ライフサイクル待ち |
| ISS-016 | .claude/rules/ 向けルールファイル整備 | フェーズ2完了待ち |

#### 関連課題グループ（rule-change-checklist 改善）

| ID | タイトル | 優先度 |
|----|---------|--------|
| ISS-042 | grep 検証の走査対象漏れ | 中 |
| ISS-048 | deny リストの Read/Write/Edit 網羅性 | 低 |
| ISS-050 | Read/Write/Edit 3ツール網羅的考慮 | 中 |

### backlog 関係性分析（TG-005）

| アイテムA | アイテムB | 関係種別 | 詳細 | 提案 |
|----------|----------|---------|------|------|
| ルール分離テーマ別分割パターン（inbox） | 長文rulesのコンテキストコスト最適化 | 重複候補 | 同じ問題の異なるアプローチ | 長文rules施策に統合 |
| metacognition-manager記述構造統一（inbox） | triage-metacognition テンプレート共通化（inbox保留） | 重複候補 | 構造統一 vs テンプレート共通化 | 同時着手推奨 |
| disallowedTools活用（inbox） | Claude Code標準skills評価 | 依存関係 | 仕様理解が評価に影響 | disallowedTools先行 |
| ai-driven-dev-patterns_source-of-truth明示 | ai-driven-dev-patterns-triage-standard-policy作成 | 依存関係 | SoT明示がポリシー作成の前提 | SoT先行 |
| backlog-archive-matching改善 | backlogテンプレート凡例強化 | 依存関係 | 突合改善がテンプレートに影響 | matching先行 |
| rule-change-checklist_deny対称性（inbox） | denyリスト変更副作用分析必須化 | 統合候補 | 共に rule-change-checklist 改善 | 1施策に統合 |
| L2知見発見ギャップ改善（inbox） | ゲート判定基準の課題重大度明文化（inbox） | 統合候補 | 知見→アクション変換の改善 | 1施策に統合検討 |

### initiative 状態確認

進行中施策 0件。全施策アーカイブ済み。

## backlog 追加・変更案

### 追加候補

| 優先度 | 施策名 | 課題概要 | 期待効果 |
|--------|--------|---------|---------|
| 中 | L2知見発見と修正適用のギャップ改善 | L2が知見発見しても修正に反映されないギャップ | プロセスの知見→改善変換率向上 |
| 低 | agentsの管理方法のガイドライン追記 | エージェント管理ベストプラクティスの文書化 | エージェント設計の品質向上 |
| 低 | disallowedToolsフィールド活用検討 | deferred tools 制限の代替手段 | SDK環境でのツール制限実現 |
| 低 | metacognition-managerの記述構造統一 | 知見集約・課題集約の独立セクション化 | セッション間の構造一貫性 |
| 低 | ゲート判定基準での課題重大度の明文化 | 課題重大度判断の暗黙知解消 | ゲート判定の透明性向上 |
| 低 | フォーマット変換の内容同等性基準 | 変換時の省略可/不可基準の明確化 | フォーマット変換品質の向上 |
| 低 | ルール分離テーマ別分割パターン | 長文rules最適化と統合 | 既存backlog「長文rulesのコンテキストコスト最適化」に統合推奨 |

### 優先度変更候補

なし

### 削除・クローズ候補

| 施策名 | 理由 |
|--------|------|
| 外部リポジトリ変更時のブランチ・PR運用ルール整備 | 施策化済み（_archive/external-repo-branch-pr-rules） |
| ガイドラインとルールファイルの二重管理リスク対策 | 施策化済み（_archive/docs-dual-management-prevention） |
| README整合性チェック | 施策化済み（_archive/readme-consistency-check） |
| inboxと課題管理とbacklogを管理方法見直し(v2) | 施策化済み（_archive/課題管理とinbox管理の方法見直し） |
| claude-directory最適化(ai-driven-dev-patterns) | 施策化済み（_archive/claude-directory最適化/）※前回報告済み・ユーザー確認待ち |

## 振り返り

### うまくいったこと
- 事前調査の並列エージェント活用で効率的に情報収集できた
- inbox/backlog/CSV の横断的な関係性分析が体系的に実施できた

### 改善すべきこと
- ワーカーエージェントがコンテキスト制約で成果物を書き出せなかった。タスク分割の粒度を検討する必要あり
- ISS-041（施策化済みCSV残存）が再発。l1-manager クローズ手順への組み込みが必要

### プロセス改善の気づき
- inbox のbacklog化率は約50%（7/15件）。気づきの質が高い
- 施策化済みCSV残存は構造的問題。手動チェックでは限界がある

### 次回トリアージへの申し送り

- 判断保留3件（entries-pattern-inbox適用, triage-metacognition テンプレート共通化, 適用マトリクス列数増加リスク）を引き続き保持
- claude-directory最適化(ai-driven-dev-patterns) のユーザー確認結果を反映

## 知見集約

### ルール化候補（.claude/rules/ や skills/ に反映できるパターン）

| # | 知見 | 発見元 Set | 対象ファイル・領域 | 詳細 |
|---|------|----------|-----------------|------|
| 1 | triage-manager 担当ファイルに存在しない ideas.md が記載 | set-1 | .claude/skills/triage-manager/SKILL.md | 担当ファイルテーブルから backlog/ideas.md 行を削除 |
| 2 | 施策化済みCSV残存の再発防止 | set-1 | l1-manager / triage-manager | ISS-041。l1 クローズ手順に CSV 行削除ステップ追加推奨 |
| 3 | rule-change-checklist に deny 対称性チェック追加 | inbox | .claude/skills/rule-change-checklist/SKILL.md | ISS-050。Read/Write/Edit 3ツール網羅性確認 |
| 4 | 複数リポジトリ施策のPR作成漏れ防止 | inbox | l1-manager SKILL.md | クローズ手順に全対象リポのPR作成確認追加 |
| 5 | エージェント名ケバブケース規則 | inbox | session-flow-policy SKILL.md | agents name フィールドはケバブケースのみ |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 発見元 Set | 背景・文脈 |
|---|------|----------|-----------|
| 1 | inbox 気づきエントリの蓄積傾向 | set-1 | 3施策完了ごとに10件前後。backlog化率50% |
| 2 | CSV ファイル名列と実ファイル名の不一致パターン | set-1 | 施策名変更時にファイル名列が未更新 |

## 課題集約

### ワーカーセット別課題件数

| Set | 課題件数 | CSV転記件数 | 備考 |
|-----|---------|-----------|------|
| set-1 | 1 | 0 | ISS-041 の再発パターン（既存課題。新規CSV転記不要） |

### CSV転記済み課題

なし（新規課題は発見されず、既存課題 ISS-041 の再発確認のみ）

## 課題起票

- 起票した課題（合計）：0 件（ISS-041 の再発パターンのみで新規転記不要）

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-09
**レビュー依頼先**: ユーザー
**レビュー状態**: レビュー待ち
