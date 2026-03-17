# dev-process-improvement

開発プロセス改善サイクルを管理するディレクトリ。
**イニシアティブセッション**（施策の計画・実施・評価）と**トリアージセッション**（inbox・backlog の定期整理）の2種類のセッションで運用する。

## ディレクトリ構成

```
.
├── CLAUDE.md                            # 全セッション共通の Claude ルール
├── プロセス改善_課題管理.csv             # 全施策横断の課題管理（単一ソース・オブ・トゥルース）
│
├── .claude/rules/                       # 常時参照 Claude ルール
│   ├── commit-message.md               # コミットメッセージ規約
│   ├── gha-workflow-security.md        # GHA ワークフローセキュリティチェックリスト
│   ├── pr-url-output.md                # PR URL 出力規約
│   ├── parallel-dev.md                # 並列ディスパッチルール
│   ├── rebase-conflict-handling.md     # rebase コンフリクト時の対応フロー
│   └── session-start-branch-cleanup.md # セッション開始時ブランチ整理
│
├── .claude/skills/                      # セッション別スキル（起動型のみ記載）
│   ├── l1-manager/                      # L1（マネージャー）セッション
│   │   ├── SKILL.md
│   │   └── agents/ (l2-worker.md, l2-evaluator.md)
│   ├── triage-manager/                  # トリアージマネージャーセッション
│   │   ├── SKILL.md
│   │   └── agents/ (triage-worker.md, triage-evaluator.md)
│   ├── sync-manager/                    # リポジトリ間同期セッション
│   │   ├── SKILL.md
│   │   └── agents/ (sync-worker.md, sync-evaluator.md)
│   ├── metacognition-manager/           # メタ認知セッション
│   │   ├── SKILL.md
│   │   └── agents/ (metacognition-worker.md, metacognition-evaluator.md)
│   ├── backlog-maintenance-manager/     # バックログメンテナンスセッション
│   │   ├── SKILL.md
│   │   └── agents/ (bm-worker.md, bm-evaluator.md)
│   ├── l1-impl-manager/                  # コード実装専用4フェーズマネージャー
│   │   ├── SKILL.md
│   │   └── agents/ (investigation-worker.md, design-worker.md, impl-plan-worker.md, impl-worker.md, impl-evaluator.md)
│   ├── automation-manager/                # 自動化マネージャーセッション
│   │   ├── SKILL.md
│   │   └── agents/ (automation-worker.md, automation-evaluator.md)
│   ├── config-optimizer-manager/          # config最適化マネージャーセッション
│   │   ├── SKILL.md
│   │   └── agents/ (config-collection-worker.md, config-analysis-worker.md, config-proposal-worker.md, config-optimizer-evaluator.md)
│   ├── session-consistency-manager/       # セッション整合性マネージャーセッション
│   │   ├── SKILL.md
│   │   └── agents/ (sc-collection-worker.md, sc-analysis-worker.md, sc-proposal-worker.md, sc-evaluator.md)
│   ├── repo-sync-checklist/               # リポジトリ間同期チェックリスト
│   │   └── SKILL.md
│   └── fork-sync/                       # upstream/origin 双方向 git 同期
│       └── SKILL.md
│
├── sessions/
│   ├── initiatives/                     # 改善施策ごとのフォルダ
│   │   ├── _template/                   # ひな形（00〜08: proposal〜gate_review）
│   │   └── <施策名>/                    # 実施中・完了施策（_template と同構成）
│   ├── triage/                          # トリアージセッションの成果物
│   │   ├── _template/                   # ひな形（00〜04 + workers/_template/）
│   │   └── YYYYMMDD/
│   ├── sync/                            # リポジトリ間同期セッションの成果物
│   │   └── YYYYMMDD/
│   ├── metacognition/                   # メタ認知セッションの成果物
│   │   └── YYYYMMDD/
│   ├── backlog-maintenance/             # バックログメンテナンスセッションの成果物
│   │   └── YYYYMMDD/
│   ├── automation/                     # 自動化セッションの成果物
│   │   └── YYYYMMDD/
│   ├── config-optimization/            # config最適化セッションの成果物
│   │   └── YYYYMMDD/
│   ├── session-consistency/            # セッション整合性セッションの成果物
│   │   └── YYYYMMDD/
│   └── impl/                           # 実装セッションの成果物
│       └── <施策名>/
│
├── inbox/                               # 未処理アイテムの投入口
│   └── <ファイル名>.md
│
├── issues/                              # 課題詳細（CSV と対の 1 課題 1 ファイル形式）
│   ├── README.md                        # 課題管理の運用ガイド
│   ├── _template.md                     # 課題詳細テンプレート
│   └── entries/ISS-NNN.md              # 各課題の詳細ファイル
│
├── backlog/                             # 施策候補のストック
│   ├── README.md                        # バックログ運用ガイド
│   ├── backlog.csv                      # 施策候補一覧（CSV）
│   ├── _template.md                     # 施策候補テンプレート
│   └── entries/<施策名>.md             # 各施策候補の詳細
│
└── docs/                                # 運用ドキュメント（人間向け）
    ├── workflow.md                       # プロセス仕様書（.claude/skills/ の人間向け可視化）
    ├── implementation.md                 # 実装ノート・補足
    ├── management-system-guide.md        # 課題管理システムの運用手順
    ├── subagent-permission-guide.md      # サブエージェント権限の運用手順
    ├── coordination-protocol-guideline.md # 協調プロトコルガイドライン（参考資料）
    └── git-worktree-guideline.md         # git worktree ガイドライン（参考資料）
```

## セッション種別と起動方法

| 種別 | 目的 | 頻度 | 使用ルール | 成果物の場所 |
|------|------|------|-----------|------------|
| **イニシアティブ** | 施策の計画・実施・評価（L1→L2自動起動） | 施策ごと | `skills/l1-manager/` | `sessions/initiatives/<施策名>/` |
| **トリアージ** | inbox・backlog・CSV の定期整理 | 任意 | `skills/triage-manager/SKILL.md` | `sessions/triage/YYYYMMDD/` |
| **同期マネージャー** | リポジトリ間の構成・ルール・テンプレート同期 | 必要時 | `skills/sync-manager/SKILL.md` | `sessions/sync/YYYYMMDD/` |
| **メタ認知マネージャー** | 施策アーカイブの横断分析・振り返り | 任意 | `skills/metacognition-manager/SKILL.md` | `sessions/metacognition/YYYYMMDD/` |
| **バックログメンテナンス** | backlog エントリの陳腐化チェック・鮮度管理 | 任意 | `skills/backlog-maintenance-manager/SKILL.md` | `sessions/backlog-maintenance/YYYYMMDD/` |
| **実装マネージャー** | 外部リポジトリへのコード実装の4フェーズオーケストレーション | 施策ごと | `skills/l1-impl-manager/SKILL.md` | `sessions/initiatives/<施策名>/` |
| **自動化マネージャー** | 自動化候補の探索・再評価・進捗追跡 | 任意 | `skills/automation-manager/SKILL.md` | `sessions/automation/YYYYMMDD/` |
| **config最適化マネージャー** | .claude/ 配下の設定ファイル分析・最適化提案 | 任意 | `skills/config-optimizer-manager/SKILL.md` | `sessions/config-optimization/YYYYMMDD/` |
| **セッション整合性マネージャー** | セッション定義の整合性チェック・改善提案 | 任意 | `skills/session-consistency-manager/SKILL.md` | `sessions/session-consistency/YYYYMMDD/` |
| **同期チェックリスト** | リポジトリ間同期作業時のチェックリスト | 必要時 | `skills/repo-sync-checklist/SKILL.md` | - |
| **fork 同期** | upstream/origin の双方向 git 同期 | 必要時 | `skills/fork-sync/SKILL.md` | - |

各セッションはリポジトリルートで Claude Code を起動し、スラッシュコマンドで開始する。L2 ワーカー・評価者は L1/マネージャーがサブエージェントとして自律的に起動する。
詳細フローは [`docs/workflow.md`](docs/workflow.md) を参照。

### 1. イニシアティブセッション

```
/l1-manager
```

改善施策を L1（マネージャー）→ L2（実施）→ L2（評価）の3体制で進める。
起動後、バックログから新施策を開始するか、既存施策を継続するかを質問される。

### 2. トリアージセッション

```
/triage-manager
```

inbox・backlog・課題管理CSVを走査・整理する定期メンテナンスセッション。

### 3. 同期セッション

```
/sync-manager
```

リポジトリ間で構成・ルール・テンプレートを同期する。起動後、同期元・同期先を選択する。

### 4. メタ認知セッション

```
/metacognition-manager
```

施策アーカイブを横断分析し、反復パターン・未回収知見・プロセス効率を評価する振り返りセッション。

### 5. バックログメンテナンスセッション

```
/backlog-maintenance-manager
```

backlog エントリの陳腐化チェック・鮮度管理を行う定期メンテナンスセッション。

### 6. fork 同期

```
/fork-sync
```

upstream/origin の双方向 git 同期。対象リポジトリを選択し、ブランチ + PR 方式で fast-forward マージを行う。

## ドキュメントマップ

### 人間向けドキュメント

| ドキュメント | 役割 | 備考 |
|------------|------|------|
| **このREADME** | エントリーポイント。セッション起動方法・全体マップ | - |
| [`docs/workflow.md`](docs/workflow.md) | プロセス全体の仕様書（フロー図・ファイルオーナーシップ・課題管理フロー） | `.claude/skills/` の人間向け可視化。ルール変更時は合わせて更新する |
| [`docs/management-system-guide.md`](docs/management-system-guide.md) | 課題管理システムの運用手順 | 運用ガイド |
| [`docs/subagent-permission-guide.md`](docs/subagent-permission-guide.md) | サブエージェント権限の運用手順 | 運用ガイド |
| [`docs/implementation.md`](docs/implementation.md) | 実装ノート・補足 | 運用ガイド |
| [`docs/coordination-protocol-guideline.md`](docs/coordination-protocol-guideline.md) | 協調プロトコルのガイドライン | 参考資料（ドラフト）、一部統合済み |
| [`docs/git-worktree-guideline.md`](docs/git-worktree-guideline.md) | git worktree のガイドライン | 参考資料（ドラフト）、一部統合済み |

### AI 向けスキル・エージェント定義（Source of Truth）

各マネージャースキル（`SKILL.md`）と配下エージェント（`agents/`）が正の情報源。`docs/workflow.md` はその人間向け要約。定義を変更したら `workflow.md` も合わせて更新すること。

| スキルディレクトリ | 構成 | workflow.md との関係 |
|------------------|------|---------------------|
| [`.claude/skills/l1-manager/`](.claude/skills/l1-manager/) | SKILL.md + agents/ (l2-worker, l2-evaluator) | イニシアティブフロー |
| [`.claude/skills/triage-manager/`](.claude/skills/triage-manager/) | SKILL.md + agents/ (triage-worker, triage-evaluator) | トリアージフロー |
| [`.claude/skills/sync-manager/`](.claude/skills/sync-manager/) | SKILL.md + agents/ (sync-worker, sync-evaluator) | リポジトリ間同期フロー |
| [`.claude/skills/metacognition-manager/`](.claude/skills/metacognition-manager/) | SKILL.md + agents/ (metacognition-worker, metacognition-evaluator) | メタ認知フロー |
| [`.claude/skills/backlog-maintenance-manager/`](.claude/skills/backlog-maintenance-manager/) | SKILL.md + agents/ (bm-worker, bm-evaluator) | バックログメンテナンスフロー |
| [`.claude/skills/l1-impl-manager/`](.claude/skills/l1-impl-manager/) | SKILL.md + agents/ (investigation-worker, design-worker, impl-plan-worker, impl-worker, impl-evaluator) | 実装フロー |
| [`.claude/skills/automation-manager/`](.claude/skills/automation-manager/) | SKILL.md + agents/ (automation-worker, automation-evaluator) | 自動化フロー |
| [`.claude/skills/config-optimizer-manager/`](.claude/skills/config-optimizer-manager/) | SKILL.md + agents/ (config-collection-worker, config-analysis-worker, config-proposal-worker, config-optimizer-evaluator) | config最適化フロー |
| [`.claude/skills/session-consistency-manager/`](.claude/skills/session-consistency-manager/) | SKILL.md + agents/ (sc-collection-worker, sc-analysis-worker, sc-proposal-worker, sc-evaluator) | セッション整合性フロー |
| [`.claude/skills/repo-sync-checklist/`](.claude/skills/repo-sync-checklist/) | SKILL.md | - |
| [`.claude/skills/fork-sync/`](.claude/skills/fork-sync/) | SKILL.md | - |

### その他

| 知りたいこと | 参照先 | 読者 |
|------------|--------|------|
| 施策のひな形・各ファイルの書き方 | [`sessions/initiatives/_template/`](sessions/initiatives/_template/) | 人間 |
| トリアージのひな形・手順 | [`sessions/triage/_template/`](sessions/triage/_template/) | 人間 |
| 課題の一覧・ステータス | [`プロセス改善_課題管理.csv`](プロセス改善_課題管理.csv) | 人間 |
| 施策候補・バックログ | [`backlog/README.md`](backlog/README.md) | 人間 |

### 文書分類ポリシー

本ディレクトリではドキュメントの読者（人間 or Claude）を明確に区別している。

| 分類 | 配置先 | 説明 |
|------|--------|------|
| 人間用 | `docs/`, `README.md` | プロセス仕様の人間向け可視化（workflow.md 等） |
| Claude 常時参照 | `.claude/rules/` | 毎リクエストで自動読み込み。コミットメッセージ規約等 |
| Claude オンデマンド参照（スキル） | `.claude/skills/` | セッション起動時のみ読み込み。l1-manager, triage-manager 等 |
| Claude 独立コンテキスト（エージェント） | `.claude/skills/*/agents/` | サブエージェントとして独立コンテキストで動作。l2-worker, triage-worker 等 |

判断基準: 「毎回のリクエストで参照が必要か？」→ Yes なら `rules/`、セッション起動時のみなら `skills/`、独立コンテキストなら `agents/`。
