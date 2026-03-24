# AI Dev Chain — プロジェクト全体計画書

> このファイルは `sessions/initiatives/` の各セッションを横断して参照される恒久計画書。
> セッションを跨いでも「何を作っているか・どこまで進んでいるか」を把握するための単一ソース。

---

## ビジョン

人間が要望書（`request.md`）を書くと、Claude Code の Skills チェーンが裏側でシステム開発を自動的に進める仕組みを `dev-process-improvement` 上に構築する。

```
request.md（要望書）
    ↓ /gen-req
requirements.json / requirements.md
    ↓ /gen-design
openapi.yaml / design.md
    ↓ /gen-tests
tests.json / tests.md
    ↓ /gen-ci
ci/pipeline.yaml（GitHub Actions）
    ↓ 人間レビュー＆承認
    ↓ /gen-tasks
tasks.json
    ↓ l1-impl-manager（既存 Skill）
実装コード / CI パス
```

---

## 対象スコープ

- **実装先リポジトリ**: `dev-process-improvement`
- **動作環境**: Claude Code CLI（`/スキル名` コマンドで呼び出し）
- **プロジェクト管理場所**: `projects/<project-name>/`
- **成果物の保存先**: 各プロジェクトディレクトリ内（`projects/<project-name>/artifacts/`）

---

## 追加する Skills 一覧

| Skill 名 | コマンド | 入力 | 出力 | 状態 |
|---------|---------|------|------|------|
| project-init | `/project-init <project-name>` | プロジェクト名 | `projects/<name>/` ディレクトリ一式 | 🔲 未着手 |
| gen-req | `/gen-req <project-path>` | `request.md` | `requirements.json` / `requirements.md` | 🔲 未着手 |
| gen-design | `/gen-design <project-path>` | `requirements.json` | `openapi.yaml` / `design.md` | 🔲 未着手 |
| gen-tests | `/gen-tests <project-path>` | `requirements.json` + `openapi.yaml` | `tests.json` / `tests.md` | 🔲 未着手 |
| gen-ci | `/gen-ci <project-path>` | `tests.json` | `ci/pipeline.yaml` | 🔲 未着手 |
| gen-tasks | `/gen-tasks <project-path>` | `openapi.yaml` + `tests.json` | `tasks.json` | 🔲 未着手 |

**引数なし呼び出し時の動作**: 全 Skill 共通で「対象プロジェクトのパスを教えてください（例: projects/my-api）」とユーザーに質問する。

---

## リポジトリ追加構成

```
dev-process-improvement/
│
├── refs/
│   └── ai-dev-chain/
│       └── overview.md          ← このファイル（恒久計画書）
│
├── .claude/
│   └── skills/
│       ├── project-init/SKILL.md
│       ├── gen-req/SKILL.md
│       ├── gen-design/SKILL.md
│       ├── gen-tests/SKILL.md
│       ├── gen-ci/SKILL.md
│       └── gen-tasks/SKILL.md
│
└── projects/
    ├── _template/               ← project-init がコピーする雛形
    │   ├── request.md
    │   ├── backlog.md
    │   └── artifacts/
    │       ├── requirements.json
    │       ├── requirements.md
    │       ├── openapi.yaml
    │       ├── design.md
    │       ├── tests.json
    │       ├── tests.md
    │       ├── tasks.json
    │       └── ci/pipeline.yaml
    │
    └── <project-name>/          ← _template からコピーして使用
        ├── request.md
        ├── backlog.md
        └── artifacts/
```

---

## マイルストーン

| # | 内容 | 対応 Initiative | 状態 |
|---|------|----------------|------|
| M1 | `projects/_template/` とディレクトリ骨格を作成 | ai-dev-chain-bootstrap | ✅ 完了 |
| M2 | `project-init` Skill 作成 | ai-dev-chain-bootstrap | ✅ 完了（骨格） |
| M3 | `gen-req` Skill 作成・動作確認 | ai-dev-chain-gen-req | 🔲 未着手 |
| M4 | `gen-design` Skill 作成・動作確認 | ai-dev-chain-gen-design | 🔲 未着手 |
| M5 | `gen-tests` Skill 作成・動作確認 | ai-dev-chain-gen-tests | 🔲 未着手 |
| M6 | `gen-ci` Skill 作成・動作確認 | ai-dev-chain-gen-ci | 🔲 未着手 |
| M7 | `gen-tasks` Skill 作成・動作確認 | ai-dev-chain-gen-tasks | 🔲 未着手 |
| M8 | サンプル要望書で E2E 通し確認 | ai-dev-chain-e2e | 🔲 未着手 |

---

## セッション再開時のチェックポイント

1. このファイル（`refs/ai-dev-chain/overview.md`）のマイルストーン状態を確認
2. 直近のイニシアティブ（`sessions/initiatives/ai-dev-chain-*/`）の `03_tasks.md` を確認
3. 次の未着手マイルストーンに対応するイニシアティブを開始（または継続）
