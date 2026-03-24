# 改善施策提案: ai-dev-chain-gen-req

## 背景・課題

ai-dev-chain-bootstrap 施策（M1・M2）で、6 Skills の骨格と `projects/_template/` が作成済み。`gen-req` Skill は SKILL.md に処理フローの枠組みと TODO リストがあるが、実際のプロンプト実装がなく、`/gen-req` を実行しても要件定義ファイルは生成されない。

overview.md のマイルストーン M3 として `gen-req` Skill の中身実装が次のステップとして定義されている。

## 目標

- `/gen-req projects/<name>` コマンドで `request.md` から `requirements.json` / `requirements.md` を実際に生成できる状態にする
- サンプル要望書を使った動作テストで正常に生成されることを確認する
- overview.md の入出力仕様と整合した実装であることを確認する

## スコープ
### やること
- `gen-req/SKILL.md` の処理フロー（プロンプト）を実装する
- `requirements.json` の出力スキーマを確定する（現行プレースホルダー構造をベース）
- `requirements.md` の出力テンプレートを確定する
- バリデーション（`request.md` 不在時のエラーハンドリング）を実装する
- 既存 `requirements.json` がある場合の上書き確認ロジックを実装する
- サンプル要望書を作成し、動作テストを実施する

### やらないこと
- 他の gen-* Skills（gen-design / gen-tests / gen-ci / gen-tasks）の実装
- E2E チェーン全体の通し確認（M8）
- `projects/_template/` の構造変更（bootstrap で確定済み）

## 外部リポジトリ

| リポジトリ名 | ローカルパス | 変更内容の概要 |
|-------------|------------|-------------|
| なし | - | - |

## 期待される効果

- `/gen-req` コマンド1つで要望書から構造化された要件定義が生成され、手動での要件整理作業が不要になる
- 後工程（`/gen-design`）への入力が標準フォーマットで供給されるようになる

## リスク

| リスク | 影響度 | 対策 |
|--------|--------|------|
| 要望書の記述品質によって生成結果の品質がばらつく | 中 | プロンプトに構造化ガイドラインを含め、不足情報はユーザーに確認する |
| requirements.json のスキーマ変更が後工程に影響する | 低 | 現行プレースホルダー構造をベースとし、大幅な変更は避ける |

## 壁打ちの背景

- `requirements.json` のスキーマは現行プレースホルダー構造（案A: `project`, `functional_requirements[]`, `non_functional_requirements[]`, `constraints`, `assumptions`, `out_of_scope`）をベースとする。bootstrap で合意済みの構造であり、後工程 `/gen-design` の入力仕様に影響するため大幅変更は避ける
- 動作テスト込みで完了とする（サンプル要望書での実行確認まで）
- SDK 環境のため `claude/l1-manager-KXKFi` ブランチを施策ブランチとして使用
- 前施策の知見: チェーン型 Skill の完了条件に overview.md との入出力照合を含めるべき → タスク完了条件に反映

## 備考・設計パターン

チェーン型 Skill の初実装であるため、ここで確立したプロンプト設計パターン（入力読み取り → 分析 → JSON 生成 → MD 生成 → レポート）は後続の gen-design 以降の参考になる。

---
**起票者**: L1
**起票日**: 2026-03-24
**ステータス**: 実施中
**backlog元ファイル**: なし
