#!/bin/bash
# PreToolUse hook: git commit 実行前に CSV を自動再生成
#
# PreToolUse の Bash matcher で呼ばれるため、
# $TOOL_INPUT から command を取得し、git commit かどうかを判定する。
# git commit の場合のみ CSV を再生成してステージングする。

# stdin から JSON を読む
INPUT=$(cat)

# command フィールドを抽出（jq がなければ grep で代替）
if command -v jq &>/dev/null; then
    COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
else
    COMMAND=$(echo "$INPUT" | grep -oP '"command"\s*:\s*"[^"]*"' | head -1 | sed 's/.*: *"//;s/"$//')
fi

# git commit コマンドでない場合は何もしない
if [[ ! "$COMMAND" =~ ^git\ commit ]]; then
    exit 0
fi

# CSV を再生成
SCRIPT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
python3 "$SCRIPT_DIR/scripts/generate-csvs.py" 2>/dev/null

# 再生成した CSV をステージングに追加
git add "$SCRIPT_DIR/プロセス改善_課題管理.csv" "$SCRIPT_DIR/backlog/backlog.csv" 2>/dev/null

exit 0
