#!/usr/bin/env bash
# SessionStart hook: ブランチ整理自動化
# セッション開始時に前セッションの未プッシュコミットやPR未作成の状態を整理する。
# 出力: JSON 形式で結果を stdout に出力する。
# 保証: 全パスで exit 0 を返す（hook がセッション開始をブロックしない）。
#
# 参照: .claude/rules/session-start-branch-cleanup.md（設計仕様リファレンス）

set -euo pipefail

# --- ヘルパー関数 ---

# JSON エスケープ（ダブルクォート・バックスラッシュ・改行）
json_escape() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  printf '%s' "$s"
}

# 結果 JSON を組み立てて stdout に出力し、exit 0 で終了する
output_result() {
  local branch="$1"
  local action="$2"
  local pr_url="$3"
  local warnings_json="$4"
  local errors_json="$5"

  cat <<ENDJSON
{
  "branch": "$(json_escape "$branch")",
  "action": "$(json_escape "$action")",
  "pr_url": "$(json_escape "$pr_url")",
  "warnings": $warnings_json,
  "errors": $errors_json
}
ENDJSON
  exit 0
}

# --- メイン処理 ---

warnings="[]"
errors="[]"

# ステップ 1: 現在ブランチの確認
current_branch=$(git branch --show-current 2>/dev/null || true)

if [ -z "$current_branch" ]; then
  errors='["git branch --show-current failed: detached HEAD or not a git repository"]'
  output_result "" "error" "" "$warnings" "$errors"
fi

# main ブランチの場合: git pull のみ
if [ "$current_branch" = "main" ]; then
  pull_output=$(git pull 2>&1) || {
    errors="[\"git pull failed: $(json_escape "$pull_output")\"]"
    output_result "main" "pull_failed" "" "$warnings" "$errors"
  }
  output_result "main" "pull_only" "" "$warnings" "$errors"
fi

# --- main 以外のブランチ ---

pr_url=""

# ステップ 2: 未プッシュコミットの確認
needs_push=false
unpushed_output=$(git log "origin/${current_branch}..HEAD" --oneline 2>/dev/null) || {
  # リモートブランチが存在しない場合 → 初回プッシュが必要
  needs_push=true
}

if [ "$needs_push" = false ] && [ -n "$unpushed_output" ]; then
  needs_push=true
fi

# ステップ 3: 未プッシュコミットのプッシュ
if [ "$needs_push" = true ]; then
  push_output=$(git push -u origin "$current_branch" 2>&1) || {
    errors="[\"git push failed: $(json_escape "$push_output")\"]"
    output_result "$current_branch" "push_failed" "" "$warnings" "$errors"
  }
fi

# ステップ 4: PR の確認・作成
if command -v gh >/dev/null 2>&1; then
  # gh が利用可能 → PR 確認
  existing_pr=$(gh pr list --head "$current_branch" --base main --state open --json url --jq '.[0].url' 2>/dev/null || true)

  if [ -n "$existing_pr" ]; then
    pr_url="$existing_pr"
  else
    # PR が存在しない → 作成
    pr_create_output=$(gh pr create \
      --base main \
      --head "$current_branch" \
      --title "$current_branch" \
      --body "前セッションからの継続作業。セッション開始時のブランチ整理で自動作成。" 2>&1) || {
      warnings="[\"gh pr create failed: $(json_escape "$pr_create_output")\"]"
    }

    if [ -z "$pr_url" ]; then
      # pr_create_output から URL を抽出
      pr_url=$(echo "$pr_create_output" | grep -oE 'https://github\.com/[^ ]+' | head -1 || true)
    fi
  fi
else
  warnings='["gh command not found: PR step skipped"]'
fi

# ステップ 5: main ブランチへの切り替え・最新化
checkout_output=$(git checkout main 2>&1) || {
  errors="[\"git checkout main failed: $(json_escape "$checkout_output")\"]"
  output_result "$current_branch" "checkout_failed" "$pr_url" "$warnings" "$errors"
}

pull_output=$(git pull 2>&1) || {
  errors="[\"git pull failed after checkout: $(json_escape "$pull_output")\"]"
  output_result "$current_branch" "pull_failed_after_checkout" "$pr_url" "$warnings" "$errors"
}

# ステップ 6: 完了
output_result "$current_branch" "cleanup_complete" "$pr_url" "$warnings" "$errors"
