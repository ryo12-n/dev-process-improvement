# 課題バッファ: Phase 1（情報収集）

## 課題一覧

### ISS-TEMP-001: settings.json deny ルールの非機能性
- **発見フェーズ**: Phase 1
- **発見者**: config-collection-worker
- **重要度**: 高
- **内容**: v1.0.93 時点で settings.json の deny パーミッションが機能しないバグが報告されている（GitHub Issue #6699）。本プロジェクトでは `.claude/settings.json` に deny ルール（`Read(./.env)`, `Read(./secrets/**)` 等）を設定しているが、実際に機能していない可能性がある
- **影響**: セキュリティ上のリスク。センシティブファイルへのアクセスが deny ルールで防止されていない可能性
- **推奨対応**: Phase 2 の現状分析で deny ルールの実効性を検証し、必要に応じて PreToolUse hook（exit code 2）による代替ガード実装を Phase 3 で提案
- **CSV転記**: [未転記]

### ISS-TEMP-002: hooks イベント数の大幅増加（24イベント）
- **発見フェーズ**: Phase 1
- **発見者**: config-collection-worker
- **重要度**: 中
- **内容**: 従来のリファレンスでは hooks は4タイプ（SessionStart, PreToolUse, PostToolUse, Stop）として管理されていたが、公式ドキュメントでは24イベントに拡張されている。本プロジェクトは SessionStart のみ使用中
- **影響**: 活用されていない hook イベント（PostToolUse, Stop, ConfigChange, InstructionsLoaded 等）により、品質ゲートや自動化の改善余地がある
- **推奨対応**: Phase 2 で現在の hook 使用状況を分析し、Phase 3 で活用可能な新イベントの導入提案を行う
- **CSV転記**: [未転記]
