# ワーカータスク指示: Set-1

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-001 | inbox | 全24件を「backlog候補 / ルール反映 / 却下 / 対応不要」に分類する。meta_* 6件は改善提案としての具体性を評価する。backlog との重複もチェックする | 全件に分類が付いている |
| TG-INT | ルール・整合性 | (1) .claude/skills/*/SKILL.md・agents/*.md と docs/workflow.md の整合性確認 (2) README.md の4セクション整合性（ディレクトリ構成図・セッション種別テーブル・AI向けスキル定義テーブル・ドキュメントマップ） (3) 参考資料（ドラフト）ステータスチェック（CLAUDE.md の docs/ 文書分類テーブル参照） (4) refs/ 孤立エントリ確認 | チェック結果がスキャンレポートに記録されている |

## 走査時の注意事項

- inbox の ref_* 4件（ref_ai-driven-development-poc, ref_ai-functions, ref_openspec-official-summary, ref_個人PCローカル環境構築-手順書）は refs/ に本体があるポインターメモ。分類判断時に refs/ の内容も確認すること
- inbox の meta_* 6件はメタ認知セッション 20260311 からの気づき。ISS-052〜055 と重複する可能性があるためCSV課題との関連も確認すること
- sync-worker同期先コミット漏れ防止.md が inbox と backlog entries 両方に存在する。重複をレポートすること
- builtin-skills-reference SKILL.md が新規追加されている（user-invocable: false）。docs/workflow.md への反映要否を確認すること
- TG-009: 走査結果に削除・統合候補が含まれる場合は情報欠損リスク評価を実施すること

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-12
