# 課題バッファ: Phase 2（現状分析）

## 課題一覧

### ISS-TEMP-003: セキュリティガードの単一障害点
- **発見フェーズ**: Phase 2
- **発見者**: config-analysis-worker
- **重要度**: 高
- **内容**: settings.json の deny ルール14件が v1.0.93 の既知バグにより非機能の可能性が高い（ISS-TEMP-001 で既報）。加えて、代替手段である PreToolUse hook も sandbox も未実装であり、セキュリティガードが一切機能していない単一障害点の状態にある
- **影響**: `.env*`, `secrets/**`, `*.pem`, `*.key` 等のセンシティブファイルへのアクセスが防止されていない。Bash 経由でのアクセスも deny ルールをバイパス可能（sandbox 未有効化のため）
- **推奨対応**: Phase 3 で PreToolUse hook による deny ルール代替ガードの実装提案 + sandbox 有効化の検討を行う。二重防御（hook + sandbox）が望ましい
- **CSV転記**: [未転記]

### ISS-TEMP-004: CLAUDE.md の公式推奨超過（192行 vs 50-100行推奨）
- **発見フェーズ**: Phase 2
- **発見者**: config-analysis-worker
- **重要度**: 中
- **内容**: CLAUDE.md が192行で、公式推奨の50-100行を大幅に超過している。import(@) 構文が未使用であり、rules/ への委譲も不十分。ドキュメント整合性ルール（42行）、セッション終了時の気づき記録（23行）、ディレクトリ構成詳細（15行）の計80行が分離候補として特定された
- **影響**: 長い CLAUDE.md は遵守率が低下する（公式ドキュメント記載）。毎セッションで192行分のコンテキストが消費される
- **推奨対応**: Phase 3 で import(@) 活用 + rules/ 委譲による分離提案を行う。目標は112行以下
- **CSV転記**: [未転記]

### ISS-TEMP-005: GHA スキル5件の disable-model-invocation 未設定
- **発見フェーズ**: Phase 2
- **発見者**: config-analysis-worker
- **重要度**: 中
- **内容**: GHA 専用スキル5件（gha-close, gha-execute, gha-wallbash, gha-question, gha-test）が `disable-model-invocation: true` 未設定のため、CLI セッションでも description がコンテキスト予算に読み込まれている。これらは GHA ワークフローからのみ使用されるスキルであり、CLI セッションでの自動起動は不要
- **影響**: 5件分の description トークン（~500トークン）が不要に消費される。また Claude が誤ってこれらのスキルを自動起動するリスクがある
- **推奨対応**: Phase 3 で GHA スキル5件に `disable-model-invocation: true` の設定を提案
- **CSV転記**: [未転記]
