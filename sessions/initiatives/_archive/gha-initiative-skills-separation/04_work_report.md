# 作業レポート: GHA 用 initiative skills の分離

## サマリ

GHA ワークフロー4つ（wallbash/execute/close/question）に対応する GHA 専用スキルファイルを作成し、ワークフロー YAML のプロンプトをスキルファイル参照方式にリファクタした。併せて execution_file 出力修正を3ワークフローに横展開し、ドキュメント類（gha-guideline, workflow.md, knowledge.md）を更新した。全13タスク（T-001〜T-013、うち T-014/T-015 は評価ワーカー担当）を完了。

## タスク実績

| ID | タスク | 計画 | 実績 | 差異・備考 |
|----|--------|------|------|-----------|
| T-001 | gha-wallbash スキル作成 | SKILL.md 作成 | 完了 | 差異なし |
| T-002 | gha-execute スキル作成 | SKILL.md 作成（approve/reject） | 完了 | 差異なし |
| T-003 | gha-close スキル作成 | SKILL.md 作成 | 完了 | 差異なし |
| T-004 | gha-question スキル作成 | SKILL.md 作成（読み取り専用） | 完了 | 差異なし |
| T-005 | YAML プロンプトリファクタ | 4ファイル短縮化 | 完了 | 差異なし |
| T-006 | execution_file 修正横展開 | 3ファイル jq 抽出適用 | 完了 | wallbash パターンを忠実に踏襲 |
| T-007 | gha-guideline 更新 | 権限マトリクス更新 | 完了 | question ワークフロー追加 + スキル参照追加 |
| T-008 | workflow.md 更新 | GHA スキルセクション追加 | 完了 | 差異なし |
| T-009 | knowledge.md 追記 | 知見 #12, #13 追記 | 完了 | 差異なし |
| T-010 | inbox ファイル削除 | git rm | 完了 | 差異なし |
| T-011 | 知見記録 | 本セクション記載 | 完了 | 差異なし |
| T-012 | 課題転記 | 未転記課題確認 | 完了 | 転記対象なし |
| T-013 | メタルール横断検証 | 3領域検証 | 完了 | 1件の改善提案を 07_issues.md に起票 |

## 成果物一覧

### 新規作成
- `.claude/skills/gha-wallbash/SKILL.md`
- `.claude/skills/gha-execute/SKILL.md`
- `.claude/skills/gha-close/SKILL.md`
- `.claude/skills/gha-question/SKILL.md`

### 修正
- `.github/workflows/initiative-wallbash.yml` — プロンプト短縮化
- `.github/workflows/initiative-execute.yml` — プロンプト短縮化 + execution_file 修正
- `.github/workflows/initiative-close.yml` — プロンプト短縮化 + execution_file 修正
- `.github/workflows/initiative-question.yml` — プロンプト短縮化 + execution_file 修正

### 更新
- `.claude/skills/gha-guideline/SKILL.md` — 権限マトリクスに question 追加 + スキル参照追加
- `docs/workflow.md` — GHA Initiative スキルセクション追加
- `refs/claude-code-action/knowledge.md` — 知見 #12, #13 追記

### 削除
- `inbox/gha-execution-file-fix-rollout.md`

## 発生した課題

- gha-skills-mapping.yml に initiative ワークフローのマッピングが未登録（07_issues.md 参照、転記不要）

## 作業中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA 専用スキル作成時のテンプレートパターン | `.claude/skills/gha-*/SKILL.md` | frontmatter に `user-invocable: false` + 「CLAUDE.md や l1-manager のルールには従わない」明記 + やること/やらないことの分離が、スコープ制御問題の根本対策として有効。今後の GHA ワークフロー追加時にも同じパターンを適用すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | YAML プロンプト短縮化の効果 | プロンプトを「Read 指示 + 動的コンテキスト + 1行リマインダー」に短縮することで、YAML の行数が大幅に削減され可読性が向上した。一方、Claude がスキルファイルを Read しない場合のリスクは残る（knowledge.md #12 で記載済み） |
| 2 | execution_file 抽出パターンの標準化 | wallbash の jq 抽出パターン（`[.[] | select(.type == "assistant") | .message.content[]? | select(.type == "text") | .text] | last // empty`）は全ワークフローで共通利用可能。フォールバックメッセージは各ワークフロー固有のものを設定 |

## メタルール横断検証結果（T-013）

| 領域 | 結果 | 詳細 |
|------|------|------|
| (1) メタルールフロー記述 | 合格 | 新 GHA スキルは `user-invocable: false` で GHA からのみ使用。他スキルのフロー記述への影響なし。gha-guideline の関連ファイル一覧に4スキルを追加済み |
| (2) workflow.md 同期 | 修正済 | T-008 で「GHA Initiative スキル」セクションを追加し、スキル一覧テーブルと設計方針を記載 |
| (3) TG-008 基準連動 | 該当なし | GHA スキルはセッション型ライフサイクル（壁打ち/計画/実行/評価/ゲート判定）に該当しないため、TG-008 の走査対象には含めない。TG-010（GHA↔Skills整合性チェック）で gha-skills-mapping.yml を介してカバーされるべきだが、マッピング未登録を 07_issues.md に起票済み |

## 所感・次フェーズへの申し送り

- 全タスクが計画通り完了し、差異なし
- `gha-skills-mapping.yml` への initiative ワークフローマッピング追加は次回トリアージまたは別施策で対応推奨
- GHA ワークフローの動作検証（実際に Issue 作成 → ワークフロー起動）は本施策スコープ外だが、初回実行時に Read 指示が正しく動作するか確認が必要

---
**作成者**: L2（実施）
**作成日**: 2026-03-15
