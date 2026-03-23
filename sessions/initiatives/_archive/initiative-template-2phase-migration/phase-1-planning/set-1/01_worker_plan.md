# 計画ワーカー: initiative-template-2phase-migration

## 壁打ちフェーズ [2026-03-20]

### 理解のサマリー
- タスクの目的: `sessions/initiatives/_template/` の旧フラット構造（16ファイル）を `session-lifecycle-policy` §1.4.3 定義の 2-phase 構造に改修する
- スコープ: テンプレートファイルのリネーム・移動・新規作成・削除。内容の改善は行わない。ポリシーの「移行中」注記解除と l1-manager/SKILL.md の整合確認も含む
- 完了条件: `phase-1-planning/set-1/08_task_division.md` と `phase-1-planning/set-1/03_worker_report.md` が作成されていること

### 前提条件チェック
- [x] 施策計画（01_plan.md）の内容を理解: 理解済み — 成功基準7項目、変更対象テーブル（削除11件、リネーム7件、新規作成17件、ポリシー更新1件）を確認
- [x] 提案書（00_proposal.md）の確認: 確認済み — template-structure-unification 施策でポリシー側は更新済み、本施策は実ファイルの構造変更に集中
- [x] 変更対象ファイル群の特定: 特定済み

### 不明点・確認事項
なし

### 分析結果

#### 現状の _template/ 構造（旧: フラット16ファイル）
```
_template/
├── 00_proposal.md
├── 00a_wallbash_log.md
├── 01_plan.md
├── 02_tasks.md
├── 02a_task_division.md
├── 02b_dispatch_log.md
├── 03_work_log.md
├── 03_work_log_W_template.md
├── 04_work_report.md
├── 05_eval_plan.md
├── 06_eval_report.md
├── 07_issues.md
├── 07_issues_W_template.md
├── 08_gate_review.md
└── 09_cost_record.md
```

#### §1.4.3 定義の新構造（2-phase）
```
_template/
├── 00_wallbash_log.md
├── 01_proposal.md
├── 02_plan.md
├── 03_tasks.md
├── 04_dispatch_log.md
├── 05_gate_review.md
├── 06_cost_record.md
├── phase-1-planning/
│   ├── 01_gate.md
│   └── _template/
│       ├── 01_worker_plan.md
│       ├── 02_worker_log.md
│       ├── 03_worker_report.md
│       ├── 04_eval_plan.md
│       ├── 05_eval_log.md
│       ├── 06_eval_report.md
│       ├── 07_issues.md
│       └── 08_task_division.md
└── phase-2-execution/
    ├── 01_gate.md
    └── _template/
        ├── 01_worker_plan.md
        ├── 02_worker_log.md
        ├── 03_worker_report.md
        ├── 04_eval_plan.md
        ├── 05_eval_log.md
        ├── 06_eval_report.md
        └── 07_issues.md
```

#### ファイル対応マッピング

| 旧パス | 新パス | 操作 |
|--------|--------|------|
| `00a_wallbash_log.md` | `00_wallbash_log.md` | リネーム |
| `00_proposal.md` | `01_proposal.md` | リネーム |
| `01_plan.md` | `02_plan.md` | リネーム |
| `02_tasks.md` | `03_tasks.md` | リネーム |
| `02b_dispatch_log.md` | `04_dispatch_log.md` | リネーム |
| `08_gate_review.md` | `05_gate_review.md` | リネーム |
| `09_cost_record.md` | `06_cost_record.md` | リネーム |
| `02a_task_division.md` | `phase-1-planning/_template/08_task_division.md` | 移動 |
| `03_work_log.md` | → 内容を `phase-2-execution/_template/02_worker_log.md` に移行 | 移動（ファイル名変更あり） |
| `04_work_report.md` | → 内容を `phase-2-execution/_template/03_worker_report.md` に移行 | 移動（ファイル名変更あり） |
| `05_eval_plan.md` | → 内容を `phase-2-execution/_template/04_eval_plan.md` に移行 | 移動（番号変更なし） |
| `06_eval_report.md` | → 内容を `phase-2-execution/_template/06_eval_report.md` に移行 | 移動（番号変更なし） |
| `07_issues.md` | → 内容を `phase-2-execution/_template/07_issues.md` に移行 | 移動（番号変更なし） |
| `03_work_log_W_template.md` | （削除） | set コピー方式で不要 |
| `07_issues_W_template.md` | （削除） | set コピー方式で不要 |
| （なし） | `phase-1-planning/01_gate.md` | 新規作成 |
| （なし） | `phase-1-planning/_template/01_worker_plan.md` | 新規作成 |
| （なし） | `phase-1-planning/_template/02_worker_log.md` | 新規作成 |
| （なし） | `phase-1-planning/_template/03_worker_report.md` | 新規作成 |
| （なし） | `phase-1-planning/_template/04_eval_plan.md` | 新規作成 |
| （なし） | `phase-1-planning/_template/05_eval_log.md` | 新規作成 |
| （なし） | `phase-1-planning/_template/06_eval_report.md` | 新規作成 |
| （なし） | `phase-1-planning/_template/07_issues.md` | 新規作成 |
| （なし） | `phase-2-execution/01_gate.md` | 新規作成 |
| （なし） | `phase-2-execution/_template/01_worker_plan.md` | 新規作成 |
| （なし） | `phase-2-execution/_template/05_eval_log.md` | 新規作成 |

#### phase-1 と phase-2 のテンプレート内容差異

§1.4.2 で initiative 向けワーカーセットは同じ 7 ファイルと定義されているが、ロールが異なる:
- **phase-1-planning**: plan-worker / plan-evaluator が使用。壁打ちテンプレートは計画の理解・分析計画向け
- **phase-2-execution**: worker / evaluator が使用。壁打ちテンプレートは実施タスクの理解・環境確認向け

旧テンプレートの `03_work_log.md`（壁打ちセクション含む）は実施ワーカー向けの内容。計画ワーカー用は `l2-plan-worker.md` エージェント定義内の壁打ちフォーマットが正。

**結論**: phase-1 と phase-2 の `01_worker_plan.md` は壁打ちセクションの内容が異なる（前提条件チェック項目が異なる）。それ以外の 6 ファイル（`02_worker_log.md` ～ `07_issues.md`）はロール名の差異はあるが、テンプレート構造は共通で使える。

#### l1-manager/SKILL.md 整合確認ポイント

`l1-manager/SKILL.md` の関連ファイル一覧（行413-416）で旧パスが参照されている:
- `sessions/initiatives/_template/` → そのまま有効（ディレクトリパスは変わらない）
- `sessions/initiatives/_template/04_dispatch_log.md` → 新番号体系で正しい（旧 `02b_dispatch_log.md` → 新 `04_dispatch_log.md`）
- `sessions/initiatives/_template/06_cost_record.md` → 新番号体系で正しい（旧 `09_cost_record.md` → 新 `06_cost_record.md`）
- `sessions/initiatives/_template/00_wallbash_log.md` → 新番号体系で正しい（旧 `00a_wallbash_log.md` → 新 `00_wallbash_log.md`）

**結論**: l1-manager/SKILL.md の関連ファイル一覧は既に新番号体系のパスで記載されている。テンプレートの実ファイル名が新番号体系に合えば整合する。ただし、新施策の開始手順（行81-84）でコピー後の初期化対象ファイル名が新番号体系と合っているか確認が必要。

確認事項なし：計画開始
