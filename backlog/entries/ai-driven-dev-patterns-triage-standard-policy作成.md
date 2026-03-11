# ai-driven-dev-patterns triage-standard-policy 作成

## メタ情報

| 項目 | 内容 |
|------|------|
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | ai-driven-dev-patterns |
| **起票日** | 2026-03-07 |

## 課題・背景

ai-driven-dev-patterns のトリアージプロセスに TG-008（セッションルール整合性チェック）を新設したが、チェック基準が triage-worker.md に直接埋め込まれている。dev-process-improvement 側では triage-standard-policy として独立したポリシーファイルに分離されており、以下の問題がある:

- チェック基準の変更時に triage-worker.md 全体を編集する必要がある
- ポリシーの再利用性が低い（他のスキル定義からの参照が困難）
- dev-process-improvement 側との構造的な対称性が崩れている

## 期待効果

- TG-008 のチェック基準をポリシーファイル（`.claude/skills/triage-standard-policy/SKILL.md` 等）として分離し、保守性・再利用性を向上させる
- dev-process-improvement 側の triage-standard-policy と構造的に対称になり、リポジトリ間の知見移植が容易になる

## 補足・参考情報

- 参照元: dev-process-improvement の `.claude/skills/triage-standard-policy/SKILL.md`
- 関連施策: `sessions/initiatives/_archive/triage-process-brushup/`（本施策で TG-008 を新設し、基準を一旦 triage-worker.md に埋め込んだ）
