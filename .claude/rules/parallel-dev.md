# 並列ディスパッチルール

> **このルールの位置づけ**
> マネージャーセッション（l1-manager, l1-impl-manager 等）が複数ワーカーを並列ディスパッチする際の前提条件・set コピー方式・運用ルールを定義する。
> `manager-common-policy` §2.2 から参照される。

---

## §1 前提条件

並列ディスパッチは以下の3条件をすべて満たす場合のみ許可する。

| # | 条件 | 検証方法 |
|---|------|---------|
| 1 | **Conflict Check Matrix 検証済み** | `phase-1-planning/set-N/08_task_division.md` の Conflict Check Matrix で、同一 Wave 内のタスク間にファイル書き込み競合（同一ファイルに対する複数タスクの CREATE/MODIFY）がないことを確認 |
| 2 | **Wave 割当定義済み** | `phase-1-planning/set-N/08_task_division.md` の Wave Assignment で、依存関係に基づく Wave 分割が定義されている |
| 3 | **set ディレクトリ作成済み** | 各ワーカーの set ディレクトリ（下記 §2）がマネージャーにより事前に作成されている |

**フェールセーフ**: 条件が1つでも満たされていない場合、マネージャーはディスパッチを中止し、不足分を補完してからリトライする。

---

## §2 set コピー方式

並列ディスパッチ時、ワーカー間のファイル競合を防ぐため、phase 内の `_template/` を `set-N/` にコピーして各ワーカーに割り当てる。

### §2.1 set ディレクトリの作成

`phase-2-execution/_template/` を `phase-2-execution/set-N/` にコピーする（N = 1, 2, 3, ...）。

各 set ディレクトリには以下のワーカーセット 7 ファイルが含まれる:

| ファイル | 用途 |
|---------|------|
| `01_worker_plan.md` | タスク理解・不明点解消（壁打ち） |
| `02_worker_log.md` | 作業中の判断・メモ |
| `03_worker_report.md` | 振り返り・課題発見 |
| `04_eval_plan.md` | 評価観点の整理（壁打ち） |
| `05_eval_log.md` | 評価中の判断・メモ |
| `06_eval_report.md` | 評価結果・改善点 |
| `07_issues.md` | 課題バッファ |

各 set は独立したワーキングスペースであり、ワーカー間のファイル競合が構造的に発生しない。

### §2.2 set 内の作業分離

set 方式では、ワーカーの全成果物が `set-N/` 内に完結する。`03_worker_report.md` も set 内に作成されるため、分離不要ファイルの概念は不要。

### §2.3 順次ディスパッチ時の扱い

順次ディスパッチ（単一ワーカー）の場合は `set-1/` を使用する。マネージャーは `_template/` を `set-1/` にコピーしてワーカーに割り当てる。

**判別条件**: マネージャーから set 番号（`set-N`）が指定されている場合はその set ディレクトリを使用する。set 番号が指定されていない場合は `set-1/` を使用する。

---

## §3 Wave 方式の運用ルール

### §3.1 基本原則

- **Wave 内は並列**: 同一 Wave に割り当てられたタスクは同時に実行できる
- **Wave 間は逐次**: Wave N+1 のディスパッチは Wave N の全ワーカーが完了してから行う

### §3.2 Wave ディスパッチ手順

1. `phase-1-planning/set-N/08_task_division.md` の Wave Assignment を確認する
2. 各ワーカーの set ディレクトリを作成する（§2.1）
3. 事前検証チェックリスト（§3.3）を実行する
4. Wave 内の各ワーカーをサブエージェントとして並列起動する
5. 全ワーカー完了を待つ
6. Wave 完了後処理（§4）を実施する
7. 次の Wave があれば 2〜6 を繰り返す

### §3.3 事前検証チェックリスト

```
1. [ ] set ディレクトリ（phase-2-execution/set-N/）が作成済み
2. [ ] Conflict Check Matrix で同一 Wave 内にファイル競合なし
3. [ ] 前 Wave の完了後処理が完了済み（Wave > 1 の場合）
```

---

## §4 成果物統合手順

Wave 完了後（または全 Wave 完了後）に、マネージャーが set 間の課題を集約する。

### §4.1 統合手順

1. **課題ファイルの集約確認**: 各 `phase-2-execution/set-N/07_issues.md` の内容を確認する
   - 施策をまたぐ課題が `issues/entries/ISS-XXX.md` に転記されていることを確認する
   - 各 set の課題ファイルは個別ファイルとして保持する（ワーカー別の作業経緯を追跡可能にするため）
2. **作業ログの確認**: 各 `phase-2-execution/set-N/02_worker_log.md` の内容を確認する
   - 全ワーカーが完了状態であることを確認する
3. **タスクステータスの更新**: `03_tasks.md` の該当タスクのステータスを更新する

### §4.2 統合後チェックリスト

```
1. [ ] 全ワーカーが完了（COMPLETE）または停止（BLOCK）状態
2. [ ] 各 set の課題ファイルの内容が確認済み（施策をまたぐ課題は ISS 転記済み）
3. [ ] 03_tasks.md のタスクステータスが更新済み
```

---

## §5 worktree 方式への escalation パス

本ルールの set コピー方式は、文書中心リポジトリ（dev-process-improvement）を主な適用対象として設計されている。

コード実装を伴う外部リポジトリでの並列ディスパッチでは、set コピー方式に加え、git worktree による物理隔離が必要になる場合がある。その場合は `l1-impl-manager/SKILL.md` の「並列ディスパッチ機構」セクションを参照すること。

### 判断基準

| 条件 | 推奨方式 |
|------|---------|
| 文書中心の変更（`.claude/skills/`、`sessions/`、`docs/` 等） | set コピー方式（本ルール） |
| コード実装を伴う外部リポジトリの変更 | set コピー方式 + git worktree（l1-impl-manager 参照） |

---

**作成日**: 2026-03-17
**最終更新**: 2026-03-20（per-worker ファイル方式 → set コピー方式に改訂）
**関連施策**: `sessions/initiatives/l1-manager-enhanced-planning/`, `sessions/initiatives/template-structure-unification/`
**参照元**: `manager-common-policy` §2.2、`session-flow-policy` §4.2
