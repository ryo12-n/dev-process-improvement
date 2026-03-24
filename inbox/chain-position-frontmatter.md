# フロントマターに chain-position メタデータ追加の検討

## 背景

ai-dev-chain-bootstrap 施策で 6 Skills の骨格を作成した際、各 Skill のチェーン内の位置づけ（何番目の Skill か、前工程・後工程は何か）を SKILL.md 本文に記載した。

## 提案

チェーン内の位置をフロントマターのメタデータ（例: `chain-position: 2`, `chain-prev: gen-req`, `chain-next: gen-tests`）として表現すると、チェーン全体の可視性が向上し、ツールによる自動検証も可能になる。

## 発見元

- 施策: ai-dev-chain-bootstrap
- 発見者: L2-worker (set-2)
- 日付: 2026-03-24
