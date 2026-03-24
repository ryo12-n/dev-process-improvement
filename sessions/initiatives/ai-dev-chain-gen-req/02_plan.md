# 実施計画: ai-dev-chain-gen-req

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | SKILL.md のプロンプト実装（処理フロー・スキーマ定義・バリデーション） | SKILL.md の TODO が全て解消され、完全な処理フローが記載されている |
| 2 | サンプル要望書作成・動作テスト | サンプル要望書に対して `/gen-req` が `requirements.json` / `requirements.md` を正常に生成する |

## 成功基準（全体）

1. `gen-req/SKILL.md` に完全な処理フロー（プロンプト）が実装されており、TODO が残っていない
2. `/gen-req projects/<test-project>` を実行した結果、`requirements.json` が出力スキーマに準拠した有効な JSON として生成される
3. `/gen-req projects/<test-project>` を実行した結果、`requirements.md` が人間可読な要件定義ドキュメントとして生成される
4. overview.md の入出力仕様（入力: `request.md` → 出力: `requirements.json` / `requirements.md`）と整合している

## 変更対象ファイル

| ファイル | 操作 | 説明 |
|---------|------|------|
| `.claude/skills/gen-req/SKILL.md` | MODIFY | 処理フロー（プロンプト）の実装 |
| `projects/_template/artifacts/requirements.json` | MODIFY | 出力スキーマの確定（現行構造ベースで微調整） |
| `projects/_template/artifacts/requirements.md` | MODIFY | 出力テンプレートの確定 |
| `projects/test-gen-req/` | CREATE | 動作テスト用プロジェクト（サンプル要望書含む） |

## リソース・前提条件

- `gen-req/SKILL.md` の骨格が bootstrap 施策で作成済み
- `projects/_template/` の全プレースホルダーが作成済み
- `refs/ai-dev-chain/overview.md` に入出力仕様が定義済み

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| プロンプトの品質により要件抽出の精度がばらつく | 中 | 中 | 構造化ガイドラインを明示し、不足情報はユーザー確認のフローを含める |
| テンプレート変更が後工程 gen-design に影響 | 低 | 中 | 現行プレースホルダー構造をベースとし、フィールド追加は最小限に留める |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
