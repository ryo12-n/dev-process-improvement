# タスクリスト: ai-dev-chain-gen-req

## 凡例
- ステータス: ⬜ 未着手 / 🔄 進行中 / ✅ 完了 / ⛔ ブロック
- 優先度: 🔴 高 / 🟡 中 / 🔵 低

## 参照ドメインエージェント

| エージェント名 | パス | 参照理由 | 対象 |
|-------------|------|---------|------|
| なし | - | 汎用 l2-worker で対応可能 | Worker |
| なし | - | 汎用 l2-evaluator で対応可能 | Evaluator |

## ディスパッチ計画

| Worker | 担当タスク | 特記事項 |
|--------|----------|---------|
| L2-worker (set-1) | T-001〜T-005 | 逐次実行（T-001→T-002→T-003→T-004→T-005） |
| L2-evaluator (set-2) | T-E01〜T-E02 | Worker 全完了後に評価 |

## Worker Set Assignment

| Set | Worker | Evaluator | 担当タスク | Wave |
|-----|--------|-----------|----------|------|
| Set-1 | L2-worker | - | T-001〜T-005 | Wave 1 |
| Set-2 | - | L2-evaluator | T-E01〜T-E02 | Wave 2 |

## Set Dispatch Order

| 順序 | Set | 方式 | 前提条件 | 備考 |
|------|-----|------|---------|------|
| 1 | Set-1 | 逐次 | なし | T-001（S）が小さいため並列不要 |
| 2 | Set-2 | 逐次 | Set-1 完了 | 評価フェーズ |

> **方式**: 逐次（1ワーカーずつ） / 並列（Wave 方式、`.claude/rules/parallel-dev.md` 参照）

## 実施タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-001 | テスト用プロジェクト `projects/test-gen-req/` を作成する。`projects/_template/` をコピーし、`request.md` に具体的なサンプル要望書（REST API で書籍管理等の具体的な題材）を記述する | `projects/test-gen-req/` が `_template/` と同一構造で存在し、`request.md` の 8 セクション全てに具体的な内容が記述されている | 🔴 | ⬜ |
| T-002 | `.claude/skills/gen-req/SKILL.md` の処理フロー（プロンプト）を実装する。TODO 5項目を全て解消する: (1) 要望書→要件抽出のプロンプト設計 (2) `requirements.json` スキーマ定義 (3) `requirements.md` テンプレート定義 (4) バリデーション（`request.md` 不在時エラー） (5) 既存ファイル上書き確認。`projects/_template/artifacts/requirements.json` と `requirements.md` もプロンプト実装と整合する構造に更新する。overview.md の入出力仕様との整合を確認する | SKILL.md に TODO が残っていない。処理フローが実行可能なプロンプトとして実装されている。`_template/artifacts/` がプロンプトと整合。overview.md の入出力仕様と整合している | 🔴 | ⬜ |
| T-003 | サンプル要望書での動作テスト。`/gen-req projects/test-gen-req` の処理フローに従って手動実行し、`requirements.json` / `requirements.md` を生成する。生成結果のスキーマ準拠・内容整合を確認する | 生成された `requirements.json` がスキーマ準拠の有効な JSON。`requirements.md` が人間可読。JSON と MD の内容が一致。`request.md` の全セクション情報が適切に要件に変換されている | 🔴 | ⬜ |
| T-004 | 作業中に発見した知見を `phase-2-execution/set-1/03_worker_report.md` の「作業中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-005 | `phase-2-execution/set-1/07_issues.md` の未転記課題を確認し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` に作成する（CSV は自動生成）。転記時は `issues/_template.md` をコピーして作成し課題詳細を記載する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

## 評価タスク

| ID | タスク | 完了条件 | 優先度 | ステータス |
|----|--------|---------|--------|-----------|
| T-E01 | 評価中に発見した知見を `phase-2-execution/set-2/06_eval_report.md` の「評価中の知見」セクションに記録する。「ルール化候補」と「参考情報」に分類し、各テーブルに最低1行記載する（該当なしの場合は「なし — 理由: ○○」と記載） | 「ルール化候補」「参考情報」の両テーブルに最低1行の記載がある | 🔴 | ⬜ |
| T-E02 | 評価中に新たに発見した課題を `phase-2-execution/set-2/07_issues.md` へ起票し、施策をまたぐ課題を `issues/entries/ISS-XXX.md` に作成する | 全課題に `[転記済 ISS-XXX]` または「転記不要」の判断が付いている | 🔴 | ⬜ |

---
**作成者**: L1
**最終更新**: 2026-03-24
