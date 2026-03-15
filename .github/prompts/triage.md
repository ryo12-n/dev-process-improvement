# GHA トリアージセッション（非対話モード）

あなたは GitHub Actions で自動実行されるトリアージセッションです。
`.claude/skills/triage-manager/SKILL.md` のトリアージマネージャーの作業フローを、非対話の単一エージェントとして実行します。

---

## 制約事項（GHA 環境）

- **非対話モード**: ユーザーへの確認待ち・壁打ちフェーズは実施しない
- **単一エージェント**: サブエージェント（Task ツール）は使用できない。ワーカー・評価者の作業を自分自身で順次実行する
- **ブランチ整理不要**: GHA が毎回クリーンな環境で実行するため、セッション開始時のブランチ整理は不要
- **コミット不要**: ファイルの作成・編集のみ行う。コミット・プッシュ・PR 作成は GHA ワークフローが行う
- **セッションライフサイクル todo 登録不要**: TaskCreate/TaskUpdate は使用しない

---

## 作業フロー

以下のステップを順に実行してください。

### ステップ 1: セッションフォルダの作成

`sessions/triage/_template/` 直下のファイル（00〜04）を `sessions/triage/YYYYMMDD/` にコピーする。
`sessions/triage/YYYYMMDD/workers/` は空ディレクトリとして作成する（`_template/workers/_template/` はコピーしない）。

YYYYMMDD はユーザーメッセージから取得した今日の日付を使用する。

### ステップ 2: 事前調査（00_pre_investigation.md）

`sessions/triage/YYYYMMDD/00_pre_investigation.md` のテンプレートを埋める。以下の調査を実施する:

1. **inbox 確認**: `inbox/` の未処理 `.md` ファイルを一覧し、件数と内容を把握する
   - `inbox/ref_*.md`（参照物ポインター）がある場合は対応する `refs/` の内容も確認する
2. **backlog 確認**: `backlog/backlog.csv` と `backlog/entries/` の件数・優先度分布を確認する
3. **課題管理 CSV 確認**: `プロセス改善_課題管理.csv` のステータス別件数を確認する
4. **進行中 initiative 確認**: `sessions/initiatives/` の進行中施策を確認する
5. **inbox 気づきエントリ確認**: セッション終了時の気づきエントリの有無を確認する
6. **ルール・workflow 整合性確認**: `.claude/skills/*/SKILL.md` および `agents/*.md` と `docs/workflow.md` の整合性を簡易確認する
7. **前回トリアージからの変化**: `sessions/triage/` 内の最新セッションの日付を確認する

事前調査の結果から走査ボリュームを算出する:
- inbox 分類対象件数 + backlog 突合・分析対象件数 + CSV 確認対象件数 = 走査ボリューム

### ステップ 3: 実施計画の作成（01_plan.md）

事前調査の結果をもとに `sessions/triage/YYYYMMDD/01_plan.md` を作成する。

GHA 環境では単一エージェントで実行するため、ワーカーセット数は常に 1 とする。
ただし、実行する TG タスクの選定は走査ボリュームに基づいて判断する。

主要な TG タスク:
- **TG-001**: inbox 走査・分類（未処理 inbox エントリの確認・分類・処理方針決定）
- **TG-002**: backlog 突合チェック（施策化済みチェック、対象リポジトリ未記入チェック含む）
- **TG-003**: CSV 確認（課題管理 CSV のステータス確認・更新）
- **TG-004**: initiative 状態確認（進行中施策のフェーズ確認）
- **TG-005**: backlog 関係性分析（重複候補・依存関係・統合候補の検出）
- **TG-006**: ルール・workflow 整合性チェック（参考資料ステータスチェック、README 整合性チェック含む）
- **TG-007**: inbox 気づきエントリ処理
- **TG-008**: セッション構造標準ポリシーチェック（前回からの変更がある場合のみ）
- **TG-009**: 情報欠損リスク評価（削除・統合候補がある場合のみ）
- **TG-010**: GHA ↔ Skills 整合性チェック（`.github/gha-skills-mapping.yml` マニフェストに基づくドリフト検出）

**フェーズ順序の注意**: GHA 環境では単一エージェントで実行するが、以下の依存関係を尊重して順序を守ること:
- Phase 1（TG-001, TG-003, TG-004, TG-007）→ Phase 2a（TG-002, TG-006, TG-008）→ Phase 2b（TG-005、TG-002 に依存）→ Phase 2c（TG-009、条件付き）→ Phase 3（TG-010）

### ステップ 4: ワーカー走査の実行

ワーカーセットのディレクトリを作成する:
1. `sessions/triage/_template/workers/_template/` を `sessions/triage/YYYYMMDD/workers/set-1/` にコピーする
2. `workers/set-1/01_tasks.md` に割り当てる TG タスクを記入する

壁打ちフェーズは省略し、直接走査を開始する。

各 TG タスクを実行し:
- 作業内容を `workers/set-1/03_work_log.md` にタイムスタンプ付きで記録する
- 走査結果を `workers/set-1/04_scan_report.md` に構造化して記載する
- 発見した課題を `workers/set-1/07_issues.md` に起票する

#### TG-001: inbox 走査・分類の実行手順

1. `inbox/` の全 `.md` ファイルを読む
2. 各ファイルを以下に分類する:
   - **backlog 候補**: 施策として検討すべきもの → `backlog/entries/` にファイルを作成し、`backlog/backlog.csv` にエントリを追加する
   - **ルール反映**: 既存ルールの改善につながるもの → 該当ルールファイルを更新する
   - **却下**: 対応不要と判断したもの → 理由を記録する
   - **保留**: 判断に追加情報が必要なもの → inbox に残す
3. 処理済みのエントリは `inbox/` から削除する（git 履歴が証跡）
   - `ref_*.md` を削除する場合でも、対応する `refs/` の本体は削除しない

#### TG-002: backlog 突合チェックの実行手順

1. `backlog/backlog.csv` の各エントリについて:
   - 「施策ディレクトリ名」列が記入済み → `sessions/initiatives/` および `sessions/initiatives/_archive/` で照合
   - 「施策ディレクトリ名」列が空欄 → `backlog/entries/<ファイル名>` と `sessions/initiatives/` 配下のディレクトリ名・`00_proposal.md` の「backlog元ファイル」で照合
2. 施策化済みのファイルを「削除・クローズ候補」としてレポートに記載する
3. 「対象リポジトリ」が未記入のエントリを検出し、レポートに記載する

#### TG-005: backlog 関係性分析の実行手順

1. `backlog/entries/` の全エントリを読む
2. 重複候補・依存関係・統合候補の3種類の関係を検出する
3. 分析結果をスキャンレポートの TG-005 セクションに記載する

#### TG-006: ルール・workflow 整合性チェックの実行手順

1. `.claude/skills/*/SKILL.md` および `agents/*.md` と `docs/workflow.md` を見比べる
2. 参考資料（ドラフト）のステータスバナーを確認する（CLAUDE.md の docs/ 文書分類テーブル参照）
3. README.md の4セクション（ディレクトリ構成図、セッション種別テーブル、AI向けスキル定義テーブル、ドキュメントマップ）の整合性を確認する
4. 軽微なズレはその場で修正する

#### 完了済み initiative のアーカイブ確認

`sessions/initiatives/` 配下で `08_gate_review.md` が「通過」判定のものがあれば、アーカイブ対象としてレポートに記載する。

#### TG-010: GHA ↔ Skills 整合性チェックの実行手順

1. `.github/gha-skills-mapping.yml` を読み込む（存在しない場合は `07_issues.md` に起票しスキップ）
2. 各 mapping について:
   - GHA ソースファイル（`gha_source.path`）を読む
   - Skill ソースファイル（`skill_source.manager` + `skill_source.agents`）を読む
   - 各 `checkpoint` を検証する:
     - `task_ids`: 正規表現パターンで両方から ID を抽出し、差集合を計算
     - `workflow_steps`: `keys` リストと両ソースのステップを突合
     - `report_sections`: `keys` リストと両ソースのセクション構造を突合
     - `file_templates` / `file_numbers`: 正規表現パターンで参照を抽出し、差集合を計算
   - `inherent_differences` の各宣言が実際に有効かを確認
3. ドリフト判定: CRITICAL（Skill にあり GHA にないタスク ID）/ WARNING（ステップ・セクション不一致）/ INFO（軽微な差異）
4. 結果を `04_scan_report.md` の TG-010 セクションに記載

### ステップ 5: 評価の実行

走査結果の自己評価を実施する（GHA 環境ではワーカーと評価者が同一エージェント）。

以下の観点で走査結果を評価する:
- **走査完全性**: 割り当てた全 TG タスクが実施されているか
- **判断品質**: 分類判断に根拠があるか
- **エビデンス品質**: 具体的なデータが記載されているか

評価結果を `workers/set-1/06_eval_report.md` に記載する。

### ステップ 6: 結果集約・レポート作成（03_report.md）

`workers/set-1/04_scan_report.md` と `workers/set-1/06_eval_report.md` を集約して `sessions/triage/YYYYMMDD/03_report.md` を作成する。

レポートには以下を含める:
- TG タスク別の走査結果サマリ
- 知見集約（ルール化候補・参考情報）
- 課題集約（起票件数・CSV転記状況）

### ステップ 7: ゲート判定（04_gate_review.md）

`sessions/triage/YYYYMMDD/04_gate_review.md` にゲート判定を記載する。

判定は「通過 / 条件付き通過 / 差し戻し」の3択で行い、判定理由を必ず記載する。

知見ルーティング:
- 施策横断で再発しうる知見 → CSV に転記
- 具体的な次施策として起動可能 → backlog に追加
- 判断が必要 → inbox に残す
- 施策内で完結 → なし

### ステップ 8: アクション実施

レポートに基づくアクションを実施する:
- inbox の処理済みアイテム削除
- backlog 作成・変更（`backlog/entries/` へのファイル作成、`backlog/backlog.csv` の更新）
- ルール反映（軽微なズレの修正）
- CSV 更新（課題の転記）

### ステップ 9: ディスパッチログの記録

`sessions/triage/YYYYMMDD/02_dispatch_log.md` に実行記録を残す。
GHA 環境のため「単一エージェントによる逐次実行」と記載する。

---

## コミットメッセージ規約

本セッションではコミットは行わないが、走査結果のレポートに記載するコミットメッセージの推奨形式:

```
[triage-mgr] YYYYMMDD: 自動トリアージ実行
```

---

## スキャンレポートの構成

`workers/set-1/04_scan_report.md` は以下の構成で作成する:

```markdown
# スキャンレポート: Set-1

## 担当タスク
| タスクID | 対象 | ステータス |
|---------|------|-----------|
| TG-XXX | ... | 完了 / スキップ |

## TG-XXX: [タスク名]
<!-- 各 TG タスクの走査結果 -->

## 課題起票
- 起票件数: __ 件

## 走査中の知見

### ルール化候補
| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|

### 参考情報
| # | 知見 | 背景・文脈 |
|---|------|-----------|
```

---

## 注意事項

- **refs/ の本体ファイルは削除しない**: 対応する `inbox/ref_*.md` のみ削除可
- **backlog の変更は慎重に**: 新規追加は行うが、既存エントリの大幅な変更は避ける
- **判断に迷う場合は保留**: 確実な判断ができないものは inbox に残し、人間のレビューに委ねる
- **知見記録は必須**: 走査中の知見セクションに最低1行の記載が必要（該当なしの場合は「なし — 理由: ○○」と記載）
