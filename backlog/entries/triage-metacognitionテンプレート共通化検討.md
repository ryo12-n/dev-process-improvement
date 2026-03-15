# triage/metacognition テンプレート共通化検討

> **バックログ ID**: BL-048


## メタ情報
| 項目 | 内容 |
|------|------|
| **対象リポジトリ** | dev-process-improvement |
| **起票日** | 2026-03-08 |
| **発生元** | metacognitive-improvement-enforcement 施策 (08_gate_review.md 次施策候補) |

## 内容

triage と metacognition のテンプレート構造は完全に同型（マネージャー5ファイル + ワーカー7ファイル）。差異は MC/TG タスク固有のセクション見出しのみ。将来的にテンプレート生成の共通化が可能。

## 提案

- 共通テンプレートを `sessions/_shared_template/` に配置し、各セッションタイプ固有の差異のみをオーバーライドする仕組みを検討する
- ただし、現時点では2セッションタイプのみのため、コスト対効果を考慮し次のセッションタイプ追加時に再検討する
