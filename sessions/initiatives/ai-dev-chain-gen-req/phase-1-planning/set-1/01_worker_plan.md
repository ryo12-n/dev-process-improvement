# ワーカー計画: ai-dev-chain-gen-req — Set-1

## 壁打ちフェーズ [2026-03-24 12:00]

### 理解のサマリー
- タスクの目的: `gen-req/SKILL.md` の TODO を全て解消し、`/gen-req` が `request.md` から `requirements.json` / `requirements.md` を生成できる状態にする
- スコープ: SKILL.md のプロンプト実装、出力スキーマ確定、出力テンプレート確定、バリデーション、上書き確認ロジック、動作テスト用プロジェクト作成
- 完了条件: SKILL.md に TODO が残っていない、サンプル要望書に対して正常に生成される、overview.md の入出力仕様と整合

### 前提条件チェック
- [x] 施策計画（02_plan.md）の内容を理解: 理解済み
- [x] 提案書（01_proposal.md）の確認: 確認済み
- [x] 変更対象ファイル群の特定: 特定済み

### 不明点・確認事項
なし

### L1 確認結果
確認事項なし：計画開始

---

## 分析計画サマリ

### 調査済みファイル
1. `.claude/skills/gen-req/SKILL.md` — 現行の骨格。TODO 5項目が残存（プロンプト設計、スキーマ定義、テンプレート定義、バリデーション、上書き確認）
2. `projects/_template/artifacts/requirements.json` — プレースホルダー構造。`project`, `functional_requirements[]`, `non_functional_requirements[]`, `constraints`, `assumptions`, `out_of_scope` の6セクション
3. `projects/_template/artifacts/requirements.md` — 人間向けテンプレート。JSON と対応する6セクション構成
4. `projects/_template/request.md` — 要望書テンプレート。8セクション（概要、背景、ユーザーストーリー、機能要件、非機能要件、技術制約、スコープ外、成功基準）
5. `refs/ai-dev-chain/overview.md` — チェーン全体の入出力仕様。gen-req: `request.md` → `requirements.json` / `requirements.md`

### タスク分割方針
- SKILL.md の MODIFY が最大のタスク（プロンプト実装）。TODO 5項目を1タスクにまとめる（構造同一の Skills は1タスクにまとめる知見を適用。gen-req 単独だが、TODO 間の依存が強いため分離するメリットなし）
- テンプレートファイル（requirements.json / requirements.md）の微調整は SKILL.md 実装と密結合のため、同一タスクに含める
- テスト用プロジェクトの作成は独立タスクとして分離可能（SKILL.md 実装前でも骨格は作れる）
- 動作テストは SKILL.md 完成後に実施するため、別 Wave に分離
