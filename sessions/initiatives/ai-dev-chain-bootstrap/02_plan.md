# 実施計画: AI Dev Chain Bootstrap

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| Phase A | `projects/_template/` とディレクトリ骨格作成 | `projects/_template/` 配下に全プレースホルダーが存在する |
| Phase B | 6 Skills の `SKILL.md` 骨格作成 | `/project-init` 〜 `/gen-tasks` が全て `/スキル名` で認識される |

## タスク一覧

### Phase A: ディレクトリ・テンプレート整備

- [ ] T-001: `projects/_template/request.md` 作成（要望書記入フォーマット）
- [ ] T-002: `projects/_template/backlog.md` 作成（AI 自動更新用進捗管理テンプレート）
- [ ] T-003: `projects/_template/artifacts/` 配下の各成果物プレースホルダー作成
  - `requirements.json` / `requirements.md`
  - `openapi.yaml` / `design.md`
  - `tests.json` / `tests.md`
  - `tasks.json`
  - `ci/pipeline.yaml`

### Phase B: Skills 骨格作成

- [ ] T-004: `.claude/skills/project-init/SKILL.md` 作成
  - `user-invocable: true`
  - 引数: `<project-name>`（なしの場合はユーザーへ質問）
  - 処理: `projects/_template/` を `projects/<project-name>/` にコピー
- [ ] T-005: `.claude/skills/gen-req/SKILL.md` 作成
  - `user-invocable: true`
  - 引数: `<project-path>`（なしの場合はユーザーへ質問）
  - 入出力仕様と TODO プレースホルダーを記載
- [ ] T-006: `.claude/skills/gen-design/SKILL.md` 作成（同上）
- [ ] T-007: `.claude/skills/gen-tests/SKILL.md` 作成（同上）
- [ ] T-008: `.claude/skills/gen-ci/SKILL.md` 作成（同上）
- [ ] T-009: `.claude/skills/gen-tasks/SKILL.md` 作成（同上）

## スケジュール

個人開発・非同期のため期間は設定しない。セッションごとに T-001 〜 T-009 を順次消化する。
次回セッション開始時は `refs/ai-dev-chain/overview.md` のマイルストーン状態を確認してから着手する。

## 成功基準（全体）

1. `projects/_template/` が存在し、全プレースホルダーファイルが揃っている
2. `.claude/skills/` 配下に 6 Skills の `SKILL.md` が存在し、`user-invocable: true` が設定されている
3. Claude Code で `/project-init test-project` を実行したとき、`projects/test-project/` が作成される

## リソース・前提条件

- 既存 Skills（`l1-manager` 等）の構造に準拠して作成する
- `refs/ai-dev-chain/overview.md` が配置済みであること（完了済み）

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| Skill 骨格のフロントマター記法が既存と異なる | 低 | 低 | `l1-manager/SKILL.md` のフロントマターを参照して合わせる |
| `projects/` と `sessions/` の用途が混同される | 低 | 低 | 両ディレクトリの README に用途を明記 |

---
**作成者**: L1
**作成日**: 2026-03-21
**最終更新**: 2026-03-21
