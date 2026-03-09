# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-001 | inbox | 完了 |
| TG-002 | backlog | 完了 |
| TG-003 | CSV | 完了 |
| TG-004 | initiative | 完了 |
| TG-005 | backlog関係性 | 完了 |
| TG-009 | 情報欠損リスク | スキップ（削除・統合候補はCSVエントリのみ、ファイル実体は既に削除済み） |

## TG-001: inbox 分類

| アイテム | 判断 | 理由 |
|---------|------|------|
| L2知見発見と修正適用のギャップ改善.md | backlog候補 | L2-worker の知見発見と修正適用のギャップ。プロセス本質的課題 |
| agentsの管理方法のガイドライン追記.md | backlog候補 | エージェント管理ベストプラクティスのガイドライン化。内容が充実 |
| backlog-ideas-md整理.md | 軽微修正 | triage-manager 担当ファイルの ideas.md 参照を削除。セッション内修正可 |
| disallowedToolsフィールド活用検討.md | backlog候補 | deferred tools 制限の代替案。ISS-047 と関連 |
| entries-pattern-inbox適用検討.md | 判断保留 | 現在 inbox ファイル数が少なく entries/ パターンの必要性が低い |
| metacognition-managerの記述構造統一検討.md | backlog候補 | metacognition-manager に知見集約・課題集約の独立セクション追加 |
| rule-change-checklist_deny対称性チェック追加.md | ルール反映 | ISS-050 直結。rule-change-checklist への項目追加で対応可 |
| triage-metacognition テンプレート共通化検討.md | 判断保留 | 前回保留継続。2セッションタイプのみでコスト対効果低い |
| エージェント名ケバブケース規則.md | ルール反映 | Claude Code agents の命名制約の文書化。session-flow-policy に追記 |
| ゲート判定基準での課題重大度の明文化.md | backlog候補 | manager-common-policy §4 への重大度判断明文化 |
| フォーマット変換の内容同等性基準.md | backlog候補 | フォーマット変換時の省略可/不可基準の明確化 |
| ルール分離テーマ別分割パターン.md | backlog候補 | 1ファイル1テーマ原則の提案。長文rules最適化と関連 |
| 共通ポリシー参照のblockquote形式標準化.md | 却下 | 既に manager-common-policy で blockquote 形式を採用済み。追加アクション不要 |
| 複数リポジトリ施策のPR作成漏れ防止.md | ルール反映 | l1-manager クローズ手順にPR作成確認チェック追加 |
| 適用マトリクス列数増加リスク.md | 判断保留 | 前回保留継続。4セッションタイプ目追加時に再検討 |

### 分類サマリ

| 分類 | 件数 |
|------|------|
| backlog候補 | 7件 |
| ルール反映 | 3件 |
| 軽微修正 | 1件 |
| 判断保留 | 3件 |
| 却下 | 1件 |

## TG-002: backlog 棚卸し

### CSV/ファイル整合性

| # | 問題 | 施策名 | 推奨アクション |
|---|------|--------|-------------|
| 1 | CSVにあるがファイルなし（施策化済み） | 外部リポジトリ変更時のブランチ・PR運用ルール整備 | CSV行削除（_archive/external-repo-branch-pr-rules） |
| 2 | CSVにあるがファイルなし（施策化済み） | ガイドラインとルールファイルの二重管理リスク対策 | CSV行削除（_archive/docs-dual-management-prevention） |
| 3 | CSVにあるがファイルなし（施策化済み） | README整合性チェック | CSV行削除（_archive/readme-consistency-check） |
| 4 | CSVにあるがファイルなし（施策化済み） | inboxと課題管理とbacklogを管理方法見直し(v2) | CSV行削除（_archive/課題管理とinbox管理の方法見直し） |
| 5 | CSVファイル名不一致 | 社内施策_devkitスペシャリストロール作成 | CSV ファイル名列を実ファイル名に修正 |
| 6 | 前回報告・ユーザー未回答 | claude-directory最適化(ai-driven-dev-patterns) | CSV行削除候補（_archive/claude-directory最適化/ に対応施策あり） |

### 30日以上放置チェック

- 最古エントリ: 2026-03-01 → 8日。30日以上放置なし。

## TG-003: 課題管理 CSV 確認

### ステータス「起票」の課題サマリ（23件）

| ISS | タイトル | 優先度 | 起票日 | 経過日数 | 対応状況 |
|-----|---------|--------|--------|---------|---------|
| ISS-006 | ロール定義とOpenSpecの統合が未定義 | 中 | 02-23 | 14日 | openspec 開発ライフサイクル待ち。ブロック中 |
| ISS-013 | Agent Teams 機能の言及なし | 低 | 02-25 | 12日 | ガイドライン改訂時に対応 |
| ISS-016 | .claude/rules/ 向けルールファイル整備 | 中 | 02-27 | 10日 | フェーズ2完了後に実施 |
| ISS-019 | claude-directory-guide.md の skills/ 移動検討 | 低 | 02-27 | 10日 | 長文rules最適化と統合検討 |
| ISS-020 | config.yaml の tasks ルールのカテゴリ分け | 低 | 02-28 | 9日 | openspec 改善の一環 |
| ISS-021 | spec 作成時のエッジケース漏れ | 低 | 02-28 | 9日 | spec ガイドライン改善 |
| ISS-022 | spec 作成フェーズがボトルネック | 中 | 02-28 | 9日 | spec 支援施策 |
| ISS-027 | Claude Code Web 1セッション=1リポ制約 | 高 | 03-02 | 7日 | 当面対応不可。環境制約 |
| ISS-032 | CSV ステータスの同期漏れパターン | 低 | 03-04 | 5日 | トリアージ走査ステップ追加 |
| ISS-033 | 成功基準とCSV対応方針案のスコープ整合 | 低 | 03-04 | 5日 | 成功基準作成ガイド改善 |
| ISS-038 | CSV列追加時の列数整合性検証 | 低 | 03-07 | 2日 | CSV操作手順改善 |
| ISS-039 | gate_review の Write と git mv の実行順序 | 低 | 03-07 | 2日 | l1-manager 手順改善 |
| ISS-041 | backlog.csv に施策化済みエントリ残存 | 低 | 03-08 | 1日 | 今回のTG-002で検出中 |
| ISS-042 | grep 検証の走査対象漏れ | 中 | 03-08 | 1日 | rule-change-checklist 改善 |
| ISS-043 | commit-message.md の2系統共存 | 低 | 03-08 | 1日 | 経過観察 |
| ISS-044 | ai-driven-dev-patterns の連動更新未実施 | 中 | 03-08 | 1日 | 次回同期で対応 |
| ISS-045 | SDK環境でdenyリスト非機能 | 中 | 03-08 | 1日 | 運用ガイド記載 |
| ISS-046 | SDK環境でtools制限非機能 | 低 | 03-08 | 1日 | tools は意図文書化 |
| ISS-047 | deferred tools がtools制限を迂回 | 中 | 03-08 | 1日 | disallowedTools 検討 |
| ISS-048 | deny リストの Read/Write/Edit 網羅性 | 低 | 03-08 | 1日 | rule-change-checklist 改善 |
| ISS-049 | deny リストは唯一の強制的制限 | 中 | 03-08 | 1日 | 知見記録 |
| ISS-050 | Read/Write/Edit 3ツール網羅的考慮 | 中 | 03-08 | 1日 | rule-change-checklist 改善 |
| ISS-051 | gh -C 未サポート | 中 | 03-09 | 0日 | ルール修正必要 |

### 方針確定（1件）

| ISS | タイトル | 確定方針 |
|-----|---------|---------|
| ISS-031 | inbox/backlog 二重構造 | 二重構造許容。README でスコープ明記 |

### CSV データ品質問題

- **ISS-025**: ステータス欄に「 reviewer, bug_fixer」が混入。正しいステータス値（起票/方針確定/クローズ等）に修正が必要
- **ISS-051**: gh -C 問題は session-start-branch-cleanup-flow で修正済み（cd + gh に置換）。**クローズ候補**

### 長期未対応パターン

- ISS-006, ISS-013: 12-14日未対応だが、前提条件（openspec ライフサイクル定義、ガイドライン改訂）待ちのためブロック扱い
- ISS-016: フェーズ2完了待ちのためブロック

## TG-004: 進行中 initiative 確認

- 進行中施策: 0件
- ブロック中: 0件
- アーカイブ待ち: 0件
- sessions/initiatives/ 配下は _archive と _template のみ

## TG-005: backlog 関係性分析

### 重複候補

| # | アイテムA | アイテムB | 重複度 | 推奨 |
|---|----------|----------|--------|------|
| 1 | ルール分離テーマ別分割パターン（inbox新規） | 長文rulesのコンテキストコスト最適化 | 高 | 統合（長文rules施策に分割パターンを含める） |
| 2 | metacognition-managerの記述構造統一検討（inbox新規） | triage-metacognition テンプレート共通化検討（inbox保留） | 中 | 関連だが観点が異なる（構造統一 vs テンプレート共通化）。同時着手推奨 |

### 依存関係

| # | 先行 | 後続 | 依存内容 |
|---|------|------|---------|
| 1 | disallowedToolsフィールド活用検討 | Claude Code標準skills評価・取り込み | disallowedTools の仕様理解が skills 評価に影響 |
| 2 | ai-driven-dev-patterns_source-of-truth明示 | ai-driven-dev-patterns-triage-standard-policy作成 | Source of Truth 明示がポリシー作成の前提 |
| 3 | backlog-archive-matching改善 | backlogテンプレート凡例強化 | CSV/ファイル突合改善がテンプレート設計に影響 |

### 統合候補

| # | 候補A | 候補B | 統合理由 |
|---|-------|-------|---------|
| 1 | rule-change-checklist_deny対称性チェック追加（inbox） | denyリスト変更提案への副作用分析必須化 | 共に rule-change-checklist の改善。1施策にまとめられる |
| 2 | L2知見発見と修正適用のギャップ改善（inbox） | ゲート判定基準での課題重大度の明文化（inbox） | 共にプロセスの知見→アクション変換の改善 |

## 課題起票

- 起票件数: 2 件（`07_issues.md` に起票）
- backlog.csv に施策化済みエントリが4件残存（ISS-041 の再発パターン）
- ISS-025 のステータス欄が破損（「 reviewer, bug_fixer」が混入）→ CSV修正が必要

## 走査中の知見

### ルール化候補（.claude/rules/ や skills/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | triage-manager 担当ファイルに存在しない ideas.md が記載 | .claude/skills/triage-manager/SKILL.md | 担当ファイルテーブルから `backlog/ideas.md` 行を削除すべき |
| 2 | backlog.csv の施策化済みエントリ残存が繰り返し発生 | l1-manager / triage-manager | ISS-041 と同パターン。l1 クローズ手順にCSVエントリ削除ステップ追加を推奨 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | inbox の気づきエントリが大量に蓄積する傾向 | 3施策完了ごとに10件前後の気づきが生まれる。backlog化率は約50% |
| 2 | CSV ファイル名列と実ファイル名の不一致パターン | 施策名変更時にCSVの施策名列は更新するがファイル名列が未更新 |

---
**作成者**: トリアージワーカー（マネージャー代理実施）
**作成日**: 2026-03-09
