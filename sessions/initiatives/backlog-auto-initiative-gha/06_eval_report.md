# 評価レポート: backlog-auto-initiative-gha

## 評価サマリ

全体として実装品質は良好であり、成功基準4項目のうち3項目を完全に達成、1項目を一部達成と判定する。YAML 構文は正しく、セキュリティ面では API キーの Secrets 参照・env 経由のインジェクション対策が適切に実装されている。主な指摘事項は、Phase 2 の `gh issue close/edit` ステップで `${{ github.event.issue.number }}` をシェルコマンドに直接展開している点（低リスクだが改善余地あり）、Claude Code プロンプトに `00_proposal.md` の「backlog元ファイル」記入ステップが欠落している点の2つ。条件付きで次フェーズ進行を推奨する。

## 評価結果

| # | 評価項目 | 判定基準 | 結果 | 判定 |
|---|---------|---------|------|------|
| 1 | YAML 構文 | 2ファイルとも構文エラーなし | Python yaml.safe_load で検証、エラーなし | ✅ |
| 2 | secrets 参照の安全性 | API キーがハードコードされていないこと | `${{ secrets.ANTHROPIC_API_KEY }}` 経由で参照。ハードコードなし | ✅ |
| 3 | permissions 最小権限 | 不要な権限が付与されていないこと | Phase 1: `issues: write`, `contents: read` — 適切。Phase 2: `contents: write`, `pull-requests: write`, `issues: write`, `id-token: write` — `id-token: write` は claude-code-action@v1 の OIDC 認証に必要だが、セキュリティ上の懸念あり（GitHub Issue #1010）。ただし現時点では必須権限 | ✅（注意事項あり） |
| 4 | トリガー条件 | 設計通りであること | Phase 1: cron 3h + workflow_dispatch。Phase 2: issues labeled + ラベル二重チェック（auto-initiative-approved AND auto-initiative-pending）。設計通り | ✅ |
| 5 | CSV パース エッジケース | 実データで正しい候補選択 | 空行: 正しくスキップ。日本語ファイル名（スペース含む）: 正常動作。候補なし: `has_candidate=false` を正しく出力。カンマ含みフィールド: 動作しない（既知の制限としてコメント記載済み） | ✅ |
| 6 | Claude Code プロンプト L1 フロー網羅性 | テンプレートコピー〜ゲート判定〜backlog 削除の全ステップ含む | 8ステップ中7ステップを網羅。`00_proposal.md` の「backlog元ファイル」記入（TG-002 突合用）が欠落 | ❌（軽微） |
| 7 | docs/workflow.md 記載 | 実装との整合性 | 2フェーズアーキテクチャ・対象条件・ラベルフロー・手動設定が正確に記載されている | ✅ |
| 8 | インジェクション対策 | `${{ }}` 直接展開リスクなし | Phase 1: Issue body の変数は env 経由で安全に渡されている。Phase 2: `gh issue close/edit` で `${{ github.event.issue.number }}` を直接展開（整数値のため実害リスクは極めて低いが、ベストプラクティスとしては env 経由が望ましい）。Phase 1 の `cat "backlog/entries/${{ steps.select.outputs.file }}"` は CSVデータ由来の値をパスに直接展開しており、CSVデータが攻撃者に制御される可能性は低いが、ベストプラクティスとしては env 経由が望ましい | ✅（改善提案あり） |

## 計画の成功基準に対する達成度

| 成功基準 | 達成度 | 根拠 |
|---------|--------|------|
| 1. backlog-candidate-propose.yml が作成され、cron + workflow_dispatch の2トリガーが定義 | 達成 | ファイル存在確認済み。`schedule: cron: '0 */3 * * *'` と `workflow_dispatch: {}` の2トリガーが定義されている |
| 2. backlog-auto-execute.yml が作成され、auto-initiative-approved ラベルトリガーで claude-code-action@v1 実行 | 達成 | `issues: [labeled]` トリガー + `github.event.label.name == 'auto-initiative-approved'` 条件 + `anthropics/claude-code-action@v1` 設定を確認 |
| 3. select-backlog-candidate.sh が作成され、CSV パースが正しく動作 | 達成 | 実 backlog.csv（54行）で正しい候補（dev-workflow-detail L1参照精査、起票日 2026-03-05）が選択されることを確認 |
| 4. セキュリティ: API キーハードコードなし、permissions 最小権限 | 一部達成 | API キーは Secrets 参照。permissions は概ね最小だが、`id-token: write` の OIDC セキュリティ懸念（Issue #1010）が存在する。これは claude-code-action@v1 の仕様上必要な権限であり、施策側での対処は困難 |

## 発見された課題・改善提案

### 課題

1. **Claude Code プロンプトの L1 フローステップ欠落**（07_issues.md EVL-001）: `backlog-auto-execute.yml` のプロンプトに `00_proposal.md` の「backlog元ファイル」記入ステップが含まれていない。TG-002 突合チェック時に紐づけが取れなくなるリスクがある。

2. **Phase 2 の `${{ }}` 直接展開**（07_issues.md EVL-002 / ISS-058）: `gh issue close/edit` ステップで `${{ github.event.issue.number }}` をシェルコマンドに直接展開している。整数値のため実害リスクは極めて低いが、Phase 1 の Issue body 作成で採用した env 経由パターンと一貫性がない。

### 改善提案

- **EVL-001 の修正**: プロンプトのステップ2とステップ7の間に「`00_proposal.md` の末尾メタ情報の『backlog元ファイル』に元ファイル名を記入」を追加する
- **EVL-002 の修正**: `ISSUE_NUMBER: ${{ github.event.issue.number }}` を `env:` に追加し、`run:` 内では `${ISSUE_NUMBER}` を使用する
- **Phase 1 の `cat` コマンド**: `backlog/entries/${{ steps.select.outputs.file }}` を env 経由に変更する（`ENTRY_FILE: ${{ steps.select.outputs.file }}`）

#### 実施ワーカー未転記課題

- **件数**: 0件
- 07_issues.md に「なし」と記載されており、未転記課題は存在しない

## 評価中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA ワークフローの `run:` ブロックでは `${{ }}` 式をシェルコマンドに直接展開せず、必ず `env:` 経由で渡すべき。整数値であっても一貫して適用する | `.github/workflows/` | Phase 1 では env 経由パターンが採用されているが Phase 2 の close/edit ステップでは直接展開が残っている。今後 GHA ワークフローを作成・レビューする際のチェック項目として `.claude/rules/` にルール化を検討 |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | `claude-code-action@v1` は `id-token: write` 権限が OIDC 認証のために必須だが、GitHub Issue #1010 でセキュリティ懸念が指摘されている（Claude セッションが OIDC トークンを発行できてしまう）。将来のバージョンで改善される可能性があるため、アップデート時に再確認が必要 | Phase 2 の permissions 評価時に発見。現時点では代替手段がなく、施策側での対処は困難。claude-code-action のバージョンアップ時に再評価すべき |

## 次フェーズへの推奨

**条件付きで進める**

理由:
- 成功基準4項目のうち3項目は完全達成、1項目（セキュリティ）は外部依存（claude-code-action@v1 の OIDC 仕様）により完全対処が困難だが、許容範囲内
- EVL-001（プロンプトの backlog元ファイル記入ステップ欠落）は軽微だが修正が望ましい。ゲート判定前の修正を推奨
- EVL-002（${{ }} 直接展開）は低リスクであり、次回の保守タスクでの対応で可

---
**作成者**: L2（評価）
**作成日**: 2026-03-13
