# GHA ワークフロー execution_file 修正の横展開

## 概要

`initiative-wallbash.yml` で実施した `claude-code-action` の出力取得修正を、他の3ワークフローにも横展開する。

## 背景

- `claude-code-action@v1` には `result` output が存在しない
- `steps.claude.outputs.result` を参照している箇所は常に空になる
- wallbash では `${{ runner.temp }}/claude-execution-output.json` から jq で抽出する方式に修正済み

## 対象ファイル

- `.github/workflows/initiative-execute.yml` — `CLAUDE_RESULT: ${{ steps.claude.outputs.result }}` を使用中
- `.github/workflows/initiative-close.yml` — 同上
- `.github/workflows/initiative-question.yml` — 同上

## 対応内容

各ワークフローで以下を実施:
1. `steps.claude.outputs.result` → `${{ runner.temp }}/claude-execution-output.json` からの jq 抽出に変更
2. サマリー抽出失敗時のフォールバックメッセージを追加

## 優先度

wallbash の再実行で動作確認した後に対応する（壁打ちが動かないと後続ワークフローもテストできないため）。

---
**起票日**: 2026-03-15
**関連施策**: initiative-metadata-comment
