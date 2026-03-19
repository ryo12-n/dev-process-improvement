# タスクリスト: GHA施策パイプライン一気通貫実行と並列化

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | GHA ワークフロー YAML とスキル定義の変更であり汎用ワーカーで対応可能 | Worker |
| なし | - | GHA セキュリティチェックリストに基づく評価は汎用評価者で対応可能 | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker (Set-1) | T-001 | L規模。initiative-execute.yml 自動連鎖 |
| L2-worker (Set-2) | T-002, T-003, T-005 | S規模3件を集約 |
| L2-worker (Set-3) | T-004 | M規模。batch-approve 新規作成 |
| L2-evaluator | T-E01, T-E02 | 固定タスク |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker-W1 | L2-evaluator | T-001 | Wave 1 |
| Set-2 | L2-worker-W2 | L2-evaluator | T-002, T-003, T-005 | Wave 1 |
| Set-3 | L2-worker-W3 | L2-evaluator | T-004 | Wave 1 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1, Set-2, Set-3 | 並列（Wave 1） | なし | 全タスクのファイル書き込み先が独立 |

> **方式**: 並列（Wave 方式、`.claude/rules/parallel-dev.md` 参照）

## タスク一覧

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `initiative-execute.yml` に自動連鎖ディスパッチを追加 | 下記詳細参照 | 🔴 | ⬜ |
| T-002 | `initiative-dispatcher.yml` の approve(wallbashing) ルートに `retry_count=0` を追加 | `-f retry_count="0"` が追加され、既存パラメータに変更なし | 🟡 | ⬜ |
| T-003 | `backlog-to-issue.yml` の cron を30分間隔に変更 | cron が `*/30 * * * *` に変更され、scheduled-create ジョブの `if` 条件が維持されている | 🟡 | ⬜ |
| T-004 | `initiative-batch-approve.yml` を新規作成 | 下記詳細参照 | 🔴 | ⬜ |
| T-005 | `gha-execute/SKILL.md` に GATE_VERDICT 出力制約を追加 | /approve と /reject の両フローに `GATE_VERDICT: 通過\|差し戻し` 出力指示が記載されている | 🟡 | ⬜ |
| T-F01 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録 | 「ルール化候補」「参考情報」の両テーブルに最低1行 | 🔴 | ⬜ |
| T-F02 | `07_issues.md` の未転記課題を確認し、施策横断課題を `issues/entries/ISS-XXX.md` に転記 | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

### T-001 詳細: initiative-execute.yml 自動連鎖ディスパッチ

**変更対象**: `.github/workflows/initiative-execute.yml`

**変更内容**:
1. `inputs:` ブロックに `retry_count` 入力を追加（type: number, required: false, default: 0）
2. `permissions` に `actions: write` を追加（`gh workflow run` に必要。それ以外の権限は変更しない）
3. `Extract gate review summary` ステップの後に verdict 抽出ステップを追加:
   - SUMMARY から `GATE_VERDICT: <判定>` を grep で抽出し `GITHUB_OUTPUT` に `verdict` を出力
4. `Update labels to gate-review` ステップの後に自動連鎖ディスパッチステップを追加:
   - verdict=`通過` or `条件付き通過` → `initiative-close.yml` をディスパッチ（issue_number, initiative_dir, branch）
   - verdict=`差し戻し` and retry_count < 2 → `initiative-execute.yml` をセルフディスパッチ（command=reject, phase=gate-review, retry_count+1）
   - verdict=`差し戻し` and retry_count >= 2 → Issue にコメント「自動リトライ上限に達しました」して停止
   - verdict 未検出 → 従来動作（gate-review ラベルで停止）

**完了条件**:
- 上記4点が全て実装されている
- `${{ }}` を `run:` ブロックで直接展開していない（`env:` 経由）
- `retry_count` の入力値は `env:` 経由でシェル変数として使用する

### T-004 詳細: initiative-batch-approve.yml 新規作成

**作成先**: `.github/workflows/initiative-batch-approve.yml`

**要件**:
- `workflow_dispatch` トリガーのみ（schedule なし）
- `initiative:wallbashing` ラベルの open Issue を一覧取得
- 各 Issue のメタデータコメント（`initiative-metadata`）から initiative_dir, branch を抽出
- 各 Issue に対して `initiative-execute.yml` をディスパッチ（issue_number, command=approve, phase=wallbashing, initiative_dir, branch, retry_count=0）
- ディスパッチ結果のサマリーをログ出力（処理件数、スキップ件数）
- メタデータ未検出の Issue はスキップし warning 出力
- `${{ }}` を `run:` ブロックで直接展開しない（`env:` 経由）
- permissions: contents: read, issues: read, actions: write

---
**作成者**: L1
**最終更新**: 2026-03-19
