# ワーカータスク指示: Set-7

## 割り当てTGタスク

| タスクID | 対象 | やること | 完了条件 |
|---------|------|---------|---------|
| TG-010 | GHA/Skills | `.github/gha-skills-mapping.yml` のマッピングマニフェストに基づき、GHA プロンプト/ワークフローとスキル定義の間のドリフトを検出する。未マッピングワークフローのギャップも報告する | 全マッピングのチェック完了、ドリフト重大度判定済み |

## 走査時の注意事項

- **マニフェスト**: `.github/gha-skills-mapping.yml` を読み、定義された全マッピングを確認すること
- **現在のマッピング**: 2件（triage-gha, l1-auto-execute-gha）
- **未マッピングワークフロー**: `.github/workflows/` に8ファイルあるが2件のみマッピング定義あり。残り6件を「ギャップ」として報告すること
- **チェックポイント**: task_ids, workflow_steps, report_sections, file_templates, file_numbers の各項目を突合
- **inherent_differences**: 宣言済みの期待差異がまだ有効かを検証
- **ドリフト重大度**: CRITICAL（機能欠落）/ WARNING（構造不一致）/ INFO（軽微差異）
- **TG-006/TG-008 からの情報**: set-4 で manager-common-policy の適用対象不整合が検出済み。triage-manager SKILL.md 自体は問題なしだが、GHA プロンプトとの突合で差異がないか注意
- triage-worker.md の TG-010 走査手順セクションに従って実施すること

---
**作成者**: トリアージマネージャー
**作成日**: 2026-03-15
