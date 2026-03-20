# initiative 実テンプレートの 2-phase 構造移行

## 凡例

| 項目 | 記法 | 説明 |
|------|------|------|
| **優先度** | 🔴 高 | 早期対応が必要。ブロッカーまたは高頻度問題 |
| | 🟡 中 | 重要だが緊急ではない |
| | 🔵 低 | 余裕があれば対応 |
| **ステータス** | 候補 | トリアージ承認済み・未着手 |
| | initiative 開始済 | `sessions/initiatives/` で施策進行中 |
| | 完了 | 施策クローズ済み |

## メタ情報

| 項目 | 内容 |
|------|------|
| **バックログ ID** | BL-118 |
| **優先度** | 🟡 中 |
| **ステータス** | 候補 |
| **対象リポジトリ** | dev-process-improvement |
| **施策ディレクトリ名** | |
| **起票日** | 2026-03-20 |
| **起票元** | template-structure-unification 施策（横展開事項 #1） |
| **依存する環境前提** | なし |

## 課題・背景

template-structure-unification 施策でポリシー・スキル定義は新テンプレート構造（2-phase + set コピー方式）に更新済みだが、実テンプレートファイル（`sessions/initiatives/_template/`）は旧構造のまま残存している。

現状の不整合:
- `session-lifecycle-policy` §1.4.3 に新構造（`phase-1-planning/_template/` + `phase-2-execution/_template/`）が定義済み
- ポリシーに「移行中」注記が付与されている
- L1 マネージャーが initiative を開始する際、旧テンプレートをコピーした後に手動で 2-phase 構造に変換する必要がある

## 提案内容

1. `sessions/initiatives/_template/` のディレクトリ構造を 2-phase 構造に改修する
   - マネージャールートファイル 7 件（`00_proposal.md` 〜 `06_cost_record.md`）
   - `phase-1-planning/_template/`（計画ワーカーセット 7 ファイル）
   - `phase-2-execution/_template/`（実施ワーカーセット 7 ファイル）
2. `session-lifecycle-policy` §1.4.3 の「移行中」注記を解除する
3. 関連ファイル（`l1-manager/SKILL.md` のテンプレートコピー手順等）が実テンプレートと整合していることを確認する

## 期待効果

- L1 マネージャーの initiative 開始時の手動変換が不要になる
- ポリシーと実テンプレートの完全一致により、新規セッション参加者の混乱を防止する
