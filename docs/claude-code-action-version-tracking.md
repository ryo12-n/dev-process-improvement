# Claude Code Action バージョン追跡手順

> **文書カテゴリ**: 運用ガイド

## 概要

GitHub Actions ワークフローで使用する `anthropics/claude-code-action` のバージョンを追跡・更新するための手順書。

## 現在のバージョン指定状況

| ワークフロー | バージョン指定 |
|------------|--------------|
| `initiative-wallbash.yml` | `anthropics/claude-code-action@v1` |
| `initiative-execute.yml` | `anthropics/claude-code-action@v1` |
| `initiative-close.yml` | `anthropics/claude-code-action@v1` |
| `initiative-question.yml` | `anthropics/claude-code-action@v1` |
| `test-permissions.yml` | `anthropics/claude-code-action@v1` |
| `test-skill-reading.yml` | `anthropics/claude-code-action@v1` |

すべて `@v1` メジャーバージョンタグで指定されており、マイナー・パッチバージョンの更新は自動的に適用される。

## バージョン確認方法

### 1. 最新リリースの確認

```bash
gh release list --repo anthropics/claude-code-action --limit 5
```

### 2. 現在使用中のバージョンの確認

```bash
grep -r "claude-code-action" .github/workflows/ | grep "uses:"
```

### 3. 変更履歴の確認

```bash
gh release view <バージョン> --repo anthropics/claude-code-action
```

## 更新手順

### メジャーバージョンタグ（`@v1`）使用時

メジャーバージョンタグを使用している場合、マイナー・パッチ更新は自動適用されるため通常は手動更新不要。

メジャーバージョンアップ（例: `v1` → `v2`）が発生した場合:

1. リリースノートで破壊的変更を確認する
2. 影響範囲を評価する（`.claude/skills/gha-guideline/SKILL.md` セクション5の権限設計を参照）
3. テストワークフロー（`test-permissions.yml`, `test-skill-reading.yml`）で動作確認する
4. 全ワークフローのバージョン指定を一括更新する

### 特定バージョン固定（`@v1.x.x`）への変更

セキュリティ要件やバグ回避のために特定バージョンに固定する場合:

1. 対象バージョンのコミット SHA を確認する
2. SHA 固定（`@<sha>`）での指定を推奨（タグの書き換えリスク回避）
3. 固定理由を PR 説明に記載する

## 確認観点

バージョン更新時に以下を確認する:

- [ ] `permissions` の要件変更がないか
- [ ] `allowed_tools` の仕様変更がないか
- [ ] `prompt` パラメータの仕様変更がないか
- [ ] 既存のスキルファイル Read 指示が正常に機能するか

## 定期確認の推奨

- オートメーションメンテナンスセッション（AT-003: 実装進捗確認）の一環として、四半期ごとにバージョンの最新状況を確認する

---

**作成日**: 2026-03-25
**起票元**: BL-060（Claude Code Action バージョン追従手順の制度化）
