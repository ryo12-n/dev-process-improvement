# 改善施策提案: CLI環境での権限継承の再検証

## 背景・課題

前施策 `subagent-permission-model` で Claude Agent SDK 環境での allow/deny リスト・tools フィールドの動作検証を実施し、以下が判明した:
- SDK 環境では `.claude/settings.json` の deny リストが機能しない（ISS-045）
- SDK 環境では エージェント定義の `tools` フィールドによるツール制限が機能しない（ISS-046）

しかし、**CLI 環境（対話型セッション・Task ツール経由）での実機検証は未実施**であり、公式ドキュメントに基づく「期待動作」と実際の動作が一致するかは未確認。

現在の `docs/subagent-permission-guide.md` の適用範囲テーブルでは CLI 環境について「有効」「継承・有効（公式ドキュメントに基づく）」と記載しているが、実機検証に裏付けされていない。

## 目標

1. CLI 環境での deny リスト・allow リスト・tools フィールドの実際の動作を検証する
2. 検証結果に基づき `docs/subagent-permission-guide.md` を更新する
3. 検証結果に基づき `.claude/settings.json` の allow/deny 設定を最適化する

## スコープ
### やること
- CLI 対話型セッションでの deny/allow リスト動作検証
- Task ツール（サブエージェント）経由での deny/allow リスト継承検証
- Task ツール経由でのエージェント定義 tools フィールドの制限検証
- `docs/subagent-permission-guide.md` の更新（検証結果の反映）
- `.claude/settings.json` の最適化（検証結果に基づく設定見直し）

### やらないこと
- Claude Agent SDK 環境の再検証（前施策で完了済み）
- Hooks による権限制御の検証（別施策のスコープ）
- bypassPermissions モードの検証

## 期待される効果
- SDK/CLI 環境差の正確な理解と運用ガイドの精緻化
- deny リスト・tools フィールドの適用範囲の実機検証による裏付け
- settings.json の設定が実環境で意図通り機能している確信

## リスク
| リスク | 影響度 | 対策 |
|--------|--------|------|
| deny リストが CLI でも機能しない場合 | 中 | 代替の安全策（Hooks 等）を次施策として起票 |
| 検証中に破壊的操作が実行される可能性 | 低 | 安全なテストコマンドのみ使用（`echo` 等で代替） |

## 壁打ちの背景

- 検証環境は CLI 対話型 + Task ツール経由の2パターンとする（SDK 環境は前施策で検証済みのため除外）
- 検証項目は deny リスト・allow リスト・tools フィールドの3項目すべてを対象とする
- 成果物は既存の `docs/subagent-permission-guide.md` に CLI 環境のセクションを追記する形式とする
- 加えて、得られた知見から `.claude/settings.json` 等の Claude 公式標準資料に反映し、適切に権限管理できるようにする

## 備考・設計パターン

前施策 `subagent-permission-model` の検証手法（T-001〜T-003）を参考にする。ただし SDK 環境とは異なり、CLI 環境では許可プロンプトの表示有無が観測ポイントとなるため、検証手順は CLI 環境に合わせて設計する。

---
**起票者**: L1
**起票日**: 2026-03-08
**ステータス**: 承認済
