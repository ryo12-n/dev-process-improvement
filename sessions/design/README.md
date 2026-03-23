# sessions/design/

design-partner スキルの成果物置き場。曖昧なアイデアを対話で具体化し、設計成果物と backlog エントリを生成するプロセスの作業ディレクトリ。

## ディレクトリ構成

```
sessions/design/
├── README.md                          ← 本ファイル
└── <テーマ名>/                         ← テーマごとのサブディレクトリ
    ├── brainstorm_log.md              ← 壁打ちログ（EXPLORE フェーズの記録）
    ├── design.md                      ← 設計ドキュメント（DEFINE + DESIGN フェーズの記録）
    └── action_plan.md                 ← 実施計画（PLAN + REVIEW フェーズの記録）
```

## ファイル命名規約

| ファイル | 作成フェーズ | 内容 |
|---------|------------|------|
| `brainstorm_log.md` | EXPLORE | 目的発散・制約明確化・アイデア収束の対話記録。却下した選択肢も含む |
| `design.md` | DEFINE + DESIGN | WHY/WHAT/HOW 分解、スコープ境界（やること/やらないこと）、成功基準（KPI） |
| `action_plan.md` | PLAN + REVIEW | タスク分解、依存関係マッピング、backlog エントリへのポインター |

## テーマ名の命名規則

- 英語のケバブケース（例: `improve-triage-flow`, `add-cost-tracking`）
- 施策化された場合の `sessions/initiatives/` ディレクトリ名と一致させることを推奨

## 他ディレクトリとの関係

```
sessions/design/<テーマ名>/         ← 設計伴走の成果物（本ディレクトリ）
    ↓ backlog エントリ生成
backlog/entries/<施策名>.md         ← 施策候補（設計成果物へのポインター付き）
    ↓ L1 マネージャーが施策化
sessions/initiatives/<施策名>/      ← 施策の実行管理
```

## 注意事項

- design-partner スキルが自動的にテーマディレクトリとファイルを作成する
- 手動でファイルを作成・編集しても構わないが、上記の命名規約に従うこと
- 施策化後も設計成果物は削除せず、参照用として残す

---
**作成日**: 2026-03-20
**関連スキル**: `.claude/skills/design-partner/SKILL.md`
