# 作業履歴: GHA 用 initiative skills の分離

## 壁打ちフェーズ [2026-03-15 10:00]

### 理解のサマリー
- タスクの目的: GHA ワークフロー（wallbash/execute/close/question）で Claude が CLAUDE.md や l1-manager のルールに従ってしまう問題を解消するため、GHA 専用スキルファイルを4つ作成し、ワークフロー YAML のプロンプトをスキルファイル参照方式にリファクタする。併せて execution_file 出力修正を3ワークフローに横展開する
- スコープ: T-001〜T-013（フェーズ1: スキル作成・YAML リファクタ・execution_file 修正、フェーズ2: ドキュメント更新・クリーンアップ、固定タスク: 知見記録・課題転記・メタルール検証）
- 完了条件: 4スキルファイル作成済み、4ワークフロー YAML 更新済み、execution_file 修正3件完了、gha-guideline 更新済み、docs/workflow.md 更新済み、inbox 削除済み、04_work_report.md と 07_issues.md が作成されている

### 前提条件チェック
- [x] 依存タスクの完了状態: 完了（施策ディレクトリ・提案・計画・タスクリスト作成済み）
- [x] 必要ツール・コマンドの利用可否: 確認済み（Read/Write/Edit/Bash/Glob/Grep 利用可能）
- [x] 環境の準備状況（ファイル・ディレクトリの存在等）: 確認済み
  - 4つの YAML ファイルが存在（initiative-wallbash/execute/close/question.yml）
  - gha-guideline/SKILL.md が存在
  - docs/workflow.md が存在
  - refs/claude-code-action/knowledge.md が存在
  - inbox/gha-execution-file-fix-rollout.md が存在
  - .github/gha-skills-mapping.yml が存在

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：実施開始

---

## 実施計画サマリ

フェーズ1（T-001〜T-006）→ フェーズ2（T-007〜T-010）→ 固定タスク（T-011〜T-013）の順で実施する。

1. T-001〜T-004: 各ワークフロー YAML の prompt セクションからスキルファイルを作成（4ファイル並行可能だが順次作成）
2. T-005: 4ワークフロー YAML のプロンプトをスキルファイル参照方式にリファクタ
3. T-006: execution_file 出力修正を execute/close/question の3ファイルに横展開
4. T-007: gha-guideline の権限マトリクスに新スキルと question ワークフローを追加
5. T-008: docs/workflow.md に GHA スキルのセクションを追加
6. T-009: knowledge.md にスキル分離アプローチの知見を追記
7. T-010: inbox/gha-execution-file-fix-rollout.md を git rm で削除
8. T-011〜T-013: 知見記録・課題転記・メタルール横断検証

---

## 作業ログ

### [2026-03-15 11:00] タスクID: T-001
**状態**: 完了
**作業内容**:
- `.claude/skills/gha-wallbash/SKILL.md` を作成
- `initiative-wallbash.yml` の prompt セクション（行46〜79）から指示・制約を抽出
- SKILL.md 標準構造（frontmatter `user-invocable: false` + あなたの役割 / 作業フロー / やること / やらないこと）で記述
- CLAUDE.md・l1-manager のルールに従わない旨を明記
**成果物**: `.claude/skills/gha-wallbash/SKILL.md`

### [2026-03-15 11:05] タスクID: T-002
**状態**: 完了
**作業内容**:
- `.claude/skills/gha-execute/SKILL.md` を作成
- `initiative-execute.yml` の prompt セクション（行77〜115）から指示・制約を抽出
- approve / reject の2サブフローを含めた
**成果物**: `.claude/skills/gha-execute/SKILL.md`

### [2026-03-15 11:10] タスクID: T-003
**状態**: 完了
**作業内容**:
- `.claude/skills/gha-close/SKILL.md` を作成
- `initiative-close.yml` の prompt セクション（行45〜71）から指示・制約を抽出
- 知見ルーティング・アーカイブ移動の手順を記載
**成果物**: `.claude/skills/gha-close/SKILL.md`

### [2026-03-15 11:15] タスクID: T-004
**状態**: 完了
**作業内容**:
- `.claude/skills/gha-question/SKILL.md` を作成
- `initiative-question.yml` の prompt セクション（行48〜68）から指示・制約を抽出
- 読み取り専用であることを明記
**成果物**: `.claude/skills/gha-question/SKILL.md`

### [2026-03-15 11:20] タスクID: T-005
**状態**: 完了
**作業内容**:
- 4ワークフロー YAML の prompt セクションをスキルファイル参照方式にリファクタ
- 各プロンプトを「Read 指示 + 動的コンテキスト + 1行リマインダー」に短縮
- 動的パラメータ（Issue番号、ブランチ名、フィードバック内容等）は YAML に残した
**成果物**: 4つの YAML ファイル更新

### [2026-03-15 11:30] タスクID: T-006
**状態**: 完了
**作業内容**:
- `initiative-execute.yml`, `initiative-close.yml`, `initiative-question.yml` の3ファイルで `steps.claude.outputs.result` を jq 抽出パターンに置換
- `initiative-wallbash.yml` の実装パターン（行100〜130）をリファレンスとして踏襲
- 各ファイルに Extract ステップを追加し、フォールバックメッセージを含めた
- 環境変数名を `CLAUDE_RESULT` → `SUMMARY` に変更し、`steps.extract.outputs.summary` を参照
**成果物**: 3つの YAML ファイル更新

### [2026-03-15 11:40] タスクID: T-007
**状態**: 完了
**作業内容**:
- `gha-guideline/SKILL.md` セクション5.1に `initiative-question.yml` を追加
- セクション5.1の各ワークフローに対応するスキルファイルパスを追記
- セクション5.2に `initiative-question.yml` の権限マトリクスを追加（contents:read, issues:write, Read/Glob/Grep/Bash(ls *)）
- セクション5.3に `initiative-question.yml` の設計判断を追加
- 関連ファイル一覧に `initiative-question.yml` と4つの GHA スキルファイルを追加
**成果物**: `gha-guideline/SKILL.md` 更新

### [2026-03-15 11:45] タスクID: T-008
**状態**: 完了
**作業内容**:
- `docs/workflow.md` に「GHA Initiative スキル」セクションを追加（自動施策化フローの後、オートメーションメンテナンスセッションの前）
- スキル一覧テーブル（4スキル）と設計方針を記載
**成果物**: `docs/workflow.md` 更新

### [2026-03-15 11:50] タスクID: T-009
**状態**: 完了
**作業内容**:
- `refs/claude-code-action/knowledge.md` に知見 #12（スキル分離アプローチ）と #13（execution_file 統一）を追記
- 「知見の詳細」セクションに「GHA 専用スキル分離アプローチ」サブセクションを追加
**成果物**: `refs/claude-code-action/knowledge.md` 更新

### [2026-03-15 11:55] タスクID: T-010
**状態**: 完了
**作業内容**:
- `inbox/gha-execution-file-fix-rollout.md` を `git rm` で削除（execution_file 修正の横展開が T-006 で完了したため）
**成果物**: ファイル削除

### [2026-03-15 12:00] タスクID: T-013
**状態**: 完了
**作業内容**:
- メタルール横断検証を実施（3領域）
- (1) メタルールフロー記述: 新 GHA スキルは user-invocable: false で GHA からのみ使用。他スキルのフロー記述に影響なし → 合格
- (2) workflow.md 同期: T-008 で GHA Initiative スキルセクションを追加済み → 合格（修正済）
- (3) TG-008 基準連動: GHA スキルはセッション型ライフサイクル（壁打ち/計画/実行/評価/ゲート判定）に該当しないため、TG-008 の走査対象には含めない → 該当なし
- 気づき: gha-skills-mapping.yml に initiative ワークフローのマッピングがないが、タスクスコープ外のため 07_issues.md に起票
**成果物**: 検証結果を 04_work_report.md に記載

