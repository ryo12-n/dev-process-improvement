# 並列ディスパッチルール

> **このルールの位置づけ**
> マネージャーセッション（l1-manager, l1-impl-manager 等）が複数ワーカーを並列ディスパッチする際の前提条件・ファイル分離パターン・運用ルールを定義する。
> `manager-common-policy` §2.2 から参照される。

---

## §1 前提条件

並列ディスパッチは以下の3条件をすべて満たす場合のみ許可する。

| # | 条件 | 検証方法 |
|---|------|---------|
| 1 | **Conflict Check Matrix 検証済み** | `02a_task_division.md` の Conflict Check Matrix で、同一 Wave 内のタスク間にファイル書き込み競合（同一ファイルに対する複数タスクの CREATE/MODIFY）がないことを確認 |
| 2 | **Wave 割当定義済み** | `02a_task_division.md` の Wave Assignment で、依存関係に基づく Wave 分割が定義されている |
| 3 | **per-worker ファイル作成済み** | 各ワーカーの per-worker ファイル（下記 §2）がマネージャーにより事前に作成されている |

**フェールセーフ**: 条件が1つでも満たされていない場合、マネージャーはディスパッチを中止し、不足分を補完してからリトライする。

---

## §2 per-worker ファイル分離パターン

並列ディスパッチ時、ワーカー間のファイル競合を防ぐため、以下のファイルを per-worker 単位で分離する。

### §2.1 分離対象ファイル

| 本体ファイル | per-worker ファイル | 用途 |
|-------------|-------------------|------|
| `03_work_log.md` | `03_work_log_W<N>.md` | ワーカー N の作業履歴 |
| `07_issues.md` | `07_issues_W<N>.md` | ワーカー N の課題起票 |

- `<N>` はワーカー番号（1, 2, 3, ...）
- per-worker ファイルは `_template/03_work_log_W_template.md`、`_template/07_issues_W_template.md` からコピーして作成する

### §2.2 分離不要なファイル

以下のファイルは per-worker 分離不要（各ワーカーの成果物として独立して作成されるため）。

- `04_work_report.md` — 順次ディスパッチ時と同じく、最後にまとめて作成する

### §2.3 順次ディスパッチ時の扱い

順次ディスパッチ（従来方式）の場合は per-worker ファイルを使用しない。ワーカーは本体ファイル（`03_work_log.md`、`07_issues.md`）に直接記録する。

**判別条件**: マネージャーから Worker ID（`W<N>`）が指定されている場合は per-worker ファイルを使用する。Worker ID が指定されていない場合は本体ファイルを使用する。

---

## §3 Wave 方式の運用ルール

### §3.1 基本原則

- **Wave 内は並列**: 同一 Wave に割り当てられたタスクは同時に実行できる
- **Wave 間は逐次**: Wave N+1 のディスパッチは Wave N の全ワーカーが完了してから行う

### §3.2 Wave ディスパッチ手順

1. `02a_task_division.md` の Wave Assignment を確認する
2. 各ワーカーの per-worker ファイルを作成する（§2.1）
3. 事前検証チェックリスト（§3.3）を実行する
4. Wave 内の各ワーカーをサブエージェントとして並列起動する
5. 全ワーカー完了を待つ
6. Wave 完了後処理（§4）を実施する
7. 次の Wave があれば 2〜6 を繰り返す

### §3.3 事前検証チェックリスト

```
1. [ ] per-worker ファイル（03_work_log_W<N>.md, 07_issues_W<N>.md）が作成済み
2. [ ] Conflict Check Matrix で同一 Wave 内にファイル競合なし
3. [ ] 前 Wave の完了後処理が完了済み（Wave > 1 の場合）
```

---

## §4 成果物統合手順

Wave 完了後（または全 Wave 完了後）に、マネージャーが per-worker ファイルを本体ファイルに統合する。

### §4.1 統合手順

1. **課題ファイルの統合**: 各 `07_issues_W<N>.md` の内容を `07_issues.md` に転記する
   - 課題IDの重複がないことを確認する
   - 転記元の per-worker ファイルは削除しない（証跡として保持）
2. **作業ログの確認**: 各 `03_work_log_W<N>.md` の内容を確認する
   - 全ワーカーが完了状態であることを確認する
   - per-worker ファイルは統合せず、個別ファイルとして保持する（ワーカー別の作業経緯を追跡可能にするため）
3. **タスクステータスの更新**: `02_tasks.md` の該当タスクのステータスを更新する

### §4.2 統合後チェックリスト

```
1. [ ] 全ワーカーが完了（COMPLETE）または停止（BLOCK）状態
2. [ ] per-worker 課題ファイルの内容が 07_issues.md に統合済み
3. [ ] 02_tasks.md のタスクステータスが更新済み
```

---

## §5 worktree 方式への escalation パス

本ルールの per-worker ファイル分離パターンは、文書中心リポジトリ（dev-process-improvement）を主な適用対象として設計されている。

コード実装を伴う外部リポジトリでの並列ディスパッチでは、per-worker ファイル分離に加え、git worktree による物理隔離が必要になる場合がある。その場合は `l1-impl-manager/SKILL.md` の「並列ディスパッチ機構」セクションを参照すること。

### 判断基準

| 条件 | 推奨方式 |
|------|---------|
| 文書中心の変更（`.claude/skills/`、`sessions/`、`docs/` 等） | per-worker ファイル分離（本ルール） |
| コード実装を伴う外部リポジトリの変更 | per-worker ファイル分離 + git worktree（l1-impl-manager 参照） |

---

**作成日**: 2026-03-17
**関連施策**: `sessions/initiatives/l1-manager-enhanced-planning/`
**参照元**: `manager-common-policy` §2.2、`session-flow-policy` §4.2
