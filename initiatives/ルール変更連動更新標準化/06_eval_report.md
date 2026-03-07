# 評価レポート: ルール変更連動更新標準化

## 評価サマリ

統合元4件の核心要件はすべて成果物にカバーされており、情報欠損は検出されなかった。7ファイルの関連ファイル一覧の参照関係は実際の参照と整合しており、標準チェックリストも既知の連動更新パターンを網羅している。01_plan.md の4つの成功基準はすべて達成されている。

## 評価結果

| # | 評価項目 | 判定基準 | 結果 | 判定 |
|---|---------|---------|------|------|
| 1 | 情報欠損評価（T-011） | 統合元4件すべて「充足」 | 4件すべて充足（詳細は下記テーブル） | OK |
| 2 | 参照関係整合性（T-012） | 全エントリが実際の参照関係と整合 | 7ファイル計51エントリを検証、全エントリ整合（詳細は下記） | OK |
| 3 | チェックリスト網羅性（T-013） | 既知パターンがすべてカバー | 5項目で既知の5パターンをすべてカバー（詳細は下記） | OK |

---

## T-011: 情報欠損評価テーブル

| 統合元 | 核心要件 | 成果物での対応箇所 | 判定 |
|--------|---------|-------------------|------|
| workflow-md更新プロセス整備 | workflow.md 更新を必須タスクとして組み込む | docs/rule-change-checklist.md チェック項目2「docs/workflow.md の更新」に3つのサブ項目（影響セクション特定・該当セクション更新・整合確認）で明記。docs/workflow.md にも「ルール変更時の連動更新」セクションが追加済み | 充足 |
| TG-008チェック基準連動更新 | TG-008 基準連動更新を標準タスク化 | docs/rule-change-checklist.md チェック項目3「TG-008 基準の連動更新」に4つの該当条件（ライフサイクルステージ追加/変更/削除、ペアリング対称性要件の変更、課題起票・ルーティング手段の変更、停止ルール・スコープの変更）と3つのサブ項目で明記 | 充足 |
| ルール変更施策の標準タスクパターン化 | 調査→文書化→ルール反映→workflow更新の定型パターンをテンプレート化 | docs/rule-change-checklist.md 冒頭の「標準タスクパターン」セクションに4段階の定型パターン（1.調査→2.文書化→3.ルール反映→4.連動更新）を明記。「使い方」セクションでL1が02_tasks.mdに固定タスクとして追加する手順、L2がコミット前に確認する手順を記載 | 充足 |
| 関連ファイル一覧セクション横展開 | triage-manager.md のパターンを l1-manager, l2-worker, l2-evaluator 等に横展開 | 7ファイルすべてに「関連ファイル一覧」セクションが追加済み。triage-manager/SKILL.md の既存パターン（テーブル形式: ファイル名 + 連動更新の内容）に準拠した形式で横展開されている | 充足 |

---

## T-012: 関連ファイル一覧の参照関係整合性検証

7ファイルの関連ファイル一覧に記載された各エントリについて、(a) 本文中に実際の参照・言及があるか、(b) 逆方向参照（当該ファイルを参照している他ファイル）から見て妥当か、を検証した。

### 1. l1-manager/SKILL.md（7エントリ）

| エントリ | 本文中の参照 | 整合性 |
|---------|-------------|--------|
| agents/l2-worker.md | 「L2サブエージェントの起動」セクションで明示的に参照 | OK |
| agents/l2-evaluator.md | 同上 | OK |
| initiatives/_template/ | 「新施策の開始手順」で `_template/` をコピーする手順を記載 | OK |
| docs/workflow.md | CLAUDE.md のドキュメント整合性ルールに基づく連動関係（本文に直接パスはないが、スキル定義→workflow.md の関係は全スキルに共通） | OK |
| session-flow-policy/SKILL.md | 「新しいセッションタイプを作成する際は session-flow-policy スキルを参照すること」と明記（79行目） | OK |
| triage-standard-policy/SKILL.md | 逆方向: triage-standard-policy が走査対象として l1-manager を列挙。連動関係は妥当 | OK |
| プロセス改善_課題管理.csv | 「課題のCSV転記」関連の手順で複数回参照 | OK |

### 2. l2-worker.md（7エントリ）

| エントリ | 本文中の参照 | 整合性 |
|---------|-------------|--------|
| l1-manager/SKILL.md | 逆方向: l1-manager が l2-worker を起動・成果物確認する関係。l2-worker は L1 の成果物を「読み取りのみ」と記載 | OK |
| l2-evaluator.md | 「ペアリングの対称性要件」として記載。l2-evaluator が l2-worker の成果物を読み取る関係 | OK |
| initiatives/_template/03_work_log.md | 壁打ちフェーズのフォーマットが 03_work_log.md に記録される旨を記載 | OK |
| initiatives/_template/04_work_report.md | 作業レポートの構成・知見記録セクションを定義 | OK |
| initiatives/_template/07_issues.md | 課題起票フォーマットと転記ルールを定義 | OK |
| docs/workflow.md | スキル定義→workflow.md の標準連動関係 | OK |
| triage-standard-policy/SKILL.md | 逆方向: triage-standard-policy が走査対象として l2-worker を列挙 | OK |

### 3. l2-evaluator.md（7エントリ）

| エントリ | 本文中の参照 | 整合性 |
|---------|-------------|--------|
| l1-manager/SKILL.md | 逆方向: l1-manager が l2-evaluator を起動する関係 | OK |
| l2-worker.md | 「ペアリングの対称性要件」として記載。l2-evaluator が l2-worker の成果物を読み取る関係 | OK |
| initiatives/_template/05_eval_plan.md | 壁打ちフェーズの記録先として定義 | OK |
| initiatives/_template/06_eval_report.md | 評価レポートの構成・知見記録セクションを定義 | OK |
| initiatives/_template/07_issues.md | 課題起票フォーマットと転記ルールを定義 | OK |
| docs/workflow.md | スキル定義→workflow.md の標準連動関係 | OK |
| triage-standard-policy/SKILL.md | 逆方向: triage-standard-policy が走査対象として l2-evaluator を列挙 | OK |

### 4. triage-worker.md（5エントリ）

| エントリ | 本文中の参照 | 整合性 |
|---------|-------------|--------|
| triage-manager/SKILL.md | 逆方向: triage-manager がワーカーをディスパッチする関係 | OK |
| triage-evaluator.md | 「ペアリングの対称性要件」として記載 | OK |
| triage-standard-policy/SKILL.md | 「TG-008: セッション構造標準ポリシーチェック」セクションで `.claude/skills/triage-standard-policy/SKILL.md` を明示的に参照（181行目） | OK |
| triage/_template/workers/_template/ | 「担当ファイル」セクションで `workers/set-N/` パターンを参照。テンプレートとの対応関係 | OK |
| docs/workflow.md | スキル定義→workflow.md の標準連動関係 | OK |

### 5. triage-evaluator.md（5エントリ）

| エントリ | 本文中の参照 | 整合性 |
|---------|-------------|--------|
| triage-manager/SKILL.md | 逆方向: triage-manager が評価者をディスパッチする関係 | OK |
| triage-worker.md | 「ペアリングの対称性要件」として記載。triage-worker の走査結果を評価する関係 | OK |
| triage-standard-policy/SKILL.md | 逆方向: triage-standard-policy がペアリング対称性要件の対象として列挙 | OK |
| triage/_template/workers/_template/ | 「担当ファイル」セクションで `workers/set-N/` パターンを参照 | OK |
| docs/workflow.md | スキル定義→workflow.md の標準連動関係 | OK |

### 6. triage-standard-policy/SKILL.md（8エントリ）

| エントリ | 本文中の参照 | 整合性 |
|---------|-------------|--------|
| l1-manager/SKILL.md | 「3.1 走査対象」で明示的に列挙 | OK |
| l1-manager/agents/l2-worker.md | 同上 | OK |
| l1-manager/agents/l2-evaluator.md | 同上 | OK |
| triage-manager/SKILL.md | 同上 | OK |
| triage-manager/agents/triage-worker.md | 同上 | OK |
| triage-manager/agents/triage-evaluator.md | 同上 | OK |
| session-flow-policy/SKILL.md | 逆方向: session-flow-policy が triage-standard-policy を「チェックリスト参照」として記載 | OK |
| docs/workflow.md | スキル定義→workflow.md の標準連動関係 | OK |

### 7. session-flow-policy/SKILL.md（9エントリ）

| エントリ | 本文中の参照 | 整合性 |
|---------|-------------|--------|
| l1-manager/SKILL.md | 「5. 既存セッションタイプとの整合性」で `.claude/skills/l1-manager/` を明示的に参照 | OK |
| l1-manager/agents/l2-worker.md | 同上セクションで `agents/l2-worker.md` を明示的に参照 | OK |
| l1-manager/agents/l2-evaluator.md | 同上セクションで `agents/l2-evaluator.md` を明示的に参照 | OK |
| triage-manager/SKILL.md | 同上セクションで `.claude/skills/triage-manager/` を明示的に参照 | OK |
| triage-manager/agents/triage-worker.md | 同上セクションで `agents/triage-worker.md` を明示的に参照 | OK |
| triage-manager/agents/triage-evaluator.md | 同上セクションで `agents/triage-evaluator.md` を明示的に参照 | OK |
| triage-standard-policy/SKILL.md | 「5.1 新セッションタイプ追加時のチェックリスト」で適用マトリクスへの追加を明記 | OK |
| docs/workflow.md | 同チェックリストで `docs/workflow.md` への追記を明記（135行目） | OK |
| .claude/rules/commit-message.md | 同チェックリストで新セッションタイプの追加時の反映を明記（136行目） | OK |

### T-012 結論

7ファイル計51エントリすべてにおいて、関連ファイル一覧の記載内容が実際の参照関係（順方向参照・逆方向参照）と整合していることを確認した。不整合は検出されなかった。

---

## T-013: 標準チェックリストの網羅性検証

docs/rule-change-checklist.md の5つのチェック項目を、既知の連動更新パターンと突合した。

| 既知の連動更新パターン | チェックリストの対応項目 | カバー状況 |
|---------------------|----------------------|----------|
| 関連ファイル一覧の確認（変更ファイルの連動更新先を特定） | 項目1「関連ファイル一覧の確認」 | カバー済み |
| docs/workflow.md の更新（人間向け可視化の整合性維持） | 項目2「docs/workflow.md の更新」 | カバー済み |
| TG-008 基準の連動更新（triage-standard-policy の整合性維持） | 項目3「TG-008 基準の連動更新」 | カバー済み |
| テンプレートの連動更新（initiatives/_template/, triage/_template/） | 項目4「テンプレートの連動更新」 | カバー済み |
| コミットメッセージ規約の更新（新セッション種別追加時） | 項目5「コミットメッセージ規約の確認」 | カバー済み |

### 追加検証: 標準タスクパターンの妥当性

チェックリスト冒頭の「標準タスクパターン: 調査→文書化→ルール反映→workflow更新」が、統合元3番目の backlog アイテム（ルール変更施策の標準タスクパターン化）の核心要件「調査→文書化→ルール反映→workflow更新の定型パターンをテンプレート化」と一致していることを確認した。

### 追加検証: 使い方セクションの妥当性

- L1 マネージャー向け: 02_tasks.md に固定タスクとして追加する手順が記載されている。L1 マネージャースキル（l1-manager/SKILL.md）の「タスクリストに含める固定タスク」セクションとの連携が想定される
- L2 ワーカー向け: コミット前の確認手順が記載されている

### T-013 結論

既知の5つの連動更新パターンがすべてカバーされている。網羅性に問題なし。

---

## 計画の成功基準に対する達成度

| 成功基準 | 達成度 | 根拠 |
|---------|--------|------|
| 全スキル/エージェント定義（7ファイル）に「関連ファイル一覧」が存在する | 達成 | 7ファイルすべてに「関連ファイル一覧」セクションが追加されていることを確認。triage-manager/SKILL.md は既存のため計8ファイルに一覧が存在 |
| docs/rule-change-checklist.md が作成され、標準タスクパターンが定義されている | 達成 | 5項目のチェックリストと4段階の標準タスクパターンが定義されている |
| 統合元4件の要件が100%カバーされている（情報欠損なし） | 達成 | 情報欠損評価テーブルで4件すべて「充足」判定 |
| docs/workflow.md にチェックリスト参照が追記されている | 達成 | 「ルール変更時の連動更新」セクションが追加され、4項目の要約とチェックリスト文書への参照リンクが記載されている |

## 発見された課題・改善提案

課題は発見されなかった（07_issues.md への起票なし）。

### 軽微な観察事項（課題レベルではないもの）

- docs/rule-change-checklist.md の「使い方」セクションで L1 が 02_tasks.md に固定タスクとして追加する手順が記載されているが、l1-manager/SKILL.md の「タスクリストに含める固定タスク」セクションにはまだこのチェックリストタスクへの言及がない。ただし、チェックリスト自体が「施策立案時に参照する形」（00_proposal.md の備考・設計パターンに記載）であるため、L1 がチェックリストを読んで判断する運用で問題ない。将来的に l1-manager/SKILL.md にチェックリスト参照の固定タスクを組み込むかは別施策の判断事項。

## 実施ワーカーの未転記確認

07_issues.md を確認した結果、未転記メモは0件であった。対応不要。

## 評価中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | 関連ファイル一覧の「docs/workflow.md」エントリは全スキル/エージェント定義に共通して存在する | 全 .claude/skills/ 配下ファイル | 8ファイルすべてに docs/workflow.md が連動更新先として記載されている。「ルールファイルを変更したら workflow.md を更新する」というルールが CLAUDE.md に既に存在するため、関連ファイル一覧としては冗長ではあるが、チェックリストの網羅性担保のために記載する方が安全。現状の運用で問題ない |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | 関連ファイル一覧のエントリ数はファイルの責務範囲に比例する | ポリシー系ファイル（session-flow-policy: 9件、triage-standard-policy: 8件）は横断的に多くのファイルに影響するため連動更新先が多い。エージェント定義（triage-worker/evaluator: 5件）は比較的少ない。L2-worker の作業レポートの知見と一致する観察 |

## 次フェーズへの推奨

進めるべき。統合元4件の情報欠損なし、成功基準すべて達成、課題なし。ゲート判定（通過）を推奨する。

---
**作成者**: L2（評価）
**作成日**: 2026-03-07
