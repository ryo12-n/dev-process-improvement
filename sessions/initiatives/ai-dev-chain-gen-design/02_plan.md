# 実施計画: ai-dev-chain-gen-design

## フェーズ構成

| フェーズ | 内容 | 成功基準 |
|---------|------|----------|
| 1 | SKILL.md のプロンプト実装（処理フロー・OpenAPI 生成ガイド・design.md テンプレート・バリデーション） | SKILL.md の TODO が全て解消され、完全な処理フローが記載されている |
| 2 | サンプルデータ（BookShelf API）での動作テスト・評価 | サンプル requirements.json に対して `/gen-design` が `openapi.yaml` / `design.md` を正常に生成する |

## 成功基準（全体）

1. `gen-design/SKILL.md` に完全な処理フロー（プロンプト）が実装されており、TODO が残っていない
2. `/gen-design projects/test-gen-req` を実行した結果、`openapi.yaml` が OpenAPI 3.0.3 準拠の有効な YAML として生成される
3. `/gen-design projects/test-gen-req` を実行した結果、`design.md` が人間可読な設計ドキュメントとして生成される
4. `openapi.yaml` の paths/components が `requirements.json` の FR/NFR と対応していること（トレーサビリティ）
5. overview.md の入出力仕様（入力: `requirements.json` → 出力: `openapi.yaml` / `design.md`）と整合している

## 変更対象ファイル

| ファイル | 操作 | 説明 |
|---------|------|------|
| `.claude/skills/gen-design/SKILL.md` | MODIFY | 処理フロー（プロンプト）の実装 |
| `projects/_template/artifacts/openapi.yaml` | MODIFY | 生成ガイドとの整合確認（必要に応じて微調整） |
| `projects/_template/artifacts/design.md` | MODIFY | 生成テンプレートとの整合確認（必要に応じて微調整） |
| `projects/test-gen-req/artifacts/openapi.yaml` | MODIFY | 動作テストで生成結果を書き込み |
| `projects/test-gen-req/artifacts/design.md` | MODIFY | 動作テストで生成結果を書き込み |

## リソース・前提条件

- `gen-design/SKILL.md` の骨格が bootstrap 施策で作成済み
- `projects/_template/artifacts/` の全プレースホルダーが作成済み
- `projects/test-gen-req/artifacts/requirements.json` が gen-req 施策で生成済み（BookShelf API: FR 7件、NFR 4件）
- `refs/ai-dev-chain/overview.md` に入出力仕様が定義済み
- gen-req の 7 ステップパターンを踏襲（再現性検証を兼ねる）

## リスクと対策

| リスク | 発生確率 | 影響 | 対策 |
|--------|---------|------|------|
| FR から API エンドポイントへの対応付けが不正確 | 中 | 中 | acceptance_criteria をエンドポイント導出の根拠として活用し、トレーサビリティを確保 |
| 要件の抽象度が高い場合に設計の具体性がばらつく | 中 | 中 | constraints をアーキテクチャ決定の根拠として明示的に活用する |
| OpenAPI スキーマが後工程 gen-tests の入力として不十分 | 低 | 中 | OpenAPI 3.0.3 標準に準拠し、request/response schema を明示する |

---
**作成者**: L1
**作成日**: 2026-03-24
**最終更新**: 2026-03-24
