# バッチ施策計画に「既存充足確認フェーズ」を追加

## 背景
batch-template-doc-fixes 施策で、BL-054（docs/workflow.md への GHA Initiative 記述追加）が他施策（gha-initiative-skills-separation）で事前解決済みだった。バッチ着手前の現状確認で早期にスキップでき、作業効率が向上した。

## 提案
- バッチ施策の計画段階で「既存充足確認フェーズ」を明示的に設ける
- 各バックログエントリの対象ファイルを事前確認し、既に解決済みのエントリを計画から除外するパターンをガイドライン化
- L1 マネージャーの壁打ちフェーズまたは plan-worker 指示に組み込む

## 発見元
- 施策: batch-template-doc-fixes
- ソース: L2-worker 参考情報 #2、L2-evaluator ルール化候補 #1

---
**起票日**: 2026-03-25
