# スキャンレポート: Set-1

## 担当タスク

| タスクID | 対象 | ステータス |
|---------|------|-----------|
| AT-001 | `.claude/skills/`, `.claude/rules/`, `.claude/hooks/`, `.github/workflows/`, `docs/` | 完了 |
| AT-002 | `automation-candidates/entries/*.md`, CSV | 完了 |
| AT-003 | `backlog/entries/*.md`, `sessions/initiatives/_archive/`, `.claude/hooks/`, `.claude/settings.json` | 完了 |
| AT-004 | AT-001〜AT-003 の結果 | 完了 |

## AT-001: 新規自動化候補スキャン

| # | 定型作業名 | 発生源 | カテゴリ | 推奨自動化手段 | 頻度 | 手動コスト | 実装難易度 | 優先度スコア |
|---|----------|--------|--------|-------------|------|----------|----------|-----------|
| 1 | GHA ワークフロー権限整合性チェック | `.claude/skills/gha-guideline/SKILL.md` セクション1.2 | 品質チェック | script | 毎ワークフロー作成/変更時 (1) | 2 | 2 | 1.0 |
| 2 | initiative ディスパッチャー入力バリデーション | `.github/workflows/initiative-dispatcher.yml` | 品質チェック | hook (PreToolUse) | 毎ディスパッチ時 (1) | 1 | 2 | 0.5 |

### 候補検出の補足

**走査範囲と検出プロセス**:

1. **新規 rules 5件の走査結果**:
   - `commit-message.md`: AC-002 で既にカバー（PreToolUse hook でバリデーション）
   - `gha-workflow-security.md`: チェックリスト形式の手動確認。ワークフロー作成時の1回限りのため自動化の費用対効果は低い
   - `pr-url-output.md`: AC-003 で既にカバー（Stop hook でチェック）
   - `rebase-conflict-handling.md`: 状況依存の判断を伴うため自動化不向き
   - `session-start-branch-cleanup.md`: AC-001 として実装済み

2. **新規 skills の走査結果**:
   - `automation-manager`: メタ的なセッション管理であり、自動化対象の走査自体が定型作業とは言えない
   - `config-optimizer-manager`: 3フェーズ構造のオーケストレーション。判断を伴う対話的プロセスで自動化不向き
   - `l1-impl-manager`: 4フェーズの並列ディスパッチ機構。Wave 方式は複雑で自動化の余地は限定的。worktree 作成・事前検証チェックリストはスクリプト化可能だが、l1-impl-manager 固有の作業で汎用性が低い
   - `gha-wallbash/execute/close/question/test`: GHA 専用スキル群。ワークフロー YAML 側で起動されるため、スキル自体の自動化は不要。権限整合性チェック（セクション1.2）が新規候補として検出
   - `session-flow-policy`: ポリシー定義であり定型作業を生まない
   - `gha-guideline`: 権限マトリクス（セクション5）の更新が定型的だが、ワークフロー追加/変更時のみで頻度が低い

3. **GHA ワークフロー群の走査結果**:
   - 9件のワークフロー（daily-triage, initiative-dispatcher, initiative-wallbash/execute/close/question, backlog-to-issue, test-skill-reading, test-permissions）
   - initiative-dispatcher の inputs 検証（施策名の形式チェック等）が候補として検出されたが、優先度は低い

4. **既存候補との重複確認**: 新規候補2件はいずれも既存 AC-001〜AC-014 と重複なし

## AT-002: 既存候補の再評価

| 候補ID | 候補名 | 変更項目 | 変更前 | 変更後 | 変更理由 |
|--------|--------|---------|--------|--------|---------|
| AC-001 | セッション開始時のブランチ整理 | ステータス | backlog起票済 | 実装完了 | SessionStart hook として `.claude/hooks/session-start-branch-cleanup.sh` に実装済み。`.claude/settings.json` に登録済み。施策アーカイブ済み（`_archive/session-branch-cleanup-flow/`）。ゲート判定「通過」 |
| AC-002 | コミットメッセージ規約の遵守 | ステータス | 候補 | backlog起票済 | BL-029（PreToolUse hookコミットメッセージバリデーション）として backlog に起票済み |
| AC-002 | コミットメッセージ規約の遵守 | 関連backlog | (空) | BL-029 | backlog エントリとの紐付け |
| AC-010 | 施策クローズ・アーカイブ移動 | 優先度スコア | 6.0 | 4.0 | gha-close スキルが GHA 環境でのアーカイブ移動（`git mv` + コミット）を実装済み。CLI 環境のみ手動残存。手動コストを 3→2 に下方修正 |
| AC-010 | 施策クローズ・アーカイブ移動 | 備考 | - | gha-close スキルで GHA 環境カバー済み | 環境変化の記録 |
| AC-012 | ルール変更時の連動更新チェック | ステータス | 候補 | backlog起票済 | BL-030（PostToolUse hookルール変更連動チェック）として backlog に起票済み |
| AC-012 | ルール変更時の連動更新チェック | 関連backlog | (空) | BL-030 | backlog エントリとの紐付け |
| AC-014 | 外部リポジトリの整理 | 自動化方針 | R-001 のスクリプトに統合して SessionStart hook で実装可能 | external-repo-cleanup スキルとして別実装済み。hook 統合ではなくスキル参照で対応 | `.claude/skills/external-repo-cleanup/SKILL.md` が存在。l1-impl-manager の壁打ちフェーズから参照されている。hook 統合よりスキル方式が適切 |
| AC-014 | 外部リポジトリの整理 | 優先度スコア | 6.0 | 3.0 | スキルとして部分実装済み。手動コストを 2→1 に下方修正（スキルが手順をガイドするため） |

### 変更なしの候補（8件）

| 候補ID | 候補名 | 現優先度 | 据え置き理由 |
|--------|--------|---------|------------|
| AC-003 | PR URL 出力形式の統一 | 1.5 | 環境変化なし。Stop hook での自動チェックは引き続き候補 |
| AC-004 | テンプレートコピーと施策ディレクトリ作成 | 2.0 | gha-wallbash が Glob+Read+Write で実装しているが、CLI 環境では `cp -r` が依然有効。優先度変更なし |
| AC-005 | 壁打ちフェーズの実施 | 1.0 | 対話的プロセスのため自動化不向き。変更なし |
| AC-006 | 作業履歴のタイムスタンプ付き記録 | 1.5 | 環境変化なし |
| AC-007 | 知見記録（ルール化候補・参考情報） | 2.0 | 環境変化なし |
| AC-008 | 課題起票・CSV転記 | 4.0 | 3段階転記は依然手動。GHA 環境では gha-close が知見ルーティングを自動化しているが、課題 CSV 転記は未自動化 |
| AC-009 | ゲート判定の実施 | 1.3 | 判断を伴うため自動化不向き。変更なし |
| AC-011 | トリアージ走査 | 2.0 | 環境変化なし |
| AC-013 | マネージャー共通ポリシーの遵守 | 1.0 | 対話的プロセスのため自動化不向き。変更なし |

## AT-003: 実装進捗確認

| 候補ID | 候補名 | 現ステータス | 関連施策 | 進捗状況 | 推奨アクション |
|--------|--------|------------|---------|---------|-------------|
| AC-001 | セッション開始時のブランチ整理 | backlog起票済 → **実装完了** | `_archive/session-branch-cleanup-flow/` | `.claude/hooks/session-start-branch-cleanup.sh`（126行）として完全実装済み。`settings.json` に SessionStart hook 登録済み（matcher: "startup"）。施策はゲート「通過」判定でアーカイブ済み。ルールファイルは「実行ロジック移行済み」バナー付きで設計仕様リファレンスとして維持 | ステータスを「実装完了」に更新。CSV の最終評価日を 2026-03-16 に更新 |

### AC-001 実装の詳細

- **実装ファイル**: `.claude/hooks/session-start-branch-cleanup.sh`
- **登録**: `.claude/settings.json` の `hooks.SessionStart[0]`（matcher: "startup"）
- **設計仕様**: `.claude/rules/session-start-branch-cleanup.md`（リファレンスとして維持）
- **施策アーカイブ**: `sessions/initiatives/_archive/session-branch-cleanup-flow/`
- **ゲート判定**: 全4件の成功基準を達成、「通過」判定（2026-03-07）
- **実装カバレッジ**:
  - ステップ1〜5: hook で完全実装
  - ステップ6（外部リポ整理）: hook には含まず、`external-repo-cleanup` スキルとして別実装
  - matcher: "startup" のみ（resume は並列セッション問題の回避のため対象外、設計通り）
- **出力形式**: JSON（branch, action, pr_url, warnings, errors）
- **安全性**: 全パスで exit 0 を保証

## AT-004: backlog 起票提案

| # | 候補ID | 候補名 | 優先度スコア | 提案理由 | backlog ドラフト |
|---|--------|--------|------------|---------|----------------|
| 1 | (新規) | GHA ワークフロー権限整合性チェック | 1.0 | gha-guideline の権限3層モデル（L1 GHA権限 / L2 Claude Code ツール / L3 プロンプト指示）の整合性を、ワークフロー YAML とスキルファイルから自動チェックするスクリプト。現在9ワークフローが存在し、手動確認では漏れリスクがある。ただし頻度が低い（ワークフロー追加/変更時のみ）ため即時起票は不要 | 候補登録のみ（AC-015 として登録提案）。backlog 起票は次回メンテナンスで再評価 |
| 2 | (新規) | initiative ディスパッチャー入力バリデーション | 0.5 | initiative-dispatcher.yml の inputs（施策名・コマンド）の形式検証。優先度が低く即時起票は不要 | 候補登録のみ（AC-016 として登録提案）。backlog 起票は見送り |

### ステータス更新提案（backlog 起票不要）

| 候補ID | 更新内容 | 理由 |
|--------|---------|------|
| AC-001 | ステータス: backlog起票済 → 実装完了 | SessionStart hook として完全実装済み |
| AC-002 | ステータス: 候補 → backlog起票済、関連backlog: BL-029 | BL-029 として backlog に起票済み |
| AC-010 | 優先度スコア: 6.0 → 4.0 | gha-close で GHA 環境カバー済み |
| AC-012 | ステータス: 候補 → backlog起票済、関連backlog: BL-030 | BL-030 として backlog に起票済み |
| AC-014 | 優先度スコア: 6.0 → 3.0、自動化方針更新 | external-repo-cleanup スキルで部分実装済み |

## 課題起票
- 起票件数: 1 件（`07_issues.md` に起票）

## 走査中の知見

### ルール化候補（.claude/rules/ や roles/ に反映できるパターン）

| # | 知見 | 対象ファイル・領域 | 詳細 |
|---|------|-----------------|------|
| 1 | GHA スキルの「やらないこと」共通4項目は全 GHA スキルで統一されており、テンプレートパターンとして確立している | `.claude/skills/gha-*/SKILL.md` | gha-guideline セクション7.2 で定義済み。新規 GHA スキル作成時の必須チェック項目として rule-change-checklist への追加を検討 |
| 2 | hook 実装後のルールファイル維持パターン（「実行ロジック移行済み」バナー + 設計仕様リファレンス）は他の hook 実装時にも適用すべき | `.claude/rules/session-start-branch-cleanup.md` | AC-001 の実装で確立されたパターン。AC-002（BL-029）実装時にも同じパターンを適用すべき |

### 参考情報（文脈依存の気づき・今後の参考）

| # | 知見 | 背景・文脈 |
|---|------|-----------|
| 1 | GHA 環境と CLI 環境で同じ定型作業の自動化手段が異なる場合がある | AC-010（アーカイブ移動）は GHA では gha-close スキル、CLI ではスクリプト化が必要。AC-004（テンプレートコピー）も GHA では Glob+Read+Write、CLI では cp -r。環境別の自動化方針を候補エントリに記載すべき |
| 2 | backlog 起票済みの候補（AC-002→BL-029、AC-012→BL-030）が automation-candidates の CSV/エントリに反映されていない | 候補管理と backlog 管理の間の同期が手動に依存しており、ステータス乖離が発生している。次回メンテナンスまでに候補管理の更新プロセスを明確化すべき |
| 3 | hook 実装の「全パス exit 0」パターンは安全性の観点で重要 | session-start-branch-cleanup.sh の設計判断。hook がセッション開始をブロックしないことを保証する。今後の hook 実装（AC-002 等）でも同じパターンを適用すべき |

---
**作成者**: オートメーションワーカー
**作成日**: 2026-03-16
