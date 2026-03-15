# metacognition-manager の記述構造統一

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-027 |
| **優先度** | 🔵 低 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-09 |

## 課題・背景

metacognition-manager には独立した「知見集約手順」「課題集約手順」セクションがなく、「結果の集約」に埋め込まれている。triage-manager では独立セクションとして定義されており、構造に不一致がある。manager-common-policy の参照置換方法も異なっている。

## 期待効果

- セッション間の構造一貫性向上
- manager-common-policy の参照パターン統一

## 実施案

- metacognition-manager SKILL.md に知見集約手順・課題集約手順の独立セクションを追加
- triage-manager のセクション構造に合わせる
