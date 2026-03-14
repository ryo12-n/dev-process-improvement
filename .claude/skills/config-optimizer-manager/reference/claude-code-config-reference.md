# Claude Code Configuration Reference

> **Snapshot Date**: 未収集（初回セッション実行時に更新予定）
> **Source**: Claude Code official documentation
> **Freshness**: 初回収集時に更新。以降はセッション実行ごとに確認。

---

## 1. settings.json Schema

### Supported Fields

| Field | Type | Description | Default |
|-------|------|-------------|---------|
| <!-- Phase 1 collection-worker が収集・記入する --> | | | |

### Hook Configuration

<!-- settings.json 内の hooks フィールドの構造 -->

---

## 2. Rules (.claude/rules/)

### Rule File Format

<!-- ルールファイルのフォーマット・読み込み動作 -->

### Path-Scoped Rules

<!-- パススコープルールの記法と動作 -->

### Best Practices

<!-- 公式ドキュメントのベストプラクティス -->

---

## 3. Skills (.claude/skills/)

### SKILL.md Format

<!-- YAML フロントマター・description の最適化 -->

### Context Budget

<!-- スキル数とコンテキスト使用率の関係 -->

### Agents

<!-- エージェント定義フォーマット・tools フィールド -->

---

## 4. Hooks

### Hook Types

| Type | Trigger | Use Cases |
|------|---------|-----------|
| SessionStart | セッション開始/再開 | <!-- 収集時に記入 --> |
| PreToolUse | ツール実行前 | |
| PostToolUse | ツール実行後 | |
| Stop | セッション終了 | |

### Hook Configuration Schema

<!-- matcher, type, command, timeout -->

---

## 5. CLAUDE.md

### Structure Best Practices

<!-- import 構文・サイズガイドライン・読み込み順 -->

---

## 6. Plugins

### Plugin System

<!-- プラグインシステム・インストール・開発 -->

---

## 7. Additional Configuration

### settings.local.json

<!-- 用途・優先度 -->

### Memory

<!-- .claude/memory.md -->

### Sandbox

<!-- sandbox 設定オプション -->

### Environment Variables

<!-- 環境変数活用 -->

---

## Changelog

<!-- Phase 1 collection-worker がスナップショット更新時に追記する -->
<!--
### YYYY-MM-DD
- 初回収集
- 変更点: ...
-->
