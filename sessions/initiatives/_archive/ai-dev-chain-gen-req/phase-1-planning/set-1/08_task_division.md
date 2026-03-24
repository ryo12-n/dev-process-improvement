# File-Level Task Division: ai-dev-chain-gen-req

> このファイルは L2 計画ワーカー（l2-plan-worker）が作成する。
> L1 マネージャーはこの成果物を参考に `03_tasks.md` を作成する。

## Parallelism Analysis

- Maximum parallel workers: 2
- Dependency graph: T-001（テスト用プロジェクト作成）は独立。T-002（SKILL.md 実装 + テンプレート確定）も独立。T-003（動作テスト）は T-001, T-002 の両方に依存。

```
T-001 (テスト用PJ作成) ──┐
                          ├──→ T-003 (動作テスト)
T-002 (SKILL.md 実装)  ──┘
```

## Task Assignments

### T-001: テスト用プロジェクト作成（projects/test-gen-req/）
- **Assigned files (CREATE)**:
  - `projects/test-gen-req/request.md` — サンプル要望書（具体的な API プロジェクトを題材）
  - `projects/test-gen-req/backlog.md` — テンプレートからコピー
  - `projects/test-gen-req/artifacts/requirements.json` — テンプレートからコピー（生成前のプレースホルダー）
  - `projects/test-gen-req/artifacts/requirements.md` — テンプレートからコピー（生成前のプレースホルダー）
- **Assigned files (MODIFY)**: なし
- **Read-only dependencies**:
  - `projects/_template/` — コピー元テンプレート
  - `projects/_template/request.md` — request.md のセクション構成参照
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - `projects/test-gen-req/` ディレクトリが `_template/` と同一構造で存在する
  - `request.md` に具体的な要望内容が記述されている（プレースホルダーではない）
  - 要望書の 8 セクション（概要、背景、ユーザーストーリー、機能要件、非機能要件、技術制約、スコープ外、成功基準）が全て埋められている
- **Estimated complexity**: S
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-002: gen-req SKILL.md プロンプト実装 + 出力テンプレート確定
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**:
  - `.claude/skills/gen-req/SKILL.md` — 処理フロー（プロンプト）の実装。TODO 5項目を全て解消。セクション: 「処理フロー」「TODO」
    - 要望書→要件抽出のプロンプト設計・実装
    - `requirements.json` スキーマ定義（処理フロー内に明記）
    - `requirements.md` テンプレート定義（処理フロー内に明記）
    - バリデーション（`request.md` 不在時のエラーハンドリング）
    - 既存 `requirements.json` がある場合の上書き確認ロジック
  - `projects/_template/artifacts/requirements.json` — スキーマ微調整（プロンプト実装で確定した構造を反映）
  - `projects/_template/artifacts/requirements.md` — テンプレート微調整（プロンプト実装で確定した構造を反映）
- **Read-only dependencies**:
  - `refs/ai-dev-chain/overview.md` — 入出力仕様の整合確認
  - `projects/_template/request.md` — 入力ファイル構造の参照
  - `projects/_template/artifacts/requirements.json` — 現行プレースホルダー構造の参照
  - `projects/_template/artifacts/requirements.md` — 現行テンプレート構造の参照
- **Prerequisite tasks**: None
- **Acceptance criteria**:
  - SKILL.md に TODO が残っていない
  - 処理フローが具体的なプロンプト指示として実装されている（枠組みだけでなく実行可能な内容）
  - バリデーション: `request.md` 不在時にエラーメッセージを返す処理が定義されている
  - 上書き確認: 既存 `requirements.json` がある場合にユーザー確認を行う処理が定義されている
  - `requirements.json` のスキーマが処理フロー内に明記されている
  - `requirements.md` のテンプレートが処理フロー内に明記されている
  - overview.md の入出力仕様（入力: `request.md` → 出力: `requirements.json` / `requirements.md`）と整合している
  - テンプレートファイル（`_template/artifacts/`）がプロンプト実装と整合する構造に更新されている
- **Estimated complexity**: L
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

### T-003: サンプル要望書での動作テスト
- **Assigned files (CREATE)**: なし
- **Assigned files (MODIFY)**:
  - `projects/test-gen-req/artifacts/requirements.json` — gen-req 実行結果で上書き
  - `projects/test-gen-req/artifacts/requirements.md` — gen-req 実行結果で上書き
- **Read-only dependencies**:
  - `.claude/skills/gen-req/SKILL.md` — 実装済みの処理フロー
  - `projects/test-gen-req/request.md` — テスト入力
  - `refs/ai-dev-chain/overview.md` — 入出力仕様の照合
  - `projects/_template/artifacts/requirements.json` — スキーマ準拠の検証
- **Prerequisite tasks**: T-001, T-002
- **Acceptance criteria**:
  - `/gen-req projects/test-gen-req` を実行し、エラーなく完了する
  - 生成された `requirements.json` が出力スキーマに準拠した有効な JSON である
  - 生成された `requirements.md` が人間可読な要件定義ドキュメントである
  - JSON と MD の内容が一致している（同じ要件が両方に反映されている）
  - `request.md` の全セクション（概要、背景、ユーザーストーリー、機能要件、非機能要件、技術制約、スコープ外、成功基準）の情報が適切に要件に変換されている
- **Estimated complexity**: M
- **Recommended domain agent (Worker)**: なし
- **Recommended domain agent (Evaluator)**: なし

## Conflict Check Matrix

| File | T-001 | T-002 | T-003 |
|------|:-----:|:-----:|:-----:|
| `.claude/skills/gen-req/SKILL.md` | - | MODIFY | READ |
| `projects/_template/artifacts/requirements.json` | READ | MODIFY | READ |
| `projects/_template/artifacts/requirements.md` | READ | MODIFY | READ |
| `projects/_template/request.md` | READ | READ | - |
| `projects/test-gen-req/request.md` | CREATE | - | READ |
| `projects/test-gen-req/backlog.md` | CREATE | - | - |
| `projects/test-gen-req/artifacts/requirements.json` | CREATE | - | MODIFY |
| `projects/test-gen-req/artifacts/requirements.md` | CREATE | - | MODIFY |
| `refs/ai-dev-chain/overview.md` | - | READ | READ |

**凡例**: CREATE = 新規作成, MODIFY = 変更, READ = 読取のみ, `-` = 無関係

**競合検出**: `projects/test-gen-req/artifacts/requirements.json` と `requirements.md` に対して T-001（CREATE）と T-003（MODIFY）が競合するが、T-003 は T-001 に依存し別 Wave に分離されるため問題なし。その他の競合なし。

## Wave Assignment

### Wave 1 (並列実行可)
- T-001（テスト用プロジェクト作成）
- T-002（SKILL.md プロンプト実装 + テンプレート確定）

### Wave 2 (Wave 1 完了後)
- T-003（動作テスト）— depends on T-001, T-002

## Domain Agent Recommendations

| エージェント名 | パス | 推奨理由 | 対象 |
|-------------|------|---------|------|
| なし | - | gen-req 固有のドメインエージェントは不要。汎用 l2-worker / l2-evaluator で対応可能 | Worker |
| なし | - | 同上 | Evaluator |

## Summary

- Total tasks: 3
- Total waves: 2
- Estimated max parallelism: 2 workers（Wave 1 で T-001, T-002 を並列実行）
- Conflict count: 0（Wave 間分離で解消済み）

---
**作成者**: L2 計画ワーカー
**作成日**: 2026-03-24
