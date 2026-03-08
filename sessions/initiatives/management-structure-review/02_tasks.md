# タスクリスト: management-structure-review

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## フェーズ1: ディレクトリ構造変更

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | `backlog/entries/` を作成し、38個の施策 `.md` ファイルを `git mv` で移動する。対象: `backlog/` 直下の `.md` ファイルのうち `README.md` と `_template.md` を除く全ファイル | `ls backlog/` で CSV・README・_template・entries/ のみ表示。`ls backlog/entries/` で38ファイル表示 | 🔴 | ⬜ |
| T-002 | `issues/entries/` を作成し、3個の ISS ファイル（ISS-042.md, ISS-045.md, ISS-046.md）を `git mv` で移動する | `ls issues/` で README・_template・entries/ のみ表示。`ls issues/entries/` で3ファイル表示 | 🔴 | ⬜ |
| T-003 | `backlog/README.md` と `issues/README.md` を更新し、entries/ サブディレクトリの構造・運用ルールを記載する | 両 README に entries/ の説明が記載されている | 🟡 | ⬜ |
| T-004 | `プロセス改善_課題管理.csv` の `詳細ファイル` 列を更新する（`issues/ISS-XXX.md` → `issues/entries/ISS-XXX.md`）。更新後に CSV の行数・列数が変更前と一致することを検証する | 3行の詳細ファイルパスが更新済み。行数・列数が変更前後で一致 | 🔴 | ⬜ |

## フェーズ2: スキル・エージェント定義の更新

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-005 | `.claude/skills/l1-manager/SKILL.md` のパス参照を更新する。対象箇所: `backlog/<施策名>.md` → `backlog/entries/<施策名>.md`（L23-24, L223, L226）、`issues/ISS-XXX.md` → `issues/entries/ISS-XXX.md`（L106, L116） | 該当ファイル内で `backlog/` `issues/` を含むパス参照が全て `entries/` を経由している | 🔴 | ⬜ |
| T-006 | `.claude/skills/l1-manager/agents/l2-worker.md` のパス参照を更新する。対象: `issues/` 作成パス（L60）、`issues/_template.md` コピー先（L80-81） | コピー先が `issues/entries/ISS-XXX.md` になっている | 🔴 | ⬜ |
| T-007 | `.claude/skills/l1-manager/agents/l2-evaluator.md` のパス参照を更新する。対象: `issues/` 作成パス（L62）、`issues/_template.md` コピー先（L91-92） | コピー先が `issues/entries/ISS-XXX.md` になっている。l2-worker.md と対称であること | 🔴 | ⬜ |
| T-008 | `.claude/skills/metacognition-manager/SKILL.md` のパス参照を更新する。対象: `backlog/` への `.md` 作成パス（L40, L125, L142） | `backlog/entries/` 配下への作成が明記されている | 🟡 | ⬜ |
| T-009 | `.claude/skills/metacognition-manager/agents/metacognition-worker.md` のパス参照を更新する。対象: `backlog/` 参照（L76, L115） | `backlog/entries/*.md` の読み取りパスが更新されている | 🟡 | ⬜ |
| T-010 | `.claude/skills/triage-manager/SKILL.md` のパス参照を確認・更新する。対象: `backlog/ideas.md`（L135） — 特殊ファイルか entries/ 配下かを判断して対応する | パスが新構造と整合している | 🟡 | ⬜ |
| T-011 | `.claude/skills/triage-manager/agents/triage-worker.md` のパス参照を更新する。対象: `backlog/*.md`（L66） | `backlog/entries/*.md` に更新されている | 🟡 | ⬜ |

## フェーズ3: ドキュメント更新・環境分離方針

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-012 | `CLAUDE.md` のディレクトリ構成テーブルを更新し、`backlog/` と `issues/` に `entries/` サブディレクトリがある旨を記載する | CLAUDE.md の該当テーブルに entries/ の記載がある | 🟡 | ⬜ |
| T-013 | `docs/workflow.md` の backlog/issues 関連記述を確認し、必要箇所を更新する | ルール変更に伴う連動更新として docs/workflow.md が新構造を反映している | 🟡 | ⬜ |
| T-014 | 環境分離方針を策定する。`backlog.csv` の `対象リポジトリ` 列（dev-process-improvement / ai-driven-dev-patterns / 横断）の運用ガイドラインを CLAUDE.md に追記する。適用対象環境（CLI / SDK / 横断）を明記すること | CLAUDE.md に環境分離ポリシーセクションが追加されている | 🟡 | ⬜ |

## フェーズ4: 検証・整合性確認

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-015 | rule-change-checklist を適用し、パス参照の更新漏れを grep 走査で検出する。`grep -r "backlog/" .claude/skills/` で `entries/` を含まない参照がないことを確認。`issues/` も同様に確認 | grep 走査で更新漏れがゼロであること（_template.md 参照は除外可） | 🔴 | ⬜ |

## 固定タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-016 | 作業中に発見した知見を `04_work_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-017 | `07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `プロセス改善_課題管理.csv` へ転記する。転記時は `issues/_template.md` をコピーして `issues/entries/ISS-XXX.md` を作成し、課題詳細を記載する。CSV の `詳細ファイル` 列に `issues/entries/ISS-XXX.md` のパスを記入する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-08
